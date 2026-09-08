#!/usr/bin/env python3
"""One authorized rational input preparation; invoke only through run_input.py.

No old scientific module is imported. The only root is the previously certified
one in (-75/32, -125/64]. Exact-point detection is the sole early stopping rule.
Memory argument: 80 degree-six Horner evaluations have dyadic endpoint
denominators at most 2**86. Source coefficient numerators/denominators have fewer
than 64 bits. The finitely many degree-three interval operations, squares and
float error fractions fit the conservative 4096-bit serialization guard. At
most 20,000 serialized scalar nodes and 1 MiB of JSON are allowed. The rational
payload is consequently small; interpreter/allocator overhead is NOT certified
by that argument. The supervisor measures the actual child peak RSS after exit
and accepts it only at <=256 MiB. No RLIMIT_AS is used.
"""

import time

CHILD_CLOCK_START = time.perf_counter()

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
from fractions import Fraction as F


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUTPUT = HERE / "input-preparation.json"
MAX_OUTPUT_BYTES = 1 << 20
MAX_SCALAR_NODES = 20000
MAX_RATIONAL_BITS = 4096
Q = 36
DEN = 1 << Q
INT_LIMIT = 1 << 53
SOURCES = {
    "research/reverse/annular-source-observation/CONTRACT.md":
        "4ae019c3aac7d23a2392273a8cfb52ba08cf5131c35f8bc9e56918dae41c68d8",
    "research/reverse/annular-source-observation/INPUT_CONTRACT.md":
        "2d02549be48f26001c794b06f8d7ecb74e46be3ed051e72019860a56eab6768d",
    "research/reverse/cyclic-six-carrier/ALGEBRA_A.md":
        "a5dad046a56e3f6d6a9a417304635c23c9e84871528baffbfd5dbedf6cfea32b",
    "research/reverse/cyclic-six-carrier/ALGEBRA_B.md":
        "2321cea6a0b066e5356b98c22198bf389180e4a53181c4e5bb3ab9825093c499",
}

# Original ascending coefficients, transcribed from CA.5 and CB.3.
P_TEXT = (
    "12379608041588/607290075", "129169813631527/1012150125",
    "111813118362046/337383375", "1377133612024132/3036450375",
    "207263796033514/607290075", "401161881122159/3036450375",
    "4124532235492/202430025",
)
R_TEXT = (
    "1807613971/12393675", "9523582624/20656125",
    "27816146846/61968375", "196585982/1770525",
)
S_TEXT = (
    "536919079/2699067", "9469267576/13495335",
    "10524885968/13495335", "646271818/2699067",
)


def require(test, message):
    if not test:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sign(x):
    return (x > 0) - (x < 0)


def horner(poly, x):
    result = poly[-1]
    for coefficient in reversed(poly[:-1]):
        result = result * x + coefficient
    return result


def interval_horner(poly, interval):
    value = (poly[-1], poly[-1])
    trace = [{"coefficient_index": len(poly) - 1, "interval": value}]
    for index in range(len(poly) - 2, -1, -1):
        products = tuple(a * b for a in value for b in interval)
        value = (min(products) + poly[index], max(products) + poly[index])
        trace.append({"coefficient_index": index,
                      "four_products": products, "interval": value})
    return value, trace


def square_interval(interval):
    lo, hi = interval
    return (F(0) if lo <= 0 <= hi else min(lo * lo, hi * hi),
            max(lo * lo, hi * hi))


def max_abs(interval):
    return max(abs(interval[0]), abs(interval[1]))


def rounding_record(value):
    scaled = value * DEN
    lower, remainder = divmod(scaled.numerator, scaled.denominator)
    twice = 2 * remainder
    increment = twice > scaled.denominator or (
        twice == scaled.denominator and lower % 2 != 0)
    numerator = lower + int(increment)
    rounded = F(numerator, DEN)
    require(abs(value - rounded) <= F(1, 2 * DEN), "rounding radius")
    return numerator, {"exact_midpoint_value": value,
                       "scaled_floor": lower, "remainder": remainder,
                       "remainder_denominator": scaled.denominator,
                       "tie": twice == scaled.denominator,
                       "rounded_numerator": numerator, "rounded": rounded,
                       "absolute_midpoint_rounding_error": abs(value - rounded)}


def exact_float(value):
    number = float(value)  # One conversion from the exact rational coordinate.
    require(math.isfinite(number), "nonfinite coefficient float")
    recovered = F(*number.as_integer_ratio())
    require(recovered == value, "dyadic coefficient is not exact binary64")
    return number, {"rational": value, "float_hex": number.hex(),
                    "float_ratio": recovered, "decimal_display_only": repr(number)}


def time_float(value):
    number = float(value)
    require(math.isfinite(number) and number > 0, "invalid time float")
    recovered = F(*number.as_integer_ratio())
    return {"exact": value, "float_hex": number.hex(),
            "float_ratio": recovered, "decimal_display_only": repr(number),
            "signed_conversion_error": recovered - value,
            "absolute_conversion_error": abs(recovered - value)}


def rotate(vector):
    return (vector[2], vector[0], vector[1])


def prepare(data):
    P, rp, sp = tuple(map(F, P_TEXT)), tuple(map(F, R_TEXT)), tuple(map(F, S_TEXT))
    polys = {"v": tuple(-x for x in sp), "w": rp,
             "V1": tuple(-3 * x + 5 * y for x, y in zip(sp, rp)),
             "V2": tuple(2 * x for x in sp), "V3": tuple(-2 * x for x in rp)}
    data["polynomials_ascending"] = {"P": P, "r": rp, "s": sp, **polys}
    lo, hi = F(-75, 32), F(-125, 64)
    flo, fhi = horner(P, lo), horner(P, hi)
    require(flo * fhi < 0, "original endpoints must be nonzero and opposite")
    isolation = {"initial_half_open_interval": (lo, hi),
                 "initial_endpoint_values": (flo, fhi),
                 "single_root_uniqueness": "inherited from CB.8, not recomputed",
                 "maximum_bisections": 80, "steps": []}
    data["root_isolation"] = isolation
    exact_point = None
    for step in range(1, 81):
        before = (lo, hi)
        mid = (lo + hi) / 2
        fmid = horner(P, mid)
        record = {"step": step, "before": before,
                  "midpoint": mid, "P_midpoint": fmid}
        if fmid == 0:
            lo = hi = exact_point = mid
            flo = fhi = F(0)
            record["branch"] = "exact_root_point"
        elif sign(fmid) == sign(flo):
            lo, flo = mid, fmid
            record["branch"] = "right_half"
        else:
            require(sign(fmid) == sign(fhi), "unclassified nonzero sign")
            hi, fhi = mid, fmid
            record["branch"] = "left_half"
        require(before[0] <= lo <= hi <= before[1], "lost interval inclusion")
        require(exact_point is not None or flo * fhi < 0, "lost endpoint signs")
        record["after"] = (lo, hi)
        isolation["steps"].append(record)
        if exact_point is not None:
            break
    require(exact_point is not None or len(isolation["steps"]) == 80,
            "unpermitted early stopping")
    isolation.update({"completed_bisections": len(isolation["steps"]),
                      "exact_root_point": exact_point,
                      "final_closed_interval": (lo, hi),
                      "final_endpoint_values": (flo, fhi),
                      "stop_reason": "exact_root" if exact_point is not None
                      else "exactly_80_bisections"})

    intervals = {"alpha": (lo, hi)}
    traces = {}
    for name, poly in polys.items():
        intervals[name], traces[name] = interval_horner(poly, (lo, hi))
    data["interval_horner_traces"] = traces
    data["intervals"] = intervals
    alpha_mid = (lo + hi) / 2
    midpoints = {"alpha": alpha_mid, "v": horner(polys["v"], alpha_mid),
                 "w": horner(polys["w"], alpha_mid)}
    rounding, integers = {}, {}
    for name, value in midpoints.items():
        integers[name], rounding[name] = rounding_record(value)
    data["rounding"] = {"q": Q, "common_denominator": DEN,
                        "rule": "nearest; ties to even", "records": rounding}
    A, Vn, Wn = integers["alpha"], integers["v"], integers["w"]
    intermediate = {"A": A, "Vn": Vn, "Wn": Wn, "denominator": DEN,
                    "3Vn": 3 * Vn, "5Wn": 5 * Wn,
                    "3Vn+5Wn": 3 * Vn + 5 * Wn,
                    "-2Vn": -2 * Vn, "-2Wn": -2 * Wn}
    require(all(abs(x) <= INT_LIMIT for x in intermediate.values()),
            "dyadic construction integer exceeds 2**53")
    nums_U, nums_V = (0, DEN, A), (3 * Vn + 5 * Wn, -2 * Vn, -2 * Wn)
    U, V = tuple(F(x, DEN) for x in nums_U), tuple(F(x, DEN) for x in nums_V)
    float_U, float_V, float_records = [], [], {"U": [], "V": []}
    for label, vector, floats in (("U", U, float_U), ("V", V, float_V)):
        for value in vector:
            number, record = exact_float(value)
            floats.append(number)
            float_records[label].append(record)
    data["dyadic_reconstruction"] = {"U": U, "V": V,
                                      "common_numerators_U": nums_U,
                                      "common_numerators_V": nums_V,
                                      "construction_integers": intermediate,
                                      "binary64": float_records}
    modes, by_frequency = [], {}
    max_integer = max(abs(x) for x in intermediate.values())
    for label, initial_k, initial_nums, initial_floats in (
            ("low", (1, 0, 0), nums_U, tuple(float_U)),
            ("high", (2, 3, 5), nums_V, tuple(float_V))):
        k, nums, floats = initial_k, initial_nums, initial_floats
        for cycle in range(3):
            for polarity in (1, -1):
                frequency = tuple(polarity * x for x in k)
                require(frequency not in by_frequency, "duplicate carrier")
                partial, floating_partial, terms, sums = 0, 0.0, [], []
                for component in range(3):
                    term = frequency[component] * nums[component]
                    partial += term
                    max_integer = max(max_integer, abs(nums[component]),
                                      abs(term), abs(partial))
                    require(max_integer <= INT_LIMIT, "dot intermediate exceeds 2**53")
                    floating_term = frequency[component] * floats[component]
                    require(F(*floating_term.as_integer_ratio()) == F(term, DEN),
                            "binary64 dot product term rounded")
                    floating_partial += floating_term
                    require(F(*floating_partial.as_integer_ratio()) == F(partial, DEN),
                            "binary64 left-to-right partial sum rounded")
                    terms.append(term)
                    sums.append(partial)
                require(partial == 0 and floating_partial == 0.0, "nonzero divergence")
                entry = {"family": label, "cycle": cycle, "polarity": polarity,
                         "frequency": frequency, "common_numerators": nums,
                         "coefficients": tuple(F(x, DEN) for x in nums),
                         "float_hex": tuple(x.hex() for x in floats),
                         "dot_product_integer_terms": terms,
                         "dot_product_integer_partial_sums": sums,
                         "dot_product_float_hex": floating_partial.hex()}
                modes.append(entry)
                by_frequency[frequency] = nums
            k, nums, floats = rotate(k), rotate(nums), rotate(floats)
    require(len(modes) == 12 and (0, 0, 0) not in by_frequency, "carrier count/mean")
    for k, nums in by_frequency.items():
        require(by_frequency[tuple(-x for x in k)] == nums, "real conjugacy")
        require(by_frequency[rotate(k)] == rotate(nums), "C3 covariance")
    data["twelve_modes"] = modes
    data["integer_exactness"] = {"checked_limit": INT_LIMIT,
                                 "maximum_absolute_checked_integer": max_integer,
                                 "domain": "dyadic reconstruction and all twelve dot sums"}

    U_intervals = ((F(0), F(0)), (F(1), F(1)), intervals["alpha"])
    V_intervals = tuple(intervals[name] for name in ("V1", "V2", "V3"))
    eU = tuple(max(abs(x - actual) for x in interval)
               for interval, actual in zip(U_intervals, U))
    eV = tuple(max(abs(x - actual) for x in interval)
               for interval, actual in zip(V_intervals, V))
    sumU, sumV = sum(eU, F(0)), sum(eV, F(0))
    data["initial_error_upper_bounds"] = {
        "coordinate_eU": eU, "coordinate_eV": eV, "eU": sumU, "eV": sumV,
        "A0": 6 * (sumU + sumV), "L2_normalized": 3 * (sumU + sumV),
        "homogeneous_H3_normalized": 3 * (sumU + 266 * sumV),
        "H3_definition": "sqrt(sum_k |k|**6 * |f_k|**2); homogeneous",
        "unnormalized_L2_and_H3_conversion": "multiply each bound by (2*pi)**(3/2)",
        "meaning": "certified upper bounds, not actual errors"}
    squares_U = tuple(square_interval(x) for x in U_intervals)
    squares_V = tuple(square_interval(x) for x in V_intervals)
    M2 = tuple(6 * sum((x[end] for x in squares_U + squares_V), F(0))
               for end in (0, 1))
    data["original_norm_bounds"] = {
        "M_squared_interval_normalized": M2,
        "energy_interval_normalized": tuple(x / 2 for x in M2),
        "A0_upper": 6 * (sum(map(max_abs, U_intervals), F(0))
                         + sum(map(max_abs, V_intervals), F(0)))}
    Aalpha = max_abs((lo, hi))
    AV = tuple(map(max_abs, V_intervals))
    C = 6 * (1 + Aalpha + 7 * sum(AV, F(0)))
    T, a = 8 / C, 4 / C
    require(C > 0 and C * T == 8 and 2 * a == T, "fixed time identities")
    data["fixed_observation"] = {
        "A_alpha": Aalpha, "A_V_coordinates": AV, "C": C, "T": T, "a": a,
        "C_meaning": "upper bound on original homogeneous A1, not the norm",
        "T_binary64": time_float(T), "a_binary64": time_float(a),
        "node_convention": "exact rational T times exact rational node ratios",
        "scope": "fixed observation endpoints, not a lifespan or source-gate certificate"}


def encode(value, stats):
    stats["scalar_nodes"] += 1
    require(stats["scalar_nodes"] <= MAX_SCALAR_NODES, "serialized node bound")
    if isinstance(value, F):
        bits = max(abs(value.numerator).bit_length(), value.denominator.bit_length())
        stats["maximum_rational_bits"] = max(stats["maximum_rational_bits"], bits)
        require(bits <= MAX_RATIONAL_BITS, "rational bit bound")
        return {"numerator": str(value.numerator), "denominator": str(value.denominator)}
    if isinstance(value, dict):
        return {str(k): encode(v, stats) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v, stats) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--supervisor-pid", required=True, type=int)
    args = parser.parse_args()
    data = {"schema": "annular-input-v1", "status": "FAIL",
            "scientific_execution_count": 0, "scientific_completed": False,
            "source_commit_supplied": args.source_commit,
            "pid": os.getpid(), "supervisor_pid": args.supervisor_pid,
            "science": "same a_* approximation preparation only; no NS integration"}
    try:
        stream = OUTPUT.open("x", encoding="utf-8")
    except FileExistsError:
        print("REFUSED: input-preparation.json already exists; no rerun", file=sys.stderr)
        return 2
    with stream:
        try:
            require(len(args.source_commit) == 40 and all(
                x in "0123456789abcdef" for x in args.source_commit), "commit syntax")
            require(os.getppid() == args.supervisor_pid, "not the designated supervisor child")
            require(sys.float_info.radix == 2 and sys.float_info.mant_dig == 53
                    and sys.float_info.max_exp == 1024, "requires IEEE binary64")
            data["source_bindings"] = {}
            for relative, expected in SOURCES.items():
                actual = sha(ROOT / relative)
                data["source_bindings"][relative] = {"expected": expected, "actual": actual}
                require(actual == expected, "source hash mismatch: " + relative)
            data["source_hashes"] = {name: sha(HERE / name)
                                     for name in ("prepare_input.py", "run_input.py")}
            data["environment"] = {"python": sys.version, "executable": sys.executable,
                                   "uname": tuple(os.uname()), "byteorder": sys.byteorder}
            data["scientific_execution_count"] = 1
            prepare(data)
            data["scientific_completed"] = True
            data["status"] = "INPUT_PREPARATION_PASS_PENDING_INDEPENDENT_VALIDATION"
        except Exception as exc:
            data["error"] = {"type": type(exc).__name__, "message": str(exc)}
        data["child_self_timing"] = {
            "seconds": time.perf_counter() - CHILD_CLOCK_START,
            "scope": "first perf_counter after importing time through before serialization; "
                     "supervisor separately covers child startup, serialization and exit"}
        stats = {"scalar_nodes": 0, "maximum_rational_bits": 0}
        try:
            packed = encode(data, stats)
            packed["serialization_guards"] = dict(stats, maximum_bytes=MAX_OUTPUT_BYTES)
            payload = json.dumps(packed, ensure_ascii=True, indent=2, allow_nan=False) + "\n"
            require(len(payload.encode("utf-8")) <= MAX_OUTPUT_BYTES, "JSON byte bound")
        except Exception as exc:
            data["status"] = "FAIL"
            payload = json.dumps({"schema": "annular-input-v1", "status": "FAIL",
                                  "scientific_execution_count": data["scientific_execution_count"],
                                  "scientific_completed": data["scientific_completed"],
                                  "error": "serialization guard: " + str(exc)}) + "\n"
        stream.write(payload)
        stream.flush()
    return 0 if data["status"].startswith("INPUT_PREPARATION_PASS") else 1


if __name__ == "__main__":
    sys.exit(main())
