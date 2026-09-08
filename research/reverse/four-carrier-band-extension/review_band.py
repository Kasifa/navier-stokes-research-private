#!/usr/bin/env python3
"""Nonauthor fixed-band verifier; execution needs separate parent authorization.

Independent mathematical organization: explicit ordered trees and permutations,
cross-product Leray, rational polynomial pairs, one fixed real embedding.
Core formed before reading the final author's files.  The adapter was added
after their stop and full reads; this is not a third blind construction.
Exactly one invocation is permitted after the parent's separate confirmation.
"""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import os
import resource
import signal
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
OUT = HERE / "review-band-output.json"
BASE_BINDINGS = {
    "CONTRACT.md": "8687b89a22dd0788e826453f143d8aaef2fd566446f23319cfdb734a3494225e",
    "SOURCE_WINDOW.md": "16a38027facd09455fb9e9b241a377e5867d82664d4367f5fe7dc7d279ed9285",
    "../four-carrier-source-test/INDEPENDENT_ALGEBRA.md":
        "a87cdef2cc2517e391ee193c3ad17b0e6776af3d7b8dff8f0427c2b063e08d1a",
    "../four-carrier-source-test/independent-output.json":
        "de084e897e08c7faa48dd49dbb00af61f0449587b34e8a4890711c4a176a0bc7",
}
REFERENCE_BINDINGS = {
    "exact_band.py": "2498b4d0ad430f467a48c15e5ca7d7891cbf44b97e35e506ba8d8642f1a8dc2c",
    "exact-band-output.json": "672265033fcbc05fb7881374d703a673bc2779d20b0612e67adb14f4dd068668",
    "ALGEBRA.md": "1874c7c34d24c52572f2d046d0786a853942e15f6acd28b8c9bb25b80d4262e7",
    "PROOF.md": "ef58ab47c42ecb77d1854b7af56ec371dc06f44cbbeedaa971ad8f0b4546705c",
    "OUTCOME.md": "98211024b66cac8d5e1050a26b65ba45fa83807359941405f7dd172e0d863eb7",
    "SOURCES.md": "cab14c17b22a58633c246916628602d21064e1cd58c2f01898af8e248338f2d9",
    "BAND_SCOPE_NOTE.md": "e49d298c04d2a7f47caf84762ed9510235dd0bd5916e6c7641b02748d2ff7779",
}
AUTHORIZATION_FLAG = "--run-once-after-parent-authorization"
PARENT_DECLARED_PRECOMPUTATION_COMMIT = "1dea1d349b6073bec9e2afacff927044184b2586"
P = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 3, 5))
FC, FB, FA = map(F, (37138824124764, 104767331941035, 73555298559275))
ALPHA_LO = -F(55889541592004, 73555298559275)
ALPHA_HI = -F(111779083184007, 147110597118550)
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
THETA = (F(0), F(1))
LEAF = "*"
PAIR = (LEAF, LEAF)
SHAPES = (((PAIR, LEAF), LEAF), ((LEAF, PAIR), LEAF),
          (PAIR, PAIR), (LEAF, (PAIR, LEAF)), (LEAF, (LEAF, PAIR)))


def qadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qscale(c, x):
    return (c * x[0], c * x[1])


def qneg(x):
    return qscale(-1, x)


def qmul(x, y):
    quadratic = x[1] * y[1]
    return (x[0] * y[0] - quadratic * FC / FA,
            x[0] * y[1] + x[1] * y[0] - quadratic * FB / FA)


def qsum(values):
    total = ZERO
    for x in values:
        total = qadd(total, x)
    return total


def vadd(x, y):
    return tuple(qadd(a, b) for a, b in zip(x, y))


def vscale(c, x):
    return tuple(qscale(c, a) for a in x)


def frequency_dot_vector(k, v):
    return qsum(qscale(c, a) for c, a in zip(k, v))


def frequency_cross_vector(k, v):
    return (qadd(qscale(k[1], v[2]), qscale(-k[2], v[1])),
            qadd(qscale(k[2], v[0]), qscale(-k[0], v[2])),
            qadd(qscale(k[0], v[1]), qscale(-k[1], v[0])))


def vertex(p, q, x, y):
    """Real stripped coefficient P_(p+q)((x dot q)y), retaining order."""
    k = tuple(a + b for a, b in zip(p, q))
    assert frequency_dot_vector(p, x) == ZERO
    assert frequency_dot_vector(q, y) == ZERO
    derivative = frequency_dot_vector(q, x)
    if k == (0, 0, 0):
        assert derivative == ZERO
        return k, (ZERO, ZERO, ZERO)
    # k cross (y cross k) = -k cross (k cross y).
    transverse = vscale(-F(1, sum(c * c for c in k)),
                        frequency_cross_vector(k, frequency_cross_vector(k, y)))
    value = tuple(qmul(derivative, component) for component in transverse)
    assert frequency_dot_vector(k, value) == ZERO
    return k, value


def shape_name(shape):
    return "*" if shape == LEAF else "(" + shape_name(shape[0]) + "," + shape_name(shape[1]) + ")"


def explicit_tree(shape, ordering, signed_frequencies, seeds):
    if shape == LEAF:
        j = next(ordering)
        return signed_frequencies[j], seeds[j], 1
    p, x, nl = explicit_tree(shape[0], ordering, signed_frequencies, seeds)
    q, y, nr = explicit_tree(shape[1], ordering, signed_frequencies, seeds)
    k, value = vertex(p, q, x, y)
    return k, vscale(F(1, nl + nr - 1), value), nl + nr


def polynomial(t):
    return FA * t * t + FB * t + FC


def linear_interval(x, lo, hi):
    endpoints = (x[0] + x[1] * lo, x[0] + x[1] * hi)
    return min(endpoints), max(endpoints)


def certified_sign(x):
    """Each query refines the same smaller root, at most 128 bisections."""
    if x == ZERO:
        return 0, {"sign": 0, "method": "exact zero polynomial pair", "bisections": 0}
    lo, hi = ALPHA_LO, ALPHA_HI
    for step in range(129):
        lower, upper = linear_interval(x, lo, hi)
        if lower > 0 or upper < 0:
            sign = 1 if lower > 0 else -1
            return sign, {"sign": sign, "alpha_interval": [str(lo), str(hi)],
                          "value_interval": [str(lower), str(upper)], "bisections": step}
        if step == 128:
            break
        mid = (lo + hi) / 2
        value = polynomial(mid)
        assert value != 0  # The fixed quadratic is irreducible over Q.
        if value > 0:
            lo = mid
        else:
            hi = mid
    raise ArithmeticError("NOT_CERTIFIED: fixed-root sign exceeded 128 bisections")


def squared_norm(v):
    # All vectors here have had their common physical i removed.
    return qsum(qmul(component, component) for component in v)


def qjson(x):
    return {"constant": str(x[0]), "alpha": str(x[1])}


def vjson(v):
    return [qjson(x) for x in v]


def exact_rank(frequencies):
    rows = [list(map(F, k)) for k in frequencies]
    rank, pivots = 0, []
    for col in range(3):
        pivot = next((j for j in range(rank, len(rows)) if rows[j][col] != 0), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        factor = rows[rank][col]
        rows[rank] = [x / factor for x in rows[rank]]
        for j in range(len(rows)):
            if j != rank:
                factor = rows[j][col]
                rows[j] = [x - factor * y for x, y in zip(rows[j], rows[rank])]
        pivots.append(col)
        rank += 1
    return rank, {"pivot_columns": pivots, "row_reduced": [[str(x) for x in row] for row in rows]}


def prepare_seeds():
    w = (F(111626564931091, 129542798481515),
         F(1009178696233253, 466354074533454))
    u4 = (qadd((F(3), F(0)), qscale(5, w)), (F(-2), F(0)), qscale(-2, w))
    seeds = ((ZERO, ONE, THETA), (ZERO, ZERO, ONE), (ONE, ZERO, ZERO), u4)
    assert all(frequency_dot_vector(k, v) == ZERO for k, v in zip(P, seeds))
    return w, seeds


def compute_fixed_band(progress):
    # All checks concern the already selected root; no alpha probes occur.
    assert ALPHA_LO < ALPHA_HI < -FB / (2 * FA)
    assert polynomial(ALPHA_LO) > 0 and polynomial(ALPHA_HI) < 0
    discriminant = FB * FB - 4 * FA * FC
    assert 7011751242972 ** 2 < discriminant < 7011751242973 ** 2
    assert qadd(qadd(qscale(FA, qmul(THETA, THETA)), qscale(FB, THETA)),
                (FC, F(0))) == ZERO
    w, seeds = prepare_seeds()
    progress["normalization"] = {"alpha_embedding": "smaller real root",
                                 "v": "1", "w": qjson(w)}
    progress["receiver_rows"] = []
    raw = {}
    count = 0
    for signs in product((1, -1), repeat=4):
        signed = tuple(tuple(signs[j] * x for x in P[j]) for j in range(4))
        k = tuple(sum(p[i] for p in signed) for i in range(3))
        assert k != (0, 0, 0) and k not in raw
        shapes = {}
        for shape in SHAPES:
            total = (ZERO, ZERO, ZERO)
            for order in permutations(range(4)):
                output_k, term, size = explicit_tree(shape, iter(order), signed, seeds)
                assert output_k == k and size == 4
                total = vadd(total, term)
                count += 1
            shapes[shape_name(shape)] = total
        c = shapes[shape_name((PAIR, PAIR))]
        z = (ZERO, ZERO, ZERO)
        for shape in SHAPES:
            if shape != (PAIR, PAIR):
                z = vadd(z, shapes[shape_name(shape)])
        cc, zz = squared_norm(c), squared_norm(z)
        margin = qadd(cc, qscale(-64, zz))
        sign, sign_proof = certified_sign(margin)
        c_nonzero = any(x != ZERO for x in c)
        passed = c_nonzero and sign >= 0
        row = {"signs": list(signs), "k": list(k),
               "physical_phase_C_Z": "i times the real polynomial-pair vector",
               "shapes_stripped": {name: vjson(vector) for name, vector in shapes.items()},
               "C_stripped": vjson(c), "Z_stripped": vjson(z),
               "C_norm_squared": qjson(cc), "Z_norm_squared": qjson(zz),
               "threshold_margin": qjson(margin), "margin_certificate": sign_proof,
               "C_nonzero": c_nonzero, "threshold_pass": passed}
        progress["receiver_rows"].append(row)
        raw[k] = {"signs": signs, "C": c, "Z": z, "passed": passed, "row": row}
    assert len(raw) == 16 and count == 1920
    for k, row in raw.items():
        opposite = raw[tuple(-c for c in k)]
        assert opposite["C"] == vscale(-1, row["C"])
        assert opposite["Z"] == vscale(-1, row["Z"])
        assert opposite["passed"] == row["passed"]
    selected = {k: row for k, row in raw.items() if row["passed"]}
    rank, rank_proof = exact_rank(sorted(selected))
    progress["G_all_signed"] = [list(k) for k in sorted(selected)]
    progress["G_rank"] = rank
    progress["rank_certificate"] = rank_proof
    progress["root_ordered_terms"] = count
    progress["pair_lower_bounds"] = []
    lower_bounds = []
    for k, row in selected.items():
        if row["signs"][0] != 1:
            continue
        index = next(i for i, x in enumerate(row["C"]) if x != ZERO)
        sign, proof = certified_sign(row["C"][index])
        lower, upper = map(F, proof["value_interval"])
        ell = lower if sign > 0 else -upper
        assert ell > 0
        # ell <= |one component| <= |C_k| <= 2|C_k| = w_k.
        lower_bounds.append(ell)
        progress["pair_lower_bounds"].append(
            {"representative": list(k), "component_zero_based": index,
             "component_stripped": qjson(row["C"][index]), "component_certificate": proof,
             "ell_pair": str(ell), "pair_factor_two_not_needed_for_this_lower_bound": True})
    e = 80 * 29 ** 4 * 7 ** 5 + 3 * 29 * 812 ** 4
    assert e == 38772884140592
    if selected:
        assert len(lower_bounds) * 2 == len(selected)
        ell = min(lower_bounds)
        tg = min(F(1, 1624), ell / (32 * e), F(1, 76484296))
        assert tg > 0 and 32 * e * tg <= ell
        assert 812 * tg <= F(1, 2)
        assert 38242148 * tg <= F(1, 2)
        assert F(1, 8) + F(1, 32) == F(5, 32)
        assert F(31, 32) - F(5, 32) == F(13, 16)
        assert F(1, 4) - F(5, 31) == F(11, 124) > 0
        progress["BW_rational_budget"] = {
            "ell_min": str(ell), "E": str(e), "T_G": str(tg),
            "source_lower_fraction": "31/32", "target_lower_fraction": "13/16",
            "numerator_upper_fraction": "5/32", "ratio_upper": "5/31",
            "strict_margin_below_one_quarter": "11/124",
            "all_pairs_and_aggregate_share_this_window": True,
            "scope": "Exact arithmetic for previously hand-proved conditional BW.1-4"}
    else:
        progress["BW_rational_budget"] = {"status": "NOT_APPLICABLE_EMPTY_G"}
    if rank != 3:
        progress["formal_shape_self_action"] = {"status": "SKIPPED_RANK_NOT_THREE"}
    else:
        coefficients = {}
        for p, left in selected.items():
            for q, right in selected.items():
                k, term = vertex(p, q, left["C"], right["C"])
                coefficients[k] = vadd(coefficients.get(k, (ZERO, ZERO, ZERO)), term)
        # B(i C, i C)=i Q(C,C), so the returned stripped coefficient has + sign.
        assert coefficients.get((0, 0, 0), (ZERO, ZERO, ZERO)) == (ZERO, ZERO, ZERO)
        for k, value in coefficients.items():
            assert coefficients[tuple(-x for x in k)] == vscale(-1, value)
        progress["formal_shape_self_action"] = {
            "status": "COMPUTED_ONCE", "physical_phase": "i times stripped coefficient",
            "all_outputs": [{"k": list(k), "coefficient_stripped": vjson(v)}
                            for k, v in sorted(coefficients.items())],
            "nonzero": any(any(x != ZERO for x in v) for v in coefficients.values()),
            "not_actual_v7": True}
    return raw


def compare_final_author_certificate(progress, raw):
    """Compare independent 16-row trees with the stopped full-convolution output."""
    source = json.loads((HERE / "exact-band-output.json").read_text(encoding="utf-8"))
    assert source["execution_status"] == "completed"
    assert source["source_sha256"] == REFERENCE_BINDINGS["exact_band.py"]
    assert source["actual_contract_sha256"] == BASE_BINDINGS["CONTRACT.md"]
    assert source["expected_final_contract_sha256"] == BASE_BINDINGS["CONTRACT.md"]
    assert source["source_commit_parent_supplied"] == PARENT_DECLARED_PRECOMPUTATION_COMMIT
    result = source["result"]
    fixed = result["fixed_input"]
    assert list(map(F, fixed["minimal_polynomial_ascending"])) == [FC, FB, FA]
    assert fixed["selected_embedding"] == "smaller_real_root"
    assert list(map(F, fixed["root_isolation_open"])) == [ALPHA_LO, ALPHA_HI]
    assert F(fixed["v"]) == 1 and F(fixed["nu"]) == 1
    w, seeds = prepare_seeds()
    assert read_q(fixed["w"]) == w
    expected_initial = {tuple(sign * x for x in k): v
                        for k, v in zip(P, seeds) for sign in (1, -1)}
    actual_initial = {tuple(map(int, k.split(","))): read_v(v)
                      for k, v in fixed["initial_full_eight_mode_field_real"].items()}
    assert actual_initial == expected_initial
    rows = result["all_16_receivers"]
    assert len(rows) == 16
    original = {tuple(row["frequency"]): row for row in rows}
    assert len(original) == 16 and original.keys() == raw.keys()
    for k, ours in raw.items():
        theirs = original[k]
        assert tuple(theirs["signs"]) == ours["signs"]
        assert theirs["is_pair_representative_sigma1_positive"] == (ours["signs"][0] == 1)
        assert theirs["physical_phase_all_four_leaf_vectors"] == "+i"
        shapes = ours["row"]["shapes_stripped"]
        m13 = vadd(read_v(shapes[shape_name(SHAPES[3])]),
                   read_v(shapes[shape_name(SHAPES[4])]))
        m31 = vadd(read_v(shapes[shape_name(SHAPES[0])]),
                   read_v(shapes[shape_name(SHAPES[1])]))
        for name, value in (("C_W0_stripped", ours["C"]),
                            ("Z_M0_stripped", ours["Z"]),
                            ("M13_stripped", m13), ("M31_stripped", m31),
                            ("H3_stripped", vadd(ours["C"], ours["Z"]))):
            assert read_v(theirs[name]) == value
        assert theirs["C_zero"] == all(x == ZERO for x in ours["C"])
        assert theirs["Z_zero"] == all(x == ZERO for x in ours["Z"])
        cc, zz = squared_norm(ours["C"]), squared_norm(ours["Z"])
        margin = qadd(cc, qscale(-64, zz))
        assert read_q(theirs["C_Hermitian_norm_squared"]) == cc
        assert read_q(theirs["Z_Hermitian_norm_squared"]) == zz
        assert read_q(theirs["margin_C2_minus_64Z2"]) == margin
        sign = verify_author_sign(theirs["margin_sign_certificate"], margin)
        assert sign == ours["row"]["margin_certificate"]["sign"]
        assert theirs["passes_BE1"] == ours["passed"]
        if theirs["C_zero"]:
            assert not ours["passed"]
        elif sign > 0:
            assert theirs["status"] == "PASS_STRICT"
        elif sign < 0:
            assert theirs["status"] == "FAIL_RATIO"
    selected = {k for k, row in raw.items() if row["passed"]}
    assert [list(k) for k in sorted(selected)] == result["complete_G"]
    rank = progress["G_rank"]
    rank_source = result["frequency_rank_certificate"]
    assert rank_source["rank"] == rank
    basis = [tuple(k) for k in rank_source["basis"]]
    assert all(k in selected for k in basis)
    assert len(basis) == rank and exact_rank(basis)[0] == rank
    assert exact_rank(basis + sorted(selected))[0] == rank
    if rank != 3:
        assert result["formal_self_interaction"]["execution"] == "strictly_skipped_rank_below_three"
        assert progress["formal_shape_self_action"]["status"] == "SKIPPED_RANK_NOT_THREE"
    else:
        # This artifact's stopped output is in the rank<3 branch.  A different
        # branch is not an authorized object and must not be silently adapted.
        raise ArithmeticError("Unexpected rank-three original; fixed-object review stops")
    representative_keys = {k for k in selected if raw[k]["signs"][0] == 1}
    supplied = result["pair_supply_lower_bounds"]
    assert len(supplied) == len(representative_keys)
    bound_keys = set()
    lower_bounds = []
    checked_bounds = []
    for item in supplied:
        k = tuple(item["representative"])
        assert k in representative_keys and k not in bound_keys
        bound_keys.add(k)
        assert item["status"] == "certified"
        j = item["coordinate_zero_based"]
        assert isinstance(j, int) and 0 <= j < 3
        component = raw[k]["C"][j]
        proof = item["sign_certificate"]
        sign = verify_author_sign(proof, component)
        assert sign in (-1, 1)
        lo, hi = F(proof["value_lower"]), F(proof["value_upper"])
        absolute_lower = min(abs(lo), abs(hi))
        ell = F(item["pair_A0_supply_lower_rational"])
        assert absolute_lower > 0
        assert F(item["component_absolute_lower_rational"]) == absolute_lower
        assert ell == 2 * absolute_lower
        # Hermitian pair norm is 2|C_k|.  This is the full conjugate-pair
        # factor, not an additional copy of an already paired source S_k.
        lower_bounds.append(ell)
        checked_bounds.append({"representative": list(k), "ell_pair": str(ell)})
    assert bound_keys == representative_keys
    if lower_bounds:
        ell_min = min(lower_bounds)
        assert F(result["minimum_pair_supply_lower_rational"]) == ell_min
        assert F(result["aggregate_supply_lower_rational"]) == sum(lower_bounds, F(0))
        budget = verify_window_budget(ell_min)
        # Explicit displayed BR.2 datum, checked against the raw certificate.
        br2 = F(31058644197216930893482616803633, 3138707406577797440120037955275)
        assert ell_min == br2 and len(lower_bounds) == 1
        budget["all_author_pair_bounds"] = checked_bounds
        progress["author_BR2_BR3_BW4_rational_budget"] = budget
    progress["author_comparison"] = {
        "fixed_initial_eight_vectors_equal": True,
        "all_signed_receiver_rows_compared": len(rows),
        "full_C_Z_M13_M31_H3_vectors_equal": True,
        "all_norms_margins_and_rational_sign_certificates_verified": True,
        "complete_G_and_rank_equal": True,
        "all_pair_lower_bounds_verified": True,
        "H1_H2_arrays": "Read in full and source code reviewed; not separately recomputed here",
        "outside_K4_root_arrays": "Not independently recomputed or stored by this label-tree verifier",
        "scope": "One fixed certificate comparison after author stop; not a third blind proof"}


def read_q(record):
    return F(record["constant"]), F(record["alpha"])


def read_v(record):
    assert len(record) == 3
    return tuple(read_q(x) for x in record)


def verify_author_sign(record, value):
    assert read_q(record["value"]) == value
    sign = record["sign"]
    assert sign in (-1, 0, 1)
    if value == ZERO:
        assert sign == 0 and record["method"] == "exact_quotient_zero"
        return sign
    if record["method"] == "rational":
        assert value[1] == 0 and value[0] != 0
        assert sign == (1 if value[0] > 0 else -1)
        return sign
    assert record["method"] == "smaller_root_rational_interval"
    assert isinstance(record["bisections"], int) and 0 <= record["bisections"] <= 128
    lo, hi = map(F, record["root_interval_open"])
    assert ALPHA_LO <= lo < hi <= ALPHA_HI < -FB / (2 * FA)
    assert polynomial(lo) > 0 and polynomial(hi) < 0
    lower, upper = linear_interval(value, lo, hi)
    assert F(record["value_lower"]) == lower and F(record["value_upper"]) == upper
    assert (sign == 1 and lower > 0) or (sign == -1 and upper < 0)
    return sign


def verify_window_budget(ell):
    e = 80 * 29 ** 4 * 7 ** 5 + 3 * 29 * 812 ** 4
    assert e == 38772884140592 and ell > 0
    candidates = (F(1, 1624), ell / (32 * e), F(1, 76484296))
    tg = min(candidates)
    assert tg > 0 and 32 * e * tg <= ell
    assert 812 * tg <= F(1, 2) and 38242148 * tg <= F(1, 2)
    numerator = F(1, 8) + F(1, 32)
    source_lower = 1 - F(1, 32)
    target_lower = source_lower - numerator
    ratio = numerator / source_lower
    assert (source_lower, numerator, target_lower, ratio) == (F(31, 32), F(5, 32), F(13, 16), F(5, 31))
    margin = F(1, 4) - ratio
    assert margin == F(11, 124) > 0
    return {"ell_min": str(ell), "E": str(e), "T_G": str(tg),
            "three_window_candidates": list(map(str, candidates)),
            "tail_budget_slack_ell_minus_32ET": str(ell - 32 * e * tg),
            "q_slack_to_half": str(F(1, 2) - 812 * tg),
            "first_band_slack_to_half": str(F(1, 2) - 38242148 * tg),
            "source_lower_fraction": str(source_lower), "numerator_upper_fraction": str(numerator),
            "target_lower_fraction": str(target_lower), "ratio_upper": str(ratio),
            "strict_margin_below_one_quarter": str(margin),
            "scope": "Same-run rational instance of hand-proved BW.1-4 and displayed BR.2-3"}


def deadline(signum, frame):
    raise TimeoutError("Single fixed-band verification exceeded 60 seconds")


def main():
    # This guard runs before any new scientific arithmetic or output creation.
    args = sys.argv[1:]
    if (len(args) != 3 or args[0] != AUTHORIZATION_FLAG
            or args[1] != "--reviewer-source-commit"
            or len(args[2]) != 40 or any(c not in "0123456789abcdef" for c in args[2])):
        raise SystemExit("NOT_AUTHORIZED: use the one-run flag only after parent confirmation")
    if OUT.exists():
        raise SystemExit("NO_RERUN: review-band-output.json already exists")
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, deadline)
    signal.alarm(60)
    record = {"review_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "base_bindings": BASE_BINDINGS, "reference_bindings": REFERENCE_BINDINGS,
              "parent_declared_precomputation_commit": PARENT_DECLARED_PRECOMPUTATION_COMMIT,
              "reviewer_source_commit_parent_supplied": args[2],
              "commit_status": "Parent-provided identifier; no Git verification by this reviewer",
              "command_argv": [sys.executable] + sys.argv,
              "working_directory": str(Path.cwd()),
              "environment": {"python": sys.version, "executable": sys.executable,
                              "uname": list(os.uname()), "logical_cpu_count": os.cpu_count(),
                              "scientific_workers": 1, "scientific_threads": 1,
                              "third_party_libraries": [], "subprocesses_started_by_verifier": 0,
                              "scientific_arithmetic": "Fraction and exact integers"},
              "result": {}}
    status = 0
    try:
        for bindings in (BASE_BINDINGS, REFERENCE_BINDINGS):
            for name, expected in bindings.items():
                assert hashlib.sha256((HERE / name).read_bytes()).hexdigest() == expected
        raw = compute_fixed_band(record["result"])
        compare_final_author_certificate(record["result"], raw)
        record["execution_status"] = "completed"
    except Exception:
        status = 1
        record["execution_status"] = "NOT_CERTIFIED"
        record["error"] = traceback.format_exc()
    finally:
        signal.alarm(0)
        usage = resource.getrusage(resource.RUSAGE_SELF)
        peak = usage.ru_maxrss if sys.platform == "darwin" else 1024 * usage.ru_maxrss
        record["resources"] = {"wall_seconds_before_serialization": time.perf_counter() - started,
                               "self_user_cpu_seconds": usage.ru_utime,
                               "self_system_cpu_seconds": usage.ru_stime,
                               "self_peak_resident_bytes": peak,
                               "not_process_tree_resource_accounting": True,
                               "metadata_only": True}
        if peak >= 256 * 1024 * 1024:
            status = 1
            record["execution_status"] = "NOT_CERTIFIED_RESOURCE_LIMIT"
        content = json.dumps(record, ensure_ascii=False, indent=2) + "\n"
        after = resource.getrusage(resource.RUSAGE_SELF)
        after_peak = after.ru_maxrss if sys.platform == "darwin" else 1024 * after.ru_maxrss
        after_wall = time.perf_counter() - started
        record["resources_after_first_serialization"] = {
            "wall_from_main_seconds": after_wall,
            "self_user_cpu_seconds": after.ru_utime,
            "self_system_cpu_seconds": after.ru_stime,
            "self_peak_resident_bytes": after_peak,
            "scope": "RUSAGE_SELF only; through first serialization; excludes final write and children"}
        if after_peak >= 256 * 1024 * 1024 or after_wall >= 60:
            status = 1
            record["execution_status"] = "NOT_CERTIFIED_RESOURCE_LIMIT"
        content = json.dumps(record, ensure_ascii=False, indent=2) + "\n"
        if len(content.encode("utf-8")) >= 1024 * 1024:
            status = 1
            record["execution_status"] = "NOT_CERTIFIED_OUTPUT_LIMIT"
            content = json.dumps({"execution_status": record["execution_status"],
                                  "review_source_sha256": record["review_source_sha256"]}) + "\n"
        with OUT.open("xb") as handle:
            handle.write(content.encode("utf-8"))
        print(json.dumps({"execution_status": record["execution_status"],
                          "G_rank": record["result"].get("G_rank"),
                          "resources": record["resources"],
                          "output_sha256": hashlib.sha256(OUT.read_bytes()).hexdigest()}, indent=2))
    return status


if __name__ == "__main__":
    sys.exit(main())
