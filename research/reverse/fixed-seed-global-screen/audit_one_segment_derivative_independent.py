#!/usr/bin/env python3
"""One fixed segment, independent Fraction reconstruction; no FFT or integration.

Default/check-only does not import NumPy, load node arrays, or create output.
Execution requires a separate root code review bound to this script's bytes.
"""
import time

START = time.perf_counter()

import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import resource
import signal
import subprocess
import sys
from datetime import datetime, timezone
from fractions import Fraction as F

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = HERE / "one-segment-derivative-independent-trial-01"
P = 128
Q52 = 1 << 52
COUNT = 4912
BIT_LIMIT = 8192
WALL = 60.0
RSS_LIMIT = 256 << 20
ARCHIVE_LIMIT = 16 << 20
RESERVE = 256 << 10
ORIGINAL_CONFIG_SHA = "7649e366ee0fba6c5a051f0eecb45fc387a8bf91bc4bd06befa7e444e409f047"
INPUTS = {
    "node-trial-01/manifest.json": "5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd",
    "node-trial-01/modes.npy": "f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896",
    "node-trial-01/block-01280-01343.npz": "abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e",
}
SOURCES = {
    "ONE_SEGMENT_DERIVATIVE_CONTRACT.md": "a53006b424c2166ad943166abca8e284138e64d31a6d07131041f9da9afa229a",
    "ONE_SEGMENT_DERIVATIVE_INDEPENDENT_CONTRACT.md": "f3a382ffc6ba5770cb552b3c8192345d2e6ae1eb871c6ca68f39a0b926855689",
    "C1_RESIDUAL_CONTRACT.md": "a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251",
    "STRAIN_CONTROL_REFINEMENT.md": "d6ab251e47d5818078f045d3f0ab7aae778e8e624c468633c360a9ed08930e01",
    "STRAIN_CONTROL_INDEPENDENT_REVIEW.md": "628ced02a9107039119dcb1744a718db7e2a4b692444c9867b3c62886e39c42e",
}
CONFIG = {
    "kind": "INDEPENDENT_FRACTION_SINGLE_SEGMENT_DERIVATIVE_UPPER",
    "node_indices": [1280, 1281], "time_denominator": 2048,
    "G": "lexicographic [-8,8]^3 excluding zero", "G_count": COUNT,
    "bernstein_degree": 3, "derivative_orders": [1, 2, 3],
    "template": "a=2(cos(x3),cos(x1),cos(x2))",
    "chi": "Re(v_(+e1),component_2)", "viscosity": 1,
    "normalization": "normalized volume, Fourier series, ordered Frobenius",
    "projection": "componentwise Fraction conjugate average then exact P_k",
    "root": "128 normalized fractional bits; rational scaled isqrt",
    "use_common_spectral_denominator": False,
    "main_implementation_or_outputs_read": False,
    "FFT": False, "integration": False, "parameter_scan": False,
    "wall_seconds": WALL, "rss_bytes": RSS_LIMIT,
    "archive_bytes": ARCHIVE_LIMIT, "metadata_reserve_bytes": RESERVE,
    "integer_bit_limit": BIT_LIMIT, "retry": False,
}
THREAD_KEYS = (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS",
    "OMP_DYNAMIC", "MKL_DYNAMIC",
)


class AuditFailure(Exception):
    pass


class BudgetStop(AuditFailure):
    pass


def require(condition, message):
    if not condition:
        raise AuditFailure(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def utc():
    return datetime.now(timezone.utc).isoformat()


def bits(*integers):
    if any(abs(n).bit_length() > BIT_LIMIT for n in integers):
        raise BudgetStop("INTEGER_BIT_LIMIT")


def checked_fraction(x):
    bits(x.numerator, x.denominator)
    return x


def pair(x):
    checked_fraction(x)
    return [str(x.numerator), str(x.denominator)]


def interval(lo, hi):
    require(F(0) <= lo <= hi, "INVALID_NONNEGATIVE_INTERVAL")
    return {"lower": pair(lo), "upper": pair(hi)}


def peak_rss():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def archive_size():
    return sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())


def observation():
    return {"wall_seconds": time.perf_counter() - START,
            "peak_rss_bytes": peak_rss(), "archive_bytes": archive_size()}


def over_budget(obs, reserve=False):
    return (obs["wall_seconds"] > WALL or obs["peak_rss_bytes"] > RSS_LIMIT
            or obs["archive_bytes"] > ARCHIVE_LIMIT - (RESERVE if reserve else 0))


def budget():
    obs = observation()
    if over_budget(obs, reserve=True):
        raise BudgetStop("OBSERVED_BUDGET_EXCEEDED: " + json.dumps(obs))
    return obs


def alarm_handler(_signum, _frame):
    raise BudgetStop("WALL_TIMER_EXPIRED")


def atomic_bytes(path, data):
    temp = path.with_name(path.name + ".partial")
    with temp.open("wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)


def write_json(path, value):
    data = canonical(value)
    atomic_bytes(path, data)
    readback = path.read_bytes()
    require(readback == data, "JSON_BYTE_READBACK: " + path.name)
    require(json.loads(readback) == value, "JSON_PARSE_READBACK: " + path.name)
    return {"file": path.name, "bytes": len(readback), "sha256": sha_bytes(readback)}


def write_gzip_json(path, value):
    raw = canonical(value)
    compressed = gzip.compress(raw, compresslevel=6, mtime=0)
    if archive_size() + len(compressed) > ARCHIVE_LIMIT - RESERVE:
        raise BudgetStop("OUTPUT_PREFLIGHT_LIMIT")
    atomic_bytes(path, compressed)
    stored = path.read_bytes()
    unpacked = gzip.decompress(stored)
    require(unpacked == raw, "GZIP_RAW_READBACK")
    require(json.loads(unpacked) == value, "GZIP_PARSE_READBACK")
    return {"file": path.name, "bytes": len(stored), "sha256": sha_bytes(stored),
            "canonical_json_sha256": sha_bytes(unpacked),
            "canonical_json_bytes": len(unpacked), "parse_readback": True}


def progress(log, stage, **detail):
    record = {"at_utc": utc(), "stage": stage, **detail, **budget()}
    with (OUT / "progress.jsonl").open("ab") as stream:
        stream.write(canonical(record))
        stream.flush()
        os.fsync(stream.fileno())
    log["progress"] = record
    print(json.dumps(record, ensure_ascii=False), flush=True)


def command_text(args):
    return subprocess.check_output(args, cwd=ROOT, text=True,
                                   timeout=5, stderr=subprocess.DEVNULL).strip()


def checkout():
    commit = command_text(["git", "rev-parse", "HEAD"])
    branch = command_text(["git", "branch", "--show-current"])
    require(len(commit) == 40 and all(c in "0123456789abcdef" for c in commit),
            "INVALID_GIT_HEAD")
    require(branch == "codex/ns-reverse", "WRONG_BRANCH")
    return {"commit": commit, "branch": branch, "root": str(ROOT),
            "git_operations": "read-only HEAD and branch identity"}


def environment(np):
    cpu = platform.processor() or "unavailable"
    if sys.platform == "darwin":
        try:
            cpu = command_text(["/usr/sbin/sysctl", "-n", "machdep.cpu.brand_string"])
        except (OSError, subprocess.SubprocessError):
            pass
    return {"python": sys.version, "executable": sys.executable,
            "numpy": np.__version__, "numpy_path": np.__file__,
            "platform": platform.platform(), "machine": platform.machine(),
            "cpu": cpu, "logical_cpu_count": os.cpu_count(),
            "thread_environment": {k: os.environ.get(k) for k in THREAD_KEYS},
            "scientific_process_count": 1, "scientific_arithmetic_threads": 1,
            "note": "Single Python Fraction/isqrt process. NumPy only decodes/hash-checks arrays; no FFT/BLAS invoked. No thread environment changed."}


def check_sources(bindings):
    for relative, expected in bindings.items():
        require(file_sha(HERE / relative) == expected, "SOURCE_HASH: " + relative)


def array_sha(arr):
    # All input arrays are required C contiguous: raw memory has canonical C order.
    require(arr.flags.c_contiguous, "NONCONTIGUOUS_INPUT")
    return hashlib.sha256(memoryview(arr).cast("B")).hexdigest()


def load_original(np, log):
    check_sources(INPUTS)
    manifest = json.loads((HERE / "node-trial-01/manifest.json").read_bytes())
    require(manifest["schema"] == "reverse-fixed-seed-nodes-v1", "SCHEMA")
    require(manifest["status"] == "CANDIDATE_NODES_COMPLETE_NOT_NS_CERTIFIED", "NODE_STATUS")
    require(manifest["config_sha256"] == ORIGINAL_CONFIG_SHA, "ORIGINAL_CONFIG_HASH")
    config = manifest["config"]
    for key, value in {"viscosity": 1, "scale": 1, "rho": 1, "time_denominator": 2048,
                       "quantization_denominator": Q52, "nodes": 5121, "steps": 5120,
                       "G_count": COUNT, "cutoff": 8}.items():
        require(config[key] == value, "CONFIG: " + key)
    mode_array = np.load(HERE / "node-trial-01/modes.npy", allow_pickle=False)
    md = manifest["modes"]
    require(mode_array.dtype.str == md["dtype"] == "<i8", "MODE_DTYPE")
    require(list(mode_array.shape) == md["shape"] == [COUNT, 3], "MODE_SHAPE")
    require(array_sha(mode_array) == md["array_sha256"], "MODE_ARRAY_HASH")
    modes = [tuple(int(x) for x in row) for row in mode_array]
    expected_modes = [(x, y, z) for x in range(-8, 9) for y in range(-8, 9)
                      for z in range(-8, 9) if (x, y, z) != (0, 0, 0)]
    require(modes == expected_modes, "MODE_ORDER_OR_SUPPORT")
    descriptions = [b for b in manifest["blocks"] if b["file"] == "block-01280-01343.npz"]
    require(len(descriptions) == 1, "BLOCK_COUNT")
    desc = descriptions[0]
    require((desc["first_node"], desc["last_node"], desc["node_count"]) == (1280, 1343, 64),
            "BLOCK_RANGE")
    copied = {}
    checked = {}
    with np.load(HERE / "node-trial-01/block-01280-01343.npz", allow_pickle=False) as archive:
        require(set(archive.files) == set(desc["arrays"]), "BLOCK_KEYS")
        for name in sorted(archive.files):
            arr = archive[name]
            spec = desc["arrays"][name]
            require(arr.dtype.str == spec["dtype"] == "<i8", "ARRAY_DTYPE: " + name)
            require(list(arr.shape) == spec["shape"], "ARRAY_SHAPE: " + name)
            require(arr.nbytes == spec["nbytes"], "ARRAY_NBYTES: " + name)
            digest = array_sha(arr)
            require(digest == spec["data_sha256"], "ARRAY_HASH: " + name)
            checked[name] = {"data_sha256": digest, "dtype": arr.dtype.str,
                             "shape": list(arr.shape), "nbytes": arr.nbytes}
            if name in ("value_q52", "slope_q52"):
                require(arr.shape == (64, COUNT, 3, 2), "SPECTRAL_ARRAY_SHAPE")
                copied[name] = arr[:2].copy()
            elif name in ("node_index", "time_numerator"):
                require([int(x) for x in arr] == list(range(1280, 1344)), "NODE_TIME_SEQUENCE")
            elif name == "time_denominator":
                require(arr.shape == (1,) and int(arr[0]) == 2048, "TIME_UNIT")
            elif name == "quantization_denominator":
                require(arr.shape == (1,) and int(arr[0]) == Q52, "Q52_UNIT")
            else:
                raise AuditFailure("UNEXPECTED_ARRAY: " + name)
            del arr
            budget()
    log["input_arrays"] = checked
    log["mode_array_sha256"] = md["array_sha256"]
    log["original_config_sha256"] = ORIGINAL_CONFIG_SHA
    return modes, copied


def exact_project(raw, row, index, opposite, k):
    # Six real Fractions: Re/Im are separate; integer promotion precedes arithmetic.
    averaged = []
    for component in range(3):
        for ri in range(2):
            x = int(raw[row, index, component, ri])
            y = int(raw[row, opposite, component, ri])
            require(abs(x) < (1 << 63) and abs(y) < (1 << 63), "RAW_SCALAR_RANGE")
            averaged.append(F(x + (y if ri == 0 else -y), 2 * Q52))
    s = sum(t * t for t in k)
    dots = [sum((k[a] * averaged[2 * a + ri] for a in range(3)), F(0))
            for ri in range(2)]
    return tuple(checked_fraction(averaged[2 * a + ri] - F(k[a], s) * dots[ri])
                 for a in range(3) for ri in range(2))


def verify_vector_constraints(vectors, modes, opposites):
    for index, k in enumerate(modes):
        v = vectors[index]
        opposite = vectors[opposites[index]]
        for ri in range(2):
            require(sum((k[a] * v[2 * a + ri] for a in range(3)), F(0)) == 0,
                    "EXACT_DIVERGENCE")
        for a in range(3):
            require(v[2 * a] == opposite[2 * a], "EXACT_REAL_CONJUGACY")
            require(v[2 * a + 1] == -opposite[2 * a + 1], "EXACT_IMAG_CONJUGACY")
        if index % 256 == 0:
            budget()


def root_interval(x):
    """Exact normalized rational isqrt, returning lower, upper, exponent, square."""
    checked_fraction(x)
    require(x >= 0, "NEGATIVE_RADICAND")
    if x == 0:
        return F(0), F(0), None, True
    n, d = x.numerator, x.denominator
    q = n.bit_length() - d.bit_length()
    below_power = (n < (d << q)) if q >= 0 else ((n << (-q)) < d)
    if below_power:
        q -= 1
    e = q // 2
    shift = 2 * (P - e)
    aa, bb = ((n << shift), d) if shift >= 0 else (n, (d << (-shift)))
    bits(aa, bb)
    ell = math.isqrt(aa // bb)
    require((1 << P) <= ell < (1 << (P + 1)), "SQRT_NORMALIZATION")
    lower_square = ell * ell * bb
    next_square = (ell + 1) * (ell + 1) * bb
    bits(ell, lower_square, next_square)
    require(lower_square <= aa < next_square, "ISQRT_ENCLOSURE")
    exact = lower_square == aa
    upper = ell if exact else ell + 1
    scale = F(1 << (e - P)) if e >= P else F(1, 1 << (P - e))
    lo, hi = checked_fraction(ell * scale), checked_fraction(upper * scale)
    require(lo * lo <= x <= hi * hi, "RATIONAL_SQRT_ENCLOSURE")
    return lo, hi, e, exact


def template_component(k):
    if k in ((1, 0, 0), (-1, 0, 0)):
        return 1
    if k in ((0, 1, 0), (0, -1, 0)):
        return 2
    if k in ((0, 0, 1), (0, 0, -1)):
        return 0
    return None


def bernstein_vector(m, i, tables):
    c0, d0, c1, d1 = (table[i] for table in tables)
    if m == 0:
        return c0
    if m == 1:
        return tuple(checked_fraction(c0[a] + d0[a] / 6144) for a in range(6))
    if m == 2:
        return tuple(checked_fraction(c1[a] - d1[a] / 6144) for a in range(6))
    return c1


def compute(np, log):
    modes, raw = load_original(np, log)
    positions = {k: i for i, k in enumerate(modes)}
    opposites = [positions[tuple(-x for x in k)] for k in modes]
    tables = []
    for label, name, row in (("c0", "value_q52", 0), ("d0", "slope_q52", 0),
                             ("c1", "value_q52", 1), ("d1", "slope_q52", 1)):
        table = []
        for i, k in enumerate(modes):
            table.append(exact_project(raw[name], row, i, opposites[i], k))
            if i % 256 == 0:
                progress(log, "FRACTION_PROJECT", table=label, completed_modes=i + 1)
        verify_vector_constraints(table, modes, opposites)
        tables.append(table)
        progress(log, "PROJECTED_TABLE_COMPLETE", table=label, modes=COUNT)
    del raw
    chi_index = positions[(1, 0, 0)]
    chi = []
    norms = []
    artifact_records = []
    result_rows = []
    for m in range(4):
        vectors = [bernstein_vector(m, i, tables) for i in range(COUNT)]
        verify_vector_constraints(vectors, modes, opposites)
        cm = vectors[chi_index][2]
        chi.append(cm)
        b = []
        for i, k in enumerate(modes):
            vals = list(vectors[i])
            component = template_component(k)
            if component is not None:
                vals[2 * component] -= cm
            b.append(tuple(checked_fraction(x) for x in vals))
        verify_vector_constraints(b, modes, opposites)
        require(b[chi_index][2] == 0, "CHI_REAL_COMPONENT_NOT_REMOVED")
        squared = []
        sums = [[F(0), F(0)] for _ in range(3)]
        nonsquares = [0, 0, 0]
        exponent_ranges = [[None, None] for _ in range(3)]
        for i, k in enumerate(modes):
            ss = checked_fraction(sum((x * x for x in b[i]), F(0)))
            require(ss >= 0, "NEGATIVE_NORM_SQUARE")
            squared.append(pair(ss))
            s = sum(x * x for x in k)
            for j in (1, 2, 3):
                lo, hi, e, exact = root_interval(checked_fraction((s ** j) * ss))
                sums[j - 1][0] = checked_fraction(sums[j - 1][0] + lo)
                sums[j - 1][1] = checked_fraction(sums[j - 1][1] + hi)
                nonsquares[j - 1] += int(not exact)
                if e is not None:
                    oldlo, oldhi = exponent_ranges[j - 1]
                    exponent_ranges[j - 1] = [e if oldlo is None else min(e, oldlo),
                                               e if oldhi is None else max(e, oldhi)]
            if i % 256 == 0:
                progress(log, "NORM_SUM", bernstein=m, completed_modes=i + 1)
        for i, opposite in enumerate(opposites):
            require(squared[i] == squared[opposite], "NORM_SQUARE_CONJUGACY")
        archive = {
            "schema": "independent-fraction-mode-norm-squares-v1", "bernstein": m,
            "quantity": "sum of six squared Fraction components of b_(k,m)",
            "ordering": "original modes.npy; full signed lexicographic G",
            "mode_count": COUNT, "norm_square": squared,
            "chi": pair(cm), "input_file_sha256": INPUTS,
            "mode_array_sha256": log["mode_array_sha256"],
            "constraints": {"projected_nodes": True, "v_divergence_conjugacy": True,
                            "b_divergence_conjugacy": True, "chi_real_component_removed": True},
        }
        record = write_gzip_json(OUT / ("norm-squares-m%d.json.gz" % m), archive)
        artifact_records.append(record)
        row = {"bernstein": m, "chi": pair(cm), "A": {
            str(j): {**interval(*sums[j - 1]), "terms": COUNT,
                     "nonsquare_count": nonsquares[j - 1],
                     "normalized_exponent_range": exponent_ranges[j - 1]}
            for j in (1, 2, 3)}}
        result_rows.append(row)
        norms.append(sums)
        # A complete group survives later budget failures.
        write_json(OUT / ("partial-sums-m%d.json" % m), row)
        log["completed_bernstein_groups"] = m + 1
        log["norm_square_files"] = list(artifact_records)
        progress(log, "BERNSTEIN_GROUP_COMPLETE", bernstein=m, terms=COUNT * 3)
        del vectors, b, squared, archive
    cchi = max(abs(x) for x in chi)
    maximum = [[max(norms[m][j][side] for m in range(4)) for side in (0, 1)]
               for j in range(3)]
    sqrt2_lo, sqrt2_hi, _, _ = root_interval(F(2))
    sqrt3_lo, sqrt3_hi, _, _ = root_interval(F(3))
    sigma = (2 * cchi + maximum[0][0] * sqrt2_lo / 2,
             2 * cchi + maximum[0][1] * sqrt2_hi / 2)
    mj = {str(j): interval(2 * cchi * sqrt3_lo + maximum[j - 1][0],
                           2 * cchi * sqrt3_hi + maximum[j - 1][1]) for j in (2, 3)}
    return {
        "schema": "independent-fraction-one-segment-upper-v1",
        "mathematical_status": "FIXED_REFERENCE_SINGLE_SEGMENT_DERIVATIVE_UPPER_ONLY",
        "segment": [["1280", "2048"], ["1281", "2048"]],
        "config_sha256": log["config_sha256"], "input_file_sha256": INPUTS,
        "source_sha256": log["source_sha256"], "checkout": log["checkout"],
        "chi": [pair(x) for x in chi], "C_chi": pair(cchi), "bernstein": result_rows,
        "max_A_intervals": {str(j): interval(*maximum[j - 1]) for j in (1, 2, 3)},
        "sqrt2": interval(sqrt2_lo, sqrt2_hi), "sqrt3": interval(sqrt3_lo, sqrt3_hi),
        "sigma_envelope_expression": interval(*sigma), "M_envelope_expression": mj,
        "interval_meaning": "Upper endpoints bound actual sigma_v/M_j throughout this one segment; lower endpoints bound only the envelope expression, never the actual field norm.",
        "norm_square_files": artifact_records,
        "constraints": {"all_four_projected_tables": True, "all_four_v_and_b": True,
                        "full_signed_modes": COUNT, "chi_component_removed": True},
        "limitations": ["No residual r0/r2 bound", "No other time segment",
                        "No control comparison or global NS conclusion",
                        "No main implementation/output used", "No new physical initial datum"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--run", action="store_true")
    mode.add_argument("--check-only", action="store_true")
    parser.add_argument("--approved-source-sha256")
    parser.add_argument("--code-review-file")
    parser.add_argument("--code-review-sha256")
    args = parser.parse_args()
    try:
        require(sys.version_info >= (3, 10), "Python >=3.10 is the supported audited entry")
        require(ROOT == Path("/Users/kasifa/Documents/Math/navier-stokes-reverse"), "WRONG_TREE")
        check_sources(SOURCES)
        for relative in INPUTS:
            require((HERE / relative).is_file(), "MISSING_INPUT: " + relative)
        own_sha = file_sha(Path(__file__).resolve())
        require(not OUT.exists(), "EXCLUSIVE_DIRECTORY_EXISTS_NO_RETRY")
        if not args.run:
            print(json.dumps({"status": "STARTUP_PREFLIGHT_PASS_NOT_RUN", "script_sha256": own_sha,
                              "config_sha256": sha_bytes(canonical(CONFIG)), "output_exists": False,
                              "node_arrays_loaded": False, "mathematics_executed": False}, sort_keys=True))
            return 0
        require(args.approved_source_sha256 == own_sha, "APPROVED_SOURCE_SHA_REQUIRED")
        require(args.code_review_file is not None and args.code_review_sha256 is not None,
                "ROOT_CODE_REVIEW_REQUIRED")
        review = Path(args.code_review_file).resolve()
        require(review.parent == HERE and review.suffix == ".md", "REVIEW_PATH_MUST_BE_LOCAL_MD")
        require(file_sha(review) == args.code_review_sha256, "REVIEW_HASH")
        require(own_sha.encode("ascii") in review.read_bytes(), "REVIEW_DOES_NOT_BIND_SCRIPT")
        bindings = {**SOURCES, Path(__file__).name: own_sha, review.name: args.code_review_sha256}
        identity = checkout()
        # No run directory before every preceding startup requirement has passed.
        OUT.mkdir(exist_ok=False)
    except (AuditFailure, OSError, subprocess.SubprocessError) as exc:
        print(json.dumps({"status": "STARTUP_REFUSED", "error": str(exc)}, ensure_ascii=False),
              file=sys.stderr, flush=True)
        return 2
    log = {"schema": "independent-fraction-single-segment-run-v1", "status": "CLAIMED",
           "started_at_utc": utc(), "pid": os.getpid(), "working_directory": str(ROOT),
           "command_argv": list(getattr(sys, "orig_argv", [sys.executable] + sys.argv)),
           "source_sha256": bindings, "input_file_sha256": INPUTS,
           "config": CONFIG, "config_sha256": sha_bytes(canonical(CONFIG)), "checkout": identity,
           "completed_bernstein_groups": 0, "output_files": [],
           "budget_semantics": "Observed overruns cannot COMPLETE; not OS prevention of transient over-allocation."}
    finished = False
    result = None
    try:
        # Atomic directory claim prevents both overwrite and same-task concurrent runs.
        write_json(OUT / "claim.json", {"pid": os.getpid(), "script_sha256": own_sha,
                                        "started_at_utc": log["started_at_utc"], "retry": False})
        remaining = WALL - (time.perf_counter() - START)
        if remaining <= 0:
            raise BudgetStop("STARTUP_EXHAUSTED_WALL_BUDGET")
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.setitimer(signal.ITIMER_REAL, remaining)
        import numpy as np
        log["environment"] = environment(np)
        progress(log, "INPUT_VERIFICATION_START")
        result = compute(np, log)
        log["output_files"].append(write_json(OUT / "result.json", result))
        check_sources(bindings)
        check_sources(INPUTS)
        require(checkout() == identity, "CHECKOUT_CHANGED_DURING_RUN")
        # Re-read all complete group files, including those written earlier.
        for record in result["norm_square_files"]:
            path = OUT / record["file"]
            require(file_sha(path) == record["sha256"], "FINAL_ARCHIVE_HASH")
            decoded = gzip.decompress(path.read_bytes())
            require(sha_bytes(decoded) == record["canonical_json_sha256"], "FINAL_CANONICAL_HASH")
            parsed = json.loads(decoded)
            require(len(parsed["norm_square"]) == COUNT, "FINAL_GROUP_COUNT")
            require(parsed["bernstein"] in range(4), "FINAL_GROUP_INDEX")
        require(json.loads((OUT / "result.json").read_bytes()) == result, "FINAL_RESULT_READBACK")
        progress(log, "ALL_DATA_VERIFIED")
        log["status"] = "DATA_VERIFIED_FINALIZING"
        finished = True
    except BaseException as exc:
        log["status"] = "BUDGET_STOP" if isinstance(exc, BudgetStop) else "FAILED_PRESERVED"
        log["error"] = {"type": type(exc).__name__, "message": str(exc)}
    finally:
        try:
            signal.setitimer(signal.ITIMER_REAL, 0)
        except BaseException as exc:
            # A one-shot deadline can arrive just as finalization begins.
            log["status"] = "BUDGET_STOP" if isinstance(exc, BudgetStop) else "FAILED_PRESERVED"
            log["error"] = {"type": type(exc).__name__, "message": str(exc)}
            finished = False
            signal.setitimer(signal.ITIMER_REAL, 0)
    # Metadata is finalized outside the alarm, but measured afterwards. An overrun
    # here changes status to BUDGET_STOP; finalization cannot inherit a stale PASS.
    try:
        log["finished_at_utc"] = utc()
        log["final_budget_observation"] = observation()
        if over_budget(log["final_budget_observation"]):
            log["status"] = "BUDGET_STOP"
        elif finished:
            log["status"] = "COMPLETE_FIXED_SEGMENT_INDEPENDENT_UPPER"
        write_json(OUT / "run.json", log)
        run_digest = file_sha(OUT / "run.json")
        post = observation()
        if over_budget(post):
            log["status"] = "BUDGET_STOP"
            log["post_write_budget_observation"] = post
            write_json(OUT / "run.json", log)
            run_digest = file_sha(OUT / "run.json")
            post = observation()
        print(json.dumps({"status": log["status"], "run_sha256": run_digest,
                          "post_write_budget_observation": post,
                          "output_directory": str(OUT)}, sort_keys=True), flush=True)
        return 0 if log["status"] == "COMPLETE_FIXED_SEGMENT_INDEPENDENT_UPPER" else 1
    except BaseException as exc:
        print(json.dumps({"status": "FINALIZATION_FAILED_PRESERVED", "error": str(exc),
                          "output_directory": str(OUT)}, ensure_ascii=False), file=sys.stderr, flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
