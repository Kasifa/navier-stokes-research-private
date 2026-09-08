#!/usr/bin/env python3
"""PREPARATION ONLY: stage C coefficient core, never yet executed.

Nonauthor different organization after reading the stage A source: explicit
five ordered shapes, 24 label permutations, sparse rational polynomials and
double-cross Leray.  This core was formed before reading the stopped A output.
The A adapter was then prepared after a documented scoped read of that output.
The future B schema remains unread; root/candidate/window work is pending.
No import, compile, probe or execution is authorized for this prepared file.
"""

from fractions import Fraction as Rational
import hashlib
from itertools import permutations
import json
from pathlib import Path


BASE_BINDINGS = {
    "CONTRACT.md": "a441be9b7adf0ee900eeaa786119e7c6f8fecb4c3a01bc4678f1c23fddad1a9b",
    "exact_coefficients.py": "7ce63da05ad2d2e51acfdc7cd51f6630191734574f62af000f3edba7221d9a64",
    "APPLICATION_PROOF.md": "096f626a754654039922eae0b13354e27e870ef113ee0967ffaebd29713955d4",
}
# Exact stopped bytes, with the actual human reading scope recorded in DESIGN.
STAGE_A_OUTPUT_BINDING = "9329464c09faa50558bc090b3af8c3ec6f074619e01a9fe2d5eb6d0f1c079ae6"
STAGE_B_SOURCE_BINDING = None
STAGE_B_OUTPUT_BINDING = None
EXECUTION_READY = False

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


def verify_stopped_B_all_roots_and_main_window(report, columns, determinant):
    raise NotImplementedError("Future B schema, all-root certificates and main window are not yet bound")


def main():
    # No coefficient call, output write, trial import or partial certificate.
    raise SystemExit("PREPARED_ONLY: stage C adapters and final parent execution gate are not complete")


if __name__ == "__main__":
    main()
