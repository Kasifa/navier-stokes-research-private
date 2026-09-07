#!/usr/bin/env python3
"""Five full direct tensors + exact per-mode Fraction residual, one fixed node.

Reads only original data and previously certified independent tensor12/centers.
Default/check-only hashes inputs but never loads scientific arrays or runs kernels.
"""
import time

START = time.perf_counter()

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import gzip
import hashlib
import json
import math
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
OUT = HERE / "full-nodal-independent-trial-01"
COUNT, OUTPUT_COUNT = 4912, 35937
Q52, Q96 = 1 << 52, 1 << 96
SCALAR_LIMIT, OUTPUT_LIMIT = 1 << 109, 1 << 235
BITS, ROOT_BITS = 8192, 128
WALL, RSS_CAP, ARCHIVE_CAP, RESERVE = 60.0, 256 << 20, 64 << 20, 256 << 10
PROGRESS_ROWS = 128
NEW_TENSORS = ((0, 0), (0, 2), (1, 1), (1, 2), (2, 2))
OLD = "kronecker-direct-independent-trial-01/"
ORIGINAL_CONFIG_SHA = "7649e366ee0fba6c5a051f0eecb45fc387a8bf91bc4bd06befa7e444e409f047"
INPUTS = {
    "node-trial-01/manifest.json": "5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd",
    "node-trial-01/modes.npy": "f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896",
    "node-trial-01/block-01280-01343.npz": "abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e",
    "kronecker-direct-independent-trial-01/centers-independent.i112le.bin": "c16d26dcbea14b63614d192da27a8b268fa49e689a02fb15499601cc1b611c9e",
    "kronecker-direct-independent-trial-01/tensor12-direct.i240le.bin": "795ce995481d41b1fd4c6810101b62d37b187a268eaba992e97ef6f3f79ca0e6",
    "kronecker-direct-independent-trial-01/rounding-witnesses.json.gz": "637e467edbb178fa25e8f05cb5dcf9bc48a299fce2350e930153b6367007333c",
    "kronecker-direct-independent-trial-01/run.json": "e4d54cf0690702f54029b4c36412d9d922e14a632090e5a4ac88f2e8b8e293e7",
    "kronecker-direct-independent-trial-01/result.json": "af998444847ef90696cc5e18fb716d60f2625748a98d2d11438e0f73b009853f",
    "kronecker-independent-agreement.json": "5510285fed346165e428bac4dfcb572548283322937a712be6465829481b5779",
}
SOURCES = {
    "FULL_NODAL_RESIDUAL_CONTRACT.md": "f3c5327e59931a2e638c039078f78175f4138c53eec139cc57c1ae5fd2cb513b",
    "FULL_NODAL_RESIDUAL_INDEPENDENT_REVIEW.md": "5a1341a58a93582b31a56a33d10a296499ed921daa2c5dac7ee9d27369c87ece",
    "FULL_NODAL_EXECUTION_INDEPENDENT_REVIEW.md": "5f1c40039f8de23250ef103c16e2991535dadaa4824c4f05e8cc045c75b55e53",
    "FULL_NODAL_INDEPENDENT_EXECUTION_CONTRACT.md": "61450a286e2f300f4444a29b45fa53fe93ec1b655fab3b4f03afb4261e93307c",
    "CONTINUOUS_RESIDUAL_COST_PREFLIGHT.md": "0c7ea4b3d33d152f298058a909e446505150d1004529f1a4518c2e1fedc7f796",
    "C1_RESIDUAL_CONTRACT.md": "a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251",
    "audit_kronecker_direct_independent.py": "057951051c5aeaf6d70d2d232811fd84731a6d81f32782156fdae30b48f9a499",
}
CONFIG = {
    "kind": "BLIND_FULL_NODAL_FRACTION_RESIDUAL", "node": 1280,
    "time": [1280, 2048], "viscosity": 1, "G_count": COUNT, "H_count": OUTPUT_COUNT,
    "QP": str(Q96), "root_bits": ROOT_BITS, "residual_scalar_num_bytes": 32,
    "residual_scalar_den_bytes": 32, "residual_array_bytes": OUTPUT_COUNT * 6 * 64,
    "new_tensors_one_based": [[a + 1, b + 1] for a, b in NEW_TENSORS],
    "reused_tensor": "12", "new_ordered_pairs": 5 * COUNT * COUNT,
    "new_scalar_multiplications": 20 * COUNT * COUNT, "zero_skipping": False,
    "original_reconstruction": "independent Fraction conjugate average + exact P_k",
    "residual": "Fraction d+s*c+i*P_kF/QP^2; no common A/J/V denominator",
    "norms": "exact Fraction Parseval sums from all readback residual components",
    "epsilon2": ["1", "5000000"], "epsilon0": ["1", "320000000"],
    "exp": "x=5/4; S32 lower, S32+term33/(1-5/136) upper",
    "main_new_source_or_output_read": False, "FFT": False,
    "packed_convolution": False, "integration": False, "compute_lcm": False,
    "progress_rows": PROGRESS_ROWS, "wall_seconds": WALL, "rss_bytes": RSS_CAP,
    "archive_bytes": ARCHIVE_CAP, "metadata_reserve_bytes": RESERVE,
    "integer_bit_limit": BITS, "retry": False,
}
THREAD_KEYS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
               "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS",
               "OMP_DYNAMIC", "MKL_DYNAMIC")

# Infrastructure and project_fraction copied from the pinned, previously reviewed independent direct script.
# No runtime import or scientific reuse of its execution path.

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


def fp(x):
    checked(x)
    return [str(x.numerator), str(x.denominator)]


def read_fraction(value):
    must(isinstance(value, list) and len(value) == 2, "FRACTION_SCHEMA")
    n, d = int(value[0]), int(value[1])
    must(d > 0, "FRACTION_POSITIVE_DENOMINATOR")
    return checked(Fraction(n, d))


def k_from_index(index):
    return (index % 33 - 16, (index // 33) % 33 - 16, index // 1089 - 16)


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
    spec = manifest["modes"]
    must(ma.dtype.str == spec["dtype"] == "<i8", "MODES_DTYPE")
    must(list(ma.shape) == spec["shape"] == [COUNT, 3], "MODES_SHAPE")
    must(array_sha(ma) == spec["array_sha256"], "MODES_ARRAY_SHA")
    modes = [tuple(int(x) for x in row) for row in ma]
    expected = [(x, y, z) for x in range(-8, 9) for y in range(-8, 9)
                for z in range(-8, 9) if (x, y, z) != (0, 0, 0)]
    must(modes == expected, "MODE_ORDER_OR_SUPPORT")
    blocks = [b for b in manifest["blocks"] if b["file"] == "block-01280-01343.npz"]
    must(len(blocks) == 1, "BLOCK_UNIQUENESS")
    bd = blocks[0]
    must((bd["first_node"], bd["last_node"], bd["node_count"]) == (1280, 1343, 64), "BLOCK_RANGE")
    rows, checks = {}, {}
    with np.load(HERE / "node-trial-01/block-01280-01343.npz", allow_pickle=False) as block:
        must(set(block.files) == set(bd["arrays"]), "BLOCK_KEYS")
        for name in sorted(block.files):
            arr = block[name]
            desc = bd["arrays"][name]
            must(arr.dtype.str == desc["dtype"] == "<i8", "ARRAY_DTYPE: " + name)
            must(list(arr.shape) == desc["shape"] and arr.nbytes == desc["nbytes"], "ARRAY_SHAPE_SIZE: " + name)
            digest = array_sha(arr)
            must(digest == desc["data_sha256"], "ARRAY_DATA_SHA: " + name)
            checks[name] = {"data_sha256": digest, "dtype": arr.dtype.str,
                            "shape": list(arr.shape), "nbytes": arr.nbytes}
            if name in ("value_q52", "slope_q52"):
                must(arr.shape == (64, COUNT, 3, 2), "VALUE_SLOPE_SHAPE")
                rows["c" if name == "value_q52" else "d"] = arr[0].copy()
            elif name in ("node_index", "time_numerator"):
                must([int(x) for x in arr] == list(range(1280, 1344)), "NODE_TIME_SEQUENCE")
            elif name == "time_denominator":
                must(arr.shape == (1,) and int(arr[0]) == 2048, "TIME_DENOMINATOR")
            elif name == "quantization_denominator":
                must(arr.shape == (1,) and int(arr[0]) == Q52, "Q52_DENOMINATOR")
            else:
                raise Failure("UNEXPECTED_ARRAY")
            del arr
            budget()
    must(set(rows) == {"c", "d"}, "MISSING_ORIGINAL_ROW")
    log["authenticated_arrays"] = checks
    log["mode_array_sha256"] = spec["array_sha256"]
    return modes, rows


def decode_signed(path, rows, columns, width, limit):
    data = path.read_bytes()
    must(len(data) == rows * columns * width, "SIGNED_ARRAY_LENGTH")
    result = []
    for i in range(rows):
        row = []
        for a in range(columns):
            pos = (i * columns + a) * width
            x = int.from_bytes(data[pos:pos + width], "little", signed=True)
            must(abs(x) < limit, "SIGNED_ARRAY_BOUND")
            row.append(x)
        result.append(tuple(row))
    return result


def validate_tensor(real, imag):
    must(len(real) == len(imag) == OUTPUT_COUNT, "TENSOR_LENGTH")
    for i in range(OUTPUT_COUNT):
        must(abs(real[i]) < OUTPUT_LIMIT and abs(imag[i]) < OUTPUT_LIMIT, "TENSOR_BOUND")
        other = OUTPUT_COUNT - 1 - i
        must(real[i] == real[other] and imag[i] == -imag[other], "TENSOR_CONJUGACY")
    must(imag[17968] == 0, "TENSOR_ZERO_IMAG")


def prepare_inputs(np, log):
    modes, raw = load_original(np, log)
    oldrun = json.loads((HERE / OLD / "run.json").read_bytes())
    oldresult = json.loads((HERE / OLD / "result.json").read_bytes())
    must(oldrun["status"] == "COMPLETE_DIRECT_GAUSSIAN_INDEPENDENT", "OLD_RUN_STATUS")
    must(oldresult["ordered_pairs"] == COUNT * COUNT and oldresult["output_count"] == OUTPUT_COUNT,
         "OLD_COMPLETE_TENSOR_COUNT")
    must(int(oldresult["tensor_denominator"]) == Q96 * Q96, "OLD_TENSOR_DENOMINATOR")
    centers = decode_signed(HERE / OLD / "centers-independent.i112le.bin", COUNT, 6, 14, SCALAR_LIMIT)
    witness_raw = gzip.decompress((HERE / OLD / "rounding-witnesses.json.gz").read_bytes())
    must(sha(witness_raw) == "e4a5d2d7ca0deca0260714bfcb76731edcf5703360ebebf70a7f1250ba8ae214", "OLD_WITNESS_CANONICAL_SHA")
    witness = json.loads(witness_raw)
    must(witness["node"] == 1280 and len(witness["entries"]) == COUNT, "WITNESS_NODE_OR_COUNT")
    positions = {k: i for i, k in enumerate(modes)}
    opposite = [positions[tuple(-x for x in k)] for k in modes]
    c, d = [], []
    M, delta = Fraction(0), Fraction(0)
    for i, k in enumerate(modes):
        cv = project_fraction(raw["c"], i, opposite[i], k)
        dv = project_fraction(raw["d"], i, opposite[i], k)
        c.append(cv)
        d.append(dv)
        must(len(witness["entries"][i]) == 6, "WITNESS_COMPONENTS")
        for a in range(6):
            n, den, q, r, rounded = map(int, witness["entries"][i][a])
            must(den > 0 and 0 <= r < den and n == q * den + r, "WITNESS_DIVISION")
            must(checked(Fraction(n, den)) == cv[a] * Q96, "WITNESS_ORIGINAL_FRACTION")
            must(rounded == centers[i][a], "WITNESS_FIXED_CENTER")
            chosen = q + int(2 * r > den or (2 * r == den and q % 2 != 0))
            must(chosen == rounded and 2 * abs(n - den * rounded) <= den, "WITNESS_TIES_EVEN")
            M = checked(M + abs(cv[a]))
            delta = checked(delta + abs(cv[a] - Fraction(rounded, Q96)))
        if (i + 1) % 512 == 0 or i + 1 == COUNT:
            progress(log, "ORIGINAL_VALUE_AND_SLOPE", completed_modes=i + 1)
    for i, k in enumerate(modes):
        for table in (c, d):
            for ri in range(2):
                must(sum((k[a] * table[i][2*a+ri] for a in range(3)), Fraction(0)) == 0,
                     "ORIGINAL_DIVERGENCE")
            for a in range(3):
                must(table[i][2*a] == table[opposite[i]][2*a] and
                     table[i][2*a+1] == -table[opposite[i]][2*a+1], "ORIGINAL_CONJUGACY")
        for a in range(3):
            must(centers[i][2*a] == centers[opposite[i]][2*a] and
                 centers[i][2*a+1] == -centers[opposite[i]][2*a+1], "CENTER_CONJUGACY")
    E = {j: checked((28 ** (j + 1)) * (2 * M * delta + delta * delta)) for j in (0, 2)}
    must(M < (1 << 28) and delta < Fraction(1, 1 << 82), "INPUT_PERTURBATION_PRIOR_BOUNDS")
    must(E[0] < Fraction(1, 1 << 47) and E[2] < Fraction(1, 1 << 37), "E_PRIOR_BOUNDS")
    agreement = json.loads((HERE / "kronecker-independent-agreement.json").read_bytes())
    must(agreement["status"] == "PASS_ACTUAL_BLIND_DIRECT_ALL_PAIR_RECONSTRUCTION_AND_COMPLETE_COMPARISON", "OLD_AGREEMENT_STATUS")
    comp = agreement["comparison"]
    must(M == read_fraction(comp["M_from_independent_witnesses"]), "M_AGREEMENT")
    must(delta == read_fraction(comp["delta_from_independent_witnesses"]), "DELTA_AGREEMENT")
    must(E[0] == read_fraction(comp["E0"]) and E[2] == read_fraction(comp["E2"]), "E_AGREEMENT")
    log["input_connection"] = {"M": fp(M), "delta": fp(delta), "E0": fp(E[0]), "E2": fp(E[2]),
                               "rechecked_witnesses": COUNT * 6, "original_c_d_exact_constraints": True,
                               "old_center_reused": True, "old_tensor12_recomputed": False}
    old_tensor = decode_signed(HERE / OLD / "tensor12-direct.i240le.bin", OUTPUT_COUNT, 2, 30, OUTPUT_LIMIT)
    t12 = ([row[0] for row in old_tensor], [row[1] for row in old_tensor])
    validate_tensor(*t12)
    return modes, positions, centers, c, d, E, {(0, 1): t12}


def new_tensor(pair, modes, centers, log, state):
    a, b = pair
    name = str(a + 1) + str(b + 1)
    exponents = [(k[0]+8) + 33*(k[1]+8) + 1089*(k[2]+8) for k in modes]
    left = [(exponents[i], row[2*a], row[2*a+1]) for i, row in enumerate(centers)]
    right = [(exponents[i], row[2*b], row[2*b+1]) for i, row in enumerate(centers)]
    real, imag = [0] * OUTPUT_COUNT, [0] * OUTPUT_COUNT
    state.update({"tensor": name, "real": real, "imag": imag, "completed_rows": 0})
    started = time.perf_counter()
    progress(log, "NEW_TENSOR_START", tensor=name)
    for row, (ep, u, v) in enumerate(left):
        for eq, x, y in right:
            index = ep + eq
            real[index] += u * x - v * y
            imag[index] += u * y + v * x
        state["completed_rows"] = row + 1
        if (row + 1) % PROGRESS_ROWS == 0 or row + 1 == COUNT:
            progress(log, "NEW_TENSOR_ROWS", tensor=name, completed_rows=row + 1,
                     completed_pairs=(row + 1) * COUNT, tensor_wall_seconds=time.perf_counter()-started)
    validate_tensor(real, imag)
    record = scalar_binary(OUT / ("tensor%s-direct.i240le.bin" % name), list(zip(real, imag)), 30, OUTPUT_LIMIT)
    record.update({"tensor": name, "ordered_pairs": COUNT * COUNT,
                   "scalar_multiplications": 4 * COUNT * COUNT,
                   "wall_seconds_including_archive": time.perf_counter() - started})
    log["output_files"].append(record)
    log["completed_new_tensors"].append(name)
    state.clear()
    progress(log, "NEW_TENSOR_COMPLETE", tensor=name)
    return real, imag


def residual_vector(index, k, s, tensors, positions, c, d):
    if s == 0:
        return (Fraction(0),) * 6
    f = []
    for ell in range(3):
        f.append(tuple(sum(k[j] * tensors[tuple(sorted((j, ell)))][ri][index]
                           for j in range(3)) for ri in range(2)))
    dots = [sum(k[j] * f[j][ri] for j in range(3)) for ri in range(2)]
    # Direct Fraction application of P_k. No common V or global denominator.
    pf = [[checked(Fraction(f[a][ri]) - Fraction(k[a] * dots[ri], s))
           for ri in range(2)] for a in range(3)]
    for ri in range(2):
        must(sum((k[a] * pf[a][ri] for a in range(3)), Fraction(0)) == 0, "P_F_DIVERGENCE")
    original = positions.get(k)
    cv = (Fraction(0),) * 6 if original is None else c[original]
    dv = (Fraction(0),) * 6 if original is None else d[original]
    values = []
    for a in range(3):
        values.append(checked(dv[2*a] + s * cv[2*a] - pf[a][1] / (Q96 * Q96)))
        values.append(checked(dv[2*a+1] + s * cv[2*a+1] + pf[a][0] / (Q96 * Q96)))
    for ri in range(2):
        must(sum((k[a] * values[2*a+ri] for a in range(3)), Fraction(0)) == 0, "R_HAT_DIVERGENCE")
    for value in values:
        must(abs(value.numerator) < (1 << 253) and value.denominator < (1 << 202), "R_HAT_STORAGE_BOUND")
        must((s << 192) % value.denominator == 0, "R_HAT_LOCAL_DENOMINATOR_DIVISIBILITY")
    return tuple(values)


def residual_archive_and_norms(tensors, positions, c, d, log):
    target = OUT / "residual-hat-fractions.i256-u256le.bin"
    temporary = target.with_name(target.name + ".partial")
    digest = hashlib.sha256()
    with temporary.open("wb") as stream:
        for index in range(OUTPUT_COUNT):
            k = k_from_index(index)
            s = sum(x*x for x in k)
            vals = residual_vector(index, k, s, tensors, positions, c, d)
            chunk = b"".join(value.numerator.to_bytes(32, "little", signed=True) +
                             value.denominator.to_bytes(32, "little", signed=False) for value in vals)
            stream.write(chunk)
            digest.update(chunk)
            if (index + 1) % 1024 == 0 or index + 1 == OUTPUT_COUNT:
                stream.flush()
                progress(log, "FRACTION_RESIDUAL_WRITE", completed_outputs=index + 1)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, target)
    raw = target.read_bytes()
    must(len(raw) == OUTPUT_COUNT * 6 * 64 == 13799808, "R_HAT_FILE_SIZE")
    must(sha(raw) == digest.hexdigest(), "R_HAT_WRITE_READBACK_SHA")
    norm0, norm2 = Fraction(0), Fraction(0)
    peak_n_bits = peak_d_bits = 0
    for index in range(OUTPUT_COUNT):
        k = k_from_index(index)
        s = sum(x*x for x in k)
        ss = Fraction(0)
        other = OUTPUT_COUNT - 1 - index
        for component in range(6):
            start = (index * 6 + component) * 64
            n = int.from_bytes(raw[start:start+32], "little", signed=True)
            den = int.from_bytes(raw[start+32:start+64], "little", signed=False)
            must(abs(n) < (1 << 253) and 0 < den < (1 << 202), "R_READBACK_BOUND")
            value = checked(Fraction(n, den))
            must(value.numerator == n and value.denominator == den, "R_READBACK_REDUCED")
            reverse = (other * 6 + component) * 64
            nn = int.from_bytes(raw[reverse:reverse+32], "little", signed=True)
            dd = int.from_bytes(raw[reverse+32:reverse+64], "little", signed=False)
            must(den == dd and n == (nn if component % 2 == 0 else -nn), "R_READBACK_CONJUGACY")
            if s == 0:
                must(n == 0 and den == 1, "R_ZERO_MODE")
            ss = checked(ss + value * value)
        norm0 = checked(norm0 + ss)
        norm2 = checked(norm2 + (s*s) * ss)
        peak_n_bits = max(peak_n_bits, norm0.numerator.bit_length(), norm2.numerator.bit_length())
        peak_d_bits = max(peak_d_bits, norm0.denominator.bit_length(), norm2.denominator.bit_length())
        if (index + 1) % 1024 == 0 or index + 1 == OUTPUT_COUNT:
            progress(log, "EXACT_FRACTION_NORM_READBACK", completed_outputs=index + 1)
    must((1 << 384) % norm2.denominator == 0, "NORM2_POWER_TWO_DENOMINATOR")
    record = {"file": target.name, "bytes": len(raw), "sha256": sha(raw),
              "scalar_count": 6 * OUTPUT_COUNT, "numerator_width": 32, "denominator_width": 32,
              "every_fraction_parsed_reduced_and_conjugate": True,
              "norms_computed_from_actual_readback": True}
    log["output_files"].append(record)
    log["norm_fraction_peak_bits"] = {"numerator": peak_n_bits, "denominator": peak_d_bits}
    return {0: norm0, 2: norm2}, record


def root_interval(value):
    checked(value)
    must(value >= 0, "NEGATIVE_ROOT_INPUT")
    n, den = value.numerator << (2 * ROOT_BITS), value.denominator
    must(n.bit_length() <= BITS, "ROOT_SHIFT_BIT_GUARD")
    ell = math.isqrt(n // den)
    lower_square = ell * ell * den
    next_square = (ell + 1) * (ell + 1) * den
    must(max(lower_square.bit_length(), next_square.bit_length()) <= BITS, "ROOT_SQUARE_BIT_GUARD")
    must(lower_square <= n < next_square, "TRUE_RATIONAL_ROOT_BOUND")
    upper = ell + int(lower_square != n)
    lo, hi = Fraction(ell, 1 << ROOT_BITS), Fraction(upper, 1 << ROOT_BITS)
    must(lo * lo <= value <= hi * hi, "ROOT_SQUARED_CHECK")
    return lo, hi, {"input": fp(value), "bits": ROOT_BITS, "scaled_numerator": str(n),
                    "denominator": str(den), "floor_root": str(ell), "ceil_root": str(upper),
                    "lower": fp(lo), "upper": fp(hi), "true_rational_equality": ell * ell * den == n}


def exponential_bounds():
    x = Fraction(5, 4)
    term = total = Fraction(1)
    for n in range(1, 33):
        term = checked(term * x / n)
        total = checked(total + term)
    term33 = checked(term * x / 33)
    upper = checked(total + term33 / (1 - Fraction(5, 136)))
    return total, upper, {"x": fp(x), "terms_through_degree": 32,
                           "lower": fp(total), "upper": fp(upper), "term33": fp(term33),
                           "tail_ratio_upper": ["5", "136"]}


def final_intervals(norms, E):
    exp_lo, exp_hi, exponent = exponential_bounds()
    results = {}
    for j, eps in ((0, Fraction(1, 320000000)), (2, Fraction(1, 5000000))):
        h_lo, h_hi, root = root_interval(norms[j])
        lo, hi = max(Fraction(0), checked(h_lo - E[j])), checked(h_hi + E[j])
        lower_product, upper_product = checked(lo * exp_lo), checked(hi * exp_hi)
        rejected, accepted = lower_product > eps, upper_product <= eps
        must(not (rejected and accepted), "CONTRADICTORY_GATE")
        results[str(j)] = {"center_norm_square": fp(norms[j]), "center_root": root,
                           "E": fp(E[j]), "original_residual_lower": fp(lo),
                           "original_residual_upper": fp(hi), "epsilon": fp(eps),
                           "lower_times_exp_lower": fp(lower_product),
                           "upper_times_exp_upper": fp(upper_product),
                           "gate": "REFUTED" if rejected else "NODE_PASS" if accepted else "UNDECIDED"}
    return results, exponent


def perform(np, log, state):
    modes, positions, centers, c, d, E, tensors = prepare_inputs(np, log)
    progress(log, "OLD_C_T12_CONNECTED_NO_T12_RECOMPUTATION")
    for pair in NEW_TENSORS:
        tensors[pair] = new_tensor(pair, modes, centers, log, state)
    must(set(tensors) == {(0,0), (0,1), (0,2), (1,1), (1,2), (2,2)}, "SIX_TENSORS_REQUIRED")
    norms, residual_file = residual_archive_and_norms(tensors, positions, c, d, log)
    intervals, exponent = final_intervals(norms, E)
    result = {"schema": "full-nodal-independent-fraction-result-v1",
              "mathematical_status": "ONE_FIXED_REFERENCE_NODAL_RESIDUAL_BOUNDS",
              "new_main_comparison": "NOT_READ_OR_PERFORMED", "node": 1280,
              "time": ["1280", "2048"], "viscosity": 1,
              "new_ordered_pairs": 5 * COUNT * COUNT, "new_scalar_multiplications": 20 * COUNT * COUNT,
              "new_tensors": list(log["completed_new_tensors"]), "reused_tensor12": True,
              "norm_square": {str(j): fp(norms[j]) for j in (0,2)},
              "residual_file": residual_file, "intervals": intervals, "exponential": exponent,
              "input_connection": log["input_connection"], "input_sha256": INPUTS,
              "source_sha256": log["source_sha256"], "checkout": log["checkout"],
              "config_sha256": log["config_sha256"], "output_files": list(log["output_files"]),
              "scope": "One reference node only; no continuous residual/control, no NS trajectory/global/singularity certificate."}
    log["output_files"].append(json_file(OUT / "result.json", result))
    for record in log["output_files"]:
        must(file_sha(OUT / record["file"]) == record["sha256"], "FINAL_OUTPUT_SHA")
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
        must(sys.version_info >= (3,10), "SUPPORTED_PYTHON_3_10_REQUIRED")
        must(ROOT == Path("/Users/kasifa/Documents/Math/navier-stokes-reverse"), "WRONG_TREE")
        check_bindings(SOURCES)
        check_bindings(INPUTS)
        own_sha = file_sha(Path(__file__).resolve())
        must(not OUT.exists(), "EXCLUSIVE_DIRECTORY_EXISTS_NO_RETRY")
        if not args.run:
            print(json.dumps({"status": "STARTUP_PREFLIGHT_PASS_NOT_RUN", "script_sha256": own_sha,
                              "config_sha256": sha(canonical(CONFIG)), "pins_checked": len(INPUTS)+len(SOURCES),
                              "node_arrays_loaded": False, "scientific_kernel_executed": False,
                              "output_exists": False}, sort_keys=True))
            return 0
        must(args.approved_source_sha256 == own_sha, "APPROVED_SOURCE_SHA_REQUIRED")
        must(args.code_review_file is not None and args.code_review_sha256 is not None, "ROOT_CODE_REVIEW_REQUIRED")
        review = Path(args.code_review_file).resolve()
        must(review.parent == HERE and review.suffix == ".md", "LOCAL_CODE_REVIEW_MD_REQUIRED")
        must(re.fullmatch(r"[0-9a-f]{64}", args.code_review_sha256) is not None, "REVIEW_SHA_FORMAT")
        must(file_sha(review) == args.code_review_sha256, "REVIEW_SHA_MISMATCH")
        must(own_sha.encode("ascii") in review.read_bytes(), "REVIEW_DOES_NOT_BIND_SCRIPT")
        bindings = {**SOURCES, Path(__file__).name: own_sha, review.name: args.code_review_sha256}
        identity = checkout()
        OUT.mkdir(exist_ok=False)
    except (Failure, OSError, subprocess.SubprocessError) as exc:
        print(json.dumps({"status": "STARTUP_REFUSED", "error": str(exc)}, ensure_ascii=False), file=sys.stderr, flush=True)
        return 2
    log = {"schema": "full-nodal-independent-run-v1", "status": "CLAIMED",
           "started_at_utc": utc(), "pid": os.getpid(), "working_directory": str(ROOT),
           "command_argv": list(getattr(sys,"orig_argv",[sys.executable]+sys.argv)),
           "source_sha256": bindings, "input_sha256": INPUTS, "checkout": identity,
           "config": CONFIG, "config_sha256": sha(canonical(CONFIG)),
           "completed_new_tensors": [], "output_files": [],
           "budget_semantics": "Observed overruns cannot COMPLETE; not OS prevention of transient overallocation."}
    state, complete = {}, False
    try:
        json_file(OUT / "claim.json", {"pid": os.getpid(), "source_sha256": own_sha,
                                       "started_at_utc": log["started_at_utc"], "retry": False})
        remaining = WALL - (time.perf_counter()-START)
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
        log["status"] = "COST_NOT_PAID" if isinstance(exc,BudgetStop) else "FAILED_PRESERVED"
        log["error"] = {"type": type(exc).__name__, "message": str(exc)}
    finally:
        try:
            signal.setitimer(signal.ITIMER_REAL, 0)
        except BaseException as exc:
            log["status"] = "COST_NOT_PAID" if isinstance(exc,BudgetStop) else "FAILED_PRESERVED"
            log["error"] = {"type": type(exc).__name__, "message": str(exc)}
            complete = False
            signal.setitimer(signal.ITIMER_REAL, 0)
    if not complete and "real" in state:
        try:
            record = scalar_binary(OUT / ("partial-tensor%s-UNCERTIFIED.i240le.bin" % state["tensor"]),
                                   list(zip(state["real"],state["imag"])), 30, OUTPUT_LIMIT)
            record.update({"meaning": "Interrupted, may be within one real/imag pair; not certified or resumable.",
                           "fully_completed_rows": state["completed_rows"]})
            log["output_files"].append(record)
        except BaseException as exc:
            log["partial_preservation_error"] = {"type":type(exc).__name__, "message":str(exc)}
    try:
        log["finished_at_utc"] = utc()
        log["final_budget_observation"] = observed()
        if exceeds(log["final_budget_observation"]):
            log["status"] = "COST_NOT_PAID"
        elif complete:
            log["status"] = "COMPLETE_FULL_NODAL_INDEPENDENT"
        json_file(OUT / "run.json", log)
        digest = file_sha(OUT / "run.json")
        post = observed()
        if exceeds(post):
            log["status"] = "COST_NOT_PAID"
            log["post_write_budget_observation"] = post
            json_file(OUT / "run.json", log)
            digest = file_sha(OUT / "run.json")
            post = observed()
        print(json.dumps({"status":log["status"], "run_sha256":digest,
                          "post_write_budget_observation":post, "output_directory":str(OUT)},sort_keys=True),flush=True)
        return 0 if log["status"] == "COMPLETE_FULL_NODAL_INDEPENDENT" else 1
    except BaseException as exc:
        print(json.dumps({"status":"FINALIZATION_FAILED_PRESERVED", "error":str(exc),
                          "output_directory":str(OUT)}),file=sys.stderr,flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
