#!/usr/bin/env python3
"""Stage C: prepared final source, not executed before a separate parent gate.

Nonauthor different organization after reading the stage A source: explicit
five ordered shapes, 24 label permutations, sparse rational polynomials and
double-cross Leray.  This core was formed before reading the stopped A output.
The A adapter was then prepared after a documented scoped read of that output.
The B source and stopped certificate were read later for evidence adaptation.
This is a nonauthor verification with another tree organization, not blind.
No import, compile, probe or execution is authorized by source preparation.
"""

import time

MODULE_START = time.perf_counter()

import argparse
from fractions import Fraction as Rational
import hashlib
from itertools import permutations
import json
import os
from pathlib import Path
import resource
import signal
import sys


BASE_BINDINGS = {
    "CONTRACT.md": "a441be9b7adf0ee900eeaa786119e7c6f8fecb4c3a01bc4678f1c23fddad1a9b",
    "exact_coefficients.py": "7ce63da05ad2d2e51acfdc7cd51f6630191734574f62af000f3edba7221d9a64",
    "APPLICATION_PROOF.md": "096f626a754654039922eae0b13354e27e870ef113ee0967ffaebd29713955d4",
}
# Exact stopped bytes, with the actual human reading scope recorded in DESIGN.
STAGE_A_OUTPUT_BINDING = "9329464c09faa50558bc090b3af8c3ec6f074619e01a9fe2d5eb6d0f1c079ae6"
STAGE_B_SOURCE_BINDING = "4206577cf1464207899b7fa47741c2cff7ffac843221fb140d7f172a4b75de80"
STAGE_B_OUTPUT_BINDING = "6fd933ebd18bdf8b129f7cabdbf1f02438de3fd95f9720b18e41887815f31bcb"
METHOD_BINDING = "2fb88e7166ee62fa1b3df24415542970580bb3d520971386b482f5a5db80453a"
GATE_BINDING = "af692a572eee828b7415e29fb784197c10329e3c98cdf0a5a765ec6b884fe39f"
# Code completeness is not execution authorization; main needs an explicit flag.
EXECUTION_READY = True

LEAF = "*"
PAIR = (LEAF, LEAF)
ORDERED_FOUR_LEAF_SHAPES = (
    (((LEAF, LEAF), LEAF), LEAF),
    ((LEAF, (LEAF, LEAF)), LEAF),
    ((LEAF, LEAF), (LEAF, LEAF)),
    (LEAF, ((LEAF, LEAF), LEAF)),
    (LEAF, (LEAF, (LEAF, LEAF))),
)
FIXED_FREQUENCIES = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 3, 5))
WALL_LIMIT_SECONDS = 60
SELF_RSS_LIMIT_BYTES = 256 * 1024 * 1024
OUTPUT_LIMIT_BYTES = 1024 * 1024
ROOT_REFINEMENT_LIMIT = 128


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def budget_guard():
    require(time.perf_counter() - MODULE_START <= WALL_LIMIT_SECONDS, "WALL_BUDGET_EXCEEDED")
    require(resource_snapshot()["maximum_RSS_SELF_bytes"] <= SELF_RSS_LIMIT_BYTES,
            "SELF_RSS_TARGET_EXCEEDED")


def polynomial(terms):
    """Sparse exponent -> Rational; no polynomial is evaluated at an alpha."""
    result = {}
    for exponent, coefficient in terms:
        require(isinstance(exponent, int) and exponent >= 0, "bad exponent")
        result[exponent] = result.get(exponent, Rational(0)) + Rational(coefficient)
    return {exponent: coefficient for exponent, coefficient in result.items()
            if coefficient != 0}


def constant(value):
    return polynomial(((0, value),))


def p_add(left, right):
    return polynomial(tuple(left.items()) + tuple(right.items()))


def p_scale(value, scalar):
    scalar = Rational(scalar)
    return polynomial((exponent, scalar * coefficient)
                      for exponent, coefficient in value.items())


def p_multiply(left, right):
    return polynomial((i + j, x * y)
                      for i, x in left.items() for j, y in right.items())


def p_degree(value):
    return max(value, default=-1)


def zero_vector():
    return ({}, {}, {})


def v_add(left, right):
    require(len(left) == len(right) == 3, "bad vector length")
    return tuple(p_add(x, y) for x, y in zip(left, right))


def v_scale(value, scalar):
    return tuple(p_scale(x, scalar) for x in value)


def v_sum(values):
    total = zero_vector()
    for value in values:
        total = v_add(total, value)
    return total


def rotate(value, power):
    for unused in range(power % 3):
        value = (value[2], value[0], value[1])
    return value


def frequency_dot(frequency, value):
    total = {}
    for integer, coefficient in zip(frequency, value):
        total = p_add(total, p_scale(coefficient, integer))
    return total


def frequency_cross(frequency, value):
    k1, k2, k3 = frequency
    x1, x2, x3 = value
    return (p_add(p_scale(x3, k2), p_scale(x2, -k3)),
            p_add(p_scale(x1, k3), p_scale(x3, -k1)),
            p_add(p_scale(x2, k1), p_scale(x1, -k2)))


def vertex(left_frequency, right_frequency, left, right, counts):
    """Full ordered Q = P_k ((left dot right_frequency) right), B=-iQ."""
    counts["explicit_vertex_calls"] += 1
    if counts["explicit_vertex_calls"] % 24 == 0:
        budget_guard()
    require(not frequency_dot(left_frequency, left), "left is not transverse")
    require(not frequency_dot(right_frequency, right), "right is not transverse")
    output = tuple(x + y for x, y in zip(left_frequency, right_frequency))
    derivative = frequency_dot(right_frequency, left)
    if output == (0, 0, 0):
        require(not derivative, "zero frequency ordered gate did not vanish")
        counts["zero_output_vertex_calls"] += 1
        return output, zero_vector()
    raw = tuple(p_multiply(derivative, x) for x in right)
    # Independent projection formula: -k cross (k cross raw) / |k|^2.
    projected = v_scale(frequency_cross(output, frequency_cross(output, raw)),
                        -Rational(1, sum(x * x for x in output)))
    require(not frequency_dot(output, projected), "projected gate is not transverse")
    return output, projected


def name_shape(shape):
    return LEAF if shape == LEAF else "(" + name_shape(shape[0]) + "," + name_shape(shape[1]) + ")"


def evaluate_shape(shape, label_order, frequencies, amplitudes, counts):
    """Symbolic multilinear tree evaluation, not an alpha-parameter evaluation."""
    if shape == LEAF:
        label = next(label_order)
        return frequencies[label], amplitudes[label], 1
    left_k, left, left_size = evaluate_shape(
        shape[0], label_order, frequencies, amplitudes, counts)
    right_k, right, right_size = evaluate_shape(
        shape[1], label_order, frequencies, amplitudes, counts)
    output, value = vertex(left_k, right_k, left, right, counts)
    size = left_size + right_size
    return output, v_scale(value, Rational(1, size - 1)), size


def fixed_inputs(rotation, sign, high_column):
    require(rotation in (0, 1, 2) and sign in (1, -1), "bad fixed target")
    alpha = polynomial(((1, 1),))
    low_first = ({}, constant(1), alpha)
    if high_column == "v":
        high = (constant(3), constant(-2), {})
    elif high_column == "w":
        high = (constant(5), {}, constant(-2))
    else:
        raise ArithmeticError("unknown formal high column")
    base = (low_first, rotate(low_first, 1), rotate(low_first, 2), high)
    frequencies = tuple(tuple(sign * x for x in rotate(k, rotation))
                        for k in FIXED_FREQUENCIES)
    amplitudes = tuple(rotate(value, rotation) for value in base)
    require(all(not frequency_dot(k, value)
                for k, value in zip(frequencies, amplitudes)), "fixed leaf not transverse")
    return frequencies, amplitudes


def encode_poly(value):
    return {"sparse_rational_coefficients": {
        str(exponent): str(coefficient) for exponent, coefficient in sorted(value.items())},
        "degree": p_degree(value)}


def encode_vector(value):
    return [encode_poly(x) for x in value]


def compute_coefficient_core():
    """Prepared computation; no call has been made while forming this file."""
    columns = {}
    records = []
    counts = {"explicit_vertex_calls": 0, "zero_output_vertex_calls": 0,
              "four_leaf_root_terms": 0}
    for rotation in range(3):
        for sign in (1, -1):
            target = tuple(sign * x for x in rotate((3, 4, 6), rotation))
            target_columns = {}
            for high_column in ("v", "w"):
                frequencies, amplitudes = fixed_inputs(rotation, sign, high_column)
                shapes = {}
                for shape in ORDERED_FOUR_LEAF_SHAPES:
                    total = zero_vector()
                    for order in permutations(range(4)):
                        output, value, size = evaluate_shape(
                            shape, iter(order), frequencies, amplitudes, counts)
                        require(output == target and size == 4, "wrong full tree target")
                        require(all(p_degree(x) <= 3 for x in value), "degree exceeds three")
                        total = v_add(total, value)
                        counts["four_leaf_root_terms"] += 1
                    shapes[name_shape(shape)] = total
                c = shapes[name_shape(ORDERED_FOUR_LEAF_SHAPES[2])]
                m13 = v_sum(shapes[name_shape(ORDERED_FOUR_LEAF_SHAPES[j])] for j in (3, 4))
                m31 = v_sum(shapes[name_shape(ORDERED_FOUR_LEAF_SHAPES[j])] for j in (0, 1))
                z = v_add(m13, m31)
                full = v_sum(shapes.values())
                require(full == v_add(c, z), "full root split failed")
                root = {"C": c, "M13": m13, "M31": m31, "Z": z,
                        "full_four_leaf": full}
                for value in root.values():
                    require(not frequency_dot(target, value), "root is not transverse")
                    require(all(p_degree(x) <= 3 for x in value), "root degree exceeds three")
                target_columns[high_column] = {"root": root, "shapes": shapes}
            columns[(rotation, sign)] = target_columns
            records.append({
                "rotation": rotation, "sign": sign, "target": list(target),
                "columns": {column: {
                    "all_five_shapes": {shape: encode_vector(value)
                                        for shape, value in item["shapes"].items()},
                    "root_vectors": {name: encode_vector(value)
                                     for name, value in item["root"].items()}}
                    for column, item in target_columns.items()}})
    require(counts["four_leaf_root_terms"] == 1440, "wrong fixed tree-term count")
    require(counts["explicit_vertex_calls"] == 4320, "wrong explicit vertex count")
    for (rotation, sign), target_columns in columns.items():
        for high_column, item in target_columns.items():
            reference = columns[(0, 1)][high_column]
            for collection in ("root", "shapes"):
                require(item[collection].keys() == reference[collection].keys(), "unequal covariance domain")
                for name, value in item[collection].items():
                    require(value == v_scale(rotate(reference[collection][name], rotation), sign),
                            "six-target rotation or real-conjugacy failure")
    primary = columns[(0, 1)]
    zv, zw = primary["v"]["root"]["Z"], primary["w"]["root"]["Z"]
    determinant = p_add(p_multiply(zv[0], zw[1]), p_scale(p_multiply(zv[1], zw[0]), -1))
    require(p_degree(determinant) <= 6, "mixed determinant degree exceeds contract")
    # This field has no asserted actual degree or guessed coefficient.
    report = {"coefficient_records": records, "counts": counts,
              "independent_determinant": encode_poly(determinant),
              "physical_four_leaf_phase": "i times stripped real polynomial vector",
              "scope": "Six specified targets and two formal columns, not the full NS spectrum"}
    return report, columns, determinant


def distinct_json_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON object key")
        result[key] = value
    return result


def read_bound_A_output(path):
    """Prepared byte-bound read; it has not been called during preparation."""
    path = Path(path)
    require(path.name == "exact-coefficients-output.json", "wrong A output name")
    raw = path.read_bytes()
    require(len(raw) < OUTPUT_LIMIT_BYTES, "A input exceeds its frozen output limit")
    require(hashlib.sha256(raw).hexdigest() == STAGE_A_OUTPUT_BINDING,
            "stopped A output byte binding failed")
    for name, expected_sha in BASE_BINDINGS.items():
        require(hashlib.sha256(path.with_name(name).read_bytes()).hexdigest() == expected_sha,
                "base source byte binding failed: " + name)
    document = json.loads(raw.decode("utf-8"), object_pairs_hook=distinct_json_object)
    require(isinstance(document, dict), "A output is not an object")
    return document


def decode_A_polynomial(item, maximum_degree=6):
    require(isinstance(item, dict) and set(item) == {"coefficients_low_to_high", "degree"},
            "unexpected A polynomial encoding")
    coefficients = item["coefficients_low_to_high"]
    require(isinstance(coefficients, list) and 1 <= len(coefficients) <= maximum_degree + 1,
            "bad A polynomial coefficient count")
    decoded = []
    for coefficient in coefficients:
        require(isinstance(coefficient, str), "A rational coefficient is not a string")
        value = Rational(coefficient)
        require(str(value) == coefficient, "noncanonical A rational coefficient")
        decoded.append(value)
    value = polynomial(enumerate(decoded))
    require(type(item["degree"]) is int and item["degree"] == p_degree(value),
            "A polynomial degree field is inconsistent")
    require((not value and coefficients == ["0"]) or
            (bool(value) and decoded[-1] != 0), "A polynomial trailing-zero convention failed")
    return value


def decode_A_vector(item, maximum_degree=3):
    require(isinstance(item, list) and len(item) == 3, "A vector is not full three-component")
    return tuple(decode_A_polynomial(x, maximum_degree) for x in item)


def decode_A_frequency(item):
    require(isinstance(item, list) and len(item) == 3 and
            all(type(x) is int for x in item), "A frequency is not an integer triple")
    return tuple(item)


def compare_stopped_A_output(report, columns, determinant, stage_a_path):
    """Full root coefficient comparison; no intermediate subset recomputation."""
    source = read_bound_A_output(stage_a_path)
    require(source["schema"] == "cyclic-six-carrier-stage-A-exact-coefficients-v1",
            "unexpected stopped A schema")
    require(source["execution_status"] == "completed" and
            source["scientific_stage_completed"] is True and
            type(source["scientific_execution_count_in_this_invocation"]) is int and
            source["scientific_execution_count_in_this_invocation"] == 1,
            "stopped A did not report one completed scientific stage")
    require(source["resource_checks_at_recorded_boundary"] == ["PASS"],
            "stopped A resource status is not PASS at its recorded boundary")
    provenance = source["provenance"]
    require(provenance["source_sha256"] == BASE_BINDINGS["exact_coefficients.py"] and
            provenance["contract_sha256"] == BASE_BINDINGS["CONTRACT.md"],
            "A reported provenance disagrees with stopped source bytes")
    records = source["target_records"]
    require(isinstance(records, list) and len(records) == 6, "A does not contain six targets")
    by_target = {}
    for record in records:
        rotation, sign = record["rotation_index"], record["sign"]
        require(type(rotation) is int and type(sign) is int and
                rotation in (0, 1, 2) and sign in (1, -1), "A target index is outside the contract")
        key = (rotation, sign)
        require(key not in by_target, "duplicate A target")
        by_target[key] = record
    require(set(by_target) == set(columns), "A and independently computed target domains differ")

    comparison_counts = {"targets": 0, "formal_columns": 0, "input_vectors": 0,
                         "root_vectors": 0, "four_leaf_shape_vectors": 0,
                         "mask15_total_vectors": 0, "primary_matrix_polynomials": 0,
                         "determinant_polynomials": 0}
    for (rotation, sign), independent_columns in columns.items():
        record = by_target[(rotation, sign)]
        expected_target = tuple(sign * x for x in rotate((3, 4, 6), rotation))
        require(decode_A_frequency(record["target"]) == expected_target, "A target frequency mismatch")
        require(isinstance(record["columns"], dict) and set(record["columns"]) == {"v", "w"},
                "A formal column domain is not exactly v,w")
        comparison_counts["targets"] += 1
        for column, independent in independent_columns.items():
            actual = record["columns"][column]
            frequencies, amplitudes = fixed_inputs(rotation, sign, column)
            inputs = actual["input_labels"]
            require(isinstance(inputs, list) and len(inputs) == 4, "A input label count is not four")
            for label, item in enumerate(inputs):
                require(type(item["label"]) is int and item["label"] == label, "A input label order differs")
                require(decode_A_frequency(item["frequency"]) == frequencies[label],
                        "A input frequency differs from fixed data")
                require(decode_A_vector(item["amplitude"], 1) == amplitudes[label],
                        "A input amplitude differs from fixed formal data")
                comparison_counts["input_vectors"] += 1
            subsets = actual["all_nonempty_label_subsets"]
            require(isinstance(subsets, list) and len(subsets) == 15, "A subset record count is not fifteen")
            by_mask = {}
            for subset in subsets:
                mask = subset["mask"]
                require(type(mask) is int and mask in range(1, 16) and mask not in by_mask,
                        "A subset mask domain has an invalid or repeated mask")
                by_mask[mask] = subset
            require(set(by_mask) == set(range(1, 16)), "A subset mask coverage failed")
            root_subset = by_mask[15]
            require(root_subset["labels"] == [0, 1, 2, 3] and
                    decode_A_frequency(root_subset["frequency"]) == expected_target,
                    "A mask15 metadata differs from the four fixed labels")
            root_vectors = actual["root_vectors"]
            require(isinstance(root_vectors, dict) and set(root_vectors) == set(independent["root"]),
                    "A full root vector domain differs")
            for name, expected in independent["root"].items():
                require(decode_A_vector(root_vectors[name]) == expected,
                        "A full root coefficient mismatch: " + str((rotation, sign, column, name)))
                comparison_counts["root_vectors"] += 1
            actual_shapes = root_subset["ordered_tree_shapes"]
            expected_shapes = {name.replace(LEAF, "x"): value
                               for name, value in independent["shapes"].items()}
            require(isinstance(actual_shapes, dict) and set(actual_shapes) == set(expected_shapes),
                    "A mask15 does not contain exactly the five expected ordered shapes")
            for shape, expected in expected_shapes.items():
                require(decode_A_vector(actual_shapes[shape]) == expected,
                        "A ordered root shape coefficient mismatch: " + str((rotation, sign, column, shape)))
                comparison_counts["four_leaf_shape_vectors"] += 1
            require(decode_A_vector(root_subset["total"]) == independent["root"]["full_four_leaf"],
                    "A mask15 total coefficient mismatch")
            comparison_counts["mask15_total_vectors"] += 1
            comparison_counts["formal_columns"] += 1

    matrices = source["primary_matrices"]
    require(decode_A_frequency(matrices["target"]) == (3, 4, 6), "A primary matrix target mismatch")
    for field, root_name, row_count in (
            ("C_full_three_rows_v_w_columns", "C", 3),
            ("Z_full_three_rows_v_w_columns", "Z", 3),
            ("M_first_two_Z_rows", "Z", 2)):
        matrix = matrices[field]
        require(isinstance(matrix, list) and len(matrix) == row_count, "A primary matrix row count failed")
        for row_index, row in enumerate(matrix):
            require(isinstance(row, list) and len(row) == 2, "A primary matrix column count failed")
            for column_index, column in enumerate(("v", "w")):
                require(decode_A_polynomial(row[column_index], 3) ==
                        columns[(0, 1)][column]["root"][root_name][row_index],
                        "A primary matrix coefficient mismatch: " + str((field, row_index, column)))
                comparison_counts["primary_matrix_polynomials"] += 1
    require(decode_A_polynomial(matrices["P_determinant"]) == determinant,
            "A determinant differs from independently formed Z minor")
    comparison_counts["determinant_polynomials"] += 1
    if not determinant:
        expected_outcome = "DEGENERATE_CHART_NO_CERTIFICATE"
    elif p_degree(determinant) == 0:
        expected_outcome = "NO_CANDIDATE_FOR_THIS_CONTRACT_NONZERO_CONSTANT_DETERMINANT"
    else:
        expected_outcome = "COEFFICIENTS_CERTIFIED_ROOT_STAGE_PENDING"
    require(source["stage_A_outcome"] == expected_outcome, "A determinant branch label mismatch")
    require(comparison_counts == {
        "targets": 6, "formal_columns": 12, "input_vectors": 48,
        "root_vectors": 60, "four_leaf_shape_vectors": 60,
        "mask15_total_vectors": 12, "primary_matrix_polynomials": 16,
        "determinant_polynomials": 1}, "incomplete A comparison count")
    report["stage_A_comparison"] = {
        "status": "PASS", "output_sha256": STAGE_A_OUTPUT_BINDING,
        "counts": comparison_counts, "independent_determinant_degree": p_degree(determinant),
        "source_commit_reported_by_A_not_verified_with_git": provenance["source_commit_parent_supplied"],
        "compared": "All six targets, both formal columns, all three components of C/M13/M31/Z/total, all mask15 five shapes, primary matrices and P; all four fixed inputs per column",
        "not_recomputed": "The coefficients in masks1..14, A's aggregated vertex counts, full twelve-mode convolution, or an NS spectrum",
        "resource_scope": "A's immutable resource fields refer to its SELF/first-serialization boundary; these are not stage C measurements",
    }
    return source


def rational_text(value):
    require(isinstance(value, str), "exact rational field is not a string")
    result = Rational(value)
    require(str(result) == value, "noncanonical exact rational field")
    return result


def p_derivative(value):
    return polynomial((exponent - 1, exponent * coefficient)
                      for exponent, coefficient in value.items() if exponent)


def p_evaluate(value, point):
    result = Rational(0)
    for exponent in range(p_degree(value), -1, -1):
        result = result * point + value.get(exponent, Rational(0))
    return result


def interval_pair(value):
    require(isinstance(value, list) and len(value) == 2, "bad rational interval")
    result = tuple(rational_text(x) for x in value)
    require(result[0] <= result[1], "reversed closed interval")
    return result


def p_enclosure(value, interval):
    """Closed rational Horner enclosure, also valid for an exact point."""
    low = high = Rational(0)
    for exponent in range(p_degree(value), -1, -1):
        products = (low * interval[0], low * interval[1],
                    high * interval[0], high * interval[1])
        coefficient = value.get(exponent, Rational(0))
        low, high = min(products) + coefficient, max(products) + coefficient
    return low, high


def apply_formal_columns(columns, field, v, w):
    return tuple(p_add(p_multiply(x, v), p_multiply(y, w))
                 for x, y in zip(columns["v"]["root"][field],
                                 columns["w"]["root"][field]))


class RootEvidenceVerifier:
    """Validate saved evidence identities; never generate a new isolation tree."""

    def __init__(self, document):
        self.document = document
        self.polynomials = []
        self.polynomial_references = set()
        seen = set()
        for index, item in enumerate(document["polynomials"]):
            require(type(item["id"]) is int and item["id"] == index, "bad polynomial ID order")
            value = decode_A_polynomial({key: item[key] for key in
                                         ("coefficients_low_to_high", "degree")})
            canonical = tuple(sorted(value.items()))
            require(canonical not in seen, "B polynomial deduplication failed")
            seen.add(canonical)
            self.polynomials.append(value)
        require(len(self.polynomials) == 160, "frozen B polynomial table coverage changed")
        self.gcds = self.records("gcd_certificates", 21)
        self.sturms = self.records("sturm_chains", 2)
        self.nodes = self.records("isolation_nodes", 15)
        self.zero_tests = self.records("zero_tests", 38)
        self.roots = self.records("roots", 2, "index")
        self.gcd_results = {}
        self.chains = {}
        self.zero_results = {}
        self.used_zero_tests = set()
        self.q = None
        self.normalized = []
        self.count_checks = 0

    def records(self, name, expected_count, key="id"):
        values = self.document[name]
        require(isinstance(values, list) and len(values) == expected_count,
                "frozen B record count changed: " + name)
        for index, item in enumerate(values):
            require(type(item[key]) is int and item[key] == index, "invalid record ID: " + name)
        return values

    def P(self, identifier):
        require(type(identifier) is int and 0 <= identifier < len(self.polynomials),
                "invalid polynomial reference")
        self.polynomial_references.add(identifier)
        return self.polynomials[identifier]

    def vector(self, identifiers, length):
        require(isinstance(identifiers, list) and len(identifiers) == length, "bad vector ID length")
        return tuple(self.P(identifier) for identifier in identifiers)

    def matrix(self, identifiers, rows):
        require(isinstance(identifiers, list) and len(identifiers) == rows, "bad matrix ID rows")
        return tuple(self.vector(row, 2) for row in identifiers)

    def validate_all_gcds(self):
        for record in self.gcds:
            budget_guard()
            inputs = self.vector(record["inputs"], 2)
            require(any(inputs), "gcd(0,0) is outside the saved certificate")
            initial = self.vector(record["initial_polynomials"], 2)
            multipliers = tuple(rational_text(x) for x in record["initial_positive_multipliers"])
            require(len(multipliers) == 2 and all(x > 0 for x in multipliers), "bad initial gcd scales")
            require(initial == tuple(p_scale(p, c) for p, c in zip(inputs, multipliers)),
                    "gcd initial positive scaling identity failed")
            left, right = initial
            for step in record["steps"]:
                require(right and self.P(step["left"]) == left and self.P(step["right"]) == right,
                        "noncontiguous Euclidean certificate")
                quotient, nxt = self.P(step["quotient"]), self.P(step["next"])
                factor = rational_text(step["positive_multiplier"])
                require(factor > 0, "nonpositive Euclidean remainder scale")
                require(left == p_add(p_multiply(quotient, right), p_scale(nxt, 1 / factor)),
                        "Euclidean division identity failed")
                require(not nxt or p_degree(nxt) < p_degree(right), "Euclidean remainder degree failed")
                left, right = right, nxt
            require(left and not right, "Euclidean chain did not terminate at a nonzero gcd")
            scale = rational_text(record["final_monic_multiplier_not_a_Sturm_scaling"])
            require(scale == 1 / left[p_degree(left)], "incorrect final monic gcd multiplier")
            result = self.P(record["result"])
            require(result == p_scale(left, scale) and result[p_degree(result)] == 1,
                    "final gcd identity or monicity failed")
            quotients = self.vector(record["input_quotients_by_result"], 2)
            require(all(p_multiply(q, result) == a for q, a in zip(quotients, inputs)),
                    "gcd input quotient identity failed")
            require(record["verified"] is True, "B gcd label disagrees after identity verification")
            self.gcd_results[record["id"]] = (inputs, result)

    def gcd_result(self, identifier, left, right):
        require(type(identifier) is int and identifier in self.gcd_results, "unknown gcd certificate")
        inputs, result = self.gcd_results[identifier]
        require(inputs == (left, right), "gcd certificate belongs to other polynomials")
        return result

    def validate_all_sturms(self):
        for record in self.sturms:
            budget_guard()
            q = self.P(record["input"])
            chain = tuple(self.P(identifier) for identifier in record["polynomials"])
            require(q and chain and chain[0] == q and rational_text(record["S0_multiplier"]) == 1,
                    "bad Sturm initial polynomial")
            if p_degree(q) == 0:
                require(len(chain) == 1 and record["negative_remainder_steps"] == [] and
                        record["constant_root_count"] == 0, "bad constant Sturm chain")
            else:
                require(len(chain) >= 2, "missing Sturm derivative")
                scale = rational_text(record["S1_positive_multiplier_of_derivative"])
                require(scale > 0 and chain[1] == p_scale(p_derivative(q), scale),
                        "Sturm derivative positive scaling failed")
                steps = record["negative_remainder_steps"]
                require(len(steps) == len(chain) - 2, "Sturm step count differs from chain")
                for index, step in enumerate(steps):
                    quotient = self.P(step["quotient"])
                    factor = rational_text(step["positive_multiplier"])
                    nxt = self.P(step["next"])
                    require(factor > 0 and nxt == chain[index + 2] and nxt,
                            "bad signed Sturm step")
                    require(chain[index] == p_add(p_multiply(quotient, chain[index + 1]),
                                                  p_scale(nxt, -1 / factor)),
                            "Sturm negative-remainder identity failed")
                    require(p_degree(nxt) < p_degree(chain[index + 1]), "Sturm degree did not decrease")
                require(p_degree(chain[-1]) == 0 and not self.P(record["terminal_remainder"]),
                        "Sturm chain did not end at a nonzero constant")
                require(chain[-2] == p_multiply(self.P(record["terminal_quotient"]), chain[-1]),
                        "terminal Sturm division failed")
            require(record["verified"] is True, "Sturm label disagrees after exact identities")
            self.chains[record["id"]] = (q, chain)

    @staticmethod
    def variation(chain, endpoint):
        signs = []
        for value in chain:
            result = p_evaluate(value, endpoint)
            if result:
                signs.append(result > 0)
        return sum(signs[j] != signs[j - 1] for j in range(1, len(signs)))

    def count(self, record, polynomial, interval):
        chain_id = record["sturm_chain"]
        require(type(chain_id) is int and chain_id in self.chains, "unknown Sturm count chain")
        q, chain = self.chains[chain_id]
        require(q == polynomial and interval_pair(record["interval"]) == interval and
                interval[0] < interval[1] and record["ownership"] == "(a,b]",
                "Sturm count polynomial, interval or endpoint ownership mismatch")
        left, right = (self.variation(chain, endpoint) for endpoint in interval)
        value = left - right
        for field, expected in (("V_a", left), ("V_b", right), ("count", value)):
            require(type(record[field]) is int and record[field] == expected, "incorrect Sturm count field")
        require(0 <= value <= p_degree(q), "Sturm count outside degree bound")
        self.count_checks += 1
        return value

    def square_free(self, determinant):
        require(1 <= p_degree(determinant) <= 6, "frozen B success requires nonconstant P")
        record = self.document["square_free_decomposition"]
        leading = determinant[p_degree(determinant)]
        require(rational_text(record["original_leading_coefficient"]) == leading, "original P scale changed")
        monic = p_scale(determinant, 1 / leading)
        require(self.P(record["monic_F"]) == monic, "monic F does not come from original P")
        g = self.gcd_result(record["initial_derivative_gcd"], monic, p_derivative(monic))
        q = self.P(record["Q"])
        require(p_multiply(q, g) == monic, "Q times initial gcd is not F")
        w = q
        factors = []
        for index, step in enumerate(record["steps"], 1):
            require(w != constant(1) and index <= p_degree(determinant), "extra Yun step")
            require(step["multiplicity"] == index and self.P(step["w"]) == w and self.P(step["g"]) == g,
                    "Yun state or multiplicity mismatch")
            y = self.gcd_result(step["gcd_certificate"], w, g)
            factor, next_g = self.P(step["factor"]), self.P(step["next_g"])
            require(self.P(step["y"]) == y and p_multiply(factor, y) == w and
                    p_multiply(next_g, y) == g, "Yun exact quotient identity failed")
            if factor != constant(1):
                require(p_degree(factor) > 0, "unexpected constant Yun factor")
                factors.append((index, factor))
            w, g = y, next_g
        require(w == g == constant(1), "Yun residual is not one")
        saved_factors = [(item["multiplicity"], self.P(item["polynomial"])) for item in record["factors"]]
        require(saved_factors == factors, "Yun factor list or multiplicities differ")
        reconstruction = product = constant(1)
        square_free_ids = record["square_free_gcd_certificates"]
        pair_ids = iter(record["pairwise_coprime_gcd_certificates"])
        require(len(square_free_ids) == len(factors), "missing square-free factor gcd")
        pair_count = 0
        for index, (multiplicity, factor) in enumerate(factors):
            for unused in range(multiplicity):
                reconstruction = p_multiply(reconstruction, factor)
            product = p_multiply(product, factor)
            require(self.gcd_result(square_free_ids[index], factor, p_derivative(factor)) == constant(1),
                    "factor is not certified square-free")
            for unused, earlier in factors[:index]:
                require(self.gcd_result(next(pair_ids), earlier, factor) == constant(1), "factors not coprime")
                pair_count += 1
        require(pair_count == len(record["pairwise_coprime_gcd_certificates"]), "extra pairwise gcd record")
        require(reconstruction == monic == self.P(record["reconstruction"]) and product == q,
                "square-free reconstruction failed")
        require(self.gcd_result(record["Q_square_free_gcd_certificate"], q, p_derivative(q)) == constant(1),
                "global Q is not square-free")
        require(record["irreducibility_claimed"] is False and record["verified"] is True,
                "square-free scope or result label differs")
        self.q = q
        return factors

    def descendant(self, child, ancestor):
        require(type(child) is int and type(ancestor) is int and
                0 <= child < len(self.nodes) and 0 <= ancestor < len(self.nodes), "bad node reference")
        while child != ancestor:
            child = self.nodes[child]["parent"]
            if child is None:
                return False
        return True

    def validate_nodes(self):
        global_record = self.document["global_root_certificate"]
        maximum = max(abs(self.q.get(j, Rational(0)) / self.q[p_degree(self.q)])
                      for j in range(p_degree(self.q)))
        bound = 2 + (-(-maximum.numerator // maximum.denominator))
        require(rational_text(global_record["Cauchy_maximum_coefficient_ratio"]) == maximum and
                type(global_record["B"]) is int and global_record["B"] == bound,
                "Cauchy bound formula changed")
        require(p_evaluate(self.q, -bound) and p_evaluate(self.q, bound) and
                global_record["Q_endpoints_nonzero"] is True, "Cauchy endpoints are not excluded")
        require(global_record["global_node"] == 0, "global root node is not first")
        for index, node in enumerate(self.nodes):
            budget_guard()
            interval = interval_pair(node["interval"])
            count = self.count(node, self.q, interval)
            require(type(node["depth"]) is int and 0 <= node["depth"] <= ROOT_REFINEMENT_LIMIT,
                    "root depth budget is not certified")
            require(node["right_endpoint_is_Q_root"] is (p_evaluate(self.q, interval[1]) == 0),
                    "right endpoint root flag failed")
            if index == 0:
                require(interval == (-bound, bound) and node["parent"] is None and node["depth"] == 0 and
                        node["side"] == "global" and node["purpose"] == "root_bound", "bad global node")
            else:
                parent = node["parent"]
                require(type(parent) is int and 0 <= parent < index and
                        index in self.nodes[parent].get("children", []), "orphan or cyclic isolation node")
                require(node["depth"] == self.nodes[parent]["depth"] + 1, "root depth was reset")
            if "children" in node:
                children = node["children"]
                require(isinstance(children, list) and len(children) == 2 and children[0] != children[1] and
                        all(type(j) is int and index < j < len(self.nodes) for j in children), "bad split children")
                left, right = (self.nodes[j] for j in children)
                midpoint = (interval[0] + interval[1]) / 2
                require(interval_pair(left["interval"]) == (interval[0], midpoint) and
                        interval_pair(right["interval"]) == (midpoint, interval[1]) and
                        left["parent"] == right["parent"] == index and
                        left["side"] == "left" and right["side"] == "right" and
                        left["count"] + right["count"] == count, "half-open split identity failed")
            if node["purpose"] in ("root_bound", "global_all_root_isolation"):
                expected_status = "empty" if count == 0 else "one_root" if count == 1 else "split_multiple_roots"
                require(node["status"] == expected_status, "global isolation status disagrees")
            else:
                require(node["purpose"] == "selected_root_C_lower_bound" and count in (0, 1),
                        "unrecognized or multiple-root window refinement")
        ordered = []
        global_node_ids = set()

        def visit(identifier):
            require(identifier not in global_node_ids, "global isolation node visited twice")
            global_node_ids.add(identifier)
            node = self.nodes[identifier]
            if node["count"] == 0:
                require("children" not in node, "empty node was split")
            elif node["count"] == 1:
                ordered.append(identifier)
            else:
                require("children" in node, "unresolved multiple-root node")
                for child in node["children"]:
                    require(self.nodes[child]["purpose"] == "global_all_root_isolation", "global isolation truncated")
                    visit(child)

        visit(0)
        require(global_node_ids == {node["id"] for node in self.nodes
                                    if node["purpose"] in ("root_bound", "global_all_root_isolation")},
                "unused global isolation subtree")
        require(len(ordered) == self.nodes[0]["count"] == global_record["all_real_roots_count"] == len(self.roots),
                "global real-root completeness failed")
        require(ordered == [root["initial_node"] for root in self.roots], "root order is not left-first tree order")
        for index, root in enumerate(self.roots):
            first, current = root["initial_node"], root["current_node"]
            require(self.descendant(current, first) and self.nodes[current]["count"] == 1,
                    "current root node is not the same isolated root")
            require(root["cumulative_bisection_depth"] == self.nodes[current]["depth"], "root depth record differs")
            point = interval_pair(self.nodes[current]["interval"])[1]
            exact = str(point) if p_evaluate(self.q, point) == 0 else None
            require(root["exact_rational_point_if_detected"] == exact, "rational point detection differs")
            if index:
                require(interval_pair(self.nodes[ordered[index - 1]]["interval"])[1] <=
                        interval_pair(self.nodes[first]["interval"])[0], "isolated root intervals overlap")

    def validate_all_zero_tests(self):
        seen = set()
        for record in self.zero_tests:
            budget_guard()
            root_index, node_id = record["root_index"], record["root_node"]
            require(type(root_index) is int and 0 <= root_index < len(self.roots), "unknown root in zero test")
            root = self.roots[root_index]
            require(self.descendant(node_id, root["initial_node"]) and
                    self.descendant(root["current_node"], node_id) and self.nodes[node_id]["count"] == 1,
                    "zero test belongs to another real root")
            f = self.P(record["polynomial"])
            key = (root_index, tuple(sorted(f.items())))
            require(key not in seen, "duplicate B zero-test cache entry")
            seen.add(key)
            divisor = self.gcd_result(record["gcd_certificate"], self.q, f)
            require(self.P(record["gcd_polynomial"]) == divisor, "zero-test gcd polynomial differs")
            interval = interval_pair(self.nodes[node_id]["interval"])
            count = self.count(record["gcd_count"], divisor, interval)
            require(count in (0, 1), "zero-test gcd count outside single-root range")
            zero = count == 1
            require(record["is_zero_at_specified_root"] is zero, "specified root zero flag failed")
            if p_evaluate(self.q, interval[1]) == 0:
                value = p_evaluate(f, interval[1])
                require(rational_text(record["exact_point_value"]) == value and (value == 0) == zero,
                        "exact-point and gcd test disagree")
            else:
                require("exact_point_value" not in record, "unjustified exact-point value")
            self.zero_results[record["id"]] = (root_index, f, zero)

    def zero(self, identifier, root_index, expected):
        require(type(identifier) is int and identifier in self.zero_results, "missing exact zero test")
        actual_root, polynomial, result = self.zero_results[identifier]
        require(actual_root == root_index and polynomial == expected, "zero-test reference names another object")
        self.used_zero_tests.add(identifier)
        return result

    def zeros(self, identifiers, root_index, expected):
        require(isinstance(identifiers, list) and len(identifiers) == len(expected), "incomplete vector zero tests")
        return [self.zero(identifier, root_index, value) for identifier, value in zip(identifiers, expected)]

    def classify_all(self, columns, determinant, factors):
        primary = columns[(0, 1)]
        c = tuple(zip(primary["v"]["root"]["C"], primary["w"]["root"]["C"]))
        z = tuple(zip(primary["v"]["root"]["Z"], primary["w"]["root"]["Z"]))
        m = z[:2]
        original = self.document["original_inputs"]
        require(self.matrix(original["C"], 3) == c and self.matrix(original["Z"], 3) == z and
                self.matrix(original["M_unscaled"], 2) == m and self.P(original["P"]) == determinant and
                original["physical_phase_C_Z"] == "+i", "B input IDs differ from independent full coefficients")
        for root_index, root in enumerate(self.roots):
            budget_guard()
            interval = interval_pair(self.nodes[root["initial_node"]]["interval"])
            memberships = root["factor_memberships"]
            require(len(memberships) == len(factors), "missing root factor membership")
            multiplicities = []
            for record, (multiplicity, factor) in zip(memberships, factors):
                require(record["multiplicity"] == multiplicity and self.P(record["polynomial"]) == factor,
                        "root factor membership identity changed")
                count = self.count(record["count_certificate"], factor, interval)
                require(count in (0, 1), "multiple factor roots in one isolated root interval")
                if count:
                    multiplicities.append(multiplicity)
            require(len(multiplicities) == 1 and root["original_P_root_multiplicity"] == multiplicities[0],
                    "original P multiplicity is not uniquely certified")
            require(self.zero(root["determinant_zero_test"], root_index, determinant),
                    "INCONSISTENT_CERTIFICATE: nonzero determinant at certified P root")
            row_tests = root["M_entry_zero_tests_in_original_row_order"]
            require(isinstance(row_tests, list) and len(row_tests) == 2, "missing original M row tests")
            row_zero = [all(self.zeros(tests, root_index, row)) for tests, row in zip(row_tests, m)]
            rank = 0 if all(row_zero) else 1
            require(type(root["rank"]) is int and root["rank"] == rank, "root rank label differs from exact tests")
            normalization = root["normalization"]
            if rank == 1:
                row_index = next(j for j, zero in enumerate(row_zero) if not zero)
                r, s = m[row_index]
                v, w = p_scale(s, -1), r
                require(normalization["original_row_index"] == row_index and
                        self.vector(normalization["original_r_s"], 2) == (r, s) and
                        normalization["no_row_scaling_or_denominator_clearing"] is True,
                        "original first-row normalization changed")
            else:
                first = tuple(row[0] for row in c)
                zero_flags = self.zeros(root["rank_zero_first_C_column_tests"], root_index, first)
                chosen = 1 if all(zero_flags) else 0
                v, w = (constant(1), {}) if chosen == 0 else ({}, constant(1))
                require(normalization["chosen_column_index"] == chosen, "rank-zero C column rule changed")
            high = (p_add(p_scale(v, 3), p_scale(w, 5)), p_scale(v, -2), p_scale(w, -2))
            cv, zv = (apply_formal_columns(primary, name, v, w) for name in ("C", "Z"))
            saved = root["normalized_polynomials"]
            require(self.P(saved["v"]) == v and self.P(saved["w"]) == w and
                    self.vector(saved["V"], 3) == high and self.vector(saved["C"], 3) == cv and
                    self.vector(saved["Z"], 3) == zv, "normalized polynomial IDs differ from original data")
            tests = root["normalized_zero_tests"]
            require(not all(self.zeros(tests["v_w"], root_index, (v, w))), "normalized (v,w) is zero")
            require(not all(self.zeros(tests["V"], root_index, high)), "normalized V is zero")
            require(all(self.zeros(tests["Z"], root_index, zv)), "complete normalized Z is not zero")
            c_flags = self.zeros(tests["C"], root_index, cv)
            eligible = not all(c_flags)
            require(root["C_component_zero_flags"] == c_flags and root["eligible"] is eligible and
                    root["classification_complete"] is True, "C eligibility classification failed")
            targets = root["all_six_normalized_target_vectors"]
            require(len(targets) == len(columns) == 6, "missing normalized target")
            for target_record, ((rotation, sign), target_columns) in zip(targets, columns.items()):
                target = tuple(sign * x for x in rotate((3, 4, 6), rotation))
                tc, tz = (apply_formal_columns(target_columns, name, v, w) for name in ("C", "Z"))
                require(decode_A_frequency(target_record["target"]) == target and
                        self.vector(target_record["C"], 3) == tc and self.vector(target_record["Z"], 3) == tz,
                        "full six-target normalized polynomial mismatch")
                require((not all(self.zeros(target_record["C_zero_tests"], root_index, tc))) == eligible and
                        all(self.zeros(target_record["Z_zero_tests"], root_index, tz)), "six-target zero status differs")
                require(target_record["C_is_nonzero"] is eligible and target_record["Z_is_zero"] is True,
                        "six-target reported zero flag differs")
            self.normalized.append({"v": v, "w": w, "V": high, "C": cv, "Z": zv,
                                    "rank": rank, "eligible": eligible, "C_zero_flags": c_flags,
                                    "multiplicity": multiplicities[0]})
        require(self.used_zero_tests == set(range(len(self.zero_tests))), "unused/unanchored zero-test records")
        require(self.document["real_root_multiplicity_sum"] ==
                sum(item["multiplicity"] for item in self.normalized) <= p_degree(determinant),
                "real root multiplicity sum failed")
        require(self.document["all_distinct_roots_classified_before_selection"] is True,
                "all-root classification marker differs")

    def verify_main_window(self):
        eligible = [j for j, item in enumerate(self.normalized) if item["eligible"]]
        require(eligible, "frozen B success has no eligible root")
        selected = eligible[0]
        require(self.document["selected_root_index"] == selected, "not the first eligible ordered real root")
        root, normalized = self.roots[selected], self.normalized[selected]
        window = self.document["selected_window"]
        coordinate = next(j for j, zero in enumerate(normalized["C_zero_flags"]) if not zero)
        f = normalized["C"][coordinate]
        require(window["selected_root_index"] == selected and
                window["first_nonzero_C_coordinate_index"] == coordinate and
                self.P(window["C_coordinate_polynomial"]) == f,
                "window changed root or first nonzero C coordinate")
        trace = window["refinement_trace"]
        require(isinstance(trace, list) and trace, "missing window refinement trace")
        expected_node = root["initial_node"]
        refinement_parents = set()
        for index, item in enumerate(trace):
            node_id = item["root_node"]
            require(node_id == expected_node, "window did not follow the same isolated root")
            node = self.nodes[node_id]
            a, b = interval_pair(node["interval"])
            point = p_evaluate(self.q, b) == 0
            interval = (b, b) if point else (a, b)
            enclosure = p_enclosure(f, interval)
            avoids_zero = enclosure[0] > 0 or enclosure[1] < 0
            require(item["cumulative_depth"] == node["depth"] and
                    interval_pair(item["closed_input_enclosure"]) == interval and
                    interval_pair(item["C_coordinate_closed_enclosure"]) == enclosure and
                    item["strictly_avoids_zero"] is avoids_zero,
                    "window trace enclosure, sign or depth mismatch")
            if index == len(trace) - 1:
                require(avoids_zero and "children" not in node, "window stops without positive bound or after extra split")
            else:
                require(not avoids_zero and not point and "children" in node,
                        "unnecessary or unjustified C-bound refinement")
                children = node["children"]
                require(sorted(self.nodes[j]["count"] for j in children) == [0, 1] and
                        all(self.nodes[j]["purpose"] == "selected_root_C_lower_bound" for j in children),
                        "C-bound split does not retain exactly the same root")
                expected_node = next(j for j in children if self.nodes[j]["count"] == 1)
                refinement_parents.add(node_id)
        require({node["parent"] for node in self.nodes if node["purpose"] == "selected_root_C_lower_bound"}
                == refinement_parents, "unclaimed root refinement work")
        require(node_id == root["current_node"] == window["final_root_node"] and
                window["cumulative_bisection_depth"] == node["depth"] <= ROOT_REFINEMENT_LIMIT,
                "window final same-root node/depth differs")
        for index, other in enumerate(self.roots):
            if index != selected:
                require(other["current_node"] == other["initial_node"], "an unselected root was refined for its bound")
        require(interval_pair(window["alpha_closed_enclosure"]) == interval and
                interval_pair(window["C_coordinate_closed_enclosure"]) == enclosure,
                "final alpha or C enclosure differs")
        delta = min(abs(enclosure[0]), abs(enclosure[1]))
        ell = 2 * delta
        require(delta > 0 and rational_text(window["delta_near_zero_endpoint_absolute_value"]) == delta and
                rational_text(window["ell"]) == ell, "near-endpoint positive two-mode ell differs")
        v_box, w_box = (p_enclosure(normalized[name], interval) for name in ("v", "w"))
        high_boxes = tuple(p_enclosure(value, interval) for value in normalized["V"])
        require(interval_pair(window["v_closed_enclosure"]) == v_box and
                interval_pair(window["w_closed_enclosure"]) == w_box and
                tuple(interval_pair(item) for item in window["V_three_coordinate_closed_enclosures"]) == high_boxes,
                "original normalization amplitude enclosures differ")
        aalpha = max(abs(endpoint) for endpoint in interval)
        uv = max(abs(endpoint) for endpoint in v_box)
        uw = max(abs(endpoint) for endpoint in w_box)
        uv1 = max(abs(endpoint) for endpoint in high_boxes[0])
        abar = 6 * (1 + aalpha + uv1 + 2 * uv + 2 * uw)
        bbar = 28 * abar
        ebar = 80 * abar ** 4 * 7 ** 5 + 3 * abar * bbar ** 4
        dfirst = 2 * (1 + aalpha ** 2) + 2 * abar * bbar ** 2
        computed = {"Aalpha": aalpha, "Uv": uv, "Uw": uw, "UV1": uv1,
                    "Abar": abar, "bbar": bbar, "Ebar": ebar, "Dfirst": dfirst, "ell": ell}
        for name, value in computed.items():
            require(rational_text(window[name]) == value, "original main-window constant differs: " + name)
        candidates = (1 / (2 * bbar), ell / (8 * ebar), 1 / (2 * dfirst))
        main_t = min(candidates)
        require(all(value > 0 for value in (abar, bbar, ebar, dfirst, ell, main_t) + candidates),
                "original main-window positivity failed")
        require(tuple(rational_text(value) for value in window["three_time_candidates_in_contract_order"]) == candidates and
                rational_text(window["T"]) == main_t and
                window["minimum_attaining_indices"] == [j for j, value in enumerate(candidates) if value == main_t],
                "original main T is not the exact minimum of the three actual budgets")
        budgets = (("bbar*T<=1/2", bbar * main_t, Rational(1, 2)),
                   ("Ebar*T<=ell/8", ebar * main_t, ell / 8),
                   ("Dfirst*T<=1/2", dfirst * main_t, Rational(1, 2)))
        saved_budgets = window["exact_budget_certificates"]
        require(len(saved_budgets) == 3, "missing original-window budget")
        for saved, (name, left, right) in zip(saved_budgets, budgets):
            require(saved["name"] == name and rational_text(saved["left"]) == left and
                    rational_text(saved["right"]) == right and rational_text(saved["slack"]) == right - left and
                    left <= right and saved["verified"] is True, "original main T budget identity failed")
        require(window["certified"] is True and window["no_smaller_replacement_window"] is True and
                window["all_required_constants_and_three_times_positive"] is True,
                "B window label disagrees with independent exact checks")
        return {"selected_root_index": selected, "first_nonzero_C_coordinate_index": coordinate,
                "final_root_node": node_id, "cumulative_depth": node["depth"],
                "extra_C_bound_bisections": len(trace) - 1,
                "alpha_closed_enclosure": [str(value) for value in interval],
                "C_coordinate_closed_enclosure": [str(value) for value in enclosure],
                "computed_constants": {name: str(value) for name, value in computed.items()},
                "three_time_candidates_in_contract_order": [str(value) for value in candidates],
                "original_main_T": str(main_t), "smaller_window_substituted": False,
                "exact_budgets": [{"name": name, "left": str(left), "right": str(right),
                                   "slack": str(right - left)} for name, left, right in budgets]}


def verify_stopped_B_all_roots_and_main_window(report, columns, determinant, stage_b_path):
    path = Path(stage_b_path)
    require(path.name == "exact-roots-output.json", "wrong B output name")
    raw = path.read_bytes()
    require(len(raw) < OUTPUT_LIMIT_BYTES and hashlib.sha256(raw).hexdigest() == STAGE_B_OUTPUT_BINDING,
            "B stopped output byte binding failed")
    source = json.loads(raw.decode("utf-8"), object_pairs_hook=distinct_json_object)
    require(source["schema"] == "cyclic-six-carrier-stage-B-exact-roots-v1" and
            source["execution_status"] == "completed" and source["scientific_stage_completed"] is True and
            type(source["scientific_execution_count_in_this_invocation"]) is int and
            source["scientific_execution_count_in_this_invocation"] == 1,
            "B did not report one completed stage")
    require(source["resource_checks_at_recorded_boundary"] == ["PASS"], "B's own resource boundary was not passed")
    expected_sources = {"source": STAGE_B_SOURCE_BINDING, "contract": BASE_BINDINGS["CONTRACT.md"],
                        "stage_A_input": STAGE_A_OUTPUT_BINDING, "method": METHOD_BINDING,
                        "implementation_gate": GATE_BINDING}
    require(source["provenance"]["sha256_before_science"] == expected_sources ==
            source["provenance"]["sha256_after_science"], "B source bindings differ before/after its science")
    verifier = RootEvidenceVerifier(source)
    verifier.validate_all_gcds()
    verifier.validate_all_sturms()
    factors = verifier.square_free(determinant)
    verifier.validate_nodes()
    verifier.validate_all_zero_tests()
    verifier.classify_all(columns, determinant, factors)
    window = verifier.verify_main_window()
    require(verifier.polynomial_references == set(range(len(verifier.polynomials))),
            "some registered polynomial was not reached by full identity verification")
    require(source["stage_B_outcome"] == "EXACT_DATA_AND_WINDOW_CERTIFIED_PENDING_STAGE_C_AND_MATH_REVIEW",
            "B success label differs from the completed fixed-object certificate")
    report["stage_B_comparison"] = {
        "status": "PASS", "output_sha256": STAGE_B_OUTPUT_BINDING,
        "verified_record_counts": {"polynomials": len(verifier.polynomials), "gcd_certificates": len(verifier.gcds),
                                   "Sturm_chains": len(verifier.sturms), "isolation_nodes": len(verifier.nodes),
                                   "zero_tests": len(verifier.zero_tests), "distinct_real_roots": len(verifier.roots)},
        "Sturm_count_fields_recomputed": verifier.count_checks,
        "all_polynomial_IDs_referenced_and_checked": sorted(verifier.polynomial_references),
        "all_zero_test_IDs_used_by_same_data_claims": sorted(verifier.used_zero_tests),
        "root_summaries_in_certified_order": [
            {"index": index, "initial_half_open_interval": list(verifier.nodes[root["initial_node"]]["interval"]),
             "original_multiplicity": item["multiplicity"], "rank": item["rank"],
             "eligible": item["eligible"], "v_polynomial": encode_poly(item["v"]),
             "w_polynomial": encode_poly(item["w"]), "C_polynomials": encode_vector(item["C"]),
             "Z_polynomials": encode_vector(item["Z"]), "six_targets_verified": 6}
            for index, (root, item) in enumerate(zip(verifier.roots, verifier.normalized))],
        "independently_recomputed_original_main_window": window,
        "new_root_searches_or_bisections": 0,
        "scope": "All saved B identities and claims checked against independently regenerated full target coefficients; no new root or normalization choice",
    }


def resource_snapshot():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    darwin = os.uname().sysname == "Darwin"
    return {"wall_seconds_since_module_start": time.perf_counter() - MODULE_START,
            "user_CPU_seconds_SELF": usage.ru_utime, "system_CPU_seconds_SELF": usage.ru_stime,
            "maximum_RSS_SELF_bytes": usage.ru_maxrss if darwin else usage.ru_maxrss * 1024,
            "RSS_conversion": "Darwin ru_maxrss is bytes" if darwin else "non-Darwin ru_maxrss interpreted as KiB"}


def all_source_bindings(directory):
    expected = dict(BASE_BINDINGS)
    expected.update({"exact-coefficients-output.json": STAGE_A_OUTPUT_BINDING,
                     "exact_roots.py": STAGE_B_SOURCE_BINDING,
                     "exact-roots-output.json": STAGE_B_OUTPUT_BINDING,
                     "ROOT_METHOD_PREFLIGHT.md": METHOD_BINDING,
                     "STAGE_B_IMPLEMENTATION_GATE.md": GATE_BINDING})
    for name, expected_sha in expected.items():
        require(hashlib.sha256((directory / name).read_bytes()).hexdigest() == expected_sha,
                "stopped source byte binding failed: " + name)
    return expected


def json_bytes(report):
    return (json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def alarm_handler(signum, frame):
    raise TimeoutError("WALL_ALARM_EXPIRED")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-once-after-parent-authorization", action="store_true")
    parser.add_argument("--reviewer-source-commit", required=True)
    args = parser.parse_args()
    require(EXECUTION_READY and args.run_once_after_parent_authorization,
            "separate parent saved-source authorization flag is required")
    require(len(args.reviewer_source_commit) == 40 and
            all(value in "0123456789abcdef" for value in args.reviewer_source_commit),
            "reviewer source commit must be lowercase hexadecimal")
    source_path = Path(__file__).resolve()
    directory = source_path.parent
    output_path = directory / "verify-cyclic-output.json"
    require(not output_path.exists(), "output already exists: rerun/overwrite forbidden")
    source_sha = hashlib.sha256(source_path.read_bytes()).hexdigest()
    bindings = all_source_bindings(directory)
    uname = os.uname()
    report = {"schema": "cyclic-six-carrier-stage-C-exact-verification-v1",
              "execution_status": "not_started", "certification_status": "NOT_CERTIFIED",
              "scientific_execution_count_in_this_invocation": 0, "scientific_stage_completed": False,
              "provenance": {"reviewer_source_sha256": source_sha,
                             "reviewer_source_commit_parent_supplied": args.reviewer_source_commit,
                             "commit_not_verified_with_git": True,
                             "bound_inputs_before_science": bindings, "command_argv": list(sys.argv)},
              "formation_history": "Explicit five-tree/24-permutation core formed after A source review but before A output; A/B adapters followed actual documented scoped readings; not a blind third proof",
              "environment": {"python_version": sys.version, "python_executable": sys.executable,
                              "os_uname": {"sysname": uname.sysname, "nodename": uname.nodename,
                                           "release": uname.release, "version": uname.version, "machine": uname.machine},
                              "scientific_workers": 1, "scientific_threads": 1,
                              "external_processes_started": 0, "third_party_scientific_libraries": []},
              "limits": {"wall_seconds": WALL_LIMIT_SECONDS, "maximum_RSS_SELF_target_bytes": SELF_RSS_LIMIT_BYTES,
                         "output_bytes_strictly_below": OUTPUT_LIMIT_BYTES, "saved_root_depth_maximum": ROOT_REFINEMENT_LIMIT},
              "scope": "Fixed six-target finite tree coefficients, complete saved real-root certificates and the same original rational window; conditional AP input only, no NS simulation or generation claim"}
    signal.signal(signal.SIGALRM, alarm_handler)
    try:
        remaining = WALL_LIMIT_SECONDS - (time.perf_counter() - MODULE_START)
        require(remaining > 0, "wall budget exhausted before scientific start")
        signal.setitimer(signal.ITIMER_REAL, remaining)
        report["execution_status"] = "running"
        report["scientific_execution_count_in_this_invocation"] += 1
        core_report, columns, determinant = compute_coefficient_core()
        report["coefficient_computation"] = core_report
        compare_stopped_A_output(report, columns, determinant, directory / "exact-coefficients-output.json")
        verify_stopped_B_all_roots_and_main_window(report, columns, determinant, directory / "exact-roots-output.json")
        report["scientific_stage_completed"] = True
        require(hashlib.sha256(source_path.read_bytes()).hexdigest() == source_sha, "reviewer source changed during run")
        report["provenance"]["bound_inputs_after_science"] = all_source_bindings(directory)
        budget_guard()
        report["execution_status"] = "completed"
        report["certification_status"] = "EXACT_COEFFICIENTS_ALL_ROOTS_AND_ORIGINAL_WINDOW_VERIFIED"
    except Exception as error:
        report["execution_status"] = "not_certified"
        report["certification_status"] = "NOT_CERTIFIED"
        report["failure"] = {"type": type(error).__name__, "reason": str(error)}
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    report["resources_before_first_full_serialization"] = resource_snapshot()
    first = json_bytes(report)
    measured = resource_snapshot()
    report["resources_after_first_full_serialization"] = measured
    problems = []
    if measured["wall_seconds_since_module_start"] > WALL_LIMIT_SECONDS:
        problems.append("WALL_BUDGET_EXCEEDED")
    if measured["maximum_RSS_SELF_bytes"] > SELF_RSS_LIMIT_BYTES:
        problems.append("SELF_RSS_TARGET_EXCEEDED")
    if len(first) >= OUTPUT_LIMIT_BYTES:
        problems.append("OUTPUT_LIMIT_EXCEEDED")
    report["resource_checks_at_recorded_boundary"] = problems or ["PASS"]
    report["resource_scope"] = (
        "This Python process only. Wall starts immediately after importing time at module entry. "
        "The latter snapshot covers subsequent imports, input reads, science, assertions, byte rechecks and first full JSON serialization. "
        "Final resource fields, final serialization and unique disk write are outside this boundary. "
        "RUSAGE_SELF is not a whole-process-tree or full-lifecycle measurement.")
    if problems:
        report["execution_status"] = "not_certified"
        report["certification_status"] = "NOT_CERTIFIED"
    final_bytes = json_bytes(report)
    if len(final_bytes) >= OUTPUT_LIMIT_BYTES:
        report = {"schema": report["schema"], "execution_status": "not_certified",
                  "certification_status": "NOT_CERTIFIED",
                  "scientific_execution_count_in_this_invocation": report["scientific_execution_count_in_this_invocation"],
                  "scientific_stage_completed": report["scientific_stage_completed"],
                  "failure": {"reason": "FINAL_OUTPUT_LIMIT_EXCEEDED", "attempted_output_bytes": len(final_bytes)},
                  "provenance": report["provenance"], "environment": report["environment"],
                  "resources_after_first_full_serialization": measured, "resource_scope": report["resource_scope"],
                  "complete_verification_certificate_in_this_artifact": False}
        final_bytes = json_bytes(report)
    require(len(final_bytes) < OUTPUT_LIMIT_BYTES, "bounded failure record still exceeds output limit")
    with output_path.open("xb") as output:
        output.write(final_bytes)
    print(json.dumps({"execution_status": report["execution_status"],
                      "certification_status": report["certification_status"],
                      "scientific_execution_count_in_this_invocation": report["scientific_execution_count_in_this_invocation"],
                      "scientific_stage_completed": report["scientific_stage_completed"],
                      "output_path": str(output_path), "output_bytes": len(final_bytes),
                      "output_sha256": hashlib.sha256(final_bytes).hexdigest(),
                      "resources_after_first_full_serialization": measured}, ensure_ascii=False))
    return 0 if report["execution_status"] == "completed" else 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print(json.dumps({"execution_status": "failed", "certification_status": "NOT_CERTIFIED",
                          "type": type(error).__name__, "reason": str(error)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(2)
