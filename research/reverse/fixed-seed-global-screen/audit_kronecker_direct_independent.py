#!/usr/bin/env python3
"""Blind Fraction-to-Q96 reconstruction and all ordered-pair integer convolution.

No main implementation/output, FFT, packed convolution, integration, or retry.
Default/check-only authenticates files without loading node arrays or mathematics.
"""
import time

START = time.perf_counter()

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import resource
import signal
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = HERE / "kronecker-direct-independent-trial-01"
COUNT = 4912
OUTPUT_COUNT = 35937
Q52 = 1 << 52
Q96 = 1 << 96
SCALAR_LIMIT = 1 << 109
OUTPUT_LIMIT = 1 << 235
BITS = 8192
WALL = 60.0
RSS_CAP = 256 << 20
ARCHIVE_CAP = 8 << 20
RESERVE = 256 << 10
PROGRESS_ROWS = 128
ORIGINAL_CONFIG_SHA = "7649e366ee0fba6c5a051f0eecb45fc387a8bf91bc4bd06befa7e444e409f047"
INPUTS = {
    "node-trial-01/manifest.json": "5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd",
    "node-trial-01/modes.npy": "f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896",
    "node-trial-01/block-01280-01343.npz": "abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e",
}
SOURCES = {
    "KRONECKER_DECODING_INDEPENDENT_REVIEW.md": "16d36272c65f4e42040fcc7e79f4661a2b047d50c86dcabcf4b083281c3d82b9",
    "CONTINUOUS_RESIDUAL_COST_PREFLIGHT.md": "0c7ea4b3d33d152f298058a909e446505150d1004529f1a4518c2e1fedc7f796",
    "C1_RESIDUAL_CONTRACT.md": "a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251",
    "KRONECKER_DIRECT_INDEPENDENT_CONTRACT.md": "4693c1aed265dcd77a5d20b1d08eb715156d451379936cf012fdfa0749b76c12",
}
CONFIG = {
    "kind": "BLIND_DIRECT_GAUSSIAN_INTEGER_CONVOLUTION",
    "node": 1280, "time_numerator": 1280, "time_denominator": 2048,
    "G_count": COUNT, "G": "lexicographic [-8,8]^3 excluding zero",
    "tensor_components_one_based": [1, 2], "Q96": str(Q96),
    "tensor_denominator": str(1 << 192), "output_count": OUTPUT_COUNT,
    "reconstruction": "componentwise Fraction conjugate average then exact P_k",
    "rounding": "nearest integer ties even via Euclidean Fraction numerator division",
    "ordered_pairs": COUNT * COUNT, "zero_pair_skipping": False,
    "scalar_multiplications": 4 * COUNT * COUNT,
    "index": "(k1+16)+33*(k2+16)+1089*(k3+16)",
    "main_sources_or_outputs_read": False, "FFT": False,
    "integer_packed_convolution": False, "integration": False,
    "progress_rows": PROGRESS_ROWS, "wall_seconds": WALL,
    "rss_bytes": RSS_CAP, "archive_bytes": ARCHIVE_CAP,
    "metadata_reserve_bytes": RESERVE, "integer_bit_limit": BITS,
    "retry": False,
}
THREAD_KEYS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
               "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS",
               "OMP_DYNAMIC", "MKL_DYNAMIC")


class Failure(Exception):
    pass


class BudgetStop(Failure):
    pass


def must(condition, message):
    if not condition:
        raise Failure(message)


def utc():
    return datetime.now(timezone.utc).isoformat()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def checked(x):
    if max(abs(x.numerator).bit_length(), x.denominator.bit_length()) > BITS:
        raise BudgetStop("FRACTION_BIT_LIMIT")
    return x


def check_bindings(bindings):
    for relative, pin in bindings.items():
        must(re.fullmatch(r"[0-9a-f]{64}", pin) is not None, "INVALID_SHA_PIN: " + relative)
        must(file_sha(HERE / relative) == pin, "HASH_MISMATCH: " + relative)


def archive_bytes():
    return sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())


def observed():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return {"wall_seconds": time.perf_counter() - START,
            "peak_rss_bytes": int(rss if sys.platform == "darwin" else rss * 1024),
            "archive_bytes": archive_bytes()}


def exceeds(obs, reserve=False):
    return (obs["wall_seconds"] > WALL or obs["peak_rss_bytes"] > RSS_CAP or
            obs["archive_bytes"] > ARCHIVE_CAP - (RESERVE if reserve else 0))


def budget():
    obs = observed()
    if exceeds(obs, reserve=True):
        raise BudgetStop("OBSERVED_BUDGET_EXCEEDED: " + json.dumps(obs))
    return obs


def alarm_handler(_signum, _frame):
    raise BudgetStop("WALL_DEADLINE_EXPIRED")


def atomic(path, data):
    tmp = path.with_name(path.name + ".partial")
    with tmp.open("wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(tmp, path)


def json_file(path, value):
    data = canonical(value)
    atomic(path, data)
    back = path.read_bytes()
    must(back == data and json.loads(back) == value, "JSON_READBACK: " + path.name)
    return {"file": path.name, "bytes": len(back), "sha256": sha(back), "parsed_back": True}


def gzip_json(path, value):
    raw = canonical(value)
    encoded = gzip.compress(raw, compresslevel=6, mtime=0)
    if archive_bytes() + len(encoded) > ARCHIVE_CAP - RESERVE:
        raise BudgetStop("WITNESS_ARCHIVE_BUDGET")
    atomic(path, encoded)
    stored = path.read_bytes()
    decoded = gzip.decompress(stored)
    must(decoded == raw and json.loads(decoded) == value, "GZIP_PARSE_READBACK")
    return {"file": path.name, "bytes": len(stored), "sha256": sha(stored),
            "canonical_json_sha256": sha(decoded), "canonical_json_bytes": len(decoded),
            "parsed_back": True}


def progress(log, stage, **details):
    item = {"at_utc": utc(), "stage": stage, **details, **budget()}
    with (OUT / "progress.jsonl").open("ab") as stream:
        stream.write(canonical(item))
        stream.flush()
        os.fsync(stream.fileno())
    log["progress"] = item
    # Current metadata only; earlier progress remains append-only.
    json_file(OUT / "run.json", log)
    print(json.dumps(item, sort_keys=True), flush=True)


def cmd(args):
    return subprocess.check_output(args, cwd=ROOT, text=True, timeout=5,
                                   stderr=subprocess.DEVNULL).strip()


def checkout():
    commit = cmd(["git", "rev-parse", "HEAD"])
    branch = cmd(["git", "branch", "--show-current"])
    must(re.fullmatch(r"[0-9a-f]{40}", commit) is not None, "GIT_HEAD_FORMAT")
    must(branch == "codex/ns-reverse", "WRONG_BRANCH")
    return {"commit": commit, "branch": branch, "root": str(ROOT), "read_only": True}


def environment(np):
    cpu = platform.processor() or "unavailable"
    if sys.platform == "darwin":
        try:
            cpu = cmd(["/usr/sbin/sysctl", "-n", "machdep.cpu.brand_string"])
        except (OSError, subprocess.SubprocessError):
            pass
    return {"python": sys.version, "executable": sys.executable,
            "numpy": np.__version__, "numpy_path": np.__file__,
            "platform": platform.platform(), "machine": platform.machine(),
            "cpu": cpu, "logical_cpu_count": os.cpu_count(),
            "thread_environment": {key: os.environ.get(key) for key in THREAD_KEYS},
            "scientific_processes": 1, "scientific_python_threads": 1,
            "note": "NumPy only decodes and authenticates arrays. No FFT/BLAS, thread-setting changes, or scientific child process."}


def array_sha(arr):
    must(arr.flags.c_contiguous, "ARRAY_CONTIGUITY")
    return hashlib.sha256(memoryview(arr).cast("B")).hexdigest()


def load_original(np, log):
    check_bindings(INPUTS)
    manifest = json.loads((HERE / "node-trial-01/manifest.json").read_bytes())
    must(manifest["schema"] == "reverse-fixed-seed-nodes-v1", "ORIGINAL_SCHEMA")
    must(manifest["status"] == "CANDIDATE_NODES_COMPLETE_NOT_NS_CERTIFIED", "ORIGINAL_STATUS")
    must(manifest["config_sha256"] == ORIGINAL_CONFIG_SHA, "ORIGINAL_CONFIG_SHA")
    for key, value in {"viscosity": 1, "scale": 1, "rho": 1, "cutoff": 8,
                       "time_denominator": 2048, "quantization_denominator": Q52,
                       "G_count": COUNT, "steps": 5120, "nodes": 5121}.items():
        must(manifest["config"][key] == value, "ORIGINAL_CONFIG: " + key)
    ma = np.load(HERE / "node-trial-01/modes.npy", allow_pickle=False)
    desc = manifest["modes"]
    must(ma.dtype.str == desc["dtype"] == "<i8", "MODES_DTYPE")
    must(list(ma.shape) == desc["shape"] == [COUNT, 3], "MODES_SHAPE")
    must(array_sha(ma) == desc["array_sha256"], "MODES_ARRAY_SHA")
    modes = [tuple(int(x) for x in row) for row in ma]
    expected = [(x, y, z) for x in range(-8, 9) for y in range(-8, 9)
                for z in range(-8, 9) if (x, y, z) != (0, 0, 0)]
    must(modes == expected, "MODE_ORDER_OR_SUPPORT")
    blocks = [b for b in manifest["blocks"] if b["file"] == "block-01280-01343.npz"]
    must(len(blocks) == 1, "BLOCK_UNIQUENESS")
    bd = blocks[0]
    must((bd["first_node"], bd["last_node"], bd["node_count"]) == (1280, 1343, 64), "BLOCK_RANGE")
    value_row = None
    checks = {}
    with np.load(HERE / "node-trial-01/block-01280-01343.npz", allow_pickle=False) as block:
        must(set(block.files) == set(bd["arrays"]), "BLOCK_KEYS")
        for name in sorted(block.files):
            arr = block[name]
            spec = bd["arrays"][name]
            must(arr.dtype.str == spec["dtype"] == "<i8", "ARRAY_DTYPE: " + name)
            must(list(arr.shape) == spec["shape"] and arr.nbytes == spec["nbytes"], "ARRAY_SHAPE_SIZE: " + name)
            digest = array_sha(arr)
            must(digest == spec["data_sha256"], "ARRAY_DATA_SHA: " + name)
            checks[name] = {"data_sha256": digest, "dtype": arr.dtype.str,
                            "shape": list(arr.shape), "nbytes": arr.nbytes}
            if name == "value_q52":
                must(arr.shape == (64, COUNT, 3, 2), "VALUE_SHAPE")
                value_row = arr[0].copy()
            elif name == "slope_q52":
                must(arr.shape == (64, COUNT, 3, 2), "SLOPE_SHAPE")
            elif name in ("node_index", "time_numerator"):
                must([int(x) for x in arr] == list(range(1280, 1344)), "NODE_TIME_SEQUENCE")
            elif name == "time_denominator":
                must(arr.shape == (1,) and int(arr[0]) == 2048, "TIME_DENOMINATOR")
            elif name == "quantization_denominator":
                must(arr.shape == (1,) and int(arr[0]) == Q52, "QUANTIZATION_DENOMINATOR")
            else:
                raise Failure("UNEXPECTED_ARRAY")
            del arr
            budget()
    must(value_row is not None, "MISSING_VALUE_ROW")
    log["authenticated_arrays"] = checks
    log["mode_array_sha256"] = desc["array_sha256"]
    log["original_config_sha256"] = ORIGINAL_CONFIG_SHA
    return modes, value_row


def project_fraction(raw, index, opposite, k):
    avg = []
    for component in range(3):
        for ri in range(2):
            x, y = int(raw[index, component, ri]), int(raw[opposite, component, ri])
            must(abs(x) < (1 << 63) and abs(y) < (1 << 63), "RAW_SCALAR_RANGE")
            avg.append(Fraction(x + (y if ri == 0 else -y), 2 * Q52))
    s = sum(x * x for x in k)
    dots = [sum((k[a] * avg[2 * a + ri] for a in range(3)), Fraction(0))
            for ri in range(2)]
    return tuple(checked(avg[2 * a + ri] - Fraction(k[a], s) * dots[ri])
                 for a in range(3) for ri in range(2))


def round_fraction(c):
    scaled = checked(c * Q96)
    n, d = scaled.numerator, scaled.denominator
    q, r = divmod(n, d)
    must(0 <= r < d and n == d * q + r, "EUCLIDEAN_DIVISION")
    rounded = q + int(2 * r > d or (2 * r == d and q % 2 != 0))
    must(2 * abs(n - d * rounded) <= d, "ROUNDING_ERROR")
    must(2 * r != d or rounded % 2 == 0, "ROUNDING_TIE")
    must(abs(rounded) < SCALAR_LIMIT, "Q96_SCALAR_LIMIT")
    return rounded, [str(n), str(d), str(q), str(r), str(rounded)]


def scalar_binary(path, rows, width, limit):
    # Per-scalar storage encoding only; never used as a convolution operand.
    blob = bytearray(sum(len(row) for row in rows) * width)
    cursor = 0
    for row in rows:
        for x in row:
            must(abs(x) < limit, "BINARY_SCALAR_BOUND")
            blob[cursor:cursor + width] = x.to_bytes(width, "little", signed=True)
            cursor += width
    if archive_bytes() + len(blob) > ARCHIVE_CAP - RESERVE:
        raise BudgetStop("BINARY_ARCHIVE_BUDGET")
    atomic(path, blob)
    back = path.read_bytes()
    must(back == blob, "BINARY_BYTE_READBACK")
    cursor = 0
    for row in rows:
        for x in row:
            must(int.from_bytes(back[cursor:cursor + width], "little", signed=True) == x,
                 "BINARY_SCALAR_READBACK")
            cursor += width
    return {"file": path.name, "bytes": len(back), "sha256": sha(back),
            "signed_scalar_width_bytes": width, "scalar_count": cursor // width,
            "every_scalar_decoded_back": True}


def reconstruct(np, log):
    modes, raw = load_original(np, log)
    lookup = {k: i for i, k in enumerate(modes)}
    opposite = [lookup[tuple(-x for x in k)] for k in modes]
    projected = []
    centers = []
    witnesses = []
    for i, k in enumerate(modes):
        c = project_fraction(raw, i, opposite[i], k)
        projected.append(c)
        values, records = [], []
        for x in c:
            rounded, record = round_fraction(x)
            values.append(rounded)
            records.append(record)
        centers.append(tuple(values))
        witnesses.append(records)
        if (i + 1) % 512 == 0 or i + 1 == COUNT:
            progress(log, "FRACTION_RECONSTRUCTION", completed_modes=i + 1)
    del raw
    for i, k in enumerate(modes):
        c, cn = projected[i], projected[opposite[i]]
        v, vn = centers[i], centers[opposite[i]]
        for ri in range(2):
            must(sum((k[a] * c[2 * a + ri] for a in range(3)), Fraction(0)) == 0,
                 "EXACT_PROJECTED_DIVERGENCE")
        for a in range(3):
            must(c[2*a] == cn[2*a] and c[2*a+1] == -cn[2*a+1], "PROJECTED_CONJUGACY")
            must(v[2*a] == vn[2*a] and v[2*a+1] == -vn[2*a+1], "Q96_CONJUGACY")
        if (i + 1) % 512 == 0:
            budget()
    log["constraints"] = {"projected_divergence": True, "projected_conjugacy": True,
                          "q96_conjugacy": True, "q96_divergence_required": False,
                          "rounding_scalars_verified": 6 * COUNT}
    record = scalar_binary(OUT / "centers-independent.i112le.bin", centers, 14, SCALAR_LIMIT)
    log["output_files"].append(record)
    witness = {"schema": "independent-q96-fraction-rounding-v1", "node": 1280,
               "ordering": "original mode order; component-major real,imag",
               "entries": witnesses, "entry_fields": ["scaled_numerator", "scaled_denominator",
                                                           "floor_quotient", "remainder", "rounded"],
               "scaled_value": "2^96 times exact projected original Fraction",
               "input_sha256": INPUTS, "mode_array_sha256": log["mode_array_sha256"]}
    log["output_files"].append(gzip_json(OUT / "rounding-witnesses.json.gz", witness))
    del projected, witnesses, witness
    progress(log, "INDEPENDENT_INPUT_COMPLETE", modes=COUNT)
    return modes, centers


def direct_convolution(modes, centers, log, state):
    # Coordinates are shifted only for ordinary output array indexing.
    exponents = [(k[0] + 8) + 33 * (k[1] + 8) + 1089 * (k[2] + 8) for k in modes]
    must(len(set(exponents)) == COUNT and min(exponents) >= 0 and max(exponents) <= 17968,
         "ORDINARY_INDEX_MAP")
    left = [(exponents[i], c[0], c[1]) for i, c in enumerate(centers)]
    right = [(exponents[i], c[2], c[3]) for i, c in enumerate(centers)]
    real = [0] * OUTPUT_COUNT
    imag = [0] * OUTPUT_COUNT
    state["real"], state["imag"] = real, imag
    state["completed_rows"] = 0
    progress(log, "DIRECT_CONVOLUTION_START", ordered_pairs=COUNT * COUNT)
    convolution_start = time.perf_counter()
    for row, (ep, u, v) in enumerate(left):
        # All 4912 right inputs are visited, including exact zero values.
        # Four integer products; signed cancellation precedes output accumulation.
        for eq, x, y in right:
            index = ep + eq
            real[index] += u * x - v * y
            imag[index] += u * y + v * x
        state["completed_rows"] = row + 1
        log["completed_rows"] = row + 1
        log["completed_pairs"] = (row + 1) * COUNT
        if (row + 1) % PROGRESS_ROWS == 0 or row + 1 == COUNT:
            progress(log, "DIRECT_CONVOLUTION_ROWS", completed_rows=row + 1,
                     completed_pairs=(row + 1) * COUNT,
                     convolution_wall_seconds=time.perf_counter() - convolution_start)
    log["convolution_wall_seconds"] = time.perf_counter() - convolution_start
    must(log["completed_pairs"] == COUNT * COUNT, "PAIR_COUNT")
    for j in range(OUTPUT_COUNT):
        must(abs(real[j]) < OUTPUT_LIMIT and abs(imag[j]) < OUTPUT_LIMIT, "OUTPUT_BOUND")
        neg = OUTPUT_COUNT - 1 - j
        must(real[j] == real[neg] and imag[j] == -imag[neg], "TENSOR_CONJUGACY")
    must(imag[17968] == 0, "ZERO_FREQUENCY_IMAGINARY_PART")
    log["constraints"].update({"full_tensor_conjugacy": True, "zero_frequency_imaginary_zero": True,
                               "every_output_bound_2pow235": True})
    return real, imag


def perform(np, log, state):
    modes, centers = reconstruct(np, log)
    real, imag = direct_convolution(modes, centers, log, state)
    rows = list(zip(real, imag))
    tensor = scalar_binary(OUT / "tensor12-direct.i240le.bin", rows, 30, OUTPUT_LIMIT)
    must(tensor["bytes"] == 2156220 and tensor["scalar_count"] == 71874, "TENSOR_ARCHIVE_SIZE")
    log["output_files"].append(tensor)
    result = {
        "schema": "direct-gaussian-tensor-result-v1",
        "mathematical_status": "ONE_FIXED_DIRECT_GAUSSIAN_CONVOLUTION_RECOMPUTED",
        "main_result_comparison": "NOT_PERFORMED_BLIND_OUTPUT_FROZEN_FIRST",
        "node": 1280, "time": ["1280", "2048"],
        "tensor_components_one_based": [1, 2], "tensor_denominator": str(1 << 192),
        "output_count": OUTPUT_COUNT, "scalar_count": 2 * OUTPUT_COUNT,
        "ordering": "j=(k1+16)+33*(k2+16)+1089*(k3+16); real then imaginary",
        "completed_rows": log["completed_rows"], "ordered_pairs": log["completed_pairs"],
        "scalar_integer_multiplications": 4 * log["completed_pairs"],
        "tensor_file": tensor, "output_files": list(log["output_files"]),
        "constraints": log["constraints"], "input_sha256": INPUTS,
        "source_sha256": log["source_sha256"], "config_sha256": log["config_sha256"],
        "checkout": log["checkout"],
        "limitations": ["One dyadic tensor only", "No pressure/output derivative contraction",
                        "No linear term or full residual", "No time interval or NS trajectory certificate"],
    }
    log["output_files"].append(json_file(OUT / "result.json", result))
    for record in log["output_files"]:
        path = OUT / record["file"]
        must(file_sha(path) == record["sha256"], "FINAL_FILE_HASH: " + path.name)
    must(json.loads((OUT / "result.json").read_bytes()) == result, "FINAL_RESULT_PARSE")
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--run", action="store_true")
    group.add_argument("--check-only", action="store_true")
    ap.add_argument("--approved-source-sha256")
    ap.add_argument("--code-review-file")
    ap.add_argument("--code-review-sha256")
    args = ap.parse_args()
    try:
        must(sys.version_info >= (3, 10), "SUPPORTED_PYTHON_REQUIRES_3_10_OR_NEWER")
        must(ROOT == Path("/Users/kasifa/Documents/Math/navier-stokes-reverse"), "WRONG_TREE")
        check_bindings(SOURCES)
        check_bindings(INPUTS)
        own_sha = file_sha(Path(__file__).resolve())
        must(not OUT.exists(), "EXCLUSIVE_DIRECTORY_EXISTS_NO_RETRY")
        if not args.run:
            print(json.dumps({"status": "STARTUP_PREFLIGHT_PASS_NOT_RUN", "script_sha256": own_sha,
                              "config_sha256": sha(canonical(CONFIG)), "input_sha256": INPUTS,
                              "all_pin_lengths": 64, "node_arrays_loaded": False,
                              "scientific_kernel_executed": False, "output_exists": False}, sort_keys=True))
            return 0
        must(args.approved_source_sha256 == own_sha, "APPROVED_SOURCE_SHA_REQUIRED")
        must(args.code_review_file is not None and args.code_review_sha256 is not None,
             "ROOT_CODE_REVIEW_REQUIRED")
        review = Path(args.code_review_file).resolve()
        must(review.parent == HERE and review.suffix == ".md", "LOCAL_CODE_REVIEW_MD_REQUIRED")
        must(re.fullmatch(r"[0-9a-f]{64}", args.code_review_sha256) is not None, "REVIEW_SHA_FORMAT")
        must(file_sha(review) == args.code_review_sha256, "REVIEW_SHA_MISMATCH")
        must(own_sha.encode("ascii") in review.read_bytes(), "REVIEW_DOES_NOT_BIND_THIS_SCRIPT")
        bindings = {**SOURCES, Path(__file__).name: own_sha, review.name: args.code_review_sha256}
        identity = checkout()
        OUT.mkdir(exist_ok=False)
    except (Failure, OSError, subprocess.SubprocessError) as exc:
        print(json.dumps({"status": "STARTUP_REFUSED", "error": str(exc)}, ensure_ascii=False),
              file=sys.stderr, flush=True)
        return 2
    log = {"schema": "direct-gaussian-independent-run-v1", "status": "CLAIMED",
           "started_at_utc": utc(), "pid": os.getpid(), "working_directory": str(ROOT),
           "command_argv": list(getattr(sys, "orig_argv", [sys.executable] + sys.argv)),
           "source_sha256": bindings, "input_sha256": INPUTS, "checkout": identity,
           "config": CONFIG, "config_sha256": sha(canonical(CONFIG)),
           "completed_rows": 0, "completed_pairs": 0, "output_files": [],
           "budget_semantics": "Observed overruns cannot COMPLETE; not OS prevention of temporary over-allocation."}
    state = {}
    complete = False
    try:
        json_file(OUT / "claim.json", {"pid": os.getpid(), "source_sha256": own_sha,
                                       "started_at_utc": log["started_at_utc"], "retry": False})
        remaining = WALL - (time.perf_counter() - START)
        if remaining <= 0:
            raise BudgetStop("STARTUP_EXHAUSTED_WALL_BUDGET")
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.setitimer(signal.ITIMER_REAL, remaining)
        import numpy as np
        log["environment"] = environment(np)
        progress(log, "INPUT_AUTHENTICATION_START")
        perform(np, log, state)
        check_bindings(bindings)
        check_bindings(INPUTS)
        must(checkout() == identity, "CHECKOUT_CHANGED_DURING_RUN")
        progress(log, "ALL_INDEPENDENT_DATA_VERIFIED")
        log["status"] = "DATA_VERIFIED_FINALIZING"
        complete = True
    except BaseException as exc:
        log["status"] = "COST_NOT_PAID" if isinstance(exc, BudgetStop) else "FAILED_PRESERVED"
        log["error"] = {"type": type(exc).__name__, "message": str(exc)}
    finally:
        try:
            signal.setitimer(signal.ITIMER_REAL, 0)
        except BaseException as exc:
            log["status"] = "COST_NOT_PAID" if isinstance(exc, BudgetStop) else "FAILED_PRESERVED"
            log["error"] = {"type": type(exc).__name__, "message": str(exc)}
            complete = False
            signal.setitimer(signal.ITIMER_REAL, 0)
    if not complete and "real" in state:
        try:
            partial = scalar_binary(OUT / "partial-tensor-UNCERTIFIED.i240le.bin",
                                    list(zip(state["real"], state["imag"])), 30, OUTPUT_LIMIT)
            partial["meaning"] = "Interrupted accumulators, possibly within a real/imaginary pair; not a certified partial sum and not a resume checkpoint."
            partial["fully_completed_outer_rows"] = state["completed_rows"]
            log["output_files"].append(partial)
        except BaseException as exc:
            log["partial_preservation_error"] = {"type": type(exc).__name__, "message": str(exc)}
    try:
        log["finished_at_utc"] = utc()
        log["final_budget_observation"] = observed()
        if exceeds(log["final_budget_observation"]):
            log["status"] = "COST_NOT_PAID"
        elif complete:
            log["status"] = "COMPLETE_DIRECT_GAUSSIAN_INDEPENDENT"
        json_file(OUT / "run.json", log)
        digest = file_sha(OUT / "run.json")
        post = observed()
        if exceeds(post):
            log["status"] = "COST_NOT_PAID"
            log["post_write_budget_observation"] = post
            json_file(OUT / "run.json", log)
            digest = file_sha(OUT / "run.json")
            post = observed()
        print(json.dumps({"status": log["status"], "run_sha256": digest,
                          "post_write_budget_observation": post,
                          "output_directory": str(OUT)}, sort_keys=True), flush=True)
        return 0 if log["status"] == "COMPLETE_DIRECT_GAUSSIAN_INDEPENDENT" else 1
    except BaseException as exc:
        print(json.dumps({"status": "FINALIZATION_FAILED_PRESERVED", "error": str(exc),
                          "output_directory": str(OUT)}, ensure_ascii=False), file=sys.stderr, flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
