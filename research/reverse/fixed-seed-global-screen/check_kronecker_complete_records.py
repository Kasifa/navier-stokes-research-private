#!/usr/bin/env python3
"""Final stored metadata/byte audit. No node, scalar-array, witness, or convolution replay."""
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PRIMARY = HERE / "kronecker-block-trial-02"
INDEP = HERE / "kronecker-direct-independent-trial-01"


def need(condition, label):
    if not condition:
        raise ValueError(label)


def load(path):
    return json.loads(path.read_bytes())


def sha(path):
    d = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            d.update(chunk)
    return d.hexdigest()


def frac(v):
    if isinstance(v, dict):
        return F(int(v["numerator"]), int(v["denominator"]))
    return F(int(v[0]), int(v[1]))


def main():
    p, run, result = load(PRIMARY/"run.json"), load(INDEP/"run.json"), load(INDEP/"result.json")
    agreement_path = HERE/"kronecker-independent-agreement.json"
    need(sha(agreement_path) == "5510285fed346165e428bac4dfcb572548283322937a712be6465829481b5779",
         "fixed actual agreement")
    agreement = load(agreement_path)
    need(agreement["status"] ==
         "PASS_ACTUAL_BLIND_DIRECT_ALL_PAIR_RECONSTRUCTION_AND_COMPLETE_COMPARISON", "agreement status")
    need(p["execution_status"] == "COMPLETE" and run["status"] ==
         "COMPLETE_DIRECT_GAUSSIAN_INDEPENDENT", "actual complete statuses")
    need(result["main_result_comparison"] == "NOT_PERFORMED_BLIND_OUTPUT_FROZEN_FIRST",
         "independent original result preserved")
    pins = {"run.json": "e4d54cf0690702f54029b4c36412d9d922e14a632090e5a4ac88f2e8b8e293e7",
            "result.json": "af998444847ef90696cc5e18fb716d60f2625748a98d2d11438e0f73b009853f"}
    for name, pin in pins.items():
        need(sha(INDEP/name) == pin, "independent fixed record: "+name)
    bindings = {}
    for name, expected in agreement["input_sha256"].items():
        need(sha(HERE/name) == expected, "comparison input bytes: "+name)
        bindings[name] = expected
    agreement_binding_count = len(bindings)
    need(agreement_binding_count == 32, "comparison binding count")
    old = load(HERE/"kronecker-primary-record-check.json")
    for name, expected in old["input_sha256"].items():
        need(sha(HERE/name) == expected, "previous primary audit input bytes: "+name)
        bindings[name] = expected
    for key in ("source_sha256", "input_sha256", "checkout", "config_sha256"):
        need(run[key] == result[key], "shared run/result field: "+key)
    need(p["inputs"]["archive_pins"] == run["input_sha256"], "same original input pins")
    need(run["checkout"]["commit"] == agreement["independent_source_commit"] ==
         "49bf28aad70bdcb4adde2fd2cccc0e6b84544f1c", "independent HEAD record")
    need(p["source_commit"]["git_HEAD"] == agreement["primary_source_commit"] ==
         "7943df9127f28ceda67cffcc9b60311ec1f635c1", "primary HEAD record")
    canonical = (json.dumps(run["config"], sort_keys=True, separators=(",", ":"),
                            ensure_ascii=False, allow_nan=False)+"\n").encode()
    need(hashlib.sha256(canonical).hexdigest() == run["config_sha256"], "independent config hash")
    need((run["completed_rows"], run["completed_pairs"], result["completed_rows"],
          result["ordered_pairs"], result["output_count"], result["scalar_count"],
          result["scalar_integer_multiplications"]) ==
         (4912, 24127744, 4912, 24127744, 35937, 71874, 96510976), "full loop metadata")
    c = agreement["comparison"]
    expected_counts = {"center_scalars_equal": 29472, "tensor_scalars_equal": 71874,
                       "complex_outputs_equal": 35937, "ordered_pairs_independently_executed": 24127744,
                       "rounding_witnesses_checked": 29472, "ties": 0}
    for key, value in expected_counts.items():
        need(c[key] == value, "saved comparison count: "+key)
    d = p["rounding_and_error"]
    for key, primary_key in (("M_from_independent_witnesses", "M"),
                              ("delta_from_independent_witnesses", "delta"),
                              ("E0", "future_full_operator_E0"),
                              ("E2", "future_full_operator_E2")):
        need(frac(c[key]) == frac(d[primary_key]), "saved aggregate equality: "+key)
    need(frac(c["E0"]) < F(1, 10**23) and frac(c["E2"]) < F(8, 10**21),
         "saved aggregate readable bounds")
    need([v["in_memory_mutation"] for v in agreement["negative_controls"]] ==
         ["center_scalar", "tensor_real", "tensor_imag", "pair_count", "denominator", "rounding_witness"],
         "six saved negative-control cases")
    need(all(v["rejected_by"] for v in agreement["negative_controls"]), "saved rejection reasons")
    specs = {v["file"]: v for v in run["output_files"]}
    need(len(specs) == 4, "independent artifact count")
    for name, spec in specs.items():
        need(sha(INDEP/name) == spec["sha256"] and
             (INDEP/name).stat().st_size == spec["bytes"], "independent artifact bytes: "+name)
    for spec in result["output_files"]:
        need(spec == specs[spec["file"]], "result artifact pointer")
    need(result["tensor_file"] == specs["tensor12-direct.i240le.bin"], "tensor pointer")
    need(specs["centers-independent.i112le.bin"]["bytes"] == 4912*6*14 and
         specs["tensor12-direct.i240le.bin"]["bytes"] == 35937*2*30, "independent binary widths")
    need(int(result["tensor_denominator"]) == 1 << 192, "tensor units")
    witness_spec = specs["rounding-witnesses.json.gz"]
    content = gzip.decompress((INDEP/"rounding-witnesses.json.gz").read_bytes())
    need(len(content) == witness_spec["canonical_json_bytes"] and
         hashlib.sha256(content).hexdigest() == witness_spec["canonical_json_sha256"],
         "witness canonical bytes")
    witness = json.loads(content)
    need(witness["schema"] == "independent-q96-fraction-rounding-v1" and witness["node"] == 1280 and
         witness["input_sha256"] == run["input_sha256"] and len(witness["entries"]) == 4912,
         "witness header and outer shape only")
    # Deliberately do not inspect/recompute the 29472 individual rational witnesses.
    progress = [json.loads(line) for line in (INDEP/"progress.jsonl").read_text().splitlines()]
    rows = [v for v in progress if v["stage"] == "DIRECT_CONVOLUTION_ROWS"]
    expected_rows = list(range(128, 4913, 128))
    if expected_rows[-1] != 4912:
        expected_rows.append(4912)
    need([v["completed_rows"] for v in rows] == expected_rows, "saved completed row checkpoints")
    need(all(v["completed_pairs"] == 4912*v["completed_rows"] for v in rows), "saved progress counts")
    resources = {}
    for label, folder, logname, obskey, hashkey, byteskey in (
        ("primary", PRIMARY, "kronecker-block-root-recovery-run.log", "final_observation",
         "sha256", "output_bytes"),
        ("independent", INDEP, "kronecker-direct-independent.stdout.log",
         "post_write_budget_observation", "run_sha256", "archive_bytes")):
        path = HERE/logname
        last = json.loads(path.read_text().splitlines()[-1])
        need(last[hashkey] == sha(folder/"run.json"), "final stdout/run binding")
        actual = sum(v.stat().st_size for v in folder.iterdir() if v.is_file())
        obs = last[obskey]
        need(actual == obs[byteskey], "actual final directory bytes")
        total = actual + path.stat().st_size
        if label == "independent":
            stderr = HERE/"kronecker-direct-independent.stderr.log"
            need(stderr.stat().st_size == 0, "independent stderr")
            total += stderr.stat().st_size
        need(obs["wall_seconds"] < 60 and obs["peak_rss_bytes"] < 256*(1 << 20) and
             total < 8*(1 << 20)-256*(1 << 10), "saved resource limits")
        need(agreement["resources"][label]["including_logs_bytes"] == total and
             agreement["resources"][label]["actual_directory_bytes"] == actual, "agreement resource link")
        resources[label] = {**obs, "actual_directory_bytes": actual, "including_logs_bytes": total}
    for name in ("KRONECKER_COMPLETE_OUTCOME.md", "kronecker-independent-agreement.json",
                 "kronecker-primary-record-check.json", "kronecker-primary-record-check.stdout.txt",
                 Path(__file__).name):
        bindings[name] = sha(HERE/name)
    output = {"status": "PASS_FINAL_KRONECKER_METADATA_AND_BYTE_AUDIT",
              "scientific_kernel_reexecuted": False, "node_arrays_decoded": False,
              "per_mode_arithmetic_or_comparison_reexecuted": False,
              "rounding_witness_arithmetic_reexecuted": False,
              "negative_controls_reexecuted": False,
              "comparison_bindings_checked": agreement_binding_count,
              "saved_direct_row_checkpoints_checked": len(rows),
              "saved_counts": expected_counts, "resources": resources,
              "input_sha256": bindings,
              "environment": {"python": sys.version, "executable": sys.executable},
              "scope": "One completed dyadic tensor block; no added residual or NS conclusion."}
    path = HERE/"kronecker-complete-final-record-check.json"
    with path.open("x") as stream:
        json.dump(output, stream, sort_keys=True, indent=2)
        stream.write("\n")
    print(json.dumps({"status": output["status"], "input_bindings": len(bindings),
                      "saved_row_checkpoints": len(rows), "resources": resources,
                      "output_sha256": sha(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
