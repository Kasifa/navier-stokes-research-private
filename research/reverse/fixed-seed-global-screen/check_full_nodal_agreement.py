#!/usr/bin/env python3
"""Compare frozen full-node archives; never integrate, convolve, or decode nodes.

Default only prints usage. --run requires the two frozen run SHA values and
explicit external stdout/stderr files. No trial output is created or modified.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
MAIN = HERE / "full-nodal-residual-trial-01"
INDEP = HERE / "full-nodal-independent-trial-01"
OUTPUT = HERE / "full-nodal-agreement.json"
COUNT, ZERO, QP, P = 35937, 17968, 1 << 96, 1 << 128
TENSORS = ("11", "13", "22", "23", "33")
SOURCE_PINS = {
    "audit_full_nodal_residual.py": "54af5a2eac8be72acacef40f1be73ba00916704d64aef539d4459375a9d18e8c",
    "audit_full_nodal_residual_independent.py": "6b65b6f536d77c544c8803832eadcf37c72568f951a9982edf40e73dbc272fbf",
    "FULL_NODAL_RESIDUAL_CONTRACT.md": "f3c5327e59931a2e638c039078f78175f4138c53eec139cc57c1ae5fd2cb513b",
    "FULL_NODAL_RESIDUAL_INDEPENDENT_REVIEW.md": "5a1341a58a93582b31a56a33d10a296499ed921daa2c5dac7ee9d27369c87ece",
    "FULL_NODAL_EXECUTION_CONTRACT.md": "879deca7e881073dc3fc31506aaf681e7d243d068621092fe361fc60963ae40c",
    "FULL_NODAL_INDEPENDENT_EXECUTION_CONTRACT.md": "61450a286e2f300f4444a29b45fa53fe93ec1b655fab3b4f03afb4261e93307c",
    "FULL_NODAL_EXECUTION_INDEPENDENT_REVIEW.md": "5f1c40039f8de23250ef103c16e2991535dadaa4824c4f05e8cc045c75b55e53",
    "FULL_NODAL_PRIMARY_CODE_REVIEW.md": "a28d49df6c91012f57fe2a086b2b4a4d205698187484685b755514770865e182",
    "FULL_NODAL_INDEPENDENT_CODE_REVIEW.md": "f6185da959f93adcca2ad77de6f66fa52fb063d559023db9e09c10f8f43a56aa",
}
ORIGINAL_PINS = {
    "node-trial-01/manifest.json": "5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd",
    "node-trial-01/modes.npy": "f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896",
    "node-trial-01/block-01280-01343.npz": "abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e",
    "kronecker-independent-agreement.json": "5510285fed346165e428bac4dfcb572548283322937a712be6465829481b5779",
}
MAIN_SPECS = {
    "A.i256le.bin": 4912 * 6 * 32, "J.i256le.bin": 4912 * 6 * 32,
    "V.i512le.bin": COUNT * 6 * 64, "S.u960le.bin": COUNT * 120,
    **{"tensor-" + t + ".i240le.bin": COUNT * 60 for t in TENSORS},
    **{"tensor-" + t + "-product-" + str(i) + ".signed-le.bin": COUNT * 30
       for t in TENSORS for i in range(3)},
}
INDEP_SPECS = {
    **{"tensor" + t + "-direct.i240le.bin": COUNT * 60 for t in TENSORS},
    "residual-hat-fractions.i256-u256le.bin": COUNT * 6 * 64,
}
NORMAL_GATE = {
    "REFUTED_AT_FIXED_NODE": "REFUTED", "CERTIFIED_AT_FIXED_NODE": "NODE_PASS",
    "REFUTED": "REFUTED", "NODE_PASS": "NODE_PASS", "UNDECIDED": "UNDECIDED",
}


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value):
    need(type(value) in (int, str), "integer representation")
    n = int(value)
    need(type(value) is int or str(n) == value, "canonical integer text")
    need(abs(n).bit_length() <= 8192, "small-integer guard")
    return n


def fraction(value):
    if isinstance(value, dict):
        n, d = value["numerator"], value["denominator"]
    else:
        need(isinstance(value, list) and len(value) == 2, "fraction schema")
        n, d = value
    n, d = integer(n), integer(d)
    need(d > 0, "positive fraction denominator")
    return F(n, d)


def pair(value):
    return [str(value.numerator), str(value.denominator)]


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def digest_match(expected, actual):
    need(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected),
         "source/input SHA format")
    need(expected == actual, "source/input SHA mismatch")


def load(path):
    return json.loads(path.read_bytes())


def artifact_names(expected, actual):
    need(set(expected) == set(actual), "complete artifact set")


def signed(blob, offset, width):
    return int.from_bytes(blob[offset:offset + width], "little", signed=True)


def scalar_equal(a, b):
    need(a == b, "tensor real/imag scalar equality")
    need(abs(a) < 1 << 235, "tensor scalar bound")


def residual_equal(v, common, n, d):
    need(abs(n) < 1 << 253 and 0 < d < 1 << 202, "residual N/D range")
    need(math.gcd(n, d) == 1, "residual N/D reduced")
    need(n * common == v * d, "residual signed rational equality")


def weighted_square(ss, s, claimed):
    need(claimed == s * s * ss, "full ordered second-derivative s-squared weight")


def root_proof(value, ell, upper, lo, hi, equality):
    need(value >= 0 and ell >= 0, "root nonnegative input")
    scaled, den = value.numerator * P * P, value.denominator
    need(ell * ell * den <= scaled < (ell + 1) ** 2 * den, "true rational root cell")
    eq = ell * ell * den == scaled
    need(type(equality) is bool and equality == eq, "true rational root equality flag")
    need(upper == ell + int(not eq), "true rational root upper integer")
    need(lo == F(ell, P) and hi == F(upper, P), "root endpoint normalization")
    need(lo * lo <= value <= hi * hi, "root squared enclosure")
    return lo, hi


def main_root(data, A, H0):
    need(integer(data["A"]) == A and integer(data["denominator"]) == P,
         "primary root input")
    scaled = P * P * A
    q, rem = divmod(scaled, H0)
    need(integer(data["quotient"]) == q and integer(data["remainder"]) == rem,
         "primary root Euclidean witness")
    ell, up = integer(data["lower_numerator"]), integer(data["upper_numerator"])
    return root_proof(F(A, H0), ell, up, F(ell, P), F(up, P),
                      ell * ell * H0 == scaled)


def independent_root(data, value):
    need(fraction(data["input"]) == value and data["bits"] == 128,
         "independent root input")
    need(integer(data["scaled_numerator"]) == value.numerator * P * P
         and integer(data["denominator"]) == value.denominator, "root exact scaling")
    return root_proof(value, integer(data["floor_root"]), integer(data["ceil_root"]),
                      fraction(data["lower"]), fraction(data["upper"]),
                      data["true_rational_equality"])


def error_interval(hlo, hhi, E, lo, hi):
    need(E >= 0 and 0 <= hlo <= hhi, "error interval preconditions")
    need(lo == max(F(0), hlo - E) and hi == hhi + E, "norm error minus/plus direction")
    need(0 <= lo <= hi, "original-reference interval order")


def exponential(a, b):
    x, term, total = F(5, 4), F(1), F(1)
    for n in range(1, 33):
        term = term * x / n
        total += term
    t33, ratio = term * x / 33, F(5, 136)
    upper = total + t33 / (1 - ratio)
    need(fraction(a["argument"]) == fraction(b["x"]) == x, "exponential argument")
    need(a["degree"] == b["terms_through_degree"] == 32, "fixed exponential degree")
    for keya, keyb, value in [
        ("lower_P32", "lower", total), ("term33", "term33", t33),
        ("tail_ratio_upper", "tail_ratio_upper", ratio), ("upper", "upper", upper),
    ]:
        need(fraction(a[keya]) == fraction(b[keyb]) == value, "exponential exact witness")
    need(0 < ratio < 1 and total < upper, "positive exponential enclosure")
    return total, upper


def gate(lo, hi, elo, ehi, epsilon, lp, up, recorded):
    need(lp == lo * elo and up == hi * ehi, "gate exact endpoint products")
    verdict = "REFUTED" if lp > epsilon else "NODE_PASS" if up <= epsilon else "UNDECIDED"
    need(recorded in NORMAL_GATE and NORMAL_GATE[recorded] == verdict, "gate semantics")
    return verdict


def negative_control(name, callback, kind="actual_archival_item_mutated_in_memory"):
    try:
        callback()
    except ValueError as exc:
        return {"name": name, "kind": kind, "rejected_by": str(exc)}
    raise ValueError("negative control accepted: " + name)


class Bindings:
    def __init__(self):
        self.values = {}

    def path(self, name):
        p = Path(name)
        p = (HERE / p).resolve() if not p.is_absolute() else p.resolve()
        need(p.is_relative_to(HERE), "binding outside assigned directory")
        need(p.is_file(), "missing bound file: " + str(p))
        return p

    def bind(self, name, expected=None):
        p = self.path(name)
        actual = digest(p)
        if expected is not None:
            digest_match(expected, actual)
        key = str(p.relative_to(HERE))
        if key in self.values:
            digest_match(self.values[key], actual)
        self.values[key] = actual
        return p

    def table(self, table):
        need(isinstance(table, dict) and table, "nonempty source/input table")
        normalized = {}
        for name, pin in table.items():
            p = self.bind(name, pin)
            normalized[str(p.relative_to(HERE))] = pin
        need(len(normalized) == len(table), "duplicate normalized source/input path")
        return normalized


def authenticate(args, bindings):
    need(not OUTPUT.exists(), "exclusive comparison output already exists")
    for name, pin in SOURCE_PINS.items():
        bindings.bind(name, pin)
    for name, pin in ORIGINAL_PINS.items():
        bindings.bind(name, pin)
    bindings.bind(MAIN / "run.json", args.primary_run_sha256)
    bindings.bind(INDEP / "run.json", args.independent_run_sha256)
    main, run = load(MAIN / "run.json"), load(INDEP / "run.json")
    need(main["execution_status"] == "COMPLETE"
         and main["mathematical_status"] == "FULL_FIXED_NODE_RESIDUAL_BOUNDS_VERIFIED",
         "primary completed scope")
    need(run["schema"] == "full-nodal-independent-run-v1"
         and run["status"] == "COMPLETE_FULL_NODAL_INDEPENDENT", "independent completed scope")
    ms = bindings.table(main["inputs"]["source_sha256"])
    mi = bindings.table(main["inputs"]["input_sha256"])
    rs = bindings.table(run["source_sha256"])
    ri = bindings.table(run["input_sha256"])
    for name, pin in ORIGINAL_PINS.items():
        need(mi.get(name) == ri.get(name) == pin, "same fixed original input")
    for name in ("FULL_NODAL_RESIDUAL_CONTRACT.md", "FULL_NODAL_RESIDUAL_INDEPENDENT_REVIEW.md",
                 "FULL_NODAL_EXECUTION_INDEPENDENT_REVIEW.md"):
        need(ms.get(name) == rs.get(name) == SOURCE_PINS[name], "same approved mathematical interface")
    for table, name in [(ms, "audit_full_nodal_residual.py"),
                        (rs, "audit_full_nodal_residual_independent.py")]:
        need(table.get(name) == SOURCE_PINS[name], "approved executed source")
    need(ms.get("FULL_NODAL_EXECUTION_CONTRACT.md") == SOURCE_PINS["FULL_NODAL_EXECUTION_CONTRACT.md"],
         "primary execution contract pin")
    need(rs.get("FULL_NODAL_INDEPENDENT_EXECUTION_CONTRACT.md")
         == SOURCE_PINS["FULL_NODAL_INDEPENDENT_EXECUTION_CONTRACT.md"], "independent execution contract pin")
    need(rs.get("FULL_NODAL_INDEPENDENT_CODE_REVIEW.md")
         == SOURCE_PINS["FULL_NODAL_INDEPENDENT_CODE_REVIEW.md"], "independent executed approval")
    for script, review in [("audit_full_nodal_residual.py", "FULL_NODAL_PRIMARY_CODE_REVIEW.md"),
                           ("audit_full_nodal_residual_independent.py", "FULL_NODAL_INDEPENDENT_CODE_REVIEW.md")]:
        need(SOURCE_PINS[script] in (HERE / review).read_text(), "root review binds executed source")
    # Recompute metadata config digests only. Never import either scientific script.
    mc = main["inputs"]["config"]
    proofs = {name: pin for name, pin in ms.items()
              if name not in ("audit_full_nodal_residual.py", "FULL_NODAL_RESIDUAL_INDEPENDENT_REVIEW.md")}
    config_object = {"config": mc, "proofs": proofs, "inputs": mi,
                     "math_review": main["inputs"]["math_review"]}
    canonical = json.dumps(config_object, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("ascii")
    digest_match(main["inputs"]["config_sha256"], hashlib.sha256(canonical).hexdigest())
    ic = run["config"]
    canonical = (json.dumps(ic, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                            allow_nan=False) + "\n").encode("utf-8")
    digest_match(run["config_sha256"], hashlib.sha256(canonical).hexdigest())
    need(mc["node_index"] == ic["node"] == 1280 and mc["time_numerator"] == 1280
         and mc["time_denominator"] == 2048 and ic["time"] == [1280, 2048], "fixed node/time")
    need(mc["center_Q"] == integer(ic["QP"]) == QP
         and mc["root_fractional_bits"] == ic["root_bits"] == 128, "fixed precision")
    need(mc["G_count"] == ic["G_count"] == 4912 and mc["H_count"] == ic["H_count"] == COUNT,
         "fixed full supports")
    need(mc["large_real_products"] == 15 and ic["new_ordered_pairs"] == 120638720
         and ic["new_scalar_multiplications"] == 482554880, "full prescribed work counts")
    for key in ("FFT", "integration", "retry"):
        need(mc[key] is False and ic[key] is False, "no extra scientific operation")
    need(ic["main_new_source_or_output_read"] is False and ic["compute_lcm"] is False,
         "independent recorded route")
    need(mc["output_bytes"] == ic["archive_bytes"] == 64 << 20
         and mc["peak_rss_bytes"] == ic["rss_bytes"] == 256 << 20
         and mc["wall_seconds"] == ic["wall_seconds"] == 60, "fixed resource caps")
    need(mc["metadata_reserve_bytes"] == ic["metadata_reserve_bytes"] == 256 << 10,
         "fixed metadata reserve")
    need(mc["small_integer_bit_guard"] == ic["integer_bit_limit"] == 8192, "integer guard")
    need(main["source_commit"]["worktree"] == run["checkout"]["root"] == str(HERE.parents[2]),
         "reverse scientific checkout")
    need(run["checkout"]["branch"] == "codex/ns-reverse", "independent branch")
    for commit in (main["source_commit"]["git_HEAD"], run["checkout"]["commit"]):
        need(re.fullmatch(r"[0-9a-f]{40}", commit), "recorded source commit")
    need(main["launch"]["command"] and main["environment"]["python"]
         and run["command_argv"] and run["environment"]["python"], "execution environment records")
    # Authenticate every new artifact, including the unused A/J and raw products.
    artifact_names(MAIN_SPECS, main["artifacts"])
    for name, length in MAIN_SPECS.items():
        spec = main["artifacts"][name]
        p = bindings.bind(MAIN / name, spec["sha256"])
        need(p.stat().st_size == spec["bytes"] == length and spec["actual_readback"] == "PASS",
             "primary artifact size/readback")
    need(main["actual_new_binary_bytes"] == sum(MAIN_SPECS.values()) == 46951206,
         "primary complete archive size")
    specs = {item["file"]: item for item in run["output_files"]}
    need(len(specs) == len(run["output_files"]), "independent unique output descriptors")
    artifact_names(set(INDEP_SPECS) | {"result.json"}, specs)
    for name, spec in specs.items():
        p = bindings.bind(INDEP / name, spec["sha256"])
        need(p.stat().st_size == spec["bytes"], "independent artifact size")
        if name in INDEP_SPECS:
            need(spec["bytes"] == INDEP_SPECS[name], "fixed independent binary width")
    result = load(INDEP / "result.json")
    for field in ("source_sha256", "input_sha256", "config_sha256", "checkout", "input_connection"):
        need(result[field] == run[field], "independent run/result field: " + field)
    need(result["schema"] == "full-nodal-independent-fraction-result-v1"
         and result["mathematical_status"] == "ONE_FIXED_REFERENCE_NODAL_RESIDUAL_BOUNDS"
         and result["new_main_comparison"] == "NOT_READ_OR_PERFORMED", "independent result scope")
    need(result["node"] == 1280 and result["time"] == ["1280", "2048"]
         and result["viscosity"] == 1, "independent result fixed parameters")
    need(result["new_ordered_pairs"] == 120638720 and result["new_scalar_multiplications"] == 482554880,
         "independent result complete work")
    need(result["new_tensors"] == run["completed_new_tensors"] == list(TENSORS)
         and result["reused_tensor12"] is True, "five new tensors and reused T12")
    result_specs = {item["file"]: item for item in result["output_files"]}
    artifact_names(INDEP_SPECS, result_specs)
    need(len(result_specs) == len(result["output_files"]), "unique independent result outputs")
    for name in INDEP_SPECS:
        need(result_specs[name] == specs[name], "independent result/output connection")
    need(result["residual_file"] == specs["residual-hat-fractions.i256-u256le.bin"],
         "independent residual pointer")
    need(main["reused_T12"]["convolution_recomputed"] is False
         and main["reused_T12"]["complete_outputs_read"] == COUNT
         and integer(main["reused_T12"]["denominator"]) == QP * QP, "primary reused T12")
    need(main["maximum_small_integer_bits_observed"] <= 8192, "observed primary integer cap")
    need(all(0 <= integer(x) <= 8192 for x in run["norm_fraction_peak_bits"].values()),
         "observed independent aggregate integer cap")
    return main, run, result


def compare_tensors(main, run):
    need(len(main["products"]) == 15 and len(main["tensor_results"]) == 5,
         "complete primary multiplication metadata")
    products = {(x["tensor"], x["index"]): x for x in main["products"]}
    need(len(products) == 15 and set(products) == {(t, i) for t in TENSORS for i in range(3)},
         "unique prescribed product identities")
    for (t, i), item in products.items():
        name = "tensor-" + t + "-product-" + str(i) + ".signed-le.bin"
        need(item["product_file"] == name and item["product_sha256"] == main["artifacts"][name]["sha256"],
             "product artifact connection")
        need(item["decoded_coefficients"] == COUNT and item["terminal_quotient"] == 0
             and item["terminal_carry"] == int(item["product_negative"]), "recorded full product decode")
        need(len(item["inputs"]) == 2, "two recorded product inputs")
        for descriptor in item["inputs"]:
            need(descriptor["signed_width_bytes"] == 539070
                 and 0 <= descriptor["absolute_bit_length"] < 8 * 539070
                 and descriptor["sign"] in (-1, 0, 1), "packed input descriptor")
            need(re.fullmatch(r"[0-9a-f]{64}", descriptor["sha256"]), "packed input digest format")
    records = {x["file"]: x for x in run["output_files"]}
    meta = {tuple(x["pair_one_based"]): x for x in main["tensor_results"]}
    need(set(meta) == {(1,1), (1,3), (2,2), (2,3), (3,3)}, "primary full tensor metadata")
    samples = {}
    for t in TENSORS:
        a = (MAIN / ("tensor-" + t + ".i240le.bin")).read_bytes()
        b = (INDEP / ("tensor" + t + "-direct.i240le.bin")).read_bytes()
        imeta = records["tensor" + t + "-direct.i240le.bin"]
        mmeta = meta[(int(t[0]), int(t[1]))]
        need(imeta["ordered_pairs"] == 24127744 and imeta["scalar_multiplications"] == 96510976,
             "independent per-tensor complete count")
        need(mmeta["outputs"] == COUNT and mmeta["zero_direct_ordered_terms"] == 4912
             and mmeta["file"] == "tensor-" + t + ".i240le.bin", "primary per-tensor count")
        for scalar in range(2 * COUNT):
            va, vb = signed(a, 30 * scalar, 30), signed(b, 30 * scalar, 30)
            scalar_equal(va, vb)
            index, ri = divmod(scalar, 2)
            mirror = 2 * (COUNT - 1 - index) + ri
            opposite = signed(a, 30 * mirror, 30)
            need(va == (opposite if ri == 0 else -opposite), "full tensor conjugacy")
            samples.setdefault(ri, (va, vb))
        need(signed(a, 60 * ZERO + 30, 30) == integer(mmeta["zero_imaginary_numerator"]) == 0,
             "tensor zero imaginary part")
        need(signed(a, 60 * ZERO, 30) == integer(mmeta["zero_real_numerator"]),
             "recorded zero direct sum connection")
    return samples


def compare_residuals(main, result):
    orig, cert = main["original_node_and_center"], main["exact_norm_certificates"]
    D = integer(orig["D"])
    need(0 < D < 1 << 225 and integer(orig["L_lcm"]) * (1 << 53) == D,
         "recorded original denominator")
    H0 = D * D * QP ** 4
    need(integer(cert["H0"]) == H0, "H0 denominator")
    vdata = (MAIN / "V.i512le.bin").read_bytes()
    sdata = (MAIN / "S.u960le.bin").read_bytes()
    rdata = (INDEP / "residual-hat-fractions.i256-u256le.bin").read_bytes()
    A2 = A0lo = A0hi = inexact = 0
    norm0, norm2 = F(0), F(0)
    sample = {}
    for index in range(COUNT):
        k = (index % 33 - 16, (index // 33) % 33 - 16, index // 1089 - 16)
        s = sum(x * x for x in k)
        common = D * s * QP * QP
        vs, ss = [], F(0)
        for ri in range(6):
            offset = 64 * (6 * index + ri)
            v = signed(vdata, offset, 64)
            n = signed(rdata, offset, 32)
            den = int.from_bytes(rdata[offset + 32:offset + 64], "little")
            need(abs(v) < 1 << 478, "V scalar width")
            if s:
                residual_equal(v, common, n, den)
                need((s * QP * QP) % den == 0, "independent local denominator divisibility")
            else:
                need(v == n == 0 and den == 1, "exact zero residual 0/1")
            other = 64 * (6 * (COUNT - 1 - index) + ri)
            vn = signed(vdata, other, 64)
            nn = signed(rdata, other, 32)
            dd = int.from_bytes(rdata[other + 32:other + 64], "little")
            sign = 1 if ri % 2 == 0 else -1
            need(v == sign * vn and n == sign * nn and den == dd, "V/Fraction full conjugacy")
            vs.append(v)
            ss += F(n * n, den * den)
            if s and n and "residual" not in sample:
                sample["residual"] = (v, common, n, den)
        storedS = int.from_bytes(sdata[index * 120:(index + 1) * 120], "little")
        need(0 <= storedS < 1 << 959 and storedS == sum(v * v for v in vs),
             "complete S versus V square sum")
        if s:
            need(all(sum(k[a] * vs[2 * a + ri] for a in range(3)) == 0 for ri in (0, 1)),
                 "full V divergence")
            quotient, rem = divmod(storedS, s * s)
            A2 += storedS
            A0lo += quotient
            A0hi += quotient + int(rem != 0)
            inexact += int(rem != 0)
        else:
            need(storedS == 0, "zero S")
        contribution = s * s * ss
        weighted_square(ss, s, contribution)
        norm0 += ss
        norm2 += contribution
        if s > 1 and ss and "weight" not in sample:
            sample["weight"] = (ss, s, contribution)
    for key, value in [("A2", A2), ("A0_lower", A0lo), ("A0_upper", A0hi),
                       ("noninteger_S_over_s_squared_count", inexact)]:
        need(integer(cert[key]) == value, "primary full aggregate " + key)
    need(cert["complete_nonzero_signed_outputs"] == 35936 and A0hi - A0lo == inexact,
         "complete zero-order aggregate count")
    need(fraction(cert["r0_squared_interval_width"]) == F(inexact, H0), "zero-order square interval width")
    need(fraction(result["norm_square"]["0"]) == norm0
         and fraction(result["norm_square"]["2"]) == norm2, "independent full exact squared norms")
    need(norm2 == F(A2, H0), "H2 s-squared cancellation")
    need(F(A0lo, H0) <= norm0 <= F(A0hi, H0), "exact independent L2 square inside primary interval")
    need((1 << 384) % norm2.denominator == 0, "H2 dyadic denominator")
    roots = {
        "r0lo": main_root(cert["r0_lower_root"], A0lo, H0),
        "r0hi": main_root(cert["r0_upper_root"], A0hi, H0),
        "r2": main_root(cert["r2_root"], A2, H0),
    }
    return {0: norm0, 2: norm2}, roots, sample


def compare_intervals(main, result, norms, roots):
    a, b = main["original_node_and_center"], result["input_connection"]
    old = load(HERE / "kronecker-independent-agreement.json")["comparison"]
    M, delta = fraction(a["M"]), fraction(a["delta"])
    need(M == fraction(b["M"]) == fraction(old["M_from_independent_witnesses"])
         and delta == fraction(b["delta"]) == fraction(old["delta_from_independent_witnesses"]),
         "same accepted M/delta")
    need(M >= 0 and delta >= 0, "nonnegative input perturbation")
    E = {j: 28 ** (j + 1) * (2 * M * delta + delta * delta) for j in (0, 2)}
    for j in (0, 2):
        key = "E" + str(j)
        need(fraction(a[key]) == fraction(b[key]) == fraction(old[key]) == E[j], "same exact E expression")
    elo, ehi = exponential(main["fixed_exponential_certificate"], result["exponential"])
    cert, comparison, sample = main["exact_norm_certificates"], {}, None
    primary_gates = []
    for j in (0, 2):
        sj = str(j)
        mh = (roots["r0lo"][0], roots["r0hi"][1]) if j == 0 else roots["r2"]
        ir = result["intervals"][sj]
        need(fraction(ir["center_norm_square"]) == norms[j], "independent interval norm input")
        ih = independent_root(ir["center_root"], norms[j])
        for label, endpoints in (("primary", mh), ("independent", ih)):
            lo, hi = endpoints
            need(0 <= lo <= hi and lo * lo <= norms[j] <= hi * hi, label + " root encloses exact norm")
        need(fraction(cert["center_norm_intervals"][sj]["lower"]) == mh[0]
             and fraction(cert["center_norm_intervals"][sj]["upper"]) == mh[1], "primary assembled root interval")
        mo = cert["original_reference_norm_intervals"][sj]
        ml, mu = fraction(mo["lower"]), fraction(mo["upper"])
        il, iu = fraction(ir["original_residual_lower"]), fraction(ir["original_residual_upper"])
        need(fraction(ir["E"]) == E[j], "independent interval E")
        error_interval(*mh, E[j], ml, mu)
        error_interval(*ih, E[j], il, iu)
        epsilon = F(1, 5000000) if j == 2 else F(1, 320000000)
        mg = main["old_epsilon_node_gates"][sj]
        need(fraction(mg["target_coefficient"]) == fraction(ir["epsilon"]) == epsilon,
             "same fixed amplitude target")
        need(fraction(mg["lower"]) == ml and fraction(mg["upper"]) == mu, "primary gate interval")
        mv = gate(ml, mu, elo, ehi, epsilon, fraction(mg["lower_times_exp_lower"]),
                  fraction(mg["upper_times_exp_upper"]), mg["verdict"])
        iv = gate(il, iu, elo, ehi, epsilon, fraction(ir["lower_times_exp_lower"]),
                  fraction(ir["upper_times_exp_upper"]), ir["gate"])
        need({mv, iv} != {"REFUTED", "NODE_PASS"}, "contradictory rigorous gate outcomes")
        primary_gates.append(mv)
        comparison[sj] = {"primary_gate": mv, "independent_gate": iv,
                          "same_classification": mv == iv,
                          "primary_interval": [pair(ml), pair(mu)],
                          "independent_interval": [pair(il), pair(iu)],
                          "endpoint_identity_required": False}
        if E[j] > 0 and sample is None:
            sample = (*ih, E[j], il, iu)
    expected_joint = ("REFUTED" if "REFUTED" in primary_gates else
                      "NODE_PASS" if all(x == "NODE_PASS" for x in primary_gates) else "UNDECIDED")
    need(NORMAL_GATE[main["old_epsilon_joint_node_verdict"]] == expected_joint, "primary joint node gate")
    return comparison, sample, {"M": pair(M), "delta": pair(delta),
                                "E0": pair(E[0]), "E2": pair(E[2])}


def final_resources(args, main, run, bindings):
    output = {}
    settings = [
        ("primary", MAIN, args.primary_stdout, args.primary_stderr, main,
         "sha256", "final_observation", "output_bytes", "resources"),
        ("independent", INDEP, args.independent_stdout, args.independent_stderr, run,
         "run_sha256", "post_write_budget_observation", "archive_bytes", "final_budget_observation"),
    ]
    for label, folder, stdout, stderr, record, hashkey, obskey, sizekey, snapshotkey in settings:
        sp, ep = bindings.bind(stdout), bindings.bind(stderr)
        need(sp != ep and not sp.is_relative_to(folder) and not ep.is_relative_to(folder),
             "distinct external stdout/stderr paths")
        need(ep.stat().st_size == 0, "completed run nonempty stderr")
        lines = sp.read_text().splitlines()
        need(lines, "missing final stdout")
        last = json.loads(lines[-1])
        bindings.bind(folder / "run.json", last[hashkey])
        if label == "primary":
            need(last["execution_status"] == "COMPLETE"
                 and last["mathematical_status"] == "FULL_FIXED_NODE_RESIDUAL_BOUNDS_VERIFIED"
                 and last["output"] == str(folder / "run.json"), "primary final stdout status")
            expected = set(MAIN_SPECS) | {"RUN_CLAIM.json", "run.json"}
        else:
            need(last["status"] == "COMPLETE_FULL_NODAL_INDEPENDENT"
                 and last["output_directory"] == str(folder), "independent final stdout status")
            expected = set(INDEP_SPECS) | {"claim.json", "progress.jsonl", "run.json", "result.json"}
        entries = list(folder.iterdir())
        need(all(p.is_file() and not p.is_symlink() for p in entries), "no untracked output directory/symlink")
        artifact_names(expected, [p.name for p in entries])
        for p in entries:
            bindings.bind(p)
        actual = sum(p.stat().st_size for p in entries)
        observed = last[obskey]
        need(integer(observed[sizekey]) == actual, "actual post-write directory bytes")
        wall = observed["wall_seconds"]
        wall_ok = 0 <= wall and (wall < 60 if label == "primary" else wall <= 60)
        need(wall_ok and 0 < observed["peak_rss_bytes"] <= (256 << 20),
             "post-write wall/RSS cap")
        snapshot = record[snapshotkey]
        need(0 <= snapshot["wall_seconds"] <= observed["wall_seconds"]
             and 0 < snapshot["peak_rss_bytes"] <= observed["peak_rss_bytes"], "snapshot/post-write chronology")
        # Snapshot precedes final run.json write; do not demand its byte count equals the final count.
        total = actual + sp.stat().st_size + ep.stat().st_size
        need(total <= (64 << 20), "complete archive plus external logs cap")
        output[label] = {"post_write": observed, "pre_write_snapshot": snapshot,
                         "actual_directory_bytes": actual, "including_external_logs_bytes": total,
                         "stdout": str(sp.relative_to(HERE)), "stderr": str(ep.relative_to(HERE))}
    return output


def run_comparison(args):
    bindings = Bindings()
    main, irun, result = authenticate(args, bindings)
    tensors = compare_tensors(main, irun)
    norms, roots, samples = compare_residuals(main, result)
    intervals, error_sample, perturbation = compare_intervals(main, result, norms, roots)
    resources = final_resources(args, main, irun, bindings)
    # Small mutations only; none repeats the full comparison, node recovery or a convolution.
    controls = []
    name, pin = next(iter(SOURCE_PINS.items()))
    changed = ("0" if pin[0] != "0" else "1") + pin[1:]
    controls.append(negative_control("source_pin", lambda: digest_match(changed, pin)))
    missing = set(MAIN_SPECS)
    missing.remove("V.i512le.bin")
    controls.append(negative_control("missing_output", lambda: artifact_names(MAIN_SPECS, missing)))
    for ri, label in ((0, "tensor_real"), (1, "tensor_imag")):
        a, b = tensors[ri]
        controls.append(negative_control(label, lambda a=a, b=b: scalar_equal(a, b + 1)))
    need("residual" in samples and "weight" in samples and error_sample is not None,
         "fixed-data witnesses for requested negative controls")
    v, common, n, den = samples["residual"]
    controls.append(negative_control("residual_common_denominator",
                    lambda: residual_equal(v, common + 1, n, den)))
    controls.append(negative_control("residual_sign", lambda: residual_equal(v, common, -n, den)))
    ss, s, correct = samples["weight"]
    controls.append(negative_control("s_squared_weight", lambda: weighted_square(ss, s, s * ss)))
    # This synthetic boundary has a square floor, but is not an exact rational square.
    value = F(3, 2 * P * P)
    root_proof(value, 1, 2, F(1, P), F(2, P), False)
    controls.append(negative_control("floor_square_not_true_rational_equality",
                    lambda: root_proof(value, 1, 1, F(1, P), F(1, P), True),
                    "explicit_tiny_synthetic_boundary_not_an_archival_measurement"))
    hlo, hhi, E, lo, hi = error_sample
    controls.append(negative_control("E_lower_sign", lambda: error_interval(hlo, hhi, E, hlo + E, hi)))
    controls.append(negative_control("E_upper_sign", lambda: error_interval(hlo, hhi, E, lo, hhi - E)))
    bindings.bind(Path(__file__))
    bindings.bind(HERE / "FULL_NODAL_COMPARISON_NOTES.md")
    # Detect source/input/output drift during this read-only comparison.
    for name, pin in list(bindings.values.items()):
        bindings.bind(name, pin)
    out = {
        "status": "PASS_FROZEN_FULL_NODAL_ARCHIVE_COMPARISON",
        "primary_run_sha256": args.primary_run_sha256,
        "independent_run_sha256": args.independent_run_sha256,
        "comparison": {"new_tensor_scalars_equal": 5 * 2 * COUNT,
                       "compared_field": "center residual Rhat; original-reference R bounded only through E",
                       "residual_rational_components_equal": 6 * COUNT,
                       "V_S_outputs_checked": COUNT, "full_signed_nonzero_outputs": COUNT - 1,
                       "independent_exact_norm0_squared": pair(norms[0]),
                       "independent_exact_norm2_squared": pair(norms[2]),
                       "norm0_inside_primary_integer_bracket": True,
                       "norm2_equals_primary_A2_over_H0": True,
                       "gate_comparison": intervals, "perturbation": perturbation},
        "negative_controls": controls, "resources": resources,
        "primary_source_commit": main["source_commit"]["git_HEAD"],
        "independent_source_commit": irun["checkout"]["commit"],
        "input_sha256": bindings.values,
        "checker_source_sha256": bindings.values[Path(__file__).name],
        "checker_environment": {"python": sys.version, "executable": sys.executable, "argv": sys.argv},
        "kernel_operations_reexecuted": {"convolution": False, "integration": False, "node_reconstruction": False},
        "scope": "Complete saved fields for one reference node; exact archival arithmetic comparison and enclosure checks only. No continuous-time residual bound or NS solution conclusion.",
    }
    with OUTPUT.open("x", encoding="utf-8") as stream:
        json.dump(out, stream, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write("\n")
    print(json.dumps({"status": out["status"], "comparison": out["comparison"],
                      "negative_controls_rejected": len(controls), "output_sha256": digest(OUTPUT)},
                     sort_keys=True))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="store_true")
    for name in ("primary-run-sha256", "independent-run-sha256", "primary-stdout",
                 "primary-stderr", "independent-stdout", "independent-stderr"):
        parser.add_argument("--" + name)
    args = parser.parse_args()
    if not args.run:
        parser.print_help()
        return 0
    need(sys.version_info >= (3, 10) and sys.flags.optimize == 0, "supported non-optimized Python")
    need(HERE.parents[2] == Path("/Users/kasifa/Documents/Math/navier-stokes-reverse"),
         "reverse scientific worktree only")
    need(all(getattr(args, name) for name in ("primary_run_sha256", "independent_run_sha256",
             "primary_stdout", "primary_stderr", "independent_stdout", "independent_stderr")),
         "frozen run SHA values and external logs required")
    run_comparison(args)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(json.dumps({"status": "COMPARISON_REJECTED", "error": str(exc)}, sort_keys=True), file=sys.stderr)
        raise SystemExit(1)
