#!/usr/bin/env python3
"""One fixed-data full-eight-mode exact experiment; prepare, freeze, then run.

Scientific inputs are constants, inherited from the already fixed smaller
quadratic root and normalized w.  Command-line arguments are provenance only.
No alpha probes, alternate roots, parameters, random choices, or floats.
All B vertices are ordered and include the full Leray projection.

Leading phase convention:
  a is real/even, H1 has physical factor -i, H2 factor -1;
  W0 and M0 have factor +i times the stored real quadratic-field vectors.
  B(P_G W0,P_G W0) also has factor +i times Q(C,C), with NO time
  integration factor.  That conditional calculation is NOT the actual v7.
"""

import argparse
from fractions import Fraction as F
import hashlib
from itertools import product
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time
import traceback


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "exact-band-output.json"
P = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 3, 5))
D0 = 37138824124764
D1 = 104767331941035
D2 = 73555298559275
RED0 = -F(D0, D2)
RED1 = -F(D1, D2)
ROOT_LO = -F(55889541592004, 73555298559275)
ROOT_HI = -F(111779083184007, 147110597118550)
MAX_BISECTIONS = 128
MAX_WALL_SECONDS = 60
MAX_OUTPUT_BYTES = 1024 * 1024
MAX_SELF_RSS_BYTES = 256 * 1024 * 1024
INHERITED_ALGEBRA_SHA = "a87cdef2cc2517e391ee193c3ad17b0e6776af3d7b8dff8f0427c2b063e08d1a"
INHERITED_PROGRAM_SHA = "e588da476addd56f092fea94b8f0315a0eb7df3e304d9fba3e51071d17c35f6c"
INHERITED_OUTPUT_SHA = "de084e897e08c7faa48dd49dbb00af61f0449587b34e8a4890711c4a176a0bc7"


class Q:
    """The fixed irreducible field Q[alpha]/(D2 alpha^2+D1 alpha+D0)."""
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def cast(value):
        return value if isinstance(value, Q) else Q(value)

    def __add__(self, other):
        other = Q.cast(other)
        return Q(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-Q.cast(other))

    def __rsub__(self, other):
        return Q.cast(other) - self

    def __mul__(self, other):
        if not isinstance(other, Q):
            other = F(other)
            return Q(self.a * other, self.b * other)
        bb = self.b * other.b
        return Q(self.a * other.a + bb * RED0,
                 self.a * other.b + self.b * other.a + bb * RED1)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, Q):
            other = F(other)
            if other == 0:
                raise ZeroDivisionError("rational divisor is zero")
            return Q(self.a / other, self.b / other)
        conjugate = Q(other.a + other.b * RED1, -other.b)
        norm = other * conjugate
        if norm.b != 0 or norm.a == 0:
            raise ZeroDivisionError("quadratic-field divisor is zero or invalid")
        return (self * conjugate) / norm.a

    def __eq__(self, other):
        other = Q.cast(other)
        return self.a == other.a and self.b == other.b


ZERO = (Q(), Q(), Q())
ALPHA = Q(0, 1)
FIXED_W = Q(F(111626564931091, 129542798481515),
            F(1009178696233253, 466354074533454))


def qstr(value):
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else str(value)


def qrecord(value):
    return {"constant": qstr(value.a), "alpha": qstr(value.b)}


def vrecord(vector):
    return [qrecord(value) for value in vector]


def krecord(k):
    return ",".join(str(x) for x in k)


def negk(k):
    return tuple(-x for x in k)


def vadd(left, right):
    return tuple(x + y for x, y in zip(left, right))


def vscale(scalar, vector):
    return tuple(x * scalar for x in vector)


def vdot(left, right):
    return sum((x * y for x, y in zip(left, right)), Q())


def is_zero_vector(vector):
    return all(x == 0 for x in vector)


def norm_square(vector):
    # Only stripped vectors at the fixed REAL embedding occur here.
    return sum((x * x for x in vector), Q())


def clean(field):
    return {k: vector for k, vector in field.items()
            if not is_zero_vector(vector)}


def field_scale(scalar, field):
    return clean({k: vscale(scalar, vector) for k, vector in field.items()})


def field_add(left, right):
    result = dict(left)
    for k, vector in right.items():
        result[k] = vadd(result.get(k, ZERO), vector)
    return clean(result)


def field_record(field):
    return {krecord(k): vrecord(field[k]) for k in sorted(field)}


def assert_transverse(field):
    for k, vector in field.items():
        assert k != (0, 0, 0)
        assert vdot(vector, k) == 0


def assert_parity(field, sign):
    for k, vector in field.items():
        assert field.get(negk(k), ZERO) == vscale(sign, vector)


def full_ordered_vertex(left, right):
    """All ordered convolution pairs, including pairs outside K4.

    Returns B with the single vertex factor -i stripped.  Zero output is
    checked using transverse first inputs before discarding it.
    """
    assert_transverse(left)
    assert_transverse(right)
    output = {}
    pair_count = 0
    zero_frequency_pairs = 0
    zero_dot_pairs = 0
    for r, left_vector in left.items():
        for s, right_vector in right.items():
            pair_count += 1
            k = tuple(x + y for x, y in zip(r, s))
            contracted = vdot(left_vector, s)
            if k == (0, 0, 0):
                assert contracted == 0
                zero_frequency_pairs += 1
                continue
            if contracted == 0:
                zero_dot_pairs += 1
                continue
            raw = vscale(contracted, right_vector)
            kk = sum(x * x for x in k)
            normal = vdot(raw, k) / kk
            projected = tuple(raw[i] - normal * k[i] for i in range(3))
            output[k] = vadd(output.get(k, ZERO), projected)
    output = clean(output)
    assert_transverse(output)
    return output, {
        "left_nonzero_modes": len(left), "right_nonzero_modes": len(right),
        "ordered_pairs_visited": pair_count,
        "zero_output_frequency_pairs_checked": zero_frequency_pairs,
        "other_zero_dot_pairs": zero_dot_pairs,
        "nonzero_output_modes_after_exact_cancellation": len(output),
        "target_filter_in_convolution": False}


def polynomial_at(value):
    return D2 * value * value + D1 * value + D0


def rational_sign(value):
    return (value > 0) - (value < 0)


def sign_certificate(value):
    """Exact sign at the smaller root, at most 128 root bisections.

    Values are first reduced to a+b*alpha.  Zero is equality in the
    irreducible quotient field; nonzero signs come from a rational interval.
    """
    if value == 0:
        return {"value": qrecord(value), "sign": 0,
                "method": "exact_quotient_zero", "bisections": 0}
    if value.b == 0:
        return {"value": qrecord(value), "sign": rational_sign(value.a),
                "method": "rational", "bisections": 0,
                "value_lower": qstr(value.a), "value_upper": qstr(value.a)}
    lo, hi = ROOT_LO, ROOT_HI
    for step in range(MAX_BISECTIONS + 1):
        end1 = value.a + value.b * lo
        end2 = value.a + value.b * hi
        lower, upper = min(end1, end2), max(end1, end2)
        if lower > 0 or upper < 0:
            return {"value": qrecord(value), "sign": 1 if lower > 0 else -1,
                    "method": "smaller_root_rational_interval",
                    "bisections": step, "root_interval_open": [qstr(lo), qstr(hi)],
                    "value_lower": qstr(lower), "value_upper": qstr(upper)}
        if step == MAX_BISECTIONS:
            return {"value": qrecord(value), "sign": None,
                    "method": "NOT_CERTIFIED_128_BISECTIONS",
                    "bisections": step, "root_interval_open": [qstr(lo), qstr(hi)],
                    "value_lower": qstr(lower), "value_upper": qstr(upper)}
        middle = (lo + hi) / 2
        fmid = polynomial_at(middle)
        # The fixed irreducible polynomial has no rational root.
        assert fmid != 0
        # Initial interval lies to the left of the vertex and contains
        # only the smaller root: f>0 on its left and f<0 on its right.
        if fmid > 0:
            lo = middle
        else:
            hi = middle
    raise AssertionError("unreachable sign loop")


def pair_supply_lower_bound(k, vector):
    """Rational lower bound for ||P_{+-k} W0||_A0 = 2 |vector|_2."""
    coordinate = next(i for i, value in enumerate(vector) if value != 0)
    certificate = sign_certificate(vector[coordinate])
    if certificate["sign"] is None:
        return {"representative": list(k), "status": "NOT_CERTIFIED",
                "coordinate_zero_based": coordinate, "sign_certificate": certificate}
    assert certificate["sign"] != 0
    lower = F(certificate["value_lower"])
    upper = F(certificate["value_upper"])
    abs_lower = min(abs(lower), abs(upper))
    assert abs_lower > 0
    bound = 2 * abs_lower
    return {"representative": list(k), "status": "certified",
            "coordinate_zero_based": coordinate,
            "component_absolute_lower_rational": qstr(abs_lower),
            "pair_A0_supply_lower_rational": qstr(bound),
            "reason": "2*Euclidean_norm >= 2*absolute_selected_component",
            "sign_certificate": certificate}


def cross(left, right):
    return (left[1] * right[2] - left[2] * right[1],
            left[2] * right[0] - left[0] * right[2],
            left[0] * right[1] - left[1] * right[0])


def intdot(left, right):
    return sum(x * y for x, y in zip(left, right))


def frequency_rank(frequencies):
    """Integer minors certify real frequency rank; no floating matrix routine."""
    ordered = sorted(frequencies)
    if not ordered:
        return {"rank": 0, "basis": [], "certificate": "empty_set"}
    first = ordered[0]
    assert first != (0, 0, 0)
    second = next((k for k in ordered if cross(first, k) != (0, 0, 0)), None)
    if second is None:
        return {"rank": 1, "basis": [list(first)],
                "certificate": "every_frequency_cross_first_is_zero"}
    normal = cross(first, second)
    third = next((k for k in ordered if intdot(normal, k) != 0), None)
    if third is None:
        return {"rank": 2, "basis": [list(first), list(second)],
                "nonzero_normal": list(normal),
                "certificate": "every_frequency_dot_normal_is_zero"}
    return {"rank": 3, "basis": [list(first), list(second), list(third)],
            "nonzero_determinant": intdot(normal, third)}


def fixed_initial_field():
    vectors = ((Q(), Q(1), ALPHA), (Q(), Q(), Q(1)), (Q(1), Q(), Q()),
               (Q(3) + 5 * FIXED_W, Q(-2), -2 * FIXED_W))
    field = {}
    for k, vector in zip(P, vectors):
        assert not is_zero_vector(vector)
        field[k] = vector
        field[negk(k)] = vector
    assert len(field) == 8
    assert_transverse(field)
    assert_parity(field, 1)
    return field


def run_science(result):
    assert polynomial_at(ROOT_LO) > 0
    assert polynomial_at(ROOT_HI) < 0
    assert ROOT_LO < ROOT_HI < -F(D1, 2 * D2)
    assert ALPHA * ALPHA + ALPHA * F(D1, D2) + F(D0, D2) == 0
    initial = fixed_initial_field()
    result["fixed_input"] = {
        "minimal_polynomial_ascending": [D0, D1, D2],
        "selected_embedding": "smaller_real_root",
        "root_isolation_open": [qstr(ROOT_LO), qstr(ROOT_HI)],
        "v": "1", "w": qrecord(FIXED_W), "nu": "1",
        "initial_full_eight_mode_field_real": field_record(initial)}
    stats = {}
    h1, stats["H1_Q_a_a"] = full_ordered_vertex(initial, initial)
    h2left, stats["H2_left_Q_a_H1"] = full_ordered_vertex(initial, h1)
    h2right, stats["H2_right_Q_H1_a"] = full_ordered_vertex(h1, initial)
    h2 = field_scale(F(1, 2), field_add(h2left, h2right))
    assert_parity(h1, -1)
    assert_parity(h2, 1)
    result["H1"] = {"physical_phase": "-i", "full_coefficients_stripped": field_record(h1)}
    result["H2"] = {"physical_phase": "-1", "full_coefficients_stripped": field_record(h2)}
    # All frequencies are computed in each third-gate convolution.
    # K4 extraction is only after these full fields have been formed.
    pure, stats["root_Q_H1_H1"] = full_ordered_vertex(h1, h1)
    mixed13, stats["root_Q_a_H2"] = full_ordered_vertex(initial, h2)
    mixed31, stats["root_Q_H2_a"] = full_ordered_vertex(h2, initial)
    w0 = field_scale(F(1, 3), pure)
    m13 = field_scale(F(1, 3), mixed13)
    m31 = field_scale(F(1, 3), mixed31)
    m0 = field_add(m13, m31)
    h3 = field_add(w0, m0)
    assert_parity(w0, -1)
    assert_parity(m13, -1)
    assert_parity(m31, -1)
    assert_parity(h3, -1)
    result["complete_convolution_statistics"] = stats
    signed_receivers = []
    for suffix in product((-1, 1), repeat=3):
        signs = (1,) + suffix
        k = tuple(sum(signs[j] * P[j][i] for j in range(4)) for i in range(3))
        signed_receivers.append((signs, k))
        signed_receivers.append((tuple(-s for s in signs), negk(k)))
    assert len({k for signs, k in signed_receivers}) == 16
    assert all(k != (0, 0, 0) for signs, k in signed_receivers)
    # These checks supplement, not replace, the length-11 relation proof.
    assert all(k not in initial and k not in h1 and k not in h2
               for signs, k in signed_receivers)
    rows = []
    passed = []
    unresolved_sign = False
    for signs, k in signed_receivers:
        c = w0.get(k, ZERO)
        z13, z31 = m13.get(k, ZERO), m31.get(k, ZERO)
        z = m0.get(k, ZERO)
        assert z == vadd(z13, z31)
        assert h3.get(k, ZERO) == vadd(c, z)
        assert w0.get(negk(k), ZERO) == vscale(-1, c)
        assert m0.get(negk(k), ZERO) == vscale(-1, z)
        c2, z2 = norm_square(c), norm_square(z)
        czero, zzero = is_zero_vector(c), is_zero_vector(z)
        assert (c2 == 0) == czero
        assert (z2 == 0) == zzero
        margin = c2 - 64 * z2
        certificate = sign_certificate(margin)
        sign = certificate["sign"]
        if sign is None:
            status = "NOT_CERTIFIED_SIGN"
            passes = None
            unresolved_sign = True
        elif czero:
            status = "FAIL_ZERO_SUPPLY"
            passes = False
        elif sign < 0:
            status = "FAIL_RATIO"
            passes = False
        else:
            status = "PASS_EQUALITY" if sign == 0 else "PASS_STRICT"
            passes = True
            passed.append(k)
        rows.append({
            "signs": list(signs), "frequency": list(k),
            "is_pair_representative_sigma1_positive": signs[0] == 1,
            "physical_phase_all_four_leaf_vectors": "+i",
            "C_W0_stripped": vrecord(c), "Z_M0_stripped": vrecord(z),
            "M13_stripped": vrecord(z13), "M31_stripped": vrecord(z31),
            "H3_stripped": vrecord(h3.get(k, ZERO)),
            "C_zero": czero, "Z_zero": zzero,
            "C_Hermitian_norm_squared": qrecord(c2),
            "Z_Hermitian_norm_squared": qrecord(z2),
            "margin_C2_minus_64Z2": qrecord(margin),
            "margin_sign_certificate": certificate,
            "passes_BE1": passes, "status": status})
    result["all_16_receivers"] = rows
    result["outside_K4"] = {
        "computed_in_all_root_convolutions": True,
        "not_removed_from_any_claimed_NS_equation": True,
        "full_H3_nonzero_mode_count": len(h3),
        "raw_root_output_scope": "all K4 vectors stored; no higher NS iterate computed"}
    if unresolved_sign:
        result["outcome"] = "NOT_CERTIFIED_UNRESOLVED_RECEIVER_SIGN"
        result["complete_G"] = None
        result["formal_self_interaction"] = {"execution": "skipped_due_to_unresolved_G"}
        return
    g = set(passed)
    assert all(negk(k) in g for k in g)
    result["complete_G"] = [list(k) for k in sorted(g)]
    representatives = [(signs, k) for signs, k in signed_receivers
                       if signs[0] == 1 and k in g]
    assert len(g) == 2 * len(representatives)
    bounds = [pair_supply_lower_bound(k, w0[k]) for signs, k in representatives]
    result["pair_supply_lower_bounds"] = bounds
    all_bounds_certified = all(item["status"] == "certified" for item in bounds)
    if bounds and all_bounds_certified:
        values = [F(item["pair_A0_supply_lower_rational"]) for item in bounds]
        result["minimum_pair_supply_lower_rational"] = qstr(min(values))
        result["aggregate_supply_lower_rational"] = qstr(sum(values, F(0)))
    else:
        result["minimum_pair_supply_lower_rational"] = None
        result["aggregate_supply_lower_rational"] = None
    rank_certificate = frequency_rank(g)
    result["frequency_rank_certificate"] = rank_certificate
    if not all_bounds_certified:
        result["outcome"] = "NOT_CERTIFIED_PAIR_LOWER_BOUND"
        result["formal_self_interaction"] = {"execution": "skipped_due_to_unresolved_pair_bound"}
        return
    if rank_certificate["rank"] < 3:
        result["formal_self_interaction"] = {"execution": "strictly_skipped_rank_below_three"}
        result["outcome"] = ("NO_NONZERO_SUPPLY_PAIR_IN_BE1" if not g
                             else "THREE_DIMENSIONAL_RECEIVER_PREMISE_NOT_PASSED")
        return
    # Conditional check ONCE, on the WHOLE selected leading field.
    leading_g = {k: w0[k] for k in g}
    form, form_stats = full_ordered_vertex(leading_g, leading_g)
    assert_parity(form, -1)
    result["formal_self_interaction"] = {
        "execution": "performed_once_rank_three",
        "input": "whole P_G W0, not one pair or a reset initial datum",
        "formula": "B(i*C,i*C)=i*Q(C,C)",
        "physical_phase": "+i", "time_integral_factor": "none",
        "is_actual_v7_or_actual_third_generation": False,
        "complete_ordered_convolution_statistics": form_stats,
        "identically_zero": not bool(form),
        "all_nonzero_output_coefficients_stripped": field_record(form)}
    result["outcome"] = ("RANK_THREE_LEADING_FORMAL_SELF_INTERACTION_ZERO" if not form
                         else "RANK_THREE_LEADING_FORMAL_SELF_INTERACTION_NONZERO")


def timeout_handler(signum, frame):
    raise TimeoutError("fixed 60-second scientific wall budget exceeded")


def validate_hash(value, name):
    if len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
        raise ValueError(name + " must be a lowercase SHA-256")


def self_resources():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    rss = usage.ru_maxrss if sys.platform == "darwin" else 1024 * usage.ru_maxrss
    return {"user_cpu_seconds": usage.ru_utime, "system_cpu_seconds": usage.ru_stime,
            "maximum_resident_set_bytes_RUSAGE_SELF": rss,
            "scope": "this Python process only, through this measurement; excludes children"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-commit", required=True,
                        help="parent-provided commit containing this frozen source; metadata only")
    parser.add_argument("--contract-sha", required=True,
                        help="parent-confirmed final contract SHA-256; metadata only")
    args = parser.parse_args()
    validate_hash(args.contract_sha, "contract-sha")
    if len(args.source_commit) < 7 or any(
            c not in "0123456789abcdef" for c in args.source_commit):
        raise ValueError("source-commit must be a hexadecimal provenance identifier")
    if OUTPUT.exists():
        raise FileExistsError("refusing to replace an existing experiment output")
    began = time.perf_counter()
    uname = os.uname()
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    actual_contract_sha = hashlib.sha256((HERE / "CONTRACT.md").read_bytes()).hexdigest()
    record = {
        "source_sha256": source_sha,
        "source_commit_parent_supplied": args.source_commit,
        "commit_verification": "no Git used in this process; parent records source freeze",
        "expected_final_contract_sha256": args.contract_sha,
        "actual_contract_sha256": actual_contract_sha,
        "command_argv": [sys.executable] + sys.argv,
        "working_directory": os.getcwd(),
        "inherited_exact_input_provenance": {
            "algebra_text_sha256": INHERITED_ALGEBRA_SHA,
            "previous_program_sha256": INHERITED_PROGRAM_SHA,
            "previous_output_sha256": INHERITED_OUTPUT_SHA,
            "scope": "fixed quadratic field, smaller embedding, normalized w; not a new independent derivation"},
        "environment": {"python": sys.version, "executable": sys.executable,
                        "os_uname": {"sysname": uname.sysname, "release": uname.release,
                                     "version": uname.version, "machine": uname.machine},
                        "logical_cpu_count": os.cpu_count(),
                        "scientific_processes": 1, "scientific_worker_threads": 1,
                        "third_party_libraries": [], "platform_module_used": False,
                        "external_metadata_processes_started": False,
                        "scientific_floating_point_used": False},
        "budget": {"wall_seconds": MAX_WALL_SECONDS,
                   "self_rss_target_bytes": MAX_SELF_RSS_BYTES,
                   "output_bytes_limit": MAX_OUTPUT_BYTES,
                   "bisections_per_sign_maximum": MAX_BISECTIONS},
        "result": {
            "arithmetic": "exact Fraction/integer quadratic field and rational root isolation",
            "not_certified_here": ["actual NS window and all infinite tails",
                                   "actual v7 or any further NS iterate",
                                   "template matching, amplification, iteration, singularity"]}}
    exit_status = 0
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(MAX_WALL_SECONDS)
    try:
        assert actual_contract_sha == args.contract_sha, "final contract byte mismatch"
        run_science(record["result"])
        record["execution_status"] = "completed"
        if record["result"].get("outcome", "").startswith("NOT_CERTIFIED"):
            exit_status = 1
    except Exception:
        exit_status = 1
        record["execution_status"] = "NOT_CERTIFIED"
        record["failure"] = traceback.format_exc()
    finally:
        signal.alarm(0)
    science_ended = time.perf_counter()
    record["resource_evidence_before_serialization"] = self_resources()
    record["resource_evidence_before_serialization"]["wall_from_main_seconds"] = science_ended - began
    # Serialize once before measuring resources again, so the record clearly
    # states how much of serialization its RUSAGE_SELF evidence covers.
    content = json.dumps(record, ensure_ascii=False, indent=2) + "\n"
    final_usage = self_resources()
    final_usage["wall_from_main_seconds"] = time.perf_counter() - began
    final_usage["measurement_boundary"] = (
        "after one complete result serialization, before adding this metadata and final write")
    record["resource_evidence_after_first_serialization"] = final_usage
    if final_usage["maximum_resident_set_bytes_RUSAGE_SELF"] > MAX_SELF_RSS_BYTES:
        exit_status = 1
        record["execution_status"] = "NOT_CERTIFIED_SELF_RSS_TARGET_EXCEEDED"
    if final_usage["wall_from_main_seconds"] > MAX_WALL_SECONDS:
        exit_status = 1
        record["execution_status"] = "NOT_CERTIFIED_WALL_BOUND_EXCEEDED"
    content = json.dumps(record, ensure_ascii=False, indent=2) + "\n"
    encoded = content.encode("utf-8")
    if len(encoded) >= MAX_OUTPUT_BYTES:
        exit_status = 1
        record = {"execution_status": "NOT_CERTIFIED_OUTPUT_LIMIT_EXCEEDED",
                  "source_sha256": source_sha, "source_commit_parent_supplied": args.source_commit,
                  "actual_contract_sha256": actual_contract_sha,
                  "attempted_output_bytes": len(encoded),
                  "resource_evidence_after_first_serialization": final_usage,
                  "raw_result_status": "not stored beyond the fixed output budget; no rerun"}
        content = json.dumps(record, ensure_ascii=False, indent=2) + "\n"
        encoded = content.encode("utf-8")
    with OUTPUT.open("xb") as handle:
        handle.write(encoded)
    print(json.dumps({"execution_status": record["execution_status"],
                      "scientific_outcome": record.get("result", {}).get("outcome"),
                      "source_sha256": source_sha,
                      "output_path": str(OUTPUT), "output_bytes": len(encoded),
                      "output_sha256": hashlib.sha256(encoded).hexdigest(),
                      "resources": final_usage}, ensure_ascii=False, indent=2))
    return exit_status


if __name__ == "__main__":
    sys.exit(main())
