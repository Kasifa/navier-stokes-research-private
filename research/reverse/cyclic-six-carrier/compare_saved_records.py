"""Compare already saved representations only; no Fourier, root or window computation."""
import hashlib
import json
from pathlib import Path
import subprocess

BASE = Path(__file__).resolve().parent
REL = "research/reverse/cyclic-six-carrier/"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canon(p):
    if "coefficients_low_to_high" in p:
        return {str(i): c for i, c in enumerate(p["coefficients_low_to_high"]) if c != "0"}
    return p["sparse_rational_coefficients"]


def vector(v):
    return [canon(p) for p in v]


names = ["exact-coefficients-output.json", "exact-roots-output.json", "verify-cyclic-output.json"]
a, b, c = [json.loads((BASE / name).read_text()) for name in names]
assert c["execution_status"] == "completed"
assert c["certification_status"] == "EXACT_COEFFICIENTS_ALL_ROOTS_AND_ORIGINAL_WINDOW_VERIFIED"
assert c["scientific_execution_count_in_this_invocation"] == 1
assert c["scientific_stage_completed"] is True
assert c["resource_checks_at_recorded_boundary"] == ["PASS"]
arecs = {(r["rotation_index"], r["sign"]): r for r in a["target_records"]}
counts = {"root_vectors": 0, "shape_vectors": 0, "root_normalized_vectors": 0}
for r in c["coefficient_computation"]["coefficient_records"]:
    ar = arecs[(r["rotation"], r["sign"])]
    assert r["target"] == ar["target"]
    for col, cr in r["columns"].items():
        ac = ar["columns"][col]
        assert set(cr["root_vectors"]) == set(ac["root_vectors"])
        for label, value in cr["root_vectors"].items():
            assert vector(value) == vector(ac["root_vectors"][label])
            counts["root_vectors"] += 1
        shapes = next(s for s in ac["all_nonempty_label_subsets"] if s["mask"] == 15)["ordered_tree_shapes"]
        assert {s.replace("*", "x") for s in cr["all_five_shapes"]} == set(shapes)
        for label, value in cr["all_five_shapes"].items():
            assert vector(value) == vector(shapes[label.replace("*", "x")])
            counts["shape_vectors"] += 1
assert counts["root_vectors"] == counts["shape_vectors"] == 60
assert canon(a["primary_matrices"]["P_determinant"]) == canon(c["coefficient_computation"]["independent_determinant"])
for br, cr in zip(b["roots"], c["stage_B_comparison"]["root_summaries_in_certified_order"]):
    for key in ["index", "rank", "eligible"]:
        assert br[key] == cr[key]
    assert br["original_P_root_multiplicity"] == cr["original_multiplicity"]
    assert b["isolation_nodes"][br["initial_node"]]["interval"] == cr["initial_half_open_interval"]
    n = br["normalized_polynomials"]
    for key in ["v", "w"]:
        assert canon(b["polynomials"][n[key]]) == canon(cr[key + "_polynomial"])
    for key in ["C", "Z"]:
        assert vector([b["polynomials"][i] for i in n[key]]) == vector(cr[key + "_polynomials"])
        counts["root_normalized_vectors"] += 1
w = c["stage_B_comparison"]["independently_recomputed_original_main_window"]
bw = b["selected_window"]
assert w["original_main_T"] == bw["T"]
assert w["smaller_window_substituted"] is False
for key in ["selected_root_index", "first_nonzero_C_coordinate_index", "alpha_closed_enclosure", "C_coordinate_closed_enclosure", "three_time_candidates_in_contract_order"]:
    assert w[key] == bw[key]
for key, value in w["computed_constants"].items():
    assert value == bw[key]
for saved, original in zip(w["exact_budgets"], bw["exact_budget_certificates"]):
    for key in ["name", "left", "right", "slack"]:
        assert saved[key] == original[key]
objects = []
for filename, commit in [
    ("exact_coefficients.py", "9e606f2d7d39969eb39b7e9088903c75a6909ee8"),
    ("exact_roots.py", "f49ebe2a6ed7b7111ade1effaf3be253807e08e0"),
    ("verify_cyclic.py", "2b1c213ba5ff7a259a2a5655eb0c9cf4d9615db9"),
]:
    assert (BASE / filename).read_bytes() == subprocess.check_output(["git", "show", commit + ":" + REL + filename])
    objects.append({"path": REL + filename, "source_commit": commit, "sha256": digest(BASE / filename)})
report = {"status": "PASS_EXISTING_RECORD_COMPARISON", "classification": "PRIVATE_CORE",
          "not_a_new_scientific_experiment": True,
          "scope": "Representation equality of saved A/C roots and five shapes; saved B/C normalization, root order and original window. No regenerated coefficients, determinant, roots or constants.",
          "input_sha256": {n: digest(BASE / n) for n in names}, "source_objects": objects,
          "comparison_counts": counts, "original_main_T_identical": True,
          "script_sha256": digest(Path(__file__).resolve())}
out = BASE / "root-output-comparison.json"
with out.open("x") as f:
    json.dump(report, f, indent=2)
    f.write("\n")
print(json.dumps(report, separators=(",", ":")))
