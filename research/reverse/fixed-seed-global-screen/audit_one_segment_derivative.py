#!/usr/bin/env python3
"""One fixed Hermite segment: integer Bernstein/template norm upper bounds.

No integration, FFT, mode selection or parameter scan. Explicit --run requires
the separately approved strain-review binding. Default is read-only preflight.
"""
from __future__ import annotations

import argparse
import ast
import datetime as dt
from fractions import Fraction
import gzip
import hashlib
import itertools
import json
import math
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
WORKTREE = HERE.parents[2]
OUT = HERE / "one-segment-derivative-trial-01"
OWN_CONTRACT = HERE / "ONE_SEGMENT_DERIVATIVE_CONTRACT.md"
STRAIN = HERE / "STRAIN_CONTROL_REFINEMENT.md"
C1 = HERE / "C1_RESIDUAL_CONTRACT.md"
STRAIN_APPROVED_SHA256 = "d6ab251e47d5818078f045d3f0ab7aae778e8e624c468633c360a9ed08930e01"
STRAIN_REVIEW = {
    "file": "STRAIN_CONTROL_INDEPENDENT_REVIEW.md",
    "sha256": "628ced02a9107039119dcb1744a718db7e2a4b692444c9867b3c62886e39c42e",
}
ARCHIVE = {
    "node-trial-01/manifest.json": "5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd",
    "node-trial-01/modes.npy": "f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896",
    "node-trial-01/block-01280-01343.npz": "abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e",
}
CONFIG = {
    "segment_index": 1280, "node_indices": [1280, 1281], "time_denominator": 2048,
    "Q": 1 << 52, "G_count": 4912, "cutoff": 8, "Bernstein_count": 4,
    "derivative_orders": [1, 2, 3], "sqrt_fractional_bits": 128,
    "common_Bernstein_multiplier": 6144, "maximum_integer_bits": 8192,
    "wall_seconds": 60, "peak_rss_bytes": 256 * 1024**2,
    "output_bytes": 16 * 1024**2, "metadata_reserve_bytes": 256 * 1024,
    "chi": "Re(v_(+e1),component2); no template fitting",
    "integration": False, "FFT": False, "selection": False, "retry": False,
    "run_directory": str(OUT),
}


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


def mode_list():
    return [k for k in itertools.product(range(-8, 9), repeat=3) if k != (0, 0, 0)]


def rational(numerator, denominator=1):
    value = Fraction(numerator, denominator)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def preflight(for_run=False):
    if sys.version_info < (3, 10):
        raise RuntimeError("Python >=3.10 required; use bundled Python 3.12")
    compile(ast.parse(Path(__file__).read_bytes()), str(Path(__file__)), "exec")
    ready = all(STRAIN_REVIEW.values())
    if for_run and not ready:
        raise ValueError("independently approved S.3 review is not bound; execution refused before creating a directory")
    if sha(STRAIN) != STRAIN_APPROVED_SHA256:
        raise ValueError("independently approved strain proof SHA mismatch")
    sources = [Path(__file__), OWN_CONTRACT, STRAIN, C1]
    if ready:
        review = HERE / STRAIN_REVIEW["file"]
        if sha(review) != STRAIN_REVIEW["sha256"]:
            raise ValueError("approved strain review SHA mismatch")
        sources.append(review)
    return {"status": "READY_FOR_ROOT_SOURCE_REVIEW" if ready else "AWAITING_STRAIN_REVIEW_BINDING_AND_ROOT_SOURCE_REVIEW",
            "scientific_execution": False, "config": CONFIG, "strain_review": STRAIN_REVIEW,
            "approved_strain_proof_sha256": STRAIN_APPROVED_SHA256,
            "config_sha256": hashlib.sha256(canonical({"config": CONFIG, "strain_review": STRAIN_REVIEW,
                                                       "approved_strain_proof_sha256": STRAIN_APPROVED_SHA256})).hexdigest(),
            "source_sha256": {str(p): sha(p) for p in sources},
            "pinned_archive_sha256": ARCHIVE, "output_directory_exists": OUT.exists()}


class BudgetStop(RuntimeError):
    pass


def peak_rss():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def run(info):
    preflight(for_run=True)
    OUT.mkdir(exist_ok=True)
    if any(OUT.iterdir()):
        raise FileExistsError("fixed trial directory is not empty; no retry or overwrite")
    with (OUT / "RUN_CLAIM.json").open("x") as stream:
        json.dump({"started_at_utc": utc(), "pid": os.getpid(), "launch": launch()}, stream)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    started = time.perf_counter()
    record = {"execution_status": "RUNNING", "mathematical_status": "NOT_COMPUTED",
              "started_at_utc": utc(), "launch": launch(), "inputs": info,
              "maximum_integer_bits_observed": 0, "Bernstein_results": [],
              "scope": "only the fixed segment derivative upper bounds; no actual eigenvalue, residual, global control, or NS trajectory certificate"}

    def total_bytes():
        return sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())

    def resources():
        return {"wall_seconds": time.perf_counter() - started, "peak_rss_bytes": peak_rss(), "output_bytes": total_bytes()}

    def over_budget(observation):
        return (observation["wall_seconds"] >= 60 or observation["peak_rss_bytes"] > CONFIG["peak_rss_bytes"]
                or observation["output_bytes"] > CONFIG["output_bytes"])

    def check():
        observation = resources()
        if over_budget(observation):
            raise BudgetStop("observed fixed wall/RSS/output limit: " + json.dumps(observation))

    def guard(*integers):
        bits = max((abs(x).bit_length() for x in integers), default=0)
        record["maximum_integer_bits_observed"] = max(record["maximum_integer_bits_observed"], bits)
        if bits > 8192:
            raise BudgetStop("8192-bit integer/intermediate limit")

    def atomic_bytes(name, data, metadata=False):
        cap = CONFIG["output_bytes"] - (0 if metadata else CONFIG["metadata_reserve_bytes"])
        if total_bytes() + len(data) > cap:
            raise BudgetStop("output cap including atomic temporary and metadata reserve")
        temporary = OUT / (name + ".tmp")
        with temporary.open("wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(OUT / name)

    def checkpoint(final=False):
        record["resources"] = resources()
        atomic_bytes("run.json", canonical(record) + b"\n", metadata=final)

    def square_root_bounds(N):
        if N < 0:
            raise AssertionError("negative norm square")
        shifted = N << 256
        guard(N, shifted)
        low = math.isqrt(shifted)
        exact = low * low == shifted
        high = low if exact else low + 1
        if not (low*low <= shifted <= high*high and shifted < (low+1)*(low+1)):
            raise AssertionError("integer square-root containment failed")
        return low, high, not exact

    def stop_signal(signum, frame):
        raise BudgetStop("deadline or external stop signal " + str(signum))

    for signum in (signal.SIGALRM, signal.SIGINT, signal.SIGTERM):
        signal.signal(signum, stop_signal)
    signal.setitimer(signal.ITIMER_REAL, 60)
    try:
        checkpoint()
        sys.dont_write_bytecode = True
        import numpy as np
        source_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=WORKTREE, text=True, timeout=2).strip()
        if len(source_commit) != 40 or any(c not in "0123456789abcdef" for c in source_commit):
            raise ValueError("unexpected reverse worktree source commit format")
        record["source_commit"] = {"worktree": str(WORKTREE), "git_HEAD": source_commit,
                                   "scope": "observed at execution; individual input/source byte hashes remain binding"}
        cpu = platform.processor()
        if sys.platform == "darwin":
            cpu = subprocess.check_output(["/usr/sbin/sysctl", "-n", "machdep.cpu.brand_string"], text=True, timeout=1).strip()
        record["environment"] = {"python": sys.version, "numpy": np.__version__, "numpy_path": np.__file__,
                                 "platform": platform.platform(), "cpu": cpu, "logical_cpu_count": os.cpu_count(),
                                 "thread_environment": {k: os.environ.get(k) for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS")},
                                 "arithmetic": "single-process Python arbitrary-precision int/isqrt and Fraction; no workers or multiprocessing; NumPy only authenticates/reads original int64 arrays"}
        authenticated = {}
        for path, expected in ARCHIVE.items():
            if sha(HERE / path) != expected:
                raise ValueError("original archive SHA mismatch: " + path)
            authenticated[path] = expected
            check()
        manifest = json.loads((HERE / "node-trial-01/manifest.json").read_text())
        if manifest["status"] != "CANDIDATE_NODES_COMPLETE_NOT_NS_CERTIFIED":
            raise ValueError("original node archive did not complete")
        physical = {"scale": 1, "viscosity": 1, "rho": 1, "grid": 27, "cutoff": 8,
                    "time_denominator": 2048, "steps": 5120, "nodes": 5121, "quantization_denominator": 1 << 52}
        if any(manifest["config"].get(k) != v for k, v in physical.items()):
            raise ValueError("original physical/encoding configuration mismatch")
        modes = mode_list()
        g = np.load(HERE / "node-trial-01/modes.npy", allow_pickle=False)
        if g.dtype.str != "<i8" or g.shape != (4912, 3) or [tuple(int(x) for x in row) for row in g] != modes:
            raise ValueError("complete signed G/order mismatch")
        if hashlib.sha256(memoryview(g).cast("B")).hexdigest() != manifest["modes"]["array_sha256"]:
            raise ValueError("mode array SHA mismatch")
        matches = [b for b in manifest["blocks"] if b["first_node"] <= 1280 and b["last_node"] >= 1281]
        if len(matches) != 1 or matches[0]["file"] != "block-01280-01343.npz":
            raise ValueError("unique two-node source block mismatch")
        block = matches[0]
        raw = {}
        with np.load(HERE / "node-trial-01" / block["file"], allow_pickle=False) as archive:
            required = {"node_index", "time_numerator", "time_denominator", "quantization_denominator", "value_q52", "slope_q52"}
            if set(archive.files) != required or set(block["arrays"]) != required:
                raise ValueError("unexpected original array keys")
            for name in sorted(required):
                array = archive[name]
                descriptor = {"shape": list(array.shape), "dtype": array.dtype.str, "nbytes": array.nbytes,
                              "data_sha256": hashlib.sha256(memoryview(array).cast("B")).hexdigest()}
                if descriptor != block["arrays"][name] or array.dtype.str != "<i8":
                    raise ValueError("array byte/dtype/shape authentication failed: " + name)
                if name in ("value_q52", "slope_q52"):
                    if array.shape != (64, 4912, 3, 2):
                        raise ValueError("unexpected original coefficient shape")
                    raw[name] = array[:2].copy()
                elif name in ("node_index", "time_numerator"):
                    if array.tolist() != list(range(1280, 1344)):
                        raise ValueError("time/node sequence mismatch")
                elif array.tolist() != ([2048] if name == "time_denominator" else [1 << 52]):
                    raise ValueError("time or Q52 denominator mismatch")
                del array
                check()
        record["authenticated_archive_sha256"] = authenticated
        positions = {p: n for n, p in enumerate(modes)}
        opposite = [positions[tuple(-x for x in p)] for p in modes]
        s = [sum(x*x for x in p) for p in modes]
        L = math.lcm(*s)
        D = 2 * (1 << 52) * L
        E = 6144 * D
        guard(L, D, E)
        record["common_denominators"] = {"L": str(L), "D": str(D), "E": str(E)}

        def check_constraints(field, label):
            for n, p in enumerate(modes):
                value, other = field[n], field[opposite[n]]
                if sum(p[j]*value[2*j] for j in range(3)) or sum(p[j]*value[2*j+1] for j in range(3)):
                    raise AssertionError("exact divergence failed: " + label)
                if any(value[2*j] != other[2*j] or value[2*j+1] != -other[2*j+1] for j in range(3)):
                    raise AssertionError("exact conjugacy failed: " + label)
                guard(*value)

        def decode(encoded, label):
            result = []
            for n, p in enumerate(modes):
                re, im = [], []
                for j in range(3):
                    pr, pi = int(encoded[n, j, 0]), int(encoded[n, j, 1])
                    nr, ni = int(encoded[opposite[n], j, 0]), int(encoded[opposite[n], j, 1])
                    if max(abs(pr), abs(pi), abs(nr), abs(ni)) >= 1 << 63:
                        raise ValueError("stored integer violates strict Q52 signed bound")
                    re.append(pr + nr)
                    im.append(pi - ni)
                dot_re = sum(p[j]*re[j] for j in range(3))
                dot_im = sum(p[j]*im[j] for j in range(3))
                factor = L // s[n]
                value = tuple(x for j in range(3) for x in (factor*(s[n]*re[j]-p[j]*dot_re), factor*(s[n]*im[j]-p[j]*dot_im)))
                guard(*value)
                result.append(value)
                if n % 128 == 0:
                    check()
            check_constraints(result, label)
            return result

        A0 = decode(raw["value_q52"][0], "A0")
        A1 = decode(raw["value_q52"][1], "A1")
        J0 = decode(raw["slope_q52"][0], "J0")
        J1 = decode(raw["slope_q52"][1], "J1")
        del raw, g
        seed_components = {}
        for axis, component in ((0, 1), (1, 2), (2, 0)):
            for sign in (-1, 1):
                p = [0, 0, 0]
                p[axis] = sign
                seed_components[positions[tuple(p)]] = component
        chi_position = positions[(1, 0, 0)]
        norm_inputs = {"schema": "Bernstein-template-base-squares-v1", "segment_index": 1280,
                       "mode_order_source": "node-trial-01/modes.npy", "mode_order_file_sha256": ARCHIVE["node-trial-01/modes.npy"],
                       "normalization": "N_(m,k,j)=|k|^(2j)*base_squared[m][k]; root sum divided by E",
                       "L": str(L), "D": str(D), "E": str(E), "chi_numerators": [], "base_squared": [],
                       "source_binding": info["source_sha256"], "original_archive_binding": ARCHIVE}
        upper_by_order = {j: [] for j in (1, 2, 3)}
        sqrt_unit = 1 << 128
        for m in range(4):
            check()
            base = A0 if m < 2 else A1
            slope = J0 if m == 1 else J1 if m == 2 else None
            sign = 1 if m == 1 else -1 if m == 2 else 0
            V = [tuple(6144*base[n][j] + (sign*slope[n][j] if slope is not None else 0) for j in range(6)) for n in range(4912)]
            check_constraints(V, "V" + str(m))
            chi_num = V[chi_position][2]  # component 2 real part; flat [re0,im0,re1,im1,re2,im2]
            W = []
            for n, value in enumerate(V):
                vector = list(value)
                if n in seed_components:
                    vector[2*seed_components[n]] -= chi_num
                W.append(tuple(vector))
            check_constraints(W, "W" + str(m))
            squared = [sum(component*component for component in value) for value in W]
            for N in squared:
                guard(N)
            norm_inputs["chi_numerators"].append(str(chi_num))
            norm_inputs["base_squared"].append([str(N) for N in squared])
            item = {"m": m, "chi_numerator_over_E": str(chi_num), "chi": rational(chi_num, E),
                    "complete_signed_mode_count": 4912, "exact_divergence_and_conjugacy": "PASS", "orders": {}}
            for j in (1, 2, 3):
                lower_sum = upper_sum = inexact_count = 0
                for n, N in enumerate(squared):
                    lower, upper, inexact = square_root_bounds(s[n]**j * N)
                    lower_sum += lower
                    upper_sum += upper
                    inexact_count += int(inexact)
                    if n % 128 == 0:
                        check()
                guard(lower_sum, upper_sum)
                upper_value = Fraction(upper_sum, E * sqrt_unit)
                upper_by_order[j].append(upper_value)
                item["orders"][str(j)] = {"sum_floor_scaled_roots": str(lower_sum),
                                          "sum_ceil_scaled_roots": str(upper_sum), "non_square_count": inexact_count,
                                          "sum_denominator": str(E * sqrt_unit),
                                          "A_j_lower": rational(lower_sum, E * sqrt_unit),
                                          "A_j_upper": rational(upper_sum, E * sqrt_unit)}
            record["Bernstein_results"].append(item)
            checkpoint()
            print(json.dumps({"segment_derivative_progress": {"completed_Bernstein_coefficients": m + 1, "wall_seconds": time.perf_counter()-started}}), flush=True)
            del V, W, squared
        data = canonical(norm_inputs)
        check()
        compressed = gzip.compress(data, compresslevel=6, mtime=0)
        check()
        atomic_bytes("norm-square-inputs.json.gz", compressed)
        norm_file = OUT / "norm-square-inputs.json.gz"
        record["norm_square_evidence"] = {"file": norm_file.name, "file_bytes": norm_file.stat().st_size,
                                          "file_sha256": sha(norm_file), "uncompressed_bytes": len(data),
                                          "canonical_json_sha256": hashlib.sha256(data).hexdigest(),
                                          "base_square_shape": [4, 4912], "derived_root_input_count": 4 * 4912 * 3}
        # Actual post-write decompression/readback, not merely an in-memory hash.
        reread = gzip.decompress(norm_file.read_bytes())
        if reread != data or json.loads(reread) != norm_inputs:
            raise AssertionError("norm-square evidence file readback failed")
        chi_max = Fraction(max(abs(int(x)) for x in norm_inputs["chi_numerators"]), E)
        U = {j: max(upper_by_order[j]) for j in (1, 2, 3)}
        root2lo, root2hi, _ = square_root_bounds(2)
        root3lo, root3hi, _ = square_root_bounds(3)
        invsqrt2_upper = Fraction(root2hi, 2 * sqrt_unit)
        sqrt3_upper = Fraction(root3hi, sqrt_unit)
        sigma_upper = 2*chi_max + U[1]*invsqrt2_upper
        M_upper = {j: 2*sqrt3_upper*chi_max + U[j] for j in (2, 3)}
        for number in [chi_max, *U.values(), invsqrt2_upper, sqrt3_upper, sigma_upper, *M_upper.values()]:
            guard(number.numerator, number.denominator)
        record["whole_segment_upper_bounds"] = {
            "time_numerators": [1280, 1281], "time_denominator": 2048,
            "chi_absolute_upper": rational(chi_max),
            "A_j_b_upper": {str(j): rational(U[j]) for j in (1, 2, 3)},
            "sqrt2_interval": [rational(root2lo, sqrt_unit), rational(root2hi, sqrt_unit)],
            "sqrt3_interval": [rational(root3lo, sqrt_unit), rational(root3hi, sqrt_unit)],
            "inverse_sqrt2_upper": rational(invsqrt2_upper), "sigma_upper": rational(sigma_upper),
            "M2_upper": rational(M_upper[2]), "M3_upper": rational(M_upper[3]),
            "sigma_meaning": "certified upper bound from S.3; not the actual minimum eigenvalue or spatial optimum",
            "scope": "one full fixed segment only; usefulness for global control not asserted",
        }
        record["input_constraints"] = {"endpoint_value_slope_fields": 4, "modes_per_field": 4912,
                                       "exact_endpoint_and_Bernstein_divergence_conjugacy": "PASS",
                                       "full_signed_spectrum_no_extra_factor_two": True}
        record["execution_status"] = "RESULT_PENDING_FINAL_CHECKS"
        record["mathematical_status"] = "ONE_SEGMENT_TEMPLATE_DERIVATIVE_UPPER_BOUNDS"
        checkpoint()
        if json.loads((OUT / "run.json").read_text()) != record:
            raise AssertionError("result JSON actual readback failed")
        for path, expected in info["source_sha256"].items():
            if sha(Path(path)) != expected:
                raise ValueError("source/proof bytes changed during run")
        for path, expected in ARCHIVE.items():
            if sha(HERE / path) != expected:
                raise ValueError("original archive changed during run")
        check()
        record["execution_status"] = "VERIFIED_FINALIZING"
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL, 0)
        record["execution_status"] = "BUDGET_STOP" if isinstance(exc, BudgetStop) else "FAILED"
        record["mathematical_status"] = "NOT_ACCEPTED"
        record["error"] = {"type": type(exc).__name__, "message": str(exc)}
        print(json.dumps({"segment_derivative_stop": record["error"]}), file=sys.stderr, flush=True)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        record["finished_at_utc"] = utc()
        observation = resources()
        if over_budget(observation):
            record["execution_status"], record["mathematical_status"] = "BUDGET_STOP", "NOT_ACCEPTED"
            record["final_budget_overrun"] = observation
        elif record["execution_status"] == "VERIFIED_FINALIZING":
            record["execution_status"] = "COMPLETE"
        checkpoint(final=True)
        result_hash = sha(OUT / "run.json")
        final_observation = resources()
        if record["execution_status"] == "COMPLETE" and over_budget(final_observation):
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
        info = preflight(for_run=args.run)
        if args.run:
            return run(info)
        print(json.dumps(info, sort_keys=True, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"execution_status": "STARTUP_REFUSED_OR_UNRECOVERABLE_IO", "launch": launch(),
                          "error": {"type": type(exc).__name__, "message": str(exc)}}), file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
