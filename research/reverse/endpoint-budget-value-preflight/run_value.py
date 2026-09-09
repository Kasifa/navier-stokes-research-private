"""One exclusive numerical-value worker; standard-library supervision only.

PASS means completed computation, identity/source checks and resource acceptance.
It is not a numerical inequality certificate or an NS/source-gate conclusion.
The root owns execution authorization, live resource gates and Git-object checks.
No scientific import, auxiliary process, retry, array decoding or Git call here.
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
OLD = "research/reverse/annular-source-observation/"
RUN_ID = "value-scout-160-512"
PYTHON = Path("/Users/kasifa/.cache/codex-runtimes/codex-primary-runtime/"
              "dependencies/python/bin/python3")
WORKER = HERE / "value_worker.py"
WORKER_STATUS = "COMPLETED_NUMERICAL_VALUE_ONLY"
THREADS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")
BUDGET = {"seconds": 120, "rss_bytes": 6 * 1024 ** 3,
          "output_bytes": 1024 ** 3, "json_bytes": 16 * 1024 ** 2}
COUNTS = {"processed_checkpoints": 17, "rhs160_calls": 17, "rhs216_calls": 1,
          "fft_batched_api_calls": 54, "fft_scalar_3d_transforms": 162}
REQUIRED = {PREFIX + name for name in (
    "run_value.py", "value_worker.py", "budget_formulas.py",
    "EXECUTION_CONTRACT.md", "input-bindings.json")}
REQUIRED.update(OLD + name for name in (
    "numerical_kernel.py", "input-preparation.json", "input-acceptance.json",
    "numerical-runs/trajectory160_512/result.json",
    "numerical-runs/trajectory160_512/execution.json",
    "numerical-runs/trajectory160_512/checkpoints.jsonl"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def regular(path):
    require(path.is_absolute() and path.resolve(strict=True) == path
            and path.is_file(), "expected a regular nonsymlink file: " + str(path))


def file_record(path):
    regular(path)
    digest, size = hashlib.sha256(), 0
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 ** 2), b""):
            size += len(chunk)
            digest.update(chunk)
    return {"bytes": size, "sha256": digest.hexdigest()}


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2,
                       allow_nan=False) + "\n").encode("ascii")


def read_json(path):
    regular(path)
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_lock(path):
    regular(path)
    require(path.is_relative_to(ROOT), "source-lock must stay inside this reverse tree")
    raw = path.read_bytes()
    data = json.loads(raw)
    require(isinstance(data, dict) and type(data.get("schema")) is int
            and data["schema"] == 1, "source-lock schema must be 1")
    bindings = data.get("bindings")
    require(isinstance(bindings, list) and bindings, "empty source bindings")
    seen = set()
    for row in bindings:
        require(isinstance(row, dict), "source binding must be an object")
        name, digest, size = row.get("path"), row.get("sha256"), row.get("bytes")
        require(isinstance(name, str) and name and "\\" not in name,
                "source path must be nonempty POSIX text")
        relative = PurePosixPath(name)
        require(not relative.is_absolute() and ".." not in relative.parts
                and relative.as_posix() == name and name not in seen,
                "unsafe, non-normalized or duplicate source path")
        require(not any(suffix.lower() in (".npz", ".npy", ".gz", ".zip")
                        for suffix in relative.suffixes),
                "array/archive bytes belong to the worker, not parent source hashes")
        require(not name.startswith(PREFIX + "numerical-runs/"),
                "new run artifacts cannot be source bindings")
        require(isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest)
                and type(size) is int and size >= 0, "invalid source hash or length")
        target = ROOT / name
        regular(target)
        require(target != path, "source-lock cannot self-bind")
        seen.add(name)
    require(REQUIRED <= seen, "missing required source bindings: "
            + repr(sorted(REQUIRED - seen)))
    return bindings, hashlib.sha256(raw).hexdigest()


def source_snapshot(bindings):
    records = []
    for row in bindings:
        record = {"path": row["path"], "expected_sha256": row["sha256"],
                  "expected_bytes": row["bytes"]}
        try:
            actual = file_record(ROOT / row["path"])
            record.update(actual)
            record["match"] = (actual["sha256"] == row["sha256"]
                               and actual["bytes"] == row["bytes"])
        except Exception:
            record.update(match=False, error=traceback.format_exc())
        records.append(record)
    return records


def inventory(directory, exclude_receipt=True):
    records = []
    for path in sorted(directory.rglob("*")):
        require(not path.is_symlink(), "run artifacts cannot be symlinks")
        if path.is_dir():
            continue
        name = path.relative_to(directory).as_posix()
        if exclude_receipt and name == "execution.json.tmp":
            continue
        records.append({"path": name, **file_record(path)})
    return records


def is_json_artifact(name):
    return any(suffix in (".json", ".jsonl") for suffix in PurePosixPath(name).suffixes)


def usage_record(usage):
    return {"user_seconds": usage.ru_utime, "system_seconds": usage.ru_stime,
            "ru_maxrss_raw": usage.ru_maxrss, "ru_maxrss_unit": "Darwin bytes",
            "peak_rss_bytes": int(usage.ru_maxrss)}


def terminate_and_reap(process):
    try:
        process.kill()
    except ProcessLookupError:
        pass
    finally:
        process.wait()


def finish_receipt(receipt, handle, directory, parent_start):
    try:
        records = inventory(directory)
        receipt["artifact_inventory_before_receipt"] = records
        total_artifacts = sum(row["bytes"] for row in records)
        json_artifacts = sum(row["bytes"] for row in records
                             if is_json_artifact(row["path"]))
    except Exception:
        receipt["artifact_inventory_error"] = traceback.format_exc()
        receipt["non_output_gates_pass"] = False
        total_artifacts = json_artifacts = None
    receipt["artifact_inventory_scope"] = (
        "All run artifacts including logs and failure temporaries; excludes only the "
        "parent-owned execution.json.tmp, whose final bytes are added exactly once. "
        "execution.json has no self-hash; final stdout gives its hash.")
    receipt["parent_self_at_pre_serialization"] = usage_record(
        resource.getrusage(resource.RUSAGE_SELF))
    receipt["parent_wall_to_pre_serialization_seconds"] = time.monotonic() - parent_start
    receipt["parent_measurement_cutoff"] = (
        "After source/result checks and artifact hashing, before receipt serialization, "
        "publication and final inventory; not the complete parent lifecycle or a concurrent peak.")
    receipt["output_total_bytes_including_execution_receipt"] = 0
    receipt["json_bytes_including_execution_receipt"] = 0
    for _ in range(16):
        raw = json_bytes(receipt)
        total = None if total_artifacts is None else total_artifacts + len(raw)
        json_total = None if json_artifacts is None else json_artifacts + len(raw)
        output_ok = total is not None and total <= BUDGET["output_bytes"]
        json_ok = json_total is not None and json_total <= BUDGET["json_bytes"]
        status = "PASS" if receipt["non_output_gates_pass"] and output_ok and json_ok else "FAIL"
        if (receipt["output_total_bytes_including_execution_receipt"] == total
                and receipt["json_bytes_including_execution_receipt"] == json_total
                and receipt["budget_pass"]["output_bytes"] == output_ok
                and receipt["budget_pass"]["json_bytes"] == json_ok
                and receipt["status"] == status):
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
            return
        receipt.update(output_total_bytes_including_execution_receipt=total,
                       json_bytes_including_execution_receipt=json_total, status=status)
        receipt["budget_pass"].update(output_bytes=output_ok, json_bytes=json_ok)
    raise RuntimeError("receipt byte accounting did not stabilize")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", choices=(RUN_ID,), required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--source-lock", type=Path, required=True)
    args = parser.parse_args()
    require(sys.platform == "darwin", "this fixed resource contract requires Darwin")
    require(re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", args.source_commit),
            "source-commit must be a lowercase 40/64-character hex identifier")
    parent_start = time.monotonic()
    run_parent = HERE / "numerical-runs"
    require(not run_parent.is_symlink(), "run parent cannot be a symlink")
    run_parent.mkdir(exist_ok=True)
    require(run_parent.resolve(strict=True) == run_parent, "unsafe run parent")
    directory = run_parent / RUN_ID
    try:
        directory.mkdir()
    except FileExistsError:
        print(json.dumps({"status": "REFUSED", "run_id": RUN_ID,
                          "scientific_execution_count": 0,
                          "reason": "existing run directory; no overwrite or retry"}))
        return 2
    receipt = {
        "schema": 1, "run_id": RUN_ID, "status": "FAIL", "budget": dict(BUDGET),
        "scope": "COMPLETION_SOURCE_AND_RESOURCE_ONLY_NOT_A_NUMERICAL_OR_NS_CERTIFICATE",
        "source_commit_claim": args.source_commit,
        "source_commit_verification": "external root Git-object gate; not checked here",
        "external_launch_gates": "root checks live free memory >=40%, disk >=8GiB, "
                                 "17 regular input files/sizes and no concurrent task worker before this parent",
        "supervisor_runtime": {"executable": sys.executable, "version": sys.version,
                               "platform": sys.platform, "pid": os.getpid()},
        "expected_worker_runtime": {"python": "3.12.14", "numpy": "2.3.5",
                                    "verification": "worker checks actual versions and reports them"},
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source_lock_path": str(args.source_lock), "source_lock_sha256": None,
        "thread_environment": {name: "1" for name in THREADS},
        "popen_attempts": 0, "scientific_execution_count": 0,
        "worker_output_status": None, "child_wall_seconds": None, "returncode": None,
        "child_reaped": False, "timed_out": False, "sources_unchanged": False,
        "worker_identity_and_source_maps_match": False,
        "worker_completion_counts_match": False, "non_output_gates_pass": False,
        "budget_pass": {"wall_time": False, "rss": False,
                        "output_bytes": False, "json_bytes": False},
        "resource_scope": "one fresh parent and at most one scientific child; Popen-to-reap "
                          "wall limit; Darwin CHILDREN peak after reap is posthoc, not an RSS hard cap; "
                          "SELF is separate and is never added to CHILDREN as a concurrent peak",
    }
    process = bindings = None
    temporary = directory / "execution.json.tmp"
    with temporary.open("xb") as handle:
        try:
            before = resource.getrusage(resource.RUSAGE_CHILDREN)
            receipt["children_before"] = usage_record(before)
            require(not (before.ru_utime or before.ru_stime or before.ru_maxrss),
                    "supervisor has prior child usage")
            bindings, lock_sha = load_lock(args.source_lock)
            receipt["source_lock_sha256"] = lock_sha
            receipt["sources_before"] = source_snapshot(bindings)
            require(all(row["match"] for row in receipt["sources_before"]),
                    "source binding failed before launch")
            require(PYTHON.is_file() and os.access(PYTHON, os.X_OK), "fixed Python is missing")
            command = [str(PYTHON), "-B", str(WORKER), "--run-id", RUN_ID,
                       "--output-dir", str(directory), "--source-lock", str(args.source_lock)]
            receipt["command"] = command
            environment = dict(os.environ)
            environment.update(receipt["thread_environment"])
            with (directory / "stdout.log").open("xb") as stdout, (
                    directory / "stderr.log").open("xb") as stderr:
                receipt["popen_attempts"] = 1
                started = time.monotonic()
                try:
                    process = subprocess.Popen(command, cwd=ROOT, env=environment,
                                               stdout=stdout, stderr=stderr)
                    receipt.update(scientific_execution_count=1, pid=process.pid)
                    remaining = BUDGET["seconds"] - (time.monotonic() - started)
                    if remaining <= 0:
                        raise subprocess.TimeoutExpired(command, BUDGET["seconds"])
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
                        receipt.update(returncode=process.returncode,
                                       child_reaped=process.returncode is not None)
            result = read_json(directory / "result.json")
            receipt["worker_output_status"] = result.get("status")
            expected = {row["path"]: row["sha256"] for row in bindings}
            require(result.get("run_id") == RUN_ID and result.get("source_lock_sha256") == lock_sha
                    and type(result.get("pid")) is int and result["pid"] == process.pid
                    and type(result.get("supervisor_pid")) is int
                    and result["supervisor_pid"] == os.getpid()
                    and type(result.get("scientific_worker_invocations")) is int
                    and result["scientific_worker_invocations"] == 1
                    and result.get("source_hashes_start") == expected
                    and result.get("source_hashes_end") == expected,
                    "worker identity, invocation or complete source maps disagree")
            receipt["worker_identity_and_source_maps_match"] = True
            receipt["worker_environment"] = result.get("environment")
            receipt["worker_completion_counts"] = {key: result.get(key) for key in COUNTS}
            require(result.get("completion_verified") is True and all(
                type(result.get(key)) is int and result[key] == value for key, value in COUNTS.items()),
                "worker completion or actual operation counts disagree")
            receipt["worker_completion_counts_match"] = True
        except BaseException:
            receipt["exception"] = traceback.format_exc()
        finally:
            receipt["children_after_reap"] = usage_record(resource.getrusage(resource.RUSAGE_CHILDREN))
            if bindings is not None:
                receipt["sources_after"] = source_snapshot(bindings)
                try:
                    receipt["source_lock_after"] = file_record(args.source_lock)
                    receipt["sources_unchanged"] = (
                        all(row["match"] for row in receipt.get("sources_before", []))
                        and all(row["match"] for row in receipt["sources_after"])
                        and receipt["source_lock_after"]["sha256"] == receipt["source_lock_sha256"])
                except Exception:
                    receipt["source_after_error"] = traceback.format_exc()
            wall, rss = receipt["child_wall_seconds"], receipt["children_after_reap"]["peak_rss_bytes"]
            receipt["budget_pass"].update(
                wall_time=wall is not None and wall <= BUDGET["seconds"] and not receipt["timed_out"],
                rss=rss <= BUDGET["rss_bytes"])
            receipt["non_output_gates_pass"] = (
                "exception" not in receipt and receipt["scientific_execution_count"] == 1
                and receipt["child_reaped"] and receipt["returncode"] == 0
                and receipt["worker_output_status"] == WORKER_STATUS and receipt["sources_unchanged"]
                and receipt["worker_identity_and_source_maps_match"] and receipt["worker_completion_counts_match"]
                and receipt["budget_pass"]["wall_time"] and receipt["budget_pass"]["rss"])
            finish_receipt(receipt, handle, directory, parent_start)
    os.link(temporary, directory / "execution.json")  # Atomic publication; never overwrites.
    temporary.unlink()
    complete = inventory(directory, exclude_receipt=False)
    total = sum(row["bytes"] for row in complete)
    require([row for row in complete if row["path"] != "execution.json"]
            == receipt.get("artifact_inventory_before_receipt"),
            "artifact hashes changed during receipt closure")
    require(total == receipt["output_total_bytes_including_execution_receipt"],
            "output bytes changed during receipt closure")
    print(json.dumps({"status": receipt["status"], "run_id": RUN_ID, "scope": receipt["scope"],
                      "scientific_execution_count": receipt["scientific_execution_count"],
                      "execution": file_record(directory / "execution.json"),
                      "complete_directory_logical_bytes": total,
                      "complete_directory_manifest_sha256": hashlib.sha256(json_bytes(complete)).hexdigest(),
                      "manifest_definition": "SHA256 of sorted path/bytes/sha256 records encoded as "
                                             "ASCII sorted-key indent=2 JSON plus newline, including execution.json"},
                     sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
