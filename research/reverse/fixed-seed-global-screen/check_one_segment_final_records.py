#!/usr/bin/env python3
"""Audit saved records and rational endpoints only; no scientific kernel replay."""
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
MAIN = HERE / "one-segment-derivative-trial-01"
INDEP = HERE / "one-segment-derivative-independent-trial-01"


def need(value, label):
    if not value:
        raise ValueError(label)


def load(path):
    return json.loads(path.read_bytes())


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def frac(value):
    if isinstance(value, dict):
        return F(int(value["numerator"]), int(value["denominator"]))
    return F(int(value[0]), int(value[1]))


def pair(value):
    return [str(value.numerator), str(value.denominator)]


def last_json(path):
    return json.loads(path.read_text().splitlines()[-1])


def main():
    p = load(MAIN / "run.json")
    ir = load(INDEP / "run.json")
    ind = load(INDEP / "result.json")
    agreement = load(HERE / "one-segment-independent-agreement.json")
    need(p["execution_status"] == "COMPLETE", "main status")
    need(ir["status"] == "COMPLETE_FIXED_SEGMENT_INDEPENDENT_UPPER", "independent status")
    for key in ("source_sha256", "input_file_sha256", "checkout", "config_sha256"):
        need(ir[key] == ind[key], "shared run/result field: " + key)
    need(len(ir["output_files"]) == 1, "independent result description count")
    spec = ir["output_files"][0]
    need(spec["file"] == "result.json" and
         spec["sha256"] == sha(INDEP / "result.json") and
         spec["bytes"] == (INDEP / "result.json").stat().st_size,
         "independent run binds result bytes")
    need(agreement["status"] == "PASS_ACTUAL_INDEPENDENT_FRACTION_RECONSTRUCTION",
         "comparison status")
    binding = {}
    for name, expected in agreement["input_sha256"].items():
        path = Path(name)
        need(path.is_relative_to(HERE), "unexpected binding path")
        need(sha(path) == expected, "comparison binding: " + name)
        binding[str(path.relative_to(HERE))] = expected
    need(len(binding) == 27, "expected comparison binding count")
    for table in (p["inputs"]["source_sha256"], p["authenticated_archive_sha256"],
                  ir["source_sha256"], ir["input_file_sha256"],
                  ind["source_sha256"], ind["input_file_sha256"]):
        for name, expected in table.items():
            path = Path(name) if Path(name).is_absolute() else HERE / name
            need(binding[str(path.relative_to(HERE))] == expected, "record binding consistency")
    c = agreement["comparison"]
    need((c["exact_mode_norm_squares_compared"], c["chi_coefficients_compared"],
          c["norm_intervals_compared"], c["main_intervals_contained_in_independent"],
          c["main_root_inputs_recomputed_from_saved_squares"]) == (19648, 4, 12, 12, 58944),
         "saved comparison counts")
    need([x["in_memory_mutation"] for x in agreement["negative_controls"]] ==
         ["norm_square", "chi", "count", "root_sum", "strain_factor", "M3_bound"],
         "saved negative-control labels")
    need(all(x["rejected_by"] for x in agreement["negative_controls"]),
         "saved negative-control reasons")
    compressed_checks = []
    specs = [(MAIN, p["norm_square_evidence"])]
    specs += [(INDEP, item) for item in ind["norm_square_files"]]
    for folder, spec in specs:
        path = folder / spec["file"]
        need(sha(path) == spec.get("file_sha256", spec.get("sha256")), "compressed hash")
        content = gzip.decompress(path.read_bytes())
        need(hashlib.sha256(content).hexdigest() == spec["canonical_json_sha256"],
             "canonical content hash")
        decoded = json.loads(content)
        if folder == MAIN:
            need(len(decoded["base_squared"]) == 4 and
                 all(len(row) == 4912 for row in decoded["base_squared"]), "main shape")
        else:
            need(len(decoded["norm_square"]) == 4912, "independent shape")
        compressed_checks.append(str(path.relative_to(HERE)))
    # No operation on any per-mode norm-square entry is performed here.
    C = frac(ind["C_chi"])
    bound = p["whole_segment_upper_bounds"]
    need(C == max(abs(frac(v)) for v in ind["chi"]) ==
         frac(bound["chi_absolute_upper"]), "C chi")
    nested = 0
    for m in range(4):
        a, b = p["Bernstein_results"][m], ind["bernstein"][m]
        need(frac(a["chi"]) == frac(b["chi"]) == frac(ind["chi"][m]), "chi agreement")
        for j in (1, 2, 3):
            x, y = a["orders"][str(j)], b["A"][str(j)]
            ml, mu = frac(x["A_j_lower"]), frac(x["A_j_upper"])
            il, iu = frac(y["lower"]), frac(y["upper"])
            need(il <= ml <= mu <= iu, "saved norm interval nesting")
            denominator = int(x["sum_denominator"])
            need(F(int(x["sum_floor_scaled_roots"]), denominator) == ml and
                 F(int(x["sum_ceil_scaled_roots"]), denominator) == mu,
                 "stored sum normalization")
            need(int(x["sum_ceil_scaled_roots"]) - int(x["sum_floor_scaled_roots"])
                 == x["non_square_count"], "stored sum width")
            nested += 1
    roots = {}
    for n in (2, 3):
        lo, hi = map(frac, bound["sqrt%d_interval" % n])
        need(0 <= lo <= hi and lo * lo <= n <= hi * hi, "stored scalar enclosure")
        roots[n] = hi
    A = {}
    for j in (1, 2, 3):
        A[j] = max(frac(p["Bernstein_results"][m]["orders"][str(j)]["A_j_upper"])
                   for m in range(4))
        need(A[j] == frac(bound["A_j_b_upper"][str(j)]), "stored A maximum")
    values = {"sigma": 2*C+A[1]*roots[2]/2,
              "M2": 2*C*roots[3]+A[2],
              "M3": 2*C*roots[3]+A[3]}
    limits = {"sigma": F(343, 100), "M2": F(3833, 500), "M3": F(6507, 500)}
    endpoint_checks = {}
    for key, value in values.items():
        need(value == frac(bound[key+"_upper"]), "stored envelope expression")
        env = ind["sigma_envelope_expression"] if key == "sigma" else \
            ind["M_envelope_expression"][key[-1]]
        need(frac(env["lower"]) <= value <= frac(env["upper"]),
             "expression interval agreement")
        need(value <= limits[key], "readable rational upper")
        endpoint_checks[key] = {"exact_primary_upper": pair(value),
                                "readable_upper": pair(limits[key]),
                                "positive_rounding_margin": pair(limits[key]-value)}
    ml = last_json(HERE / "one-segment-derivative-root-run.log")
    il = last_json(HERE / "one-segment-derivative-independent.stdout.log")
    need(ml["sha256"] == sha(MAIN / "run.json"), "main stdout binds final run")
    need(il["run_sha256"] == sha(INDEP / "run.json"), "independent stdout binds final run")
    need((HERE / "one-segment-derivative-independent.stderr.log").stat().st_size == 0,
         "independent stderr")
    resources = {}
    for label, folder, obs, bytes_key, logname in (
        ("primary", MAIN, ml["final_observation"], "output_bytes",
         "one-segment-derivative-root-run.log"),
        ("independent", INDEP, il["post_write_budget_observation"], "archive_bytes",
         "one-segment-derivative-independent.stdout.log")):
        actual = sum(path.stat().st_size for path in folder.iterdir() if path.is_file())
        need(actual == obs[bytes_key], "final directory byte count")
        need(obs["wall_seconds"] < 60 and obs["peak_rss_bytes"] < 256*(1 << 20),
             "saved final time/RSS within budget")
        extra = (HERE / logname).stat().st_size
        need(actual + extra < 16*(1 << 20)-256*(1 << 10),
             "archive plus external stdout below reserved budget")
        resources[label] = {**obs, "actual_directory_bytes": actual,
                            "external_stdout_bytes": extra,
                            "archive_plus_external_stdout_bytes": actual+extra}
    additions = [
        "one-segment-independent-agreement.json", "one-segment-root-readback.json",
        "one-segment-independent-final-readback.json",
        "ONE_SEGMENT_DERIVATIVE_REVIEW.md", "ONE_SEGMENT_DERIVATIVE_ROOT_REVIEW.md",
        "ONE_SEGMENT_DERIVATIVE_OUTCOME.md", "one-segment-derivative-root-run.log",
        "one-segment-derivative-independent.stdout.log",
        "one-segment-derivative-independent.stderr.log",
        Path(__file__).name,
    ]
    for name in additions:
        binding[name] = sha(HERE / name)
    result = {
        "status": "PASS_SAVED_ENDPOINT_ARITHMETIC_AND_BYTE_AUDIT",
        "scientific_kernel_reexecuted": False,
        "node_arrays_decoded": False, "projection_or_roots_recomputed": False,
        "saved_per_mode_values_compared_again": False,
        "saved_comparison_bindings_checked": 27,
        "compressed_and_canonical_hashes_checked": len(compressed_checks),
        "saved_norm_interval_nestings_checked": nested,
        "negative_control_record_only": 6,
        "rational_endpoint_checks": endpoint_checks,
        "final_resources": resources,
        "input_sha256": binding,
        "environment": {"python": sys.version, "executable": sys.executable},
        "scope": "Final audit of stored rational endpoints and hashes, not a third reconstruction.",
    }
    output = HERE / "one-segment-final-record-check.json"
    with output.open("x") as stream:
        json.dump(result, stream, ensure_ascii=False, sort_keys=True, indent=2)
        stream.write("\n")
    print(json.dumps({"status": result["status"], "binding_count": len(binding),
                      "resources": resources, "output_sha256": sha(output)},
                     ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
