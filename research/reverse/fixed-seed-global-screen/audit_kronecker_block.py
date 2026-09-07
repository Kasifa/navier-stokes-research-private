#!/usr/bin/env python3
"""Prepare/execute one fixed exact Kronecker tensor block; default is read-only.

No FFT, integration, parameter search, other node or full NS residual.
Only explicit --run, after root source review, performs scientific arithmetic.
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
OUT = HERE / "kronecker-block-trial-01"
Q = 1 << 52
QP = 1 << 96
BASE = 1 << 240
HALF = BASE >> 1
INPUT_DIGITS = 17969
OUTPUT_DIGITS = 35937
INPUT_BYTES = 30 * INPUT_DIGITS
OUTPUT_BYTES = 30 * OUTPUT_DIGITS
PROOFS = {
    "CONTINUOUS_RESIDUAL_COST_PREFLIGHT.md": "0c7ea4b3d33d152f298058a909e446505150d1004529f1a4518c2e1fedc7f796",
    "CONTINUOUS_RESIDUAL_COST_ROOT_REVIEW.md": "4865cf0639e20bc6d8d6c2546e8382c08b59366814168ff2f0b309bc8ef4e5da",
}
ARCHIVE = {
    "node-trial-01/manifest.json": "5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a75c6f81622c1cd",
    "node-trial-01/modes.npy": "f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896",
    "node-trial-01/block-01280-01343.npz": "abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e",
}
CONFIG = {
    "node_index": 1280, "time_numerator": 1280, "time_denominator": 2048,
    "original_Q": Q, "center_Q": QP, "rounding": "nearest_integer_ties_to_even",
    "G_count": 4912, "cutoff": 8, "spatial_radix": 33, "coefficient_bits": 240,
    "input_digits": INPUT_DIGITS, "output_digits": OUTPUT_DIGITS,
    "components_one_based": [1, 2], "general_large_products": 3,
    "wall_seconds": 60, "peak_rss_bytes": 256 * 1024**2,
    "output_bytes": 8 * 1024**2, "metadata_reserve_bytes": 128 * 1024,
    "small_integer_bit_guard": 8192, "single_process": True,
    "FFT": False, "integration": False, "selection": False, "retry": False,
    "run_directory": str(OUT),
}


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("ascii")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for part in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(part)
    return h.hexdigest()


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def launch():
    argv = getattr(sys, "orig_argv", None)
    return {"command": shlex.join(argv or [sys.executable, *sys.argv]),
            "command_source": "sys.orig_argv" if argv else "reconstructed; interpreter flags unavailable",
            "python": sys.version, "executable": sys.executable}


def rational(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def preflight():
    if sys.version_info < (3, 10):
        raise RuntimeError("Python >=3.10 required; use bundled Python 3.12")
    source = Path(__file__).read_bytes()
    source.decode("ascii")
    compile(ast.parse(source), str(Path(__file__)), "exec")
    for filename, expected in PROOFS.items():
        if sha(HERE / filename) != expected:
            raise ValueError("approved proof SHA mismatch: " + filename)
    paths = [Path(__file__), HERE / "KRONECKER_BLOCK_CONTRACT.md", HERE / "C1_RESIDUAL_CONTRACT.md"]
    paths.extend(HERE / filename for filename in PROOFS)
    return {"status": "PREPARED_REQUIRES_ROOT_SOURCE_REVIEW_AND_EXPLICIT_RUN_INSTRUCTION",
            "scientific_execution": False, "config": CONFIG,
            "config_sha256": hashlib.sha256(canonical({"config": CONFIG, "proof_pins": PROOFS, "archive_pins": ARCHIVE})).hexdigest(),
            "source_sha256": {str(p): sha(p) for p in paths},
            "proof_pins": PROOFS, "archive_pins": ARCHIVE,
            "output_directory_exists": OUT.exists()}


class BudgetStop(RuntimeError):
    pass


def peak_rss():
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


def execute(info):
    OUT.mkdir(exist_ok=True)
    if any(OUT.iterdir()):
        raise FileExistsError("fixed trial directory has existing contents; retry/overwrite refused")
    started = time.perf_counter()
    with (OUT / "RUN_CLAIM.json").open("x") as stream:
        json.dump({"started_at_utc": utc(), "pid": os.getpid(), "launch": launch()}, stream)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    record = {"execution_status": "RUNNING", "mathematical_status": "NOT_COMPUTED",
              "started_at_utc": utc(), "launch": launch(), "inputs": info,
              "maximum_small_integer_bits_observed": 0, "products": [], "artifacts": {},
              "resource_snapshot_semantics": "run.json resources are sampled before that atomic write; final stdout reports the actual post-write directory bytes and run.json SHA",
              "scope": "one c96 component-1/component-2 full tensor convolution; not the full conservative operator, Leray pressure, NS residual or trajectory"}

    def total_bytes():
        return sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())

    def observation():
        return {"wall_seconds": time.perf_counter() - started, "peak_rss_bytes": peak_rss(), "output_bytes": total_bytes()}

    def exceeded(obs):
        return (obs["wall_seconds"] >= CONFIG["wall_seconds"] or obs["peak_rss_bytes"] > CONFIG["peak_rss_bytes"]
                or obs["output_bytes"] > CONFIG["output_bytes"])

    def check():
        obs = observation()
        if exceeded(obs):
            raise BudgetStop("observed resource limit exceeded: " + json.dumps(obs))

    def small_guard(*values):
        bits = max((abs(x).bit_length() for x in values), default=0)
        record["maximum_small_integer_bits_observed"] = max(record["maximum_small_integer_bits_observed"], bits)
        if bits > CONFIG["small_integer_bit_guard"]:
            raise BudgetStop("small-integer arithmetic exceeded 8192 bits")

    def atomic(name, data, final_metadata=False):
        cap = CONFIG["output_bytes"] - (0 if final_metadata else CONFIG["metadata_reserve_bytes"])
        if total_bytes() + len(data) > cap:
            raise BudgetStop("output cap including atomic temporary and metadata reserve")
        temporary = OUT / (name + ".tmp")
        with temporary.open("wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(OUT / name)

    def checkpoint(final=False):
        record["resources"] = observation()
        atomic("run.json", canonical(record) + b"\n", final_metadata=final)

    def artifact(name, data, schema):
        check()
        atomic(name, data)
        reread = (OUT / name).read_bytes()
        expected = hashlib.sha256(data).hexdigest()
        if reread != data or hashlib.sha256(reread).hexdigest() != expected:
            raise AssertionError("actual binary archive readback failed: " + name)
        record["artifacts"][name] = {"bytes": len(data), "sha256": expected, "schema": schema, "actual_readback": "PASS"}
        check()
        return reread

    def stop(signum, frame):
        raise BudgetStop("deadline or external stop signal " + str(signum))

    for sig in (signal.SIGALRM, signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, stop)
    signal.setitimer(signal.ITIMER_REAL, 60)
    try:
        checkpoint()
        sys.dont_write_bytecode = True
        import numpy as np
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=WORKTREE, text=True, timeout=2).strip()
        if len(commit) != 40 or any(c not in "0123456789abcdef" for c in commit):
            raise ValueError("invalid reverse-worktree git HEAD")
        cpu = platform.processor()
        if sys.platform == "darwin":
            cpu = subprocess.check_output(["/usr/sbin/sysctl", "-n", "machdep.cpu.brand_string"], text=True, timeout=1).strip()
        record["source_commit"] = {"worktree": str(WORKTREE), "git_HEAD": commit, "individual_source_byte_hashes_remain_binding": True}
        record["environment"] = {"python": sys.version, "numpy": np.__version__, "numpy_path": np.__file__,
                                 "platform": platform.platform(), "cpu": cpu, "logical_cpu_count": os.cpu_count(),
                                 "thread_environment": {k: os.environ.get(k) for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS")},
                                 "arithmetic": "single-process Python arbitrary-precision int and Fraction; no workers; NumPy only reads/authenticates original int64 arrays"}
        for filename, expected in ARCHIVE.items():
            if sha(HERE / filename) != expected:
                raise ValueError("original archive SHA mismatch: " + filename)
            check()
        manifest = json.loads((HERE / "node-trial-01/manifest.json").read_text())
        if manifest["status"] != "CANDIDATE_NODES_COMPLETE_NOT_NS_CERTIFIED":
            raise ValueError("original archive was not complete")
        physical = {"scale": 1, "viscosity": 1, "rho": 1, "grid": 27, "cutoff": 8, "time_denominator": 2048,
                    "steps": 5120, "nodes": 5121, "quantization_denominator": Q}
        if any(manifest["config"].get(k) != v for k, v in physical.items()):
            raise ValueError("original fixed configuration mismatch")
        modes = [k for k in itertools.product(range(-8, 9), repeat=3) if k != (0, 0, 0)]
        mode_array = np.load(HERE / "node-trial-01/modes.npy", allow_pickle=False)
        if (mode_array.dtype.str != "<i8" or mode_array.shape != (4912, 3)
                or [tuple(int(x) for x in row) for row in mode_array] != modes):
            raise ValueError("full original signed mode order mismatch")
        if hashlib.sha256(memoryview(mode_array).cast("B")).hexdigest() != manifest["modes"]["array_sha256"]:
            raise ValueError("mode array data SHA mismatch")
        matches = [b for b in manifest["blocks"] if b["first_node"] <= 1280 <= b["last_node"]]
        if len(matches) != 1 or matches[0]["file"] != "block-01280-01343.npz":
            raise ValueError("unique node-1280 block mismatch")
        block = matches[0]
        encoded = None
        with np.load(HERE / "node-trial-01" / block["file"], allow_pickle=False) as archive:
            keys = {"node_index", "time_numerator", "time_denominator", "quantization_denominator", "value_q52", "slope_q52"}
            if set(archive.files) != keys or set(block["arrays"]) != keys:
                raise ValueError("original array key mismatch")
            for name in sorted(keys):
                array = archive[name]
                descriptor = {"shape": list(array.shape), "dtype": array.dtype.str, "nbytes": array.nbytes,
                              "data_sha256": hashlib.sha256(memoryview(array).cast("B")).hexdigest()}
                if descriptor != block["arrays"][name] or array.dtype.str != "<i8":
                    raise ValueError("original array authentication failed: " + name)
                if name in ("value_q52", "slope_q52"):
                    if array.shape != (64, 4912, 3, 2):
                        raise ValueError("unexpected coefficient array shape")
                    if name == "value_q52":
                        encoded = array[0].copy()
                elif name in ("node_index", "time_numerator"):
                    if array.tolist() != list(range(1280, 1344)):
                        raise ValueError("node/time sequence mismatch")
                elif array.tolist() != ([2048] if name == "time_denominator" else [Q]):
                    raise ValueError("original denominator mismatch")
                del array
                check()
        if encoded is None:
            raise ValueError("node value row missing")
        pos = {k: n for n, k in enumerate(modes)}
        opposite = [pos[tuple(-x for x in p)] for p in modes]
        squares = [sum(x*x for x in p) for p in modes]
        L = math.lcm(*squares)
        D = 2 * Q * L
        small_guard(L, D)
        exact = []
        center = []
        m_num = error_num = maximum_error_num = tie_count = 0
        for n, p in enumerate(modes):
            sums, differences = [], []
            for j in range(3):
                ar, ai = int(encoded[n, j, 0]), int(encoded[n, j, 1])
                br, bi = int(encoded[opposite[n], j, 0]), int(encoded[opposite[n], j, 1])
                if max(abs(ar), abs(ai), abs(br), abs(bi)) >= 1 << 63:
                    raise ValueError("original scalar violates strict int64 production bound")
                sums.append(ar + br)
                differences.append(ai - bi)
            sr = sum(p[j]*sums[j] for j in range(3))
            si = sum(p[j]*differences[j] for j in range(3))
            factor = L // squares[n]
            values = tuple(x for j in range(3) for x in (factor*(squares[n]*sums[j]-p[j]*sr), factor*(squares[n]*differences[j]-p[j]*si)))
            rounded = []
            for a in values:
                numerator = QP * a
                q, rem = divmod(numerator, D)
                c = q + int(2*rem > D or (2*rem == D and q % 2 != 0))
                err = abs(numerator - D*c)
                if 2*err > D or (2*rem == D and c % 2):
                    raise AssertionError("ties-to-even rounding bound failed")
                if abs(c) >= 1 << 109:
                    raise AssertionError("a priori center scalar width failed")
                tie_count += int(2*rem == D)
                m_num += abs(a)
                error_num += err
                maximum_error_num = max(maximum_error_num, err)
                small_guard(a, numerator, q, rem, c, err, m_num, error_num)
                rounded.append(c)
            exact.append(values)
            center.append(tuple(rounded))
            if n % 128 == 0:
                check()
        for n, p in enumerate(modes):
            a, other = exact[n], exact[opposite[n]]
            if any(sum(p[j]*a[2*j+d] for j in range(3)) for d in (0, 1)):
                raise AssertionError("original exact node divergence failed")
            for field in (exact, center):
                a, other = field[n], field[opposite[n]]
                if any(a[2*j] != other[2*j] or a[2*j+1] != -other[2*j+1] for j in range(3)):
                    raise AssertionError("full signed conjugacy failed")
        M = Fraction(m_num, D)
        delta = Fraction(error_num, D*QP)
        perturbation = 2*M*delta + delta*delta
        E0, E2 = 28*perturbation, 28**3*perturbation
        if not (M < 1 << 28 and delta < Fraction(1, 1 << 82) and E0 < Fraction(1, 1 << 47) and E2 < Fraction(1, 1 << 37)):
            raise AssertionError("fixed a priori input perturbation bounds failed")
        for r in (M, delta, E0, E2):
            small_guard(r.numerator, r.denominator)
        record["rounding_and_error"] = {
            "L": str(L), "D": str(D), "center_denominator": str(QP), "scalar_count": 29472,
            "ties_to_even_count": tie_count, "maximum_abs_rounding_error_numerator_over_D_Qp": str(maximum_error_num),
            "sum_abs_A": str(m_num), "sum_abs_QpA_minus_DC": str(error_num),
            "M": rational(M), "delta": rational(delta), "future_full_operator_E0": rational(E0), "future_full_operator_E2": rational(E2),
            "original_exact_divergence": "PASS", "original_and_center_full_conjugacy": "PASS",
            "center_divergence_not_assumed": True, "perturbation_is_not_a_residual_bound": True,
        }
        center_bytes = b"".join(c.to_bytes(14, "little", signed=True) for row in center for c in row)
        reread = artifact("c96-centers.i112le.bin", center_bytes, "4912 original-order modes; 3 components each real,imag; signed 14-byte little-endian integer; denominator 2^96")
        if any(int.from_bytes(reread[14*i:14*(i+1)], "little", signed=True) != c
               for i, c in enumerate(c for row in center for c in row)):
            raise AssertionError("rounded center integer readback failed")
        del encoded, mode_array, exact, center_bytes, reread
        exponents = [(p[0]+8)+33*(p[1]+8)+1089*(p[2]+8) for p in modes]

        def pack(component):
            positive = bytearray(INPUT_BYTES)
            negative = bytearray(INPUT_BYTES)
            for n, row in enumerate(center):
                value = row[component]
                target = positive if value >= 0 else negative
                offset = 30*exponents[n]
                target[offset:offset+30] = abs(value).to_bytes(30, "little")
            number = int.from_bytes(positive, "little") - int.from_bytes(negative, "little")
            if abs(number).bit_length() >= 8*INPUT_BYTES:
                raise AssertionError("packed input fixed signed width failed")
            check()
            return number

        def unpack(data, z_negative):
            if len(data) != OUTPUT_BYTES:
                raise AssertionError("raw product byte width failed")
            coefficients = []
            carry = 0
            for j in range(OUTPUT_DIGITS):
                r = int.from_bytes(data[30*j:30*(j+1)], "little")
                t = r + carry
                if t >= HALF:
                    value, carry = t - BASE, 1
                else:
                    value, carry = t, 0
                # t==BASE is allowed and gives value=0, carry=1.
                if abs(value) >= 1 << 233:
                    raise AssertionError("raw coefficient a priori bound failed")
                coefficients.append(value)
                if j % 512 == 0:
                    check()
            if carry != int(z_negative):
                raise AssertionError("nonzero terminal signed decoding quotient")
            return coefficients, carry

        U, V, X, Y = (pack(j) for j in (0, 1, 2, 3))
        pairs = [(U, X, "U*X"), (V, Y, "V*Y"), (U+V, X+Y, "(U+V)*(X+Y)")]
        del U, V, X, Y
        decoded = []
        checkpoint()
        for number, (left, right, label) in enumerate(pairs):
            check()
            input_descriptors = []
            for packed in (left, right):
                data = packed.to_bytes(INPUT_BYTES, "little", signed=True)
                input_descriptors.append({"signed_fixed_width_bytes": INPUT_BYTES, "sha256": hashlib.sha256(data).hexdigest(),
                                          "absolute_bit_length": abs(packed).bit_length(), "sign": (packed > 0)-(packed < 0)})
            del data
            record["next_product"] = {"index": number, "formula": label, "inputs": input_descriptors}
            checkpoint()
            check()
            multiplication_started = time.perf_counter()
            product = left * right
            multiplication_seconds = time.perf_counter() - multiplication_started
            check()
            if abs(product).bit_length() >= 8*OUTPUT_BYTES:
                raise AssertionError("raw product fixed signed width failed")
            data = product.to_bytes(OUTPUT_BYTES, "little", signed=True)
            filename = "product-" + str(number) + ".signed-le.bin"
            reread = artifact(filename, data, "one whole signed integer in fixed 1078110-byte little-endian two's-complement form; not balanced digit bytes")
            values, carry = unpack(reread, product < 0)
            decoded.append(values)
            record["products"].append({"index": number, "formula": label, "inputs": input_descriptors,
                                        "multiplication_wall_seconds": multiplication_seconds,
                                        "product_absolute_bit_length": abs(product).bit_length(), "product_negative": product < 0,
                                        "product_file": filename, "product_sha256": record["artifacts"][filename]["sha256"],
                                        "decoded_coefficients": OUTPUT_DIGITS, "terminal_carry": carry,
                                        "terminal_quotient": 0, "raw_coefficient_bound_strict_2pow233": "PASS"})
            del product, data, reread
            checkpoint()
            print(json.dumps({"kronecker_progress": {"completed_large_products": number+1, "wall_seconds": time.perf_counter()-started}}), flush=True)
        del pairs
        real = [a-b for a, b in zip(decoded[0], decoded[1], strict=True)]
        imag = [c-a-b for a, b, c in zip(decoded[0], decoded[1], decoded[2], strict=True)]
        del decoded
        for j in range(OUTPUT_DIGITS):
            if max(abs(real[j]), abs(imag[j])) >= 1 << 235:
                raise AssertionError("final tensor coefficient a priori bound failed")
            if real[j] != real[OUTPUT_DIGITS-1-j] or imag[j] != -imag[OUTPUT_DIGITS-1-j]:
                raise AssertionError("full output conjugacy failed")
            if j % 512 == 0:
                check()
        zero_re = zero_im = 0
        for n in range(4912):
            ar, ai = center[n][0:2]
            br, bi = center[opposite[n]][2:4]
            zero_re += ar*br-ai*bi
            zero_im += ar*bi+ai*br
        zero_index = 16+33*16+1089*16
        if (real[zero_index], imag[zero_index]) != (zero_re, zero_im) or zero_im != 0:
            raise AssertionError("independent full zero-frequency direct sum failed")
        record["zero_frequency_direct_check"] = {"ordered_terms": 4912, "physical_k": [0, 0, 0], "output_index": zero_index,
                                                   "real_numerator": str(zero_re), "imaginary_numerator": str(zero_im),
                                                   "denominator": str(QP*QP), "full_signed_direct_sum": "PASS"}
        tensor_bytes = b"".join(x.to_bytes(30, "little", signed=True) for pair in zip(real, imag, strict=True) for x in pair)
        reread = artifact("tensor12-complex.i240le.bin", tensor_bytes, "35937 outputs; index=(kx+16)+33*(ky+16)+1089*(kz+16); signed 30-byte real then imaginary; denominator 2^192")
        for j in range(OUTPUT_DIGITS):
            if (int.from_bytes(reread[60*j:60*j+30], "little", signed=True) != real[j]
                    or int.from_bytes(reread[60*j+30:60*j+60], "little", signed=True) != imag[j]):
                raise AssertionError("complete tensor integer readback failed")
            if j % 512 == 0:
                check()
        record["complete_tensor_checks"] = {"complex_output_count": OUTPUT_DIGITS, "full_conjugacy": "PASS",
                                             "coefficient_bound_strict_2pow235": "PASS", "actual_full_integer_readback": "PASS",
                                             "tensor_denominator": str(QP*QP), "large_products_executed": len(record["products"])}
        record.pop("next_product", None)
        record["execution_status"] = "RESULT_PENDING_FINAL_CHECKS"
        record["mathematical_status"] = "ONE_FIXED_COMPLEX_TENSOR_BLOCK_VERIFIED"
        checkpoint()
        if json.loads((OUT / "run.json").read_text()) != record:
            raise AssertionError("result JSON actual readback failed")
        for path, expected in info["source_sha256"].items():
            if sha(Path(path)) != expected:
                raise ValueError("source bytes changed during execution")
        for path, expected in ARCHIVE.items():
            if sha(HERE / path) != expected:
                raise ValueError("original archive changed during execution")
        check()
        record["execution_status"] = "VERIFIED_FINALIZING"
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL, 0)
        record["execution_status"] = "BUDGET_STOP" if isinstance(exc, BudgetStop) else "FAILED"
        record["mathematical_status"] = "COST_NOT_PAID"
        record["error"] = {"type": type(exc).__name__, "message": str(exc)}
        print(json.dumps({"kronecker_stop": record["error"]}), file=sys.stderr, flush=True)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        record["finished_at_utc"] = utc()
        obs = observation()
        if exceeded(obs):
            record["execution_status"], record["mathematical_status"] = "BUDGET_STOP", "COST_NOT_PAID"
            record["final_budget_overrun"] = obs
        elif record["execution_status"] == "VERIFIED_FINALIZING":
            record["execution_status"] = "COMPLETE"
        checkpoint(final=True)
        result_sha = sha(OUT / "run.json")
        final_observation = observation()
        if record["execution_status"] == "COMPLETE" and exceeded(final_observation):
            record["execution_status"], record["mathematical_status"] = "BUDGET_STOP", "COST_NOT_PAID"
            record["final_budget_overrun"] = final_observation
            checkpoint(final=True)
            result_sha = sha(OUT / "run.json")
            final_observation = observation()
    print(json.dumps({"output": str(OUT / "run.json"), "sha256": result_sha,
                      "execution_status": record["execution_status"], "mathematical_status": record["mathematical_status"],
                      "final_observation": final_observation}, sort_keys=True), flush=True)
    return 0 if record["execution_status"] == "COMPLETE" else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--run", action="store_true")
    mode.add_argument("--describe", action="store_true")
    mode.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    try:
        info = preflight()
        if args.run:
            return execute(info)
        print(json.dumps(info, sort_keys=True, indent=2))
        return 0
    except Exception as exc:
        print(json.dumps({"execution_status": "STARTUP_REFUSED_OR_UNRECOVERABLE_IO", "launch": launch(),
                          "error": {"type": type(exc).__name__, "message": str(exc)}}), file=sys.stderr, flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
