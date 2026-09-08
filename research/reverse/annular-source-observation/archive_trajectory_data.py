"""Archive exactly 52 passed trajectory checkpoints without interpreting arrays.

Reuses archive_numerical_data.py's streaming gzip(level=6, mtime=0), followed by
actual streaming decompression and original SHA/byte verification. No NumPy,
science worker, subprocess, Git, retry, deletion, splitting or source overwrite.
Run only after all four trajectories and the unique comparison have passed.
An existing trajectory-data-archive directory is refused and never reused.
"""

import sys

sys.dont_write_bytecode = True

import datetime
import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath
import resource
import time
import traceback
import zlib


HERE = Path(__file__).resolve().parent
RUNS = {
    "trajectory128_256": (256, 900, 2 * 1024**3),
    "trajectory160_256": (256, 1500, 3 * 1024**3),
    "trajectory128_512": (512, 1800, 4 * 1024**3),
    "trajectory160_512": (512, 3000, 5 * 1024**3),
}
COMPARISON = "trajectory_comparison"
GZIP_LIMIT = 100 * 1024**2  # Equality also fails; no splitting/recompression.
BLOCK = 1024 * 1024


def require(condition, message):
    if not condition:
        raise ValueError(message)


def record(path):
    require(path.is_absolute() and path.resolve(strict=True) == path and path.is_file(),
            "expected a regular non-symlink absolute file")
    digest, size = hashlib.sha256(), 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(BLOCK), b""):
            digest.update(block)
            size += len(block)
    return {"bytes": size, "sha256": digest.hexdigest()}


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
                       indent=2, allow_nan=False) + "\n").encode("ascii")


def read_json(path):
    record(path)  # Regular-file gate also applies to metadata.
    return json.loads(path.read_text(encoding="utf-8"))


def relative(name):
    require(isinstance(name, str) and bool(name) and "\\" not in name, "artifact path text")
    path = PurePosixPath(name)
    require(not path.is_absolute() and ".." not in path.parts and path.as_posix() == name,
            "artifact path must be normalized relative POSIX text")
    return name


def expected_counts(run_id):
    if run_id == COMPARISON:
        return {"comparison_groups": 4, "checkpoint_pairs": 44, "scalar_node_pairs": 1284,
                "fft_batched_api_calls": 0, "fft_scalar_3d_transforms": 0}
    m = RUNS[run_id][0]
    return {"completed_steps": m, "expected_steps": m, "checkpoint_count": m // 32 + 1,
            "node_count": m + 1, "fft_batched_api_calls": 36 * m,
            "fft_scalar_3d_transforms": 108 * m}


def passed_run(run_id):
    directory = HERE / "numerical-runs" / run_id
    receipt_path, result_path = directory / "execution.json", directory / "result.json"
    receipt, result = read_json(receipt_path), read_json(result_path)
    require(receipt.get("status") == result.get("status") == "PASS"
            and receipt.get("run_id") == result.get("run_id") == run_id
            and receipt.get("source_lock_sha256") == result.get("source_lock_sha256")
            and isinstance(receipt.get("source_lock_sha256"), str), "run identity/PASS/lock")
    require(receipt.get("scientific_execution_count") == 1
            and receipt.get("worker_output_status") == "PASS" and receipt.get("returncode") == 0
            and receipt.get("child_reaped") is True and receipt.get("timed_out") is False
            and receipt.get("sources_unchanged") is True
            and receipt.get("worker_identity_and_source_maps_match") is True
            and receipt.get("worker_completion_counts_match") is True
            and receipt.get("non_output_gates_pass") is True
            and receipt.get("budget_pass") == {"wall_time": True, "rss": True, "output_bytes": True}
            and result.get("completion_verified") is True
            and result.get("scientific_worker_invocations") == 1
            and result.get("pid") == receipt.get("pid")
            and result.get("supervisor_pid") == receipt["supervisor_runtime"]["pid"],
            "run execution/resource/completion gate")
    counts = expected_counts(run_id)
    require(all(type(result.get(key)) is int and result[key] == value for key, value in counts.items())
            and receipt.get("worker_completion_counts") == counts, "fixed completion counts")
    seconds, output_limit = ((180, 64 * 1024**2) if run_id == COMPARISON
                             else RUNS[run_id][1:])
    require(receipt["budget"] == {"seconds": seconds, "rss_bytes": 6 * 1024**3,
                                  "output_bytes": output_limit}
            and 0 <= receipt["child_wall_seconds"] <= seconds
            and 0 <= receipt["children_after_reap"]["peak_rss_bytes"] <= 6 * 1024**3
            and 0 <= receipt["output_total_bytes_including_execution_receipt"] <= output_limit,
            "recorded resource bounds")
    require(result.get("source_hashes_start") == result.get("source_hashes_end")
            and bool(result.get("source_hashes_start")), "worker source map changed")
    inventory = {}
    for row in receipt["artifact_inventory_before_receipt"]:
        name = relative(row["path"])
        require(name not in inventory, "duplicate receipt artifact")
        inventory[name] = {"bytes": row["bytes"], "sha256": row["sha256"]}
    require(record(result_path) == inventory.get("result.json"), "result differs from receipt")
    if run_id == COMPARISON:
        require(result.get("all_input_bytes_unchanged") is True
                and result.get("unique_input_checkpoints_validated") == 52,
                "comparison did not validate all 52 inputs")
    return directory, receipt, result, inventory, {
        "run_id": run_id, "execution": record(receipt_path), "result": record(result_path),
        "source_lock_sha256": receipt["source_lock_sha256"], "completion_counts": counts}


def usage():
    value = resource.getrusage(resource.RUSAGE_SELF)
    require(sys.platform == "darwin", "archive RSS convention is locked to Darwin bytes")
    return {"user_seconds": value.ru_utime, "system_seconds": value.ru_stime,
            "peak_rss_bytes": int(value.ru_maxrss), "ru_maxrss_unit": "Darwin bytes"}


def main():
    started = time.perf_counter()
    archive = HERE / "trajectory-data-archive"
    try:
        archive.mkdir()  # Existence is refusal, including a prior failed attempt.
    except FileExistsError:
        print(json.dumps({"status": "REFUSED", "reason": "archive directory exists; no retry"}))
        return 2
    manifest = {
        "schema": 1, "status": "FAIL", "scope": "LOSSLESS_BYTE_ARCHIVE_ONLY_NO_SCIENTIFIC_EXECUTION",
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "script_start": record(Path(__file__).resolve()), "python": sys.version,
        "zlib_version": zlib.ZLIB_VERSION, "zlib_runtime_version": zlib.ZLIB_RUNTIME_VERSION,
        "gzip_compresslevel": 6, "gzip_mtime": 0, "gzip_filename_header": "",
        "single_gzip_required_strictly_below_bytes": GZIP_LIMIT,
        "original_files_preserved": True, "scientific_worker_invocations": 0,
        "prerequisites": [], "selected": [], "files": []}
    with (archive / "progress.jsonl").open("xb") as progress:
        def event(name, **values):
            progress.write(json_bytes({"event": name, "elapsed_seconds": time.perf_counter() - started,
                                       **values}).replace(b"\n", b" ") + b"\n")
            progress.flush()

        try:
            manifest["self_before"] = usage()
            all_runs, locks = {}, set()
            for run_id in (*RUNS, COMPARISON):
                data = passed_run(run_id)
                all_runs[run_id] = data
                manifest["prerequisites"].append(data[4])
                locks.add(data[1]["source_lock_sha256"])
                event("prerequisite_passed", run_id=run_id)
            require(len(locks) == 1, "four trajectories/comparison do not share one source lock")
            compared = all_runs[COMPARISON][2]["prerequisite_receipts"]
            require(len(compared) == 4 and {row["run_id"] for row in compared} == set(RUNS),
                    "comparison prerequisite receipt coverage")
            for row in compared:
                current = all_runs[row["run_id"]][4]
                require(row["execution"] == current["execution"] and row["result"] == current["result"]
                        and row["counts"] == current["completion_counts"],
                        "comparison did not use these exact four passed runs")
            for run_id, (m, _, _) in RUNS.items():
                directory, receipt, result, inventory, evidence = all_runs[run_id]
                index_path = directory / "checkpoints.jsonl"
                require(record(index_path) == inventory.get("checkpoints.jsonl"), "checkpoint index binding")
                rows = [json.loads(line) for line in index_path.read_text(encoding="utf-8").splitlines()]
                require([row["j"] for row in rows] == list(range(0, m + 1, 32))
                        and len(rows) == m // 32 + 1
                        and result["artifacts"]["checkpoints"] == rows, "complete checkpoint sequence")
                selected_names = set()
                for row in rows:
                    name = relative(row["file"])
                    require(name.endswith(".npz") and name not in selected_names, "checkpoint filename")
                    selected_names.add(name)
                    expected = {"bytes": row["bytes"], "sha256": row["sha256"]}
                    require(expected == inventory.get(name), "checkpoint index/receipt mismatch")
                    source = directory / name
                    require(record(source) == expected, "original checkpoint bytes differ")
                    target = archive / (run_id + "-" + source.name + ".gz")
                    manifest["selected"].append({
                        "run_id": run_id, "j": row["j"], "original": source.relative_to(HERE).as_posix(),
                        "original_record": expected, "archive": target.relative_to(HERE).as_posix()})
                require(selected_names == {name for name in inventory if name.endswith(".npz")},
                        "receipt has missing/unindexed checkpoints")
            require(len(manifest["selected"]) == 52, "must select exactly 52 original checkpoints")
            require(len({row["archive"] for row in manifest["selected"]}) == 52, "archive target collision")
            manifest["selected_count"] = len(manifest["selected"])
            event("all_52_originals_validated")
            for index, selected in enumerate(manifest["selected"], 1):
                item = {**selected, "status": "PENDING", "restoration_verified": False}
                manifest["files"].append(item)  # Retain this row even on a partial gzip failure.
                source, target = HERE / item["original"], HERE / item["archive"]
                file_started = time.perf_counter()
                event("file_start", index=index, original=item["original"], archive=item["archive"])
                require(record(source) == item["original_record"], "original changed before compression")
                with source.open("rb") as src, target.open("xb") as dst:
                    with gzip.GzipFile(filename="", mode="wb", compresslevel=6, mtime=0,
                                       fileobj=dst) as compressed:
                        for block in iter(lambda: src.read(BLOCK), b""):
                            compressed.write(block)
                item["archive_record"] = record(target)
                item["status"] = "COMPRESSED"
                require(item["archive_record"]["bytes"] < GZIP_LIMIT,
                        "gzip is at least 100 MiB; retain failure, do not split/recompress or claim Git eligibility")
                restored_hash, restored_size = hashlib.sha256(), 0
                with gzip.open(target, "rb") as stream:
                    for block in iter(lambda: stream.read(BLOCK), b""):
                        restored_hash.update(block)
                        restored_size += len(block)
                item["restored_record"] = {"bytes": restored_size, "sha256": restored_hash.hexdigest()}
                require(item["restored_record"] == item["original_record"], "streaming restoration failed")
                require(record(source) == item["original_record"], "original changed during archival")
                item.update(status="VERIFIED", restoration_verified=True,
                            file_wall_seconds=time.perf_counter() - file_started)
                event("file_verified", index=index, original=item["original"],
                      original_bytes=item["original_record"]["bytes"],
                      gzip_bytes=item["archive_record"]["bytes"], file_wall_seconds=item["file_wall_seconds"])
            require(len(manifest["files"]) == 52 and all(
                item["restoration_verified"] for item in manifest["files"]), "incomplete archive")
            for evidence in manifest["prerequisites"]:
                directory = HERE / "numerical-runs" / evidence["run_id"]
                require(record(directory / "execution.json") == evidence["execution"]
                        and record(directory / "result.json") == evidence["result"], "prerequisite metadata changed")
            manifest["script_end"] = record(Path(__file__).resolve())
            require(manifest["script_end"] == manifest["script_start"], "archive script changed")
            manifest["status"] = "PASS"
        except BaseException as error:
            manifest["error"] = {"type": type(error).__name__, "message": str(error),
                                 "traceback": traceback.format_exc()}
            if manifest["files"] and manifest["files"][-1]["status"] != "VERIFIED":
                failed = manifest["files"][-1]
                failed["status"] = "FAIL"
                partial = HERE / failed["archive"]
                if partial.is_file():
                    failed["partial_archive_record"] = record(partial)
            event("archive_failed", error=manifest["error"])
        finally:
            manifest["archive_wall_seconds_to_manifest"] = time.perf_counter() - started
            manifest["self_at_pre_manifest_serialization"] = usage()
            manifest["resource_scope"] = (
                "one byte-archive process, no child; wall starts after stdlib imports and ends before "
                "final manifest serialization; SELF CPU/RSS sampled there, RSS is process lifetime "
                "peak in Darwin bytes, not a full lifecycle or concurrent-process peak certificate")
            manifest["verified_files"] = sum(item["restoration_verified"] for item in manifest["files"])
            manifest["verified_original_bytes"] = sum(item["original_record"]["bytes"] for item
                in manifest["files"] if item["restoration_verified"])
            manifest["gzip_bytes_recorded"] = sum(
                item.get("archive_record", item.get("partial_archive_record", {})).get("bytes", 0)
                for item in manifest["files"])
            manifest["restoration"] = (
                "Stream gzip to the listed original path only when absent; verify original SHA/bytes. "
                "Never overwrite existing originals. Archives are byte copies, not array or NS certificates.")
            with (archive / "manifest.json").open("xb") as stream:
                stream.write(json_bytes(manifest))
    print(json.dumps({"status": manifest["status"], "verified_files": manifest["verified_files"],
                      "seconds_to_manifest": manifest["archive_wall_seconds_to_manifest"],
                      "peak_rss_bytes": manifest["self_at_pre_manifest_serialization"]["peak_rss_bytes"]}))
    return 0 if manifest["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
