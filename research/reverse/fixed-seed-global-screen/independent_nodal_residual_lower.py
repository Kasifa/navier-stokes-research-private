#!/usr/bin/env python3
"""Independent, one-node Fraction residual audit. No integration or selection.

Frozen primary selection/run bindings must be supplied before --run is allowed.
Default and --check-only never decode nodes or perform the convolution.
"""
from __future__ import annotations

import argparse
import ast
import datetime as dt
from fractions import Fraction as F
import hashlib
import itertools
import json
import os
from pathlib import Path
import platform
import resource
import shlex
import signal
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
OUT = HERE / "nodal-residual-independent-trial-01"
OWN_CONTRACT = HERE / "INDEPENDENT_NODAL_RESIDUAL_CONTRACT.md"
PRIMARY_CONTRACT = HERE / "NODAL_RESIDUAL_LOWER_CONTRACT.md"
C1_CONTRACT = HERE / "C1_RESIDUAL_CONTRACT.md"
PINNED_ARCHIVE = {
    "node-trial-01/manifest.json": "5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd",
    "node-trial-01/modes.npy": "f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896",
    "node-trial-01/block-01280-01343.npz": "abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e",
}
# Root supplies these exact bindings once; no fallback, mode search or retry.
LOCKED = {
    "selection_file": "nodal-residual-trial-01/selection.json",
    "selection_sha256": "62c066774e2e6d6c6ab20e6d9b4f92b5599c9acda7bf64420a819997ec5f3d69",
    "selection_key_path": ["selected_modes"],
    "selected_modes": [
        [9, -4, 4], [-9, 4, -4], [4, -9, 4], [4, -4, 9],
        [-4, -9, -4], [-4, 4, 9], [-4, 9, -4], [4, 9, 4],
        [4, 4, -9], [-4, 9, 4], [9, 4, 4], [-4, 4, -9],
        [-4, -4, -9], [4, 4, 9], [4, -4, -9], [4, 9, -4],
        [4, -9, -4], [9, -4, -4], [-9, 4, 4], [9, 4, -4],
        [-9, -4, -4], [-4, -9, 4], [-4, -4, 9], [-9, -4, 4],
    ],
    "primary_run_file": "nodal-residual-trial-01/run.json",
    "primary_run_sha256": "1c86e99028c1d279c2beddd7f932462112814720ebc71ffb5f737256079411be",
}
CONFIG = {
    "node_index": 1280, "time_numerator": 1280, "time_denominator": 2048,
    "quantization_denominator": 1 << 52, "input_cutoff": 8,
    "maximum_output_modes": 24, "output_cutoff": 16,
    "wall_budget_seconds": 120, "peak_rss_budget_bytes": 256 * 1024**2,
    "output_budget_bytes": 8 * 1024**2, "metadata_reserve_bytes": 256 * 1024,
    "maximum_integer_bits": 8192, "P_degree": 32, "P_argument": [5, 2],
    "threshold_squared": [1, 10**14],
    "algorithm": "per-mode Fraction conjugate average and P; unordered p<q adds both distinct ordered terms, p=q once",
    "run_directory": str(OUT), "integration": False, "selection": False, "retry": False,
}
ZERO = (F(0), F(0))
ZERO_VECTOR = (ZERO, ZERO, ZERO)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def sha(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def launch():
    original = getattr(sys, "orig_argv", None)
    return {"command": shlex.join(original or [sys.executable, *sys.argv]),
            "command_source": "sys.orig_argv" if original is not None else "reconstructed; interpreter flags unavailable",
            "python": sys.version, "executable": sys.executable}


def modes():
    return list(k for k in itertools.product(range(-8, 9), repeat=3) if k != (0, 0, 0))


def cadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def cscale(a, scalar):
    return a[0] * scalar, a[1] * scalar


def cmul(a, b):
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]


def cdot(vector, wave):
    return sum((vector[j][0]*wave[j] for j in range(3)), F(0)), sum((vector[j][1]*wave[j] for j in range(3)), F(0))


def conjugate(vector):
    return tuple((x[0], -x[1]) for x in vector)


def project(vector, wave):
    k2 = sum(x*x for x in wave)
    if not k2:
        return vector
    dot = cdot(vector, wave)
    return tuple(cadd(vector[j], cscale(dot, F(-wave[j], k2))) for j in range(3))


def fraction_json(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def vector_json(vector):
    return [{"real": fraction_json(x[0]), "imag": fraction_json(x[1])} for x in vector]


def locked_ready():
    return all(value is not None for value in LOCKED.values())


def preflight(require_bindings=False):
    if sys.version_info < (3, 10):
        raise RuntimeError("Python >=3.10 required; use bundled Python 3.12")
    source = Path(__file__).read_bytes()
    compile(ast.parse(source), str(Path(__file__)), "exec")
    if require_bindings and not locked_ready():
        raise ValueError("frozen selection and primary-run SHA have not been supplied; execution refused before creating a directory")
    if locked_ready():
        selected = LOCKED["selected_modes"]
        if not 1 <= len(selected) <= 24 or len({tuple(k) for k in selected}) != len(selected):
            raise ValueError("invalid frozen mode count or duplicates")
        for k in selected:
            if len(k) != 3 or any(type(x) is not int for x in k) or not any(k) or max(map(abs, k)) > 16:
                raise ValueError("invalid frozen output mode")
        for key in ("selection_sha256", "primary_run_sha256"):
            if len(LOCKED[key]) != 64 or any(c not in "0123456789abcdef" for c in LOCKED[key]):
                raise ValueError("invalid frozen SHA")
    return {"status": "READY_FOR_REVIEW" if locked_ready() else "CORE_READY_AWAITING_FROZEN_SELECTION",
            "scientific_execution": False, "config": CONFIG, "locked": LOCKED,
            "config_sha256": hashlib.sha256(canonical({"config": CONFIG, "locked": LOCKED})).hexdigest(),
            "source_sha256": {str(p): sha(p) for p in [Path(__file__), OWN_CONTRACT, PRIMARY_CONTRACT, C1_CONTRACT]},
            "pinned_archive": PINNED_ARCHIVE, "output_directory_exists": OUT.exists()}


class BudgetStop(RuntimeError):
    pass


def rss():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def run(info):
    preflight(require_bindings=True)
    OUT.mkdir(exist_ok=True)
    if any(OUT.iterdir()):
        raise FileExistsError("independent trial directory is not empty; no overwrite/retry")
    with (OUT / "RUN_CLAIM.json").open("x") as stream:
        json.dump({"pid": os.getpid(), "launch": launch(), "started_at_utc": utc()}, stream)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    start = time.perf_counter()
    record = {"execution_status": "RUNNING", "mathematical_status": "NOT_COMPUTED",
              "started_at_utc": utc(), "launch": launch(), "inputs": info,
              "node": 1280, "mode_results": [], "maximum_integer_bits_observed": 0,
              "independent_agreement": "NOT_COMPARED_IN_THIS_PROGRAM",
              "scope": "same fixed rational reference only; not actual NS error or global regularity/singularity"}

    def output_bytes():
        return sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())

    def check():
        if time.perf_counter() - start >= 120:
            raise BudgetStop("120-second wall budget")
        if rss() > CONFIG["peak_rss_budget_bytes"]:
            raise BudgetStop("256-MiB observed peak RSS budget")
        if output_bytes() > CONFIG["output_budget_bytes"]:
            raise BudgetStop("8-MiB output budget")

    def atom_json(name, payload, metadata=False):
        data = canonical(payload) + b"\n"
        limit = CONFIG["output_budget_bytes"] - (0 if metadata else CONFIG["metadata_reserve_bytes"])
        # The temporary and previous checkpoint coexist until atomic replacement.
        if output_bytes() + len(data) > limit:
            raise BudgetStop("output cap while preserving metadata reserve")
        temporary = OUT / (name + ".tmp")
        with temporary.open("wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(OUT / name)

    def snapshot():
        return {"wall_seconds": time.perf_counter() - start,
                "peak_rss_bytes": rss(), "output_bytes": output_bytes()}

    def checkpoint(final=False):
        record["resources"] = snapshot()
        atom_json("run.json", record, metadata=final)

    def guard_fraction(value):
        bits = max(abs(value.numerator).bit_length(), value.denominator.bit_length())
        record["maximum_integer_bits_observed"] = max(record["maximum_integer_bits_observed"], bits)
        if bits > 8192:
            raise BudgetStop("8192-bit rational numerator/denominator limit")

    def guard_vector(vector):
        for part in vector:
            for value in part:
                guard_fraction(value)

    def interrupted(signum, frame):
        raise BudgetStop("deadline or external stop signal " + str(signum))

    for number in (signal.SIGALRM, signal.SIGINT, signal.SIGTERM):
        signal.signal(number, interrupted)
    signal.setitimer(signal.ITIMER_REAL, 120)
    try:
        checkpoint()
        sys.dont_write_bytecode = True
        import numpy as np
        cpu = platform.processor()
        if sys.platform == "darwin":
            cpu = subprocess.check_output(["/usr/sbin/sysctl", "-n", "machdep.cpu.brand_string"], text=True, timeout=1).strip()
        record["environment"] = {"python": sys.version, "numpy": np.__version__, "numpy_path": np.__file__,
                                 "platform": platform.platform(), "cpu": cpu, "logical_cpus": os.cpu_count(),
                                 "thread_environment": {k: os.environ.get(k) for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS")},
                                 "arithmetic": "Python int and fractions.Fraction; NumPy only authenticates/reads archived integer arrays"}
        check()
        verified = {}
        for name, expected in PINNED_ARCHIVE.items():
            actual = sha(HERE / name)
            if actual != expected:
                raise ValueError("original archive SHA mismatch: " + name)
            verified[name] = actual
            check()
        # Primary run bytes are hashed only, never parsed as mathematical input.
        for path_key, sha_key in (("selection_file", "selection_sha256"), ("primary_run_file", "primary_run_sha256")):
            actual = sha(HERE / LOCKED[path_key])
            if actual != LOCKED[sha_key]:
                raise ValueError("frozen selection/run SHA mismatch: " + path_key)
            verified[LOCKED[path_key]] = actual
        selection = json.loads((HERE / LOCKED["selection_file"]).read_text())
        for key in LOCKED["selection_key_path"]:
            selection = selection[key]
        if selection != LOCKED["selected_modes"]:
            raise ValueError("selection list differs from source-frozen modes")
        selected = [tuple(k) for k in selection]
        record["authenticated_file_sha256"] = verified
        manifest = json.loads((HERE / "node-trial-01/manifest.json").read_text())
        if manifest["status"] != "CANDIDATE_NODES_COMPLETE_NOT_NS_CERTIFIED":
            raise ValueError("original node archive did not complete")
        physical = {"scale": 1, "viscosity": 1, "rho": 1, "grid": 27, "cutoff": 8,
                    "time_denominator": 2048, "steps": 5120, "nodes": 5121,
                    "quantization_denominator": 1 << 52}
        if any(manifest["config"].get(key) != value for key, value in physical.items()):
            raise ValueError("original fixed physical/encoding configuration differs")
        expected_g = modes()
        g_array = np.load(HERE / "node-trial-01/modes.npy", allow_pickle=False)
        if g_array.dtype.str != "<i8" or g_array.shape != (4912, 3) or [tuple(int(x) for x in row) for row in g_array] != expected_g:
            raise ValueError("original complete signed G differs")
        if hashlib.sha256(memoryview(g_array).cast("B")).hexdigest() != manifest["modes"]["array_sha256"]:
            raise ValueError("modes array hash mismatch")
        entries = [b for b in manifest["blocks"] if b["first_node"] <= 1280 <= b["last_node"]]
        if len(entries) != 1 or entries[0]["file"] != "block-01280-01343.npz":
            raise ValueError("original unique node block mismatch")
        block = entries[0]
        raw = {}
        with np.load(HERE / "node-trial-01" / block["file"], allow_pickle=False) as arrays:
            expected_keys = {"node_index", "time_numerator", "time_denominator", "quantization_denominator", "value_q52", "slope_q52"}
            if set(arrays.files) != expected_keys or set(block["arrays"]) != expected_keys:
                raise ValueError("unexpected node archive array keys")
            for name in sorted(expected_keys):
                array = arrays[name]
                description = {"shape": list(array.shape), "dtype": array.dtype.str, "nbytes": array.nbytes,
                               "data_sha256": hashlib.sha256(memoryview(array).cast("B")).hexdigest()}
                if description != block["arrays"][name] or array.dtype.str != "<i8":
                    raise ValueError("original array authentication failed: " + name)
                if name in ("value_q52", "slope_q52"):
                    if array.shape != (64, 4912, 3, 2):
                        raise ValueError("unexpected full Q52 block shape")
                    raw[name] = array[0].copy()
                elif name in ("node_index", "time_numerator"):
                    if array.tolist() != list(range(1280, 1344)):
                        raise ValueError("node/time numerator sequence mismatch")
                elif array.tolist() != ([2048] if name == "time_denominator" else [1 << 52]):
                    raise ValueError("node time or quantization denominator mismatch")
                del array
                check()
        positions = {p: n for n, p in enumerate(expected_g)}

        def decode(encoded):
            result = {}
            for n, p in enumerate(expected_g):
                opposite = positions[tuple(-x for x in p)]
                averaged = []
                for j in range(3):
                    # Convert each scalar before conjugation/addition: no int64 arithmetic.
                    pr, pi = int(encoded[n, j, 0]), int(encoded[n, j, 1])
                    mr, mi = int(encoded[opposite, j, 0]), int(encoded[opposite, j, 1])
                    if max(abs(pr), abs(pi), abs(mr), abs(mi)) >= 1 << 63:
                        raise ValueError("raw integer outside the producer's strict signed bound")
                    averaged.append((F(pr + mr, 2 * (1 << 52)), F(pi - mi, 2 * (1 << 52))))
                result[p] = project(tuple(averaged), p)
                if cdot(result[p], p) != ZERO:
                    raise AssertionError("exact projected coefficient is not divergence-free")
                guard_vector(result[p])
                if n % 64 == 0:
                    check()
            for p in expected_g:
                if result[tuple(-x for x in p)] != conjugate(result[p]):
                    raise AssertionError("exact node conjugacy failed")
            return result

        c = decode(raw["value_q52"])
        d = decode(raw["slope_q52"])
        del raw, g_array
        record["exact_input_checks"] = {"value_and_slope_modes": 4912, "divergence": "PASS", "conjugacy": "PASS",
                                         "decoder": "per-coefficient Fraction average then Fraction Leray, no shared LCM decoding"}
        checkpoint()
        residuals = {}
        lower = F(0)
        for k in selected:
            check()
            accumulator = list(ZERO_VECTOR)
            coverage = hashlib.sha256()
            ordered_count = unordered_count = diagonal_count = 0
            for p in expected_g:
                q = tuple(k[j] - p[j] for j in range(3))
                if q not in c:
                    continue
                ordered_count += 1
                coverage.update((",".join(map(str, p)) + ";" + ",".join(map(str, q)) + "\n").encode())
                if p > q:
                    continue
                if p == q:
                    diagonal_count += 1
                    factor = cdot(c[p], q)
                    for j in range(3):
                        accumulator[j] = cadd(accumulator[j], cmul(factor, c[q][j]))
                else:
                    unordered_count += 1
                    first, reverse = cdot(c[p], q), cdot(c[q], p)
                    for j in range(3):
                        pair = cadd(cmul(first, c[q][j]), cmul(reverse, c[p][j]))
                        accumulator[j] = cadd(accumulator[j], pair)
                if (unordered_count + diagonal_count) % 64 == 0:
                    guard_vector(accumulator)
                    check()
            if ordered_count != 2 * unordered_count + diagonal_count:
                raise AssertionError("unordered grouping lost an ordered source pair")
            full_F = tuple(accumulator)
            projected_F = project(full_F, k)
            k2 = sum(x*x for x in k)
            linear = tuple(cadd(d.get(k, ZERO_VECTOR)[j], cscale(c.get(k, ZERO_VECTOR)[j], k2)) for j in range(3))
            R = tuple(cadd(linear[j], (-projected_F[j][1], projected_F[j][0])) for j in range(3))
            if cdot(R, k) != ZERO:
                raise AssertionError("complete residual is not exactly divergence-free")
            for vector in (full_F, projected_F, linear, R):
                guard_vector(vector)
            contribution = k2**2 * sum((part*part for component in R for part in component), F(0))
            guard_fraction(contribution)
            lower += contribution
            guard_fraction(lower)
            residuals[k] = R
            record["mode_results"].append({"k": list(k), "k_squared": k2,
                                           "ordered_pairs": ordered_count, "unordered_distinct_pairs": unordered_count,
                                           "diagonal_pairs": diagonal_count, "ordered_pair_stream_sha256": coverage.hexdigest(),
                                           "F_unprojected": vector_json(full_F), "F_projected": vector_json(projected_F),
                                           "linear_d_plus_k2c": vector_json(linear), "R": vector_json(R),
                                           "weighted_R_squared": fraction_json(contribution)})
            record["partial_Lambda"] = fraction_json(lower)
            checkpoint()
            now = time.perf_counter()
            print(json.dumps({"independent_residual_progress": {"completed_modes": len(record["mode_results"]),
                              "total_modes": len(selected), "wall_seconds": now - start}}), flush=True)
        for k, value in residuals.items():
            opposite = tuple(-x for x in k)
            if opposite in residuals and residuals[opposite] != conjugate(value):
                raise AssertionError("selected residual conjugacy failed")
        term = polynomial = F(1)
        for j in range(1, 33):
            term *= F(5, 2*j)
            polynomial += term
        necessity = lower * polynomial
        for value in (polynomial, necessity):
            guard_fraction(value)
        lhs, rhs = necessity.numerator * 10**14, necessity.denominator
        if max(abs(lhs).bit_length(), rhs.bit_length()) > 8192:
            raise BudgetStop("comparison integer bit limit")
        record["result"] = {"Lambda": fraction_json(lower), "P32_of_5_over_2": fraction_json(polynomial),
                            "necessary_epsilon_squared_lower": fraction_json(necessity),
                            "old_threshold_comparison": {"lhs": str(lhs), "rhs": str(rhs), "difference": str(lhs-rhs),
                                                         "meaning": "Lambda * P32(5/2) > 1/10^14"}}
        record["mathematical_status"] = "OLD_REFERENCE_R2_ENVELOPE_REFUTED" if lhs > rhs else "LOWER_BOUND_INCONCLUSIVE"
        record["execution_status"] = "EXACT_RESULT_PENDING_FINAL_CHECKS"
        check()
        checkpoint()
        reread = json.loads((OUT / "run.json").read_text())
        if reread != record:
            raise AssertionError("exact evidence JSON readback mismatch")
        if any(sha(Path(name)) != expected for name, expected in info["source_sha256"].items()):
            raise AssertionError("source changed during execution")
        check()
        record["execution_status"] = "COMPLETE"
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL, 0)
        record["execution_status"] = "BUDGET_STOP" if isinstance(exc, BudgetStop) else "FAILED"
        record["mathematical_status"] = "NOT_ACCEPTED"
        record["error"] = {"type": type(exc).__name__, "message": str(exc)}
        print(json.dumps({"independent_residual_stop": record["error"]}), file=sys.stderr, flush=True)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        record["finished_at_utc"] = utc()
        observation = snapshot()
        over = observation["wall_seconds"] >= 120 or observation["peak_rss_bytes"] > CONFIG["peak_rss_budget_bytes"] or observation["output_bytes"] > CONFIG["output_budget_bytes"]
        if over:
            record["execution_status"], record["mathematical_status"] = "BUDGET_STOP", "NOT_ACCEPTED"
            record["final_budget_overrun"] = observation
        checkpoint(final=True)
        result_hash = sha(OUT / "run.json")
        final_observation = snapshot()
        over = final_observation["wall_seconds"] >= 120 or final_observation["peak_rss_bytes"] > CONFIG["peak_rss_budget_bytes"] or final_observation["output_bytes"] > CONFIG["output_budget_bytes"]
        if record["execution_status"] == "COMPLETE" and over:
            record["execution_status"], record["mathematical_status"] = "BUDGET_STOP", "NOT_ACCEPTED"
            record["final_budget_overrun"] = final_observation
            checkpoint(final=True)
            result_hash = sha(OUT / "run.json")
    print(json.dumps({"output": str(OUT / "run.json"), "sha256": result_hash,
                      "execution_status": record["execution_status"], "mathematical_status": record["mathematical_status"],
                      "final_observation": final_observation}, sort_keys=True), flush=True)
    return 0 if record["execution_status"] == "COMPLETE" else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--run", action="store_true")
    group.add_argument("--describe", action="store_true")
    group.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    try:
        info = preflight(require_bindings=args.run)
        if args.run:
            return run(info)
        print(json.dumps(info, indent=2, sort_keys=True))
        return 0
    except Exception as exc:
        print(json.dumps({"execution_status": "STARTUP_REFUSED_OR_UNRECOVERABLE_IO", "launch": launch(),
                          "error": {"type": type(exc).__name__, "message": str(exc)}}), file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
