#!/usr/bin/env python3
"""Read-only replay of an inspected immutable reverse-task calculation.

This is NOT a second Fourier implementation or a PDE solver. It reads three
hash-bound Git blobs, calls only calculation() from the reviewed module, checks
the entire result and independently recomputes the stated rational constants.
It writes nothing; stdout is the deterministic acceptance evidence.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
import subprocess
import sys
import types


REV = "90c44d1703486e3983d12b87ed54f22c8c677982"
PREFIX = "research/reverse/first-cycle/"
EXPECTED = {
    "exact_algebra.py": "5b9903f1b70a5f38e838a8ae82102a43354efda4878c3e295815d9ea5b166deb",
    "algebra-result.json": "27e7d80b602de0b5fad577039efe1e9d5274d7e8e1ddda0d8d719541f8b46b68",
    "certificate.json": "0146a8f88e224f922b4fc87daec5adb9acce9577cabea6a979abb0ae6b854ce4",
}


def main():
    root = Path(__file__).resolve().parent.parent
    blobs = {}
    for name, expected in EXPECTED.items():
        value = subprocess.check_output(["git", "-C", str(root), "show", REV + ":" + PREFIX + name])
        if hashlib.sha256(value).hexdigest() != expected:
            raise ValueError("immutable source hash mismatch: " + name)
        blobs[name] = value

    # Source was read in full before authorizing this fixed-version replay.
    # __name__ is not __main__, so its file-writing CLI is never called.
    name = "_forward_review_of_frozen_reverse_algebra"
    module = types.ModuleType(name)
    sys.modules[name] = module
    try:
        exec(compile(blobs["exact_algebra.py"], REV + ":exact_algebra.py", "exec"), module.__dict__)
        value = module.calculation()
    finally:
        del sys.modules[name]
    encoded = (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()
    if encoded != blobs["algebra-result.json"]:
        raise ValueError("complete algebra result differs from frozen bytes")

    cert = json.loads(blobs["certificate.json"])
    bounds = {k: F(v) for k, v in value["component_l1_upper_bounds"].items()}
    T = F(1, 10000)
    A = bounds["a"]
    U = A + bounds["b"] * T + bounds["c"] * T * T / 2
    M = 2 * (bounds["t2"] / 3 + bounds["t3"] * T / 4 + bounds["t4"] * T * T / 5)
    checks = {
        "all_primary_checks_recomputed": all(value["checks"].values()),
        "bounds_match_proof_table": bounds == {"a": F(6), "b": F(18), "c": F(66), "t2": F(213), "t3": F(56504, 165), "t4": F(64003, 165)},
        "fixed_time_contraction": 256 * A * A * T <= 1,
        "polynomial_in_ball": U <= 2 * A,
        "M_below_143": M < 143,
        "j_lower_bound": 1 - 2 * T - 143 * T * T >= F(1, 2),
        "k_lower_bound": F(1, 2) - 143 * T >= F(1, 4),
        "stored_rational_constants_match": str(M) == cert["M_exact"] and str(U) == cert["U_upper"],
        "certificate_points_to_full_algebra": cert["algebra_sha256"] == hashlib.sha256(encoded).hexdigest(),
    }
    if not all(checks.values()):
        raise ValueError("rational hypothesis failure: " + repr(checks))
    print(json.dumps({
        "status": "PASS_SCOPED_REPLAY",
        "source_commit": REV,
        "source_hashes": EXPECTED,
        "complete_algebra_bytes_match": True,
        "original_primary_check_count": len(value["checks"]),
        "rational_and_binding_checks": checks,
        "residual_modes": {k: len(v) for k, v in value["residual_coefficients"].items()},
        "bounds": {k: str(v) for k, v in bounds.items()},
        "M_exact": str(M),
        "U_upper": str(U),
        "T": str(T),
        "second_Fourier_implementation": False,
        "original_certify_py_mutation_suite_reexecuted": False,
        "PDE_solver": False,
        "mathematical_limit": "Same-code complete replay and exact constants only. The infinite-dimensional proof and the limited forward usefulness require analytic review; no new regularity or singularity result.",
    }, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
