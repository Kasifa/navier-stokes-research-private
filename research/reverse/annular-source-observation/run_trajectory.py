"""Four fixed trajectory workers and one separate comparison, each supervised alone.

Adapted from the locked run_numerical.py; no old science worker is imported or run.
The old validation is checked as immutable prerequisite metadata under its own
old lock. New trajectory/comparison outputs must use the new common source lock.

One fresh standard-library supervisor, one worker, one exclusive run directory.

No NumPy/scientific module imports, Git calls, retries, or auxiliary processes.
The source commit is an externally asserted identifier, NOT verified by Git here.
Source-lock bytes and every binding are checked before and after the worker.
RSS and output limits are post-run acceptance bounds; no virtual-address limit
is presented as an RSS cap.  Failure evidence is retained without deletion.
"""

import sys

sys.dont_write_bytecode = True

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import resource
import subprocess
import time
import traceback


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = HERE.relative_to(ROOT).as_posix() + "/"
PYTHON = Path("/Users/kasifa/.cache/codex-runtimes/codex-primary-runtime/"
              "dependencies/python/bin/python3")
REQUESTED_RUN_ID = None
REQUIRED = {PREFIX + name for name in (
    "run_numerical.py", "numerical_experiment.py", "numerical_kernel.py",
    "numerical_reference.py", "NUMERICAL_EXECUTION_CONTRACT.md",
    "input-preparation.json", "input-acceptance.json", "numerical-acceptance.json",
    "numerical-source-lock.json", "TRAJECTORY_CONTRACT.md", "TRAJECTORY_CONTRACT_DRAFT.md",
    "trajectory_driver.py", "compare_trajectories.py", "run_trajectory.py")}
BUDGETS = {
    "trajectory128_256": {"seconds": 900, "rss_bytes": 6 * 1024**3, "output_bytes": 2 * 1024**3},
    "trajectory160_256": {"seconds": 1500, "rss_bytes": 6 * 1024**3, "output_bytes": 3 * 1024**3},
    "trajectory128_512": {"seconds": 1800, "rss_bytes": 6 * 1024**3, "output_bytes": 4 * 1024**3},
    "trajectory160_512": {"seconds": 3000, "rss_bytes": 6 * 1024**3, "output_bytes": 5 * 1024**3},
    "trajectory_comparison": {"seconds": 180, "rss_bytes": 6 * 1024**3, "output_bytes": 64 * 1024**2},
}
TRAJECTORY_STEPS = {"trajectory128_256": 256, "trajectory160_256": 256,
                    "trajectory128_512": 512, "trajectory160_512": 512}
OLD_NUMERICAL_LOCK_SHA = "060e72f189c2b6ecade7b6425509f68c2efb6d056b4f71e25b76c91fdb5ce3d2"
NUMERICAL_ACCEPTANCE_SHA = "dceb856c85a109ccbf5e3b204ca29d36f37793125bade90cade3bf4150ffae97"


def file_record(path):
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(128 * 1024), b""):
            size += len(chunk)
            digest.update(chunk)
    return {"bytes": size, "sha256": digest.hexdigest()}


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
                       indent=2, allow_nan=False) + "\n").encode("ascii")


def read_json(path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_lock(path):
    if not path.is_absolute() or not path.is_file():
        raise ValueError("source-lock must name an existing absolute file")
    raw = path.read_bytes()
    lock = json.loads(raw)
    if not isinstance(lock, dict) or type(lock.get("schema")) is not int or lock["schema"] != 1:
        raise ValueError("source-lock schema must be 1")
    bindings = lock.get("bindings")
    if not isinstance(bindings, list) or not bindings:
        raise ValueError("source-lock bindings must be a nonempty list")
    seen = set()
    for item in bindings:
        if not isinstance(item, dict):
            raise ValueError("each source binding must be an object")
        name, digest = item.get("path"), item.get("sha256")
        if not isinstance(name, str) or not name or "\\" in name:
            raise ValueError("source binding path must be repo-relative POSIX text")
        relative = PurePosixPath(name)
        if relative.is_absolute() or ".." in relative.parts or relative.as_posix() != name:
            raise ValueError("source binding path is not normalized repo-relative")
        if name in seen or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValueError("duplicate source path or invalid SHA-256")
        target = ROOT / name
        if target.resolve(strict=True) != target or not target.is_file():
            raise ValueError("source binding must be a regular non-symlink repo file")
        seen.add(name)
    if not REQUIRED <= seen:
        raise ValueError("source-lock lacks required files: " + repr(sorted(REQUIRED - seen)))
    return bindings, hashlib.sha256(raw).hexdigest()


def source_snapshot(bindings):
    records = []
    for binding in bindings:
        record = {"path": binding["path"], "expected_sha256": binding["sha256"]}
        try:
            target = ROOT / binding["path"]
            if target.resolve(strict=True) != target or not target.is_file():
                raise ValueError("source path changed to a symlink or non-file")
            record.update(file_record(target))
            record["match"] = record["sha256"] == binding["sha256"]
        except Exception as error:
            record.update(match=False, error=repr(error))
        records.append(record)
    return records


def inventory(directory, exclude_receipt=True):
    """Logical bytes and hashes of every regular artifact, not allocated blocks."""
    records = []
    for path in sorted(directory.rglob("*")):
        if path.is_symlink():
            raise ValueError("run artifacts must not contain symlinks")
        if path.is_dir():
            continue
        if not path.is_file():
            raise ValueError("run artifact is not a regular file")
        name = path.relative_to(directory).as_posix()
        if exclude_receipt and name == "execution.json":
            continue
        records.append({"path": name, **file_record(path)})
    return records


def validate_numeric_prior_run(lock_sha):
    directory = HERE / "numerical-runs" / "validation"
    receipt_path, result_path = directory / "execution.json", directory / "result.json"
    receipt, result = read_json(receipt_path), read_json(result_path)
    for record in (receipt, result):
        if record.get("status") != "PASS" or record.get("run_id") != "validation":
            raise ValueError("cost requires a passed validation result and receipt")
        if record.get("source_lock_sha256") != lock_sha:
            raise ValueError("cost source-lock differs from validation")
    if (receipt.get("worker_output_status") != "PASS"
            or receipt.get("worker_identity_and_source_maps_match") is not True
            or receipt.get("returncode") != 0
            or receipt.get("child_reaped") is not True
            or receipt.get("scientific_execution_count") != 1
            or receipt.get("timed_out") is not False
            or receipt.get("budget_pass") != {
                "wall_time": True, "rss": True, "output_bytes": True}):
        raise ValueError("validation execution or resource gate did not pass")
    if not receipt.get("sources_unchanged"):
        raise ValueError("validation source integrity gate did not pass")
    actual = inventory(directory)
    if actual != receipt.get("artifact_inventory_before_receipt"):
        raise ValueError("validation artifacts changed after their receipt")
    if sum(item["bytes"] for item in actual) + receipt_path.stat().st_size != receipt.get(
            "output_total_bytes_including_execution_receipt"):
        raise ValueError("validation total output byte count changed")
    return {"execution": file_record(receipt_path), "result": file_record(result_path),
            "source_lock_sha256": lock_sha}


def completion_counts(result, run_id):
    if run_id == "trajectory_comparison":
        expected = {"comparison_groups": 4, "checkpoint_pairs": 44,
                    "scalar_node_pairs": 1284, "fft_batched_api_calls": 0,
                    "fft_scalar_3d_transforms": 0}
    else:
        steps = TRAJECTORY_STEPS[run_id]
        expected = {"completed_steps": steps, "expected_steps": steps,
                    "checkpoint_count": steps // 32 + 1, "node_count": steps + 1,
                    "fft_batched_api_calls": 36 * steps,
                    "fft_scalar_3d_transforms": 108 * steps}
    if any(type(result.get(key)) is not int or result[key] != value
           for key, value in expected.items()):
        raise ValueError("worker completion counts differ from fixed contract")
    return expected


def completed_trajectory(run_id, lock_sha):
    directory = HERE / "numerical-runs" / run_id
    receipt_path, result_path = directory / "execution.json", directory / "result.json"
    receipt, result = read_json(receipt_path), read_json(result_path)
    for item in (receipt, result):
        if (item.get("status") != "PASS" or item.get("run_id") != run_id
                or item.get("source_lock_sha256") != lock_sha):
            raise ValueError("prerequisite trajectory did not pass on this source lock")
    if (receipt.get("returncode") != 0 or receipt.get("child_reaped") is not True
            or receipt.get("timed_out") is not False
            or receipt.get("scientific_execution_count") != 1
            or receipt.get("worker_output_status") != "PASS"
            or receipt.get("sources_unchanged") is not True
            or receipt.get("worker_identity_and_source_maps_match") is not True
            or receipt.get("worker_completion_counts_match") is not True
            or receipt.get("budget_pass") != {
                "wall_time": True, "rss": True, "output_bytes": True}):
        raise ValueError("prerequisite trajectory execution/resource gate failed")
    completed = completion_counts(result, run_id)
    current = inventory(directory)
    if current != receipt.get("artifact_inventory_before_receipt"):
        raise ValueError("prerequisite trajectory artifacts changed")
    if sum(row["bytes"] for row in current) + receipt_path.stat().st_size != receipt.get(
            "output_total_bytes_including_execution_receipt"):
        raise ValueError("prerequisite trajectory output total changed")
    return {"run_id": run_id, "execution": file_record(receipt_path),
            "result": file_record(result_path), "completion_counts": completed}


def validate_prior_run(lock_sha):
    # This calls metadata validation only. It never runs the closed old worker.
    numeric = validate_numeric_prior_run(OLD_NUMERICAL_LOCK_SHA)
    acceptance_path = HERE / "numerical-acceptance.json"
    acceptance_record = file_record(acceptance_path)
    if acceptance_record["sha256"] != NUMERICAL_ACCEPTANCE_SHA:
        raise ValueError("accepted implementation/cost record changed")
    acceptance = read_json(acceptance_path)
    if (acceptance.get("status") != "ACCEPTED_FIXED_TESTS_AND_COST_ONLY"
            or acceptance.get("scientific_worker_executions") != 3
            or acceptance.get("all_three_runs_closed") is not True):
        raise ValueError("implementation/cost qualification not accepted")
    if REQUESTED_RUN_ID == "trajectory_comparison":
        required_runs = tuple(TRAJECTORY_STEPS)
    elif TRAJECTORY_STEPS[REQUESTED_RUN_ID] == 512:
        required_runs = ("trajectory128_256", "trajectory160_256")
    else:
        required_runs = ()
    prior = [completed_trajectory(run_id, lock_sha) for run_id in required_runs]
    return {"old_numeric_validation": numeric, "numeric_acceptance": acceptance_record,
            "current_source_lock_sha256": lock_sha, "completed_trajectory_inputs": prior}


def usage_record(usage):
    if sys.platform == "darwin":
        unit, rss_bytes = "bytes", int(usage.ru_maxrss)
    elif sys.platform.startswith("linux"):
        unit, rss_bytes = "KiB", int(usage.ru_maxrss) * 1024
    else:
        unit, rss_bytes = "unsupported platform unit", None
    return {"user_seconds": usage.ru_utime, "system_seconds": usage.ru_stime,
            "ru_maxrss_raw": usage.ru_maxrss, "ru_maxrss_unit": unit,
            "peak_rss_bytes": rss_bytes}


def terminate_and_reap(process):
    """Reap even if the child exited between timeout detection and kill."""
    try:
        process.kill()
    except ProcessLookupError:
        pass
    finally:
        process.wait()


def finish_receipt(receipt, handle, directory, budget):
    try:
        artifacts = inventory(directory)
        receipt["artifact_inventory_before_receipt"] = artifacts
        artifact_bytes = sum(item["bytes"] for item in artifacts)
        receipt["artifact_inventory_scope"] = (
            "All regular run files before final execution.json serialization; "
            "execution.json excludes its own hash. Final stdout hashes the complete directory.")
    except Exception:
        receipt["artifact_inventory_error"] = traceback.format_exc()
        receipt["status"] = "FAIL"
        artifact_bytes = None
    receipt["output_total_bytes_including_execution_receipt"] = 0
    for _ in range(16):
        raw = json_bytes(receipt)
        total = None if artifact_bytes is None else artifact_bytes + len(raw)
        output_ok = total is not None and total <= budget["output_bytes"]
        status = "PASS" if receipt["non_output_gates_pass"] and output_ok else "FAIL"
        if (receipt["output_total_bytes_including_execution_receipt"] == total
                and receipt["budget_pass"]["output_bytes"] == output_ok
                and receipt["status"] == status):
            break
        receipt["output_total_bytes_including_execution_receipt"] = total
        receipt["budget_pass"]["output_bytes"] = output_ok
        receipt["status"] = status
    else:
        raise RuntimeError("receipt byte-count metadata did not stabilize")
    handle.write(raw)
    handle.flush()
    os.fsync(handle.fileno())


def main():
    global REQUESTED_RUN_ID
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", choices=tuple(BUDGETS), required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--source-lock", type=Path, required=True)
    args = parser.parse_args()
    REQUESTED_RUN_ID = args.run_id
    worker_path = HERE / ("compare_trajectories.py" if args.run_id == "trajectory_comparison"
                          else "trajectory_driver.py")
    if not re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", args.source_commit):
        parser.error("source-commit must be a lowercase 40- or 64-digit hex identifier")
    parent_start = time.monotonic()
    directory = HERE / "numerical-runs" / args.run_id
    directory.parent.mkdir(exist_ok=True)
    try:
        directory.mkdir()  # An existing directory is never reused, even after failure.
    except FileExistsError:
        print(json.dumps({"status": "REFUSED", "run_id": args.run_id,
                          "reason": "run directory already exists; no worker launched"}))
        return 2
    budget = BUDGETS[args.run_id]
    receipt = {
        "schema": 1, "run_id": args.run_id, "status": "FAIL",
        "supervisor_runtime": {"executable": sys.executable, "version": sys.version,
                               "platform": sys.platform, "pid": os.getpid()},
        "source_commit_claim": args.source_commit,
        "source_commit_verification": "external root gate; no Git call by supervisor",
        "source_lock_path": str(args.source_lock), "source_lock_sha256": None,
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "budget": budget, "scientific_execution_count": 0,
        "worker_output_status": None, "returncode": None, "child_reaped": False,
        "worker_identity_and_source_maps_match": False,
        "worker_completion_counts_match": False,
        "timed_out": False, "child_wall_seconds": None, "sources_unchanged": False,
        "budget_pass": {"wall_time": False, "rss": False, "output_bytes": False},
        "non_output_gates_pass": False,
        "resource_scope": "one fresh supervisor and exactly one possible scientific child; "
                          "CHILDREN is sampled after reap; SELF is separate, never added as a simultaneous peak",
        "external_resource_gate": "root must check live memory pressure and available disk "
                                  "before each trajectory wave and before comparison; "
                                  "this supervisor launches no extra metadata process",
    }
    process = None
    bindings = None
    with (directory / "execution.json").open("xb") as receipt_handle:
        try:
            before_usage = resource.getrusage(resource.RUSAGE_CHILDREN)
            receipt["children_before"] = usage_record(before_usage)
            if before_usage.ru_utime or before_usage.ru_stime or before_usage.ru_maxrss:
                raise ValueError("supervisor is not fresh: pre-existing child usage")
            bindings, lock_sha = load_lock(args.source_lock)
            receipt["source_lock_sha256"] = lock_sha
            receipt["sources_before"] = source_snapshot(bindings)
            if not all(item["match"] for item in receipt["sources_before"]):
                raise ValueError("a source binding failed before worker launch")
            receipt["validation_gate"] = validate_prior_run(lock_sha)
            if not PYTHON.is_file():
                raise ValueError("fixed bundled Python executable is missing")
            command = [str(PYTHON), "-B", str(worker_path), "--run-id", args.run_id,
                       "--output-dir", str(directory), "--source-lock", str(args.source_lock)]
            receipt["command"] = command
            with (directory / "stdout.log").open("xb") as stdout, (
                    directory / "stderr.log").open("xb") as stderr:
                started = time.monotonic()  # Immediately before Popen, not inside the worker.
                try:
                    process = subprocess.Popen(command, cwd=ROOT, stdout=stdout, stderr=stderr)
                    receipt["scientific_execution_count"] = 1
                    receipt["pid"] = process.pid
                    remaining = budget["seconds"] - (time.monotonic() - started)
                    if remaining <= 0:
                        raise subprocess.TimeoutExpired(command, budget["seconds"])
                    process.wait(timeout=remaining)
                except subprocess.TimeoutExpired:
                    receipt["timed_out"] = True
                    if process is not None:
                        terminate_and_reap(process)
                except BaseException:
                    if process is not None and process.returncode is None:
                        terminate_and_reap(process)
                    raise
                finally:
                    receipt["child_wall_seconds"] = time.monotonic() - started
                    if process is not None:
                        receipt["returncode"] = process.returncode
                        receipt["child_reaped"] = process.returncode is not None
            result = read_json(directory / "result.json")
            receipt["worker_output_status"] = result.get("status")
            if (result.get("run_id") != args.run_id
                    or result.get("source_lock_sha256") != lock_sha):
                raise ValueError("worker result run-id or source-lock binding differs")
            expected_hashes = {item["path"]: item["sha256"] for item in bindings}
            if (result.get("pid") != process.pid
                    or result.get("supervisor_pid") != os.getpid()
                    or result.get("scientific_worker_invocations") != 1
                    or result.get("source_hashes_start") != expected_hashes
                    or result.get("source_hashes_end") != expected_hashes):
                raise ValueError("worker identity, invocation count or source maps differ")
            receipt["worker_identity_and_source_maps_match"] = True
            receipt["worker_completion_counts"] = completion_counts(result, args.run_id)
            receipt["worker_completion_counts_match"] = True
        except BaseException:
            receipt["exception"] = traceback.format_exc()
        finally:
            receipt["children_after_reap"] = usage_record(
                resource.getrusage(resource.RUSAGE_CHILDREN))
            if bindings is not None:
                receipt["sources_after"] = source_snapshot(bindings)
                try:
                    receipt["source_lock_after_sha256"] = file_record(args.source_lock)["sha256"]
                    receipt["sources_unchanged"] = (
                        all(item["match"] for item in receipt.get("sources_before", []))
                        and all(item["match"] for item in receipt["sources_after"])
                        and receipt["source_lock_after_sha256"] == receipt["source_lock_sha256"])
                except Exception:
                    receipt["source_after_error"] = traceback.format_exc()
            wall = receipt["child_wall_seconds"]
            rss = receipt["children_after_reap"]["peak_rss_bytes"]
            receipt["budget_pass"]["wall_time"] = (
                wall is not None and wall <= budget["seconds"] and not receipt["timed_out"])
            receipt["budget_pass"]["rss"] = rss is not None and rss <= budget["rss_bytes"]
            receipt["non_output_gates_pass"] = (
                "exception" not in receipt and receipt["scientific_execution_count"] == 1
                and receipt["child_reaped"] and receipt["returncode"] == 0
                and receipt["worker_output_status"] == "PASS" and receipt["sources_unchanged"]
                and receipt["worker_identity_and_source_maps_match"]
                and receipt["worker_completion_counts_match"]
                and receipt["budget_pass"]["wall_time"] and receipt["budget_pass"]["rss"])
            receipt["parent_self_at_pre_serialization"] = usage_record(
                resource.getrusage(resource.RUSAGE_SELF))
            receipt["parent_wall_to_pre_serialization_seconds"] = time.monotonic() - parent_start
            receipt["parent_measurement_cutoff"] = (
                "after source/result checks, before final artifact hashing and receipt "
                "serialization; not a measurement of the full supervisor lifecycle")
            finish_receipt(receipt, receipt_handle, directory, budget)
    complete = inventory(directory, exclude_receipt=False)
    summary = {
        "status": receipt["status"], "run_id": args.run_id,
        "scientific_execution_count": receipt["scientific_execution_count"],
        "execution": file_record(directory / "execution.json"),
        "complete_directory_logical_bytes": sum(item["bytes"] for item in complete),
        "complete_directory_manifest_sha256": hashlib.sha256(json_bytes(complete)).hexdigest(),
        "directory_manifest_definition": "SHA256 of ASCII sorted-key indented JSON + newline; "
                                         "lexicographically sorted {path,bytes,sha256} records, including execution.json",
    }
    print(json.dumps(summary, sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
