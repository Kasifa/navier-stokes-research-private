#!/usr/bin/env python3
"""One independent exact check of the locked four-carrier certificate.

No imports from the author's programs. Coefficients are checked using the five
ordered binary tree shapes, permutations of four distinct leaves, and symbolic
linear polynomials in alpha, rather than full Fourier convolution/interpolation.
Root bounds are checked by monotonic fractional-linear functions after reduction.
This does not numerically solve NS or certify the analytic tail proof.
"""
from fractions import Fraction as F
from itertools import permutations
from math import gcd, isqrt
from pathlib import Path
import hashlib
import json
import os
import platform
import resource
import signal
import sys
import time

BASE = Path(__file__).resolve().parent
INPUTS = (
    "CONTRACT.md", "CONTRACT_REVIEW.md", "PROOF.md", "exact_screen.py",
    "certify_root.py", "exact-output.json", "root-certificate.json",
)
P = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 3, 5))
TARGET = (3, 4, 6)
TREES = (
    (((0, 1), 2), 3),
    ((0, (1, 2)), 3),
    ((0, 1), (2, 3)),
    (0, ((1, 2), 3)),
    (0, (1, (2, 3))),
)


def trim(p):
    p = tuple(F(x) for x in p)
    while len(p) > 1 and p[-1] == 0:
        p = p[:-1]
    return p


def padd(p, q):
    n = max(len(p), len(q))
    return trim((p[j] if j < len(p) else 0)
                + (q[j] if j < len(q) else 0) for j in range(n))


def pscale(p, c):
    return trim(c * x for x in p)


def pmul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for j, x in enumerate(p):
        for k, y in enumerate(q):
            r[j + k] += x * y
    return trim(r)


def peval(p, x):
    ans = F(0)
    for a in reversed(p):
        ans = ans * x + a
    return ans


def vadd(u, v):
    return tuple(padd(x, y) for x, y in zip(u, v))


def vscale(u, c):
    return tuple(pscale(x, c) for x in u)


ZV = ((F(0),),) * 3


def dotpoly(k, u):
    ans = (F(0),)
    for x, y in zip(k, u):
        ans = padd(ans, pscale(y, x))
    return ans


def tree_value(tree, perm, basis, sign):
    if isinstance(tree, int):
        leaf = perm[tree]
        k = tuple(sign * z for z in P[leaf])
        u = (
            ((0,), (1,), (0, 1)),
            ((0,), (0,), (1,)),
            ((1,), (0,), (0,)),
            (((3,), (-2,), (0,)) if basis == 0
             else ((5,), (0,), (-2,))),
        )[leaf]
        u = tuple(trim(x) for x in u)
        assert dotpoly(k, u) == (0,)
        return k, u, 1
    r, u, nl = tree_value(tree[0], perm, basis, sign)
    s, v, nr = tree_value(tree[1], perm, basis, sign)
    k = tuple(x + y for x, y in zip(r, s))
    assert k != (0, 0, 0)
    # Q at this ordered vertex, followed by exact time-monomial integration.
    raw = tuple(pmul(dotpoly(s, u), x) for x in v)
    kk = sum(x * x for x in k)
    longitudinal = dotpoly(k, raw)
    projected = tuple(padd(x, pscale(longitudinal, -F(ki, kk)))
                      for ki, x in zip(k, raw))
    out = vscale(projected, F(1, nl + nr - 1))
    assert dotpoly(k, out) == (0,)
    assert all(len(x) <= 2 for x in out)  # alpha occurs in exactly one leaf.
    return k, out, nl + nr


def pmod(p, d):
    r = trim(p)
    while len(r) >= len(d) and r != (0,):
        deg = len(r) - len(d)
        sub = (F(0),) * deg + pscale(d, -r[-1] / d[-1])
        r = padd(r, sub)
    return r


def mobius_range(num, den, interval):
    """Exact endpoint range: (a+b*x)/(c+d*x) has constant derivative sign."""
    assert len(num) <= 2 and len(den) <= 2
    l, r = interval
    dl, dr = peval(den, l), peval(den, r)
    assert dl * dr > 0
    values = (peval(num, l) / dl, peval(num, r) / dr)
    return min(values), max(values)


def inside(inner, outer):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def ceil_fraction(x):
    return (x.numerator + x.denominator - 1) // x.denominator


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def enc(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [enc(y) for y in x]
    return x


def main():
    started = time.monotonic()
    signal.alarm(60)
    hashes = {name: sha(BASE / name) for name in INPUTS}
    raw = json.loads((BASE / "exact-output.json").read_text())
    cert = json.loads((BASE / "root-certificate.json").read_text())
    assert cert["input_sha256"] == hashes["exact-output.json"]
    assert tuple(map(tuple, raw["p"])) == P
    assert tuple(raw["target"]) == TARGET
    assert raw["finite_leaf_hits"] == {
        "1": [], "2": [], "3": [], "4": [[0, 1, 2, 3]]}
    # Independent non-enumerative support argument is checked in MAIN_REVIEW:
    # relation kernel = Z*(-2,-3,-5,1), minimal nonzero l1 length 11 > 8.
    assert P[3] == tuple(2 * P[0][j] + 3 * P[1][j] + 5 * P[2][j]
                         for j in range(3))
    assert sum(abs(x) for x in (-2, -3, -5, 1)) > 8
    signed = P + tuple(tuple(-x for x in p) for p in P)
    L = {tuple(x + y for x, y in zip(r, s))
         for r in signed for s in signed} - {(0, 0, 0)}
    assert len(L) == raw["L_cardinality"] == 32
    assert L.isdisjoint(signed)

    computed = {"W": [None, None], "M": [None, None]}
    terms = {"W": 0, "M": 0}
    for basis in (0, 1):
        totals = {}
        for sign in (1, -1):
            total = {"W": ZV, "M": ZV}
            for tree_index, tree in enumerate(TREES):
                group = "W" if tree_index == 2 else "M"
                for perm in permutations(range(4)):
                    k, val, n = tree_value(tree, perm, basis, sign)
                    assert n == 4
                    assert k == tuple(sign * z for z in TARGET)
                    total[group] = vadd(total[group], val)
                    terms[group] += 1
            totals[sign] = total
        for name in computed:
            assert totals[-1][name] == vscale(totals[1][name], -1)
            computed[name][basis] = totals[1][name]
    # (-i)^3=i; odd real coefficient parity supplies the actual conjugate mode.
    phase = (1, 0)  # exact integer real/imaginary pair
    for _ in range(3):
        phase = (phase[1], -phase[0])  # multiply by -i
    assert phase == (0, 1)
    matrices = {}
    for name in ("W", "M"):
        matrices[name] = tuple(tuple(computed[name][j][i] for j in (0, 1))
                               for i in range(3))
        observed = tuple(tuple(trim(p) for p in row)
                         for row in raw["matrices_constant_first_polynomials"][name])
        assert matrices[name] == observed
        for alpha in (0, 1, -1):  # the locked three validation points only.
            for basis in (0, 1):
                val = tuple(peval(matrices[name][i][basis], F(alpha))
                            for i in range(3))
                assert val == tuple(map(F, raw["samples"][f"{alpha},{basis}"][name]))

    m, wmat = matrices["M"], matrices["W"]
    det = padd(pmul(m[0][0], m[1][1]), pscale(pmul(m[0][1], m[1][0]), -1))
    assert det == trim(raw["det_first_two_components"])
    kernel = (pscale(m[0][1], -1), m[0][0])
    assert kernel == tuple(trim(p) for p in raw["kernel_v_w"])
    for name in ("M", "W"):
        residual = tuple(pmod(padd(pmul(row[0], kernel[0]),
                                  pmul(row[1], kernel[1])), det)
                         for row in matrices[name])
        assert residual == tuple(trim(p) for p in raw["remainders_mod_det"][name])
    d = trim(cert["primitive_det_constant_first"])
    assert len(d) == 3 and d[2] > 0 and all(x.denominator == 1 for x in d)
    assert gcd(gcd(int(d[0]), int(d[1])), int(d[2])) == 1
    assert all(x == det[0] * y / d[0] for x, y in zip(det, d))
    disc = d[1] ** 2 - 4 * d[2] * d[0]
    assert disc == F(cert["discriminant"]) > 0
    n = isqrt(disc.numerator)
    assert n * n < disc < (n + 1) ** 2
    vertex = -d[1] / (2 * d[2])

    root_checks = []
    for index, item in enumerate(cert["roots_in_increasing_order"]):
        interval = tuple(map(F, item["alpha_interval"]))
        l, r = interval
        assert l < r
        if index == 0:
            assert r < vertex and peval(d, l) > 0 > peval(d, r)
        else:
            assert index == 1 and l > vertex and peval(d, l) < 0 < peval(d, r)
        # Derivative has fixed nonzero sign on either side of the vertex.
        # These two disjoint intervals therefore contain exactly all two roots.
        assert F(item["normalized_v"]) == 1
        wrange = mobius_range(pscale(m[0][0], -1), m[0][1], interval)
        assert inside(wrange, tuple(map(F, item["w_interval"])))
        residuals = tuple(pmod(padd(pmul(row[0], m[0][1]),
                                   pscale(pmul(row[1], m[0][0]), -1)), d)
                          for row in m)
        assert residuals == ((0,),) * 3
        assert residuals == tuple(trim(p) for p in item["M_residuals_mod_det"])
        output_ranges = []
        numerators = []
        for component, row in enumerate(wmat):
            numerator = pmod(padd(pmul(row[0], m[0][1]),
                                  pscale(pmul(row[1], m[0][0]), -1)), d)
            numerators.append(numerator)
            # Reduced expression agrees at the root; endpoints give an exact
            # enclosure there without treating alpha and w as independent.
            actual_range = mobius_range(numerator, m[0][1], interval)
            stated_range = tuple(map(F, item["W_real_component_intervals"][component]))
            assert inside(actual_range, stated_range)
            assert actual_range[0] * actual_range[1] > 0
            assert stated_range[0] * stated_range[1] > 0
            output_ranges.append(actual_range)
        assert tuple(numerators) == tuple(trim(p) for p in item["W_numerators_mod_det"])
        assert item["certified_nonzero_components"] == [0, 1, 2]
        root_checks.append({"alpha_interval": interval,
                            "w_mobius_endpoint_enclosure": wrange,
                            "W_root_reduced_enclosures": output_ranges})
    assert len(root_checks) == 2 and cert["selected_root_index"] == 0

    alpha_interval = tuple(map(F, cert["roots_in_increasing_order"][0]["alpha_interval"]))
    w_interval = tuple(map(F, cert["roots_in_increasing_order"][0]["w_interval"]))
    Abound = 16 + 2 * max(map(abs, alpha_interval)) + 14 * max(map(abs, w_interval))
    assert Abound <= cert["A_upper"] == ceil_fraction(Abound) == 29
    assert cert["K_upper"] == 7 and 38 < 7 ** 2
    lower = F(cert["W0_A0_lower"])
    first_stated = tuple(map(F, cert["roots_in_increasing_order"][0]["W_real_component_intervals"][0]))
    assert lower == min(map(abs, first_stated)) > 0
    assert lower <= min(map(abs, root_checks[0]["W_root_reduced_enclosures"][0]))
    A, K = 29, 7
    b = 4 * A * K
    E = 80 * A ** 4 * K ** 5 + 3 * A * b ** 4
    birth = 4 * K ** 2 + 2 * A * b ** 2
    assert b == 812
    assert E == cert["error_other_and_source_upper_coefficient"] == 38772884140592
    assert birth == cert["first_birth_error_upper_coefficient"] == 38242148
    tsb, tsource, tbirth = F(1, 8 * A * K), lower / (8 * E), F(1, 2 * birth)
    assert tsb == F(cert["T_full_NS"])
    assert tsource == F(cert["T_source"])
    assert tbirth == F(cert["T_first_birth"])
    tstar = F(cert["T_star"])
    assert tstar == min(tsb, tsource, tbirth) == tsource > 0
    assert b * tstar <= F(1, 2)
    assert E * tstar <= lower / 8
    assert birth * tstar <= F(1, 2)
    assert F(1, 8) / F(7, 8) == F(1, 7) < F(1, 4)
    # Analytic constants: integrate the full cross + h*h envelope.
    assert F(1, 4) + F(4, 5) * F(1, 2) == F(13, 20)
    assert 16 * 5 == 80
    for name in INPUTS:
        assert sha(BASE / name) == hashes[name]
    platform_label = platform.platform()
    cpu_arch = platform.machine()
    cpu_count = os.cpu_count()
    elapsed = time.monotonic() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert elapsed < 60 and rss < 256 * 1024 * 1024
    signal.alarm(0)
    report = {
        "status": "PASS_FIXED_CHART_EXACT_REVIEW_CHECK",
        "input_sha256": hashes,
        "review_script_sha256": sha(Path(__file__).resolve()),
        "method": "Five ordered tree shapes, all 24 distinct-leaf orders, symbolic alpha; both kernel basis inputs and both signed targets. No author-code imports.",
        "ordered_tree_terms_checked": terms,
        "whole_signed_fourier_recursion_rerun": False,
        "full_vector_matrices_match": True,
        "six_locked_samples_match": True,
        "negative_target_conjugacy_checked": True,
        "root_check_method": "Quadratic sign/vertex isolation and reduced Mobius endpoint bounds, not author interval-function imports.",
        "root_checks": root_checks,
        "A_l1_enclosure_upper_before_ceiling": Abound,
        "A_upper": A,
        "K_upper": K,
        "W0_A0_lower": lower,
        "source_and_birth_time_bounds_match": True,
        "T_star": tstar,
        "analytic_NS_tail_not_replaced_by_this_script": True,
        "no_candidate_or_singularity_acceptance": True,
        "resource": {
            "command": "/usr/bin/python3 research/reverse/four-carrier-source-test/review_verify.py > research/reverse/four-carrier-source-test/review-verification.json",
            "python": sys.version,
            "platform": platform_label,
            "cpu_arch": cpu_arch,
            "cpu_count": cpu_count,
            "processes": 1,
            "threads": 1,
            "process_count_scope": "One scientific Python worker; possible platform-metadata helper processes are not included.",
            "arithmetic": "exact Fraction, integer isqrt; no floating scientific evaluations",
            "tolerance": None,
            "random_seed": None,
            "wall_seconds": elapsed,
            "wall_scope": "Checker main entry through validation and platform metadata, before final JSON serialization/output.",
            "max_rss_bytes_macos": rss,
            "rss_scope": "RUSAGE_SELF measured before final JSON serialization; not a complete process-tree peak.",
            "complete_process_tree_resource_certificate": False,
        },
    }
    output = json.dumps(enc(report), ensure_ascii=False, indent=2)
    assert len(output.encode("utf-8")) < 1024 * 1024
    print(output)


if __name__ == "__main__":
    main()
