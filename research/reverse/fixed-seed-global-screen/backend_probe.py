#!/usr/bin/env python3
"""One fixed static Fourier kernel probe; no time integration or PDE certificate.

The independent ordered convolution never calls the backend projector.
Run once with Python -B; a ten-second wall alarm includes dependency imports.
"""
from __future__ import annotations

import time

START = time.perf_counter()
import signal


class ProbeTimeout(RuntimeError):
    pass


def timeout_handler(signum, frame):
    raise ProbeTimeout("fixed ten-second wall budget exhausted; do not retry")


signal.signal(signal.SIGALRM, timeout_handler)
signal.setitimer(signal.ITIMER_REAL, 10.0)

import datetime
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import resource
import shlex
import statistics
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BACKEND = ROOT / "research/critical_packet_dynamics.py"
ALGEBRA = ROOT / "research/reverse/first-cycle/ALGEBRA.md"
OUTPUT = HERE / "backend-probe-run.json"
CONFIG = {
    "status": "STATIC_KERNEL_DIAGNOSTIC_NOT_NS_TRAJECTORY",
    "scale": 1, "viscosity": 1.0, "rho": 1.0,
    "grid": 27, "cutoff": 8, "delta_constructor_placeholder": 0.1,
    "static_fields": ["a", "a+N/8"],
    "absolute_max_component_error_threshold": 1e-12,
    "negative_control_minimum_difference": 1e-6,
    "timed_rhs_calls": 3,
    "timed_field": "a+N/8",
    "wall_budget_seconds": 10.0,
    "time_steps": 0,
    "parameter_or_grid_scan": False,
    "sparse_convention": "B_k=-i P_k sum_(p+q=k) (f_p dot q) f_q; P_0=I",
    "sparse_sum": "all ordered positive and negative mode pairs; no truncation",
    "array_dtype": "complex128",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


record = {
    "status": CONFIG["status"],
    "result": "INCOMPLETE",
    "started_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "actual_command": shlex.join([sys.executable, *sys.orig_argv[1:]]),
    "working_directory": os.getcwd(),
    "config": CONFIG,
    "config_sha256": hashlib.sha256(json.dumps(CONFIG, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
    "source_sha256": {
        str(Path(__file__).resolve()): sha(Path(__file__)),
        str(BACKEND): sha(BACKEND),
        str(ALGEBRA): sha(ALGEBRA),
    },
    "limits": [
        "Floating-point static diagnostic only; not a rigorous certificate.",
        "Neither field is advanced; a+N/8 is an algebraic test field, not a new initial-datum proposal.",
        "No continuum error estimate, NS trajectory, global regularity, or singularity conclusion.",
        "Array nbytes records exclude ephemeral FFT workspace; process peak RSS is reported separately.",
    ],
}

try:
    import numpy as np

    spec = importlib.util.spec_from_file_location("reverse_static_probe_backend", BACKEND)
    backend = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = backend
    spec.loader.exec_module(backend)
    cpu_name = platform.processor()
    if sys.platform == "darwin":
        cpu_name = subprocess.check_output(
            ["/usr/sbin/sysctl", "-n", "machdep.cpu.brand_string"], text=True, timeout=1
        ).strip()
    thread_keys = [
        "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
        "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS",
        "OMP_DYNAMIC", "MKL_DYNAMIC", "OMP_MAX_ACTIVE_LEVELS",
    ]
    record["environment"] = {
        "python": sys.version,
        "executable": sys.executable,
        "numpy": np.__version__,
        "numpy_path": np.__file__,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "cpu": cpu_name,
        "logical_cpu_count": os.cpu_count(),
        "thread_environment": {k: os.environ.get(k) for k in thread_keys},
        "thread_count_note": "Environment values are recorded, not inferred actual FFT worker counts; no thread setting was changed.",
        "precision": "numpy complex128 / float64",
    }

    # The six original coefficients and all twelve N coefficients are defined
    # independently of both the backend initializer and the sparse convolution.
    a = {}
    for axis, polarization in [(0, 1), (1, 2), (2, 0)]:
        for sign in (-1, 1):
            k = [0, 0, 0]
            k[axis] = sign
            value = np.zeros(3, dtype=np.complex128)
            value[polarization] = 1
            a[tuple(k)] = value
    N = {}
    for s in (-1, 1):
        for t in (-1, 1):
            N[(0, s, t)] = np.array([-1j*t, 0, 0], dtype=np.complex128)
            N[(s, 0, t)] = np.array([0, -1j*s, 0], dtype=np.complex128)
            N[(s, t, 0)] = np.array([0, 0, -1j*t], dtype=np.complex128)
    mixed = {k: value.copy() for k, value in a.items()}
    for k, value in N.items():
        mixed[k] = value / 8

    def sparse_ordered_kernel(field, project):
        raw = {}
        for p, fp in field.items():
            for q, fq in field.items():
                k = tuple(p[j] + q[j] for j in range(3))
                # Bilinear dot, never a Hermitian dot. Both orders are kept.
                raw.setdefault(k, np.zeros(3, dtype=np.complex128))
                raw[k] += -1j * sum(fp[j] * q[j] for j in range(3)) * fq
        if project:
            for k, value in raw.items():
                k2 = sum(ki*ki for ki in k)
                if k2:
                    dot = sum(k[j] * value[j] for j in range(3))
                    raw[k] = value - np.asarray(k) * (dot / k2)
        return raw

    def array_from_sparse(field):
        result = np.zeros((3, 27, 27, 27), dtype=np.complex128)
        for k, value in field.items():
            # This is a checked embedding, not truncation or modulo aliasing.
            if any(abs(ki) > CONFIG["cutoff"] for ki in k):
                raise ValueError("full sparse support escaped the predetermined cutoff")
            result[(slice(None),) + tuple(ki % 27 for ki in k)] = value
        return result

    def nonzero_records(field):
        return [
            {"k": list(k), "coefficient_real": v.real.tolist(), "coefficient_imag": v.imag.tolist()}
            for k, v in sorted(field.items()) if np.max(np.abs(v)) > 0
        ]

    def max_error(actual, expected):
        errors = np.abs(actual - expected)
        index = np.unravel_index(int(np.argmax(errors)), errors.shape)
        return {"maximum": float(errors[index]), "array_index": [int(i) for i in index]}

    system = backend.SpectralSystem(
        scale=1, delta=0.1, grid=27, cutoff=8, viscosity=1.0, rho=1.0
    )
    # Independently form the complete Laplacian multiplier.
    indices = np.arange(27)
    frequencies = np.where(indices <= 13, indices, indices - 27)
    laplace_squared = (
        frequencies[:, None, None]**2
        + frequencies[None, :, None]**2
        + frequencies[None, None, :]**2
    )
    sparse_a = sparse_ordered_kernel(a, project=True)
    n_definition_error = max_error(array_from_sparse(sparse_a), array_from_sparse(N))
    checks = {"N_direct_definition_matches_ordered_Baa": n_definition_error["maximum"] < 1e-12}
    record["N_definition_max_error"] = n_definition_error
    cases = []
    states = {}
    for name, field in [("a", a), ("a+N/8", mixed)]:
        state = array_from_sparse(field)
        states[name] = state
        expected_sparse = sparse_ordered_kernel(field, project=True)
        expected = array_from_sparse(expected_sparse)
        unprojected = array_from_sparse(sparse_ordered_kernel(field, project=False))
        actual = system.rotational_nonlinearity(state)
        expected_rhs = -laplace_squared[None, ...] * state + expected
        actual_rhs = system.rhs(state)
        nonlinear_error = max_error(actual, expected)
        rhs_error = max_error(actual_rhs, expected_rhs)
        no_pressure_difference = max_error(unprojected, expected)
        # Dropping P from u x curl u differs from dropping P from -u.grad u.
        # The latter independent raw-convection control is the one used here.
        checks[name + ": full_nonlinearity"] = nonlinear_error["maximum"] < 1e-12
        checks[name + ": full_rhs"] = rhs_error["maximum"] < 1e-12
        cases.append({
            "field": name,
            "input_nonzero_mode_count": len(field),
            "ordered_pair_count": len(field)**2,
            "full_output_support": nonzero_records(expected_sparse),
            "nonlinearity_error_all_grid_components": nonlinear_error,
            "rhs_error_all_grid_components": rhs_error,
            "unprojected_convective_negative_control_difference": no_pressure_difference,
            "nonlinear_zero_mode": [[float(x.real), float(x.imag)] for x in actual[:, 0, 0, 0]],
        })
        if name == "a+N/8":
            checks["mixed_field_detects_deleted_Leray_pressure"] = no_pressure_difference["maximum"] > 1e-6
    record["static_cases"] = cases

    timed_rhs_seconds = []
    for _ in range(3):
        before = time.perf_counter()
        timed_rhs = system.rhs(states["a+N/8"])
        timed_rhs_seconds.append(time.perf_counter() - before)
    record["timing"] = {
        "timed_rhs_seconds": timed_rhs_seconds,
        "median_rhs_seconds": statistics.median(timed_rhs_seconds),
        "sample_count": 3,
        "note": "Three RHS evaluations on the identical static mixed array, after correctness evaluations; no time step is applied.",
    }
    record["array_memory"] = {
        "one_complex_state_shape": list(states["a"].shape),
        "one_complex_state_nbytes": states["a"].nbytes,
        "two_static_states_nbytes": sum(v.nbytes for v in states.values()),
        "one_rhs_output_nbytes": timed_rhs.nbytes,
        "backend_attribute_array_nbytes": {
            key: value.nbytes for key, value in vars(system).items() if isinstance(value, np.ndarray)
        },
        "note": "Per-array nbytes are measured directly. Attribute views can share backing storage; no sum of this list is claimed as unique or peak memory. FFT transient workspace is excluded.",
    }
    record["checks"] = checks
    record["result"] = "PASS" if all(checks.values()) else "FAIL"
except Exception as exc:
    record["result"] = "TIME_BUDGET_STOP" if isinstance(exc, ProbeTimeout) else "ERROR"
    record["error"] = {"type": type(exc).__name__, "message": str(exc)}
finally:
    signal.setitimer(signal.ITIMER_REAL, 0)
    elapsed = time.perf_counter() - START
    record["total_script_wall_seconds_before_json_write"] = elapsed
    if elapsed >= 10.0 and record["result"] == "PASS":
        record["result"] = "TIME_BUDGET_STOP"
    record["process_peak_rss"] = {
        "ru_maxrss": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "unit": "bytes" if sys.platform == "darwin" else "KiB",
        "note": "Whole-process peak, including Python/libraries; not a pure NumPy-array allocation measurement.",
    }
    OUTPUT.write_text(json.dumps(record, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps({
        "record": str(OUTPUT), "record_sha256": sha(OUTPUT),
        "result": record["result"], "wall_seconds": elapsed,
        "timing": record.get("timing"), "checks": record.get("checks"),
    }, sort_keys=True))

raise SystemExit(0 if record["result"] == "PASS" else 1)
