#!/usr/bin/env python3
"""Compare frozen full integer outputs and independent rounding witnesses.

No node decoding, packing, direct convolution, or scientific kernel replay.
"""
import copy
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAIN = HERE / "kronecker-block-trial-02"
INDEP = HERE / "kronecker-direct-independent-trial-01"
Q96 = 1 << 96


def need(value, label):
    if not value:
        raise ValueError(label)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_bytes())


def frac(obj):
    return F(int(obj["numerator"]), int(obj["denominator"]))


def pair(value):
    return [str(value.numerator), str(value.denominator)]


def decode(path, width, count):
    blob = path.read_bytes()
    need(len(blob) == width * count, "fixed scalar binary length")
    return [int.from_bytes(blob[i*width:(i+1)*width], "little", signed=True)
            for i in range(count)]


def compare(data):
    a, b = data["main_centers"], data["independent_centers"]
    x, y = data["main_tensor"], data["independent_tensor"]
    need(len(a) == len(b) == 29472, "center count")
    need(len(x) == len(y) == 71874, "output scalar count")
    need(data["ordered_pairs"] == 24127744, "complete ordered-pair count")
    need(data["tensor_denominator"] == 1 << 192, "tensor denominator")
    for i in range(29472):
        need(a[i] == b[i], "center scalar mismatch at %d" % i)
        need(abs(a[i]) < 1 << 109, "center scalar bound")
    for i in range(71874):
        need(x[i] == y[i], "tensor scalar mismatch at %d" % i)
        need(abs(x[i]) < 1 << 235, "tensor scalar bound")
    w = data["witnesses"]
    need(len(w) == 4912 and all(len(row) == 6 for row in w), "witness shape")
    M, delta, ties = F(0), F(0), 0
    for i, row in enumerate(w):
        for j, item in enumerate(row):
            need(len(item) == 5, "witness field count")
            n, d, q, r, c = map(int, item)
            need(d > 0 and 0 <= r < d and n == d*q+r, "witness Euclidean division")
            reduced = F(n, d)
            need((reduced.numerator, reduced.denominator) == (n, d), "normalized Fraction witness")
            expected = q + int(2*r > d or (2*r == d and q % 2 != 0))
            need(c == expected == b[6*i+j], "witness ties-even center")
            need(2*abs(n-d*c) <= d, "witness rounding radius")
            ties += int(2*r == d)
            M += abs(reduced) / Q96
            delta += abs(reduced-c) / Q96
    need(M == data["main_M"], "independent witness M sum")
    need(delta == data["main_delta"], "independent witness delta sum")
    E0, E2 = 28*(2*M*delta+delta*delta), 28**3*(2*M*delta+delta*delta)
    need(E0 == data["main_E0"] and E2 == data["main_E2"], "input error expression")
    need(E0 < F(1, 10**23) and E2 < F(8, 10**21), "input error readable bounds")
    return {"center_scalars_equal": len(a), "tensor_scalars_equal": len(x),
            "complex_outputs_equal": len(x)//2, "ordered_pairs_independently_executed": 24127744,
            "rounding_witnesses_checked": 29472, "ties": ties,
            "M_from_independent_witnesses": pair(M), "delta_from_independent_witnesses": pair(delta),
            "E0": pair(E0), "E2": pair(E2)}


def main():
    primary, run, result = load(MAIN/"run.json"), load(INDEP/"run.json"), load(INDEP/"result.json")
    need(primary["execution_status"] == "COMPLETE", "primary complete")
    need(run["status"] == "COMPLETE_DIRECT_GAUSSIAN_INDEPENDENT", "independent complete")
    need(result["mathematical_status"] == "ONE_FIXED_DIRECT_GAUSSIAN_CONVOLUTION_RECOMPUTED", "independent result")
    need(result["main_result_comparison"] == "NOT_PERFORMED_BLIND_OUTPUT_FROZEN_FIRST", "blind result state")
    bindings = {}
    def bind(path, expected=None):
        path = path.resolve()
        need(path.is_relative_to(HERE), "unexpected path")
        actual = sha(path)
        need(expected is None or actual == expected, "file hash: " + path.name)
        bindings[str(path.relative_to(HERE))] = actual
    for name, pin in primary["inputs"]["source_sha256"].items():
        bind(Path(name), pin)
    need(primary["inputs"]["archive_pins"] == run["input_sha256"], "same original input pins")
    for table in [run["source_sha256"], run["input_sha256"]]:
        for name, pin in table.items():
            bind(HERE/name, pin)
    for field in ["source_sha256", "input_sha256", "config_sha256", "checkout"]:
        need(run[field] == result[field], "run/result shared field " + field)
    need(result["node"] == 1280 and result["time"] == ["1280", "2048"], "fixed node/time")
    need(result["tensor_components_one_based"] == [1, 2], "fixed tensor")
    need(result["completed_rows"] == run["completed_rows"] == 4912, "full outer rows")
    need(result["ordered_pairs"] == run["completed_pairs"] == 24127744, "full pair metadata")
    need(result["scalar_integer_multiplications"] == 96510976, "four products per pair")
    need(result["output_count"] == 35937 and result["scalar_count"] == 71874, "result output counts")
    specs = {v["file"]: v for v in run["output_files"]}
    need(set(specs) == {"centers-independent.i112le.bin", "rounding-witnesses.json.gz",
                        "tensor12-direct.i240le.bin", "result.json"}, "independent artifact set")
    for name, spec in specs.items():
        p = INDEP/name
        bind(p, spec["sha256"])
        need(p.stat().st_size == spec["bytes"], "independent artifact bytes")
    for spec in result["output_files"]:
        need(specs[spec["file"]] == spec, "result artifact description")
    need(result["tensor_file"] == specs["tensor12-direct.i240le.bin"], "tensor pointer")
    for name, spec in primary["artifacts"].items():
        p = MAIN/name
        bind(p, spec["sha256"])
        need(p.stat().st_size == spec["bytes"], "primary artifact bytes")
    raw = gzip.decompress((INDEP/"rounding-witnesses.json.gz").read_bytes())
    spec = specs["rounding-witnesses.json.gz"]
    need(hashlib.sha256(raw).hexdigest() == spec["canonical_json_sha256"], "witness canonical bytes")
    need(len(raw) == spec["canonical_json_bytes"], "witness canonical length")
    witness = json.loads(raw)
    need(witness["schema"] == "independent-q96-fraction-rounding-v1" and witness["node"] == 1280, "witness schema")
    need(witness["input_sha256"] == run["input_sha256"], "witness input binding")
    need(witness["entry_fields"] == ["scaled_numerator", "scaled_denominator", "floor_quotient", "remainder", "rounded"], "witness fields")
    d = primary["rounding_and_error"]
    data = {"main_centers": decode(MAIN/"c96-centers.i112le.bin",14,29472),
            "independent_centers": decode(INDEP/"centers-independent.i112le.bin",14,29472),
            "main_tensor": decode(MAIN/"tensor12-complex.i240le.bin",30,71874),
            "independent_tensor": decode(INDEP/"tensor12-direct.i240le.bin",30,71874),
            "ordered_pairs": result["ordered_pairs"], "tensor_denominator": int(result["tensor_denominator"]),
            "witnesses": witness["entries"], "main_M": frac(d["M"]), "main_delta": frac(d["delta"]),
            "main_E0": frac(d["future_full_operator_E0"]), "main_E2": frac(d["future_full_operator_E2"])}
    comparison = compare(data)
    mutations = []
    for kind in ["center_scalar", "tensor_real", "tensor_imag", "pair_count", "denominator", "rounding_witness"]:
        bad = dict(data)
        if kind == "center_scalar":
            bad["independent_centers"] = list(data["independent_centers"])
            bad["independent_centers"][0] += 1
        elif kind in ["tensor_real", "tensor_imag"]:
            bad["independent_tensor"] = list(data["independent_tensor"])
            bad["independent_tensor"][int(kind == "tensor_imag")] += 1
        elif kind == "pair_count":
            bad["ordered_pairs"] -= 1
        elif kind == "denominator":
            bad["tensor_denominator"] += 1
        else:
            bad["witnesses"] = copy.deepcopy(data["witnesses"])
            bad["witnesses"][0][0][3] = str(int(bad["witnesses"][0][0][3])+1)
        try:
            compare(bad)
        except ValueError as exc:
            mutations.append({"in_memory_mutation": kind, "rejected_by": str(exc)})
        else:
            raise AssertionError("negative control accepted: " + kind)
    resources = {}
    for label, folder, logname, hashkey, obskey, sizekey in [
        ("primary",MAIN,"kronecker-block-root-recovery-run.log","sha256","final_observation","output_bytes"),
        ("independent",INDEP,"kronecker-direct-independent.stdout.log","run_sha256","post_write_budget_observation","archive_bytes")]:
        lp=HERE/logname
        last=json.loads(lp.read_text().splitlines()[-1])
        bind(folder/"run.json",last[hashkey]);bind(lp)
        obs=last[obskey]
        actual=sum(p.stat().st_size for p in folder.iterdir() if p.is_file())
        need(actual==obs[sizekey],"final directory size")
        need(obs["wall_seconds"]<60 and obs["peak_rss_bytes"]<256*(1<<20),"final resource cap")
        total=actual+lp.stat().st_size
        if label=="independent":
            ep=HERE/"kronecker-direct-independent.stderr.log";bind(ep)
            need(ep.stat().st_size==0,"independent stderr")
            total+=ep.stat().st_size
        need(total<8*(1<<20)-256*(1<<10),"archive and external logs")
        resources[label]={**obs,"actual_directory_bytes":actual,"including_logs_bytes":total}
    for p in [Path(__file__),HERE/"KRONECKER_PRIMARY_RESULT_REVIEW.md",HERE/"KRONECKER_STARTUP_RECOVERY.md",
              HERE/"KRONECKER_STARTUP_RECOVERY_REVIEW.md",INDEP/"claim.json",INDEP/"progress.jsonl"]:
        bind(p)
    out={"status":"PASS_ACTUAL_BLIND_DIRECT_ALL_PAIR_RECONSTRUCTION_AND_COMPLETE_COMPARISON",
         "comparison":comparison,"negative_controls":mutations,"resources":resources,
         "primary_source_commit":primary["source_commit"]["git_HEAD"],"independent_source_commit":run["checkout"]["commit"],
         "source_sha256":bindings[Path(__file__).name],"input_sha256":bindings,
         "node_reconstruction_or_convolution_reexecuted_by_checker":False,
         "scope":"All scalars of one fixed dyadic tensor; witness sums independently connect M/delta. Not a full residual or NS conclusion."}
    p=HERE/"kronecker-independent-agreement.json"
    with p.open("x") as stream:
        json.dump(out,stream,sort_keys=True,indent=2);stream.write("\n")
    print(json.dumps({"status":out["status"],"comparison":comparison,"negative_controls_rejected":len(mutations),
                      "output_sha256":sha(p),"resources":resources},sort_keys=True))


if __name__=="__main__":
    main()
