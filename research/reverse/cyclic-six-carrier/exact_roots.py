#!/usr/bin/env python3
"""Stage B, prepared source only until a separate saved-source execution gate.

Read the frozen stage-A coefficients; do not generate Fourier coefficients.
Use rational square-free decomposition and one global half-open Sturm tree.
Q is allowed to be reducible: zero tests use gcd(Q,f) at a specified root,
never an inverse in Q[X]/(Q). Original M rows determine the fixed amplitudes.
No import, compilation probe, test run, factor/root probe, or retry is allowed.
"""

import time

MODULE_START = time.perf_counter()

import argparse
from fractions import Fraction
import hashlib
import json
from math import gcd
import os
from pathlib import Path
import resource
import signal
import sys


CONTRACT_SHA = "a441be9b7adf0ee900eeaa786119e7c6f8fecb4c3a01bc4678f1c23fddad1a9b"
A_INPUT_SHA = "9329464c09faa50558bc090b3af8c3ec6f074619e01a9fe2d5eb6d0f1c079ae6"
METHOD_SHA = "2fb88e7166ee62fa1b3df24415542970580bb3d520971386b482f5a5db80453a"
GATE_SHA = "af692a572eee828b7415e29fb784197c10329e3c98cdf0a5a765ec6b884fe39f"
A_SAVED_COMMIT = "1865656c86a4824069a32186d3928be226dc8d98"
WALL_LIMIT_SECONDS = 60
SELF_RSS_LIMIT_BYTES = 256 * 1024 * 1024
OUTPUT_LIMIT_BYTES = 1024 * 1024
MAX_ROOT_DEPTH = 128


class NotCertified(Exception):
    """A budget or required certificate has not been completed."""


class InconsistentCertificate(NotCertified):
    """A claimed exact identity or already-certified root is inconsistent."""


def require(condition, message):
    if not condition:
        raise InconsistentCertificate(message)


def resource_snapshot():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    darwin = os.uname().sysname == "Darwin"
    return {
        "wall_seconds_since_module_start": time.perf_counter() - MODULE_START,
        "user_CPU_seconds_SELF": usage.ru_utime,
        "system_CPU_seconds_SELF": usage.ru_stime,
        "maximum_RSS_SELF_bytes": usage.ru_maxrss if darwin else usage.ru_maxrss * 1024,
        "RSS_conversion": ("Darwin ru_maxrss is bytes" if darwin
                           else "non-Darwin ru_maxrss interpreted as KiB"),
    }


def budget_problems(snapshot):
    problems = []
    if snapshot["wall_seconds_since_module_start"] > WALL_LIMIT_SECONDS:
        problems.append("WALL_BUDGET_EXCEEDED")
    if snapshot["maximum_RSS_SELF_bytes"] > SELF_RSS_LIMIT_BYTES:
        problems.append("SELF_RSS_TARGET_EXCEEDED")
    return problems


def budget_guard():
    problems = budget_problems(resource_snapshot())
    if problems:
        raise NotCertified(",".join(problems))


# Reused mathematical representation from stage A, without importing it.
def poly(values):
    values = tuple(Fraction(x) for x in values)
    if not values:
        return (Fraction(0),)
    last = len(values) - 1
    while last and values[last] == 0:
        last -= 1
    return values[:last + 1]


ZERO = poly((0,))
ONE = poly((1,))
ALPHA = poly((0, 1))


def degree(a):
    return -1 if a == ZERO else len(a) - 1


def add(a, b):
    result = [Fraction(0)] * max(len(a), len(b))
    for j, x in enumerate(a):
        result[j] += x
    for j, x in enumerate(b):
        result[j] += x
    return poly(result)


def scale(a, c):
    return poly(c * x for x in a)


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    result = [Fraction(0)] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            result[j + k] += x * y
    return poly(result)


def derivative(a):
    return poly(j * a[j] for j in range(1, len(a)))


def evaluate(a, x):
    value = Fraction(0)
    for coefficient in reversed(a):
        value = value * x + coefficient
    return value


def divide(a, b):
    require(b != ZERO, "polynomial division by zero")
    q = [Fraction(0)] * max(1, degree(a) - degree(b) + 1)
    r = a
    while r != ZERO and degree(r) >= degree(b):
        budget_guard()
        shift = degree(r) - degree(b)
        coefficient = r[-1] / b[-1]
        q[shift] += coefficient
        r = sub(r, poly([Fraction(0)] * shift + list(scale(b, coefficient))))
    q = poly(q)
    require(add(mul(q, b), r) == a, "division reconstruction failed")
    require(r == ZERO or degree(r) < degree(b), "division remainder degree failed")
    return q, r


def exact_divide(a, b):
    q, r = divide(a, b)
    require(r == ZERO, "required exact division has nonzero remainder")
    return q


def positive_primitive(a):
    """Return c*a and exact c>0, preserving every coefficient sign."""
    if a == ZERO:
        return ZERO, Fraction(1)
    denominator = 1
    for x in a:
        denominator = denominator * x.denominator // gcd(denominator, x.denominator)
    integers = [x.numerator * (denominator // x.denominator) for x in a]
    content = 0
    for x in integers:
        content = gcd(content, abs(x))
    require(content > 0, "nonzero polynomial has zero content")
    multiplier = Fraction(denominator, content)
    result = scale(a, multiplier)
    require(multiplier > 0 and all(x.denominator == 1 for x in result),
            "positive primitive scaling failed")
    return result, multiplier


def parse_poly(record):
    values = record["coefficients_low_to_high"]
    require(isinstance(values, list) and values, "bad coefficient list")
    require(all(isinstance(x, str) for x in values), "coefficients are not strings")
    result = poly(Fraction(x) for x in values)
    require(len(result) == len(values), "noncanonical input trailing zeros")
    require(degree(result) == record["degree"], "input polynomial degree mismatch")
    return result


def parse_vector(records):
    require(len(records) == 3, "vector lost a component")
    return tuple(parse_poly(x) for x in records)


def parse_matrix(records, rows):
    require(len(records) == rows and all(len(row) == 2 for row in records),
            "matrix shape mismatch")
    return tuple(tuple(parse_poly(x) for x in row) for row in records)


def rotate(vector, times):
    for unused in range(times):
        vector = (vector[2], vector[0], vector[1])
    return vector


def normal_dot(k, vector):
    value = ZERO
    for coefficient, component in zip(k, vector):
        value = add(value, scale(component, coefficient))
    return value


def apply_matrix(matrix, v, w):
    return tuple(add(mul(row[0], v), mul(row[1], w)) for row in matrix)


def interval_multiply(left, right):
    products = (left[0] * right[0], left[0] * right[1],
                left[1] * right[0], left[1] * right[1])
    return min(products), max(products)


def interval_evaluate(polynomial, interval):
    value = (Fraction(0), Fraction(0))
    for coefficient in reversed(polynomial):
        value = interval_multiply(value, interval)
        value = (value[0] + coefficient, value[1] + coefficient)
    return value


def interval_record(interval):
    return [str(interval[0]), str(interval[1])]


class Evidence:
    """Deduplicated exact polynomial, Euclidean, Sturm and root-test evidence."""

    def __init__(self, report):
        self.report = report
        self.polynomial_ids = {}
        self.gcd_cache = {}
        self.sturm_cache = {}
        self.zero_cache = {}
        self.nodes = []
        self.roots = []
        self.q = None
        self.q_chain = None
        for name in ("polynomials", "gcd_certificates", "sturm_chains",
                     "isolation_nodes", "zero_tests", "roots"):
            report[name] = []

    def register(self, polynomial):
        if polynomial not in self.polynomial_ids:
            identifier = len(self.report["polynomials"])
            self.polynomial_ids[polynomial] = identifier
            self.report["polynomials"].append({
                "id": identifier, "degree": degree(polynomial),
                "coefficients_low_to_high": [str(x) for x in polynomial],
            })
        return self.polynomial_ids[polynomial]

    def vector_ids(self, vector):
        return [self.register(x) for x in vector]

    def matrix_ids(self, matrix):
        return [self.vector_ids(row) for row in matrix]

    def gcd(self, a, b):
        key = (a, b)
        if key in self.gcd_cache:
            return self.gcd_cache[key]
        require(a != ZERO or b != ZERO, "gcd(0,0) not used by this certificate")
        x, sx = positive_primitive(a)
        y, sy = positive_primitive(b)
        record = {
            "id": len(self.report["gcd_certificates"]),
            "inputs": [self.register(a), self.register(b)],
            "initial_positive_multipliers": [str(sx), str(sy)],
            "initial_polynomials": [self.register(x), self.register(y)],
            "steps": [],
            "step_identity": "left = quotient*right + next/positive_multiplier",
        }
        self.report["gcd_certificates"].append(record)
        while y != ZERO:
            budget_guard()
            quotient, remainder = divide(x, y)
            next_polynomial, multiplier = positive_primitive(remainder)
            require(add(mul(quotient, y), scale(next_polynomial, 1 / multiplier)) == x,
                    "scaled Euclidean identity failed")
            record["steps"].append({
                "left": self.register(x), "right": self.register(y),
                "quotient": self.register(quotient),
                "next": self.register(next_polynomial),
                "positive_multiplier": str(multiplier),
            })
            x, y = y, next_polynomial
        require(x != ZERO, "gcd unexpectedly zero")
        final_multiplier = 1 / x[-1]
        result = scale(x, final_multiplier)
        # Monic gcd normalization may be negative; this is NOT Sturm scaling.
        record["final_monic_multiplier_not_a_Sturm_scaling"] = str(final_multiplier)
        record["result"] = self.register(result)
        record["input_quotients_by_result"] = [
            self.register(exact_divide(a, result)),
            self.register(exact_divide(b, result)),
        ]
        record["verified"] = True
        answer = result, record["id"]
        self.gcd_cache[key] = answer
        return answer

    def sturm(self, q):
        if q in self.sturm_cache:
            return self.sturm_cache[q]
        require(q != ZERO, "Sturm requested for identically zero polynomial")
        s0 = q
        record = {
            "id": len(self.report["sturm_chains"]),
            "input": self.register(q),
            "polynomials": [self.register(s0)],
            "S0_multiplier": "1",
            "negative_remainder_steps": [],
        }
        self.report["sturm_chains"].append(record)
        chain = [s0]
        if degree(q) > 0:
            s1, first_multiplier = positive_primitive(derivative(q))
            record["S1_positive_multiplier_of_derivative"] = str(first_multiplier)
            chain.append(s1)
            record["polynomials"].append(self.register(s1))
            while True:
                budget_guard()
                quotient, remainder = divide(chain[-2], chain[-1])
                if remainder == ZERO:
                    require(degree(chain[-1]) == 0,
                            "Sturm input is not square-free")
                    record["terminal_quotient"] = self.register(quotient)
                    record["terminal_remainder"] = self.register(ZERO)
                    break
                next_polynomial, multiplier = positive_primitive(scale(remainder, -1))
                require(multiplier > 0, "nonpositive Sturm scaling")
                require(next_polynomial == scale(remainder, -multiplier),
                        "negative Sturm remainder identity failed")
                record["negative_remainder_steps"].append({
                    "quotient": self.register(quotient),
                    "positive_multiplier": str(multiplier),
                    "next": self.register(next_polynomial),
                })
                chain.append(next_polynomial)
                record["polynomials"].append(self.register(next_polynomial))
        else:
            record["constant_root_count"] = 0
        record["verified"] = True
        answer = tuple(chain), record["id"]
        self.sturm_cache[q] = answer
        return answer

    @staticmethod
    def variation(chain, endpoint):
        signs = []
        for polynomial in chain:
            value = evaluate(polynomial, endpoint)
            if value:
                signs.append(1 if value > 0 else -1)
        return sum(left != right for left, right in zip(signs, signs[1:]))

    def count(self, polynomial, a, b):
        require(a < b, "half-open root interval is not ordered")
        chain, chain_id = self.sturm(polynomial)
        left = self.variation(chain, a)
        right = self.variation(chain, b)
        count = left - right
        require(0 <= count <= degree(polynomial) or degree(polynomial) == 0 and count == 0,
                "Sturm count outside degree range")
        return count, {
            "sturm_chain": chain_id, "interval": [str(a), str(b)],
            "ownership": "(a,b]", "V_a": left, "V_b": right, "count": count,
        }

    def node(self, a, b, depth, parent, side, purpose):
        budget_guard()
        count, count_record = self.count(self.q, a, b)
        internal = {"a": a, "b": b, "depth": depth, "count": count,
                    "id": len(self.nodes)}
        self.nodes.append(internal)
        record = dict(count_record)
        record.update({"id": internal["id"], "depth": depth,
                       "parent": parent, "side": side, "purpose": purpose,
                       "right_endpoint_is_Q_root": evaluate(self.q, b) == 0})
        self.report["isolation_nodes"].append(record)
        return internal

    def split(self, node, purpose):
        if node["depth"] >= MAX_ROOT_DEPTH:
            self.report["unresolved_node"] = node["id"]
            raise NotCertified("PER_ROOT_128_BISECTION_BUDGET_EXHAUSTED")
        middle = (node["a"] + node["b"]) / 2
        depth = node["depth"] + 1
        left = self.node(node["a"], middle, depth, node["id"], "left", purpose)
        right = self.node(middle, node["b"], depth, node["id"], "right", purpose)
        require(left["count"] + right["count"] == node["count"],
                "child Sturm counts do not sum to parent")
        self.report["isolation_nodes"][node["id"]]["children"] = [left["id"], right["id"]]
        return left, right

    def isolate(self, node):
        if node["count"] == 0:
            self.report["isolation_nodes"][node["id"]]["status"] = "empty"
            return
        if node["count"] == 1:
            root = {"index": len(self.roots), "initial_node": node,
                    "current_node": node}
            self.roots.append(root)
            self.report["roots"].append({
                "index": root["index"], "initial_node": node["id"],
                "current_node": node["id"],
                "exact_rational_point_if_detected": (
                    str(node["b"]) if evaluate(self.q, node["b"]) == 0 else None),
                "cumulative_bisection_depth": node["depth"],
                "classification_complete": False,
            })
            self.report["isolation_nodes"][node["id"]]["status"] = "one_root"
            return
        self.report["isolation_nodes"][node["id"]]["status"] = "split_multiple_roots"
        left, right = self.split(node, "global_all_root_isolation")
        self.isolate(left)
        self.isolate(right)

    def zero_test(self, root, f):
        key = (root["index"], f)
        if key in self.zero_cache:
            return self.zero_cache[key]
        node = root["current_node"]
        divisor, gcd_id = self.gcd(self.q, f)
        count, count_record = self.count(divisor, node["a"], node["b"])
        require(count in (0, 1), "gcd has multiple roots in a Q-single-root interval")
        zero = count == 1
        record = {
            "id": len(self.report["zero_tests"]), "root_index": root["index"],
            "polynomial": self.register(f), "gcd_certificate": gcd_id,
            "gcd_polynomial": self.register(divisor), "root_node": node["id"],
            "gcd_count": count_record, "is_zero_at_specified_root": zero,
        }
        if evaluate(self.q, node["b"]) == 0:
            value = evaluate(f, node["b"])
            require((value == 0) == zero, "point and gcd zero tests disagree")
            record["exact_point_value"] = str(value)
        self.report["zero_tests"].append(record)
        answer = zero, record["id"]
        self.zero_cache[key] = answer
        return answer

    def vector_tests(self, root, vector):
        tests = [self.zero_test(root, f) for f in vector]
        return [zero for zero, unused in tests], [identifier for unused, identifier in tests]


def read_stored_coefficients(data, evidence):
    require(data["schema"] == "cyclic-six-carrier-stage-A-exact-coefficients-v1",
            "unexpected A schema")
    require(data["execution_status"] == "completed"
            and data["stage_A_outcome"] == "COEFFICIENTS_CERTIFIED_ROOT_STAGE_PENDING"
            and data["scientific_execution_count_in_this_invocation"] == 1
            and data["scientific_stage_completed"] is True, "A stage is not certified")
    require(data["exact_checks"] and all(x is True for x in data["exact_checks"].values()),
            "A exact check is not true")
    matrices = data["primary_matrices"]
    c = parse_matrix(matrices["C_full_three_rows_v_w_columns"], 3)
    z = parse_matrix(matrices["Z_full_three_rows_v_w_columns"], 3)
    m = parse_matrix(matrices["M_first_two_Z_rows"], 2)
    p = parse_poly(matrices["P_determinant"])
    require(m == z[:2], "original M is not the stored first two Z rows")
    determinant = sub(mul(m[0][0], m[1][1]), mul(m[0][1], m[1][0]))
    require(p == determinant, "stored P is not determinant of original M")
    require(degree(p) <= 6, "P exceeds fixed degree bound")
    for matrix in (c, z):
        for column in range(2):
            vector = tuple(row[column] for row in matrix)
            require(normal_dot((3, 4, 6), vector) == ZERO, "primary transverse identity failed")
            require(all(degree(f) <= 3 for f in vector), "primary degree exceeds three")
    target_matrices = []
    records = data["target_records"]
    require(len(records) == 6, "A target count changed")
    primary_fields = {}
    for column_name in ("v", "w"):
        primary_fields[column_name] = {
            name: parse_vector(values) for name, values in
            records[0]["columns"][column_name]["root_vectors"].items()
        }
    fields = {"C", "M13", "M31", "Z", "full_four_leaf"}
    for index, record in enumerate(records):
        rotation, sign = index // 2, 1 if index % 2 == 0 else -1
        target = tuple(sign * x for x in rotate((3, 4, 6), rotation))
        require(record["rotation_index"] == rotation and record["sign"] == sign
                and tuple(record["target"]) == target, "target ordering or orbit changed")
        columns = {}
        for column_index, column_name in enumerate(("v", "w")):
            roots = record["columns"][column_name]["root_vectors"]
            require(set(roots) == fields, "stored root field set changed")
            roots = {name: parse_vector(value) for name, value in roots.items()}
            for name in fields:
                expected = tuple(scale(f, sign) for f in
                                 rotate(primary_fields[column_name][name], rotation))
                require(roots[name] == expected, "stored six-target covariance failed")
                require(normal_dot(target, roots[name]) == ZERO, "stored field not transverse")
            require(tuple(add(x, y) for x, y in zip(roots["M13"], roots["M31"])) == roots["Z"],
                    "stored complete M13+M31 identity failed")
            require(tuple(add(x, y) for x, y in zip(roots["C"], roots["Z"])) == roots["full_four_leaf"],
                    "stored complete root total identity failed")
            if index == 0:
                require(roots["C"] == tuple(row[column_index] for row in c)
                        and roots["Z"] == tuple(row[column_index] for row in z),
                        "primary matrix differs from actual root columns")
            columns[column_name] = roots
        target_matrices.append({
            "target": target,
            "C": tuple((columns["v"]["C"][j], columns["w"]["C"][j]) for j in range(3)),
            "Z": tuple((columns["v"]["Z"][j], columns["w"]["Z"][j]) for j in range(3)),
        })
    evidence.report["stored_input_identity_checks"] = {
        "P_equals_original_M_determinant": True,
        "original_M_equals_first_two_complete_Z_rows": True,
        "all_six_stored_C_Z_M13_M31_total_and_transversality": True,
        "no_Fourier_coefficient_regeneration": True,
    }
    evidence.report["original_inputs"] = {
        "C": evidence.matrix_ids(c), "Z": evidence.matrix_ids(z),
        "M_unscaled": evidence.matrix_ids(m), "P": evidence.register(p),
        "physical_phase_C_Z": "+i",
    }
    return c, z, m, p, target_matrices


def square_free(p, evidence):
    leading = p[-1]
    f = scale(p, 1 / leading)
    g, initial_gcd = evidence.gcd(f, derivative(f))
    q = exact_divide(f, g)
    w = q
    factors = []
    steps = []
    record = {
        "original_leading_coefficient": str(leading),
        "monic_F": evidence.register(f), "initial_derivative_gcd": initial_gcd,
        "Q": evidence.register(q), "steps": steps, "factors": [],
        "irreducibility_claimed": False,
    }
    evidence.report["square_free_decomposition"] = record
    multiplicity = 1
    while w != ONE:
        budget_guard()
        require(multiplicity <= degree(p), "square-free loop exceeded degree")
        y, gcd_id = evidence.gcd(w, g)
        factor = exact_divide(w, y)
        next_g = exact_divide(g, y)
        steps.append({"multiplicity": multiplicity, "w": evidence.register(w),
                      "g": evidence.register(g), "gcd_certificate": gcd_id,
                      "y": evidence.register(y), "factor": evidence.register(factor),
                      "next_g": evidence.register(next_g)})
        if factor != ONE:
            require(degree(factor) > 0, "unexpected constant square-free factor")
            factors.append((multiplicity, factor))
            record["factors"].append({"multiplicity": multiplicity,
                                      "polynomial": evidence.register(factor)})
        w, g = y, next_g
        multiplicity += 1
    require(g == ONE, "square-free residual g is not one")
    reconstruction = ONE
    q_product = ONE
    square_free_gcd_ids = []
    coprime_gcd_ids = []
    for index, (multiplicity, factor) in enumerate(factors):
        for unused in range(multiplicity):
            reconstruction = mul(reconstruction, factor)
        q_product = mul(q_product, factor)
        divisor, identifier = evidence.gcd(factor, derivative(factor))
        require(divisor == ONE, "factor is not square-free")
        square_free_gcd_ids.append(identifier)
        for unused_multiplicity, earlier in factors[:index]:
            divisor, identifier = evidence.gcd(earlier, factor)
            require(divisor == ONE, "square-free factors are not pairwise coprime")
            coprime_gcd_ids.append(identifier)
    require(reconstruction == f and scale(reconstruction, leading) == p,
            "square-free reconstruction failed")
    require(q_product == q, "global Q differs from factor product")
    divisor, q_gcd = evidence.gcd(q, derivative(q))
    require(divisor == ONE, "global Q is not square-free")
    record.update({"reconstruction": evidence.register(reconstruction),
                   "square_free_gcd_certificates": square_free_gcd_ids,
                   "pairwise_coprime_gcd_certificates": coprime_gcd_ids,
                   "Q_square_free_gcd_certificate": q_gcd, "verified": True})
    return q, factors


def classify_root(root, factors, c, z, m, p, target_matrices, evidence):
    record = evidence.report["roots"][root["index"]]
    node = root["current_node"]
    memberships = []
    for multiplicity, factor in factors:
        count, count_record = evidence.count(factor, node["a"], node["b"])
        require(count in (0, 1), "factor count outside single-root domain")
        memberships.append({"multiplicity": multiplicity,
                            "polynomial": evidence.register(factor),
                            "count_certificate": count_record})
    selected = [x for x in memberships if x["count_certificate"]["count"] == 1]
    require(len(selected) == 1, "root has nonunique square-free factor membership")
    record["factor_memberships"] = memberships
    record["original_P_root_multiplicity"] = selected[0]["multiplicity"]
    determinant_zero, determinant_test = evidence.zero_test(root, p)
    record["determinant_zero_test"] = determinant_test
    if not determinant_zero:
        record["rank"] = 2
        raise InconsistentCertificate("rank 2 at a certified P root; stop, do not skip")
    row_zero = []
    record["M_entry_zero_tests_in_original_row_order"] = []
    for row in m:
        zeros, tests = evidence.vector_tests(root, row)
        row_zero.append(all(zeros))
        record["M_entry_zero_tests_in_original_row_order"].append(tests)
    rank = 0 if all(row_zero) else 1
    record["rank"] = rank
    if rank == 1:
        row_index = 0 if not row_zero[0] else 1
        r, s = m[row_index]
        v, w = scale(s, -1), r
        record["normalization"] = {
            "rule": "(v,w)=(-s,r) from first nonzero ORIGINAL M row",
            "original_row_index": row_index,
            "original_r_s": [evidence.register(r), evidence.register(s)],
            "no_row_scaling_or_denominator_clearing": True,
        }
    else:
        first_column = tuple(row[0] for row in c)
        zeros, tests = evidence.vector_tests(root, first_column)
        record["rank_zero_first_C_column_tests"] = tests
        if not all(zeros):
            v, w = ONE, ZERO
            chosen_column = 0
        else:
            v, w = ZERO, ONE
            chosen_column = 1
        record["normalization"] = {
            "rule": "first C column if nonzero, otherwise second C column",
            "chosen_column_index": chosen_column,
        }
    normalized_c = apply_matrix(c, v, w)
    normalized_z = apply_matrix(z, v, w)
    high = (add(scale(v, 3), scale(w, 5)), scale(v, -2), scale(w, -2))
    vw_zeros, vw_tests = evidence.vector_tests(root, (v, w))
    high_zeros, high_tests = evidence.vector_tests(root, high)
    z_zeros, z_tests = evidence.vector_tests(root, normalized_z)
    c_zeros, c_tests = evidence.vector_tests(root, normalized_c)
    record["normalized_polynomials"] = {
        "v": evidence.register(v), "w": evidence.register(w),
        "V": evidence.vector_ids(high), "Z": evidence.vector_ids(normalized_z),
        "C": evidence.vector_ids(normalized_c),
    }
    record["normalized_zero_tests"] = {
        "v_w": vw_tests, "V": high_tests, "Z": z_tests, "C": c_tests,
    }
    require(not all(vw_zeros), "normalization produced zero amplitude pair")
    require(not all(high_zeros), "nonzero amplitude pair produced zero V")
    require(all(z_zeros), "normalized complete three-component Z is nonzero")
    record["all_six_normalized_target_vectors"] = []
    for target in target_matrices:
        tc = apply_matrix(target["C"], v, w)
        tz = apply_matrix(target["Z"], v, w)
        tc_zeros, tc_tests = evidence.vector_tests(root, tc)
        tz_zeros, tz_tests = evidence.vector_tests(root, tz)
        require(all(tz_zeros), "a rotated or conjugate full Z target is nonzero")
        require(all(tc_zeros) == all(c_zeros), "target C nonzero status breaks covariance")
        record["all_six_normalized_target_vectors"].append({
            "target": list(target["target"]), "C": evidence.vector_ids(tc),
            "Z": evidence.vector_ids(tz), "C_zero_tests": tc_tests,
            "Z_zero_tests": tz_tests, "C_is_nonzero": not all(tc_zeros),
            "Z_is_zero": True,
        })
    record["C_component_zero_flags"] = c_zeros
    record["eligible"] = not all(c_zeros)
    record["classification_complete"] = True
    root.update({"v": v, "w": w, "V": high, "C": normalized_c,
                 "eligible": not all(c_zeros), "C_zero_flags": c_zeros})


def certify_window(root, evidence):
    """Refine only the preselected first eligible root, without resetting depth."""
    record = evidence.report["roots"][root["index"]]
    coordinate = next(j for j, zero in enumerate(root["C_zero_flags"]) if not zero)
    f = root["C"][coordinate]
    window = {"selected_root_index": root["index"],
              "first_nonzero_C_coordinate_index": coordinate,
              "C_coordinate_polynomial": evidence.register(f),
              "refinement_trace": [], "certified": False}
    evidence.report["selected_window"] = window
    while True:
        budget_guard()
        node = root["current_node"]
        point = evaluate(evidence.q, node["b"]) == 0
        interval = (node["b"], node["b"]) if point else (node["a"], node["b"])
        enclosure = interval_evaluate(f, interval)
        avoids_zero = enclosure[0] > 0 or enclosure[1] < 0
        window["refinement_trace"].append({
            "root_node": node["id"], "cumulative_depth": node["depth"],
            "closed_input_enclosure": interval_record(interval),
            "C_coordinate_closed_enclosure": interval_record(enclosure),
            "strictly_avoids_zero": avoids_zero,
        })
        if avoids_zero:
            break
        require(not point, "gcd-nonzero C coordinate vanishes at exact point")
        left, right = evidence.split(node, "selected_root_C_lower_bound")
        require(sorted((left["count"], right["count"])) == [0, 1],
                "single root refinement lost uniqueness")
        root["current_node"] = left if left["count"] == 1 else right
        node = root["current_node"]
        record["current_node"] = node["id"]
        record["cumulative_bisection_depth"] = node["depth"]
        record["exact_rational_point_if_detected"] = (
            str(node["b"]) if evaluate(evidence.q, node["b"]) == 0 else None)
    delta = min(abs(enclosure[0]), abs(enclosure[1]))
    require(delta > 0, "C lower bound is not positive")
    ell = 2 * delta
    alpha_bound = max(abs(interval[0]), abs(interval[1]))
    v_interval = interval_evaluate(root["v"], interval)
    w_interval = interval_evaluate(root["w"], interval)
    high_intervals = [interval_evaluate(fj, interval) for fj in root["V"]]
    uv = max(abs(v_interval[0]), abs(v_interval[1]))
    uw = max(abs(w_interval[0]), abs(w_interval[1]))
    uv1 = max(abs(high_intervals[0][0]), abs(high_intervals[0][1]))
    abar = 6 * (1 + alpha_bound + uv1 + 2 * uv + 2 * uw)
    bbar = 4 * abar * 7
    ebar = 80 * abar ** 4 * 7 ** 5 + 3 * abar * bbar ** 4
    dfirst = 2 * (1 + alpha_bound ** 2) + 2 * abar * bbar ** 2
    candidates = (1 / (2 * bbar), ell / (8 * ebar), 1 / (2 * dfirst))
    main_t = min(candidates)
    require(all(x > 0 for x in (abar, bbar, ebar, dfirst, ell, main_t) + candidates),
            "nonpositive window constant")
    budgets = ((bbar * main_t, Fraction(1, 2)),
               (ebar * main_t, ell / 8),
               (dfirst * main_t, Fraction(1, 2)))
    require(all(left <= right for left, right in budgets), "main T fails an original budget")
    window.update({
        "final_root_node": root["current_node"]["id"],
        "cumulative_bisection_depth": root["current_node"]["depth"],
        "alpha_closed_enclosure": interval_record(interval),
        "C_coordinate_closed_enclosure": interval_record(enclosure),
        "delta_near_zero_endpoint_absolute_value": str(delta), "ell": str(ell),
        "v_closed_enclosure": interval_record(v_interval),
        "w_closed_enclosure": interval_record(w_interval),
        "V_three_coordinate_closed_enclosures": [interval_record(x) for x in high_intervals],
        "Aalpha": str(alpha_bound), "Uv": str(uv), "Uw": str(uw), "UV1": str(uv1),
        "Abar": str(abar), "bbar": str(bbar), "Ebar": str(ebar), "Dfirst": str(dfirst),
        "Abar_formula": "6*(1+Aalpha+UV1+2*Uv+2*Uw), original M normalization",
        "three_time_candidates_in_contract_order": [str(x) for x in candidates],
        "T": str(main_t),
        "minimum_attaining_indices": [j for j, x in enumerate(candidates) if x == main_t],
        "exact_budget_certificates": [
            {"name": name, "left": str(left), "right": str(right),
             "slack": str(right - left), "verified": left <= right}
            for name, (left, right) in zip(
                ("bbar*T<=1/2", "Ebar*T<=ell/8", "Dfirst*T<=1/2"), budgets)
        ],
        "all_required_constants_and_three_times_positive": True,
        "ell_scope": "One common lower bound for each of the three target pairs by C3",
        "no_smaller_replacement_window": True,
        "certified": True,
    })


def scientific_stage(report, input_bytes):
    evidence = Evidence(report)
    data = json.loads(input_bytes.decode("utf-8"))
    c, z, m, p, target_matrices = read_stored_coefficients(data, evidence)
    if p == ZERO:
        report["stage_B_outcome"] = "DEGENERATE_CHART_NO_CERTIFICATE"
        return
    if degree(p) == 0:
        report["stage_B_outcome"] = "NO_CANDIDATE_FOR_THIS_CONTRACT"
        report["no_candidate_reason"] = "P is a nonzero constant"
        return
    require(1 <= degree(p) <= 6, "unexpected P degree")
    q, factors = square_free(p, evidence)
    evidence.q = q
    evidence.q_chain = evidence.sturm(q)
    maximum_ratio = max(abs(x / q[-1]) for x in q[:-1])
    ceiling = -(-maximum_ratio.numerator // maximum_ratio.denominator)
    bound = 2 + ceiling
    require(evaluate(q, Fraction(-bound)) != 0 and evaluate(q, Fraction(bound)) != 0,
            "Cauchy enclosure endpoints are roots")
    first = evidence.node(Fraction(-bound), Fraction(bound), 0, None, "global", "root_bound")
    report["global_root_certificate"] = {
        "Cauchy_maximum_coefficient_ratio": str(maximum_ratio),
        "B": bound, "global_node": first["id"], "all_real_roots_count": first["count"],
        "Q_endpoints_nonzero": True, "root_order": "left-first half-open isolation tree",
    }
    evidence.isolate(first)
    require(len(evidence.roots) == first["count"], "isolated root count is incomplete")
    require(all(evidence.roots[j]["initial_node"]["b"]
                <= evidence.roots[j + 1]["initial_node"]["a"]
                for j in range(len(evidence.roots) - 1)), "root intervals are not ordered")
    for root in evidence.roots:
        classify_root(root, factors, c, z, m, p, target_matrices, evidence)
    require(all(x["classification_complete"] for x in report["roots"]),
            "some root classification is missing")
    report["all_distinct_roots_classified_before_selection"] = True
    report["real_root_multiplicity_sum"] = sum(
        x["original_P_root_multiplicity"] for x in report["roots"])
    require(report["real_root_multiplicity_sum"] <= degree(p),
            "real multiplicity exceeds P degree")
    eligible = [root for root in evidence.roots if root["eligible"]]
    if not eligible:
        report["stage_B_outcome"] = "NO_CANDIDATE_FOR_THIS_CONTRACT"
        report["no_candidate_reason"] = (
            "global Sturm count is zero" if not evidence.roots
            else "every real root has a certified zero complete C under the fixed normalization")
        return
    selected = eligible[0]
    report["selected_root_index"] = selected["index"]
    report["selection_rule"] = "first eligible real root; no later replacement if lower bound unresolved"
    certify_window(selected, evidence)
    report["stage_B_outcome"] = "EXACT_DATA_AND_WINDOW_CERTIFIED_PENDING_STAGE_C_AND_MATH_REVIEW"
    report["scope"] = (
        "Exact finite algebra and rational constants for the conditional same-data NS bridge. "
        "Not an independently accepted NS theorem, numerical evolution, repeated supply, or singularity."
    )


def sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def sha256_file(path):
    return sha256_bytes(path.read_bytes())


def valid_hex(value, length):
    return len(value) == length and all(x in "0123456789abcdef" for x in value)


def alarm_handler(signum, frame):
    raise NotCertified("WALL_ALARM_EXPIRED")


def json_bytes(report):
    return (json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--contract-sha", required=True)
    parser.add_argument("--a-input-sha", required=True)
    args = parser.parse_args()
    source_path = Path(__file__).resolve()
    output_path = source_path.with_name("exact-roots-output.json")
    require(not output_path.exists(), "output exists; scientific rerun forbidden")
    require(valid_hex(args.source_commit, 40), "source commit must be lowercase hex")
    require(args.contract_sha == CONTRACT_SHA, "contract argument differs from fixed gate")
    require(args.a_input_sha == A_INPUT_SHA, "A input argument differs from fixed gate")
    paths = {
        "source": source_path, "contract": source_path.with_name("CONTRACT.md"),
        "stage_A_input": source_path.with_name("exact-coefficients-output.json"),
        "method": source_path.with_name("ROOT_METHOD_PREFLIGHT.md"),
        "implementation_gate": source_path.with_name("STAGE_B_IMPLEMENTATION_GATE.md"),
    }
    input_bytes = paths["stage_A_input"].read_bytes()
    hashes = {name: sha256_file(path) for name, path in paths.items()}
    require(sha256_bytes(input_bytes) == hashes["stage_A_input"] == A_INPUT_SHA,
            "frozen A input bytes mismatch")
    require(hashes["contract"] == CONTRACT_SHA and hashes["method"] == METHOD_SHA
            and hashes["implementation_gate"] == GATE_SHA, "method/contract/gate bytes mismatch")
    uname = os.uname()
    scientific_count = 0
    report = {
        "schema": "cyclic-six-carrier-stage-B-exact-roots-v1",
        "execution_status": "not_started", "stage_B_outcome": "NOT_CERTIFIED",
        "scientific_execution_count_in_this_invocation": scientific_count,
        "scientific_stage_completed": False,
        "provenance": {
            "source_commit_parent_supplied": args.source_commit,
            "stage_A_saved_commit_parent_supplied": A_SAVED_COMMIT,
            "commit_not_verified_by_git_in_this_program": True,
            "paths": {name: str(path) for name, path in paths.items()},
            "sha256_before_science": hashes, "command_argv": list(sys.argv),
        },
        "environment": {
            "python_version": sys.version, "python_executable": sys.executable,
            "os_uname": {"sysname": uname.sysname, "nodename": uname.nodename,
                         "release": uname.release, "version": uname.version,
                         "machine": uname.machine},
            "visible_logical_CPUs": os.cpu_count(), "scientific_workers": 1,
            "scientific_threads": 1, "external_processes_started": 0,
            "third_party_scientific_libraries": [],
        },
        "limits": {"wall_seconds": WALL_LIMIT_SECONDS,
                   "target_maximum_RSS_SELF_bytes": SELF_RSS_LIMIT_BYTES,
                   "output_bytes_strictly_below": OUTPUT_LIMIT_BYTES,
                   "cumulative_bisections_per_root": MAX_ROOT_DEPTH},
        "evidence_conventions": {
            "polynomials": "exact Fraction ascending coefficients; zero degree -1; integer IDs",
            "root_intervals": "Sturm counts (a,b], midpoint root owned by left child",
            "closed_enclosures": "interval arithmetic uses [a,b], or exact point [b,b]",
            "gcd_steps": "left=quotient*right+next/positive_multiplier; final gcd monic",
            "Sturm_steps": "next=-positive_multiplier*rem(previous,current); scales explicit",
            "Q": "global square-free polynomial, not asserted irreducible or a number field",
            "zero_tests": "gcd(Q,f) count at specified Q root; exact point cross-check if detected",
            "normalization": "original unscaled M row, with no algebraic inversion",
            "depth": "all isolation ancestors plus selected-root refinement, never reset",
        },
        "not_executed": [
            "new Fourier coefficients or stage-A recomputation", "parameter or frequency search",
            "irreducible factor search or floating-point root approximation",
            "B(W0,W0), next generation, NS time integration, singularity inference",
        ],
    }
    signal.signal(signal.SIGALRM, alarm_handler)
    try:
        remaining = WALL_LIMIT_SECONDS - (time.perf_counter() - MODULE_START)
        if remaining <= 0:
            raise NotCertified("wall budget exhausted before scientific stage")
        signal.setitimer(signal.ITIMER_REAL, remaining)
        report["execution_status"] = "running"
        scientific_count += 1
        report["scientific_execution_count_in_this_invocation"] = scientific_count
        scientific_stage(report, input_bytes)
        report["scientific_stage_completed"] = True
        after_hashes = {name: sha256_file(path) for name, path in paths.items()}
        require(after_hashes == hashes, "source/input/contract/method/gate changed during run")
        report["provenance"]["sha256_after_science"] = after_hashes
        report["execution_status"] = "completed"
    except Exception as error:
        report["execution_status"] = "not_certified"
        report["stage_B_outcome"] = "NOT_CERTIFIED"
        report["failure"] = {
            "type": type(error).__name__, "reason": str(error),
            "category": ("INCONSISTENT_CERTIFICATE" if isinstance(error, InconsistentCertificate)
                         else "NOT_CERTIFIED"),
        }
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    report["resources_before_first_full_serialization"] = resource_snapshot()
    first_serialization = json_bytes(report)
    after_serialization = resource_snapshot()
    report["resources_after_first_full_serialization"] = after_serialization
    problems = budget_problems(after_serialization)
    if len(first_serialization) >= OUTPUT_LIMIT_BYTES:
        problems.append("OUTPUT_LIMIT_EXCEEDED")
    report["resource_scope"] = (
        "This Python process only. Wall starts just after importing time at module entry. "
        "The later boundary includes remaining imports, input reads, scientific work, "
        "identity checks, byte rechecks and first full JSON serialization. Final resource "
        "fields, final serialization and the unique disk write are outside that boundary. "
        "RUSAGE_SELF peak RSS is not a whole-process-tree or full-lifecycle certificate."
    )
    report["resource_checks_at_recorded_boundary"] = problems or ["PASS"]
    if problems:
        report["execution_status"] = "not_certified"
        report["stage_B_outcome"] = "NOT_CERTIFIED"
    final_serialization = json_bytes(report)
    if len(final_serialization) >= OUTPUT_LIMIT_BYTES:
        report = {
            "schema": report["schema"], "execution_status": "not_certified",
            "stage_B_outcome": "NOT_CERTIFIED",
            "scientific_execution_count_in_this_invocation": report[
                "scientific_execution_count_in_this_invocation"],
            "scientific_stage_completed": report["scientific_stage_completed"],
            "failure": {"reason": "FINAL_OUTPUT_LIMIT_EXCEEDED",
                        "attempted_output_bytes": len(final_serialization)},
            "provenance": report["provenance"], "environment": report["environment"],
            "resources_after_first_full_serialization": after_serialization,
            "resource_scope": report["resource_scope"],
            "complete_root_or_window_certificate_in_this_artifact": False,
        }
        final_serialization = json_bytes(report)
    require(len(final_serialization) < OUTPUT_LIMIT_BYTES, "bounded failure output too large")
    with output_path.open("xb") as output_file:
        output_file.write(final_serialization)
    print(json.dumps({
        "execution_status": report["execution_status"], "stage_B_outcome": report["stage_B_outcome"],
        "output_path": str(output_path), "output_sha256": sha256_bytes(final_serialization),
        "output_bytes": len(final_serialization),
        "scientific_execution_count_in_this_invocation": report[
            "scientific_execution_count_in_this_invocation"],
        "scientific_stage_completed": report["scientific_stage_completed"],
        "resources_after_first_full_serialization": after_serialization,
    }, ensure_ascii=False))
    return 0 if report["execution_status"] == "completed" else 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        # A pre-science binding/overwrite error or disk-write failure never
        # authorizes a retry or a changed scientific input.
        print(json.dumps({"execution_status": "failed", "type": type(error).__name__,
                          "reason": str(error)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(2)
