#!/usr/bin/env python3
"""One fixed-chart exact experiment: labelled subsets, not full convolution.

Read CONTRACT.md and INDEPENDENT_ALGEBRA.md for scope and the short-leaf
uniqueness proof.  All scientific arithmetic is Fraction / exact integers.
The factors (-i)^(number_of_leaves-1) are stripped throughout.
No third-party libraries, multiprocessing, random choices, or chart changes.
"""

from fractions import Fraction as F
from functools import reduce
from itertools import combinations
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
import traceback


HERE = Path(__file__).resolve().parent
OUT = HERE / "independent-output.json"
P = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 3, 5))
KAPPA = (3, 4, 6)
ZERO = (F(0), F(0), F(0))
FULL = (0, 1, 2, 3)
CONTRACT_SHA = "7b8769fe6eb84fcaad86cde7b65e5debf79801b30f9c2ae41e0e2758c0968456"
DECLARED_SCIENCE_COMMIT = "7233ed3c"
COMMAND = "/usr/bin/python3 research/reverse/four-carrier-source-test/independent_subset.py"


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x for x in a)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def frequency(labels):
    return tuple(sum(P[j][i] for j in labels) for i in range(3))


def project(k, v):
    kk = dot(k, k)
    assert kk != 0
    ans = add(v, scale(-dot(k, v) / kk, k))
    assert dot(k, ans) == 0
    return ans


def vertex(left_labels, right_labels, left, right):
    """The ordered B vertex with its -i removed."""
    right_k = frequency(right_labels)
    out_k = tuple(x + y for x, y in
                  zip(frequency(left_labels), right_k))
    return project(out_k, scale(dot(left, right_k), right))


def partitions(labels):
    """Every nonempty proper subset as LEFT: both orders are retained."""
    for length in range(1, len(labels)):
        for left in combinations(labels, length):
            right = tuple(j for j in labels if j not in left)
            yield left, right


def shape_name(shape):
    if shape == "*":
        return "*"
    return "(" + shape_name(shape[0]) + "," + shape_name(shape[1]) + ")"


def evaluate(alpha, basis):
    # v,w are only the two contract-prescribed linear-basis probes.
    u4 = (F(3), F(-2), F(0)) if basis == "v" else (F(5), F(0), F(-2))
    seeds = (tuple(map(F, (0, 1, alpha))), tuple(map(F, (0, 0, 1))),
             tuple(map(F, (1, 0, 0))), u4)
    for k, u in zip(P, seeds):
        assert dot(k, u) == 0
    trees = {(j,): {"*": seeds[j]} for j in range(4)}
    # Shape sums are built locally on each labelled subset.  We do not
    # enumerate any unused frequencies or use a full Fourier convolution.
    for count in (2, 3, 4):
        for labels in combinations(range(4), count):
            result = {}
            for left, right in partitions(labels):
                for sl, vl in trees[left].items():
                    for sr, vr in trees[right].items():
                        shape = (sl, sr)
                        term = scale(F(1, count - 1),
                                     vertex(left, right, vl, vr))
                        result[shape] = add(result.get(shape, ZERO), term)
            trees[labels] = result
            assert all(dot(frequency(labels), v) == 0
                       for v in result.values())
    four = trees[FULL]
    pure_shape = (("*", "*"), ("*", "*"))
    assert len(four) == 5
    w = four[pure_shape]
    m = reduce(add, (v for shape, v in four.items() if shape != pure_shape),
               ZERO)
    total = reduce(add, four.values(), ZERO)
    assert total == add(w, m)
    assert dot(KAPPA, w) == dot(KAPPA, m) == 0
    return trees, w, m


def qstr(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else str(x)


def vec_json(v):
    return [qstr(x) for x in v]


def tree_json(trees):
    return {
        ",".join(str(j + 1) for j in labels): {
            "frequency": list(frequency(labels)),
            "ordered_shape_sums": {shape_name(s): vec_json(v)
                                   for s, v in data.items()}
        }
        for labels, data in trees.items()
    }


def mul_affine(a, b):
    return (a[0] * b[0], a[0] * b[1] + a[1] * b[0], a[1] * b[1])


def primitive(poly):
    degree = len(poly) - 1
    while degree >= 0 and poly[degree] == 0:
        degree -= 1
    if degree < 0:
        return []
    den = 1
    for c in poly[:degree + 1]:
        den = den * c.denominator // gcd(den, c.denominator)
    nums = [int(c * den) for c in poly[:degree + 1]]
    common = reduce(gcd, (abs(c) for c in nums))
    nums = [c // common for c in nums]
    if nums[-1] < 0:
        nums = [-c for c in nums]
    return nums


class Quadratic:
    """Q[theta]/(theta^2+B/A theta+C/A), used only if irreducible."""
    def __init__(self, a, b=0, coefficients=None):
        self.a, self.b = F(a), F(b)
        self.coefficients = coefficients

    def promote(self, other):
        return other if isinstance(other, Quadratic) else Quadratic(
            other, 0, self.coefficients)

    def __add__(self, other):
        other = self.promote(other)
        return Quadratic(self.a + other.a, self.b + other.b, self.coefficients)

    __radd__ = __add__

    def __neg__(self):
        return Quadratic(-self.a, -self.b, self.coefficients)

    def __sub__(self, other):
        return self + (-self.promote(other))

    def __rsub__(self, other):
        return self.promote(other) - self

    def __mul__(self, other):
        other = self.promote(other)
        c, b, a = map(F, self.coefficients)
        return Quadratic(self.a * other.a - self.b * other.b * c / a,
                         self.a * other.b + self.b * other.a
                         - self.b * other.b * b / a, self.coefficients)

    __rmul__ = __mul__

    def inverse(self):
        c, b, a = map(F, self.coefficients)
        conjugate = Quadratic(self.a - self.b * b / a, -self.b,
                             self.coefficients)
        norm = self * conjugate
        assert norm.b == 0 and norm.a != 0
        return Quadratic(conjugate.a / norm.a, conjugate.b / norm.a,
                         self.coefficients)

    def __truediv__(self, other):
        return self * self.promote(other).inverse()

    def __eq__(self, other):
        other = self.promote(other)
        return self.a == other.a and self.b == other.b

    def record(self):
        return {"constant": qstr(self.a), "theta": qstr(self.b)}


def element_json(x):
    return x.record() if isinstance(x, Quadratic) else qstr(x)


def affine_at(coefficients, x):
    return x * coefficients[1] + coefficients[0]


def mv(matrix, vector):
    return tuple(sum((entry * x for entry, x in zip(row, vector)), 0)
                 for row in matrix)


def root_records(poly):
    """All real roots; no exploratory alpha probes or floating evaluations."""
    if not poly:
        return "IDENTICALLY_ZERO_NOT_CERTIFIED", []
    if len(poly) == 1:
        return "NONZERO_CONSTANT_NO_REAL_ROOT", []
    if len(poly) == 2:
        root = -F(poly[0], poly[1])
        return "LINEAR", [{"value": root, "description": {"rational": qstr(root)}}]
    c, b, a = poly
    disc = b * b - 4 * a * c
    if disc < 0:
        return "QUADRATIC_NO_REAL_ROOT", []
    sq = isqrt(disc)
    if sq * sq == disc:
        values = sorted(set((-F(b + sq, 2 * a), -F(b - sq, 2 * a))))
        return ("QUADRATIC_DOUBLE" if disc == 0 else "QUADRATIC_TWO_RATIONAL"), [
            {"value": value, "description": {"rational": qstr(value)}}
            for value in values]
    # a>0 by primitive normalization.  sq<sqrt(disc)<sq+1 gives
    # exact rational intervals, one for each root, in increasing order.
    theta = Quadratic(0, 1, poly)
    intervals = ((F(-b - sq - 1, 2 * a), F(-b - sq, 2 * a)),
                 (F(-b + sq, 2 * a), F(-b + sq + 1, 2 * a)))
    records = []
    for sign, interval in zip(("-", "+"), intervals):
        lo, hi = interval
        assert lo < hi
        assert (a * lo * lo + b * lo + c) * (
            a * hi * hi + b * hi + c) < 0
        records.append({
            "value": theta,
            "description": {"minimal_polynomial_ascending": poly,
                            "expression": "(-B " + sign + " sqrt(discriminant))/(2A)",
                            "discriminant": str(disc),
                            "isolation_open": [qstr(lo), qstr(hi)]}})
    assert intervals[0][1] <= intervals[1][0]
    return "QUADRATIC_TWO_IRRATIONAL", records


def certify_root(root, m_affine, w_affine):
    x = root["value"]
    m = tuple(tuple(affine_at(c, x) for c in row) for row in m_affine)
    w = tuple(tuple(affine_at(c, x) for c in row) for row in w_affine)
    first_row = next((row for row in m[:2] if any(z != 0 for z in row)), None)
    # Full transversality means the first two rows determine the third.
    assert all(3 * m[0][j] + 4 * m[1][j] + 6 * m[2][j] == 0 for j in range(2))
    assert all(3 * w[0][j] + 4 * w[1][j] + 6 * w[2][j] == 0 for j in range(2))
    if first_row is None:
        rank = 0
        kernels = ((F(1), F(0)), (F(0), F(1)))
    else:
        rank = 1
        raw = (-first_row[1], first_row[0])
        first = next(z for z in raw if z != 0)
        kernels = (tuple(z / first for z in raw),)
    trials = []
    for kernel in kernels:
        residual = mv(m, kernel)
        supplied = mv(w, kernel)
        assert all(z == 0 for z in residual)
        passed = any(z != 0 for z in supplied)
        trials.append({"normalized_kernel_v_w": [element_json(z) for z in kernel],
                       "M_stripped": [element_json(z) for z in residual],
                       "W_stripped": [element_json(z) for z in supplied],
                       "W_nonzero": passed})
        if passed:
            break
    return {"root": root["description"], "rank": rank, "trials": trials,
            "passed_algebra": any(trial["W_nonzero"] for trial in trials)}


def experiment():
    assert hashlib.sha256((HERE / "CONTRACT.md").read_bytes()).hexdigest() == CONTRACT_SHA
    evaluations = {}
    table = {}
    for alpha in (0, 1, -1):
        for basis in ("v", "w"):
            trees, w, m = evaluate(alpha, basis)
            evaluations[(alpha, basis)] = (trees, w, m)
            table["alpha=" + str(alpha) + ",basis=" + basis] = {
                "subsets": tree_json(trees),
                "W_stripped": vec_json(w), "M_stripped": vec_json(m)}
    # The -1 check is applied to EVERY subset/shape, not just the root sum.
    for basis in ("v", "w"):
        t0 = evaluations[(0, basis)][0]
        t1 = evaluations[(1, basis)][0]
        tm = evaluations[(-1, basis)][0]
        for subset in t0:
            for shape in t0[subset]:
                assert tm[subset][shape] == add(scale(2, t0[subset][shape]),
                                                scale(-1, t1[subset][shape]))
    def matrix(which):
        return tuple(tuple((evaluations[(0, basis)][which][i],
                            evaluations[(1, basis)][which][i]
                            - evaluations[(0, basis)][which][i])
                           for basis in ("v", "w")) for i in range(3))
    w_affine, m_affine = matrix(1), matrix(2)
    det = tuple(x - y for x, y in zip(mul_affine(m_affine[0][0], m_affine[1][1]),
                                     mul_affine(m_affine[0][1], m_affine[1][0])))
    poly = primitive(det)
    kind, roots = root_records(poly)
    certifications = [certify_root(root, m_affine, w_affine) for root in roots]
    accepted_index = next((j for j, item in enumerate(certifications)
                           if item["passed_algebra"]), None)
    if kind == "IDENTICALLY_ZERO_NOT_CERTIFIED":
        outcome = "INCONCLUSIVE_IDENTICALLY_ZERO_DETERMINANT"
    elif accepted_index is None:
        outcome = "NO_CANDIDATE_IN_THIS_CHART_ALGEBRA"
    else:
        outcome = "ALGEBRA_PASS_ONLY"
    return {
        "scientific_arithmetic": "fractions.Fraction and exact integer operations only",
        "physical_phase": "v_n leading coefficient = (-i)^n times stripped value; W0 and M0 at +kappa = i times output",
        "negative_receiver": "complex conjugate; short-leaf uniqueness proved separately by hand",
        "initial_frequencies": [list(p) for p in P],
        "receiver": list(KAPPA),
        "shape_count": 5,
        "alpha_probes": [0, 1, -1],
        "probe_role": "0,1 affine recovery; -1 check for every labelled subset and shape",
        "evaluations": table,
        "affine_coefficient_order": ["constant", "alpha"],
        "M_3_by_2": [[vec_json(entry) for entry in row] for row in m_affine],
        "W_3_by_2": [[vec_json(entry) for entry in row] for row in w_affine],
        "determinant_ascending": vec_json(det),
        "determinant_primitive_ascending": poly,
        "determinant_kind": kind,
        "root_certifications": certifications,
        "selected_root_index_zero_based": accepted_index,
        "outcome": outcome,
        "not_certified_here": ["positive-time full NS errors", "source dominance time window",
                               "any other parameter chart", "iteration or singularity"]}


def alarm_handler(signum, frame):
    raise TimeoutError("60-second one-run wall budget exceeded")


def main():
    start = time.perf_counter()
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(60)
    record = {
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "contract_sha256": CONTRACT_SHA,
        "declared_parent_science_commit": DECLARED_SCIENCE_COMMIT,
        "commit_provenance": "provided in parent assignment; no Git command used",
        "command": COMMAND, "argv": sys.argv,
        "environment": {"python": sys.version, "executable": sys.executable,
                        "platform": platform.platform(), "machine": platform.machine(),
                        "processor": platform.processor(), "logical_cpu_count": os.cpu_count(),
                        "process_count": 1, "scientific_worker_threads": 1,
                        "third_party_libraries": [], "float_scientific_operations": False},
        "resource_contract": {"wall_seconds_max": 60, "target_peak_bytes": 256 * 1024 * 1024,
                              "output_bytes_max": 1024 * 1024}}
    status = 0
    try:
        record["result"] = experiment()
        record["execution_status"] = "completed"
    except Exception:
        status = 1
        record["execution_status"] = "NOT_CERTIFIED"
        record["error"] = traceback.format_exc()
    finally:
        signal.alarm(0)
        usage = resource.getrusage(resource.RUSAGE_SELF)
        peak = usage.ru_maxrss if sys.platform == "darwin" else 1024 * usage.ru_maxrss
        record["resource_evidence"] = {
            "wall_seconds_before_serialization": time.perf_counter() - start,
            "user_cpu_seconds": usage.ru_utime, "system_cpu_seconds": usage.ru_stime,
            "peak_resident_bytes": peak,
            "wall_and_resource_numbers_are_metadata_only": True}
        if peak > 256 * 1024 * 1024:
            status = 1
            record["execution_status"] = "NOT_CERTIFIED_RESOURCE_TARGET_EXCEEDED"
        content = json.dumps(record, ensure_ascii=False, indent=2) + "\n"
        if len(content.encode()) >= 1024 * 1024:
            status = 1
            record = {"execution_status": "NOT_CERTIFIED_OUTPUT_BOUND_EXCEEDED",
                      "source_sha256": record["source_sha256"]}
            content = json.dumps(record, indent=2) + "\n"
        OUT.write_text(content, encoding="utf-8")
        print(json.dumps({"execution_status": record["execution_status"],
                          "outcome": record.get("result", {}).get("outcome"),
                          "output_path": str(OUT),
                          "output_sha256": hashlib.sha256(OUT.read_bytes()).hexdigest(),
                          "source_sha256": record["source_sha256"],
                          "resource_evidence": record.get("resource_evidence")},
                         ensure_ascii=False, indent=2))
    return status


if __name__ == "__main__":
    sys.exit(main())
