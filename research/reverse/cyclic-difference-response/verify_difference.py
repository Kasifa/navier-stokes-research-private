#!/usr/bin/env python3
"""UNEXECUTED reviewer: independent core plus stopped-certificate adapter.

Organization fixed before reading exact_difference.py or any new result:
six targets, two ordered contributions each, sparse (v,w) coefficients,
double-cross Leray, then ordinary Euclidean gcd and certificate identities.
No old A/B/C module is imported or called.  No root search, new refinement,
alternative lower bound, DI window, or scientific floating point is present.

Exposure: author of GS, old C verifier, current method and independent review;
has read DI and DR, so this is a non-author different organization, not a third
blind derivation.  During this core preparation the main author sent a schema
description but no results.  The pre-output core is preserved byte-for-byte as
verify_core_pre_output.py.txt (d65938f5...).  Only after that stop was the actual
main output 2ecedeb1... read to adapt its schema.  Main source was hash-bound,
not read or imported.  This final file therefore is not a blind verifier.

This source must not be run, imported, compiled or probed while under review.
Full reread, independent static review, parent source commit and a specific
one-run authorization remain separate gates.  CLI flags are technical guards,
not a substitute for that external authorization.
"""

import time
ENTRY_TIME = time.monotonic()

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import re
import resource
import signal
import sys


BINDINGS = {
    "CONTRACT.md": "a1b50ab4293c9d6132a874ed574b7843d0deae672a8928f73d1b9dcc7c09fed6",
    "METHOD_PREFLIGHT.md": "f2c7d90186f083601cab5bc5411d5c60826b963d6ed29efe9e4dfde5e149c316",
    "INDEPENDENT.md": "68957784dd943eca6968973aeb61a49e4453a3410b816c67e59d4f61384eedc4",
    "ANALYSIS.md": "fdf1a250da8a8f02e3343000f206e9f4f45fe159fb7b7352171d4e08b0fe3367",
    "old_B_json": "6fd933ebd18bdf8b129f7cabdbf1f02438de3fd95f9720b18e41887815f31bcb",
    "old_A_json": "9329464c09faa50558bc090b3af8c3ec6f074619e01a9fe2d5eb6d0f1c079ae6",
    "ANALYSIS_REVIEW.md": "02288305451808829feace3ac1f97480ee7cf1f918e011cbbe5a2c9f1cc7080c",
    "CONTRACT_REVIEW.md": "791c80270135a1a08e6aea43840cdde8dd5faa0ddc71c6c767d8f3efcc892a73",
    "INDEPENDENT_REVIEW.md": "f8db95b2549d02c9f28fc84fa8d78ef65c235c646743015194a452a18b4a8b04",
    "VERIFY_DESIGN.md": "cb991c6e2c82b729424323bae90a673adaecf7253091533d6b0a13e7ff89ccd3",
    "verify_core_pre_output.py.txt": "d65938f58fa364e3da172ed7d98af81c05ee5a80a4c3f5b251005dbe59e3decb",
    "exact_difference.py": "842679b23991ae2f3f5a5cd76903e9abf4ebd7a71a230829f99697612ad66030",
    "exact-difference-output.json": "2ecedeb13a1b7f521e286d520e28245964b01a6cde1d3c56232ddb9ae67eff7b",
}
MAIN_SOURCE_COMMIT = "668b18916d33b2832fc46b68e00184ce37c62738"
WORKTREE = Path("/Users/kasifa/Documents/Math/navier-stokes-reverse")
RELATIVE_DIRECTORY = Path("research/reverse/cyclic-difference-response")
OUTPUT_NAME = "review-difference-output.json"
MAX_NEW_BISECTIONS = 32
MAX_WALL_SECONDS = 60
MAX_SELF_RSS_BYTES = 256 * 1024 * 1024
MAX_OUTPUT_BYTES_EXCLUSIVE = 1024 * 1024
SCIENTIFIC_WORKERS = 1
SCIENTIFIC_THREADS = 1
_budget = None


class NotCertified(Exception):
    pass


class InconsistentCertificate(NotCertified):
    pass


def require(condition, reason):
    if not condition:
        raise InconsistentCertificate(reason)


class Budget:
    """Runner must supply its entry timestamp and actual SELF RSS reader.

    This is not a process-tree measurement or a claim of a hard OS RSS limit.
    The eventual runner must also check after the first complete serialization.
    """

    def __init__(self, entry_time, clock, self_rss_bytes):
        self.entry_time = entry_time
        self.clock = clock
        self.self_rss_bytes = self_rss_bytes

    def check(self):
        if self.clock() - self.entry_time > MAX_WALL_SECONDS:
            raise NotCertified("60-second deadline exceeded")
        if self.self_rss_bytes() > MAX_SELF_RSS_BYTES:
            raise NotCertified("SELF RSS target exceeded")


def tick():
    if _budget is None:
        raise NotCertified("no authorized runner budget installed")
    _budget.check()


def read_rational(text):
    """Canonical Fraction string only: no float, decimal, NaN or infinity."""
    require(type(text) is str, "rational must be a string")
    try:
        value = Fraction(text)
    except (ValueError, ZeroDivisionError):
        raise InconsistentCertificate("invalid rational string")
    require(str(value) == text, "noncanonical rational string")
    return value


# Private representation: univariate polynomial is an ascending Fraction tuple.
# Zero is (); the stopped main-output adapter must translate its own zero form.
def trim(values):
    out = list(values)
    require(all(type(x) is Fraction for x in out), "non-Fraction coefficient")
    while out and not out[-1]:
        out.pop()
    return tuple(out)


def pconstant(value):
    require(type(value) in (int, Fraction), "inexact polynomial constant")
    return trim((Fraction(value),))


def padd(a, b):
    tick()
    out = [Fraction(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def pscale(a, scalar):
    tick()
    require(type(scalar) in (int, Fraction), "inexact scalar")
    return trim(x * scalar for x in a)


def psub(a, b):
    return padd(a, pscale(b, -1))


def pmul(a, b):
    tick()
    if not a or not b:
        return ()
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        tick()
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def ppow(a, exponent):
    require(type(exponent) is int and 0 <= exponent <= 2, "power outside two-leaf scope")
    out = pconstant(1)
    for _ in range(exponent):
        out = pmul(out, a)
    return out


def pdivmod(a, b):
    """Ordinary exact Euclidean long division, no pseudo-remainder scaling."""
    tick()
    require(bool(b), "polynomial division by zero")
    remainder = a
    quotient = [Fraction(0)] * max(0, len(a) - len(b) + 1)
    while remainder and len(remainder) >= len(b):
        tick()
        old_degree = len(remainder) - 1
        shift = len(remainder) - len(b)
        factor = remainder[-1] / b[-1]
        quotient[shift] += factor
        subtractand = (Fraction(0),) * shift + pscale(b, factor)
        remainder = psub(remainder, subtractand)
        require(len(remainder) - 1 < old_degree, "division did not lower degree")
    return trim(quotient), remainder


def pgcd(a, b):
    tick()
    while b:
        _, remainder = pdivmod(a, b)
        a, b = b, remainder
    if not a:
        return ()
    return pscale(a, 1 / a[-1])


def pderivative(a):
    return trim(Fraction(i) * a[i] for i in range(1, len(a)))


def peval(a, x):
    tick()
    require(type(x) is Fraction, "inexact evaluation point")
    value = Fraction(0)
    for coefficient in reversed(a):
        value = value * x + coefficient
    return value


# Sparse bivariate polynomials: {(v_power, w_power): Fraction}, no alpha input.
def sclean(values):
    out = {}
    for powers, coefficient in values.items():
        require(len(powers) == 2 and all(type(e) is int and e >= 0 for e in powers),
                "invalid sparse powers")
        require(type(coefficient) is Fraction, "inexact sparse coefficient")
        if coefficient:
            out[powers] = coefficient
    return out


def sadd(a, b):
    tick()
    out = dict(a)
    for powers, coefficient in b.items():
        out[powers] = out.get(powers, Fraction(0)) + coefficient
    return sclean(out)


def sscale(a, scalar):
    require(type(scalar) in (int, Fraction), "inexact sparse scalar")
    return sclean({powers: coefficient * scalar for powers, coefficient in a.items()})


def ssub(a, b):
    return sadd(a, sscale(b, -1))


def smul(a, b):
    tick()
    out = {}
    for (av, aw), ac in a.items():
        for (bv, bw), bc in b.items():
            powers = (av + bv, aw + bw)
            require(sum(powers) <= 2, "higher-than-two-leaf monomial")
            out[powers] = out.get(powers, Fraction(0)) + ac * bc
    return sclean(out)


def rotate(vector, count=1):
    out = tuple(vector)
    for _ in range(count % 3):
        out = (out[2], out[0], out[1])
    return out


def frequency_scale(vector, scalar):
    require(type(scalar) is int, "noninteger frequency multiplier")
    return tuple(scalar * x for x in vector)


def vector_add(a, b):
    require(len(a) == len(b) == 3, "vector length")
    return tuple(sadd(x, y) for x, y in zip(a, b))


def vector_scale(a, scalar):
    require(len(a) == 3, "vector length")
    return tuple(sscale(x, scalar) for x in a)


def frequency_dot(k, vector):
    require(len(k) == len(vector) == 3, "dot product length")
    out = {}
    for ki, vi in zip(k, vector):
        out = sadd(out, sscale(vi, ki))
    return out


def cross_frequency_vector(k, vector):
    require(len(k) == len(vector) == 3, "cross product length")
    return (
        ssub(sscale(vector[2], k[1]), sscale(vector[1], k[2])),
        ssub(sscale(vector[0], k[2]), sscale(vector[2], k[0])),
        ssub(sscale(vector[1], k[0]), sscale(vector[0], k[1])),
    )


def ordered_gate_plus_i(left_k, right_k, left_v, right_v):
    """Return G with physical B=iG, using k x (k x right_v)/|k|^2.

    P_k b=-k x (k x b)/|k|^2; the additional -i changes the sign again.
    Inputs have the fixed real-even Fourier phase, including negative modes.
    """
    tick()
    target = tuple(x + y for x, y in zip(left_k, right_k))
    norm_squared = sum(x * x for x in target)
    require(norm_squared > 0, "unexpected zero output")
    require(not frequency_dot(left_k, left_v), "left leaf is not transverse")
    require(not frequency_dot(right_k, right_v), "right leaf is not transverse")
    derivative = frequency_dot(right_k, left_v)
    cross_twice = cross_frequency_vector(target, cross_frequency_vector(target, right_v))
    output = tuple(sscale(smul(derivative, component), Fraction(1, norm_squared))
                   for component in cross_twice)
    require(not frequency_dot(target, output), "full gate lost transversality")
    return output


def fixed_six_coefficients():
    """Rebuild twelve actual ordered gates; never use the known J factorization."""
    tick()
    vv = {(1, 0): Fraction(1)}
    ww = {(0, 1): Fraction(1)}
    high_vector = (sadd(sscale(vv, 3), sscale(ww, 5)),
                   sscale(vv, -2), sscale(ww, -2))
    high_frequency = (2, 3, 5)
    rows = {}
    gates = []
    for j in range(3):
        pk = rotate(high_frequency, j)
        sk = rotate(high_frequency, j + 1)
        av = rotate(high_vector, j)
        bv = rotate(high_vector, j + 1)
        for sign in (1, -1):
            left = frequency_scale(pk, sign)
            right = frequency_scale(sk, -sign)
            target = tuple(x + y for x, y in zip(left, right))
            require(target not in rows, "repeated target")
            forward = ordered_gate_plus_i(left, right, av, bv)
            backward = ordered_gate_plus_i(right, left, bv, av)
            total = vector_add(forward, backward)
            require(all(all(sum(power) == 2 for power in component) for component in total),
                    "nonquadratic total")
            rows[target] = total
            gates.append((target, left, right, forward))
            gates.append((target, right, left, backward))
    require(len(rows) == 6 and len(gates) == 12, "six-target/two-gate count")
    base = rows[(-3, 1, 2)]
    for j in range(3):
        positive = rotate((-3, 1, 2), j)
        negative = frequency_scale(positive, -1)
        require(rows[positive] == rotate(base, j), "cyclic vector mismatch")
        require(rows[negative] == vector_scale(rows[positive], -1), "conjugate phase mismatch")
    return rows, tuple(gates)


def substitute_original(sparse, original_r, original_s):
    """v=-s, w=r.  No row rescaling, quotient-field inversion or normalization."""
    tick()
    require(len(original_r) <= 4 and len(original_s) <= 4, "old row degree")
    vpoly = pscale(original_s, -1)
    result = ()
    for (vpower, wpower), coefficient in sparse.items():
        term = pmul(ppow(vpoly, vpower), ppow(original_r, wpower))
        result = padd(result, pscale(term, coefficient))
    require(len(result) <= 7, "new normalized coefficient exceeds degree six")
    return result


def verify_decoded_coefficients(rows, gates, original_r, original_s,
                                saved_formal, saved_normalized, saved_phases,
                                saved_ordered_gates):
    """Private parsed mappings; the future adapter must decode every raw row."""
    targets = set(rows)
    require(set(saved_formal) == targets and set(saved_normalized) == targets
            and set(saved_phases) == targets, "missing/extra six-vector record")
    normalized = {}
    for target in rows:
        require(saved_phases[target] == "+i", "wrong physical phase convention")
        require(saved_formal[target] == rows[target], "complete formal vector mismatch")
        independent = tuple(substitute_original(component, original_r, original_s)
                            for component in rows[target])
        require(saved_normalized[target] == independent, "original r/s substitution mismatch")
        normalized[target] = independent
    expected_gates = {(target, left, right): vector for target, left, right, vector in gates}
    require(len(expected_gates) == 12 and saved_ordered_gates == expected_gates,
            "missing/extra/incorrect complete ordered contribution")
    return normalized


def verify_reduction(original, modulus, quotient, remainder):
    require(len(remainder) < len(modulus), "remainder degree")
    require(padd(pmul(modulus, quotient), remainder) == original, "reduction identity")
    require(pdivmod(original, modulus) == (quotient, remainder), "independent division")


def verify_gcd_bezout(q, f, d, q_div_d, f_div_d, bezout_a, bezout_b):
    require(bool(q) and bool(d) and d[-1] == 1, "gcd zero or not monic")
    require(pmul(d, q_div_d) == q, "gcd does not divide Q")
    require(pmul(d, f_div_d) == f, "gcd does not divide f")
    require(padd(pmul(bezout_a, q), pmul(bezout_b, f)) == d, "Bezout identity")
    require(pgcd(q, f) == d, "ordinary Euclidean gcd mismatch")


def verify_division_step(left, right, quotient, remainder):
    """For every recorded ordinary Euclid step, including an explicit zero end."""
    require(pdivmod(left, right) == (quotient, remainder), "stored Euclid division step")


def verify_sturm(q, chain, derivative_multiplier, negative_remainder_multipliers):
    tick()
    require(bool(q) and bool(chain) and chain[0] == q, "Sturm initial polynomial")
    if len(q) == 1:
        require(len(chain) == 1 and not negative_remainder_multipliers,
                "constant Sturm chain")
        require(derivative_multiplier is None, "constant has derivative multiplier")
        return tuple(chain)
    require(2 <= len(chain) <= len(q), "Sturm length")
    require(type(derivative_multiplier) is Fraction and derivative_multiplier > 0,
            "nonpositive derivative multiplier")
    require(chain[1] == pscale(pderivative(q), derivative_multiplier), "Sturm derivative")
    require(len(negative_remainder_multipliers) == len(chain) - 2, "Sturm step count")
    for i, scalar in enumerate(negative_remainder_multipliers):
        require(type(scalar) is Fraction and scalar > 0, "nonpositive Sturm scaling")
        _, remainder = pdivmod(chain[i], chain[i + 1])
        require(bool(remainder), "Sturm continued after zero remainder")
        require(chain[i + 2] == pscale(remainder, -scalar), "negative remainder identity")
    require(len(chain[-1]) == 1, "nonconstant final Sturm term")
    require(not pdivmod(chain[-2], chain[-1])[1], "Sturm terminal remainder")
    return tuple(chain)


def verify_sturm_quotients(chain, saved_step_quotients, saved_terminal_quotient):
    if len(chain) == 1:
        require(not saved_step_quotients and saved_terminal_quotient is None,
                "extra constant-chain division evidence")
        return
    require(len(saved_step_quotients) == len(chain) - 2, "Sturm quotient count")
    for i, quotient in enumerate(saved_step_quotients):
        require(pdivmod(chain[i], chain[i + 1])[0] == quotient, "stored Sturm quotient")
    require(pdivmod(chain[-2], chain[-1]) == (saved_terminal_quotient, ()),
            "stored Sturm terminal quotient/remainder")


def endpoint_evidence(chain, point):
    values = tuple(peval(poly, point) for poly in chain)
    signs = tuple((value > 0) - (value < 0) for value in values)
    nonzero = tuple(sign for sign in signs if sign)
    variations = sum(left != right for left, right in zip(nonzero, nonzero[1:]))
    return values, signs, nonzero, variations


def root_count(chain, left, right):
    require(type(left) is Fraction and type(right) is Fraction and left < right,
            "invalid half-open interval")
    return endpoint_evidence(chain, left)[3] - endpoint_evidence(chain, right)[3]


def verify_root_zero(q, f, d, verified_d_chain, interval, claimed_zero):
    """Caller must first verify gcd and this chain; no label is accepted on faith."""
    require(type(claimed_zero) is bool, "nonboolean zero claim")
    require(verified_d_chain[0] == d, "zero test references wrong gcd chain")
    require(not pdivmod(q, d)[1] and not pdivmod(f, d)[1], "zero-test divisibility")
    count = root_count(verified_d_chain, *interval)
    require(count in (0, 1), "gcd has invalid count in the fixed root interval")
    require(claimed_zero == (count == 1), "wrong specified-root zero claim")
    return count


def verify_zero_prefix(flags, first_nonzero_coordinate):
    require(1 <= len(flags) <= 3 and all(type(x) is bool for x in flags), "zero prefix")
    if first_nonzero_coordinate is None:
        require(len(flags) == 3 and all(flags), "uncertified all-zero vector")
    else:
        require(type(first_nonzero_coordinate) is int and 1 <= first_nonzero_coordinate <= 3,
                "coordinate outside fixed order")
        require(len(flags) == first_nonzero_coordinate, "extra or missing coordinate test")
        require(all(flags[:-1]) and flags[-1] is False, "not the first nonzero coordinate")


def interval_multiply(a, b):
    require(a[0] <= a[1] and b[0] <= b[1], "reversed closed enclosure")
    products = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(products), max(products)


def horner_enclosure(poly, domain):
    tick()
    value = (Fraction(0), Fraction(0))
    trace = []
    for coefficient in reversed(poly):
        product = interval_multiply(value, domain)
        after = (product[0] + coefficient, product[1] + coefficient)
        trace.append((value, domain, product, coefficient, after))
        value = after
    return value, tuple(trace)


def avoids_zero(enclosure):
    return enclosure[0] > 0 or enclosure[1] < 0


@dataclass(frozen=True)
class RootFrame:
    """Private normalized interface, NOT a guess at the future raw JSON schema.

    interval retains half-open ownership even when its right root is represented
    as an exact point.  The adapter must preserve original node/field provenance.
    left_count/right_count describe the transition from the preceding frame.
    """
    interval: tuple
    point: object
    new_depth: int
    combined_depth: int
    enclosure: tuple
    horner_trace: tuple
    left_count: object = None
    right_count: object = None


def verify_saved_path(q, verified_q_chain, original_f, frames):
    """Only replay saved nodes.  This function never proposes a new bisection."""
    tick()
    require(verified_q_chain[0] == q, "path references a different Q")
    require(1 <= len(frames) <= MAX_NEW_BISECTIONS + 1, "path budget")
    initial = (Fraction(-75, 32), Fraction(-125, 64))
    require(frames[0].interval == initial, "path does not start at old root 0")
    for index, frame in enumerate(frames):
        tick()
        require(type(frame.new_depth) is int and frame.new_depth == index, "reset/skipped depth")
        require(frame.combined_depth == 7 + index, "old depth lost")
        a, b = frame.interval
        require(root_count(verified_q_chain, a, b) == 1, "path is not a single-root interval")
        if index == 0:
            require(frame.left_count is None and frame.right_count is None, "spurious first split")
        else:
            parent = frames[index - 1]
            require(parent.point is None, "refinement after an exact point")
            require(not avoids_zero(parent.enclosure), "refinement after the first valid lower bound")
            pa, pb = parent.interval
            mid = (pa + pb) / 2
            lc = root_count(verified_q_chain, pa, mid)
            rc = root_count(verified_q_chain, mid, pb)
            require((lc, rc) in ((1, 0), (0, 1)), "invalid bisection counts")
            require((frame.left_count, frame.right_count) == (lc, rc), "saved split counts")
            expected = (pa, mid) if lc == 1 else (mid, pb)
            require(frame.interval == expected, "wrong root branch or midpoint")
        right_is_root = peval(q, b) == 0
        if frame.point is not None:
            require(type(frame.point) is Fraction and frame.point == b and right_is_root,
                    "unjustified exact point")
            evaluation_domain = (b, b)
        else:
            require(not right_is_root, "unrecorded detected right-endpoint root")
            evaluation_domain = (a, b)
        enclosure, trace = horner_enclosure(original_f, evaluation_domain)
        require(frame.enclosure == enclosure, "saved Horner enclosure mismatch")
        require(frame.horner_trace == trace, "saved Horner operations mismatch")
    last = frames[-1]
    require(last.point is None or avoids_zero(last.enclosure),
            "claimed nonzero coordinate vanishes at an exact point")
    if not avoids_zero(last.enclosure):
        raise NotCertified("nonzero identity may hold; saved lower bound is unresolved")
    delta = min(abs(last.enclosure[0]), abs(last.enclosure[1]))
    require(delta > 0, "nonpositive coordinate bound")
    return delta, 2 * delta


def verify_original_dr8_window(abar, bbar, old_t, d, saved):
    """Compare parsed private records with the ORIGINAL main DR.8 window.

    No DI.15 formula and no smaller replacement window occur in this core.
    Adapter must link all four raw budget records to these exact tuples.
    """
    tick()
    require(all(type(x) is Fraction and x > 0 for x in (abar, bbar, old_t, d)),
            "window input is not positive rational")
    require(bbar == 28 * abar, "old bbar identity")
    q0 = 315 * abar * abar + 2 * abar * bbar * bbar
    c0 = Fraction(32, 7) * abar * abar * bbar ** 6
    candidates = (old_t, Fraction(1), d / (2 * q0), d / (8 * c0))
    tau = min(candidates)
    attain = tuple(i for i, value in enumerate(candidates) if value == tau)
    budgets = ((tau, old_t, old_t - tau), (tau, Fraction(1), 1 - tau),
               (q0 * tau, d / 2, d / 2 - q0 * tau),
               (c0 * tau, d / 8, d / 8 - c0 * tau))
    require(all(left <= right and slack >= 0 for left, right, slack in budgets),
            "DR.8 budget failure")
    expected = {"Abar": abar, "bbar": bbar, "T_star": old_t, "d": d,
                "Q0": q0, "C0": c0, "candidates": candidates,
                "tau": tau, "attaining_indices": attain, "budgets": budgets}
    require(saved == expected, "main original window/candidate/budget mismatch")
    return expected


# The adapter below was written AFTER saving the inert pre-output core.
# Exact key checks prevent silently skipping added mathematical evidence fields.
def exact_keys(record, names, context):
    require(type(record) is dict and set(record) == set(names), context + ": keys")


def sequence(value, length, context):
    require(type(value) is list and len(value) == length, context + ": length/type")
    return value


def integer(value, lower, upper, context):
    require(type(value) is int and lower <= value <= upper, context + ": integer")
    return value


def frequency(raw):
    return tuple(integer(x, -10, 10, "frequency") for x in sequence(raw, 3, "frequency"))


def rational_pair(raw):
    return tuple(read_rational(x) for x in sequence(raw, 2, "rational pair"))


def polynomial(raw):
    exact_keys(raw, ("coefficients_low_to_high", "degree"), "polynomial")
    degree = integer(raw["degree"], -1, 6, "polynomial degree")
    values = sequence(raw["coefficients_low_to_high"], max(1, degree + 1), "coefficients")
    out = trim(read_rational(x) for x in values)
    require(len(out) - 1 == degree, "noncanonical polynomial degree/zero")
    return out


def formal_three(raw):
    require(type(raw) is list and len(raw) <= 10, "sparse polynomial terms")
    out = {}
    previous = None
    for term in raw:
        exact_keys(term, ("alpha_v_w_exponents", "coefficient"), "sparse term")
        powers = tuple(integer(e, 0, 2, "exponent") for e in
                       sequence(term["alpha_v_w_exponents"], 3, "exponents"))
        require(sum(powers) <= 2 and (previous is None or previous < powers),
                "sparse ordering/duplicate/degree")
        value = read_rational(term["coefficient"])
        require(value != 0, "explicit zero sparse term")
        out[powers] = value
        previous = powers
    return out


def formal_two(raw):
    full = formal_three(raw)
    require(all(power[0] == 0 for power in full), "unexpected alpha in high-high gate")
    return {(power[1], power[2]): value for power, value in full.items()}


def formal_vector(raw):
    return tuple(formal_two(part) for part in sequence(raw, 3, "formal vector"))


def polynomial_vector(raw):
    return tuple(polynomial(part) for part in sequence(raw, 3, "polynomial vector"))


def verify_count_record(raw, chain, domain):
    exact_keys(raw, ("count", "interval", "ownership", "left_endpoint", "right_endpoint"),
               "root count")
    require(raw["ownership"] == "(a,b]" and rational_pair(raw["interval"]) == domain,
            "count interval ownership")
    for name, point in zip(("left_endpoint", "right_endpoint"), domain):
        endpoint = raw[name]
        exact_keys(endpoint, ("signs", "values", "variation_after_deleting_zeros", "x"),
                   "endpoint evidence")
        values, signs, _, variation = endpoint_evidence(chain, point)
        require(read_rational(endpoint["x"]) == point, "endpoint x")
        require(tuple(read_rational(x) for x in sequence(endpoint["values"], len(chain), "values"))
                == values, "all endpoint evaluations")
        require(tuple(integer(x, -1, 1, "sign") for x in
                      sequence(endpoint["signs"], len(chain), "signs")) == signs,
                "all endpoint signs")
        require(integer(endpoint["variation_after_deleting_zeros"], 0, len(chain), "variation")
                == variation, "delete-zero sign variations")
    expected = root_count(chain, *domain)
    require(integer(raw["count"], 0, len(chain), "root count") == expected, "count mismatch")
    return expected


def decode_and_verify_chain(raw, old_polys=None, old_chain=None):
    q = polynomial(raw["input"])
    constant = len(q) == 1
    common = ("S0_multiplier", "S1_positive_multiplier_of_derivative", "input", "polynomials", "steps")
    extra = (("constant_root_count",) if constant else
             ("terminal_quotient", "terminal_remainder"))
    if old_chain is not None:
        extra += ("old_chain_id", "old_polynomial_ids", "square_free_Q_verified_by_terminal_constant")
    exact_keys(raw, common + extra, "Sturm chain")
    require(read_rational(raw["S0_multiplier"]) == 1, "Sturm S0 scaling")
    require(type(raw["polynomials"]) is list, "Sturm polynomials")
    chain = tuple(polynomial(x) for x in raw["polynomials"])
    steps = sequence(raw["steps"], max(0, len(chain) - 2), "Sturm steps")
    multipliers, quotients = [], []
    for index, step in enumerate(steps):
        exact_keys(step, ("next", "positive_multiplier", "quotient"), "Sturm step")
        require(polynomial(step["next"]) == chain[index + 2], "Sturm stored next")
        multipliers.append(read_rational(step["positive_multiplier"]))
        quotients.append(polynomial(step["quotient"]))
    derivative = read_rational(raw["S1_positive_multiplier_of_derivative"])
    if constant:
        require(derivative == 1 and raw["constant_root_count"] == 0, "constant chain metadata")
        derivative = None
        terminal = None
    else:
        terminal = polynomial(raw["terminal_quotient"])
        require(polynomial(raw["terminal_remainder"]) == (), "nonzero terminal remainder")
    verified = verify_sturm(q, chain, derivative, tuple(multipliers))
    verify_sturm_quotients(verified, tuple(quotients), terminal)
    if old_chain is not None:
        require(raw["old_chain_id"] == old_chain["id"] == 0, "old chain identity")
        require(raw["old_polynomial_ids"] == old_chain["polynomials"], "old chain IDs")
        require(chain == tuple(old_polys[i] for i in old_chain["polynomials"]), "old chain bytes")
        require(old_polys[old_chain["input"]] == q, "old chain input")
        require(raw["S0_multiplier"] == old_chain["S0_multiplier"] and
                raw["S1_positive_multiplier_of_derivative"] == old_chain["S1_positive_multiplier_of_derivative"],
                "old chain scalings")
        old_steps = sequence(old_chain["negative_remainder_steps"], len(steps), "old steps")
        for new, old in zip(steps, old_steps):
            require(polynomial(new["next"]) == old_polys[old["next"]] and
                    polynomial(new["quotient"]) == old_polys[old["quotient"]] and
                    new["positive_multiplier"] == old["positive_multiplier"], "old step identity")
        require(terminal == old_polys[old_chain["terminal_quotient"]] and
                old_polys[old_chain["terminal_remainder"]] == (), "old terminal identity")
        require(raw["square_free_Q_verified_by_terminal_constant"] is True,
                "square-free report inconsistent with checked terminal")
    return verified


def verify_old_interface(raw, old_b, main_q_chain):
    exact_keys(raw, ("P", "Q_chain_endpoint_certificate", "Q_global_not_minimal_polynomial",
                    "field_identities_verified_not_old_Fourier_reexecution", "inherited_selected_window_values",
                    "interval", "old_IDs", "old_depth", "old_node", "old_root_index",
                    "r_original", "s_original", "v_minus_s", "w_r"), "old interface")
    # Reading this table is not recomputation of the old coefficients/root search.
    table = {}
    for index, entry in enumerate(old_b["polynomials"]):
        exact_keys(entry, ("id", "degree", "coefficients_low_to_high"), "old polynomial")
        require(type(entry["id"]) is int and entry["id"] == index, "old polynomial ID")
        table[index] = polynomial({key: value for key, value in entry.items() if key != "id"})
    expected_ids = {"P": 12, "Q": 13, "r": 6, "s": 7, "v": 62, "w": 6}
    require(raw["old_IDs"] == expected_ids, "old polynomial interface IDs")
    names = {"P": "P", "Q": "Q_global_not_minimal_polynomial", "r": "r_original",
             "s": "s_original", "v": "v_minus_s", "w": "w_r"}
    decoded = {name: polynomial(raw[field]) for name, field in names.items()}
    require(all(decoded[name] == table[ident] for name, ident in expected_ids.items()),
            "original P/r/s/Q/v/w bytes")
    p, q, r, s = (decoded[x] for x in ("P", "Q", "r", "s"))
    require(len(p) == 7 and q == pscale(p, 1 / p[-1]), "original P to monic global Q")
    require(decoded["v"] == pscale(s, -1) and decoded["w"] == r, "original normalization")
    require(raw["old_root_index"] == old_b["selected_root_index"] == 0 and
            raw["old_node"] == 13 and raw["old_depth"] == 7, "fixed selected root metadata")
    root = old_b["roots"][0]
    norm = root["normalization"]
    require(root["index"] == 0 and root["current_node"] == 13 and
            root["cumulative_bisection_depth"] == 7 and
            norm["original_r_s"] == [6, 7] and norm["original_row_index"] == 0 and
            norm["no_row_scaling_or_denominator_clearing"] is True and
            root["normalized_polynomials"]["v"] == 62 and root["normalized_polynomials"]["w"] == 6,
            "old root normalization identity")
    node = old_b["isolation_nodes"][13]
    initial = (Fraction(-75, 32), Fraction(-125, 64))
    require(rational_pair(raw["interval"]) == rational_pair(node["interval"]) == initial and
            node["id"] == 13 and node["depth"] == 7 and node["ownership"] == "(a,b]" and
            node["count"] == 1 and node["sturm_chain"] == 0, "old selected node")
    qchain = decode_and_verify_chain(main_q_chain, table, old_b["sturm_chains"][0])
    require(qchain[0] == q, "different selected Q")
    require(verify_count_record(raw["Q_chain_endpoint_certificate"], qchain, initial) == 1,
            "fixed interval is not isolating")
    require(node["V_a"] == endpoint_evidence(qchain, initial[0])[3] and
            node["V_b"] == endpoint_evidence(qchain, initial[1])[3] and
            node["right_endpoint_is_Q_root"] == (peval(q, initial[1]) == 0), "old node endpoint evidence")
    expected_point = initial[1] if peval(q, initial[1]) == 0 else None
    actual_point = root["exact_rational_point_if_detected"]
    require((None if actual_point is None else read_rational(actual_point)) == expected_point,
            "old exact-point identity")
    window = old_b["selected_window"]
    require(window["selected_root_index"] == 0 and window["final_root_node"] == 13 and
            rational_pair(window["alpha_closed_enclosure"]) == initial and
            window["cumulative_bisection_depth"] == 7, "old window field identity")
    inherited = raw["inherited_selected_window_values"]
    exact_keys(inherited, ("Aalpha", "Abar", "Dfirst", "Ebar", "T", "UV1", "Uv", "Uw", "bbar", "ell"),
               "inherited constants")
    for name, value in inherited.items():
        require(value == window[name] and read_rational(value) > 0, "changed old window constant " + name)
    require(raw["field_identities_verified_not_old_Fourier_reexecution"] is True, "old scope flag")
    return q, r, s, qchain, inherited


def verify_all_modes_and_gates(raw, independent_rows, independent_gates):
    exact_keys(raw, ("all_initial_phases", "all_six_rows", "candidate_count", "exact_common_heat_factor",
                    "formal_ring", "full_vector_factor_rotation_conjugacy_transversality_verified",
                    "initial_modes", "matched_ordered_count", "ordered_candidates", "ordered_contributions",
                    "reviewed_factor"), "new coefficient evidence")
    require(raw["formal_ring"] == "Q[alpha,v,w], sparse exponent triples" and
            raw["all_initial_phases"] == "real; negative frequency is conjugate, not independent",
            "formal ring or initial phases")
    one = {(0, 0, 0): Fraction(1)}
    alpha = {(1, 0, 0): Fraction(1)}
    low_v = ({}, one, alpha)
    high_v = ({(0, 1, 0): Fraction(3), (0, 0, 1): Fraction(5)},
              {(0, 1, 0): Fraction(-2)}, {(0, 0, 1): Fraction(-2)})
    expected = []
    for kind, k, amplitude in (("low", (1, 0, 0), low_v), ("high", (2, 3, 5), high_v)):
        for j in range(3):
            for sign in (1, -1):
                expected.append((kind, frequency_scale(rotate(k, j), sign), rotate(amplitude, j)))
    modes = sequence(raw["initial_modes"], 12, "initial modes")
    for actual, (kind, k, amplitude) in zip(modes, expected):
        exact_keys(actual, ("amplitude", "k", "kind"), "initial mode")
        require(actual["kind"] == kind and frequency(actual["k"]) == k and
                tuple(formal_three(x) for x in sequence(actual["amplitude"], 3, "amplitude")) == amplitude,
                "fixed initial datum including negative modes")
    require(type(raw["candidate_count"]) is int and raw["candidate_count"] == 144 and
            type(raw["matched_ordered_count"]) is int and raw["matched_ordered_count"] == 12,
            "ordered candidate counts")
    selected = set()
    candidates = sequence(raw["ordered_candidates"], 144, "all candidates")
    for index, candidate in enumerate(candidates):
        exact_keys(candidate, ("first_mode", "second_mode", "selected", "sum"), "candidate")
        left_index, right_index = divmod(index, 12)
        require(type(candidate["first_mode"]) is int and candidate["first_mode"] == left_index and
                type(candidate["second_mode"]) is int and candidate["second_mode"] == right_index,
                "candidate ordered coverage")
        target = tuple(a + b for a, b in zip(expected[left_index][1], expected[right_index][1]))
        is_selected = target in independent_rows
        require(frequency(candidate["sum"]) == target and type(candidate["selected"]) is bool and
                candidate["selected"] == is_selected, "candidate support selection")
        if is_selected:
            require(expected[left_index][0] == expected[right_index][0] == "high", "unexpected low gate")
            selected.add((left_index, right_index))
    require(len(selected) == 12, "support exhaustion")
    gate_lookup = {(target, left, right): output for target, left, right, output in independent_gates}
    saved_gates, consumed = {}, set()
    for gate in sequence(raw["ordered_contributions"], 12, "ordered contributions"):
        exact_keys(gate, ("G_contribution_with_phase_plus_i", "Leray_matrix", "first_mode",
                          "input_heat_rates", "ordered_dot", "output_heat_rate",
                          "projected_vector_with_phase_minus_i", "r", "raw_vector", "s", "second_mode", "target"),
                   "ordered contribution")
        indices = (integer(gate["first_mode"], 0, 11, "first index"),
                   integer(gate["second_mode"], 0, 11, "second index"))
        require(indices in selected and indices not in consumed, "duplicate/unselected contribution")
        consumed.add(indices)
        left, right = expected[indices[0]][1], expected[indices[1]][1]
        av = tuple({(p[1], p[2]): c for p, c in v.items()} for v in expected[indices[0]][2])
        bv = tuple({(p[1], p[2]): c for p, c in v.items()} for v in expected[indices[1]][2])
        target = tuple(a + b for a, b in zip(left, right))
        require(frequency(gate["r"]) == left and frequency(gate["s"]) == right and
                frequency(gate["target"]) == target, "gate frequency fields")
        independent = gate_lookup[(target, left, right)]
        derivative = frequency_dot(right, av)
        raw_vector = tuple(smul(derivative, part) for part in bv)
        projected = vector_scale(independent, -1)
        require(formal_two(gate["ordered_dot"]) == derivative and
                formal_vector(gate["raw_vector"]) == raw_vector and
                formal_vector(gate["projected_vector_with_phase_minus_i"]) == projected,
                "dot/raw/full Leray projection")
        ksq = sum(k * k for k in target)
        matrix = tuple(tuple(read_rational(x) for x in sequence(row, 3, "Leray row"))
                       for row in sequence(gate["Leray_matrix"], 3, "Leray matrix"))
        for i in range(3):
            via_matrix = {}
            for j in range(3):
                require(matrix[i][j] == Fraction(int(i == j)) - Fraction(target[i] * target[j], ksq),
                        "full stored Leray matrix")
                via_matrix = sadd(via_matrix, sscale(raw_vector[j], matrix[i][j]))
            require(via_matrix == projected[i], "matrix versus independent double cross")
        require(formal_vector(gate["G_contribution_with_phase_plus_i"]) == independent,
                "ordered physical phase")
        require(gate["input_heat_rates"] == [sum(k * k for k in left), sum(k * k for k in right)] and
                gate["output_heat_rate"] == ksq == 14, "ordered heat rates")
        saved_gates[(target, left, right)] = independent
    require(consumed == selected, "not all selected ordered pairs represented")
    heat = raw["exact_common_heat_factor"]
    require(heat == {"difference": 62, "formula": "(exp(-14t)-exp(-76t))/62",
                     "heat_error_bound_from_ANALYSIS": "0<=t-J(t)<=45t^2",
                     "input_rate": 76, "output_rate": 14}, "heat interface")
    # This is a formula check, not any evaluation of an exponential or time.
    require(76 - 14 == 62 and Fraction(76 + 14, 2) == 45, "heat formula arithmetic")
    factor = formal_two(raw["reviewed_factor"])
    require(factor == {(2, 0): Fraction(3), (1, 1): Fraction(11), (0, 2): Fraction(6)},
            "factor coefficients")
    base = independent_rows[(-3, 1, 2)]
    require(base == tuple(sscale(factor, Fraction(4 * x, 7)) for x in (-1, 19, -11)),
            "factorization of independently reconstructed complete vector")
    require(raw["full_vector_factor_rotation_conjugacy_transversality_verified"] is True,
            "coefficient status inconsistent with verified identities")
    return saved_gates


def verify_six_rows(raw_rows, rows, gates, saved_gates, r, s, q):
    formal, normalized, phases, reductions = {}, {}, {}, {}
    for raw in sequence(raw_rows, 6, "all six rows"):
        exact_keys(raw, ("formal_G", "normalized_G", "physical_phase", "reductions_mod_Q", "target"),
                   "target row")
        target = frequency(raw["target"])
        require(target not in formal, "duplicate complete vector")
        formal[target] = formal_vector(raw["formal_G"])
        normalized[target] = polynomial_vector(raw["normalized_G"])
        phases[target] = raw["physical_phase"]
        parts = []
        for component, red in zip(normalized[target], sequence(raw["reductions_mod_Q"], 3, "reductions")):
            exact_keys(red, ("Q_quotient", "identity_verified", "original_f", "remainder"), "reduction")
            require(polynomial(red["original_f"]) == component, "reduction references wrong component")
            quotient, remainder = polynomial(red["Q_quotient"]), polynomial(red["remainder"])
            verify_reduction(component, q, quotient, remainder)
            require(red["identity_verified"] is True, "reduction flag inconsistent with identity")
            parts.append((quotient, remainder))
        reductions[target] = tuple(parts)
    independent = verify_decoded_coefficients(rows, gates, r, s, formal, normalized, phases, saved_gates)
    return independent, reductions


def verify_gcd_record(raw, q, f):
    exact_keys(raw, ("Bezout_A", "Bezout_B", "D_monic", "Euclid_steps",
                    "final_monic_multiplier_not_Sturm_scaling", "input_quotients_by_D",
                    "inputs", "three_gcd_identities_verified"), "gcd record")
    require(tuple(polynomial(x) for x in sequence(raw["inputs"], 2, "gcd inputs")) == (q, f),
            "gcd input pair")
    d = polynomial(raw["D_monic"])
    divisors = tuple(polynomial(x) for x in sequence(raw["input_quotients_by_D"], 2, "gcd quotients"))
    verify_gcd_bezout(q, f, d, *divisors, polynomial(raw["Bezout_A"]), polynomial(raw["Bezout_B"]))
    # The stored Euclid sequence is checked as ordinary division, with its own
    # final monic factor.  Its factor may be negative; Sturm factors may not.
    require(type(raw["Euclid_steps"]) is list and len(raw["Euclid_steps"]) <= 7, "Euclid length")
    left, right = q, f
    for step in raw["Euclid_steps"]:
        exact_keys(step, ("left", "right", "quotient", "remainder"), "Euclid step")
        require(right and polynomial(step["left"]) == left and polynomial(step["right"]) == right,
                "Euclid continuity or premature terminal")
        quotient, remainder = polynomial(step["quotient"]), polynomial(step["remainder"])
        verify_division_step(left, right, quotient, remainder)
        left, right = right, remainder
    require(left and not right, "Euclid does not end at zero remainder")
    factor = read_rational(raw["final_monic_multiplier_not_Sturm_scaling"])
    require(factor == 1 / left[-1] and pscale(left, factor) == d, "final gcd monic normalization")
    require(raw["three_gcd_identities_verified"] is True, "gcd status inconsistent with identities")
    return d, len(raw["Euclid_steps"])


def verify_coordinate_tests(raw_tests, chains, q, base_vector, reductions, first):
    require(type(raw_tests) is list and 1 <= len(raw_tests) <= 3, "coordinate prefix size")
    interval = (Fraction(-75, 32), Fraction(-125, 64))
    flags, used_chains, euclid_total = [], {0}, 0
    for coordinate, raw in enumerate(raw_tests):
        exact_keys(raw, ("Q_quotient", "Sturm_chain", "coordinate_one_based", "count_certificate",
                        "gcd_certificate", "original_f", "remainder", "right_endpoint_root_exact_f_value",
                        "zero_at_fixed_root"), "coordinate zero test")
        require(integer(raw["coordinate_one_based"], 1, 3, "coordinate") == coordinate + 1,
                "coordinate testing order")
        f = base_vector[coordinate]
        quotient, remainder = reductions[coordinate]
        require(polynomial(raw["original_f"]) == f and polynomial(raw["Q_quotient"]) == quotient and
                polynomial(raw["remainder"]) == remainder, "zero-test original reduction identity")
        verify_reduction(f, q, quotient, remainder)
        d, nsteps = verify_gcd_record(raw["gcd_certificate"], q, remainder)
        euclid_total += nsteps
        chain_index = integer(raw["Sturm_chain"], 0, len(chains) - 1, "gcd chain index")
        used_chains.add(chain_index)
        chain = chains[chain_index]
        count = verify_count_record(raw["count_certificate"], chain, interval)
        require(count == verify_root_zero(q, remainder, d, chain, interval, raw["zero_at_fixed_root"]),
                "coordinate count identity")
        exact_value = raw["right_endpoint_root_exact_f_value"]
        if peval(q, interval[1]) == 0:
            require(exact_value is not None and read_rational(exact_value) == peval(f, interval[1]),
                    "exact endpoint original f evaluation")
            require(raw["zero_at_fixed_root"] == (read_rational(exact_value) == 0), "point/gcd disagreement")
        else:
            require(exact_value is None, "spurious exact-point coordinate value")
        flags.append(raw["zero_at_fixed_root"])
    verify_zero_prefix(flags, first)
    require(used_chains == set(range(len(chains))), "unused/unexplained saved Sturm chain")
    return tuple(flags), euclid_total


def verify_horner_raw(raw, f, q, depth):
    exact_keys(raw, ("Horner_steps", "closed_input", "closed_output", "combined_depth",
                    "exact_right_endpoint_root", "new_bisection_count", "old_depth", "ownership",
                    "root_interval", "strictly_avoids_zero"), "closed enclosure record")
    interval = rational_pair(raw["root_interval"])
    require(interval[0] < interval[1] and raw["ownership"] == "(a,b]", "Horner root ownership")
    require(raw["old_depth"] == 7 and raw["new_bisection_count"] == depth and
            raw["combined_depth"] == 7 + depth, "Horner depth")
    exact_point = peval(q, interval[1]) == 0
    require(type(raw["exact_right_endpoint_root"]) is bool and raw["exact_right_endpoint_root"] == exact_point,
            "Horner exact endpoint flag")
    domain = (interval[1], interval[1]) if exact_point else interval
    require(rational_pair(raw["closed_input"]) == domain, "Horner closed input")
    enclosure, trace = horner_enclosure(f, domain)
    for step, operation in zip(sequence(raw["Horner_steps"], len(trace), "all Horner steps"), trace):
        exact_keys(step, ("coefficient", "four_products", "result"), "Horner operation")
        before, x, _, coefficient, after = operation
        products = (before[0] * x[0], before[0] * x[1], before[1] * x[0], before[1] * x[1])
        require(read_rational(step["coefficient"]) == coefficient and
                tuple(read_rational(z) for z in sequence(step["four_products"], 4, "four interval products"))
                == products and rational_pair(step["result"]) == after, "saved Horner arithmetic")
    require(rational_pair(raw["closed_output"]) == enclosure and
            type(raw["strictly_avoids_zero"]) is bool and raw["strictly_avoids_zero"] == avoids_zero(enclosure),
            "Horner final enclosure/zero exclusion")
    return interval, (interval[1] if exact_point else None), enclosure, trace


def verify_path_and_bound(main, q, qchain, f, coordinate):
    path = main["new_bisection_path"]
    require(type(path) is list and len(path) <= MAX_NEW_BISECTIONS, "new saved bisection count")
    count = len(path)
    require(integer(main["new_bisections_started"], 0, 32, "started bisections") == count and
            integer(main["new_bisections_completed"], 0, 32, "completed bisections") == count,
            "bisection counter mismatch")
    traces = sequence(main["closed_enclosure_trace"], count + 1, "all saved enclosures")
    frames = []
    for depth, raw in enumerate(traces):
        tick()
        interval, point, enclosure, trace = verify_horner_raw(raw, f, q, depth)
        lc = rc = None
        if depth:
            transition = path[depth - 1]
            exact_keys(transition, ("combined_depth", "kept_interval", "kept_side", "left_count_certificate",
                                   "midpoint", "midpoint_is_Q_root", "new_bisection_count", "parent_interval",
                                   "right_count_certificate"), "saved bisection")
            parent = frames[-1].interval
            require(rational_pair(transition["parent_interval"]) == parent, "saved path parent")
            midpoint = (parent[0] + parent[1]) / 2
            require(read_rational(transition["midpoint"]) == midpoint and
                    type(transition["midpoint_is_Q_root"]) is bool and
                    transition["midpoint_is_Q_root"] == (peval(q, midpoint) == 0), "saved midpoint identity")
            lc = verify_count_record(transition["left_count_certificate"], qchain, (parent[0], midpoint))
            rc = verify_count_record(transition["right_count_certificate"], qchain, (midpoint, parent[1]))
            require((lc, rc) in ((1, 0), (0, 1)), "same-root split counts")
            require(transition["kept_side"] == ("left" if lc == 1 else "right") and
                    rational_pair(transition["kept_interval"]) == interval and
                    transition["new_bisection_count"] == depth and transition["combined_depth"] == 7 + depth,
                    "selected child/depth record")
        frames.append(RootFrame(interval, point, depth, 7 + depth, enclosure, trace, lc, rc))
    delta, d = verify_saved_path(q, qchain, f, tuple(frames))
    lower = main["new_coordinate_lower_bound"]
    exact_keys(lower, ("closed_enclosure", "combined_depth", "coordinate_one_based", "d_two_mode_pair",
                      "delta", "final_interval", "new_bisection_count", "old_depth", "original_polynomial"),
               "coordinate lower bound")
    final = frames[-1]
    require(lower["coordinate_one_based"] == coordinate and polynomial(lower["original_polynomial"]) == f and
            rational_pair(lower["closed_enclosure"]) == final.enclosure and
            rational_pair(lower["final_interval"]) == final.interval and
            lower["old_depth"] == 7 and lower["new_bisection_count"] == count and
            lower["combined_depth"] == 7 + count and read_rational(lower["delta"]) == delta and
            read_rational(lower["d_two_mode_pair"]) == d, "original lower bound identity")
    return delta, d, tuple(frames)


def verify_raw_window(raw, inherited, d):
    exact_keys(raw, ("Abar_unchanged", "C0", "H_may_be_zero_no_division_by_H", "Q0", "T_star_unchanged",
                    "bbar_unchanged", "conditional_conclusion", "d", "exact_budgets",
                    "four_candidates_in_contract_order", "interface", "minimum_attaining_indices_zero_based",
                    "norm", "original_T_star_not_replaced", "positive_constants_and_candidates_verified",
                    "same_d_for_each_signed_pair_by_verified_rotation_conjugacy", "tau"), "raw DR.8 window")
    require(raw["Abar_unchanged"] == inherited["Abar"] and raw["bbar_unchanged"] == inherited["bbar"] and
            raw["T_star_unchanged"] == inherited["T"], "old constants changed before DR.8")
    names = ("tau<=T_star", "tau<=1", "Q0*tau<=d/2", "C0*tau<=d/8")
    budgets = []
    for name, record in zip(names, sequence(raw["exact_budgets"], 4, "all window budgets")):
        exact_keys(record, ("left", "name", "right", "slack"), "budget")
        require(record["name"] == name, "window budget order/name")
        budgets.append(tuple(read_rational(record[key]) for key in ("left", "right", "slack")))
    require(type(raw["minimum_attaining_indices_zero_based"]) is list, "attaining indices")
    saved = {"Abar": read_rational(raw["Abar_unchanged"]), "bbar": read_rational(raw["bbar_unchanged"]),
             "T_star": read_rational(raw["T_star_unchanged"]), "d": read_rational(raw["d"]),
             "Q0": read_rational(raw["Q0"]), "C0": read_rational(raw["C0"]),
             "candidates": tuple(read_rational(x) for x in sequence(raw["four_candidates_in_contract_order"], 4, "times")),
             "tau": read_rational(raw["tau"]),
             "attaining_indices": tuple(integer(x, 0, 3, "attainer") for x in raw["minimum_attaining_indices_zero_based"]),
             "budgets": tuple(budgets)}
    verified = verify_original_dr8_window(read_rational(inherited["Abar"]), read_rational(inherited["bbar"]),
                                          read_rational(inherited["T"]), d, saved)
    require(raw["interface"] == "MP.10 / DR.8, not DI.15" and
            raw["norm"] == "A0=sum of Hermitian Euclidean Fourier-vector norms" and
            raw["conditional_conclusion"] ==
            "For each pair and total E_-, 0<t<=tau: P_E u nonzero and ||H||<=||P_E u||/4.", "window scope")
    for flag in ("H_may_be_zero_no_division_by_H", "original_T_star_not_replaced",
                 "positive_constants_and_candidates_verified", "same_d_for_each_signed_pair_by_verified_rotation_conjugacy"):
        require(raw[flag] is True, "window flag inconsistent with checked identities")
    return verified


def encode_poly(poly):
    return {"coefficients_low_to_high": [str(x) for x in poly] if poly else ["0"], "degree": len(poly) - 1}


def encode_sparse(poly):
    return [{"v_w_exponents": list(p), "coefficient": str(poly[p])} for p in sorted(poly)]


def stopped_main_adapter(main, old_b):
    """Verify the saved certificate; do not construct any fresh root interval."""
    tick()
    require(main["schema"] == "cyclic-difference-response-main-v1", "main schema")
    raw_chains = main["Sturm_chains"]
    require(type(raw_chains) is list and 1 <= len(raw_chains) <= 4, "local chain count")
    q, r, s, qchain, inherited = verify_old_interface(main["old_interface"], old_b, raw_chains[0])
    chains = (qchain,) + tuple(decode_and_verify_chain(raw) for raw in raw_chains[1:])
    rows, gates = fixed_six_coefficients()
    saved_gates = verify_all_modes_and_gates(main["new_coefficients"], rows, gates)
    normalized, reductions = verify_six_rows(main["new_coefficients"]["all_six_rows"], rows, gates,
                                             saved_gates, r, s, q)
    first = main["first_nonzero_coordinate_one_based"]
    base = (-3, 1, 2)
    flags, euclid_count = verify_coordinate_tests(main["coordinate_zero_tests"], chains, q,
                                                 normalized[base], reductions[base], first)
    if first is None:
        raise NotCertified("verified all-zero coordinate prefix; no new lower bound or window")
    integer(first, 1, 3, "first nonzero coordinate")
    delta, d, frames = verify_path_and_bound(main, q, qchain, normalized[base][first - 1], first)
    window = verify_raw_window(main["new_window"], inherited, d)
    require(main["certificate_status"] == "DIFFERENCE-WINDOW-CERTIFIED" and
            main["coefficient_nonzero_certified"] is True, "main success labels disagree with evidence")
    # Retain reconstructed vectors plus complete original proof records.  The
    # latter are checked inputs, not falsely described as a new blind derivation.
    independent_evidence = []
    for target in rows:
        independent_evidence.append({"target": list(target), "physical_phase": "+i",
                                     "formal_G_v_w": [encode_sparse(x) for x in rows[target]],
                                     "original_normalized_G": [encode_poly(x) for x in normalized[target]],
                                     "Q_quotients": [encode_poly(x[0]) for x in reductions[target]],
                                     "Q_remainders": [encode_poly(x[1]) for x in reductions[target]]})
    gate_evidence = [{"target": list(target), "first": list(left), "second": list(right),
                      "G_with_plus_i": [encode_sparse(x) for x in vector]} for target, left, right, vector in gates]
    return {"independent_six_vectors": independent_evidence, "independent_twelve_gates": gate_evidence,
            "coverage": {"initial_modes": 12, "ordered_candidates": 144, "ordered_contributions": 12,
                         "full_vector_components": 18, "all_component_reductions": 18,
                         "Sturm_chains": len(chains), "coordinate_zero_tests": len(flags),
                         "gcd_certificates": len(flags), "ordinary_Euclid_steps": euclid_count,
                         "saved_bisections_replayed": len(frames) - 1, "saved_closed_Horner_records": len(frames),
                         "saved_Horner_steps": sum(len(frame.horner_trace) for frame in frames),
                         "new_reviewer_bisections": 0, "old_A_B_C_executions": 0,
                         "original_window_candidates": 4, "original_window_budgets": 4},
            "first_nonzero_coordinate_one_based": first, "zero_prefix": list(flags),
            "delta_original_coordinate": str(delta), "d_original_two_mode_pair": str(d),
            "tau_original_DR8": str(window["tau"]),
            "verified_original_records": {key: main[key] for key in
                ("old_interface", "Sturm_chains", "coordinate_zero_tests", "new_bisection_path",
                 "closed_enclosure_trace", "new_coordinate_lower_bound", "new_window")}}


def input_paths(directory):
    paths = {name: directory / name for name in BINDINGS}
    paths["old_A_json"] = directory.parent / "cyclic-six-carrier/exact-coefficients-output.json"
    paths["old_B_json"] = directory.parent / "cyclic-six-carrier/exact-roots-output.json"
    return paths


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def reject_duplicate_keys(pairs):
    record = {}
    for key, value in pairs:
        require(key not in record, "duplicate JSON object key")
        record[key] = value
    return record


def reject_json_constant(value):
    raise InconsistentCertificate("nonfinite JSON constant " + value)


def decode_json(data):
    return json.loads(data.decode("utf-8"), object_pairs_hook=reject_duplicate_keys,
                      parse_constant=reject_json_constant)


def read_bound_inputs(directory):
    retained, ledger = {}, {}
    for name, path in input_paths(directory).items():
        tick()
        data = path.read_bytes()
        actual = sha256_bytes(data)
        require(actual == BINDINGS[name], "input SHA mismatch: " + name)
        ledger[name] = {"path": str(path), "sha256": actual, "bytes": len(data)}
        if name in ("old_B_json", "exact-difference-output.json"):
            retained[name] = decode_json(data)
    require(ledger["exact-difference-output.json"]["bytes"] == 269258, "stopped main byte length")
    return retained, ledger


def recheck_sources(directory, ledger, reviewer_source, reviewer_sha):
    for name, path in input_paths(directory).items():
        tick()
        data = path.read_bytes()
        require(sha256_bytes(data) == ledger[name]["sha256"] and len(data) == ledger[name]["bytes"],
                "input changed during verification: " + name)
    require(sha256_bytes(reviewer_source.read_bytes()) == reviewer_sha, "reviewer source changed during run")
    tick()


def verify_main_metadata(main, ledger, directory):
    exact_keys(main, ("Sturm_chains", "certificate_status", "closed_enclosure_trace",
                     "coefficient_nonzero_certified", "coordinate_zero_tests", "environment", "execution_status",
                     "first_nonzero_coordinate_one_based", "limits", "mathematical_acceptance",
                     "new_bisection_path", "new_bisections_completed", "new_bisections_started", "new_coefficients",
                     "new_coordinate_lower_bound", "new_window", "old_interface", "provenance", "resource_scope",
                     "resources_after_first_full_serialization_attempt", "resources_before_first_full_serialization",
                     "resources_before_scientific_entry", "root_coordinate_scope", "schema",
                     "scientific_execution_count_in_this_invocation", "scientific_stage_completed", "scope"),
               "main complete top-level record")
    require(main["execution_status"] == "completed" and
            type(main["scientific_execution_count_in_this_invocation"]) is int and
            main["scientific_execution_count_in_this_invocation"] == 1 and main["scientific_stage_completed"] is True,
            "main not a completed single invocation")
    require(main["limits"] == {"RSS_SELF_target_bytes": MAX_SELF_RSS_BYTES,
                                "output_bytes_strictly_below": MAX_OUTPUT_BYTES_EXCLUSIVE,
                                "shared_new_bisections": MAX_NEW_BISECTIONS,
                                "wall_seconds_from_entry": MAX_WALL_SECONDS}, "main locked limits")
    require(main["mathematical_acceptance"] == "pending_non_author_certificate_and_scope_review" and
            main["root_coordinate_scope"] ==
            "Only coordinates through first nonzero classified; all six full symbolic vectors retained." and
            main["scope"] ==
            "Same fixed datum, six differences, first gate and MP.10 arithmetic only; no later restart or regeneration theorem.",
            "main claim scope")
    provenance = main["provenance"]
    exact_keys(provenance, ("argv", "input_bindings", "source_commit_not_checked_by_git",
                           "source_commit_parent_supplied", "source_path", "source_sha256"), "main provenance")
    require(provenance["source_commit_parent_supplied"] == MAIN_SOURCE_COMMIT and
            provenance["source_commit_not_checked_by_git"] is True and
            provenance["source_path"] == str(directory / "exact_difference.py") and
            provenance["source_sha256"] == BINDINGS["exact_difference.py"], "main source identity")
    require(provenance["argv"] == [str(RELATIVE_DIRECTORY / "exact_difference.py"), "--source-commit",
                                    MAIN_SOURCE_COMMIT, "--contract-sha", BINDINGS["CONTRACT.md"]], "main argv")
    aliases = {name: name for name in ("ANALYSIS.md", "ANALYSIS_REVIEW.md", "CONTRACT.md",
                                      "CONTRACT_REVIEW.md", "INDEPENDENT.md", "INDEPENDENT_REVIEW.md",
                                      "METHOD_PREFLIGHT.md")}
    aliases.update({"exact-coefficients-output.json": "old_A_json", "exact-roots-output.json": "old_B_json"})
    exact_keys(provenance["input_bindings"], aliases, "main input ledger")
    for name, alias in aliases.items():
        record = provenance["input_bindings"][name]
        exact_keys(record, ("path", "sha256"), "main binding")
        require(record == {key: ledger[alias][key] for key in ("path", "sha256")}, "main input binding " + name)
    env = main["environment"]
    exact_keys(env, ("external_processes_started", "os_uname", "python_executable", "python_version",
                     "scientific_threads", "scientific_workers", "third_party_libraries", "visible_logical_CPUs"),
               "main environment")
    require(env["external_processes_started"] == 0 and env["scientific_threads"] == 1 and
            env["scientific_workers"] == 1 and env["third_party_libraries"] == [], "main reported worker scope")
    require(type(env["python_executable"]) is str and type(env["python_version"]) is str and
            type(env["visible_logical_CPUs"]) is int and env["visible_logical_CPUs"] >= 1, "main environment types")
    exact_keys(env["os_uname"], ("machine", "nodename", "release", "sysname", "version"), "main uname")
    require(all(type(x) is str for x in env["os_uname"].values()), "main uname values")
    require(main["resource_scope"] ==
            "SELF only. Deadline starts just after importing time at entry and includes input reading, science, rechecks and first full serialization. Final resource fields, final serialization and disk write are excluded. RSS is sampled with a high-water SELF value, not a full-lifecycle hard memory guarantee.",
            "main resource boundary changed")
    previous = None
    fields = ("RSS_SELF_bytes", "system_CPU_seconds", "user_CPU_seconds", "wall_seconds_since_entry")
    for key in ("resources_before_scientific_entry", "resources_before_first_full_serialization",
                "resources_after_first_full_serialization_attempt"):
        snapshot = main[key]
        exact_keys(snapshot, fields, "main resource snapshot")
        require(type(snapshot["RSS_SELF_bytes"]) is int and 0 < snapshot["RSS_SELF_bytes"] <= MAX_SELF_RSS_BYTES,
                "main recorded SELF RSS exceeds target")
        for name in fields[1:]:
            value = snapshot[name]
            require(type(value) in (int, float) and math.isfinite(value) and value >= 0,
                    "invalid metadata resource number")
        require(snapshot["wall_seconds_since_entry"] <= MAX_WALL_SECONDS, "main recorded wall deadline")
        if previous is not None:
            require(all(snapshot[name] >= previous[name] for name in fields), "main nonmonotone resource snapshots")
        previous = snapshot
    # These checks validate recorded metadata and its boundary, not a fresh
    # process-tree audit or a retrospective measurement of the main invocation.


def self_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def resource_snapshot():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    return {"RSS_SELF_bytes": self_rss_bytes(), "user_CPU_seconds": usage.ru_utime,
            "system_CPU_seconds": usage.ru_stime, "wall_seconds_since_entry": time.monotonic() - ENTRY_TIME}


def alarm_expired(_signum, _frame):
    raise NotCertified("60-second invocation deadline signal")


def serialize_record(record):
    return (json.dumps(record, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n").encode("utf-8")


def mark_failure(record, error):
    record["certificate_status"] = "NOT-CERTIFIED"
    record["execution_status"] = "failed"
    record["failure"] = {"type": type(error).__name__, "message": str(error)[:2000]}
    record["mathematical_acceptance"] = "not granted"


def authorized_once_runner():
    """Future single invocation only; technical guard does not grant permission."""
    global _budget
    parser = argparse.ArgumentParser(description="Stopped difference certificate reviewer; no root search.")
    parser.add_argument("--run-once-after-parent-authorization", action="store_true")
    parser.add_argument("--reviewer-source-commit", required=True)
    args = parser.parse_args()
    if not args.run_once_after_parent_authorization or not re.fullmatch(r"[0-9a-f]{40}", args.reviewer_source_commit):
        parser.error("specific parent authorization and its 40-character pre-run source commit are required")
    directory = WORKTREE / RELATIVE_DIRECTORY
    source = Path(__file__).resolve()
    if source != directory / "verify_difference.py" or Path.cwd().resolve() != WORKTREE:
        parser.error("run only this fixed source in the authorized reverse worktree")
    output_path = directory / OUTPUT_NAME
    try:
        output_handle = output_path.open("xb")
    except FileExistsError:
        print(json.dumps({"certificate_status": "NOT-CERTIFIED", "reason": "exclusive output already exists",
                          "scientific_execution_count_in_this_invocation": 0, "scientific_stage_completed": False}),
              file=sys.stderr)
        return 2
    record = {"schema": "cyclic-difference-response-review-v1", "certificate_status": "NOT-CERTIFIED",
              "execution_status": "started", "scientific_execution_count_in_this_invocation": 0,
              "scientific_stage_completed": False, "mathematical_acceptance": "not granted",
              "scope": "Non-author different-organization finite certificate verification, not a third blind proof; no NS simulation, new root search, restart, or regeneration claim.",
              "provenance": {"argv": sys.argv, "reviewer_source_commit_parent_supplied": args.reviewer_source_commit,
                             "source_commit_not_checked_by_git": True, "reviewer_source_path": str(source)},
              "limits": {"wall_seconds_from_entry": MAX_WALL_SECONDS, "RSS_SELF_target_bytes": MAX_SELF_RSS_BYTES,
                         "output_bytes_strictly_below": MAX_OUTPUT_BYTES_EXCLUSIVE,
                         "scientific_workers": SCIENTIFIC_WORKERS, "scientific_threads": SCIENTIFIC_THREADS,
                         "main_saved_new_bisections_at_most": MAX_NEW_BISECTIONS, "reviewer_new_bisections": 0},
              "resource_scope": "SELF only; invocation deadline starts immediately after importing time. Input reading, verification, source rechecks and first full serialization are included. Added final resource fields, final serialization and disk write are excluded. High-water SELF RSS samples are not a hard whole-lifecycle or whole-process-tree guarantee."}
    _budget = Budget(ENTRY_TIME, time.monotonic, self_rss_bytes)
    alarm_installed = False
    first_serialized = None
    try:
        tick()
        signal.signal(signal.SIGALRM, alarm_expired)
        remaining = MAX_WALL_SECONDS - (time.monotonic() - ENTRY_TIME)
        if remaining <= 0:
            raise NotCertified("deadline expired before scientific entry")
        signal.setitimer(signal.ITIMER_REAL, remaining)
        alarm_installed = True
        source_sha = sha256_bytes(source.read_bytes())
        record["provenance"]["reviewer_source_sha256"] = source_sha
        record["environment"] = {"python_executable": sys.executable, "python_version": sys.version,
                                 "os_uname": dict(zip(("sysname", "nodename", "release", "version", "machine"), os.uname())),
                                 "visible_logical_CPUs": os.cpu_count(), "external_processes_started": 0,
                                 "scientific_workers": 1, "scientific_threads": 1, "third_party_libraries": []}
        inputs, ledger = read_bound_inputs(directory)
        record["provenance"]["input_bindings"] = ledger
        main = inputs["exact-difference-output.json"]
        verify_main_metadata(main, ledger, directory)
        record["resources_before_scientific_entry"] = resource_snapshot()
        tick()
        record["scientific_execution_count_in_this_invocation"] = 1
        result = stopped_main_adapter(main, inputs["old_B_json"])
        record["scientific_stage_completed"] = True
        record["result"] = result
        recheck_sources(directory, ledger, source, source_sha)
        record["source_bindings_rechecked_after_science"] = True
        record["verified_main_metadata"] = {key: main[key] for key in
            ("environment", "provenance", "resource_scope", "resources_before_scientific_entry",
             "resources_before_first_full_serialization", "resources_after_first_full_serialization_attempt")}
        record["certificate_status"] = "DIFFERENCE-CERTIFICATE-VERIFIED"
        record["execution_status"] = "completed"
        record["mathematical_acceptance"] = "pending parent final scope review; finite arithmetic only"
        record["resources_before_first_full_serialization"] = resource_snapshot()
        tick()
        first_serialized = serialize_record(record)
        record["resources_after_first_full_serialization_attempt"] = resource_snapshot()
        tick()
        require(len(first_serialized) < MAX_OUTPUT_BYTES_EXCLUSIVE, "first serialized output exceeds bound")
    except BaseException as error:
        mark_failure(record, error)
        # A bounded failure is retained.  Science is never called again, and a
        # completed arithmetic stage is not confused with final certification.
        if "resources_after_first_full_serialization_attempt" not in record:
            record["resources_at_failure"] = resource_snapshot()
    finally:
        if alarm_installed:
            signal.setitimer(signal.ITIMER_REAL, 0)
    try:
        if first_serialized is None:
            record["first_full_certificate_record_serialized"] = False
        else:
            record["first_full_certificate_record_serialized"] = True
            record["first_full_serialized_bytes"] = len(first_serialized)
        final_bytes = serialize_record(record)
        if len(final_bytes) >= MAX_OUTPUT_BYTES_EXCLUSIVE:
            # Retain true 0/1 and completion fields; never pretend an oversized
            # success is certified or overwrite the unique output on a rerun.
            mark_failure(record, NotCertified("final serialization exceeds output bound"))
            record.pop("result", None)
            record.pop("verified_main_metadata", None)
            record["oversized_full_record_omitted"] = True
            final_bytes = serialize_record(record)
        if len(final_bytes) >= MAX_OUTPUT_BYTES_EXCLUSIVE:
            raise NotCertified("bounded failure record still exceeds output cap")
        output_handle.write(final_bytes)
        output_handle.flush()
    except BaseException as error:
        print(json.dumps({"certificate_status": "NOT-CERTIFIED", "execution_status": "write_failed",
                          "scientific_execution_count_in_this_invocation": record["scientific_execution_count_in_this_invocation"],
                          "scientific_stage_completed": record["scientific_stage_completed"],
                          "error": str(error)[:1000]}), file=sys.stderr)
        return 2
    finally:
        output_handle.close()
    summary = {"certificate_status": record["certificate_status"], "execution_status": record["execution_status"],
               "scientific_execution_count_in_this_invocation": record["scientific_execution_count_in_this_invocation"],
               "scientific_stage_completed": record["scientific_stage_completed"], "output": str(output_path),
               "output_bytes": len(final_bytes), "output_sha256": sha256_bytes(final_bytes),
               "resources_at_recorded_boundary": record.get("resources_after_first_full_serialization_attempt",
                                                             record.get("resources_at_failure"))}
    if "failure" in record:
        summary["failure"] = record["failure"]
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0 if record["certificate_status"] == "DIFFERENCE-CERTIFICATE-VERIFIED" else 1


if __name__ == "__main__":
    sys.exit(authorized_once_runner())
