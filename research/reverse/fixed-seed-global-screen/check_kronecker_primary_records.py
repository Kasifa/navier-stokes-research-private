#!/usr/bin/env python3
"""Saved-byte/metadata audit only: no packing, balanced decoding or convolution."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
RUN = HERE / "kronecker-block-trial-02"


def need(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def frac(value):
    return F(int(value["numerator"]), int(value["denominator"]))


def pair(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def main():
    r = json.loads((RUN / "run.json").read_bytes())
    need(sha(RUN / "run.json") ==
         "375921aff0ceae1294b7d79947d9dfeaf817ad65ce9edc6c02b9b152ac922d70", "run pin")
    need(r["execution_status"] == "COMPLETE" and
         r["mathematical_status"] == "ONE_FIXED_COMPLEX_TENSOR_BLOCK_VERIFIED", "completion")
    need(r["source_commit"]["git_HEAD"] ==
         "7943df9127f28ceda67cffcc9b60311ec1f635c1", "recorded execution HEAD")
    bindings = {}
    for table in (r["inputs"]["source_sha256"], r["inputs"]["archive_pins"]):
        for name, expected in table.items():
            p = Path(name) if Path(name).is_absolute() else HERE / name
            need(p.is_relative_to(HERE), "input outside this task")
            need(sha(p) == expected, "input bytes: " + name)
            bindings[str(p.relative_to(HERE))] = expected
    cfg = r["inputs"]["config"]
    need((cfg["node_index"], cfg["center_Q"], cfg["components_one_based"],
          cfg["spatial_radix"], cfg["coefficient_bits"],
          cfg["general_large_products"], cfg["output_digits"]) ==
         (1280, 1 << 96, [1, 2], 33, 240, 3, 35937), "fixed configuration")
    canonical = json.dumps({"config": cfg, "proof_pins": r["inputs"]["proof_pins"],
                            "archive_pins": r["inputs"]["archive_pins"]},
                           sort_keys=True, separators=(",", ":"), allow_nan=False).encode("ascii")
    need(hashlib.sha256(canonical).hexdigest() == r["inputs"]["config_sha256"],
         "config hash")
    expected_widths = {"c96-centers.i112le.bin": 4912 * 6 * 14,
                       **{"product-%d.signed-le.bin" % j: 35937 * 30 for j in range(3)},
                       "tensor12-complex.i240le.bin": 35937 * 2 * 30}
    need(set(r["artifacts"]) == set(expected_widths), "five expected artifacts")
    binaries = {}
    for name, width in expected_widths.items():
        p, spec = RUN / name, r["artifacts"][name]
        need(p.stat().st_size == spec["bytes"] == width, "binary width: " + name)
        need(sha(p) == spec["sha256"], "binary bytes: " + name)
        need(spec["actual_readback"] == "PASS", "saved readback status")
        bindings[str(p.relative_to(HERE))] = spec["sha256"]
        binaries[name] = {"bytes": width, "sha256": spec["sha256"]}
    need(sum(expected_widths.values()) == 5803158, "fixed binary total")
    need(len(r["products"]) == 3, "product count")
    signs = []
    for index, item in enumerate(r["products"]):
        need(item["index"] == index and item["formula"] ==
             ["U*X", "V*Y", "(U+V)*(X+Y)"][index], "product identity")
        p = RUN / item["product_file"]
        data = p.read_bytes()
        z = int.from_bytes(data, "little", signed=True)
        negative = z < 0
        need(negative == bool(data[-1] & 128) == item["product_negative"], "signed product")
        need(abs(z).bit_length() == item["product_absolute_bit_length"], "product bit length")
        need(sha(p) == item["product_sha256"], "product record hash")
        need(item["terminal_carry"] == int(negative) and
             item["terminal_quotient"] == 0, "saved terminal carry/sign identity")
        need(item["decoded_coefficients"] == 35937 and
             item["raw_coefficient_bound_strict_2pow233"] == "PASS", "saved decoding checks")
        left, right = item["inputs"]
        need(left["signed_fixed_width_bytes"] == right["signed_fixed_width_bytes"] ==
             17969 * 30, "input width metadata")
        need(left["sign"] * right["sign"] == (z > 0)-(z < 0), "input/output sign metadata")
        signs.append({"index": index, "negative_from_raw_bytes": negative,
                      "actual_abs_bit_length": abs(z).bit_length(),
                      "reported_terminal_carry": item["terminal_carry"],
                      "reported_terminal_quotient": item["terminal_quotient"],
                      "balanced_decoding_reexecuted": False})
        del z, data
    a = r["rounding_and_error"]
    D, L, Qp = int(a["D"]), int(a["L"]), int(a["center_denominator"])
    need(D == (1 << 53)*L and Qp == 1 << 96, "stored denominators")
    M, delta = frac(a["M"]), frac(a["delta"])
    need(M == F(int(a["sum_abs_A"]), D), "stored M full-sum normalization")
    need(delta == F(int(a["sum_abs_QpA_minus_DC"]), D*Qp),
         "stored delta full-sum normalization")
    need(a["scalar_count"] == 4912*6 and a["ties_to_even_count"] == 0,
         "rounding metadata count")
    need(2*int(a["maximum_abs_rounding_error_numerator_over_D_Qp"]) <= D,
         "stored maximum rounding remainder bound")
    E0, E2 = 28*(2*M*delta+delta*delta), 28**3*(2*M*delta+delta*delta)
    need(E0 == frac(a["future_full_operator_E0"]) and
         E2 == frac(a["future_full_operator_E2"]), "stored E expressions")
    need(0 <= M < 1 << 28 and 0 <= delta <= F(14736, 1 << 96) < F(1, 1 << 82),
         "M/delta coarse allowance")
    need(E0 < F(1, 1 << 47) and E2 < F(1, 1 << 37), "E coarse allowances")
    need(E0 < F(1, 10**23) and E2 < F(8, 10**21), "readable exact E allowances")
    need(a["center_divergence_not_assumed"] and a["perturbation_is_not_a_residual_bound"],
         "input-perturbation scope")
    tensor = r["complete_tensor_checks"]
    need(int(tensor["tensor_denominator"]) == 1 << 192 and
         tensor["complex_output_count"] == 35937 and tensor["large_products_executed"] == 3,
         "tensor denominator/count")
    zero = r["zero_frequency_direct_check"]
    need(zero["ordered_terms"] == 4912 and zero["output_index"] == 17968 and
         zero["physical_k"] == [0, 0, 0] and int(zero["denominator"]) == 1 << 192,
         "saved zero-mode direct-check metadata")
    need(int(zero["real_numerator"]) == int(zero["imaginary_numerator"]) == 0,
         "saved zero-mode value")
    logpath = HERE / "kronecker-block-root-recovery-run.log"
    lines = [json.loads(line) for line in logpath.read_text().splitlines()]
    need([line["kronecker_progress"]["completed_large_products"] for line in lines[:-1]] ==
         [1, 2, 3], "three saved progress records")
    last = lines[-1]
    need(last["execution_status"] == "COMPLETE" and last["sha256"] == sha(RUN / "run.json"),
         "final stdout connects run")
    obs = last["final_observation"]
    actual = sum(p.stat().st_size for p in RUN.iterdir() if p.is_file())
    need(actual == obs["output_bytes"] == 5813537, "post-write directory size")
    need(obs["wall_seconds"] < 60 and obs["peak_rss_bytes"] < 256*(1 << 20),
         "saved final resource limits")
    total_with_log = actual + logpath.stat().st_size
    need(total_with_log < 8*(1 << 20)-128*(1 << 10), "output including external log")
    need(sha(HERE / "kronecker-block-trial-01/run.json") ==
         "44d05321296a6b25b3997495601cc9623a8fd6562b6dfd13f08dedcbbd99fcbc",
         "original failure retained")
    additions = [
        "kronecker-block-trial-02/run.json", "kronecker-block-trial-02/RUN_CLAIM.json",
        "kronecker-block-root-recovery-run.log", "KRONECKER_STARTUP_RECOVERY.md",
        "KRONECKER_STARTUP_RECOVERY_REVIEW.md", "KRONECKER_DECODING_INDEPENDENT_REVIEW.md",
        "KRONECKER_BLOCK_ROOT_REVIEW.md", "kronecker-startup-recovery-root-check.json",
        "KRONECKER_PRIMARY_COST_OUTCOME.md", "kronecker-primary-root-readback.json",
        "kronecker-block-trial-01/run.json", Path(__file__).name,
    ]
    for name in additions:
        bindings[name] = sha(HERE / name)
    output = {
        "status": "PASS_PRIMARY_SAVED_RECORDS_AND_BINARY_IDENTITIES",
        "independent_full_convolution": False,
        "scientific_kernel_or_nodes_reexecuted": False,
        "binary_width_hash_checks": binaries,
        "raw_product_sign_and_saved_carry_checks": signs,
        "recomputed_from_stored_scalar_sums": {"M": pair(M), "delta": pair(delta),
                                              "E0": pair(E0), "E2": pair(E2)},
        "strict_readable_input_perturbation_uppers": {"E0": pair(F(1, 10**23)),
                                                     "E2": pair(F(8, 10**21))},
        "full_node_sums_recomputed": False, "three_large_products_recomputed": False,
        "zero_frequency_direct_sum_recomputed": False,
        "resources": {**obs, "actual_directory_bytes": actual,
                      "external_log_bytes": logpath.stat().st_size,
                      "including_external_log_bytes": total_with_log},
        "input_sha256": bindings,
        "environment": {"python": sys.version, "executable": sys.executable},
        "scope": "One primary fixed tensor block; input perturbation allowances are not residuals.",
    }
    p = HERE / "kronecker-primary-record-check.json"
    with p.open("x") as stream:
        json.dump(output, stream, sort_keys=True, indent=2)
        stream.write("\n")
    print(json.dumps({"status": output["status"], "input_bindings": len(bindings),
                      "binary_files": len(binaries), "products_metadata": len(signs),
                      "resources": output["resources"], "record_sha256": sha(p)},
                     sort_keys=True))


if __name__ == "__main__":
    main()
