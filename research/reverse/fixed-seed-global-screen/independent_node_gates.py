#!/usr/bin/env python3
"""Independent two-node Fraction/ordered-tensor checks. No integration."""
from __future__ import annotations
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
import sys
import time

HERE = Path(__file__).resolve().parent
ARCHIVE = HERE / "node-trial-01"
EXPECTED_MANIFEST = "5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd"
TARGETS = (640, 5120)
QUANTIZATION = 1 << 52
SQRT_DENOMINATOR = 1 << 80
LIMIT_SECONDS = 60


class BudgetStop(RuntimeError):
    pass


def need(condition, message):
    if not condition:
        raise ValueError(message)


def rational(value):
    value = Fraction(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def file_digest(path):
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for piece in iter(lambda: handle.read(1 << 20), b""):
            h.update(piece)
    return h.hexdigest()


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def array_digest(array):
    return hashlib.sha256(array.tobytes(order="C")).hexdigest()


def new_json(path, value):
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, sort_keys=True, indent=2, allow_nan=False)
        handle.write("\n")


def project_fraction(raw, modes, progress):
    """Each component has its own Fraction; no common spectrum denominator."""
    integer_rows = raw.tolist()
    positions = {k: index for index, k in enumerate(modes)}
    coeff = []
    for index, wave in enumerate(modes):
        opposite = positions[tuple(-k for k in wave)]
        re = [Fraction(int(integer_rows[index][d][0]) +
                       int(integer_rows[opposite][d][0]), 2*QUANTIZATION)
              for d in range(3)]
        im = [Fraction(int(integer_rows[index][d][1]) -
                       int(integer_rows[opposite][d][1]), 2*QUANTIZATION)
              for d in range(3)]
        square = sum(k*k for k in wave)
        dot_re = sum((wave[d]*re[d] for d in range(3)), Fraction(0))
        dot_im = sum((wave[d]*im[d] for d in range(3)), Fraction(0))
        projected = tuple((re[d] - Fraction(wave[d], square)*dot_re,
                           im[d] - Fraction(wave[d], square)*dot_im)
                          for d in range(3))
        need(sum((wave[d]*projected[d][0] for d in range(3)), Fraction(0)) == 0,
             "nonzero exact real divergence")
        need(sum((wave[d]*projected[d][1] for d in range(3)), Fraction(0)) == 0,
             "nonzero exact imaginary divergence")
        coeff.append(projected)
        if index % 256 == 0:
            progress("fraction_projection", mode=index)
    for index, wave in enumerate(modes):
        other = coeff[positions[tuple(-k for k in wave)]]
        need(all(coeff[index][d][0] == other[d][0] and
                 coeff[index][d][1] == -other[d][1] for d in range(3)),
             "nonzero exact reality defect")
    return coeff


def encoded_coefficients(modes, coeff):
    return [{"mode": list(wave),
             "components": [{"real": rational(real), "imaginary": rational(imag)}
                            for real, imag in values]}
            for wave, values in zip(modes, coeff)]


def ordered_third_derivative(modes, coeff, progress):
    phased = []
    for wave, values in zip(modes, coeff):
        row = list(values)
        for _ in range(sum(wave) % 4):
            row = [(-imag, real) for real, imag in row]
        phased.append(row)
    tensor, square_norm = [], Fraction(0)
    for axes in itertools.product(range(3), repeat=3):
        re, im = [Fraction(0) for _ in range(3)], [Fraction(0) for _ in range(3)]
        for wave, values in zip(modes, phased):
            factor = wave[axes[0]] * wave[axes[1]] * wave[axes[2]]
            if factor:
                # Three ordered derivatives multiply the phased coefficient by -i.
                for d in range(3):
                    re[d] += factor * values[d][1]
                    im[d] -= factor * values[d][0]
        need(all(value == 0 for value in im), "nonreal ordered derivative")
        item_square = sum((value*value for value in re), Fraction(0))
        square_norm += item_square
        tensor.append({"ordered_axes": list(axes),
                       "real": [rational(value) for value in re],
                       "imaginary": [rational(value) for value in im],
                       "vector_square": rational(item_square)})
        progress("ordered_third_derivative", components_completed=len(tensor))
    need(len(tensor) == 27, "incomplete ordered derivative tensor")
    s = Fraction(5, 8)
    terms = [Fraction(s.numerator**degree,
                      s.denominator**degree * math.factorial(degree))
             for degree in range(33)]
    polynomial = sum(terms, Fraction(0))
    margin = square_norm*polynomial - 16
    return {"node": 640, "time": rational(Fraction(5, 16)),
            "ordered_tensor": tensor, "squared_frobenius": rational(square_norm),
            "P32_terms": [rational(term) for term in terms],
            "P32_of_twice_time": rational(polynomial),
            "q_times_P32_minus_16": rational(margin),
            "reference_M3_cost_target_refuted": margin > 0,
            "non_refutation_is_not_an_upper_bound": True}


def endpoint_bound(modes, coeff, progress):
    denominator = SQRT_DENOMINATOR
    lower, upper, nonexact = 0, 0, 0
    evidence = []
    for index, (wave, values) in enumerate(zip(modes, coeff)):
        square = sum((real*real + imag*imag for real, imag in values), Fraction(0))
        ratio = square / sum(k*k for k in wave)
        scaled_numerator = ratio.numerator * denominator**2
        floor_value = scaled_numerator // ratio.denominator
        lo = math.isqrt(floor_value)
        need(lo*lo*ratio.denominator <= scaled_numerator <
             (lo+1)*(lo+1)*ratio.denominator, "invalid endpoint square-root bracket")
        exact = lo*lo*ratio.denominator == scaled_numerator
        hi = lo if exact else lo+1
        lower += lo
        upper += hi
        nonexact += not exact
        evidence.append({"mode": list(wave), "coefficient_squared_modulus": rational(square),
                         "weighted_squared_modulus": rational(ratio),
                         "sqrt_lower_numerator": str(lo), "sqrt_upper_numerator": str(hi),
                         "sqrt_denominator": str(denominator), "exact": exact})
        if index % 256 == 0:
            progress("endpoint_square_root", mode=index)
    need(upper-lower == nonexact and nonexact <= 4912, "incorrect total bracket width")
    return {"node": 5120, "time": rational(Fraction(5, 2)),
            "square_root_precision_bits": 80, "mode_evidence": evidence,
            "A_minus_1_lower": rational(Fraction(lower, denominator)),
            "A_minus_1_upper": rational(Fraction(upper, denominator)),
            "A_minus_1_width": rational(Fraction(nonexact, denominator)),
            "upper_le_half": 2*upper <= denominator,
            "complete_plus_minus_spectrum": True,
            "scope": "REFERENCE_ENDPOINT_NORM_ONLY_NO_NS_EXTENSION"}


def main():
    need(sys.version_info >= (3, 10), "Use Python >=3.10")
    result_path = HERE / "independent-node-gates-result.json"
    run_path = HERE / "independent-node-gates-run.json"
    claim_path = HERE / "independent-node-gates-claim.json"
    need(not result_path.exists() and not run_path.exists(), "output already exists")
    started = time.perf_counter()
    begun_at = utc()
    launch = {"actual_command": [sys.executable, *sys.orig_argv[1:]],
              "cwd": os.getcwd(), "pid": os.getpid(), "started_at_utc": begun_at}
    new_json(claim_path, launch)
    state = {"scope": "TWO_FIXED_REFERENCE_NODES_ONLY_NO_NS_CONCLUSION",
             "nodes_requested": list(TARGETS), "completed": {}, "input_sha256": {},
             "source_sha256": {}, "progress": []}
    last_progress = started

    def progress(phase, force=False, **details):
        nonlocal last_progress
        now = time.perf_counter()
        if now-started >= LIMIT_SECONDS:
            raise BudgetStop("fixed 60 second arithmetic budget reached")
        if force or now-last_progress >= 10:
            item = {"phase": phase, "wall_seconds": now-started, **details}
            state["progress"].append(item)
            print(json.dumps(item), flush=True)
            last_progress = now

    def deadline(_signal, _frame):
        raise BudgetStop("fixed 60 second timer reached")

    def bind_source(path):
        state["source_sha256"][str(path.relative_to(HERE))] = file_digest(path)

    def bind_input(path, expected=None):
        digest = file_digest(path)
        if expected is not None:
            need(digest == expected, "input file hash mismatch: "+str(path))
        state["input_sha256"][str(path.relative_to(HERE))] = digest

    status, failure = "FAILED", None
    signal.signal(signal.SIGALRM, deadline)
    signal.setitimer(signal.ITIMER_REAL, max(0.001, LIMIT_SECONDS-(time.perf_counter()-started)))
    try:
        import numpy as np
        state["numpy"] = np.__version__
        for path in (Path(__file__), HERE / "NODE_GATE_INDEPENDENT_RUN_CONTRACT.md",
                     HERE / "NODE_GATE_LEMMA.md", HERE / "NODE_PRODUCTION_CONTRACT.md"):
            bind_source(path)
        manifest_path = ARCHIVE / "manifest.json"
        bind_input(manifest_path, EXPECTED_MANIFEST)
        manifest = json.loads(manifest_path.read_text())
        need(manifest["schema"] == "reverse-fixed-seed-nodes-v1", "wrong schema")
        need(manifest["status"] == "CANDIDATE_NODES_COMPLETE_NOT_NS_CERTIFIED",
             "production not complete and fixed")
        need(manifest["stored_nodes"] == 5121 and manifest["completed_steps"] == 5120,
             "incomplete production metadata")
        config = manifest["config"]
        need(config["cutoff"] == 8 and config["time_denominator"] == 2048 and
             config["quantization_denominator"] == QUANTIZATION, "wrong fixed input parameters")
        need(config["scale"] == config["rho"] == config["viscosity"] == 1,
             "wrong physical parameters")
        need(hashlib.sha256(canonical(config)).hexdigest() == manifest["config_sha256"],
             "configuration hash mismatch")
        mode_path = ARCHIVE / manifest["modes"]["file"]
        need(mode_path.parent == ARCHIVE and mode_path.name == "modes.npy", "wrong mode path")
        bind_input(mode_path, manifest["modes"]["file_sha256"])
        raw_modes = np.load(mode_path, allow_pickle=False)
        need(raw_modes.dtype.str == "<i8" and raw_modes.shape == (4912, 3), "wrong mode array")
        need(array_digest(raw_modes) == manifest["modes"]["array_sha256"], "mode array hash")
        modes = [tuple(int(value) for value in row) for row in raw_modes.tolist()]
        need(modes == [wave for wave in itertools.product(range(-8, 9), repeat=3)
                       if wave != (0, 0, 0)], "not the full prescribed spectrum")
        next_node, chosen = 0, {}
        for entry in manifest["blocks"]:
            count = entry["node_count"]
            need(1 <= count <= 64 and entry["first_node"] == next_node and
                 entry["last_node"] == next_node+count-1, "inconsistent block coverage")
            for node in TARGETS:
                if next_node <= node <= entry["last_node"]:
                    need(node not in chosen, "duplicate target block")
                    chosen[node] = entry
            next_node += count
        need(next_node == 5121 and set(chosen) == set(TARGETS), "missing requested nodes")
        for node in TARGETS:
            entry = chosen[node]
            path = ARCHIVE / entry["file"]
            expected_name = f"block-{entry['first_node']:05d}-{entry['last_node']:05d}.npz"
            need(path.parent == ARCHIVE and path.name == expected_name, "wrong block path")
            need(path.stat().st_size == entry["file_bytes"], "block length mismatch")
            bind_input(path, entry["file_sha256"])
            need(hashlib.sha256(canonical(entry["arrays"])).hexdigest() == entry["data_sha256"],
                 "array description digest")
            with np.load(path, allow_pickle=False) as archive:
                required = {"node_index", "time_numerator", "time_denominator",
                            "quantization_denominator", "value_q52", "slope_q52"}
                need(set(archive.files) == set(entry["arrays"]) == required, "wrong array inventory")
                value = None
                for name in sorted(required):
                    array = archive[name]
                    desc = entry["arrays"][name]
                    need(list(array.shape) == desc["shape"] and array.dtype.str == desc["dtype"] == "<i8",
                         "shape or dtype mismatch")
                    need(array.nbytes == desc["nbytes"] and array_digest(array) == desc["data_sha256"],
                         "array data mismatch")
                    if name in ("node_index", "time_numerator"):
                        need(array.tolist() == list(range(entry["first_node"], entry["last_node"]+1)),
                             "node numbering mismatch")
                    elif name == "time_denominator":
                        need(array.tolist() == [2048], "time denominator mismatch")
                    elif name == "quantization_denominator":
                        need(array.tolist() == [QUANTIZATION], "quantization denominator mismatch")
                    else:
                        need(array.shape == (entry["node_count"], 4912, 3, 2), "node value/slope shape")
                        if name == "value_q52":
                            value = array[node-entry["first_node"]].copy()
                    del array
            need(value is not None, "missing node values")
            progress("authenticated_fixed_node", force=True, node=node)
            coeff = project_fraction(value, modes, progress)
            del value
            computation = (ordered_third_derivative(modes, coeff, progress) if node == 640
                           else endpoint_bound(modes, coeff, progress))
            computation["projected_coefficients"] = encoded_coefficients(modes, coeff)
            state["completed"][str(node)] = computation
            del coeff
            progress("completed_fixed_node", force=True, node=node)
        for relative, expected in state["input_sha256"].items():
            need(file_digest(HERE / relative) == expected, "input changed during check")
        for relative, expected in state["source_sha256"].items():
            need(file_digest(HERE / relative) == expected, "source changed during check")
        progress("all_arithmetic_complete", force=True)
        status = "TWO_FIXED_REFERENCE_NODES_COMPUTED"
    except BaseException as exc:
        status = "BUDGET_STOP" if isinstance(exc, BudgetStop) else "FAILED"
        failure = {"type": type(exc).__name__, "message": str(exc)}
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    arithmetic_wall = time.perf_counter()-started
    if arithmetic_wall >= LIMIT_SECONDS and status == "TWO_FIXED_REFERENCE_NODES_COMPUTED":
        status = "BUDGET_STOP"
        failure = {"type": "BudgetStop", "message": "final arithmetic observation exceeded 60 seconds"}
    state["status"] = status
    state["error"] = failure
    state["unselected_block_files_or_arrays_checked"] = False
    state["root_audit_results_read_or_imported"] = False
    new_json(result_path, state)
    run = {**launch, "finished_at_utc": utc(), "status": status, "error": failure,
           "arithmetic_wall_seconds": arithmetic_wall,
           "elapsed_before_run_record_seconds": time.perf_counter()-started,
           "evidence_cleanup_seconds": time.perf_counter()-started-arithmetic_wall,
           "budget_seconds": LIMIT_SECONDS, "python": sys.version, "platform": platform.platform(),
           "numpy": state.get("numpy"), "optimization": sys.flags.optimize,
           "peak_rss_native": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
           "rss_units": "bytes on macOS; native ru_maxrss otherwise",
           "cpu_count": os.cpu_count(),
           "thread_environment": {key: os.environ.get(key) for key in
                                  ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                                   "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")},
           "thread_scope": "one Python process; no FFT or BLAS mathematical arithmetic; internal library workers not inferred",
           "result_file": result_path.name, "result_sha256": file_digest(result_path),
           "source_sha256": state["source_sha256"], "input_sha256": state["input_sha256"]}
    new_json(run_path, run)
    print(json.dumps({"status": status, "arithmetic_wall_seconds": arithmetic_wall,
                      "result": result_path.name, "result_sha256": file_digest(result_path),
                      "run": run_path.name, "run_sha256": file_digest(run_path),
                      "error": failure}), flush=True)
    return 0 if status == "TWO_FIXED_REFERENCE_NODES_COMPUTED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
