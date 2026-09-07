#!/usr/bin/env python3
"""One fixed full nodal residual. Default: static and input-byte preflight only.

Explicit --run requires root review and a bound independent mathematical review.
No FFT, integration, new node, parameter search, or continuous-time conclusion.
"""
from __future__ import annotations

import argparse
import ast
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
import shlex
import signal
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
WORKTREE = HERE.parents[2]
OUT = HERE / "full-nodal-residual-trial-01"
Q = 1 << 52
QP = 1 << 96
ROOT_SCALE = 1 << 128
BASE = 1 << 240
HALF = BASE >> 1
INPUT_BYTES = 30 * 17969
OUTPUT_COUNT = 35937
PRODUCT_BYTES = 30 * OUTPUT_COUNT
NEW_PAIRS = ((0, 0), (0, 2), (1, 1), (1, 2), (2, 2))
MATH_REVIEW = {
    "file": "FULL_NODAL_RESIDUAL_INDEPENDENT_REVIEW.md",
    "sha256": "5a1341a58a93582b31a56a33d10a296499ed921daa2c5dac7ee9d27369c87ece",
}
PROOFS = {
    "C1_RESIDUAL_CONTRACT.md": "a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251",
    "CONTINUOUS_RESIDUAL_COST_PREFLIGHT.md": "0c7ea4b3d33d152f298058a909e446505150d1004529f1a4518c2e1fedc7f796",
    "CONTINUOUS_RESIDUAL_COST_ROOT_REVIEW.md": "4865cf0639e20bc6d8d6c2546e8382c08b59366814168ff2f0b309bc8ef4e5da",
    "FULL_NODAL_RESIDUAL_CONTRACT.md": "f3c5327e59931a2e638c039078f78175f4138c53eec139cc57c1ae5fd2cb513b",
    "FULL_NODAL_EXECUTION_CONTRACT.md": "879deca7e881073dc3fc31506aaf681e7d243d068621092fe361fc60963ae40c",
    "FULL_NODAL_EXECUTION_INDEPENDENT_REVIEW.md": "5f1c40039f8de23250ef103c16e2991535dadaa4824c4f05e8cc045c75b55e53",
    "KRONECKER_COMPLETE_FINAL_REVIEW.md": "f72989cbc34a828132d317fb0f62277568fb8691ef582b501e483fdeb14c3b1f",
}
INPUTS = {
    "node-trial-01/manifest.json": "5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd",
    "node-trial-01/modes.npy": "f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896",
    "node-trial-01/block-01280-01343.npz": "abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e",
    "kronecker-block-trial-02/c96-centers.i112le.bin": "c16d26dcbea14b63614d192da27a8b268fa49e689a02fb15499601cc1b611c9e",
    "kronecker-block-trial-02/tensor12-complex.i240le.bin": "795ce995481d41b1fd4c6810101b62d37b187a268eaba992e97ef6f3f79ca0e6",
    "kronecker-block-trial-02/run.json": "375921aff0ceae1294b7d79947d9dfeaf817ad65ce9edc6c02b9b152ac922d70",
    "kronecker-direct-independent-trial-01/run.json": "e4d54cf0690702f54029b4c36412d9d922e14a632090e5a4ac88f2e8b8e293e7",
    "kronecker-independent-agreement.json": "5510285fed346165e428bac4dfcb572548283322937a712be6465829481b5779",
}
CONFIG = {
    "node_index": 1280, "time_numerator": 1280, "time_denominator": 2048,
    "original_Q": Q, "center_Q": QP, "root_fractional_bits": 128,
    "G_count": 4912, "H_count": OUTPUT_COUNT, "cutoff": 8,
    "new_tensor_pairs_one_based": [[i+1, j+1] for i, j in NEW_PAIRS],
    "reused_tensor_pair_one_based": [1, 2], "large_real_products": 15,
    "spatial_radix": 33, "coefficient_bits": 240,
    "A_J_scalar_bytes": 32, "V_scalar_bytes": 64, "S_scalar_bytes": 120,
    "expected_new_binary_bytes": 46951206,
    "exponential_argument": [5, 4], "exponential_Taylor_degree": 32,
    "old_epsilon": [2, 10000000], "r0_epsilon_divisor": 64,
    "wall_seconds": 60, "peak_rss_bytes": 256 * 1024**2,
    "output_bytes": 64 * 1024**2, "metadata_reserve_bytes": 256 * 1024,
    "small_integer_bit_guard": 8192, "single_process": True,
    "FFT": False, "integration": False, "selection": False, "retry": False,
    "run_directory": str(OUT),
}


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("ascii")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def check_pin(name, expected):
    if not isinstance(expected, str) or len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
        raise ValueError("pin is not 64 lowercase hex characters: " + name)
    if sha(HERE / name) != expected:
        raise ValueError("actual file SHA mismatch: " + name)


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def launch():
    argv = getattr(sys, "orig_argv", None)
    return {"command": shlex.join(argv or [sys.executable, *sys.argv]),
            "command_source": "sys.orig_argv" if argv else "reconstructed; interpreter flags unavailable",
            "python": sys.version, "executable": sys.executable}


def rat(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def preflight(for_run=False):
    if sys.version_info < (3, 10):
        raise RuntimeError("Python >=3.10 required; use bundled Python 3.12")
    source = Path(__file__).read_bytes()
    source.decode("ascii")
    compile(ast.parse(source), str(Path(__file__)), "exec")
    pins = {**PROOFS, **INPUTS}
    ready = all(MATH_REVIEW.values())
    if ready:
        pins[MATH_REVIEW["file"]] = MATH_REVIEW["sha256"]
    for name, expected in pins.items():
        check_pin(name, expected)
    if for_run and not ready:
        raise ValueError("independent full-node mathematical review is not bound; refusing before claim")
    sources = {str(HERE / name): expected for name, expected in PROOFS.items()}
    if ready:
        sources[str(HERE / MATH_REVIEW["file"])] = MATH_REVIEW["sha256"]
    for path in (Path(__file__), HERE / "FULL_NODAL_EXECUTION_CONTRACT.md"):
        sources[str(path)] = sha(path)
    return {"status": "READY_FOR_ROOT_SOURCE_REVIEW" if ready else "AWAITING_INDEPENDENT_MATH_REVIEW_BINDING",
            "scientific_execution": False, "all_available_fixed_pin_formats_and_actual_bytes": "PASS",
            "config": CONFIG, "math_review": MATH_REVIEW,
            "config_sha256": hashlib.sha256(canonical({"config": CONFIG, "proofs": PROOFS, "inputs": INPUTS, "math_review": MATH_REVIEW})).hexdigest(),
            "source_sha256": sources, "input_sha256": INPUTS, "output_directory_exists": OUT.exists()}


class BudgetStop(RuntimeError):
    pass


def peak_rss():
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


def execute(info, started):
    OUT.mkdir(exist_ok=True)
    if any(OUT.iterdir()):
        raise FileExistsError("fixed trial directory has contents; no overwrite or retry")
    with (OUT / "RUN_CLAIM.json").open("x") as stream:
        json.dump({"started_at_utc": utc(), "pid": os.getpid(), "launch": launch()}, stream)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    record = {"execution_status": "RUNNING", "mathematical_status": "NOT_COMPUTED", "launch": launch(),
              "started_at_utc": utc(), "inputs": info, "products": [], "tensor_results": [], "artifacts": {},
              "maximum_small_integer_bits_observed": 0,
              "resource_snapshot_semantics": "wall starts at main including pin preflight; run.json snapshot precedes its atomic write; final stdout contains post-write observations and run SHA",
              "scope": "one exact-reference nodal residual; no continuous-time or NS solution conclusion"}

    def directory_bytes():
        return sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())

    def observe():
        return {"wall_seconds": time.perf_counter()-started, "peak_rss_bytes": peak_rss(), "output_bytes": directory_bytes()}

    def exceeded(obs):
        return (obs["wall_seconds"] >= CONFIG["wall_seconds"] or obs["peak_rss_bytes"] > CONFIG["peak_rss_bytes"]
                or obs["output_bytes"] > CONFIG["output_bytes"])

    def check():
        obs = observe()
        if exceeded(obs):
            raise BudgetStop("observed fixed resource limit exceeded: " + json.dumps(obs))

    def guard(*values):
        bits = max((abs(x).bit_length() for x in values), default=0)
        record["maximum_small_integer_bits_observed"] = max(record["maximum_small_integer_bits_observed"], bits)
        if bits > 8192:
            raise BudgetStop("small arithmetic exceeded 8192-bit guard")

    def atomic(name, data, final=False):
        cap = CONFIG["output_bytes"] - (0 if final else CONFIG["metadata_reserve_bytes"])
        if directory_bytes()+len(data) > cap:
            raise BudgetStop("output cap including atomic temporary and metadata reserve")
        temporary = OUT / (name+".tmp")
        with temporary.open("wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(OUT / name)

    def checkpoint(final=False):
        record["resources"] = observe()
        atomic("run.json", canonical(record)+b"\n", final=final)

    def artifact(name, data, schema):
        check()
        atomic(name, data)
        reread = (OUT / name).read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if reread != data or hashlib.sha256(reread).hexdigest() != digest:
            raise AssertionError("actual binary archive readback failed: " + name)
        record["artifacts"][name] = {"bytes": len(data), "sha256": digest, "schema": schema, "actual_readback": "PASS"}
        check()
        return reread

    def tensor_checks(real, imag):
        if len(real) != OUTPUT_COUNT or len(imag) != OUTPUT_COUNT:
            raise AssertionError("tensor output count")
        for n in range(OUTPUT_COUNT):
            if max(abs(real[n]), abs(imag[n])) >= 1 << 235:
                raise AssertionError("tensor a priori coefficient width")
            opposite_index = OUTPUT_COUNT-1-n
            if real[n] != real[opposite_index] or imag[n] != -imag[opposite_index]:
                raise AssertionError("full tensor conjugacy")
            if n % 512 == 0:
                check()

    def stop(signum, frame):
        raise BudgetStop("deadline or external stop signal " + str(signum))

    for sig in (signal.SIGALRM, signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, stop)
    remaining = 60-(time.perf_counter()-started)
    if remaining > 0:
        signal.setitimer(signal.ITIMER_REAL, remaining)
    try:
        check()
        checkpoint()
        sys.dont_write_bytecode = True
        import numpy as np
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=WORKTREE, text=True, timeout=2).strip()
        if len(commit) != 40 or any(c not in "0123456789abcdef" for c in commit):
            raise ValueError("invalid reverse-worktree git HEAD")
        cpu = platform.processor()
        if sys.platform == "darwin":
            cpu = subprocess.check_output(["/usr/sbin/sysctl", "-n", "machdep.cpu.brand_string"], text=True, timeout=1).strip()
        record["source_commit"] = {"worktree": str(WORKTREE), "git_HEAD": commit, "individual_byte_hashes_remain_binding": True}
        record["environment"] = {"python": sys.version, "numpy": np.__version__, "numpy_path": np.__file__,
                                 "platform": platform.platform(), "cpu": cpu, "logical_cpu_count": os.cpu_count(),
                                 "thread_environment": {k: os.environ.get(k) for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS")},
                                 "arithmetic": "single-process Python int/isqrt/Fraction; NumPy only authenticates and decodes original int64 arrays"}
        manifest = json.loads((HERE / "node-trial-01/manifest.json").read_text())
        if manifest["status"] != "CANDIDATE_NODES_COMPLETE_NOT_NS_CERTIFIED":
            raise ValueError("original node archive completion status")
        physical = {"scale": 1, "viscosity": 1, "rho": 1, "grid": 27, "cutoff": 8,
                    "time_denominator": 2048, "steps": 5120, "nodes": 5121, "quantization_denominator": Q}
        if any(manifest["config"].get(k) != v for k, v in physical.items()):
            raise ValueError("fixed original physical configuration")
        modes = [p for p in itertools.product(range(-8, 9), repeat=3) if p != (0, 0, 0)]
        mode_array = np.load(HERE / "node-trial-01/modes.npy", allow_pickle=False)
        if (mode_array.dtype.str != "<i8" or mode_array.shape != (4912, 3)
                or [tuple(int(x) for x in row) for row in mode_array] != modes):
            raise ValueError("original signed mode order")
        if hashlib.sha256(memoryview(mode_array).cast("B")).hexdigest() != manifest["modes"]["array_sha256"]:
            raise ValueError("mode array data hash")
        matches = [b for b in manifest["blocks"] if b["first_node"] <= 1280 <= b["last_node"]]
        if len(matches) != 1 or matches[0]["file"] != "block-01280-01343.npz":
            raise ValueError("unique n1280 block")
        block = matches[0]
        raw = {}
        keys = {"node_index", "time_numerator", "time_denominator", "quantization_denominator", "value_q52", "slope_q52"}
        with np.load(HERE / "node-trial-01" / block["file"], allow_pickle=False) as archive:
            if set(archive.files) != keys or set(block["arrays"]) != keys:
                raise ValueError("original block keys")
            for name in sorted(keys):
                array = archive[name]
                descriptor = {"shape": list(array.shape), "dtype": array.dtype.str, "nbytes": array.nbytes,
                              "data_sha256": hashlib.sha256(memoryview(array).cast("B")).hexdigest()}
                if descriptor != block["arrays"][name] or array.dtype.str != "<i8":
                    raise ValueError("original array bytes/schema: " + name)
                if name in ("value_q52", "slope_q52"):
                    if array.shape != (64, 4912, 3, 2):
                        raise ValueError("original coefficient shape")
                    raw[name] = array[0].copy()
                elif name in ("node_index", "time_numerator"):
                    if array.tolist() != list(range(1280, 1344)):
                        raise ValueError("original node/time indices")
                elif array.tolist() != ([2048] if name == "time_denominator" else [Q]):
                    raise ValueError("original time/Q denominator")
                del array
                check()
        positions = {p: n for n, p in enumerate(modes)}
        opposite = [positions[tuple(-x for x in p)] for p in modes]
        squares = [sum(x*x for x in p) for p in modes]
        lcm = math.lcm(*squares)
        D = 2*Q*lcm
        if D >= 1 << 225:
            raise AssertionError("original common D a priori width")

        def decode(encoded):
            field = []
            for n, p in enumerate(modes):
                re, im = [], []
                for j in range(3):
                    ar, ai = int(encoded[n, j, 0]), int(encoded[n, j, 1])
                    br, bi = int(encoded[opposite[n], j, 0]), int(encoded[opposite[n], j, 1])
                    if max(abs(ar), abs(ai), abs(br), abs(bi)) >= 1 << 63:
                        raise ValueError("original strict int64 scalar bound")
                    re.append(ar+br)
                    im.append(ai-bi)
                dot_re = sum(p[j]*re[j] for j in range(3))
                dot_im = sum(p[j]*im[j] for j in range(3))
                factor = lcm//squares[n]
                value = tuple(x for j in range(3) for x in (factor*(squares[n]*re[j]-p[j]*dot_re), factor*(squares[n]*im[j]-p[j]*dot_im)))
                if max(abs(x) for x in value) >= 1 << 238:
                    raise AssertionError("A/J scalar a priori width")
                guard(*value)
                field.append(value)
                if n % 128 == 0:
                    check()
            for n, p in enumerate(modes):
                a, other = field[n], field[opposite[n]]
                if any(sum(p[j]*a[2*j+d] for j in range(3)) for d in (0, 1)):
                    raise AssertionError("original field exact divergence")
                if any(a[2*j] != other[2*j] or a[2*j+1] != -other[2*j+1] for j in range(3)):
                    raise AssertionError("original field conjugacy")
            return field

        A = decode(raw["value_q52"])
        J = decode(raw["slope_q52"])
        del raw, mode_array
        for name, field in (("A.i256le.bin", A), ("J.i256le.bin", J)):
            data = bytearray(4912*6*32)
            for n, row in enumerate(field):
                for j, value in enumerate(row):
                    offset = 32*(6*n+j)
                    data[offset:offset+32] = value.to_bytes(32, "little", signed=True)
            reread = artifact(name, data, "4912 original-G modes; three real,imag pairs; signed 32-byte little-endian numerator; denominator D")
            if any(int.from_bytes(reread[32*i:32*(i+1)], "little", signed=True) != x
                   for i, x in enumerate(x for row in field for x in row)):
                raise AssertionError("A/J full integer file readback")
            del data, reread
        center_data = (HERE / "kronecker-block-trial-02/c96-centers.i112le.bin").read_bytes()
        if len(center_data) != 4912*6*14:
            raise ValueError("reused center byte length")
        C = [tuple(int.from_bytes(center_data[14*(6*n+j):14*(6*n+j+1)], "little", signed=True) for j in range(6)) for n in range(4912)]
        del center_data
        m_num = delta_num = ties = 0
        for n, row in enumerate(A):
            for j, a in enumerate(row):
                q, rem = divmod(QP*a, D)
                expected = q+int(2*rem > D or (2*rem == D and q % 2 != 0))
                c = C[n][j]
                error = abs(QP*a-D*c)
                if c != expected or 2*error > D or (2*rem == D and c % 2 != 0) or abs(c) >= 1 << 109:
                    raise AssertionError("original A to reused C ties-to-even connection")
                m_num += abs(a)
                delta_num += error
                ties += int(2*rem == D)
                guard(QP*a, D*c, m_num, delta_num)
            other = C[opposite[n]]
            if any(C[n][2*j] != other[2*j] or C[n][2*j+1] != -other[2*j+1] for j in range(3)):
                raise AssertionError("reused center conjugacy")
            if n % 128 == 0:
                check()
        M, delta = Fraction(m_num, D), Fraction(delta_num, D*QP)
        E = {j: 28**(j+1)*(2*M*delta+delta*delta) for j in (0, 2)}
        agreement = json.loads((HERE / "kronecker-independent-agreement.json").read_text())
        if agreement["status"] != "PASS_ACTUAL_BLIND_DIRECT_ALL_PAIR_RECONSTRUCTION_AND_COMPLETE_COMPARISON":
            raise ValueError("reused exact agreement status")
        cmp = agreement["comparison"]
        if cmp["center_scalars_equal"] != 29472 or cmp["complex_outputs_equal"] != OUTPUT_COUNT:
            raise ValueError("reused agreement finite scope")
        comparisons = ((M, "M_from_independent_witnesses"), (delta, "delta_from_independent_witnesses"), (E[0], "E0"), (E[2], "E2"))
        for value, name in comparisons:
            if value != Fraction(*map(int, cmp[name])):
                raise AssertionError("independently connected reused perturbation mismatch: " + name)
            guard(value.numerator, value.denominator)
        record["original_node_and_center"] = {"L_lcm": str(lcm), "D": str(D), "A_J_modes": 4912, "original_divergence_and_conjugacy": "PASS",
                                               "reused_C_rounding_connection_scalars": 29472, "ties": ties,
                                               "M": rat(M), "delta": rat(delta), "E0": rat(E[0]), "E2": rat(E[2]),
                                               "reused_independent_M_delta_connection": "PASS", "center_divergence_not_assumed": True}
        t12_data = (HERE / "kronecker-block-trial-02/tensor12-complex.i240le.bin").read_bytes()
        if len(t12_data) != OUTPUT_COUNT*60:
            raise ValueError("reused T12 byte length")
        t12 = tuple([int.from_bytes(t12_data[60*n+30*d:60*n+30*(d+1)], "little", signed=True) for n in range(OUTPUT_COUNT)] for d in (0, 1))
        del t12_data
        tensor_checks(*t12)
        tensors = {(0, 1): t12}
        record["reused_T12"] = {"path": "kronecker-block-trial-02/tensor12-complex.i240le.bin", "convolution_recomputed": False,
                                "complete_outputs_read": OUTPUT_COUNT, "conjugacy": "PASS", "denominator": str(QP*QP)}
        exponents = [(p[0]+8)+33*(p[1]+8)+1089*(p[2]+8) for p in modes]

        def pack(component):
            positive, negative = bytearray(INPUT_BYTES), bytearray(INPUT_BYTES)
            for n, row in enumerate(C):
                value = row[component]
                destination = positive if value >= 0 else negative
                offset = 30*exponents[n]
                destination[offset:offset+30] = abs(value).to_bytes(30, "little")
            packed = int.from_bytes(positive, "little")-int.from_bytes(negative, "little")
            if abs(packed).bit_length() >= 8*INPUT_BYTES:
                raise AssertionError("fixed signed packed input width")
            check()
            return packed

        def unpack(data, negative):
            values, carry = [], 0
            for n in range(OUTPUT_COUNT):
                t = int.from_bytes(data[30*n:30*(n+1)], "little")+carry
                if t >= HALF:
                    value, carry = t-BASE, 1
                else:
                    value, carry = t, 0
                # t==BASE intentionally produces zero with carry one.
                if abs(value) >= 1 << 233:
                    raise AssertionError("raw convolution a priori coefficient bound")
                values.append(value)
                if n % 512 == 0:
                    check()
            if carry != int(negative):
                raise AssertionError("signed balanced unpack terminal quotient")
            return values, carry

        packed_components = [pack(j) for j in range(6)]
        for first, second in NEW_PAIRS:
            label = str(first+1)+str(second+1)
            record["active_tensor"] = label
            checkpoint()
            U, W = packed_components[2*first:2*first+2]
            X, Y = packed_components[2*second:2*second+2]
            pairs = ((U, X, "real*real"), (W, Y, "imag*imag"), (U+W, X+Y, "(real+imag)*(real+imag)"))
            decoded = []
            for index, (left, right, formula) in enumerate(pairs):
                descriptors = []
                for value in (left, right):
                    data = value.to_bytes(INPUT_BYTES, "little", signed=True)
                    descriptors.append({"signed_width_bytes": INPUT_BYTES, "sha256": hashlib.sha256(data).hexdigest(),
                                        "sign": (value > 0)-(value < 0), "absolute_bit_length": abs(value).bit_length()})
                del data
                record["next_product"] = {"tensor": label, "index": index, "inputs": descriptors}
                checkpoint()
                check()
                tick = time.perf_counter()
                product = left*right
                elapsed = time.perf_counter()-tick
                check()
                if abs(product).bit_length() >= 8*PRODUCT_BYTES:
                    raise AssertionError("fixed signed raw product width")
                data = product.to_bytes(PRODUCT_BYTES, "little", signed=True)
                filename = "tensor-"+label+"-product-"+str(index)+".signed-le.bin"
                reread = artifact(filename, data, "one whole signed fixed-width integer; 1078110 bytes little endian; not balanced coefficient bytes")
                values, carry = unpack(reread, product < 0)
                decoded.append(values)
                record["products"].append({"tensor": label, "index": index, "formula": formula, "inputs": descriptors,
                                           "multiplication_wall_seconds": elapsed, "product_file": filename,
                                           "product_sha256": record["artifacts"][filename]["sha256"],
                                           "product_absolute_bit_length": abs(product).bit_length(), "product_negative": product < 0,
                                           "terminal_carry": carry, "terminal_quotient": 0, "decoded_coefficients": OUTPUT_COUNT})
                del product, data, reread
                checkpoint()
            real = [a-b for a, b in zip(decoded[0], decoded[1], strict=True)]
            imag = [c-a-b for a, b, c in zip(decoded[0], decoded[1], decoded[2], strict=True)]
            del decoded, pairs
            tensor_checks(real, imag)
            direct_re = direct_im = 0
            for n in range(4912):
                ar, ai = C[n][2*first:2*first+2]
                br, bi = C[opposite[n]][2*second:2*second+2]
                direct_re += ar*br-ai*bi
                direct_im += ar*bi+ai*br
            if (real[17968], imag[17968]) != (direct_re, direct_im) or direct_im != 0:
                raise AssertionError("new tensor independent zero-frequency direct sum")
            data = bytearray(OUTPUT_COUNT*60)
            for n in range(OUTPUT_COUNT):
                data[60*n:60*n+30] = real[n].to_bytes(30, "little", signed=True)
                data[60*n+30:60*n+60] = imag[n].to_bytes(30, "little", signed=True)
            filename = "tensor-"+label+".i240le.bin"
            reread = artifact(filename, data, "35937 outputs kx-fastest in H; signed 30-byte real then imag; denominator 2^192")
            for n in range(OUTPUT_COUNT):
                if (int.from_bytes(reread[60*n:60*n+30], "little", signed=True) != real[n]
                        or int.from_bytes(reread[60*n+30:60*n+60], "little", signed=True) != imag[n]):
                    raise AssertionError("new tensor complete integer readback")
            del data, reread
            tensors[(first, second)] = (real, imag)
            record["tensor_results"].append({"pair_one_based": [first+1, second+1], "outputs": OUTPUT_COUNT,
                                             "conjugacy_and_width": "PASS", "integer_readback": "PASS",
                                             "zero_direct_ordered_terms": 4912, "zero_real_numerator": str(direct_re),
                                             "zero_imaginary_numerator": str(direct_im), "file": filename})
            record.pop("next_product", None)
            checkpoint()
            print(json.dumps({"full_node_progress": {"completed_new_tensors": len(record["tensor_results"]),
                                                      "completed_large_products": len(record["products"]), "wall_seconds": time.perf_counter()-started}}), flush=True)
        del packed_components
        record.pop("active_tensor", None)
        if len(record["products"]) != 15 or len(tensors) != 6:
            raise AssertionError("complete six-tensor/15-product scope")
        output_modes = [(x, y, z) for z in range(-16, 17) for y in range(-16, 17) for x in range(-16, 17)]
        V_bytes = bytearray(OUTPUT_COUNT*6*64)
        S_bytes = bytearray(OUTPUT_COUNT*120)
        first_S_sum = 0
        zero_vector = (0, 0, 0, 0, 0, 0)
        for index, k in enumerate(output_modes):
            s = sum(x*x for x in k)
            if s == 0:
                Lvec = Fvec = Nvec = Vvec = zero_vector
                S = 0
            else:
                original_index = positions.get(k)
                Lvec = zero_vector if original_index is None else tuple(J[original_index][d]+s*A[original_index][d] for d in range(6))
                Fvec = tuple(sum(k[j]*tensors[tuple(sorted((j, ell)))][d][index] for j in range(3)) for ell in range(3) for d in (0, 1))
                dot_F = tuple(sum(k[ell]*Fvec[2*ell+d] for ell in range(3)) for d in (0, 1))
                Nvec = tuple(s*Fvec[2*ell+d]-k[ell]*dot_F[d] for ell in range(3) for d in (0, 1))
                Vvec = tuple(x for ell in range(3) for x in (s*QP*QP*Lvec[2*ell]-D*Nvec[2*ell+1],
                                                            s*QP*QP*Lvec[2*ell+1]+D*Nvec[2*ell]))
                for vector, bits in ((Lvec, 246), (Fvec, 241), (Nvec, 252), (Vvec, 478)):
                    if max(abs(x) for x in vector) >= 1 << bits:
                        raise AssertionError("residual a priori vector scalar width: " + str(bits))
                    guard(*vector)
                for vector in (Lvec, Nvec, Vvec):
                    if any(sum(k[j]*vector[2*j+d] for j in range(3)) for d in (0, 1)):
                        raise AssertionError("complete k dot L/N/V identity")
                S = sum(x*x for x in Vvec)
            if S >= 1 << 959:
                raise AssertionError("S a priori unsigned width")
            for d, value in enumerate(Vvec):
                offset = 64*(6*index+d)
                V_bytes[offset:offset+64] = value.to_bytes(64, "little", signed=True)
            S_bytes[120*index:120*(index+1)] = S.to_bytes(120, "little")
            first_S_sum += S
            guard(S, first_S_sum)
            if index % 512 == 0 or index == OUTPUT_COUNT-1:
                check()
                record["residual_progress_outputs"] = index+1
                checkpoint()
                if index % 4096 == 0 or index == OUTPUT_COUNT-1:
                    print(json.dumps({"full_node_residual_progress": {"outputs": index+1, "wall_seconds": time.perf_counter()-started}}), flush=True)
        V_read = artifact("V.i512le.bin", V_bytes, "35937 kx-fastest H outputs; 3 real,imag pairs; signed 64-byte Gaussian numerator; zero mode zero; per-nonzero denominator D*|k|^2*QP^2")
        del V_bytes
        S_read = artifact("S.u960le.bin", S_bytes, "35937 kx-fastest H outputs; unsigned 120-byte |V|^2; zero mode zero")
        del S_bytes
        A2 = A0lo = A0hi = inexact = 0
        for index, k in enumerate(output_modes):
            s = sum(x*x for x in k)
            v = tuple(int.from_bytes(V_read[64*(6*index+d):64*(6*index+d+1)], "little", signed=True) for d in range(6))
            other_index = OUTPUT_COUNT-1-index
            other = tuple(int.from_bytes(V_read[64*(6*other_index+d):64*(6*other_index+d+1)], "little", signed=True) for d in range(6))
            S = int.from_bytes(S_read[120*index:120*(index+1)], "little")
            if S != sum(x*x for x in v):
                raise AssertionError("actual S readback versus full V squared norm")
            if any(v[2*j] != other[2*j] or v[2*j+1] != -other[2*j+1] for j in range(3)):
                raise AssertionError("actual full V readback conjugacy")
            if s == 0:
                if S or any(v):
                    raise AssertionError("exact zero residual mode")
            else:
                if any(sum(k[j]*v[2*j+d] for j in range(3)) for d in (0, 1)):
                    raise AssertionError("actual V readback divergence")
                q, remainder = divmod(S, s*s)
                A0lo += q
                A0hi += q+int(remainder != 0)
                inexact += int(remainder != 0)
                A2 += S
            if index % 512 == 0:
                check()
        if A2 != first_S_sum or A0hi-A0lo != inexact or not 0 <= inexact <= 35936:
            raise AssertionError("full readback aggregate integer sums")
        H0 = D*D*QP**4
        guard(A2, A0lo, A0hi, H0)

        def root_interval(integer):
            scaled = ROOT_SCALE*ROOT_SCALE*integer
            quotient, remainder = divmod(scaled, H0)
            lower = math.isqrt(quotient)
            upper = lower+int(lower*lower*H0 != scaled)
            if not (lower*lower*H0 <= scaled < (lower+1)*(lower+1)*H0 and scaled <= upper*upper*H0):
                raise AssertionError("fixed 128-bit rational square-root certificate")
            guard(scaled, quotient, remainder, lower*lower*H0, upper*upper*H0)
            return (Fraction(lower, ROOT_SCALE), Fraction(upper, ROOT_SCALE),
                    {"A": str(integer), "quotient": str(quotient), "remainder": str(remainder),
                     "lower_numerator": str(lower), "upper_numerator": str(upper), "denominator": str(ROOT_SCALE),
                     "exact_square_containment": "PASS"})

        r0lower = root_interval(A0lo)
        r0upper = root_interval(A0hi)
        r2root = root_interval(A2)
        centers = {0: (r0lower[0], r0upper[1]), 2: (r2root[0], r2root[1])}
        bounds = {j: (max(Fraction(0), centers[j][0]-E[j]), centers[j][1]+E[j]) for j in (0, 2)}
        x = Fraction(5, 4)
        term = partial = Fraction(1)
        for n in range(1, 33):
            term = term*x/n
            partial += term
        term33 = term*x/33
        ratio = x/34
        exponential_upper = partial+term33/(1-ratio)
        if not 0 < ratio < 1 or not partial < exponential_upper:
            raise AssertionError("fixed Taylor32 exponential tail")
        epsilon = Fraction(2, 10000000)
        gates = {}
        for j in (0, 2):
            target = epsilon if j == 2 else epsilon/64
            lo, hi = bounds[j]
            if lo*partial > target:
                verdict = "REFUTED_AT_FIXED_NODE"
            elif hi*exponential_upper <= target:
                verdict = "CERTIFIED_AT_FIXED_NODE"
            else:
                verdict = "UNDECIDED"
            gates[str(j)] = {"verdict": verdict, "target_coefficient": rat(target),
                             "lower_times_exp_lower": rat(lo*partial), "upper_times_exp_upper": rat(hi*exponential_upper),
                             "lower": rat(lo), "upper": rat(hi)}
            for value in (lo, hi, lo*partial, hi*exponential_upper):
                guard(value.numerator, value.denominator)
        record["exact_norm_certificates"] = {
            "H0": str(H0), "A2": str(A2), "A0_lower": str(A0lo), "A0_upper": str(A0hi),
            "noninteger_S_over_s_squared_count": inexact, "complete_nonzero_signed_outputs": 35936,
            "r0_squared_interval_width": rat(Fraction(inexact, H0)),
            "r0_lower_root": r0lower[2], "r0_upper_root": r0upper[2], "r2_root": r2root[2],
            "center_norm_intervals": {str(j): {"lower": rat(centers[j][0]), "upper": rat(centers[j][1])} for j in (0, 2)},
            "original_reference_norm_intervals": {str(j): {"lower": rat(bounds[j][0]), "upper": rat(bounds[j][1])} for j in (0, 2)},
            "complete_V_S_readback_and_projection_conjugacy": "PASS",
        }
        record["fixed_exponential_certificate"] = {"argument": rat(x), "degree": 32, "lower_P32": rat(partial),
                                                   "term33": rat(term33), "tail_ratio_upper": rat(ratio), "upper": rat(exponential_upper)}
        record["old_epsilon_node_gates"] = gates
        statuses = [gates[str(j)]["verdict"] for j in (0, 2)]
        record["old_epsilon_joint_node_verdict"] = ("REFUTED_AT_FIXED_NODE" if "REFUTED_AT_FIXED_NODE" in statuses
                                                     else "CERTIFIED_AT_FIXED_NODE" if all(s == "CERTIFIED_AT_FIXED_NODE" for s in statuses)
                                                     else "UNDECIDED")
        binary_size = sum(a["bytes"] for a in record["artifacts"].values())
        if binary_size != CONFIG["expected_new_binary_bytes"]:
            raise AssertionError("complete new binary archive size")
        record["actual_new_binary_bytes"] = binary_size
        record["execution_status"] = "RESULT_PENDING_FINAL_CHECKS"
        record["mathematical_status"] = "FULL_FIXED_NODE_RESIDUAL_BOUNDS_VERIFIED"
        checkpoint()
        if json.loads((OUT / "run.json").read_text()) != record:
            raise AssertionError("actual result JSON readback")
        for path, expected in info["source_sha256"].items():
            if sha(Path(path)) != expected:
                raise ValueError("source changed during execution")
        for name, expected in INPUTS.items():
            check_pin(name, expected)
            check()
        record["execution_status"] = "VERIFIED_FINALIZING"
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL, 0)
        record["execution_status"] = "BUDGET_STOP" if isinstance(exc, BudgetStop) else "FAILED"
        record["mathematical_status"] = "NOT_CERTIFIED"
        record["error"] = {"type": type(exc).__name__, "message": str(exc)}
        print(json.dumps({"full_node_stop": record["error"]}), file=sys.stderr, flush=True)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        record["finished_at_utc"] = utc()
        obs = observe()
        if exceeded(obs):
            record["execution_status"], record["mathematical_status"] = "BUDGET_STOP", "NOT_CERTIFIED"
            record["final_budget_overrun"] = obs
        elif record["execution_status"] == "VERIFIED_FINALIZING":
            record["execution_status"] = "COMPLETE"
        checkpoint(final=True)
        result_sha = sha(OUT / "run.json")
        final_observation = observe()
        if record["execution_status"] == "COMPLETE" and exceeded(final_observation):
            record["execution_status"], record["mathematical_status"] = "BUDGET_STOP", "NOT_CERTIFIED"
            record["final_budget_overrun"] = final_observation
            checkpoint(final=True)
            result_sha = sha(OUT / "run.json")
            final_observation = observe()
    print(json.dumps({"output": str(OUT / "run.json"), "sha256": result_sha,
                      "execution_status": record["execution_status"], "mathematical_status": record["mathematical_status"],
                      "final_observation": final_observation}, sort_keys=True), flush=True)
    return 0 if record["execution_status"] == "COMPLETE" else 1


def main():
    started = time.perf_counter()
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--run", action="store_true")
    mode.add_argument("--describe", action="store_true")
    mode.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    try:
        info = preflight(for_run=args.run)
        if args.run:
            return execute(info, started)
        print(json.dumps(info, sort_keys=True, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"execution_status": "STARTUP_REFUSED_OR_UNRECOVERABLE_IO", "launch": launch(),
                          "error": {"type": type(exc).__name__, "message": str(exc)}}), file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
