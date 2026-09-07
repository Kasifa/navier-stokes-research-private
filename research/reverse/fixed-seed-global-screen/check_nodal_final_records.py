#!/usr/bin/env python3
"""Parse existing residual records and rehash files. No node decoding/convolution."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import sys

HERE = Path(__file__).resolve().parent


def need(ok, message):
    if not ok:
        raise ValueError(message)


def read(name):
    return json.loads((HERE/name).read_text())


def fraction(value):
    return F(int(value["numerator"]), int(value["denominator"]))


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    primary = read("nodal-residual-trial-01/exact-result.json")
    independent = read("nodal-residual-independent-trial-01/run.json")
    run = read("nodal-residual-trial-01/run.json")
    selection = read("nodal-residual-trial-01/selection.json")
    agreement = read("nodal-residual-independent-agreement.json")
    witness = read("nodal-residual-root-witness.json")
    need(run["status"] == "COMPLETE_FIXED_NODE_LOWER_TRIAL", "primary incomplete")
    need(independent["execution_status"] == "COMPLETE", "independent incomplete")
    need(primary["node"] == independent["node"] == selection["node"] == 1280, "wrong node")
    need(fraction(primary["time"]) == F(5, 8), "wrong time")
    need(fraction(primary["P32_argument"]) == F(5, 2), "wrong exponential argument")
    need(primary["selected_modes"] == selection["selected_modes"], "selection mismatch")
    modes = primary["selected_modes"]
    need(len(modes) == len({tuple(k) for k in modes}) == 24, "non-distinct mode set")
    need(all(sorted(map(abs, k)) == [4, 4, 9] for k in modes), "unexpected mode orbit")
    need(primary["p_visits"] == 24*4912, "incorrect input visit count")
    D = int(primary["D"])
    need(D == 2**53*int(primary["L"]) and int(primary["D4"]) == D**4, "denominator relation")
    total, pairs = F(0), 0
    need(len(primary["outputs"]) == len(independent["mode_results"]) == 24, "output count")
    for index in range(24):
        a, b = primary["outputs"][index], independent["mode_results"][index]
        k = modes[index]
        need(a["k"] == b["k"] == k, "mode order mismatch")
        s = sum(x*x for x in k)
        need(s == a["squared_frequency"] == b["k_squared"] == 113, "frequency weight")
        expected_pairs = math.prod(17-abs(x) for x in k)
        need(expected_pairs == 1352 == a["ordered_pair_count"] == b["ordered_pairs"],
             "box-intersection pair count")
        need(b["diagonal_pairs"] == 0 and 2*b["unordered_distinct_pairs"] == expected_pairs,
             "unordered-pair accounting")
        need(a["ordered_pair_sequence_sha256"] == b["ordered_pair_stream_sha256"],
             "saved ordered coverage hashes differ")
        pairs += expected_pairs
        # Algebra only on previously saved sums: no p+q summation occurs here.
        full = [(fraction(c["real"]), fraction(c["imag"])) for c in b["F_unprojected"]]
        dot = [sum((k[j]*full[j][part] for j in range(3)), F(0)) for part in range(2)]
        subtotal = F(0)
        for j in range(3):
            need(full[j] == (F(int(a["F_real"][j]), D**2),
                             F(int(a["F_imag"][j]), D**2)), "saved F mismatch")
            projected = tuple(full[j][part]-F(k[j], s)*dot[part] for part in range(2))
            need(projected == (fraction(b["F_projected"][j]["real"]),
                               fraction(b["F_projected"][j]["imag"])), "saved projection algebra")
            need(fraction(b["linear_d_plus_k2c"][j]["real"]) == 0 and
                 fraction(b["linear_d_plus_k2c"][j]["imag"]) == 0, "outside-G linear part")
            residual = (-projected[1], projected[0])
            need(residual == (fraction(b["R"][j]["real"]), fraction(b["R"][j]["imag"])),
                 "saved iP F residual algebra")
            need(residual == (F(int(a["T_real"][j]), D**2*s),
                              F(int(a["T_imag"][j]), D**2*s)), "saved primary residual")
            subtotal += sum((value*value for value in residual), F(0))
        weighted = s*s*subtotal
        need(weighted == fraction(b["weighted_R_squared"]) ==
             F(int(a["squared_H2_contribution_numerator_over_D4"]), D**4),
             "mode contribution mismatch")
        total += weighted
    need(pairs == 32448, "total ordered-pair count")
    need(total == fraction(primary["r2_squared_lower"]) ==
         fraction(independent["result"]["Lambda"]) == F(int(primary["N"]), D**4),
         "saved Lambda mismatch")
    polynomial = sum((F(5**j, 2**j*math.factorial(j)) for j in range(33)), F(0))
    need(polynomial == fraction(primary["P32"]) ==
         fraction(independent["result"]["P32_of_5_over_2"]), "saved P32 mismatch")
    necessity = total*polynomial
    need(necessity == fraction(primary["necessary_epsilon_squared_lower"]) ==
         fraction(independent["result"]["necessary_epsilon_squared_lower"]), "necessity mismatch")
    need(F(1, 10**14) < necessity < F(4, 10**14), "fixed threshold comparison")
    need(13*total < F(4, 10**14), "finite Lambda cannot refute larger fixed threshold")
    left, right = 10**14*int(primary["N"])*polynomial.numerator, D**4*polynomial.denominator
    need(left == int(primary["integer_left"]) and right == int(primary["integer_right"]) and
         left-right == int(primary["integer_margin"]) > 0, "primary integer witness")
    secondary = independent["result"]["old_threshold_comparison"]
    need(int(secondary["lhs"]) == necessity.numerator*10**14 and
         int(secondary["rhs"]) == necessity.denominator and
         int(secondary["difference"]) == necessity.numerator*10**14-necessity.denominator > 0,
         "independent integer witness")
    P8 = sum((F(5**j, 2**j*math.factorial(j)) for j in range(9)), F(0))
    need(P8 == F(3588667, 294912) > F(121, 10), "short polynomial witness")
    need(total > F(83, 10**17) and F(83, 10**17)*F(121, 10) ==
         F(10043, 10**18) > F(1, 10**14), "readable strict witness")
    need(witness["r2_squared_lower_greater_than"] == ["83", "100000000000000000"],
         "root readable witness transcription")
    need(agreement["comparison"]["ordered_pairs"] == pairs and
         fraction(agreement["comparison"]["Lambda"]) == total and
         fraction(agreement["comparison"]["necessary_epsilon_squared_lower"]) == necessity,
         "stored agreement mismatch")
    need([x["in_memory_mutation"] for x in agreement["negative_controls"]] ==
         ["F", "R", "weight", "coverage", "N", "P32"], "stored mutation record inventory")
    need(all(x["rejected_by"] for x in agreement["negative_controls"]), "missing rejection reason")
    bindings = {}
    for name, expected in agreement["input_sha256"].items():
        need(digest(HERE/name) == expected, "agreement bound file changed: "+name)
        bindings[name] = expected
    for folder in ("nodal-residual-trial-01", "nodal-residual-independent-trial-01"):
        for path in sorted((HERE/folder).iterdir()):
            if path.is_file():
                bindings[str(path.relative_to(HERE))] = digest(path)
    additional = [
        "NODAL_RESIDUAL_OUTCOME.md", "NODE_TRIAL_OUTCOME.md",
        "NODAL_RESIDUAL_ROOT_REVIEW.md", "NODAL_RESIDUAL_CONTRACT_REVIEW.md",
        "INDEPENDENT_NODAL_RESIDUAL_CONTRACT.md",
        "nodal-residual-independent-agreement.json", "nodal-residual-root-witness.json",
        "nodal-residual-root-run.log", "independent-nodal-residual.stdout.log",
        "independent-nodal-residual.stderr.log", Path(__file__).name,
    ]
    for name in additional:
        bindings[name] = digest(HERE/name)
    source_dir_bytes = sum(p.stat().st_size for p in (HERE/"nodal-residual-trial-01").iterdir() if p.is_file())
    independent_dir_bytes = sum(p.stat().st_size for p in (HERE/"nodal-residual-independent-trial-01").iterdir() if p.is_file())
    need(source_dir_bytes == 2752701 and independent_dir_bytes == 78516, "actual evidence directory size")
    result = {
        "status": "PASS_EXISTING_RECORD_ARITHMETIC_AND_HASH_AUDIT",
        "scope": "No node decoding, convolution, FFT, integration, selection or mutation rerun. Algebra uses saved F/R only.",
        "python": sys.version, "modes": 24, "ordered_pairs": pairs,
        "existing_complex_F_components_checked": 72, "existing_complex_R_components_checked": 72,
        "saved_projection_and_outside_G_linear_algebra_checked": True,
        "readable_old_threshold_witness_verified": True,
        "P32_necessary_square_below_2e_minus_7_square": True,
        "thirteen_Lambda_below_2e_minus_7_square": True,
        "stored_mutation_records_read": 6, "mutations_executed_in_this_check": 0,
        "node_convolution_executions_in_this_check": 0,
        "agreement_input_bindings_verified": len(agreement["input_sha256"]),
        "primary_directory_bytes": source_dir_bytes, "independent_directory_bytes": independent_dir_bytes,
        "input_sha256": bindings,
    }
    output = HERE/"nodal-residual-final-record-check.json"
    with output.open("x") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"status": result["status"], "bindings": len(bindings), "output": output.name,
                      "sha256": digest(output), "no_node_recomputation": True}))


if __name__ == "__main__":
    main()
