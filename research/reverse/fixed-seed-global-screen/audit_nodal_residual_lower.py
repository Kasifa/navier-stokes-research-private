#!/usr/bin/env python3
"""One fixed-node, top-24 residual lower-bound trial. No integration.

Only --run computes. Selection uses a labelled floating FFT; the final
inequality uses authenticated Q52 inputs and Python arbitrary-size integers.
"""
from __future__ import annotations

import argparse
import datetime as dt
from fractions import Fraction
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import platform
import resource
import signal
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
DATA = HERE / "node-trial-01"
OUT = HERE / "nodal-residual-trial-01"
Q = 1 << 52
EXPECTED = {
    "node-trial-01/manifest.json": "5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd",
    "node-trial-01/modes.npy": "f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896",
    "node-trial-01/block-01280-01343.npz": "abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e",
    "C1_RESIDUAL_CONTRACT.md": "a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251",
    "RESIDUAL_COST_PREFLIGHT.md": "dfc54d9be18ca0d47a5c4ea13433523327ff9f0f85691d512bdbcfeed646be4e",
}
NODE_CONFIG_SHA = "7649e366ee0fba6c5a051f0eecb45fc387a8bf91bc4bd06befa7e444e409f047"
CONFIG = {
    "node": 1280, "time_numerator": 1280, "time_denominator": 2048,
    "cutoff": 8, "G_count": 4912, "quantization_denominator": Q,
    "selection_fft_grid": 35, "candidate_coordinate_bound": 16,
    "candidate_count": 35936, "selected_count": 24,
    "selection_sort": "descending binary64 squared H2 contribution; exact floating ties use lexicographic signed k",
    "conjugacy_selection": "full signed modes; no conjugate closure or factor two",
    "P32_argument": [5, 2], "P32_degree": 32,
    "old_epsilon": [1, 10000000], "integer_bit_limit": 8192,
    "wall_seconds": 60, "peak_rss_bytes": 256 * 1024**2,
    "output_bytes": 8 * 1024**2, "metadata_reserve_bytes": 256 * 1024,
    "pair_limit": 24 * 4912, "parameter_scan": False, "retry": False,
}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for part in iter(lambda: stream.read(1 << 20), b""):
            h.update(part)
    return h.hexdigest()


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def rational(value):
    f = Fraction(value)
    return {"numerator": str(f.numerator), "denominator": str(f.denominator)}


def bit_guard(*values):
    if any(abs(x).bit_length() > CONFIG["integer_bit_limit"] for x in values):
        raise RuntimeError("fixed integer bit budget exceeded")


class BudgetStop(RuntimeError):
    pass


class BoundedFile:
    def __init__(self, raw, limit, check):
        self.raw, self.limit, self.check = raw, limit, check

    def write(self, data):
        self.check()
        if self.raw.tell() + len(data) > self.limit:
            raise BudgetStop("fixed output byte budget exhausted")
        return self.raw.write(data)

    def __getattr__(self, name):
        return getattr(self.raw, name)


class Trial:
    def __init__(self):
        self.started = time.perf_counter()
        self.last_progress = self.started
        self.files = {}
        self.log = {"schema": "reverse-nodal-residual-lower-v1", "status": "RUNNING",
                    "started_at_utc": utc(), "pid": os.getpid(), "config": CONFIG,
                    "config_sha256": hashlib.sha256(canonical(CONFIG)).hexdigest(),
                    "sources": {}, "files": self.files, "progress": [],
                    "scope": "FIXED_Q52_REFERENCE_NODAL_RESIDUAL_ONLY_NOT_NS_ERROR_OR_BLOWUP"}

    def observation(self):
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rss = int(rss if sys.platform == "darwin" else rss * 1024)
        size = sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
        obs = {"wall_seconds": time.perf_counter() - self.started,
               "peak_rss_bytes": rss, "output_bytes_including_partial": size}
        obs["violations"] = [name for name, flag in (
            ("wall", obs["wall_seconds"] >= CONFIG["wall_seconds"]),
            ("peak_rss", rss > CONFIG["peak_rss_bytes"]),
            ("output_bytes", size > CONFIG["output_bytes"])) if flag]
        return obs

    def check(self):
        obs = self.observation()
        if obs["violations"]:
            raise BudgetStop("observed budget exceeded: " + ",".join(obs["violations"]))

    def progress(self, stage, force=False):
        self.check()
        now = time.perf_counter()
        if force or now - self.last_progress >= 10:
            item = {"stage": stage, **self.observation()}
            self.log["progress"].append(item)
            self.last_progress = now
            print(json.dumps({"nodal_residual_progress": item}, sort_keys=True), flush=True)

    def write(self, name, callback, metadata=False):
        if Path(name).name != name:
            raise ValueError("output name must be a basename")
        final, temporary = OUT / name, OUT / (name + ".partial")
        if not metadata and final.exists():
            raise FileExistsError(final)
        if temporary.exists():
            raise FileExistsError(temporary)
        cap = CONFIG["output_bytes"] - (0 if metadata else CONFIG["metadata_reserve_bytes"])
        occupied = sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())
        limit = cap - occupied
        check = (lambda: None) if metadata else self.check
        with temporary.open("xb") as raw:
            callback(BoundedFile(raw, limit, check))
            raw.flush()
            os.fsync(raw.fileno())
        temporary.replace(final)
        if not metadata:
            self.files[name] = {"bytes": final.stat().st_size, "sha256": sha(final)}
        return final

    def json(self, name, value, metadata=False):
        content = canonical(value) + b"\n"
        return self.write(name, lambda stream: stream.write(content), metadata)


def array_description(array):
    return {"shape": list(array.shape), "dtype": array.dtype.str, "nbytes": array.nbytes,
            "data_sha256": hashlib.sha256(memoryview(array).cast("B")).hexdigest()}


def authenticated_node(np, trial):
    for name, expected in EXPECTED.items():
        path = HERE / name
        actual = sha(path)
        if actual != expected:
            raise ValueError("fixed input hash mismatch: " + name)
        trial.log["sources"][name] = actual
        trial.check()
    for path in (Path(__file__).resolve(), HERE / "NODAL_RESIDUAL_LOWER_CONTRACT.md"):
        trial.log["sources"][path.name] = sha(path)
    manifest = json.loads((DATA / "manifest.json").read_text())
    assert manifest["schema"] == "reverse-fixed-seed-nodes-v1"
    assert manifest["status"] == "CANDIDATE_NODES_COMPLETE_NOT_NS_CERTIFIED"
    assert (manifest["stored_nodes"], manifest["completed_steps"]) == (5121, 5120)
    assert hashlib.sha256(canonical(manifest["config"])).hexdigest() == NODE_CONFIG_SHA == manifest["config_sha256"]
    cfg = manifest["config"]
    assert cfg["scale"] == cfg["rho"] == cfg["viscosity"] == 1
    assert cfg["cutoff"] == 8 and cfg["time_denominator"] == 2048 and cfg["quantization_denominator"] == Q
    modes_array = np.load(DATA / "modes.npy", allow_pickle=False)
    assert modes_array.shape == (4912, 3) and modes_array.dtype.str == "<i8"
    assert hashlib.sha256(modes_array.tobytes(order="C")).hexdigest() == manifest["modes"]["array_sha256"]
    modes = [tuple(map(int, k)) for k in modes_array.tolist()]
    assert modes == [k for k in itertools.product(range(-8, 9), repeat=3) if k != (0, 0, 0)]
    entries = [e for e in manifest["blocks"] if e["first_node"] <= 1280 <= e["last_node"]]
    assert len(entries) == 1
    entry = entries[0]
    assert (entry["first_node"], entry["last_node"], entry["node_count"]) == (1280, 1343, 64)
    assert entry["file"] == "block-01280-01343.npz"
    assert entry["file_sha256"] == EXPECTED["node-trial-01/" + entry["file"]]
    assert (DATA / entry["file"]).stat().st_size == entry["file_bytes"]
    expected_names = {"node_index", "time_numerator", "time_denominator", "quantization_denominator", "value_q52", "slope_q52"}
    rows = {}
    with np.load(DATA / entry["file"], allow_pickle=False) as archive:
        assert set(archive.files) == expected_names == set(entry["arrays"])
        for name in sorted(expected_names):
            array = archive[name]
            assert array_description(array) == entry["arrays"][name]
            assert array.dtype.str == "<i8"
            if name in ("node_index", "time_numerator"):
                assert array.tolist() == list(range(1280, 1344))
            elif name in ("time_denominator", "quantization_denominator"):
                assert array.tolist() == [2048 if name == "time_denominator" else Q]
            else:
                assert array.shape == (64, 4912, 3, 2)
                rows[name] = array[0].tolist()
            del array
            trial.check()
    trial.log["input_authentication"] = {"node": 1280, "row": 0, "block": entry["file"],
                                           "arrays": entry["arrays"], "status": "EXACT_BYTES_AND_SCHEMA_MATCH"}
    return modes, rows["value_q52"], rows["slope_q52"]


def decode(raw, modes, index, L, trial):
    result = []
    for i, p in enumerate(modes):
        other = index[tuple(-x for x in p)]
        re, im = [], []
        for a in range(3):
            z, w = [int(x) for x in raw[i][a]], [int(x) for x in raw[other][a]]
            assert all(-(1 << 63) < x < (1 << 63) for x in z + w)
            re.append(z[0] + w[0])
            im.append(z[1] - w[1])
        s = sum(x*x for x in p)
        kr, ki = sum(p[a]*re[a] for a in range(3)), sum(p[a]*im[a] for a in range(3))
        U = tuple((L//s)*(s*re[a]-p[a]*kr) for a in range(3))
        V = tuple((L//s)*(s*im[a]-p[a]*ki) for a in range(3))
        bit_guard(*U, *V)
        assert sum(p[a]*U[a] for a in range(3)) == sum(p[a]*V[a] for a in range(3)) == 0
        result.append((U, V))
        if i % 128 == 0:
            trial.check()
    for i, p in enumerate(modes):
        U, V = result[index[tuple(-x for x in p)]]
        assert U == result[i][0] and V == tuple(-x for x in result[i][1])
    return result


def select_modes(np, modes, values, slopes, D, trial):
    size = 35
    addresses = tuple((np.asarray(modes, dtype="<i8") % size).T)
    def embedded(coeff):
        v = np.asarray([[complex(U[a]/D, V[a]/D) for a in range(3)] for U, V in coeff], dtype=np.complex128)
        grid = np.zeros((3, size, size, size), dtype=np.complex128)
        grid[(slice(None),) + addresses] = v.T
        return grid
    c, d = embedded(values), embedded(slopes)
    f = np.arange(size)
    f = np.where(f <= size//2, f, f-size)
    ks = (f[:, None, None], f[None, :, None], f[None, None, :])
    kx, ky, kz = ks
    s = kx*kx + ky*ky + kz*kz
    curl = np.empty_like(c)
    curl[0], curl[1], curl[2] = 1j*(ky*c[2]-kz*c[1]), 1j*(kz*c[0]-kx*c[2]), 1j*(kx*c[1]-ky*c[0])
    v = np.fft.ifftn(size**3*c, axes=(-3, -2, -1))
    omega = np.fft.ifftn(size**3*curl, axes=(-3, -2, -1))
    cross = np.empty_like(c)
    cross[0], cross[1], cross[2] = v[1]*omega[2]-v[2]*omega[1], v[2]*omega[0]-v[0]*omega[2], v[0]*omega[1]-v[1]*omega[0]
    quadratic = np.fft.fftn(cross, axes=(-3, -2, -1))/size**3
    inverse = np.zeros_like(s, dtype=float)
    np.divide(1.0, s, out=inverse, where=s > 0)
    dot = kx*quadratic[0] + ky*quadratic[1] + kz*quadratic[2]
    for a in range(3):
        quadratic[a] -= ks[a]*dot*inverse
    quadratic[:, 0, 0, 0] = 0
    R = d+s[None, ...]*c-quadratic
    assert np.all(np.isfinite(R))
    trial.check()
    candidates = [k for k in itertools.product(range(-16, 17), repeat=3) if k != (0, 0, 0)]
    assert len(candidates) == CONFIG["candidate_count"]
    candidate_array = np.asarray(candidates, dtype="<i2")
    score_grid = s*s*np.sum(np.abs(R)**2, axis=0)
    scores = np.asarray(score_grid[tuple((candidate_array % size).T)], dtype="<f8")
    assert np.all(np.isfinite(scores)) and np.all(scores >= 0)
    rank = sorted(range(len(candidates)), key=lambda i: (-float(scores[i]), candidates[i]))
    selected = [candidates[i] for i in rank[:24]]
    for name, array in (("selection-full-R35.npy", R), ("selection-candidates.npy", candidate_array),
                        ("selection-scores.npy", scores), ("selection-ranking.npy", np.asarray(rank, dtype="<i4"))):
        trial.write(name, lambda stream, array=array: np.save(stream, array, allow_pickle=False))
        trial.files[name]["array"] = array_description(array)
    selection = {"status": "FIXED_FLOAT_SELECTION_NOT_CERTIFICATE", "node": 1280,
                 "config_sha256": trial.log["config_sha256"], "input_manifest_sha256": EXPECTED["node-trial-01/manifest.json"],
                 "coefficient_rounding": "Python int true division by common D, then binary64 complex; exact numerator ratios define the reference",
                 "normalization": "Fourier series coefficients; inverse FFT multiplied by 35^3; forward divided by 35^3",
                 "candidate_order": "lexicographic [-16,16]^3 excluding zero; +/-17 roundoff excluded from selection",
                 "score": "|k|^4 sum_components abs(full_unmasked_R_k)^2", "sort": CONFIG["selection_sort"],
                 "selected_modes": [list(k) for k in selected],
                 "selected_score_hex": [float(scores[i]).hex() for i in rank[:24]],
                 "selection_files": {name: dict(trial.files[name]) for name in trial.files if name.startswith("selection-")}}
    trial.json("selection.json", selection)
    trial.progress("selection-frozen-before-exact-convolution", True)
    return selected


def exact_outputs(selected, modes, index, values, slopes, D, trial):
    records, N, visits = [], 0, 0
    zero = ((0, 0, 0), (0, 0, 0))
    for number, k in enumerate(selected):
        Fr, Fi, count = [0]*3, [0]*3, 0
        pair_digest = hashlib.sha256()
        for i, p in enumerate(modes):
            visits += 1
            q = tuple(k[a]-p[a] for a in range(3))
            qi = index.get(q)
            if qi is not None:
                U, V = values[i]
                X, Y = values[qi]
                alpha, beta = sum(U[a]*q[a] for a in range(3)), sum(V[a]*q[a] for a in range(3))
                for a in range(3):
                    Fr[a] += alpha*X[a]-beta*Y[a]
                    Fi[a] += alpha*Y[a]+beta*X[a]
                count += 1
                pair_digest.update((",".join(map(str, p))+";"+",".join(map(str, q))+"\n").encode())
            if i % 128 == 0:
                trial.check()
        s = sum(x*x for x in k)
        Ar, Ai = values[index[k]] if k in index else zero
        Jr, Ji = slopes[index[k]] if k in index else zero
        kr, ki = sum(k[a]*Fr[a] for a in range(3)), sum(k[a]*Fi[a] for a in range(3))
        Tr = [D*s*(Jr[a]+s*Ar[a])-(s*Fi[a]-k[a]*ki) for a in range(3)]
        Ti = [D*s*(Ji[a]+s*Ai[a])+(s*Fr[a]-k[a]*kr) for a in range(3)]
        bit_guard(*Fr, *Fi, *Tr, *Ti)
        assert sum(k[a]*Tr[a] for a in range(3)) == sum(k[a]*Ti[a] for a in range(3)) == 0
        contribution = sum(x*x for x in Tr+Ti)
        N += contribution
        bit_guard(N)
        records.append({"k": list(k), "squared_frequency": s, "ordered_pair_count": count,
                        "ordered_pair_sequence_sha256": pair_digest.hexdigest(),
                        "F_real": list(map(str, Fr)), "F_imag": list(map(str, Fi)),
                        "T_real": list(map(str, Tr)), "T_imag": list(map(str, Ti)),
                        "squared_H2_contribution_numerator_over_D4": str(contribution)})
        trial.progress("exact-output-"+str(number+1)+"-of-24", True)
    assert len(selected) == len(set(selected)) == len(records) == 24
    assert visits == CONFIG["pair_limit"]
    term = total = Fraction(1)
    for j in range(1, 33):
        term *= Fraction(5, 2*j)
        total += term
    D4 = D**4
    left, right = 10**14*N*total.numerator, D4*total.denominator
    bit_guard(D4, total.numerator, total.denominator, left, right, left-right)
    return {"status": "OLD_REFERENCE_R2_ENVELOPE_REFUTED" if left > right else "LOWER_BOUND_INCONCLUSIVE",
            "acceptance": "PROVISIONAL_UNTIL_RUN_LOG_COMPLETE_AND_INDEPENDENT_REVIEW",
            "scope": "THIS_FIXED_Q52_C1_REFERENCE_NODAL_RESIDUAL_ONLY_NOT_TRUE_NS_OR_ERROR_LOWER_BOUND",
            "node": 1280, "time": rational(Fraction(5, 8)), "selected_modes": [list(k) for k in selected],
            "p_visits": visits, "D": str(D), "N": str(N), "D4": str(D4),
            "r2_squared_lower": rational(Fraction(N, D4)), "P32_argument": rational(Fraction(5, 2)),
            "P32": rational(total), "necessary_epsilon_squared_lower": rational(Fraction(N, D4)*total),
            "old_epsilon": rational(Fraction(1, 10**7)), "integer_left": str(left),
            "integer_right": str(right), "integer_margin": str(left-right), "outputs": records}


def run():
    if sys.version_info < (3, 10) or sys.flags.optimize:
        raise RuntimeError("Python >=3.10 without -O is required; assertions must remain enabled")
    # An existing directory, including a partial one, consumes this one trial.
    OUT.mkdir(exist_ok=False)
    trial = Trial()
    def stop(signum, frame):
        raise BudgetStop("deadline or interruption signal " + str(signum))
    try:
        signal.signal(signal.SIGALRM, stop)
        signal.signal(signal.SIGINT, stop)
        signal.signal(signal.SIGTERM, stop)
        signal.setitimer(signal.ITIMER_REAL, CONFIG["wall_seconds"])
        trial.json("run.json", trial.log, metadata=True)
        import numpy as np
        cpu_name, cpu_query_error = platform.processor(), None
        if sys.platform == "darwin":
            try:
                cpu_name = subprocess.check_output(
                    ["/usr/sbin/sysctl", "-n", "machdep.cpu.brand_string"],
                    text=True, timeout=1, stderr=subprocess.PIPE).strip()
            except (OSError, subprocess.SubprocessError) as exc:
                cpu_query_error = {"type": type(exc).__name__, "message": str(exc)}
        thread_keys = ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                       "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS",
                       "OMP_DYNAMIC", "MKL_DYNAMIC"]
        trial.log["environment"] = {"python": sys.version, "executable": sys.executable,
                                    "argv": list(getattr(sys, "orig_argv", [sys.executable, *sys.argv])),
                                    "numpy": np.__version__, "numpy_path": np.__file__,
                                    "platform": platform.platform(), "machine": platform.machine(),
                                    "cpu_model": cpu_name, "logical_cpu_count": os.cpu_count(),
                                    "cpu_query_error": cpu_query_error, "optimized": sys.flags.optimize,
                                    "single_scientific_python_process": True,
                                    "process_note": "No parallel scientific process; sysctl is a read-only metadata query.",
                                    "thread_environment": {k: os.environ.get(k) for k in thread_keys},
                                    "fft_worker_count": "UNKNOWN; no thread setting changed or worker count inferred from environment"}
        modes, raw_value, raw_slope = authenticated_node(np, trial)
        index = {k: i for i, k in enumerate(modes)}
        L = math.lcm(*(sum(x*x for x in k) for k in modes))
        D = 2*Q*L
        bit_guard(L, D)
        values = decode(raw_value, modes, index, L, trial)
        slopes = decode(raw_slope, modes, index, L, trial)
        del raw_value, raw_slope
        trial.log["exact_decode"] = {"L": str(L), "D": str(D), "value_and_slope_constraints": "PASS"}
        selected = select_modes(np, modes, values, slopes, D, trial)
        frozen_selection_sha = trial.files["selection.json"]["sha256"]
        result = exact_outputs(selected, modes, index, values, slopes, D, trial)
        result["L"] = str(L)
        result["selection_sha256"] = frozen_selection_sha
        result["source_bindings"] = dict(trial.log["sources"])
        trial.json("exact-result.json", result)
        for name, record in trial.files.items():
            assert (OUT/name).stat().st_size == record["bytes"] and sha(OUT/name) == record["sha256"]
            if name.endswith(".npy"):
                decoded_array = np.load(OUT/name, allow_pickle=False)
                assert array_description(decoded_array) == record["array"]
                del decoded_array
            elif name.endswith(".json"):
                decoded_json = json.loads((OUT/name).read_text())
                if name == "exact-result.json":
                    assert decoded_json == result
                elif name == "selection.json":
                    assert decoded_json["selected_modes"] == [list(k) for k in selected]
                    assert decoded_json["config_sha256"] == trial.log["config_sha256"]
                del decoded_json
            trial.check()
        assert sha(OUT/"selection.json") == frozen_selection_sha
        for name, expected in trial.log["sources"].items():
            assert sha(HERE/name) == expected, ("input/source changed", name)
            trial.check()
        trial.log["mathematical_verdict"] = result["status"]
        trial.log["status"] = "DATA_CHECKS_COMPLETE_FINALIZING"
    except BaseException as exc:
        trial.log["status"] = "BUDGET_STOP" if isinstance(exc, BudgetStop) else "FAILED"
        trial.log["error"] = {"type": type(exc).__name__, "message": str(exc)}
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        trial.log["finished_at_utc"] = utc()
        before = trial.observation()
        trial.log["final_budget_observation"] = before
        if before["violations"]:
            trial.log["status"] = "BUDGET_STOP"
        elif trial.log["status"] == "DATA_CHECKS_COMPLETE_FINALIZING":
            trial.log["status"] = "COMPLETE_FIXED_NODE_LOWER_TRIAL"
        trial.json("run.json", trial.log, metadata=True)
        run_sha = sha(OUT/"run.json")
        after = trial.observation()
        if after["violations"] and trial.log["status"] == "COMPLETE_FIXED_NODE_LOWER_TRIAL":
            trial.log["status"] = "BUDGET_STOP"
            trial.log["final_budget_observation"] = after
            trial.json("run.json", trial.log, metadata=True)
            run_sha = sha(OUT/"run.json")
    print(json.dumps({"status": trial.log["status"], "run_log": str(OUT/"run.json"),
                      "run_log_sha256": run_sha, "post_write_budget_observation": after,
                      "mathematical_verdict": trial.log.get("mathematical_verdict")}, sort_keys=True), flush=True)
    return 0 if trial.log["status"] == "COMPLETE_FIXED_NODE_LOWER_TRIAL" else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--run", action="store_true")
    mode.add_argument("--describe", action="store_true")
    args = parser.parse_args()
    if not args.run:
        print(json.dumps({"computation_started": False, "config": CONFIG}, indent=2, sort_keys=True))
        return 0
    return run()


if __name__ == "__main__":
    raise SystemExit(main())
