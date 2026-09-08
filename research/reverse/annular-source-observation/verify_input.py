#!/usr/bin/env python3
"""Independent input checker. Running requires an explicit authorized-run flag.

No producer module is imported. All scientific work belongs to one supervised
child. Enabling execution requires the final schema adaptation, static review,
source preservation, and the parent's explicit run authorization.
"""

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import struct
import subprocess
import sys
import time
import traceback
from fractions import Fraction


ADAPTER_READY = True
MAX_SECONDS = 5.0
MAX_CHILD_RSS_BYTES = 256 * 1024 * 1024
Q = 36
BISECTIONS = 80
HERE = Path(__file__).resolve().parent
REVERSE = HERE.parent
OUTPUT_PATH = HERE / "verify-input-output.json"
RECEIPT_PATH = HERE / "verifier-execution.json"
PRIMARY_SHA = "3f51705fbd934ce76d503c1c856566405ee3deb1760474b1c73ef6a6f481c61f"
PRIMARY_RECEIPT_SHA = "a1557535b1beec08f1a80e22444e811bff78a4dba91a5ea7adbfe267f3fed13b"
PRIMARY_COMMIT = "c37b516bf668a8b600b084dde91f94b7fe27ddb8"
STATIC_SOURCES = {
    "observation_contract": (
        HERE / "CONTRACT.md",
        "4ae019c3aac7d23a2392273a8cfb52ba08cf5131c35f8bc9e56918dae41c68d8",
    ),
    "input_contract": (
        HERE / "INPUT_CONTRACT.md",
        "2d02549be48f26001c794b06f8d7ecb74e46be3ed051e72019860a56eab6768d",
    ),
    "method": (
        HERE / "VERIFY_METHOD.md",
        "f0798c5d4fa8b798af3c59d8159e150ac6e30950a95a064253f8da3f7d81a3d6",
    ),
    "algebra_A": (
        REVERSE / "cyclic-six-carrier" / "ALGEBRA_A.md",
        "a5dad046a56e3f6d6a9a417304635c23c9e84871528baffbfd5dbedf6cfea32b",
    ),
    "algebra_B": (
        REVERSE / "cyclic-six-carrier" / "ALGEBRA_B.md",
        "2321cea6a0b066e5356b98c22198bf389180e4a53181c4e5bb3ab9825093c499",
    ),
    # Byte provenance only: producer source is never parsed or imported.
    "producer_source": (
        HERE / "prepare_input.py",
        "7010b49e1d13693a963963824d2c6b00ada707b197e899806a719fc4f4dc5cf1",
    ),
    "producer_supervisor": (
        HERE / "run_input.py",
        "ee83bb8f6c0ce50aae9e45553ce7e9e59d84bb641aed5b3fd9ed9c080c74f028",
    ),
}


class VerificationFailure(Exception):
    pass


def need(condition, message):
    if not condition:
        raise VerificationFailure(message)


def equal(actual, expected, label):
    need(actual == expected, "mismatch: " + label)


def integer(value, label):
    if type(value) is int:
        return value
    if isinstance(value, str):
        try:
            result = int(value)
        except ValueError as exc:
            raise VerificationFailure("invalid integer: " + label) from exc
        need(str(result) == value, "noncanonical integer: " + label)
        return result
    raise VerificationFailure("integer type required: " + label)


def rational(value, label):
    need(isinstance(value, dict), "fraction object required: " + label)
    need(set(value) == {"numerator", "denominator"},
         "fraction keys: " + label)
    n = integer(value["numerator"], label + ".numerator")
    d = integer(value["denominator"], label + ".denominator")
    need(d > 0, "positive denominator required: " + label)
    need(math.gcd(abs(n), d) == 1, "fraction not reduced: " + label)
    return Fraction(n, d)


def qlist(value, label, length=None):
    need(isinstance(value, list), "list required: " + label)
    if length is not None:
        equal(len(value), length, label + ".length")
    return [rational(x, label + "[" + str(i) + "]")
            for i, x in enumerate(value)]


def ilist(value, label, length=None):
    need(isinstance(value, list), "integer list required: " + label)
    if length is not None:
        equal(len(value), length, label + ".length")
    return [integer(x, label + "[" + str(i) + "]")
            for i, x in enumerate(value)]


def interval(value, label):
    result = qlist(value, label, 2)
    need(result[0] <= result[1], "reversed interval: " + label)
    return result


def json_value(value):
    if isinstance(value, Fraction):
        return {"numerator": str(value.numerator),
                "denominator": str(value.denominator)}
    if isinstance(value, dict):
        return {str(k): json_value(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [json_value(v) for v in value]
    return value


def exclusive_json(path, payload):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(json_value(payload), stream, ensure_ascii=False,
                  indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def fingerprint(path):
    data = path.read_bytes()
    return {"path": str(path), "sha256": hashlib.sha256(data).hexdigest(),
            "bytes": len(data)}


def valid_sha(value, label):
    need(isinstance(value, str) and len(value) == 64
         and all(c in "0123456789abcdef" for c in value),
         "invalid SHA-256: " + label)
    return value


def local_input_path(value, label):
    path = Path(value).resolve()
    need(path.parent == HERE, "input outside observation directory: " + label)
    need(path not in {OUTPUT_PATH, RECEIPT_PATH, Path(__file__).resolve()},
         "input/output alias: " + label)
    return path


def source_snapshot(args):
    equal(args.input_sha, PRIMARY_SHA, "fixed primary SHA")
    equal(args.producer_receipt_sha, PRIMARY_RECEIPT_SHA, "fixed receipt SHA")
    equal(local_input_path(args.input, "input"), HERE / "input-preparation.json",
          "fixed primary path")
    equal(local_input_path(args.producer_receipt, "receipt"),
          HERE / "input-execution.json", "fixed primary receipt path")
    paths = dict(STATIC_SOURCES)
    paths["verifier_source"] = (Path(__file__).resolve(), args.source_sha)
    paths["adaptation"] = (HERE / "VERIFY_ADAPTATION.md", args.adaptation_sha)
    paths["primary_output"] = (
        local_input_path(args.input, "input"), args.input_sha)
    paths["primary_execution"] = (
        local_input_path(args.producer_receipt, "producer receipt"),
        args.producer_receipt_sha)
    records = {}
    for name, (path, expected) in paths.items():
        valid_sha(expected, name)
        record = fingerprint(path)
        equal(record["sha256"], expected, "source hash " + name)
        records[name] = record
    return records


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key: " + key)
        result[key] = value
    return result


def reject_json_constant(value):
    raise VerificationFailure("nonfinite JSON number: " + value)


def read_json(path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream, object_pairs_hook=unique_object,
                         parse_constant=reject_json_constant)


def source_polynomials():
    # Direct transcription from CA.5 and CB.3, not from producer output.
    p = [
        Fraction(12379608041588, 607290075),
        Fraction(129169813631527, 1012150125),
        Fraction(111813118362046, 337383375),
        Fraction(1377133612024132, 3036450375),
        Fraction(207263796033514, 607290075),
        Fraction(401161881122159, 3036450375),
        Fraction(4124532235492, 202430025),
    ]
    r = [
        Fraction(1807613971, 12393675),
        Fraction(9523582624, 20656125),
        Fraction(27816146846, 61968375),
        Fraction(196585982, 1770525),
    ]
    s = [
        Fraction(536919079, 2699067),
        Fraction(9469267576, 13495335),
        Fraction(10524885968, 13495335),
        Fraction(646271818, 2699067),
    ]
    return {
        "P": p, "r": r, "s": s,
        "v": [-x for x in s], "w": list(r),
        "V1": [-3 * x + 5 * y for x, y in zip(s, r)],
        "V2": [2 * x for x in s],
        "V3": [-2 * x for x in r],
    }


def integer_polynomial(coefficients):
    denominator = 1
    for q in coefficients:
        denominator = denominator // math.gcd(denominator, q.denominator) \
            * q.denominator
    values = [q.numerator * (denominator // q.denominator)
              for q in coefficients]
    return denominator, values


def homogeneous_value(coefficients, x):
    denominator, values = integer_polynomial(coefficients)
    n, d = x.numerator, x.denominator
    degree = len(values) - 1
    terms = [value * pow(n, j) * pow(d, degree - j)
             for j, value in enumerate(values)]
    total = sum(terms)
    return Fraction(total, denominator * pow(d, degree)), {
        "clearing_denominator": denominator,
        "integer_coefficients_ascending": values,
        "point_numerator": n, "point_denominator": d,
        "homogeneous_terms": terms, "homogeneous_integer": total,
        "sign": (total > 0) - (total < 0),
    }


def bisect_independently(p):
    initial = [Fraction(-75, 32), Fraction(-125, 64)]
    lo, hi = initial
    flo, elo = homogeneous_value(p, lo)
    fhi, ehi = homogeneous_value(p, hi)
    need(flo * fhi < 0, "original endpoints not nonzero opposite signs")
    initial_values = [flo, fhi]
    steps = []
    exact = None
    for index in range(1, BISECTIONS + 1):
        before = [lo, hi]
        midpoint = (lo + hi) / 2
        fm, witness = homogeneous_value(p, midpoint)
        if fm == 0:
            branch = "exact_root_point"
            lo = hi = midpoint
            flo = fhi = Fraction(0)
            exact = midpoint
        elif flo * fm < 0:
            branch = "left_half"
            hi, fhi = midpoint, fm
        else:
            need(fm * fhi < 0, "independent sign branch contradiction")
            branch = "right_half"
            lo, flo = midpoint, fm
        steps.append({
            "step": index, "before": before, "midpoint": midpoint,
            "P_midpoint": fm, "branch": branch, "after": [lo, hi],
            "integer_witness": witness,
        })
        need(initial[0] <= lo <= hi <= initial[1], "interval escaped")
        if exact is not None:
            break
    if exact is None:
        equal(len(steps), BISECTIONS, "mandatory midpoint count")
        equal(hi - lo, (initial[1] - initial[0]) / (1 << BISECTIONS),
              "80-step width")
        need(flo * fhi < 0, "final interval lost sign change")
    else:
        equal(lo, hi, "exact-root point interval")
    return {
        "initial": initial, "initial_values": initial_values,
        "initial_integer_witnesses": [elo, ehi],
        "steps": steps, "exact": exact, "final": [lo, hi],
        "final_values": [flo, fhi],
    }


def verify_root(record, expected):
    equal(interval(record["initial_half_open_interval"], "root.initial"),
          expected["initial"], "initial interval")
    equal(qlist(record["initial_endpoint_values"], "root.initial_values", 2),
          expected["initial_values"], "initial endpoint values")
    equal(integer(record["maximum_bisections"], "maximum_bisections"),
          BISECTIONS, "bisection budget")
    steps = record["steps"]
    need(isinstance(steps, list), "root steps list required")
    equal(len(steps), len(expected["steps"]), "complete trace length")
    for got, want in zip(steps, expected["steps"]):
        label = "root.step." + str(want["step"])
        equal(integer(got["step"], label), want["step"], label + ".number")
        for key in ("before", "after"):
            equal(interval(got[key], label + "." + key), want[key],
                  label + "." + key)
        for key in ("midpoint", "P_midpoint"):
            equal(rational(got[key], label + "." + key), want[key],
                  label + "." + key)
        equal(got["branch"], want["branch"], label + ".branch")
    equal(integer(record["completed_bisections"], "completed_bisections"),
          len(expected["steps"]), "completed midpoint count")
    if expected["exact"] is None:
        equal(record["exact_root_point"], None, "exact root absence")
    else:
        equal(rational(record["exact_root_point"], "exact_root_point"),
              expected["exact"], "exact root point")
    equal(interval(record["final_closed_interval"], "root.final"),
          expected["final"], "final interval")
    equal(qlist(record["final_endpoint_values"], "root.final_values", 2),
          expected["final_values"], "final endpoint values")
    # stop_reason spelling is checked by the final metadata adapter.


def qmultiply(a, b):
    return Fraction(a.numerator * b.numerator,
                    a.denominator * b.denominator)


def qadd(a, b):
    return Fraction(a.numerator * b.denominator
                    + b.numerator * a.denominator,
                    a.denominator * b.denominator)


def qless(a, b):
    return a.numerator * b.denominator < b.numerator * a.denominator


def four_extrema(values):
    need(len(values) == 4, "four endpoint products required")
    lower = upper = values[0]
    for value in values[1:]:
        if qless(value, lower):
            lower = value
        if qless(upper, value):
            upper = value
    return lower, upper


def interval_horner(coefficients, domain):
    current = [coefficients[-1], coefficients[-1]]
    trace = [{"coefficient_index": len(coefficients) - 1,
              "interval": list(current)}]
    for index in range(len(coefficients) - 2, -1, -1):
        products = [qmultiply(x, y) for x in current for y in domain]
        lower, upper = four_extrema(products)
        current = [qadd(lower, coefficients[index]),
                   qadd(upper, coefficients[index])]
        trace.append({
            "coefficient_index": index, "four_products": products,
            "interval": list(current),
        })
    return current, trace


def same_multiset(left, right, label):
    remaining = list(right)
    for item in left:
        need(item in remaining, "wrong endpoint product: " + label)
        remaining.remove(item)
    need(not remaining, "missing endpoint products: " + label)


def verify_horner(got, expected, label):
    need(isinstance(got, list), "Horner trace required: " + label)
    equal(len(got), len(expected), label + ".length")
    for index, (row, want) in enumerate(zip(got, expected)):
        equal(integer(row["coefficient_index"], label + ".index"),
              want["coefficient_index"], label + ".index")
        equal(interval(row["interval"], label + ".interval"),
              want["interval"], label + ".interval")
        if index:
            products = qlist(row["four_products"], label + ".products", 4)
            same_multiset(products, want["four_products"], label)


def nearest_dyadic(x):
    n, d = x.numerator, x.denominator
    scaled_n = (1 << Q) * n
    floor, remainder = divmod(scaled_n, d)
    need(0 <= remainder < d, "Euclidean remainder range")
    twice = 2 * remainder
    if twice < d:
        rounded_n = floor
    elif twice > d:
        rounded_n = floor + 1
    else:
        rounded_n = floor if floor % 2 == 0 else floor + 1
    distance_n = abs(scaled_n - rounded_n * d)
    need(2 * distance_n <= d, "nearest integer distance")
    if 2 * distance_n == d:
        need(rounded_n % 2 == 0, "tie not even")
    rounded = Fraction(rounded_n, 1 << Q)
    return {
        "exact_midpoint_value": x, "scaled_floor": floor,
        "independent_remainder": remainder,
        "independent_remainder_denominator": d,
        "remainder_fraction": Fraction(remainder, d),
        "tie": twice == d, "rounded_numerator": rounded_n,
        "rounded": rounded, "absolute_midpoint_rounding_error": abs(x - rounded),
        "integer_distance_numerator": distance_n,
        "twice_distance": 2 * distance_n, "distance_denominator": d,
    }


def verify_rounding(record, expected, label):
    for key in ("exact_midpoint_value", "rounded",
                "absolute_midpoint_rounding_error"):
        equal(rational(record[key], label + "." + key), expected[key],
              label + "." + key)
    for key in ("scaled_floor", "rounded_numerator"):
        equal(integer(record[key], label + "." + key), expected[key],
              label + "." + key)
    need(type(record["tie"]) is bool, "tie flag must be boolean")
    equal(record["tie"], expected["tie"], label + ".tie")
    r = integer(record["remainder"], label + ".remainder")
    d = integer(record["remainder_denominator"], label + ".remainder_denominator")
    need(d > 0 and 0 <= r < d, "reported remainder range: " + label)
    # Reduction of the scaled rational can change these two integers.
    equal(Fraction(r, d), expected["remainder_fraction"],
          label + ".remainder value")


def ratio_from_bits(bits):
    sign = -1 if bits >> 63 else 1
    exponent = (bits >> 52) & 0x7ff
    fraction = bits & ((1 << 52) - 1)
    need(exponent != 0x7ff, "nonfinite binary64")
    if exponent == 0:
        significand, power = fraction, -1074
    else:
        significand, power = (1 << 52) + fraction, exponent - 1023 - 52
    numerator = sign * significand
    if power >= 0:
        return Fraction(numerator * (1 << power), 1)
    return Fraction(numerator, 1 << (-power))


def decode_hex(text, label):
    need(isinstance(text, str), "float hex string required: " + label)
    try:
        value = float.fromhex(text)
    except (ValueError, OverflowError) as exc:
        raise VerificationFailure("invalid binary64 hex: " + label) from exc
    bits = struct.unpack(">Q", struct.pack(">d", value))[0]
    exact = ratio_from_bits(bits)
    equal(Fraction(*value.as_integer_ratio()), exact,
          label + ".independent bit decode")
    return exact, bits


def check_exact_hex(text, expected, label):
    value, bits = decode_hex(text, label)
    equal(value, expected, label + ".exact dyadic value")
    if expected == 0:
        need(bits >> 63 == 0, "negative zero instead of rational cast: " + label)
    return {"float_hex": text, "exact_ratio": value, "bits": str(bits),
            "conversion_error": Fraction(0)}


def check_float_record(record, expected, label):
    equal(rational(record["rational"], label + ".rational"), expected,
          label + ".rational")
    witness = check_exact_hex(record["float_hex"], expected, label)
    equal(rational(record["float_ratio"], label + ".float_ratio"), expected,
          label + ".float_ratio")
    return witness


def check_time_float(record, exact, label):
    equal(rational(record["exact"], label + ".exact"), exact, label + ".exact")
    value, bits = decode_hex(record["float_hex"], label)
    need(exact > 0 and bits >> 63 == 0, "positive time conversion required")
    previous = ratio_from_bits(bits - 1) if bits else -Fraction(1, 1 << 1074)
    if bits == 0x7fefffffffffffff:
        following = Fraction(1 << 1024)
    else:
        following = ratio_from_bits(bits + 1)
    lower, upper = (previous + value) / 2, (value + following) / 2
    even = (bits & 1) == 0
    need((lower < exact < upper)
         or (even and exact in (lower, upper)),
         "not correctly rounded nearest-even binary64: " + label)
    equal(rational(record["float_ratio"], label + ".float_ratio"), value,
          label + ".float_ratio")
    signed = value - exact
    equal(rational(record["signed_conversion_error"], label + ".signed_error"),
          signed, label + ".signed_error")
    equal(rational(record["absolute_conversion_error"], label + ".abs_error"),
          abs(signed), label + ".abs_error")
    return {"float_hex": record["float_hex"], "float_ratio": value,
            "signed_conversion_error": signed,
            "absolute_conversion_error": abs(signed),
            "nearest_cell": [lower, upper], "even_low_bit": even}


def rotate(vector, count):
    result = list(vector)
    for _ in range(count):
        result = [result[2], result[0], result[1]]
    return result


def reconstruct(roundings):
    denominator = 1 << Q
    A = roundings["alpha"]["rounded_numerator"]
    Vn = roundings["v"]["rounded_numerator"]
    Wn = roundings["w"]["rounded_numerator"]
    construction = {
        "A": A, "Vn": Vn, "Wn": Wn, "denominator": denominator,
        "3Vn": 3 * Vn, "5Wn": 5 * Wn, "3Vn+5Wn": 3 * Vn + 5 * Wn,
        "-2Vn": -2 * Vn, "-2Wn": -2 * Wn,
    }
    nums_u = [0, denominator, A]
    nums_v = [construction["3Vn+5Wn"], -2 * Vn, -2 * Wn]
    modes = []
    all_integers = list(construction.values()) + nums_u + nums_v
    for family, base_frequency, base_nums in (
            ("low", [1, 0, 0], nums_u),
            ("high", [2, 3, 5], nums_v)):
        for cycle in range(3):
            positive = rotate(base_frequency, cycle)
            nums = rotate(base_nums, cycle)
            for polarity in (1, -1):
                frequency = [polarity * x for x in positive]
                terms = [k * n for k, n in zip(frequency, nums)]
                partials = []
                current = 0
                for term in terms:
                    current += term
                    partials.append(current)
                need(current == 0, "independent integer incompressibility")
                all_integers.extend(terms + partials + nums)
                modes.append({
                    "family": family, "cycle": cycle, "polarity": polarity,
                    "frequency": frequency, "common_numerators": nums,
                    "coefficients": [Fraction(n, denominator) for n in nums],
                    "dot_product_integer_terms": terms,
                    "dot_product_integer_partial_sums": partials,
                })
    maximum = max(abs(n) for n in all_integers)
    need(maximum <= (1 << 53), "53-bit integer bound failed")
    return {
        "denominator": denominator, "construction": construction,
        "nums_U": nums_u, "nums_V": nums_v,
        "U": [Fraction(n, denominator) for n in nums_u],
        "V": [Fraction(n, denominator) for n in nums_v],
        "modes": modes, "maximum_integer": maximum,
        "all_checked_integers": all_integers,
    }


def verify_reconstruction(primary, expected):
    rec = primary["dyadic_reconstruction"]
    equal(qlist(rec["U"], "U", 3), expected["U"], "U")
    equal(qlist(rec["V"], "V", 3), expected["V"], "V")
    for name in ("U", "V"):
        equal(ilist(rec["common_numerators_" + name], "numerators " + name, 3),
              expected["nums_" + name], "common numerators " + name)
    for name, number in expected["construction"].items():
        equal(integer(rec["construction_integers"][name], "construction." + name),
              number, "construction." + name)
    floats = {"U": [], "V": []}
    for name in ("U", "V"):
        need(isinstance(rec["binary64"][name], list), "binary64 vector required")
        equal(len(rec["binary64"][name]), 3, "binary64 vector length")
        for j in range(3):
            floats[name].append(check_float_record(
                rec["binary64"][name][j], expected[name][j],
                "binary64." + name + "." + str(j)))
    rows = primary["twelve_modes"]
    need(isinstance(rows, list), "twelve_modes list required")
    equal(len(rows), 12, "complete twelve-mode count")
    keyed = {}
    for row in rows:
        key = (row["family"], integer(row["cycle"], "cycle"),
               integer(row["polarity"], "polarity"))
        need(key not in keyed, "duplicate mode label")
        keyed[key] = row
    mode_witnesses = []
    for want in expected["modes"]:
        key = (want["family"], want["cycle"], want["polarity"])
        need(key in keyed, "missing mode")
        row = keyed[key]
        for field in ("frequency", "common_numerators",
                      "dot_product_integer_terms",
                      "dot_product_integer_partial_sums"):
            equal(ilist(row[field], str(key) + "." + field, 3),
                  want[field], str(key) + "." + field)
        equal(qlist(row["coefficients"], str(key) + ".coefficients", 3),
              want["coefficients"], str(key) + ".coefficients")
        need(isinstance(row["float_hex"], list), "mode float_hex list")
        equal(len(row["float_hex"]), 3, "mode float count")
        proofs = [check_exact_hex(text, coefficient, str(key) + ".float")
                  for text, coefficient in zip(row["float_hex"],
                                               want["coefficients"])]
        dot, dot_bits = decode_hex(row["dot_product_float_hex"], "mode dot")
        equal(dot, Fraction(0), "floating dot product exact value")
        mode_witnesses.append({"key": list(key), "floats": proofs,
                               "dot_ratio": dot, "dot_bits": str(dot_bits)})
    exactness = primary["integer_exactness"]
    equal(integer(exactness["checked_limit"], "integer limit"), 1 << 53,
          "integer exactness limit")
    equal(integer(exactness["maximum_absolute_checked_integer"], "integer max"),
          expected["maximum_integer"], "maximum checked integer")
    return {"representative_floats": floats, "all_twelve_mode_floats": mode_witnesses}


def absolute_endpoint_max(domain):
    return max(abs(domain[0]), abs(domain[1]))


def square_interval(domain):
    lower, upper = domain
    values = [lower * lower, upper * upper]
    return [Fraction(0) if lower <= 0 <= upper else min(values), max(values)]


def norm_and_error_data(domains, reconstruction):
    u_domains = [[Fraction(0), Fraction(0)],
                 [Fraction(1), Fraction(1)], domains["alpha"]]
    v_domains = [domains["V1"], domains["V2"], domains["V3"]]
    e_u = [max(abs(d[0] - x), abs(d[1] - x))
           for d, x in zip(u_domains, reconstruction["U"])]
    e_v = [max(abs(d[0] - x), abs(d[1] - x))
           for d, x in zip(v_domains, reconstruction["V"])]
    sum_u, sum_v = sum(e_u), sum(e_v)
    squares = [square_interval(d) for d in u_domains + v_domains]
    m2 = [6 * sum(d[side] for d in squares) for side in (0, 1)]
    energy = [x / 2 for x in m2]
    a0 = 6 * sum(absolute_endpoint_max(d) for d in u_domains + v_domains)
    return {
        "coordinate_eU": e_u, "coordinate_eV": e_v,
        "eU": sum_u, "eV": sum_v, "A0": 6 * (sum_u + sum_v),
        "L2_normalized": 3 * (sum_u + sum_v),
        "homogeneous_H3_normalized": 3 * (sum_u + 266 * sum_v),
        "U_coordinate_intervals": u_domains, "V_coordinate_intervals": v_domains,
        "coordinate_square_intervals": squares,
        "M_squared_interval_normalized": m2,
        "energy_interval_normalized": energy, "A0_upper": a0,
    }


def verify_errors_and_norms(primary, expected):
    errors = primary["initial_error_upper_bounds"]
    for name in ("coordinate_eU", "coordinate_eV"):
        equal(qlist(errors[name], name, 3), expected[name], name)
    for name in ("eU", "eV", "A0", "L2_normalized", "homogeneous_H3_normalized"):
        equal(rational(errors[name], name), expected[name], name)
    norms = primary["original_norm_bounds"]
    for name in ("M_squared_interval_normalized", "energy_interval_normalized"):
        equal(interval(norms[name], name), expected[name], name)
    equal(rational(norms["A0_upper"], "original A0 upper"),
          expected["A0_upper"], "original A0 upper")


def observation_data(domains):
    alpha = absolute_endpoint_max(domains["alpha"])
    v_max = [absolute_endpoint_max(domains[name]) for name in ("V1", "V2", "V3")]
    C = 6 * (1 + alpha + 7 * sum(v_max))
    need(C > 0, "C must be positive")
    T = 8 / C
    return {"A_alpha": alpha, "A_V_coordinates": v_max, "C": C, "T": T, "a": T / 2}


def verify_observation(record, expected):
    for name in ("A_alpha", "C", "T", "a"):
        equal(rational(record[name], "observation." + name), expected[name],
              "observation." + name)
    equal(qlist(record["A_V_coordinates"], "A_V_coordinates", 3),
          expected["A_V_coordinates"], "A_V_coordinates")
    return {
        "T_binary64": check_time_float(record["T_binary64"], expected["T"], "T"),
        "a_binary64": check_time_float(record["a_binary64"], expected["a"], "a"),
    }


def validate_primary_metadata(primary, producer_receipt, root, sources):
    need(ADAPTER_READY, "primary metadata adapter is not finalized")
    equal(primary["schema"], "annular-input-v1", "primary schema")
    equal(primary["status"], "INPUT_PREPARATION_PASS_PENDING_INDEPENDENT_VALIDATION",
          "historical primary status")
    equal(integer(primary["scientific_execution_count"], "primary count"), 1,
          "primary count")
    need(primary["scientific_completed"] is True, "primary completion absent")
    equal(primary["source_commit_supplied"], PRIMARY_COMMIT, "primary commit label")
    equal(primary["science"],
          "same a_* approximation preparation only; no NS integration",
          "primary scientific scope")
    # This adapter targets the stopped, non-exact-root, 80-step original record.
    need(root["exact"] is None and len(root["steps"]) == BISECTIONS,
         "independent classification differs from this stopped record")
    equal(primary["root_isolation"]["stop_reason"], "exactly_80_bisections",
          "actual stop reason")
    equal(primary["root_isolation"]["single_root_uniqueness"],
          "inherited from CB.8, not recomputed", "root uniqueness scope")
    equal(primary["rounding"]["rule"], "nearest; ties to even", "rounding rule")
    equal(primary["integer_exactness"]["domain"],
          "dyadic reconstruction and all twelve dot sums", "integer scope")
    errors = primary["initial_error_upper_bounds"]
    equal(errors["H3_definition"],
          "sqrt(sum_k |k|**6 * |f_k|**2); homogeneous", "H3 definition")
    equal(errors["unnormalized_L2_and_H3_conversion"],
          "multiply each bound by (2*pi)**(3/2)", "H3 conversion")
    equal(errors["meaning"], "certified upper bounds, not actual errors",
          "error bound meaning")
    fixed = primary["fixed_observation"]
    equal(fixed["C_meaning"],
          "upper bound on original homogeneous A1, not the norm", "C meaning")
    equal(fixed["node_convention"],
          "exact rational T times exact rational node ratios", "time convention")
    equal(fixed["scope"],
          "fixed observation endpoints, not a lifespan or source-gate certificate",
          "time scope")
    binding_names = {
        "research/reverse/annular-source-observation/CONTRACT.md":
            "observation_contract",
        "research/reverse/annular-source-observation/INPUT_CONTRACT.md":
            "input_contract",
        "research/reverse/cyclic-six-carrier/ALGEBRA_A.md": "algebra_A",
        "research/reverse/cyclic-six-carrier/ALGEBRA_B.md": "algebra_B",
    }
    equal(set(primary["source_bindings"]), set(binding_names), "source binding set")
    for relative, name in binding_names.items():
        rec = primary["source_bindings"][relative]
        equal(rec["expected"], sources[name]["sha256"], relative + ".expected")
        equal(rec["actual"], sources[name]["sha256"], relative + ".actual")
    producer_hashes = {
        "prepare_input.py": sources["producer_source"]["sha256"],
        "run_input.py": sources["producer_supervisor"]["sha256"],
    }
    equal(primary["source_hashes"], producer_hashes, "producer byte hashes")
    rec = producer_receipt
    equal(rec["schema"], "annular-input-execution-v1", "receipt schema")
    equal(rec["status"], "EXECUTION_PASS_PENDING_INDEPENDENT_INPUT_VALIDATION",
          "historical execution status")
    equal(rec["source_commit_supplied"], PRIMARY_COMMIT, "receipt commit label")
    for key in ("supervisor_count", "scientific_subprocess_launch_attempts",
                "scientific_subprocess_launch_count",
                "child_reported_scientific_execution_count"):
        equal(integer(rec[key], key), 1, key)
    need(rec["child_reported_scientific_completed"] is True,
         "receipt child completion absent")
    equal(rec["child_status"], primary["status"], "receipt child status")
    equal(rec["source_hashes_before_launch"], producer_hashes, "receipt source hashes")
    equal(rec["output_sha256"], sources["primary_output"]["sha256"],
          "receipt output SHA")
    equal(integer(rec["output_bytes"], "receipt output bytes"),
          sources["primary_output"]["bytes"], "receipt output bytes")
    equal(integer(primary["supervisor_pid"], "primary supervisor pid"),
          integer(rec["supervisor_pid"], "receipt supervisor pid"),
          "producer supervisor identity")
    equal(rec["environment"]["uname"][0], "Darwin", "producer OS")
    equal(rec["environment"]["rss_raw_unit"], "bytes", "producer RSS unit")
    for key in ("python", "executable", "uname"):
        equal(rec["environment"][key], primary["environment"][key],
              "producer environment." + key)
    expected_command = [
        primary["environment"]["executable"], str(HERE / "prepare_input.py"),
        "--source-commit", PRIMARY_COMMIT, "--supervisor-pid",
        str(integer(rec["supervisor_pid"], "supervisor pid")),
    ]
    equal(rec["command"], expected_command, "producer command identity")
    lifecycle = rec["child_lifecycle"]
    equal(integer(lifecycle["pid"], "recorded child pid"),
          integer(primary["pid"], "primary pid"), "producer child identity")
    equal(integer(lifecycle["returncode"], "producer returncode"), 0,
          "producer returncode")
    need(lifecycle["timed_out"] is False, "producer timed out")
    equal(lifecycle["communication_error"], None, "producer communication error")
    equal(lifecycle["wall_scope"], "immediately before Popen through after wait",
          "producer wall boundary")
    equal(lifecycle["rss_scope"], "RUSAGE_CHILDREN after sole child was reaped",
          "producer RSS boundary")
    limits = rec["limits"]
    equal(limits["child_lifecycle_wall_seconds"], MAX_SECONDS, "producer wall limit")
    equal(integer(limits["child_peak_rss_bytes"], "producer RSS limit"),
          MAX_CHILD_RSS_BYTES, "producer RSS limit")
    wall = lifecycle["wall_seconds"]
    need(type(wall) in (int, float) and math.isfinite(wall)
         and 0 <= wall <= MAX_SECONDS, "recorded producer wall budget")
    for key in ("user_seconds", "system_seconds", "maximum_rss_raw"):
        equal(lifecycle["usage_before"][key], 0, "fresh producer child accounting")
    rss = integer(lifecycle["peak_rss_bytes"], "producer RSS")
    need(0 < rss <= MAX_CHILD_RSS_BYTES, "recorded producer RSS budget")
    equal(integer(lifecycle["peak_rss_raw"], "producer raw RSS"), rss,
          "producer RSS raw conversion")
    equal(lifecycle["peak_rss_raw_unit"], "bytes", "producer RSS bytes")
    equal(integer(lifecycle["usage_after_wait"]["maximum_rss_raw"], "after RSS"),
          rss, "producer after-wait RSS")
    need(lifecycle["within_wall_limit"] is True
         and lifecycle["within_rss_limit"] is True, "producer budget flags")
    for key in ("cpu_user_seconds", "cpu_system_seconds"):
        value = lifecycle[key]
        need(type(value) in (int, float) and math.isfinite(value) and value >= 0,
             "invalid recorded CPU metadata")
    equal(lifecycle["cpu_user_seconds"], lifecycle["usage_after_wait"]["user_seconds"],
          "producer user CPU accounting")
    equal(lifecycle["cpu_system_seconds"], lifecycle["usage_after_wait"]["system_seconds"],
          "producer system CPU accounting")
    need(sources["primary_output"]["bytes"] <= 1048576, "primary byte limit")
    equal(integer(primary["serialization_guards"]["maximum_bytes"], "byte guard"),
          1048576, "producer byte guard")
    return {
        "source_and_output_bindings_checked": True,
        "producer_recorded_lifecycle_wall_seconds": wall,
        "producer_recorded_child_RSS_bytes": rss,
        "resource_scope": (
            "Consistency of stopped primary records and byte bindings only; "
            "not a new measurement of the producer run or a reread of its core."
        ),
        "historical_pending_status_preserved": True,
        "adapter_scope": "stopped annular-input-v1 nonexact 80-step record",
        "display_decimals_used_for_science": False,
        "serialization_scalar_count_and_max_bits_recomputed": False,
        "serialization_scope": (
            "Reported scalar_nodes and maximum_rational_bits are not used as "
            "mathematical evidence; the actual file byte bound is checked."
        ),
    }


def verify_mathematics(primary):
    polynomials = source_polynomials()
    got_polys = primary["polynomials_ascending"]
    for name, coefficients in polynomials.items():
        equal(qlist(got_polys[name], "polynomial." + name), coefficients,
              "original polynomial." + name)
    root = bisect_independently(polynomials["P"])
    verify_root(primary["root_isolation"], root)
    domains = {"alpha": root["final"]}
    traces = {}
    for name in ("v", "w", "V1", "V2", "V3"):
        domains[name], traces[name] = interval_horner(
            polynomials[name], root["final"])
        verify_horner(primary["interval_horner_traces"][name], traces[name],
                      "horner." + name)
    for name, domain in domains.items():
        equal(interval(primary["intervals"][name], "intervals." + name),
              domain, "intervals." + name)
    midpoint = sum(root["final"]) / 2
    v_mid, v_mid_witness = homogeneous_value(polynomials["v"], midpoint)
    w_mid, w_mid_witness = homogeneous_value(polynomials["w"], midpoint)
    point_values = {"alpha": midpoint, "v": v_mid, "w": w_mid}
    roundings = {name: nearest_dyadic(value) for name, value in point_values.items()}
    rounding = primary["rounding"]
    equal(integer(rounding["q"], "q"), Q, "fixed q")
    equal(integer(rounding["common_denominator"], "rounding denominator"),
          1 << Q, "rounding denominator")
    for name in ("alpha", "v", "w"):
        verify_rounding(rounding["records"][name], roundings[name], name)
    reconstruction = reconstruct(roundings)
    float_proofs = verify_reconstruction(primary, reconstruction)
    errors = norm_and_error_data(domains, reconstruction)
    verify_errors_and_norms(primary, errors)
    observation = observation_data(domains)
    time_proofs = verify_observation(primary["fixed_observation"], observation)
    return {
        "source_polynomials_ascending": polynomials,
        "root": root, "intervals": domains, "interval_horner_traces": traces,
        "midpoint_integer_witnesses": {"v": v_mid_witness, "w": w_mid_witness},
        "roundings": roundings, "reconstruction": reconstruction,
        "physical_binary64_witnesses": float_proofs,
        "initial_error_and_original_norm_bounds": errors,
        "fixed_observation": observation, "time_conversion_witnesses": time_proofs,
        "verified_categories": [
            "original_P_r_s_and_five_composed_polynomials",
            "all_80_midpoints_or_exact_root_early_stop",
            "all_five_contract_interval_Horner_traces",
            "q36_integer_distance_and_even_ties",
            "all_twelve_modes_and_53_bit_intermediates",
            "all_physical_binary64_values_and_exact_readbacks",
            "three_initial_error_bounds_and_original_norm_intervals",
            "same_C_T_a_and_binary64_time_conversion_errors",
        ],
    }


def worker(args):
    need(args.authorized_run and ADAPTER_READY, "explicit authorized run required")
    need(args.supervisor_pid > 0 and args.supervisor_pid == os.getppid(),
         "worker must be launched by its recorded supervisor")
    need(not OUTPUT_PATH.exists(), "independent output already exists")
    payload = {
        "scientific_execution_count_in_this_invocation": 1,
        "scientific_stage_completed": False, "status": "FAILED",
        "scope": "fixed input verification only; not an NS trajectory certificate",
    }
    code = 1
    try:
        need(sys.version_info >= (3, 9), "Python 3.9 or newer required")
        need(sys.float_info.radix == 2 and sys.float_info.mant_dig == 53
             and sys.float_info.max_exp == 1024, "binary64 environment required")
        sources = source_snapshot(args)
        primary = read_json(Path(args.input))
        producer_receipt = read_json(Path(args.producer_receipt))
        result = verify_mathematics(primary)
        metadata = validate_primary_metadata(primary, producer_receipt,
                                             result["root"], sources)
        final_sources = source_snapshot(args)
        equal(final_sources, sources, "sources changed during verification")
        payload.update({
            "status": "VERIFIED", "scientific_stage_completed": True,
            "sources_before": sources, "sources_after": final_sources,
            "mathematics": result, "primary_metadata_checks": metadata,
            "pid": os.getpid(), "supervisor_pid": args.supervisor_pid,
            "environment": {
                "python": sys.version, "executable": sys.executable,
                "uname": list(os.uname()),
                "scientific_child_processes": 1,
                "scientific_grandchildren": 0,
            },
        })
        code = 0
    except Exception as exc:
        payload["failure"] = {"type": type(exc).__name__, "message": str(exc),
                              "traceback": traceback.format_exc()}
    try:
        exclusive_json(OUTPUT_PATH, payload)
    except Exception:
        traceback.print_exc()
        return 1
    return code


def child_argv(args):
    return [
        sys.executable, str(Path(__file__).resolve()), "--worker", "--authorized-run",
        "--supervisor-pid", str(os.getpid()),
        "--input", args.input, "--input-sha", args.input_sha,
        "--producer-receipt", args.producer_receipt,
        "--producer-receipt-sha", args.producer_receipt_sha,
        "--source-sha", args.source_sha, "--adaptation-sha", args.adaptation_sha,
        "--source-commit", args.source_commit,
    ]


def supervise(args):
    need(args.authorized_run and ADAPTER_READY, "explicit authorized run required")
    equal(args.supervisor_pid, 0, "supervisor entry must not impersonate worker")
    need(sys.platform == "darwin", "Darwin RSS byte convention required")
    need(not OUTPUT_PATH.exists(), "independent output already exists")
    need(not RECEIPT_PATH.exists(), "supervisor receipt already exists")
    before_usage = resource.getrusage(resource.RUSAGE_CHILDREN)
    need(before_usage.ru_utime == 0 and before_usage.ru_stime == 0
         and before_usage.ru_maxrss == 0, "supervisor must have no earlier children")
    sources = source_snapshot(args)
    report = {
        "status": "FAILED", "scientific_child_launch_attempted": False,
        "scientific_execution_count_in_this_invocation": 0,
        "timeout_seconds": MAX_SECONDS, "RSS_limit_bytes": MAX_CHILD_RSS_BYTES,
        "source_commit_parent_supplied_not_git_verified": args.source_commit,
        "sources_before": sources,
        "resource_scope": (
            "One fresh child. Wall: before Popen through communicate/wait return. "
            "Darwin RUSAGE_CHILDREN peak RSS is posthoc child-only measurement; "
            "not a runtime RSS hard limit or parent/whole-task measurement."
        ),
    }
    # Reserve the receipt before the one permitted launch; never overwrite it.
    with RECEIPT_PATH.open("x", encoding="utf-8") as receipt_stream:
        process = None
        started = None
        try:
            argv = child_argv(args)
            report["command_argv"] = argv
            started = time.monotonic()
            report["scientific_child_launch_attempted"] = True
            process = subprocess.Popen(argv, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, text=True)
            report["scientific_execution_count_in_this_invocation"] = 1
            report["child_pid"] = process.pid
            timeout = max(0.0, started + MAX_SECONDS - time.monotonic())
            try:
                stdout, stderr = process.communicate(timeout=timeout)
                report["timed_out"] = False
            except subprocess.TimeoutExpired:
                report["timed_out"] = True
                process.kill()
                stdout, stderr = process.communicate()
            ended = time.monotonic()
            usage = resource.getrusage(resource.RUSAGE_CHILDREN)
            report.update({
                "wall_seconds_Popen_to_wait": ended - started,
                "exit_code": process.returncode, "stdout": stdout, "stderr": stderr,
                "maximum_RSS_CHILDREN_bytes": usage.ru_maxrss,
                "user_CPU_CHILDREN_seconds": usage.ru_utime,
                "system_CPU_CHILDREN_seconds": usage.ru_stime,
            })
            if OUTPUT_PATH.exists():
                report["independent_output"] = fingerprint(OUTPUT_PATH)
                output = read_json(OUTPUT_PATH)
                report["child_reported_status"] = output.get("status")
                complete = (output.get("status") == "VERIFIED"
                            and output.get("scientific_stage_completed") is True
                            and output.get("scientific_execution_count_in_this_invocation") == 1
                            and output.get("pid") == process.pid
                            and output.get("supervisor_pid") == os.getpid())
            else:
                complete = False
                report["independent_output_missing"] = True
            after_sources = source_snapshot(args)
            equal(after_sources, sources, "sources changed across child lifetime")
            report["sources_after"] = after_sources
            wall_ok = report["wall_seconds_Popen_to_wait"] <= MAX_SECONDS
            rss_ok = usage.ru_maxrss <= MAX_CHILD_RSS_BYTES
            report["wall_budget_pass"] = wall_ok
            report["RSS_posthoc_budget_pass"] = rss_ok
            if (not report["timed_out"] and process.returncode == 0
                    and complete and wall_ok and rss_ok):
                report["status"] = "VERIFIED_WITHIN_RESOURCE_BOUNDARY"
        except Exception as exc:
            if process is not None and process.poll() is None:
                process.kill()
                process.communicate()
            if started is not None:
                report["wall_seconds_until_failure_reaped"] = time.monotonic() - started
            usage = resource.getrusage(resource.RUSAGE_CHILDREN)
            report["failure_path_CHILDREN_usage"] = {
                "maximum_RSS_bytes": usage.ru_maxrss,
                "user_CPU_seconds": usage.ru_utime,
                "system_CPU_seconds": usage.ru_stime,
            }
            if process is None and report["scientific_child_launch_attempted"]:
                report["scientific_execution_count_in_this_invocation"] = None
                report["launch_outcome_uncertain"] = True
            report["failure"] = {"type": type(exc).__name__, "message": str(exc)}
        parent_usage = resource.getrusage(resource.RUSAGE_SELF)
        report["supervisor_self_usage_before_receipt_serialization"] = {
            "pid": os.getpid(),
            "user_CPU_seconds": parent_usage.ru_utime,
            "system_CPU_seconds": parent_usage.ru_stime,
            "maximum_RSS_bytes": parent_usage.ru_maxrss,
            "RSS_raw_unit": "Darwin bytes",
            "scope": (
                "Cumulative supervisor SELF usage sampled immediately before "
                "receipt serialization. Excludes later serialization, write, "
                "close and exit; not the full parent lifecycle or a "
                "simultaneous parent-child peak. Never added to child RSS."
            ),
        }
        json.dump(json_value(report), receipt_stream, ensure_ascii=False,
                  indent=2, sort_keys=True, allow_nan=False)
        receipt_stream.write("\n")
    return 0 if report["status"] == "VERIFIED_WITHIN_RESOURCE_BOUNDARY" else 1


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--authorized-run", action="store_true",
                        help="Only the parent may use after final review and preservation.")
    parser.add_argument("--supervisor-pid", type=int, default=0,
                        help=argparse.SUPPRESS)
    parser.add_argument("--input", required=True)
    parser.add_argument("--input-sha", required=True)
    parser.add_argument("--producer-receipt", required=True)
    parser.add_argument("--producer-receipt-sha", required=True)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--adaptation-sha", required=True)
    parser.add_argument("--source-commit", required=True)
    return parser.parse_args()


if __name__ == "__main__":
    try:
        arguments = parse_args()
        sys.exit(worker(arguments) if arguments.worker else supervise(arguments))
    except Exception as error:
        print(type(error).__name__ + ": " + str(error), file=sys.stderr)
        sys.exit(1)
