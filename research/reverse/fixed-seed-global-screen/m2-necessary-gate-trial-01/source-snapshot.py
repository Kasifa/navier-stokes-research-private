#!/usr/bin/env python3
"""One NI.4 necessary gate; default is ASCII/AST/configuration/byte pins only.

Only a root-reviewed --run decodes the fixed first layer and performs one sum.
No platform, subprocess, NumPy, dynamic import, helper, second representation,
new exponential evaluation, spatial kernel, parameter choice or retry.
"""
import time
START = time.monotonic()

import argparse
import ast
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import shlex
import signal
import stat
import sys
import traceback

HERE = Path(__file__).resolve().parent
TREE = HERE.parents[2]
OUT = HERE / "m2-necessary-gate-trial-01"
STDOUT, STDERR = (HERE/"m2-necessary-gate.stdout.log", HERE/"m2-necessary-gate.stderr.log")
CONTRACT = "M2_NECESSARY_GATE_EXECUTION_CONTRACT.md"
BFILE = "one-segment-residual-trial-01/hermite-b.i96le.bin"
OLD_EXP = "full-nodal-independent-trial-01/result.json"
CMP = "one-segment-residual-comparison-trial-01/"
FLAGS = {"producer_resource_complete": False, "resource_complete": False,
         "certificate_ready": False, "release_ready": False}
PINS = {
    "ONE_SEGMENT_NEXT_INPUT_SCOPE_AUDIT.md": "cecb56ff8cabe10bbce3d77fb1cef18458e4c32830f16220c1da69566937d490",
    "NODE_GATE_LEMMA.md": "177fe82983bb8d6d3e172615c716176338bdc7e31cd546e0416b502b80dd76fb",
    "FULL_NODAL_RESIDUAL_OUTCOME.md": "223c963e10ae14c93a231901dfe1554b8c61b63324537ebc250ddb7ae15d32ee",
    "FULL_NODAL_RESIDUAL_FINAL_REVIEW.md": "6d191cdb7be53601617754769b55b50be6346e5abfc2ca93083bf0518be7bc69",
    "full-nodal-agreement.json": "f2ccad0d3a963e1a0bdbf0e9695e2979271807201ef3427964b2a11052511ed8",
    OLD_EXP: "e637e7fcde5f2fa8ac7cf55d635ada579f6fae189ebf903b6a7a018c351e393b",
    BFILE: "ba831967f4eeaa69bd7d16674c1f3a0cda913c14ac864d1dcfc6518e3ed1067c",
    "node-trial-01/manifest.json": "5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd",
    "node-trial-01/modes.npy": "f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896",
    "node-trial-01/block-01280-01343.npz": "abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e",
    "ONE_SEGMENT_HIDDEN_HELPER_RESOURCE_AUDIT.md": "c971a90e0c7d230bd25df1dd80b2e27c74b9af089ad6194099e217e981a77c87",
    "ONE_SEGMENT_COMPARISON_RESOURCE_GAP_ADDENDUM.md": "212df48b07648511024524ab746d41ec3e419914cb111862ae3569663ccf9355",
    "ONE_SEGMENT_COMPARISON_RESOURCE_GAP_INDEPENDENT_REVIEW.md": "36141219e713ed8a72cb1c6cef9609d00e86aed36f7fd7d80e242d0331562e06",
    CMP+"comparison.json": "c0e454ac4fd980344c29704bdabb3e7dd8c00e00daac8942f3621d2c2428eba8",
    CMP+"run.json": "1130f56738d77a57f0227a2289b7a56fe543c49c5f86b2ba0a3dbc839247557a",
    CMP+"final-receipt.json": "2943f90b98b34513d225e4cfe7447444d13287c369e16677f6e84dd84d8f389a",
    "compare_one_segment_residual.py": "7e09b766feb86ac70bb1b05957903320d41069637d4c2ee23e8ebed88c6bd294",
    "ONE_SEGMENT_RESIDUAL_COMPARATOR_INDEPENDENT_REVIEW.md": "14bc674a61adca842a0cf09005451b1988800ef51bf5781abc3d290909421771",
    "ONE_SEGMENT_RESIDUAL_DENOMINATOR_LEMMA.md": "de6b150813559e6d0856b3df8db77491c9a3da4cad1f07a3d94282cd29642104",
    "ONE_SEGMENT_RESIDUAL_DENOMINATOR_INDEPENDENT_DERIVATION.md": "a9d6b288917eb98123afce1bd0f07bf879e530b53701ad9eb9e00f4c5a099171",
    "audit_one_segment_residual.py": "f8f871684d68303de24a8901abb35266969d2f978d218ca9d14cd16ce45fac63",
    "audit_one_segment_residual_independent.py": "1e9c9ee576049bd444ed07e858175b113bdb09d3719f1ab69820a3536564ca79",
    "one-segment-primary-root-execution-acceptance.json": "c4c8ea70c33918ddea1d7cce74b89e7e97e99ff9be7aa3f74e73e3633562770b",
    "one-segment-independent-root-execution-acceptance.json": "5265d2ebe8a3af7bd822ecdcef2f68a6e20a567f4d84135af2ccabd10f154c49",
}
# No placeholder hashes: fill only real contract/reviews/acceptances from root.
FINAL_PINS = {
    CONTRACT: "7ee3b897fd2c7cabd7fbeedb8c0c053130bcdd7e46fbc1dd1c602fa3a454e9cd",
    "ONE_SEGMENT_NEXT_INPUT_ROOT_REVIEW.md": "ad5c06c2e1da43f46ab6d74abc73db3987af9e9090b6911e46a6985ed13a0049",
    "one-segment-comparison-root-execution-acceptance.json": "35da6abd32a7b3cec346c11ca43661f5cadb7896dc37a24de6f19f76fed594ee",
    "ONE_SEGMENT_COMPARISON_EXECUTION_INDEPENDENT_REVIEW.md": "fe1986c2fc9fe78cc47663278296e10f76429bc399b1f784db3f361c4f9a0afd",
}
FINAL_REQUIRED = {CONTRACT, "ONE_SEGMENT_NEXT_INPUT_ROOT_REVIEW.md",
                  "one-segment-comparison-root-execution-acceptance.json",
                  "ONE_SEGMENT_COMPARISON_EXECUTION_INDEPENDENT_REVIEW.md"}
COMPARISON_STATUS = "ARITHMETIC_AGREEMENT_WITH_PRODUCER_RESOURCE_EVIDENCE_GAP"
COMPARISON_COMMIT = "2e7ded4313eddbe7c2d7cbefc503d7bcb671b154"
CONFIG = {"node": 1280, "time": [5, 8], "G_count": 4912, "components": 3,
          "layer": 0, "scalar_count": 29472, "scalar_bytes": 12,
          "archive_bytes": 1414656, "layer_bytes": 353664,
          "order": "power, original lexicographic G, component, real/imag; signed little-endian",
          "Q2_denominator": str(1 << 128), "threshold": [361, 25],
          "exponential_argument": [5, 4], "exponential_degree": 32,
          "wall_seconds": 60, "peak_rss_bytes": 256*1024**2, "output_bytes": 16*1024**2,
          "output_directory": str(OUT), "external_stdout": str(STDOUT), "external_stderr": str(STDERR),
          "single_process": True, "source_archive": BFILE, "zero_skipping": False,
          "second_full_sum": False, "second_representation": False, "retry": False}


class Failure(Exception):
    pass


class LimitStop(Exception):
    pass


def need(ok, message):
    if not ok:
        raise Failure(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
                       allow_nan=False)+"\n").encode("ascii")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_hash(actual, expected):
    need(all(isinstance(x, str) and len(x) == 64 and all(c in "0123456789abcdef" for c in x)
             for x in (actual, expected)), "SHA_FORMAT")
    need(actual == expected, "SOURCE_SHA_MISMATCH")


def verdict(difference):
    return "FIXED_REFERENCE_M2_ENVELOPE_REFUTED" if difference > 0 else "UNDECIDED_FOR_LINF"


def validate_verdict(difference, claimed):
    need(claimed == verdict(difference), "STRICT_NI4_BOUNDARY")


def ready():
    return set(FINAL_PINS) == FINAL_REQUIRED


def config_sha():
    return hashlib.sha256(canonical({"config": CONFIG, "pins": {**PINS, **FINAL_PINS}, **FLAGS})).hexdigest()


def preflight(run=False, review=None, review_sha=None):
    need(sys.version_info >= (3, 10) and sys.flags.optimize == 0, "PYTHON_VERSION_OPTIMIZATION")
    need(TREE == Path("/Users/kasifa/Documents/Math/navier-stokes-reverse"), "REVERSE_TREE_ONLY")
    raw = Path(__file__).read_bytes(); raw.decode("ascii")
    compile(ast.parse(raw), str(Path(__file__)), "exec")
    actual = {}
    for name, expected in {**PINS, **FINAL_PINS}.items():
        actual[name] = sha(HERE/name)
        validate_hash(actual[name], expected)
    need((HERE/BFILE).stat().st_size == CONFIG["archive_bytes"], "FULL_B_ARCHIVE_LENGTH")
    binding = None
    if review is not None or review_sha is not None:
        need(review is not None and review_sha is not None, "ROOT_REVIEW_PAIR")
        path = Path(review).resolve()
        need(path.parent == HERE, "ROOT_REVIEW_LOCAL_PATH")
        validate_hash(sha(path), review_sha)
        text = path.read_text()
        need(ready() and hashlib.sha256(raw).hexdigest() in text and FINAL_PINS[CONTRACT] in text,
             "ROOT_REVIEW_SOURCE_AND_CONTRACT_BINDING")
        binding = {"file": str(path), "sha256": review_sha}
    if run:
        need(ready() and binding is not None, "FINAL_CONTRACT_ACCEPTANCES_AND_ROOT_SOURCE_REVIEW_REQUIRED")
        need(sys.version_info[:3] == (3, 12, 14), "LOCKED_PYTHON_3_12_14")
        for fd, path in ((1, STDOUT), (2, STDERR)):
            a, b = os.fstat(fd), path.stat()
            need(stat.S_ISREG(a.st_mode) and a.st_size == 0
                 and (a.st_dev, a.st_ino) == (b.st_dev, b.st_ino), "EXCLUSIVE_EMPTY_STDIO_REQUIRED")
    return {"status": "STATIC_BYTE_PINS_PASS_SOURCE_REVIEW_NOT_BOUND" if ready() else "STATIC_BYTE_PINS_VALID_FINAL_LOCKS_PENDING",
            "B0_computed": False, "scientific_integers_decoded": False, "source_sha256": hashlib.sha256(raw).hexdigest(),
            "config_sha256": config_sha(), "config": CONFIG, "input_sha256": actual,
            "runtime_root_review": binding, "output_directory_exists": OUT.exists(), **FLAGS}


def observation():
    rss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*(1 if sys.platform == "darwin" else 1024)
    files = list(OUT.iterdir()) if OUT.exists() else []
    total = sum(p.stat().st_size for p in files if p.is_file())
    total += sum(p.stat().st_size for p in (STDOUT, STDERR) if p.exists())
    return {"elapsed_seconds": time.monotonic()-START, "self_peak_rss_bytes": rss,
            "all_output_bytes": total, "single_process_no_children": True}


def exceeded(obs):
    return (obs["elapsed_seconds"] >= 60 or obs["self_peak_rss_bytes"] > CONFIG["peak_rss_bytes"]
            or obs["all_output_bytes"] > CONFIG["output_bytes"])


def check_budget():
    if exceeded(observation()):
        raise LimitStop("OBSERVED_M2_GATE_BUDGET")


def save(name, value, new=False):
    path = OUT/name
    need(path.parent == OUT and (not new or not path.exists()), "OUTPUT_OVERWRITE")
    data = canonical(value)
    temp = OUT/(name+".tmp")
    with temp.open("xb") as stream:
        stream.write(data); stream.flush()
    temp.replace(path)
    need(path.read_bytes() == data, "METADATA_ACTUAL_BYTE_READBACK")
    return {"file": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def checkout():
    marker = (TREE/".git").read_text().strip()
    need(marker.startswith("gitdir: "), "WORKTREE_GITDIR")
    gd = Path(marker[8:]); gd = gd if gd.is_absolute() else TREE/gd
    ref = "refs/heads/codex/ns-reverse"
    need((gd/"HEAD").read_text().strip() == "ref: "+ref, "REVERSE_BRANCH")
    common = (gd/(gd/"commondir").read_text().strip()).resolve()
    if (common/ref).exists():
        commit = (common/ref).read_text().strip()
    else:
        matches = [line.split()[0] for line in (common/"packed-refs").read_text().splitlines()
                   if line and not line.startswith(("#", "^")) and line.split()[-1] == ref]
        need(len(matches) == 1, "UNIQUE_REVERSE_REF"); commit = matches[0]
    need(len(commit) == 40 and all(c in "0123456789abcdef" for c in commit), "SOURCE_COMMIT")
    return commit


def reject_control(name, validator, good, bad, evidence):
    validator(*good)
    try:
        validator(*bad)
    except Failure as error:
        return {"name": name, "validator": validator.__name__, "baseline_passed": True,
                "mutation_rejected": True, "error": str(error), "evidence": evidence}
    raise Failure("NEGATIVE_CONTROL_NOT_REJECTED: "+name)


def evaluate(info):
    comparison = json.loads((HERE/(CMP+"comparison.json")).read_bytes())
    need(comparison["status"] == COMPARISON_STATUS
         and all(comparison[k] is False for k in FLAGS), "LIMITED_COMPARISON_STATUS")
    need(comparison["counts"]["original_power_scalars"] == 117888, "ALL_ORIGINAL_COEFFICIENTS_CONNECTED")
    validate_hash(comparison["bindings"][BFILE]["sha256"], PINS[BFILE])
    run = json.loads((HERE/(CMP+"run.json")).read_bytes())
    receipt = json.loads((HERE/(CMP+"final-receipt.json")).read_bytes())
    acceptance = json.loads((HERE/"one-segment-comparison-root-execution-acceptance.json").read_bytes())
    for record in (run, receipt, acceptance):
        need(record["status"] == COMPARISON_STATUS and all(record[k] is False for k in FLAGS),
             "COMPARISON_SOURCE_RECEIPT_AND_ACCEPTANCE_SCOPE")
    need(run["checkout"]["commit"] == acceptance["source_commit"] == COMPARISON_COMMIT,
         "FIXED_COMPARISON_COMMIT")
    for record in (run, receipt):
        validate_hash(record["result"]["sha256"], PINS[CMP+"comparison.json"])
    validate_hash(receipt["run_sha256"], PINS[CMP+"run.json"])
    for key, name in (("result_sha256", "comparison.json"), ("run_sha256", "run.json"),
                      ("final_receipt_sha256", "final-receipt.json")):
        validate_hash(acceptance[key], PINS[CMP+name])
    need(acceptance["actual_tool_execution"]["exit_code"] == 0, "COMPARISON_ACTUAL_EXIT_ZERO")
    exp = json.loads((HERE/OLD_EXP).read_bytes())["exponential"]
    need(exp["x"] == ["5", "4"] and exp["terms_through_degree"] == 32, "OLD_FIXED_EXPONENTIAL_INTERFACE")
    pn, pd = map(int, exp["lower"])
    need(pn > 0 and pd > 0, "OLD_POSITIVE_EXPONENTIAL_FRACTION")
    with (HERE/BFILE).open("rb") as stream:
        first = stream.read(CONFIG["layer_bytes"])
    need(len(first) == CONFIG["layer_bytes"], "COMPLETE_FIRST_LAYER")
    subtotals, counts = [0, 0, 0], [0, 0, 0]
    for i in range(29472):
        value = int.from_bytes(first[12*i:12*(i+1)], "little", signed=True)
        need(value % 2048 == 0, "ORIGINAL_B0_2048_DIVISIBILITY")
        component = (i//2) % 3
        subtotals[component] += value*value  # One square per scalar, including every zero.
        counts[component] += 1
        if i % 512 == 0:
            check_budget()
    need(counts == [9824, 9824, 9824], "ALL_29472_SQUARES")
    B0 = sum(subtotals)  # Three subtotals, not a second traversal/square sum.
    denominator = 1 << 128
    left, right = 25*B0*pn, 361*denominator*pd
    difference = left-right
    decision = verdict(difference); validate_verdict(difference, decision)
    divisor = math.gcd(B0, denominator)
    good_sha = info["input_sha256"][BFILE]
    need(int(good_sha, 16) != 0, "ACTUAL_SOURCE_SHA_NONZERO")
    bad_sha = ("1" if good_sha[0] == "0" else "0")+good_sha[1:]
    controls = [reject_control("strict_zero_boundary_is_not_refutation", validate_verdict,
                              (0, "UNDECIDED_FOR_LINF"), (0, "FIXED_REFERENCE_M2_ENVELOPE_REFUTED"),
                              {"synthetic": True, "difference": "0"}),
                reject_control("actual_nonzero_source_SHA", validate_hash,
                               (good_sha, PINS[BFILE]), (good_sha, bad_sha),
                               {"synthetic": False, "file": BFILE, "actual_sha256": good_sha})]
    validate_verdict(-1, "UNDECIDED_FOR_LINF"); validate_verdict(1, "FIXED_REFERENCE_M2_ENVELOPE_REFUTED")
    return {"schema": "m2-fixed-reference-necessary-gate-v1", "decision": decision,
            "B0": str(B0), "component_subtotals": list(map(str, subtotals)), "component_counts": counts,
            "square_count": 29472, "zero_skipping": False, "second_full_sum": False,
            "Q2_unreduced": [str(B0), str(denominator)], "Q2": [str(B0//divisor), str(denominator//divisor)],
            "old_P32_5_over_4": [str(pn), str(pd)], "old_exponential_source": OLD_EXP,
            "left_25_B0_pn": str(left), "right_361_2pow128_pd": str(right), "D": str(difference),
            "strict_comparison": "D > 0", "negative_controls": controls,
            "input_sha256": info["input_sha256"], "source_sha256": info["source_sha256"],
            "config_sha256": info["config_sha256"], "original_storage": CONFIG["order"],
            "scope": "only this fixed reference M2 envelope; undecided is not a Linf upper bound; no NS/full-window conclusion",
            "producer_resource_evidence_gap_preserved": True, **FLAGS}


def alarm(signum, frame):
    raise LimitStop("M2_GATE_DEADLINE_OR_STOP_SIGNAL: "+str(signum))


def execute(info):
    OUT.mkdir(exist_ok=False)
    uname = os.uname()
    log = {"schema": "m2-necessary-gate-run-v1", "status": "RUNNING", **FLAGS,
           "pid": os.getpid(), "started_at_utc": datetime.now(timezone.utc).isoformat(),
           "source_sha256": info["source_sha256"], "config_sha256": info["config_sha256"],
           "preflight": info, "producer_resource_evidence_gap_preserved": True,
           "command": shlex.join(getattr(sys, "orig_argv", [sys.executable, *sys.argv])),
           "environment": {"python": sys.version, "executable": sys.executable,
                           "os_uname": {k: getattr(uname, k) for k in
                                        ("sysname", "nodename", "release", "version", "machine")},
                           "logical_cpu_count": os.cpu_count(), "single_process": True,
                           "arithmetic": "standard-library arbitrary precision integers; no helpers or children"}}
    save("claim.json", log, new=True)
    try:
        for sig in (signal.SIGALRM, signal.SIGTERM, signal.SIGINT):
            signal.signal(sig, alarm)
        check_budget()
        signal.setitimer(signal.ITIMER_REAL, 60-(time.monotonic()-START))
        log["source_commit"] = checkout()
        source = Path(__file__).read_bytes()
        with (OUT/"source-snapshot.py").open("xb") as stream:
            stream.write(source); stream.flush()
        need((OUT/"source-snapshot.py").read_bytes() == source, "SOURCE_SNAPSHOT_BYTE_READBACK")
        validate_hash(sha(OUT/"source-snapshot.py"), info["source_sha256"])
        log["source_snapshot"] = {"file": "source-snapshot.py", "bytes": len(source),
                                  "sha256": info["source_sha256"]}
        log["configuration"] = save("configuration.json", info, new=True)
        check_budget()
        result = evaluate(info)  # The only call to the one first-layer square sum.
        log["result"] = save("result.json", result, new=True)
        check_budget()
        # Final byte-only rechecks never decode or repeat the scientific sum.
        for name, expected in info["input_sha256"].items():
            validate_hash(sha(HERE/name), expected)
            check_budget()
        validate_hash(sha(Path(__file__)), info["source_sha256"])
        review = info["runtime_root_review"]
        validate_hash(sha(review["file"]), review["sha256"])
        need(checkout() == log["source_commit"], "SOURCE_COMMIT_CHANGED")
        log["decision"] = result["decision"]
        log["status"] = "COMPLETED_SINGLE_NI4_GATE"
    except BaseException as error:
        signal.setitimer(signal.ITIMER_REAL, 0)
        log["status"] = "STOP" if isinstance(error, LimitStop) else "FAILED"
        log["error"] = {"type": type(error).__name__, "message": str(error)}
        traceback.print_exc(file=sys.stderr); sys.stderr.flush()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        log["finished_at_utc"] = datetime.now(timezone.utc).isoformat()
        log["resources_before_run_write"] = observation()
        if exceeded(log["resources_before_run_write"]):
            log["status"] = "STOP"
        save("run.json", log)
        obs = observation()
        if exceeded(obs):
            log["status"] = "STOP"; log["after_run_write_overrun"] = obs
            save("run.json", log)
    final = {"status": log["status"], "decision": log.get("decision"), **FLAGS,
             "run_sha256": sha(OUT/"run.json"), "result": log.get("result"),
             "post_run_write_observation": observation(),
             "producer_resource_evidence_gap_preserved": True,
             "admission_requires": "actual exit zero plus matching final receipt; four flags remain false"}
    print(json.dumps(final, sort_keys=True), flush=True); sys.stderr.flush()
    files = {p.name: {"bytes": p.stat().st_size, "sha256": sha(p)}
             for p in OUT.iterdir() if p.is_file()}
    receipt = {"schema": "m2-necessary-gate-final-receipt-v1", "status": log["status"], **FLAGS,
               "decision": log.get("decision"), "run_sha256": final["run_sha256"],
               "result": log.get("result"), "existing_output_files": files,
               "producer_resource_evidence_gap_preserved": True,
               "external_stdio": {str(p): {"bytes": p.stat().st_size, "sha256": sha(p)} for p in (STDOUT, STDERR)},
               "observed_after_stdout_flush": observation(),
               "receipt_bytes": 0, "all_output_bytes_including_receipt": 0,
               "self_binding": "own canonical byte readback and exact byte count; no self-referential SHA"}
    base = observation()["all_output_bytes"]
    for _ in range(8):
        size = len(canonical(receipt))
        if size == receipt["receipt_bytes"]:
            break
        receipt["receipt_bytes"] = size
        receipt["all_output_bytes_including_receipt"] = base+size
    need(len(canonical(receipt)) == receipt["receipt_bytes"], "RECEIPT_SIZE_FIXED_POINT")
    save("final-receipt.json", receipt, new=True)
    # Actual final byte/SHA checks include both external logs. Receipt itself is
    # compared to its complete canonical bytes by save(), never to a self hash.
    for name, item in files.items():
        validate_hash(sha(OUT/name), item["sha256"])
        need((OUT/name).stat().st_size == item["bytes"], "FINAL_ARCHIVE_BYTE_SIZE")
    for name, item in receipt["external_stdio"].items():
        validate_hash(sha(name), item["sha256"])
        need(Path(name).stat().st_size == item["bytes"], "FINAL_STDIO_BYTE_SIZE")
    after = observation()
    problem = ("FINAL_BUDGET_OVERRUN" if exceeded(after) else
               "FINAL_TOTAL_BYTES_MISMATCH" if after["all_output_bytes"] != receipt["all_output_bytes_including_receipt"] else
               "LATE_PEAK_ABSENT_FROM_RECEIPT" if after["self_peak_rss_bytes"] !=
               receipt["observed_after_stdout_flush"]["self_peak_rss_bytes"] else None)
    if problem:
        log["status"] = "STOP" if exceeded(after) else "FAILED"
        log["final_receipt_invalid"] = {"reason": problem, "actual_observation": after}
        save("run.json", log)
        print(json.dumps({"status": log["status"], "invalidates_earlier_receipt": True,
                          "run_sha256": sha(OUT/"run.json"), **FLAGS}), flush=True)
        return 1
    return 0 if log["status"] == "COMPLETED_SINGLE_NI4_GATE" else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--run", action="store_true")
    modes.add_argument("--check-only", action="store_true")
    parser.add_argument("--source-review")
    parser.add_argument("--source-review-sha256")
    args = parser.parse_args()
    info = preflight(args.run, args.source_review, args.source_review_sha256)
    if not args.run:
        print(json.dumps(info, sort_keys=True), flush=True)
        return 0
    return execute(info)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (Exception, KeyboardInterrupt) as error:
        traceback.print_exc(file=sys.stderr); sys.stderr.flush()
        print(json.dumps({"status": "ENTRY_OR_FINAL_RECORD_FAILED", "type": type(error).__name__,
                          "message": str(error), "gate_admitted": False,
                          "producer_resource_evidence_gap_preserved": True, **FLAGS}), flush=True)
        raise SystemExit(1)
