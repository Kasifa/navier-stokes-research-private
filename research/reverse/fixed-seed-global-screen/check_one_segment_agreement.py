#!/usr/bin/env python3
"""Compare actual independent reconstructions; no PDE, FFT or node projection."""
import copy
from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAIN = HERE / "one-segment-derivative-trial-01"
INDEP = HERE / "one-segment-derivative-independent-trial-01"


def need(ok, label):
    if not ok:
        raise ValueError(label)


def frac(value):
    if isinstance(value, dict):
        return F(int(value["numerator"]), int(value["denominator"]))
    return F(int(value[0]), int(value[1]))


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load(path):
    return json.loads(path.read_bytes())


def compare(p, raw, ind, squares, sums):
    need(p["execution_status"] == "COMPLETE", "main incomplete")
    need(ind["segment"] == [["1280", "2048"], ["1281", "2048"]], "wrong segment")
    need(raw["segment_index"] == 1280, "wrong main segment")
    E = int(raw["E"])
    need(E == 6144 * int(raw["D"]) and int(raw["D"]) == 2**53 * int(raw["L"]), "common denominators")
    need(p["common_denominators"] == {k: raw[k] for k in ("L", "D", "E")}, "record denominators")
    need(len(raw["base_squared"]) == len(p["Bernstein_results"]) == len(ind["bernstein"]) == len(squares) == 4, "group count")
    exact_count = 0
    nested_intervals = 0
    chi = []
    for m in range(4):
        a, b, sq = p["Bernstein_results"][m], ind["bernstein"][m], squares[m]
        need(a["m"] == b["bernstein"] == sq["bernstein"] == m, "group index")
        need(a["complete_signed_mode_count"] == sq["mode_count"] == len(raw["base_squared"][m]) == len(sq["norm_square"]) == 4912, "full signed count")
        cm = F(int(raw["chi_numerators"][m]), E)
        need(cm == frac(a["chi"]) == frac(b["chi"]) == frac(sq["chi"]) == frac(ind["chi"][m]), "chi mismatch")
        need(int(a["chi_numerator_over_E"]) == int(raw["chi_numerators"][m]), "chi numerator mismatch")
        chi.append(cm)
        for n in range(4912):
            N = int(raw["base_squared"][m][n])
            need(N >= 0 and F(N, E*E) == frac(sq["norm_square"][n]), "exact norm square mismatch")
            exact_count += 1
        for j in (1, 2, 3):
            x, y = a["orders"][str(j)], b["A"][str(j)]
            lo, hi, count = sums[m][j]
            need(int(x["sum_floor_scaled_roots"]) == lo and int(x["sum_ceil_scaled_roots"]) == hi, "saved root sum mismatch")
            need(x["non_square_count"] == count and int(x["sum_denominator"]) == E * 2**128, "root sum normalization")
            ml, mu = F(lo, E*2**128), F(hi, E*2**128)
            need(ml == frac(x["A_j_lower"]) and mu == frac(x["A_j_upper"]), "main norm interval")
            il, iu = frac(y["lower"]), frac(y["upper"])
            need(y["terms"] == 4912 and il <= iu, "independent norm interval")
            need(max(ml, il) <= min(mu, iu), "disjoint norm intervals")
            nested_intervals += int(il <= ml <= mu <= iu)
    bound = p["whole_segment_upper_bounds"]
    need(bound["time_numerators"] == [1280, 1281] and bound["time_denominator"] == 2048, "bound time")
    cmax = max(map(abs, chi))
    need(cmax == frac(bound["chi_absolute_upper"]) == frac(ind["C_chi"]), "chi maximum")
    roots = {}
    for n in (2, 3):
        ml, mu = map(frac, bound["sqrt%d_interval" % n])
        il, iu = frac(ind["sqrt%d" % n]["lower"]), frac(ind["sqrt%d" % n]["upper"])
        need(F(0) <= ml <= mu and ml*ml <= n <= mu*mu, "main scalar root")
        need(F(0) <= il <= iu and il*il <= n <= iu*iu, "independent scalar root")
        roots[n] = (ml, mu, il, iu)
    main_upper = {}
    for j in (1, 2, 3):
        v = max(frac(p["Bernstein_results"][m]["orders"][str(j)]["A_j_upper"]) for m in range(4))
        need(v == frac(bound["A_j_b_upper"][str(j)]), "main A maximum")
        il = max(frac(ind["bernstein"][m]["A"][str(j)]["lower"]) for m in range(4))
        iu = max(frac(ind["bernstein"][m]["A"][str(j)]["upper"]) for m in range(4))
        need(il == frac(ind["max_A_intervals"][str(j)]["lower"]) and iu == frac(ind["max_A_intervals"][str(j)]["upper"]), "independent A maximum")
        main_upper[j] = v
    need(frac(bound["inverse_sqrt2_upper"]) == roots[2][1]/2, "strain root factor")
    expression = {"sigma": 2*cmax + main_upper[1]*roots[2][1]/2,
                  "M2": 2*cmax*roots[3][1] + main_upper[2],
                  "M3": 2*cmax*roots[3][1] + main_upper[3]}
    for key, value in expression.items():
        need(value == frac(bound[key + "_upper"]), "main expression mismatch")
        env = ind["sigma_envelope_expression"] if key == "sigma" else ind["M_envelope_expression"][key[1:]]
        j = 1 if key == "sigma" else int(key[1:])
        al, au = (frac(ind["max_A_intervals"][str(j)][s]) for s in ("lower", "upper"))
        il, iu = frac(env["lower"]), frac(env["upper"])
        expected = (2*cmax + al*roots[2][2]/2, 2*cmax + au*roots[2][3]/2) if j == 1 else (2*cmax*roots[3][2]+al, 2*cmax*roots[3][3]+au)
        need((il, iu) == expected, "independent expression mismatch")
        need(il <= value <= iu, "main upper outside independent expression interval")
    need(expression["sigma"] <= F(343, 100) and expression["M2"] <= F(3833, 500) and expression["M3"] <= F(6507, 500), "readable rational upper bounds")
    return {"exact_mode_norm_squares_compared": exact_count, "chi_coefficients_compared": 4,
            "norm_intervals_compared": 12, "main_intervals_contained_in_independent": nested_intervals,
            "main_root_inputs_recomputed_from_saved_squares": 58944,
            "scope": "same fixed reference and one whole interval; no new node projection or full-window conclusion"}


def main():
    p, ir, ind = load(MAIN/"run.json"), load(INDEP/"run.json"), load(INDEP/"result.json")
    need(ir["status"] == "COMPLETE_FIXED_SEGMENT_INDEPENDENT_UPPER", "independent incomplete")
    bindings = {}
    for table in (p["inputs"]["source_sha256"], p["authenticated_archive_sha256"], ir["source_sha256"], ir["input_file_sha256"]):
        for name, expected in table.items():
            path = Path(name) if Path(name).is_absolute() else HERE/name
            need(sha(path) == expected, "source/input hash: " + name)
            bindings[str(path)] = expected
    mspec = p["norm_square_evidence"]
    path = MAIN/mspec["file"]
    need(sha(path) == mspec["file_sha256"], "main compressed hash")
    data = gzip.decompress(path.read_bytes())
    need(hashlib.sha256(data).hexdigest() == mspec["canonical_json_sha256"], "main canonical hash")
    raw = json.loads(data)
    squares = []
    for spec in ind["norm_square_files"]:
        path = INDEP/spec["file"]
        need(sha(path) == spec["sha256"], "independent compressed hash")
        data = gzip.decompress(path.read_bytes())
        need(hashlib.sha256(data).hexdigest() == spec["canonical_json_sha256"], "independent canonical hash")
        squares.append(json.loads(data))
    need(len(squares) == 4, "independent group archive count")
    s = [sum(a*a for a in k) for k in itertools.product(range(-8, 9), repeat=3) if k != (0, 0, 0)]
    need(math.lcm(*s) == int(raw["L"]), "LCM mismatch")
    sums = []
    for row in raw["base_squared"]:
        orders = {}
        for j in (1, 2, 3):
            lo = hi = count = 0
            for a, value in zip(s, row):
                N = (a**j * int(value)) << 256
                low = math.isqrt(N)
                inexact = low*low != N
                lo += low
                hi += low + int(inexact)
                count += int(inexact)
            orders[j] = (lo, hi, count)
        sums.append(orders)
    result = compare(p, raw, ind, squares, sums)
    mutations = []
    for label in ("norm_square", "chi", "count", "root_sum", "strain_factor", "M3_bound"):
        pp, rr = copy.deepcopy(p), copy.deepcopy(raw)
        if label == "norm_square": rr["base_squared"][0][0] = str(int(rr["base_squared"][0][0])+1)
        elif label == "chi": rr["chi_numerators"][0] = str(int(rr["chi_numerators"][0])+1)
        elif label == "count": pp["Bernstein_results"][0]["complete_signed_mode_count"] -= 1
        elif label == "root_sum": pp["Bernstein_results"][0]["orders"]["2"]["sum_ceil_scaled_roots"] = str(int(pp["Bernstein_results"][0]["orders"]["2"]["sum_ceil_scaled_roots"])+1)
        elif label == "strain_factor": pp["whole_segment_upper_bounds"]["inverse_sqrt2_upper"]["numerator"] = "1"
        else: pp["whole_segment_upper_bounds"]["M3_upper"]["numerator"] = "1"
        try:
            compare(pp, rr, ind, squares, sums)
        except ValueError as exc:
            mutations.append({"in_memory_mutation": label, "rejected_by": str(exc)})
        else:
            raise ValueError("mutation accepted: " + label)
    for folder in (MAIN, INDEP):
        for path in folder.iterdir():
            if path.is_file(): bindings[str(path)] = sha(path)
    bindings[str(Path(__file__).resolve())] = sha(Path(__file__).resolve())
    output = HERE/"one-segment-independent-agreement.json"
    with output.open("x") as stream:
        json.dump({"status": "PASS_ACTUAL_INDEPENDENT_FRACTION_RECONSTRUCTION", "comparison": result,
                   "negative_controls": mutations, "input_sha256": bindings}, stream, indent=2)
        stream.write("\n")
    print(json.dumps({"status": "PASS", **result, "negative_controls_rejected": len(mutations), "output_sha256": sha(output)}))


if __name__ == "__main__":
    main()
