#!/usr/bin/env python3
"""Produce one locked candidate-node archive, only when explicitly run with --run.

The scientific input is the saved Q52 integer data and its exact rational
projection, not the floating-point RK stages. This is not an NS certificate.
--describe and --check-only are read-only and never import the time integrator.
"""
from __future__ import annotations

import argparse
import ast
import datetime as dt
import hashlib
import importlib.util
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
ROOT = HERE.parents[2]
BACKEND = ROOT / "research/critical_packet_dynamics.py"
CONTRACTS = [HERE / "NODE_PRODUCTION_CONTRACT.md", HERE / "C1_RESIDUAL_CONTRACT.md"]
RUN_DIR = HERE / "node-trial-01"
Q = 1 << 52
CONFIG = {
    "kind": "CANDIDATE_INTEGER_NODES_NOT_NS_SOLUTION_NOT_CERTIFICATE",
    "scale": 1, "viscosity": 1, "rho": 1, "grid": 27, "cutoff": 8,
    "delta_constructor_placeholder": 0.1,
    "time_denominator": 2048, "steps": 5120, "nodes": 5121,
    "final_time_numerator": 5120, "quantization_denominator": Q,
    "rounding": "numpy.rint: nearest integer, ties to even, separately on real/imaginary binary64 components",
    "integer_dtype": "<i8", "array_axes": ["node", "mode", "vector_component", "real_imag"],
    "block_nodes": 64, "diagnostic_nodes": list(range(0, 5121, 640)),
    "diagnostic_full_quadratic_grid": 35, "diagnostic_spatial_sample_grid": 27,
    "progress_steps": 512, "progress_seconds": 10,
    "wall_budget_seconds": 180, "archive_budget_bytes": 512 * 1024**2,
    "peak_process_budget_bytes": 256 * 1024**2,
    "G": "lexicographic integer triples k in [-8,8]^3, excluding (0,0,0)",
    "G_count": 4912, "run_directory": str(RUN_DIR),
    "node_reference": "c_k=P_k[(Z_k+conj(Z_-k))/(2*2^52)]; slopes use their own integer array by the identical formula",
    "projection": "P_k=I-k tensor k/|k|^2 over the rationals; zero mode and outside G are exactly zero",
    "reference_between_nodes": "C1_RESIDUAL_CONTRACT V.4: shared-node cubic Hermite, physical time h=1/2048",
    "slopes": "one separate SpectralSystem.rhs(state) evaluation per node; no RK stage reused",
    "stored_float_stages": False, "parameter_scan": False, "resume_or_retry": False,
}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def file_sha(path):
    digest = hashlib.sha256()
    with open(path, "rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def modes_list():
    return [k for k in itertools.product(range(-8, 9), repeat=3) if k != (0, 0, 0)]


def launch_record():
    original = getattr(sys, "orig_argv", None)
    argv = list(original) if original is not None else [sys.executable, *sys.argv]
    return {"command": shlex.join(argv), "argv": argv,
            "command_source": "sys.orig_argv" if original is not None else "reconstructed executable plus sys.argv; interpreter flags unavailable",
            "python": sys.version, "executable": sys.executable}


def require_supported_python():
    if sys.version_info < (3, 10):
        raise RuntimeError("Python >=3.10 is required by the existing backend zip(strict=True); use the bundled Python 3.12 runtime. No run directory or claim has been created.")


def checkout_reference():
    """Read this checkout's HEAD metadata without running any git command."""
    entry = ROOT / ".git"
    if entry.is_file():
        text = entry.read_text().strip()
        if not text.startswith("gitdir: "):
            raise ValueError("unrecognized worktree .git pointer")
        gitdir = (ROOT / text[8:]).resolve()
    else:
        gitdir = entry
    head = (gitdir / "HEAD").read_text().strip()
    common = gitdir
    if (gitdir / "commondir").is_file():
        common = (gitdir / (gitdir / "commondir").read_text().strip()).resolve()
    reference = None
    commit = head
    if head.startswith("ref: "):
        reference = head[5:]
        if not reference.startswith("refs/") or ".." in reference.split("/"):
            raise ValueError("invalid local HEAD reference")
        commit = None
        for base in (gitdir, common):
            if (base / reference).is_file():
                commit = (base / reference).read_text().strip()
                break
        if commit is None and (common / "packed-refs").is_file():
            for line in (common / "packed-refs").read_text().splitlines():
                if line and not line.startswith(("#", "^")):
                    object_id, ref = line.split(" ", 1)
                    if ref == reference:
                        commit = object_id
                        break
    if not commit or len(commit) not in (40, 64) or any(c not in "0123456789abcdef" for c in commit):
        raise ValueError("cannot resolve local checkout commit")
    return {"source_commit": commit, "head_reference": reference,
            "scope": "checkout reference only; no clean-tree claim; actual source bytes are separately hashed"}


def preflight():
    require_supported_python()
    for path in [Path(__file__), BACKEND, *CONTRACTS]:
        if not path.is_file():
            raise FileNotFoundError(path)
    source = Path(__file__).read_text()
    tree = ast.parse(source)
    compile(tree, str(Path(__file__)), "exec")
    forbidden = [n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)
                 and isinstance(n.ctx, ast.Load) and n.attr in ("initial_state", "evolve")]
    if forbidden:
        raise AssertionError("old packet entry point referenced")
    modes = modes_list()
    assert len(modes) == 4912 and modes == sorted(modes)
    assert {tuple(-x for x in k) for k in modes} == set(modes)
    assert 27 > 3 * 8 and 35 > 4 * 8 and 5120 * 2 == 5 * 2048
    assert CONFIG["block_nodes"] <= 64 and CONFIG["diagnostic_nodes"] == list(range(0, 5121, 640))
    return {"read_only_check": "PASS", "integration_started": False,
            "checks": ["syntax", "fixed integer grid/time", "full symmetric G", "no old packet entry point"],
            "config": CONFIG, "config_sha256": hashlib.sha256(canonical(CONFIG)).hexdigest(),
            "source_sha256": {str(p): file_sha(p) for p in [Path(__file__), BACKEND, *CONTRACTS]},
            "checkout": checkout_reference(), "existing_run_directory": RUN_DIR.exists()}


class BudgetStop(RuntimeError):
    pass


def peak_rss_bytes():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(rss if sys.platform == "darwin" else rss * 1024)


class ArchiveWriter:
    """Seekable file proxy that never writes beyond the remaining archive cap."""
    def __init__(self, raw, maximum, budget_check):
        self.raw, self.maximum, self.budget_check = raw, maximum, budget_check

    def write(self, data):
        self.budget_check()
        if self.raw.tell() + len(data) > self.maximum:
            raise BudgetStop("compressed-node archive byte budget exhausted")
        return self.raw.write(data)

    def __getattr__(self, name):
        return getattr(self.raw, name)


def produce(info):
    require_supported_python()
    launch = launch_record()
    # A persistent exclusive claim rejects concurrent launches and any retry,
    # including attempts after an incomplete/failed run. No data are overwritten.
    claim = RUN_DIR / "RUN_CLAIM.json"
    claim_created = False
    try:
        claim_record = {"pid": os.getpid(), "started_at_utc": utc(), "launch": launch}
        claim_bytes = canonical(claim_record) + b"\n"
        RUN_DIR.mkdir(exist_ok=True)
        if any(RUN_DIR.iterdir()):
            raise FileExistsError("node-trial-01 is not empty; this single trial cannot be rerun")
        with claim.open("xb") as stream:
            claim_created = True
            stream.write(claim_bytes)
            stream.flush()
            os.fsync(stream.fileno())
    except Exception as exc:
        # Do not overwrite an existing process's claim, or retry a partial one.
        # Even failed claim serialization/write/fsync has a structured launch
        # record on the caller's captured stderr, before any numerical work.
        print(json.dumps({"status": "STARTUP_CLAIM_FAILED", "integration_started": False,
                          "launch": launch, "run_directory": str(RUN_DIR),
                          "claim_created_by_this_attempt": claim_created,
                          "partial_claim_retained": claim_created,
                          "source_sha256": info["source_sha256"],
                          "error": {"type": type(exc).__name__, "message": str(exc)}}, sort_keys=True),
              file=sys.stderr, flush=True)
        return 2

    started = time.perf_counter()
    manifest = {
        "schema": "reverse-fixed-seed-nodes-v1", "status": "RUNNING", "config": CONFIG,
        "config_sha256": info["config_sha256"], "source_sha256": info["source_sha256"],
        "checkout": info["checkout"], "started_at_utc": utc(), "pid": os.getpid(),
        "actual_command": launch["command"], "launch": launch, "working_directory": os.getcwd(),
        "blocks": [], "diagnostics": [], "progress": [], "completed_steps": 0,
        "computed_nodes": 0, "stored_nodes": 0, "archive_bytes": 0,
        "mathematical_status": "FIXED_INTEGER_REFERENCE_INPUT_ONLY; CONTINUOUS_RESIDUAL_AND_CONTROL_UNCERTIFIED",
        "limitations": [
            "Successful production is neither an NS trajectory certificate nor global regularity or singularity.",
            "The rational shared-node reference is determined uniquely by archived integers, conjugate averaging and exact P_k.",
            "Q52 nearest-even conversion is quantization, not lossless compression of the unstored floating-point RK stages.",
            "Floating diagnostics evaluate that integer reference approximately; sampled M_j are not spatial supremum bounds.",
            "Nine node residual observations do not certify time-continuous Hermite residuals or infinite-dimensional errors.",
            "A small approximate endpoint A_-1 does not pay the full residual/control contract.",
        ],
        "budget_monitoring": "wall alarm plus elapsed/peak-RSS checks after each step, node, FFT group and archive write, with a post-final-write success gate. Exceeding any observed cap cannot succeed; this does not claim OS prevention of transient allocation overruns.",
    }
    count = 0
    last_progress = started
    partial = None

    def save_manifest():
        manifest["wall_seconds"] = time.perf_counter() - started
        manifest["peak_process_rss_bytes"] = peak_rss_bytes()
        temporary = RUN_DIR / "manifest.json.tmp"
        with temporary.open("w") as stream:
            json.dump(manifest, stream, sort_keys=True, indent=2, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(RUN_DIR / "manifest.json")

    def check_budget():
        nonlocal last_progress
        now = time.perf_counter()
        if now - started >= 180:
            raise BudgetStop("180-second wall budget exhausted")
        if peak_rss_bytes() > CONFIG["peak_process_budget_bytes"]:
            raise BudgetStop("256-MiB peak process RSS budget exceeded")
        if manifest["archive_bytes"] > CONFIG["archive_budget_bytes"]:
            raise BudgetStop("512-MiB node archive budget exceeded")
        # This also keeps compression and final sequential verification visible,
        # not only the RK loop's 512-step reports.
        if now - last_progress >= 10:
            item = {"completed_steps": manifest["completed_steps"],
                    "computed_nodes": manifest["computed_nodes"],
                    "stored_nodes": manifest["stored_nodes"],
                    "pending_nodes": manifest["computed_nodes"] - manifest["stored_nodes"],
                    "archive_bytes": manifest["archive_bytes"], "wall_seconds": now - started,
                    "peak_process_rss_bytes": peak_rss_bytes()}
            manifest["progress"].append(item)
            last_progress = now
            save_manifest()
            print(json.dumps({"node_production_progress": item}, sort_keys=True), flush=True)

    def deadline(signum, frame):
        raise BudgetStop("180-second wall alarm reached")

    def interrupted(signum, frame):
        raise BudgetStop("external interruption signal " + str(signum))

    signal.signal(signal.SIGALRM, deadline)
    signal.signal(signal.SIGTERM, interrupted)
    signal.signal(signal.SIGINT, interrupted)
    signal.setitimer(signal.ITIMER_REAL, 180)
    save_manifest()
    try:
        sys.dont_write_bytecode = True
        import numpy as np

        spec = importlib.util.spec_from_file_location("reverse_node_production_backend", BACKEND)
        backend = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = backend
        spec.loader.exec_module(backend)
        cpu_name = platform.processor()
        if sys.platform == "darwin":
            cpu_name = subprocess.check_output(
                ["/usr/sbin/sysctl", "-n", "machdep.cpu.brand_string"], text=True, timeout=1
            ).strip()
        env_keys = ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
                    "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS", "OMP_DYNAMIC", "MKL_DYNAMIC"]
        manifest["environment"] = {
            "python": sys.version, "executable": sys.executable, "numpy": np.__version__,
            "numpy_path": np.__file__, "platform": platform.platform(), "machine": platform.machine(),
            "cpu": cpu_name, "logical_cpu_count": os.cpu_count(),
            "thread_environment": {k: os.environ.get(k) for k in env_keys},
            "thread_note": "No thread setting changed; environment does not establish actual internal FFT worker count.",
            "floating_dtype": "complex128/float64", "integer_dtype": "little-endian int64",
        }
        check_budget()
        modes = np.asarray(modes_list(), dtype="<i8")
        mode_count = len(modes)
        modes_index = {tuple(k): n for n, k in enumerate(modes.tolist())}
        opposite = np.asarray([modes_index[tuple(-x for x in k)] for k in modes.tolist()])
        mode_k2 = np.sum(modes * modes, axis=1)
        index27 = tuple((modes % 27).T)
        mode_path = RUN_DIR / "modes.npy"
        with mode_path.open("xb") as stream:
            np.save(stream, modes, allow_pickle=False)
        manifest["archive_bytes"] += mode_path.stat().st_size
        manifest["modes"] = {"file": mode_path.name, "file_sha256": file_sha(mode_path),
                             "array_sha256": hashlib.sha256(memoryview(modes).cast("B")).hexdigest(),
                             "shape": list(modes.shape), "dtype": modes.dtype.str,
                             "ordering": CONFIG["G"]}
        system = backend.SpectralSystem(scale=1, delta=0.1, grid=27, cutoff=8, viscosity=1, rho=1)
        state = np.zeros((3, 27, 27, 27), dtype=np.complex128)
        initial_q = np.zeros((mode_count, 3, 2), dtype="<i8")
        for axis, component in [(0, 1), (1, 2), (2, 0)]:
            for sign in (-1, 1):
                k = [0, 0, 0]
                k[axis] = sign
                state[(component,) + tuple(x % 27 for x in k)] = 1
                initial_q[modes_index[tuple(k)], component, 0] = Q
        values = np.empty((64, mode_count, 3, 2), dtype="<i8")
        slopes = np.empty_like(values)
        node_indices = np.empty(64, dtype="<i8")
        manifest["array_memory"] = {"one_complex_grid_nbytes": state.nbytes,
                                    "value_block_buffer_nbytes": values.nbytes,
                                    "slope_block_buffer_nbytes": slopes.nbytes,
                                    "note": "Measured persistent array sizes, excluding transient RK/FFT/compression allocations; peak process RSS is checked separately."}
        manifest["archive_cost_boundary"] = {
            "all_node_value_and_slope_integer_bytes_before_compression": 5121 * 4912 * 3 * 2 * 8 * 2,
            "compression_feasibility": "The 512-MiB cap is a stop condition, not a claim that compression will fit; no alternative precision or block strategy is tried.",
        }
        check_budget()

        def quantize(grid_array):
            vector = grid_array[(slice(None),) + index27].T
            output = np.empty((mode_count, 3, 2), dtype="<i8")
            for component, part in enumerate((vector.real, vector.imag)):
                with np.errstate(over="ignore", invalid="ignore"):
                    rounded = np.rint(np.ldexp(part, 52))
                if not np.all(np.isfinite(rounded)):
                    raise ValueError("nonfinite state/slope or Q52 scaling overflow")
                # float(2^63-1) rounds to 2^63. The fixed safe conversion rule
                # requires strict magnitude <2^63 and rejects both endpoints.
                if np.any(np.abs(rounded) >= float(1 << 63)):
                    raise OverflowError("Q52 signed int64 conversion overflow")
                output[:, :, component] = rounded.astype("<i8")
            return output

        def rational_reference_float(encoded):
            # This is ONLY a floating diagnostic evaluation of the prescribed
            # exact rational operation. No projected floats replace the integers.
            z = np.ldexp(encoded[:, :, 0].astype(float), -52) + 1j * np.ldexp(encoded[:, :, 1].astype(float), -52)
            z = (z + np.conjugate(z[opposite])) / 2
            return z - modes * (np.sum(modes * z, axis=1) / mode_k2)[:, None]

        def embed(vector, size):
            grid = np.zeros((3, size, size, size), dtype=np.complex128)
            grid[(slice(None),) + tuple((modes % size).T)] = vector.T
            return grid

        def wave_grid(size):
            freq = np.arange(size)
            freq = np.where(freq <= size // 2, freq, freq - size)
            return freq[:, None, None], freq[None, :, None], freq[None, None, :]

        def node_diagnostic(node, encoded_value, encoded_slope):
            check_budget()
            c = rational_reference_float(encoded_value)
            d = rational_reference_float(encoded_slope)
            mode_size = np.sum(np.abs(c)**2, axis=1)
            diagnostic = {
                "node_index": node, "time_numerator": node, "time_denominator": 2048,
                "status": "SAMPLED_FLOATING_NODE_DIAGNOSTIC_NONRIGOROUS_NOT_CONTINUOUS_BOUND",
                "evaluated_object": "floating evaluation of the stored integers after prescribed conjugate average and rational P_k",
                "A_minus_1_approx": float(np.sum(np.sqrt(mode_size / mode_k2))),
                "normalized_L2_squared_approx": float(np.sum(mode_size)),
                "derivative_L2_squared_approx": {str(j): float(np.sum(mode_k2**j * mode_size)) for j in (1, 2, 3)},
                "divergence_max_approx": float(np.max(np.abs(np.sum(modes * c, axis=1)))),
                "reality_max_approx": float(np.max(np.abs(c - np.conjugate(c[opposite])))),
            }
            full = embed(c, 35)
            kx, ky, kz = wave_grid(35)
            k2 = kx*kx + ky*ky + kz*kz
            curl = np.empty_like(full)
            curl[0] = 1j * (ky * full[2] - kz * full[1])
            curl[1] = 1j * (kz * full[0] - kx * full[2])
            curl[2] = 1j * (kx * full[1] - ky * full[0])
            velocity = np.fft.ifftn(35**3 * full, axes=(-3, -2, -1))
            vorticity = np.fft.ifftn(35**3 * curl, axes=(-3, -2, -1))
            cross = np.empty_like(full)
            cross[0] = velocity[1]*vorticity[2] - velocity[2]*vorticity[1]
            cross[1] = velocity[2]*vorticity[0] - velocity[0]*vorticity[2]
            cross[2] = velocity[0]*vorticity[1] - velocity[1]*vorticity[0]
            quadratic = np.fft.fftn(cross, axes=(-3, -2, -1)) / 35**3
            inverse = np.zeros_like(k2, dtype=float)
            np.divide(1.0, k2, out=inverse, where=k2 > 0)
            dot = kx*quadratic[0] + ky*quadratic[1] + kz*quadratic[2]
            for j, kj in enumerate((kx, ky, kz)):
                quadratic[j] -= kj * dot * inverse
            quadratic[:, 0, 0, 0] = 0
            # No cutoff mask is applied to this full 35^3 quadratic term.
            inside = (np.abs(kx) <= 8) & (np.abs(ky) <= 8) & (np.abs(kz) <= 8) & (k2 > 0)
            beyond_sumset = (np.abs(kx) > 16) | (np.abs(ky) > 16) | (np.abs(kz) > 16)
            residual = embed(d, 35) + k2[None, ...]*full - quadratic
            r_squared = np.sum(np.abs(residual)**2, axis=0)
            diagnostic["full_35_grid_node_residual_norms_approx"] = {
                "r0": float(np.sqrt(np.sum(r_squared))),
                "r2": float(np.sqrt(np.sum(k2**2 * r_squared))),
                "inside_G_r0": float(np.sqrt(np.sum(r_squared[inside]))),
                "inside_G_r2": float(np.sqrt(np.sum((k2**2*r_squared)[inside]))),
                "outside_G_r0": float(np.sqrt(np.sum(r_squared[~inside]))),
                "outside_G_r2": float(np.sqrt(np.sum((k2**2*r_squared)[~inside]))),
                "quadratic_roundoff_outside_G_plus_G_max": float(np.max(np.abs(quadratic[:, beyond_sumset]))),
                "note": "All unmasked outputs retained, including roundoff outside G+G; no claim of a rigorous residual enclosure.",
            }
            del full, curl, velocity, vorticity, cross, quadratic, residual, r_squared, dot
            check_budget()
            small = embed(c, 27)
            ks = wave_grid(27)
            sampled = {}
            max_imag = 0.0
            for order in (1, 2, 3):
                squares = np.zeros((27, 27, 27))
                for alpha in itertools.product(range(order + 1), repeat=3):
                    if sum(alpha) != order:
                        continue
                    multiplicity = math.factorial(order) // math.prod(math.factorial(x) for x in alpha)
                    factor = (1j**order) * ks[0]**alpha[0] * ks[1]**alpha[1] * ks[2]**alpha[2]
                    derivative = np.fft.ifftn(27**3 * small * factor[None, ...], axes=(-3, -2, -1))
                    squares += multiplicity * np.sum(derivative.real**2, axis=0)
                    max_imag = max(max_imag, float(np.max(np.abs(derivative.imag))))
                    check_budget()
                sampled[str(order)] = float(np.sqrt(np.max(squares)))
            diagnostic["M_j_sampled_27_grid_frobenius_approx"] = sampled
            diagnostic["derivative_sample_imaginary_roundoff_max"] = max_imag
            diagnostic["spatial_sample_note"] = "Ordered derivative Frobenius multiplicities included; the sample maximum is not a full-space upper bound."
            return diagnostic

        def describe_array(array):
            return {"shape": list(array.shape), "dtype": array.dtype.str,
                    "nbytes": array.nbytes, "data_sha256": hashlib.sha256(memoryview(array).cast("B")).hexdigest()}

        def flush_block():
            nonlocal count, partial
            if not count:
                return
            check_budget()
            first, last = int(node_indices[0]), int(node_indices[count - 1])
            expected_first = manifest["stored_nodes"]
            if first != expected_first or last != first + count - 1:
                raise AssertionError("node block is not a contiguous non-overlapping sequence")
            arrays = {
                "node_index": node_indices[:count],
                "time_numerator": node_indices[:count].copy(),
                "time_denominator": np.asarray([2048], dtype="<i8"),
                "quantization_denominator": np.asarray([Q], dtype="<i8"),
                "value_q52": values[:count], "slope_q52": slopes[:count],
            }
            descriptions = {name: describe_array(array) for name, array in arrays.items()}
            entry = {"first_node": first, "last_node": last, "node_count": count,
                     "arrays": descriptions, "data_sha256": hashlib.sha256(canonical(descriptions)).hexdigest()}
            name = f"block-{first:05d}-{last:05d}.npz"
            partial = RUN_DIR / (name + ".partial")
            if (RUN_DIR / name).exists():
                raise FileExistsError(name)
            remaining = CONFIG["archive_budget_bytes"] - manifest["archive_bytes"]
            with partial.open("xb") as raw:
                bounded = ArchiveWriter(raw, remaining, check_budget)
                np.savez_compressed(bounded, **arrays)
                raw.flush()
                os.fsync(raw.fileno())
            check_budget()
            partial.replace(RUN_DIR / name)
            partial = None
            entry.update({"file": name, "file_bytes": (RUN_DIR / name).stat().st_size,
                          "file_sha256": file_sha(RUN_DIR / name)})
            manifest["blocks"].append(entry)
            manifest["archive_bytes"] += entry["file_bytes"]
            manifest["stored_nodes"] += count
            count = 0
            check_budget()
            save_manifest()

        def progress(node, force=False):
            nonlocal last_progress
            now = time.perf_counter()
            if force or node % 512 == 0 or now - last_progress >= 10:
                item = {"completed_steps": node, "computed_nodes": manifest["computed_nodes"],
                        "stored_nodes": manifest["stored_nodes"], "pending_nodes": count,
                        "archive_bytes": manifest["archive_bytes"], "wall_seconds": now - started,
                        "peak_process_rss_bytes": peak_rss_bytes()}
                manifest["progress"].append(item)
                save_manifest()
                print(json.dumps({"node_production_progress": item}, sort_keys=True), flush=True)
                last_progress = now

        save_manifest()
        for node in range(5121):
            check_budget()
            # This separate evaluation defines the candidate physical-time slope.
            slope = system.rhs(state)
            check_budget()
            values[count] = quantize(state)
            slopes[count] = quantize(slope)
            node_indices[count] = node
            if node == 0:
                if not np.array_equal(values[count], initial_q):
                    raise AssertionError("initial integer encoding differs from the fixed six modes")
                manifest["initial_node_exact_check"] = "RAW_Q52_INTEGERS_EQUAL_FIXED_SIX_MODE_ENCODING; rational average/projection preserves a exactly"
            manifest["computed_nodes"] = node + 1
            if node in CONFIG["diagnostic_nodes"]:
                manifest["diagnostics"].append(node_diagnostic(node, values[count], slopes[count]))
            count += 1
            if count == 64 or node == 5120:
                flush_block()
            progress(node)
            if node < 5120:
                state = system.rk4_step(state, 1 / 2048)
                manifest["completed_steps"] = node + 1
                check_budget()
                if not np.all(np.isfinite(state)):
                    raise ValueError("nonfinite RK4 state")

        # Full sequential archive verification is included in the same budget.
        if file_sha(mode_path) != manifest["modes"]["file_sha256"]:
            raise AssertionError("frequency-list file hash changed")
        verified = 0
        for entry in manifest["blocks"]:
            check_budget()
            path = RUN_DIR / entry["file"]
            if path.stat().st_size != entry["file_bytes"] or file_sha(path) != entry["file_sha256"]:
                raise AssertionError("block file size/hash mismatch: " + path.name)
            with np.load(path, allow_pickle=False) as archive:
                if set(archive.files) != set(entry["arrays"]):
                    raise AssertionError("unexpected NPZ array names")
                for name, expected in entry["arrays"].items():
                    array = archive[name]
                    if describe_array(array) != expected:
                        raise AssertionError("array data hash/shape/dtype mismatch: " + name)
                    if name in ("node_index", "time_numerator"):
                        if not np.array_equal(array, np.arange(verified, verified + entry["node_count"], dtype="<i8")):
                            raise AssertionError("archive node sequence mismatch")
                    del array
                    check_budget()
            verified += entry["node_count"]
        if verified != 5121 or manifest["stored_nodes"] != 5121 or manifest["completed_steps"] != 5120:
            raise AssertionError("incomplete node archive")
        if [item["node_index"] for item in manifest["diagnostics"]] != CONFIG["diagnostic_nodes"]:
            raise AssertionError("fixed diagnostic-node sequence mismatch")
        if any(file_sha(Path(name)) != expected for name, expected in manifest["source_sha256"].items()):
            raise AssertionError("source bytes changed during production")
        manifest["archive_verification"] = {"status": "PASS", "verified_nodes": verified,
                                            "scope": "all block file hashes and all uncompressed array hashes/shape/dtype; no mathematical residual certificate"}
        check_budget()
        manifest["status"] = "CANDIDATE_DATA_VERIFIED_FINALIZING"
        progress(5120, force=True)
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL, 0)
        manifest["status"] = "BUDGET_STOP" if isinstance(exc, BudgetStop) else "FAILED"
        manifest["error"] = {"type": type(exc).__name__, "message": str(exc)}
        manifest["pending_nodes_not_archived"] = manifest["computed_nodes"] - manifest["stored_nodes"]
        manifest["failure_policy"] = "Existing files/complete blocks retained. Pending floating buffers are not claimed as archived scientific data. No retry or parameter change."
        if partial is not None and partial.exists():
            manifest["incomplete_block_file"] = {"file": partial.name, "bytes": partial.stat().st_size,
                                                 "usable_as_complete_block": False}
        indexed = {entry["file"] for entry in manifest["blocks"]}
        manifest["retained_unindexed_block_files"] = [
            {"file": p.name, "bytes": p.stat().st_size, "status": "RETAINED_NOT_VERIFIED_OR_COUNTED"}
            for p in RUN_DIR.glob("block-*.npz") if p.name not in indexed
        ]
        print(json.dumps({"node_production_stopped": manifest["status"], "error": manifest["error"]}), flush=True)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        manifest["finished_at_utc"] = utc()
        manifest["actual_archive_file_bytes_including_incomplete"] = sum(
            p.stat().st_size for p in RUN_DIR.iterdir()
            if p.is_file() and (p.name.startswith("block-") or p.name == "modes.npy")
        )
        # Cleanup is allowed to preserve STOP evidence after a deadline. It must
        # never convert a measured resource overrun into a successful archive.
        def final_budget_observation():
            observation = {
                "wall_seconds": time.perf_counter() - started,
                "peak_process_rss_bytes": peak_rss_bytes(),
                "archive_bytes_including_incomplete": manifest["actual_archive_file_bytes_including_incomplete"],
            }
            violations = []
            if observation["wall_seconds"] >= CONFIG["wall_budget_seconds"]:
                violations.append("wall budget")
            if observation["peak_process_rss_bytes"] > CONFIG["peak_process_budget_bytes"]:
                violations.append("peak process RSS budget")
            if observation["archive_bytes_including_incomplete"] > CONFIG["archive_budget_bytes"]:
                violations.append("archive byte budget")
            observation["violations"] = violations
            return observation

        def mark_final_budget_stop(observation):
            if "error" in manifest:
                manifest["prior_error"] = manifest["error"]
            manifest["status"] = "BUDGET_STOP"
            manifest["error"] = {"type": "BudgetStop", "message": "finalization exceeded " + ", ".join(observation["violations"])}
            manifest["final_budget_observation"] = observation

        observation = final_budget_observation()
        manifest["final_budget_observation"] = observation
        if observation["violations"]:
            mark_final_budget_stop(observation)
        elif manifest["status"] == "CANDIDATE_DATA_VERIFIED_FINALIZING":
            manifest["status"] = "CANDIDATE_NODES_COMPLETE_NOT_NS_CERTIFIED"
        save_manifest()
        manifest_hash = file_sha(RUN_DIR / "manifest.json")
        # The successful exit checks measurements taken AFTER final atomic
        # persistence and hashing, so their wall/RSS cost cannot escape the gate.
        exit_observation = final_budget_observation()
        if manifest["status"] == "CANDIDATE_NODES_COMPLETE_NOT_NS_CERTIFIED" and exit_observation["violations"]:
            mark_final_budget_stop(exit_observation)
            save_manifest()
            manifest_hash = file_sha(RUN_DIR / "manifest.json")
    print(json.dumps({"manifest": str(RUN_DIR / "manifest.json"), "manifest_sha256": manifest_hash,
                      "status": manifest["status"], "stored_nodes": manifest["stored_nodes"],
                      "wall_seconds": manifest["wall_seconds"], "success_exit_budget_observation": exit_observation}, sort_keys=True), flush=True)
    return 0 if manifest["status"] == "CANDIDATE_NODES_COMPLETE_NOT_NS_CERTIFIED" else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--run", action="store_true", help="execute the one fixed trial; refuses any existing run artifacts")
    mode.add_argument("--describe", action="store_true", help="print fixed configuration without importing NumPy or the solver")
    mode.add_argument("--check-only", action="store_true", help="read-only syntax/configuration/source checks; no integration")
    args = parser.parse_args()
    if not args.run and not args.check_only:
        print(json.dumps({"integration_started": False, "config": CONFIG}, indent=2, sort_keys=True))
        return 0
    try:
        info = preflight()
    except Exception as exc:
        print(json.dumps({"status": "STARTUP_REFUSED", "integration_started": False,
                          "run_directory_or_claim_created_by_this_attempt": False,
                          "launch": launch_record(),
                          "error": {"type": type(exc).__name__, "message": str(exc)}}, sort_keys=True),
              file=sys.stderr, flush=True)
        return 2
    if args.check_only:
        print(json.dumps(info, indent=2, sort_keys=True))
        return 0
    return produce(info)


if __name__ == "__main__":
    raise SystemExit(main())
