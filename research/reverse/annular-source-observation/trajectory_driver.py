"""One fixed exploratory annular trajectory; execution needs a separate gate.

No old worker is imported.  Each accepted step uses four full velocity-stage
callbacks and always computes both sources.  Finite sampled gates, preserved
arrays and numerical comparisons do not certify a true-NS trajectory or gate.
The supervisor owns timeout/RSS/whole-directory acceptance and byte-map checks.
Git source-commit verification belongs to the root's separate external gate.
This worker owns the full loop and its actual completion counts.
"""

import sys
sys.dont_write_bytecode = True

import argparse
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import time
import traceback


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/reverse/annular-source-observation/"
CONFIGS = {
    "trajectory128_256": (128, 42, 256),
    "trajectory160_256": (160, 53, 256),
    "trajectory128_512": (128, 42, 512),
    "trajectory160_512": (160, 53, 512),
}
FIXED = {
    "TRAJECTORY_CONTRACT.md":
        "0886f1f992e7a6285e02ffd3c48650dca197d9ced3c1f8bd21a021711307447b",
    "numerical_kernel.py":
        "1b29e919cf5faefe1e4a5193fee0f7e0fdd11901d8aed7b3e5ade752cd23f175",
    "input-preparation.json":
        "3f51705fbd934ce76d503c1c856566405ee3deb1760474b1c73ef6a6f481c61f",
    "input-acceptance.json":
        "dbd34732c073507b6162a273fcf1ff6100cc3f723c24487ede079fba3f22d827",
}
MIB = 1024 ** 2
# Leave one MiB of the 64 MiB statistics allowance for supervisor/stdio receipts.
WORKER_JSON_LIMIT = 63 * MIB


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(MIB), b""):
            digest.update(chunk)
    return digest.hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=True, allow_nan=False,
                       separators=(",", ":"), sort_keys=True) + "\n").encode("ascii")


def q(value):
    return Fraction(int(value["numerator"]), int(value["denominator"]))


def fraction_record(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def number_record(value, rounded=None):
    rounded = float(value) if rounded is None else rounded
    require(math.isfinite(rounded), "nonfinite time conversion")
    readback = Fraction.from_float(rounded)
    error = readback - value
    return {"exact": fraction_record(value), "float_hex": rounded.hex(),
            "readback": fraction_record(readback),
            "signed_conversion_error": fraction_record(error),
            "absolute_conversion_error": fraction_record(abs(error))}


def node_time(T, j, m, h_float):
    exact = j * T / m
    record = number_record(exact)
    accumulated = j * Fraction.from_float(h_float)
    record.update(step_accumulation_exact=fraction_record(accumulated),
                  step_accumulation_signed_error=fraction_record(accumulated - exact),
                  step_accumulation_absolute_error=fraction_record(abs(accumulated - exact)))
    return record


def load_lock(path):
    require(path.is_absolute() and path.is_file() and not path.is_symlink(),
            "source lock must be an absolute regular nonsymlink file")
    data = json.loads(path.read_text(encoding="utf-8"))
    require(data.get("schema") == 1 and isinstance(data.get("bindings"), list),
            "invalid source lock schema")
    expected = {}
    for row in data["bindings"]:
        name, digest = row["path"], row["sha256"]
        relative = PurePosixPath(name)
        require(isinstance(name, str) and not relative.is_absolute()
                and str(relative) == name and ".." not in relative.parts
                and "\\" not in name and name not in expected, "invalid source path")
        target = ROOT / name
        require(target.is_file() and not target.is_symlink()
                and target.resolve().is_relative_to(ROOT), "unsafe source binding")
        require(isinstance(digest, str) and len(digest) == 64
                and all(c in "0123456789abcdef" for c in digest), "invalid SHA-256")
        expected[name] = digest
    require(PREFIX + "trajectory_driver.py" in expected, "driver missing from source lock")
    for name, digest in FIXED.items():
        require(expected.get(PREFIX + name) == digest, "fixed source binding mismatch: " + name)
    return expected


def source_hashes(expected):
    return {name: sha256(ROOT / name) for name in expected}


class Journals:
    """Streaming scalar records, without retaining the trajectory in memory."""

    def __init__(self, directory):
        self.streams = {}
        self.counts = {}
        self.sizes = {}
        try:
            for name in ("nodes.jsonl", "progress.jsonl", "checkpoints.jsonl"):
                self.streams[name] = (directory / name).open("xb")
                self.counts[name] = self.sizes[name] = 0
        except BaseException:
            self.close()
            raise

    def write(self, name, value):
        data = json_bytes(value)
        require(sum(self.sizes.values()) + len(data) <= WORKER_JSON_LIMIT,
                "worker JSON budget exceeded")
        self.streams[name].write(data)
        self.streams[name].flush()
        self.counts[name] += 1
        self.sizes[name] += len(data)

    def close(self):
        for stream in self.streams.values():
            stream.close()


class FFTCounts:
    """Count actual NumPy API invocations, not a copied theoretical total."""

    def __init__(self, np, N):
        self.np = np
        self.originals = {}
        self.counts = {f"{kind}:{n}x{n}x{n}":
                       {"batched_api_calls": 0, "scalar_3d_transforms": 0}
                       for n in (32, 64, N) for kind in ("ifftn", "fftn")}

    def __enter__(self):
        for kind in ("ifftn", "fftn"):
            original = getattr(self.np.fft, kind)
            self.originals[kind] = original

            def counted(array, *args, _kind=kind, _original=original, **kwargs):
                require(not args and tuple(kwargs.get("axes", ())) == (1, 2, 3)
                        and kwargs.get("norm") == "forward", "unexpected FFT convention")
                require(array.ndim == 4 and array.shape[0] == 3
                        and array.shape[1:] == (array.shape[1],) * 3,
                        "unexpected FFT batch shape")
                n = array.shape[1]
                key = f"{_kind}:{n}x{n}x{n}"
                require(key in self.counts, "unexpected FFT work grid")
                self.counts[key]["batched_api_calls"] += 1
                self.counts[key]["scalar_3d_transforms"] += 3
                return _original(array, **kwargs)

            setattr(self.np.fft, kind, counted)
        return self

    def __exit__(self, *_):
        for kind, original in self.originals.items():
            setattr(self.np.fft, kind, original)

    def snapshot(self):
        return {key: dict(value) for key, value in self.counts.items()}

    def check_steps_since(self, before, steps):
        for key, value in self.counts.items():
            calls = (8 if key.startswith("ifftn:") else 4) * steps
            require(value["batched_api_calls"] - before[key]["batched_api_calls"] == calls
                    and value["scalar_3d_transforms"] - before[key]["scalar_3d_transforms"]
                    == 3 * calls, "FFT counts disagree with complete augmented steps")

    def totals(self):
        return {name: sum(row[name] for row in self.counts.values())
                for name in ("batched_api_calls", "scalar_3d_transforms")}


def add_scales(np, diagnostics, field, frequency, domain):
    maximum = float(np.max(np.abs(field)))
    coefficient, frequency = max(1.0, maximum), max(1.0, float(frequency))
    diagnostics.update(max_component_abs=maximum,
                       scale={"coefficient": coefficient, "frequency": frequency,
                              "frequency_domain": domain},
                       divergence_normalized=diagnostics["divergence_max_abs"]
                       / (coefficient * frequency),
                       conjugacy_normalized=diagnostics["conjugacy_component_max_abs"]
                       / coefficient,
                       c3_normalized=diagnostics["c3_component_max_abs"] / coefficient)
    return diagnostics


class CompactDiagnostics:
    def __init__(self, np, band, a0):
        self.np, self.band, self.a0 = np, band, a0
        lookup = {tuple(int(x) for x in mode): j for j, mode in enumerate(band.modes)}
        self.neg = np.array([lookup[tuple(-int(x) for x in mode)]
                             for mode in band.modes], dtype=np.int64)
        self.inverse_cycle = np.array([lookup[(int(mode[1]), int(mode[2]), int(mode[0]))]
                                       for mode in band.modes], dtype=np.int64)
        self.frequency = math.sqrt(int(np.max(np.sum(band.modes ** 2, axis=1))))

    def __call__(self, field):
        np, modes = self.np, self.band.modes
        require(field.dtype == np.dtype(np.complex128)
                and field.shape == (3, self.band.size), "compact state shape/dtype mismatch")
        diagnostics = {
            "finite": bool(np.all(np.isfinite(field))), "a0": self.a0(field),
            "mean_hermitian_norm": 0.0,  # Both complete bands exclude k=0.
            "divergence_max_abs": float(np.max(np.abs(np.sum(field * modes.T, axis=0)))),
            "conjugacy_component_max_abs": float(np.max(np.abs(
                field - np.conjugate(field[:, self.neg])))),
            "c3_component_max_abs": float(np.max(np.abs(
                field - field[[2, 0, 1], :][:, self.inverse_cycle]))),
        }
        return add_scales(np, diagnostics, field, self.frequency, "complete_band")


def normalization(K):
    return {"dtype": "complex128", "component_axis": 0, "fft_norm": "forward",
            "frequency_order": "signed_numpy_fft", "retained_cube": K,
            "band_order": "lexicographic_all_signed_integer_modes",
            "a0": "sum_hermitian_mode_norms",
            "energy": "normalized_fourier_half_l2_squared", "viscosity": 1}


def observe(np, system, compact_diagnostics, a0, state, T, h_float, j, m):
    U, G, W = state
    h0, h1, h2 = (band.gather(U) for band in system.bands)
    e1, e2 = h1 - G, h2 - W
    vectors = {"h0": h0, "h1": h1, "h2": h2, "G": G, "W": W,
               "e1": e1, "e2": e2}
    norms = {name: a0(field) for name, field in vectors.items()}
    nonzero = {name: bool(np.any(field != 0)) for name, field in vectors.items()}
    nonzero["U"] = bool(np.any(U != 0))
    F1 = norms["e1"] - norms["G"] / 4
    post = j >= m // 2
    F2 = norms["e2"] - norms["W"] / 4 if post else None
    first_nonzero = nonzero["G"] and nonzero["h1"]
    second_nonzero = nonzero["W"] and nonzero["h2"]
    flags = {
        "first_contract_applicable": post,
        "second_contract_endpoint_applicable": j == m,
        "second_window_started": post,
        "first_sampled_nonpositive": F1 <= 0 if post else None,
        "second_sampled_nonpositive": F2 <= 0 if post else None,
        "first_source_target_nonzero_float": first_nonzero if post else None,
        "second_source_target_nonzero_float": second_nonzero if post else None,
        "first_sampled_conditions_met": F1 <= 0 and first_nonzero if post else None,
        "second_sampled_conditions_met": F2 <= 0 and second_nonzero if post else None,
    }
    full_diagnostics = add_scales(np, system.grid.diagnostics(U), U,
                                  math.sqrt(3) * system.grid.K, "retained_cube")
    return {"j": j, "m": m, "time": node_time(T, j, m, h_float), "norms": norms,
            "F1": F1, "F2": F2, "U": full_diagnostics,
            "G": compact_diagnostics[0](G), "W": compact_diagnostics[1](W),
            "nonzero_float": nonzero, "gate_flags": flags,
            "e2_scope": "NUMERICAL_POST_SOURCE_WINDOW" if post else "PRE_SOURCE_WINDOW"}


def save_checkpoint(np, directory, journal, state, system, metadata):
    j = metadata["j"]
    filename = f"checkpoint-{j:06d}.npz"
    final, temporary = directory / filename, directory / (filename + ".tmp")
    require(not final.exists(), "checkpoint already exists")
    with temporary.open("xb") as stream:
        np.savez(stream, U=state[0], G=state[1], W=state[2],
                 band1_modes=system.bands[1].modes, band2_modes=system.bands[2].modes,
                 metadata_json=np.array(json_bytes(metadata).decode("ascii")))
        stream.flush()
        os.fsync(stream.fileno())
    size, digest = temporary.stat().st_size, sha256(temporary)
    require(size <= (128 if system.grid.N == 128 else 224) * MIB,
            "checkpoint byte budget exceeded; temporary file retained")
    # A same-directory hard-link publication is atomic and fails if final exists;
    # unlike POSIX rename/replace it cannot silently overwrite a prior checkpoint.
    os.link(temporary, final)
    temporary.unlink()
    record = {"j": j, "file": filename, "bytes": size, "sha256": digest}
    journal.write("checkpoints.jsonl", record)
    return record


def initial_state(np, system, input_data):
    modes = input_data["twelve_modes"]
    require(len(modes) == 12, "expected the original twelve input modes")
    U = np.zeros((3, system.grid.N, system.grid.N, system.grid.N), dtype=np.complex128)
    seen = set()
    for row in modes:
        mode = tuple(row["frequency"])
        require(len(mode) == 3 and all(type(k) is int for k in mode)
                and mode not in seen and max(map(abs, mode)) <= system.grid.K,
                "invalid or repeated initial mode")
        seen.add(mode)
        coefficients = [float.fromhex(value) for value in row["float_hex"]]
        require(len(coefficients) == 3 and len(row["coefficients"]) == 3
                and all(math.isfinite(value) for value in coefficients), "invalid input floats")
        require(all(Fraction.from_float(value) == q(exact)
                    for value, exact in zip(coefficients, row["coefficients"])),
                "input hex does not reproduce frozen dyadic coefficient")
        U[(slice(None),) + tuple(k % system.grid.N for k in mode)] = coefficients
    return (U, np.zeros((3, system.bands[1].size), dtype=np.complex128),
            np.zeros((3, system.bands[2].size), dtype=np.complex128))


def run(args, result, directory, journal, expected):
    # First scientific import is in the supervised worker's guarded lifecycle.
    import numpy as np
    from numerical_kernel import AnnularSystem, hermitian_a0, indexed_step

    N, K, m = CONFIGS[args.run_id]
    result["environment"] = {
        "python": sys.version, "executable": sys.executable, "sys_platform": sys.platform,
        "uname": list(os.uname()), "numpy_version": np.__version__, "numpy_file": np.__file__,
        "thread_environment": {key: os.environ.get(key) for key in
                               ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                                "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")},
    }
    input_data = json.loads((HERE / "input-preparation.json").read_text(encoding="utf-8"))
    acceptance = json.loads((HERE / "input-acceptance.json").read_text(encoding="utf-8"))
    require(acceptance.get("status") == "INPUT_VERIFIED", "input acceptance is not verified")
    require(any(row["path"] == PREFIX + "input-preparation.json"
                and row["sha256"] == FIXED["input-preparation.json"]
                for row in acceptance["files"]), "input acceptance binding mismatch")
    T = q(input_data["fixed_observation"]["T"])
    a, h_exact = T / 2, T / m
    require(T > 0 and q(input_data["fixed_observation"]["a"]) == a, "invalid fixed T/a")
    h_float = float(h_exact)
    require(math.isfinite(h_float) and h_float > 0, "invalid fixed step conversion")
    times = {"T": number_record(T), "a": number_record(a),
             "h": number_record(h_exact, h_float)}
    result.update(N=N, K=K, m=m, input_sha256=FIXED["input-preparation.json"],
                  normalization=normalization(K), **times)
    start = time.perf_counter()
    journal.write("progress.jsonl", {"event": "initialization_start", "elapsed_seconds": 0.0})
    system = AnnularSystem(N, K)
    compact = tuple(CompactDiagnostics(np, band, hermitian_a0) for band in system.bands[1:])
    state = initial_state(np, system, input_data)
    checkpoints, half_reset_count, rhs_calls = [], 0, 0
    result["artifacts"] = {"nodes": "nodes.jsonl", "progress": "progress.jsonl",
                           "checkpoints_index": "checkpoints.jsonl", "checkpoints": checkpoints}
    durations = {"initialization_seconds": time.perf_counter() - start,
                 "step_seconds": 0.0, "observation_seconds": 0.0, "checkpoint_seconds": 0.0}
    result["timings"] = durations

    def progress(event, **fields):
        journal.write("progress.jsonl", {"event": event,
                      "elapsed_seconds": time.perf_counter() - start, **fields})

    with FFTCounts(np, N) as counter:
        zero_counts = counter.snapshot()

        def record_node(j):
            before = time.perf_counter()
            require(all(np.all(np.isfinite(block)) for block in state), "nonfinite accepted state")
            node = observe(np, system, compact, hermitian_a0, state, T, h_float, j, m)
            journal.write("nodes.jsonl", node)
            result["node_count"] = journal.counts["nodes.jsonl"]
            durations["observation_seconds"] += time.perf_counter() - before
            if j in (0, m // 2, m):
                result[{0: "initial_node", m // 2: "half_node", m: "final_node"}[j]] = node
            if j % 32 == 0:
                before = time.perf_counter()
                metadata = {
                    "schema": 1, "run_id": args.run_id, "N": N, "K": K, "m": m, "j": j,
                    "input_sha256": FIXED["input-preparation.json"],
                    "source_lock_sha256": result["source_lock_sha256"],
                    **times, "time": node["time"],
                    "counters": {"accepted_steps": result["completed_steps"],
                                 "rhs_calls": rhs_calls, "fft_counts": counter.snapshot()},
                    "next_index": j,
                    "half_reset": {"count": half_reset_count, "performed": half_reset_count == 1,
                                   "due_at_next_step": j == m // 2,
                                   "next_phase": None if j == m else int(j >= m // 2)},
                    "normalization": normalization(K),
                    "journal_positions_before_checkpoint": {
                        "counts": dict(journal.counts), "bytes": dict(journal.sizes)},
                }
                checkpoint = save_checkpoint(np, directory, journal, state, system, metadata)
                checkpoints.append(checkpoint)
                result["checkpoint_count"] = journal.counts["checkpoints.jsonl"]
                if j in (0, m // 2, m):
                    key = {0: "initial_checkpoint", m // 2: "half_checkpoint",
                           m: "final_checkpoint"}[j]
                    result["artifacts"][key] = checkpoint
                durations["checkpoint_seconds"] += time.perf_counter() - before

        try:
            record_node(0)
            progress("initialization_complete", completed_steps=0, next_index=0,
                     phase=0, latest_checkpoint=checkpoints[-1], eta_seconds=None)
            for index in range(m):
                require(result["completed_steps"] == index, "nonsequential accepted-step index")
                phase, local_calls = int(index >= m // 2), 0
                before_counts, before_time = counter.snapshot(), time.perf_counter()
                if index == m // 2:
                    require(half_reset_count == 0 and not np.any(state[2] != 0),
                            "unexpected pre-reset W or duplicate reset")
                    # Entry is announced here; no completed reset is counted yet.
                    progress("half_reset_entry", index=index, phase=phase,
                             resets_only_W=True, preserves_U_G_h2=True)

                def callback(stage_U):
                    nonlocal local_calls, rhs_calls
                    local_calls += 1
                    require(local_calls <= 4, "too many stage callbacks")
                    c = (Fraction(0), Fraction(1, 2), Fraction(1, 2), Fraction(1))[local_calls - 1]
                    progress("stage_start", index=index, stage=local_calls, phase=phase,
                             time=number_record((index + c) * h_exact))
                    require(np.all(np.isfinite(stage_U)), "nonfinite velocity stage")
                    values = system.rhs(stage_U)
                    require(len(values) == 3 and all(np.all(np.isfinite(value)) for value in values),
                            "nonfinite or missing nonlinear source block")
                    rhs_calls += 1
                    progress("stage_end", index=index, stage=local_calls, phase=phase,
                             completed_rhs_calls=rhs_calls, fft_counts=counter.snapshot())
                    return values

                state = indexed_step(state, system.laplacians, callback, h_float, index, m)
                require(local_calls == 4, "incomplete four-stage step")
                counter.check_steps_since(before_counts, 1)
                require(all(np.all(np.isfinite(block)) for block in state), "nonfinite updated state")
                if index == m // 2:
                    # Count only the successfully returned and accepted half-entry
                    # step, never a reset whose step or preceding log failed.
                    half_reset_count += 1
                result["completed_steps"] += 1
                durations["step_seconds"] += time.perf_counter() - before_time
                record_node(index + 1)
                elapsed = time.perf_counter() - start
                progress("step_complete", completed_steps=index + 1, next_index=index + 1,
                         phase=phase, latest_checkpoint=checkpoints[-1],
                         eta_seconds=(elapsed / (index + 1)) * (m - index - 1))
            counter.check_steps_since(zero_counts, m)
            require(rhs_calls == 4 * m and half_reset_count == 1, "callback/reset count mismatch")
            require(result["completed_steps"] == m and journal.counts["nodes.jsonl"] == m + 1
                    and journal.counts["checkpoints.jsonl"] == m // 32 + 1
                    and [row["j"] for row in checkpoints] == list(range(0, m + 1, 32)),
                    "incomplete accepted nodes or checkpoint coverage")
            result["loop_and_checkpoint_coverage_verified"] = True
        finally:
            totals = counter.totals()
            result.update(rhs_calls=rhs_calls, half_reset_count=half_reset_count,
                          fft_counts=counter.snapshot(),
                          fft_batched_api_calls=totals["batched_api_calls"],
                          fft_scalar_3d_transforms=totals["scalar_3d_transforms"])
            result["node_count"] = journal.counts["nodes.jsonl"]
            result["checkpoint_count"] = journal.counts["checkpoints.jsonl"]
            result["journal_counts"] = dict(journal.counts)
            result["journal_bytes"] = dict(journal.sizes)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", choices=tuple(CONFIGS), required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--source-lock", type=Path, required=True)
    args = parser.parse_args()
    directory = args.output_dir
    require(directory.is_absolute() and directory.is_dir() and not directory.is_symlink()
            and directory.resolve() == HERE / "numerical-runs" / args.run_id,
            "output directory must be the supervisor-owned fixed run directory")
    result_path = directory / "result.json"
    require(not result_path.exists(), "result already exists; no overwrite or retry")
    result = {
        "schema": 1, "status": "FAIL", "run_id": args.run_id,
        "pid": os.getpid(), "supervisor_pid": os.getppid(), "scientific_worker_invocations": 1,
        "source_lock_sha256": None, "source_hashes_start": {}, "source_hashes_end": {},
        "completed_steps": 0, "expected_steps": CONFIGS[args.run_id][2],
        "node_count": 0, "checkpoint_count": 0,
        "fft_batched_api_calls": 0, "fft_scalar_3d_transforms": 0,
        "completion_verified": False, "loop_and_checkpoint_coverage_verified": False,
        "classification": "EXPLORATORY_FINITE_GALERKIN_TRAJECTORY_NOT_TRUE_NS_GATES",
        "actual_NS_existence_to_T_certified": False, "actual_NS_source_gates_certified": False,
        "energy_quadrature_performed": False, "automatic_resume_or_retry": False,
    }
    expected, journal = None, None
    started = time.perf_counter()
    try:
        require(Path.cwd().resolve() == ROOT, "worker must run in the reverse worktree")
        expected = load_lock(args.source_lock)
        result["source_lock_sha256"] = sha256(args.source_lock)
        result["source_hashes_start"] = source_hashes(expected)
        require(result["source_hashes_start"] == expected, "starting source hashes mismatch")
        journal = Journals(directory)
        run(args, result, directory, journal, expected)
        result["source_hashes_end"] = source_hashes(expected)
        require(result["source_hashes_end"] == expected
                and sha256(args.source_lock) == result["source_lock_sha256"],
                "ending source or source-lock hashes mismatch")
        m = CONFIGS[args.run_id][2]
        require(result["loop_and_checkpoint_coverage_verified"]
                and result["completed_steps"] == m and result["node_count"] == m + 1
                and result["checkpoint_count"] == m // 32 + 1
                and result["fft_batched_api_calls"] == 36 * m
                and result["fft_scalar_3d_transforms"] == 108 * m, "completion totals mismatch")
        result["completion_verified"] = True
        result["status"] = "PASS"
    except BaseException as error:
        result.update(status="FAIL", completion_verified=False,
                      error={"type": type(error).__name__, "message": str(error),
                             "traceback": traceback.format_exc()})
        if expected is not None:
            try:
                result["source_hashes_end"] = source_hashes(expected)
            except BaseException as hash_error:
                result["source_hashes_end_error"] = repr(hash_error)
    finally:
        if journal is not None:
            journal.close()
        result["worker_seconds_to_result_serialization"] = time.perf_counter() - started
        data = json_bytes(result)
        prior_json_bytes = sum(journal.sizes.values()) if journal is not None else 0
        if prior_json_bytes + len(data) > WORKER_JSON_LIMIT:
            result.update(status="FAIL", completion_verified=False, worker_json_budget_exceeded=True)
            data = json_bytes(result)  # Failure receipt is preserved, even if over budget.
        with result_path.open("xb") as stream:
            stream.write(data)
        print(json.dumps({"run_id": args.run_id, "status": result["status"],
                          "completed_steps": result["completed_steps"],
                          "completion_verified": result["completion_verified"]}), flush=True)
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
