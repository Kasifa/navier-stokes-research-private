#!/usr/bin/env python3
"""Stage A only: exact labelled four-leaf coefficients for the fixed C3 family.

Do not import, compile as a probe, or run before the author-stop source has
been saved and the parent has supplied the final contract execution gate.
This program never evaluates alpha at a point, isolates roots, chooses a
candidate, computes B(W0,W0), or evolves a finite or infinite NS solution.
"""

import time

MODULE_START = time.perf_counter()

import argparse
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys


WALL_LIMIT_SECONDS = 60
SELF_RSS_LIMIT_BYTES = 256 * 1024 * 1024
OUTPUT_LIMIT_BYTES = 1024 * 1024
SCIENTIFIC_WORKERS = 1


class NotCertified(Exception):
    """A required assertion or budget has not been certified."""


def require(condition, message):
    if not condition:
        raise NotCertified(message)


# Polynomials are canonical tuples of Fraction in increasing alpha degree.
# The zero polynomial is the one-term tuple (0,), with degree -1.
def poly(coefficients):
    coefficients = tuple(Fraction(x) for x in coefficients)
    if not coefficients:
        return (Fraction(0),)
    last = len(coefficients) - 1
    while last and coefficients[last] == 0:
        last -= 1
    return coefficients[:last + 1]


ZERO = poly((0,))
ONE = poly((1,))
ALPHA = poly((0, 1))
ZERO_VECTOR = (ZERO, ZERO, ZERO)


def pdegree(a):
    return -1 if a == ZERO else len(a) - 1


def padd(a, b):
    result = [Fraction(0)] * max(len(a), len(b))
    for j, value in enumerate(a):
        result[j] += value
    for j, value in enumerate(b):
        result[j] += value
    return poly(result)


def pscale(a, scalar):
    return poly(scalar * value for value in a)


def psub(a, b):
    return padd(a, pscale(b, -1))


def pmul(a, b):
    result = [Fraction(0)] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            result[j + k] += x * y
    return poly(result)


def vadd(a, b):
    return tuple(padd(x, y) for x, y in zip(a, b))


def vscale(a, scalar):
    return tuple(pscale(x, scalar) for x in a)


def vsum(vectors):
    result = ZERO_VECTOR
    for vector in vectors:
        result = vadd(result, vector)
    return result


def polynomial_times_vector(scalar, vector):
    return tuple(pmul(scalar, x) for x in vector)


def frequency_dot(k, vector):
    result = ZERO
    for scalar, component in zip(k, vector):
        result = padd(result, pscale(component, scalar))
    return result


def rotate(vector, times=1):
    for unused in range(times % 3):
        vector = (vector[2], vector[0], vector[1])
    return vector


def fadd(k, ell):
    return tuple(x + y for x, y in zip(k, ell))


def fscale(k, scalar):
    return tuple(scalar * x for x in k)


def leray(k, vector):
    norm_squared = sum(x * x for x in k)
    require(norm_squared != 0, "Leray requested at zero frequency")
    normal = frequency_dot(k, vector)
    return tuple(
        psub(component, pscale(normal, Fraction(x, norm_squared)))
        for x, component in zip(k, vector)
    )


def ordered_vertex(left_k, left_u, right_k, right_u, stats):
    """The full one-mode ordered Q, where B=-i Q; never symmetrize by 2."""
    stats["ordered_vertices"] += 1
    require(frequency_dot(left_k, left_u) == ZERO,
            "nontransverse first input")
    require(frequency_dot(right_k, right_u) == ZERO,
            "nontransverse second input")
    output_k = fadd(left_k, right_k)
    directional_factor = frequency_dot(right_k, left_u)
    if output_k == (0, 0, 0):
        stats["zero_output_vertices"] += 1
        require(directional_factor == ZERO,
                "zero output did not vanish term by term")
        return ZERO_VECTOR
    result = leray(
        output_k, polynomial_times_vector(directional_factor, right_u)
    )
    require(frequency_dot(output_k, result) == ZERO,
            "ordered Leray output is not transverse")
    return result


LEAF_SHAPE = "x"
BALANCED_SHAPE = "((x,x),(x,x))"
EXPECTED_ROOT_SHAPES = frozenset((
    "(x,(x,(x,x)))",
    "(x,((x,x),x))",
    "((x,x),(x,x))",
    "((x,(x,x)),x)",
    "(((x,x),x),x)",
))
M13_SHAPES = frozenset(("(x,(x,(x,x)))", "(x,((x,x),x))"))
M31_SHAPES = frozenset(("((x,(x,x)),x)", "(((x,x),x),x)"))


def popcount(mask):
    return bin(mask).count("1")


def subset_labels(mask):
    return tuple(j for j in range(4) if mask & (1 << j))


def subset_frequency(mask, frequencies):
    result = (0, 0, 0)
    for j in subset_labels(mask):
        result = fadd(result, frequencies[j])
    return result


def fixed_leaves(rotation_index, sign, high_column):
    """Four labels valid for this target by the proved <=4-leaf uniqueness."""
    base_frequencies = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 3, 5))
    low_first = (ZERO, ONE, ALPHA)
    high = {
        "v": (poly((3,)), poly((-2,)), ZERO),
        "w": (poly((5,)), ZERO, poly((-2,))),
    }[high_column]
    base_amplitudes = (
        low_first, rotate(low_first), rotate(low_first, 2), high
    )
    frequencies = tuple(
        fscale(rotate(k, rotation_index), sign) for k in base_frequencies
    )
    # Negative modes have the same real coefficients, not their negatives.
    amplitudes = tuple(
        rotate(u, rotation_index) for u in base_amplitudes
    )
    return frequencies, amplitudes


def labelled_recurrence(rotation_index, sign, high_column):
    frequencies, amplitudes = fixed_leaves(rotation_index, sign, high_column)
    stats = {"ordered_vertices": 0, "zero_output_vertices": 0}
    subsets = {}
    for size in range(1, 5):
        for mask in range(1, 16):
            if popcount(mask) != size:
                continue
            labels = subset_labels(mask)
            k = subset_frequency(mask, frequencies)
            if size == 1:
                tree_values = {LEAF_SHAPE: amplitudes[labels[0]]}
            else:
                tree_values = {}
                # Each nonempty proper LEFT subset appears exactly once.
                # The right subset is the complement; reversing is separate.
                left_mask = (mask - 1) & mask
                while left_mask:
                    right_mask = mask ^ left_mask
                    left = subsets[left_mask]
                    right = subsets[right_mask]
                    for left_shape, left_u in left["trees"].items():
                        for right_shape, right_u in right["trees"].items():
                            shape = "(" + left_shape + "," + right_shape + ")"
                            term = ordered_vertex(
                                left["frequency"], left_u,
                                right["frequency"], right_u, stats
                            )
                            # A size-m subtree has m-1 ordered vertices.
                            # Integration of s^(m-2) is t^(m-1)/(m-1).
                            term = vscale(term, Fraction(1, size - 1))
                            tree_values[shape] = vadd(
                                tree_values.get(shape, ZERO_VECTOR), term
                            )
                    left_mask = (left_mask - 1) & mask
            total = vsum(tree_values.values())
            low_leaf_count = sum(1 for j in labels if j != 3)
            for tree_u in tree_values.values():
                require(frequency_dot(k, tree_u) == ZERO,
                        "tree coefficient is not transverse")
                require(all(pdegree(x) <= low_leaf_count for x in tree_u),
                        "tree alpha degree exceeds its low-leaf count")
            require(frequency_dot(k, total) == ZERO,
                    "subset total is not transverse")
            subsets[mask] = {
                "frequency": k,
                "labels": labels,
                "trees": tree_values,
                "total": total,
            }
    root = subsets[15]
    require(frozenset(root["trees"]) == EXPECTED_ROOT_SHAPES,
            "four-leaf root does not contain exactly the five ordered shapes")
    c = root["trees"][BALANCED_SHAPE]
    m13 = vsum(root["trees"][shape] for shape in sorted(M13_SHAPES))
    m31 = vsum(root["trees"][shape] for shape in sorted(M31_SHAPES))
    z = vadd(m13, m31)
    require(root["total"] == vadd(c, z),
            "full root differs from W + M13 + M31")
    for vector in (c, m13, m31, z, root["total"]):
        require(all(pdegree(x) <= 3 for x in vector),
                "target alpha degree exceeds three")
        require(frequency_dot(root["frequency"], vector) == ZERO,
                "target root is not transverse")
    return {
        "frequencies": frequencies,
        "amplitudes": amplitudes,
        "subsets": subsets,
        "root": {"C": c, "M13": m13, "M31": m31,
                 "Z": z, "full_four_leaf": root["total"]},
        "stats": stats,
    }


def encode_poly(a):
    return {
        "coefficients_low_to_high": [str(x) for x in a],
        "degree": pdegree(a),
    }


def encode_vector(vector):
    return [encode_poly(x) for x in vector]


def encode_column(column):
    return {
        "input_labels": [
            {"label": j, "frequency": list(k), "amplitude": encode_vector(u)}
            for j, (k, u) in enumerate(
                zip(column["frequencies"], column["amplitudes"])
            )
        ],
        "all_nonempty_label_subsets": [
            {
                "mask": mask,
                "labels": list(record["labels"]),
                "frequency": list(record["frequency"]),
                "total": encode_vector(record["total"]),
                "ordered_tree_shapes": {
                    shape: encode_vector(record["trees"][shape])
                    for shape in sorted(record["trees"])
                },
            }
            for mask, record in sorted(column["subsets"].items())
        ],
        "root_vectors": {
            name: encode_vector(vector)
            for name, vector in column["root"].items()
        },
        "counts": column["stats"],
    }


def check_covariance(results):
    for rotation_index in range(3):
        for sign in (1, -1):
            for basis in ("v", "w"):
                current = results[(rotation_index, sign)][basis]
                reference = results[(0, 1)][basis]
                for mask in range(1, 16):
                    expected_k = fscale(
                        rotate(reference["subsets"][mask]["frequency"],
                               rotation_index), sign
                    )
                    actual = current["subsets"][mask]
                    require(actual["frequency"] == expected_k,
                            "labelled frequency covariance failed")
                    parity = sign ** (popcount(mask) - 1)
                    reference_trees = reference["subsets"][mask]["trees"]
                    require(set(actual["trees"]) == set(reference_trees),
                            "tree-shape covariance domain mismatch")
                    for shape, vector in reference_trees.items():
                        expected = vscale(rotate(vector, rotation_index), parity)
                        require(actual["trees"][shape] == expected,
                                "rotation or negative-mode tree covariance failed")
                for name, vector in reference["root"].items():
                    expected = vscale(rotate(vector, rotation_index), sign)
                    require(current["root"][name] == expected,
                            "full target rotation or conjugacy failed")
            # With no high label the two column computations coincide.
            for mask in range(1, 8):
                v_sub = results[(rotation_index, sign)]["v"]["subsets"][mask]
                w_sub = results[(rotation_index, sign)]["w"]["subsets"][mask]
                require(v_sub == w_sub, "high-free subsets depend on high basis")
    # This is the contract's disclosed first-band identity, already contained
    # in the required two-leaf subset. It is not an alpha-value probe.
    first_band = results[(0, 1)]["v"]["subsets"][3]["total"]
    expected = (ZERO, ZERO, poly((1, 0, 1)))
    require(first_band == expected, "contract first-band polynomial mismatch")


def scientific_stage(report):
    results = {}
    report["target_records"] = []
    for rotation_index in range(3):
        for sign in (1, -1):
            columns = {}
            for basis in ("v", "w"):
                columns[basis] = labelled_recurrence(
                    rotation_index, sign, basis
                )
            target = columns["v"]["subsets"][15]["frequency"]
            expected_target = fscale(rotate((3, 4, 6), rotation_index), sign)
            require(target == expected_target, "fixed target frequency mismatch")
            results[(rotation_index, sign)] = columns
            report["target_records"].append({
                "rotation_index": rotation_index,
                "sign": sign,
                "target": list(target),
                "columns": {basis: encode_column(columns[basis])
                            for basis in ("v", "w")},
            })
    check_covariance(results)
    primary = results[(0, 1)]
    zv = primary["v"]["root"]["Z"]
    zw = primary["w"]["root"]["Z"]
    cv = primary["v"]["root"]["C"]
    cw = primary["w"]["root"]["C"]
    determinant = psub(pmul(zv[0], zw[1]), pmul(zw[0], zv[1]))
    require(pdegree(determinant) <= 6, "mixed determinant degree exceeds six")
    report["primary_matrices"] = {
        "target": [3, 4, 6],
        "C_full_three_rows_v_w_columns": [
            [encode_poly(cv[j]), encode_poly(cw[j])] for j in range(3)
        ],
        "Z_full_three_rows_v_w_columns": [
            [encode_poly(zv[j]), encode_poly(zw[j])] for j in range(3)
        ],
        "M_first_two_Z_rows": [
            [encode_poly(zv[j]), encode_poly(zw[j])] for j in range(2)
        ],
        "P_determinant": encode_poly(determinant),
        "third_component_identity": "X3=-(3*X1+4*X2)/6",
    }
    report["exact_checks"] = {
        "all_six_targets_computed_directly": True,
        "all_nonempty_proper_left_subsets_included": True,
        "all_five_ordered_four_leaf_shapes_included": True,
        "all_three_vector_components_retained": True,
        "complete_M13_and_M31_retained_separately": True,
        "all_subsets_and_trees_transverse": True,
        "all_subsets_rotation_and_negative_mode_parity": True,
        "physical_four_leaf_phase_is_plus_i": True,
        "root_real_conjugacy": True,
        "all_target_alpha_degrees_at_most_three": True,
        "determinant_alpha_degree_at_most_six": True,
        "high_free_subset_columns_agree": True,
        "disclosed_first_band_identity_verified": True,
    }
    if determinant == ZERO:
        report["stage_A_outcome"] = "DEGENERATE_CHART_NO_CERTIFICATE"
        report["root_stage_instruction"] = (
            "P is identically zero; stop under the contract, without a "
            "continuous parameter search or a universal infeasibility claim."
        )
    elif pdegree(determinant) == 0:
        report["stage_A_outcome"] = (
            "NO_CANDIDATE_FOR_THIS_CONTRACT_NONZERO_CONSTANT_DETERMINANT"
        )
        report["root_stage_instruction"] = (
            "P is a nonzero constant; the fixed exact cancellation gate "
            "has no nonzero high-amplitude solution."
        )
    else:
        report["stage_A_outcome"] = "COEFFICIENTS_CERTIFIED_ROOT_STAGE_PENDING"
        report["root_stage_instruction"] = (
            "P is nonconstant. No root, rank at a root, normalized amplitude, "
            "candidate, norm lower bound, or NS time window was computed here."
        )


def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valid_hex(value, length):
    return len(value) == length and all(c in "0123456789abcdef" for c in value)


def resource_snapshot():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    uname = os.uname()
    rss_bytes = usage.ru_maxrss if uname.sysname == "Darwin" else usage.ru_maxrss * 1024
    return {
        "wall_seconds_since_module_start": time.perf_counter() - MODULE_START,
        "user_CPU_seconds_SELF": usage.ru_utime,
        "system_CPU_seconds_SELF": usage.ru_stime,
        "maximum_RSS_SELF_bytes": rss_bytes,
        "RSS_conversion": ("Darwin ru_maxrss is bytes" if uname.sysname == "Darwin"
                           else "non-Darwin ru_maxrss interpreted as KiB"),
    }


def budget_problems(snapshot):
    problems = []
    if snapshot["wall_seconds_since_module_start"] > WALL_LIMIT_SECONDS:
        problems.append("WALL_BUDGET_EXCEEDED")
    if snapshot["maximum_RSS_SELF_bytes"] > SELF_RSS_LIMIT_BYTES:
        problems.append("SELF_RSS_TARGET_EXCEEDED")
    return problems


def alarm_handler(signum, frame):
    raise NotCertified("WALL_ALARM_EXPIRED")


def json_bytes(report):
    return (json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)
            + "\n").encode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--contract-sha", required=True)
    args = parser.parse_args()
    source_path = Path(__file__).resolve()
    contract_path = source_path.with_name("CONTRACT.md")
    output_path = source_path.with_name("exact-coefficients-output.json")
    # Existing evidence is never replaced. No scientific work has run yet.
    require(not output_path.exists(), "output already exists; rerun forbidden")
    require(valid_hex(args.source_commit, 40), "source commit must be lowercase hex")
    require(valid_hex(args.contract_sha, 64), "contract SHA must be lowercase hex")
    source_sha = sha256_file(source_path)
    contract_sha = sha256_file(contract_path)
    require(contract_sha == args.contract_sha, "contract bytes do not match argument")
    uname = os.uname()
    scientific_execution_count = 0
    report = {
        "schema": "cyclic-six-carrier-stage-A-exact-coefficients-v1",
        "execution_status": "not_started",
        "stage_A_outcome": "NOT_CERTIFIED",
        "scientific_execution_count_in_this_invocation": scientific_execution_count,
        "scientific_stage_completed": False,
        "fixed_initial_data": {
            "viscosity": "1",
            "domain": "standard (R/2*pi*Z)^3",
            "forcing": "zero",
            "R": "(x1,x2,x3) -> (x3,x1,x2)",
            "positive_frequencies": [
                [1, 0, 0], [0, 1, 0], [0, 0, 1],
                [2, 3, 5], [5, 2, 3], [3, 5, 2],
            ],
            "positive_amplitude_formulae": [
                "(0,1,alpha)", "(alpha,0,1)", "(1,alpha,0)",
                "V=(3*v+5*w,-2*v,-2*w)", "R*V", "R^2*V",
            ],
            "negative_modes": "same real coefficient as the positive mode",
            "parameters": "formal alpha; exact symbolic linear columns v,w",
            "subsequent_allowed_datum_domain": (
                "real algebraic alpha,v,w with (v,w) nonzero; no point selected"
            ),
        },
        "scientific_scope": (
            "Six specified targets only, via the proved unique signed four-leaf "
            "multiset and all ordered labelled tree shapes. This is not a "
            "full twelve-mode convolution or a full NS spectrum computation."
        ),
        "column_interpretation": (
            "For every subset containing high label 3, the two columns are "
            "the exact coefficients of v and w. High-free subsets are common "
            "to both columns and must not be added twice. The four-leaf root "
            "always contains the high label exactly once."
        ),
        "polynomial_convention": (
            "Exact Fraction coefficients, increasing alpha degree, canonical "
            "trailing zeros removed; zero has coefficients ['0'] and degree -1."
        ),
        "phase_convention": (
            "Each ordered Q has B=-i Q. A subtree with m leaves has physical "
            "phase (-i)^(m-1); the four-leaf C, M13, M31, Z have phase +i."
        ),
        "tree_normalization": (
            "Each size-m subtree divides its ordered split sum by m-1. "
            "Thus the balanced four-leaf shape has 1/3 and each chain 1/6."
        ),
        "not_executed": [
            "alpha interpolation or value probes",
            "root isolation or factorization",
            "rank tests at algebraic roots",
            "candidate selection or amplitude normalization",
            "B(W0,W0) or any eight-leaf computation",
            "actual NS time evolution or a numerical time window",
            "parameter or alternative-frequency searches",
        ],
        "provenance": {
            "source_path": str(source_path),
            "source_sha256": source_sha,
            "source_commit_parent_supplied": args.source_commit,
            "commit_not_verified_by_git_in_this_program": True,
            "contract_path": str(contract_path),
            "contract_sha256": contract_sha,
            "command_argv": list(sys.argv),
        },
        "environment": {
            "python_version": sys.version,
            "python_executable": sys.executable,
            "os_uname": {"sysname": uname.sysname, "nodename": uname.nodename,
                         "release": uname.release, "version": uname.version,
                         "machine": uname.machine},
            "visible_logical_CPUs": os.cpu_count(),
            "scientific_workers": SCIENTIFIC_WORKERS,
            "scientific_threads": 1,
            "third_party_scientific_libraries": [],
            "external_processes_started": 0,
        },
        "limits": {
            "wall_seconds": WALL_LIMIT_SECONDS,
            "target_maximum_RSS_SELF_bytes": SELF_RSS_LIMIT_BYTES,
            "output_bytes_strictly_below": OUTPUT_LIMIT_BYTES,
        },
    }
    signal.signal(signal.SIGALRM, alarm_handler)
    try:
        remaining = WALL_LIMIT_SECONDS - (time.perf_counter() - MODULE_START)
        require(remaining > 0, "wall budget exhausted before scientific stage")
        signal.setitimer(signal.ITIMER_REAL, remaining)
        report["execution_status"] = "running"
        scientific_execution_count += 1
        report["scientific_execution_count_in_this_invocation"] = scientific_execution_count
        scientific_stage(report)
        report["scientific_stage_completed"] = True
        require(sha256_file(source_path) == source_sha, "source changed during run")
        require(sha256_file(contract_path) == contract_sha, "contract changed during run")
        report["execution_status"] = "completed"
    except Exception as error:
        report["execution_status"] = "not_certified"
        report["stage_A_outcome"] = "NOT_CERTIFIED"
        report["failure"] = {"type": type(error).__name__, "reason": str(error)}
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
        "This Python process only; wall clock starts just after importing time "
        "at module entry. The latter snapshot includes science, assertions, "
        "input-byte rechecks and first full JSON serialization. Final resource "
        "fields, final JSON serialization and the unique disk write are outside "
        "that measured boundary. No whole-process-tree or full-lifecycle claim."
    )
    report["resource_checks_at_recorded_boundary"] = problems or ["PASS"]
    if problems:
        report["execution_status"] = "not_certified"
        report["stage_A_outcome"] = "NOT_CERTIFIED"
    final_serialization = json_bytes(report)
    if len(final_serialization) >= OUTPUT_LIMIT_BYTES:
        # Preserve a bounded failure record rather than silently omit a target
        # while retaining a completed scientific outcome.
        report = {
            "schema": report["schema"],
            "execution_status": "not_certified",
            "stage_A_outcome": "NOT_CERTIFIED",
            "scientific_execution_count_in_this_invocation": report[
                "scientific_execution_count_in_this_invocation"
            ],
            "scientific_stage_completed": report["scientific_stage_completed"],
            "failure": {"reason": "FINAL_OUTPUT_LIMIT_EXCEEDED",
                        "attempted_output_bytes": len(final_serialization)},
            "provenance": report["provenance"],
            "environment": report["environment"],
            "resources_after_first_full_serialization": after_serialization,
            "resource_scope": report["resource_scope"],
            "full_coefficients_certified_by_this_artifact": False,
        }
        final_serialization = json_bytes(report)
    require(len(final_serialization) < OUTPUT_LIMIT_BYTES,
            "even the bounded failure record exceeds output limit")
    with output_path.open("xb") as output_file:
        output_file.write(final_serialization)
    print(json.dumps({
        "execution_status": report["execution_status"],
        "stage_A_outcome": report["stage_A_outcome"],
        "output_path": str(output_path),
        "output_sha256": hashlib.sha256(final_serialization).hexdigest(),
        "output_bytes": len(final_serialization),
        "resources_after_first_full_serialization": after_serialization,
        "scientific_execution_count_in_this_invocation": report[
            "scientific_execution_count_in_this_invocation"
        ],
        "scientific_stage_completed": report["scientific_stage_completed"],
    }, ensure_ascii=False))
    return 0 if report["execution_status"] == "completed" else 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        # Pre-run input/overwrite errors or output I/O failures are failures,
        # never an invitation to change data or rerun.
        print(json.dumps({"execution_status": "failed",
                          "type": type(error).__name__,
                          "reason": str(error)}, ensure_ascii=False),
              file=sys.stderr)
        sys.exit(2)
