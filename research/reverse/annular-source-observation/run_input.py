#!/usr/bin/env python3
"""One-child supervisor. No science is run by importing this file.

The sole Popen call below launches prepare_input.py once. No Git, ps, platform
helper or other subprocess is invoked. RUSAGE_CHILDREN is read after child wait;
the fresh supervisor has no earlier reaped children. Peak RSS is post-run
acceptance, not RLIMIT_AS or a claim that excess RSS was prevented.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "input-preparation.json"
RECEIPT = HERE / "input-execution.json"
TIMEOUT_SECONDS = 5.0
RSS_LIMIT_BYTES = 256 * 1024 * 1024
MAX_OUTPUT_BYTES = 1 << 20


def snapshot(usage):
    return {"user_seconds": usage.ru_utime, "system_seconds": usage.ru_stime,
            "maximum_rss_raw": usage.ru_maxrss}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-commit", required=True)
    args = parser.parse_args()
    try:
        receipt = RECEIPT.open("x", encoding="utf-8")
    except FileExistsError:
        print("REFUSED: input-execution.json already exists; no rerun", file=sys.stderr)
        return 2
    record = {"schema": "annular-input-execution-v1", "status": "FAIL",
              "source_commit_supplied": args.source_commit,
              "supervisor_pid": os.getpid(), "supervisor_count": 1,
              "scientific_subprocess_launch_attempts": 0,
              "scientific_subprocess_launch_count": 0,
              "child_reported_scientific_execution_count": None,
              "child_reported_scientific_completed": None,
              "limits": {"child_lifecycle_wall_seconds": TIMEOUT_SECONDS,
                         "child_peak_rss_bytes": RSS_LIMIT_BYTES},
              "scientific_scope": "input preparation only; no Fourier/NS integration"}
    with receipt:
        try:
            if OUTPUT.exists():
                raise RuntimeError("input-preparation.json exists; refusing scientific rerun")
            system = os.uname().sysname
            if system not in ("Darwin", "Linux"):
                raise RuntimeError("unsupported ru_maxrss unit: " + system)
            rss_unit = "bytes" if system == "Darwin" else "KiB"
            rss_factor = 1 if system == "Darwin" else 1024
            before = resource.getrusage(resource.RUSAGE_CHILDREN)
            if before.ru_maxrss != 0 or before.ru_utime != 0 or before.ru_stime != 0:
                raise RuntimeError("fresh supervisor already has reaped-child usage")
            record["environment"] = {"python": sys.version, "executable": sys.executable,
                                     "uname": tuple(os.uname()), "rss_raw_unit": rss_unit}
            record["source_hashes_before_launch"] = {
                name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                for name in ("prepare_input.py", "run_input.py")}
            command = [sys.executable, str(HERE / "prepare_input.py"),
                       "--source-commit", args.source_commit,
                       "--supervisor-pid", str(os.getpid())]
            record["command"] = command
            record["scientific_subprocess_launch_attempts"] = 1
            start = time.perf_counter()  # Before Popen, including process startup.
            process = subprocess.Popen(command, cwd=str(HERE),
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            record["scientific_subprocess_launch_count"] = 1
            timed_out = False
            communication_error = None
            stdout = stderr = b""
            remaining = max(0.0, TIMEOUT_SECONDS - (time.perf_counter() - start))
            try:
                stdout, stderr = process.communicate(timeout=remaining)
            except subprocess.TimeoutExpired:
                timed_out = True
            except Exception as exc:
                communication_error = {"type": type(exc).__name__, "message": str(exc)}
            finally:
                # Reap this same child even after a timeout or pipe error; never retry.
                if process.poll() is None:
                    try:
                        process.kill()
                    except ProcessLookupError:
                        pass
                try:
                    if timed_out or communication_error is not None:
                        stdout, stderr = process.communicate()
                except Exception as exc:
                    communication_error = {"type": type(exc).__name__, "message": str(exc)}
                finally:
                    returncode = process.wait()
                    end = time.perf_counter()  # Includes startup, serialization and exit.
                    after = resource.getrusage(resource.RUSAGE_CHILDREN)
            peak_bytes = after.ru_maxrss * rss_factor
            record["child_lifecycle"] = {
                "pid": process.pid, "returncode": returncode, "timed_out": timed_out,
                "communication_error": communication_error,
                "wall_seconds": end - start,
                "wall_scope": "immediately before Popen through after wait",
                "usage_before": snapshot(before), "usage_after_wait": snapshot(after),
                "cpu_user_seconds": after.ru_utime - before.ru_utime,
                "cpu_system_seconds": after.ru_stime - before.ru_stime,
                "peak_rss_raw": after.ru_maxrss, "peak_rss_raw_unit": rss_unit,
                "peak_rss_bytes": peak_bytes,
                "rss_scope": "RUSAGE_CHILDREN after sole child was reaped",
                "within_wall_limit": not timed_out and end - start <= TIMEOUT_SECONDS,
                "within_rss_limit": peak_bytes <= RSS_LIMIT_BYTES,
                "stdout_bytes": len(stdout), "stderr_bytes": len(stderr),
                "stdout_first_8192_bytes": stdout[:8192].decode("utf-8", "replace"),
                "stderr_first_8192_bytes": stderr[:8192].decode("utf-8", "replace")}
            if OUTPUT.exists():
                size = OUTPUT.stat().st_size
                record["output_bytes"] = size
                if size > MAX_OUTPUT_BYTES:
                    raise RuntimeError("child output exceeds declared byte bound; preserved")
                raw = OUTPUT.read_bytes()
                record["output_sha256"] = hashlib.sha256(raw).hexdigest()
                try:
                    child = json.loads(raw)
                    record["child_status"] = child.get("status")
                    record["child_reported_scientific_execution_count"] = child.get(
                        "scientific_execution_count")
                    record["child_reported_scientific_completed"] = child.get("scientific_completed")
                    if "error" in child:
                        record["child_error"] = child["error"]
                except (ValueError, UnicodeError) as exc:
                    record["output_parse_error"] = str(exc)
            lifecycle = record["child_lifecycle"]
            if (returncode == 0 and lifecycle["within_wall_limit"]
                    and lifecycle["within_rss_limit"]
                    and communication_error is None
                    and record.get("child_status") ==
                    "INPUT_PREPARATION_PASS_PENDING_INDEPENDENT_VALIDATION"
                    and record["child_reported_scientific_execution_count"] == 1
                    and record["child_reported_scientific_completed"] is True):
                record["status"] = "EXECUTION_PASS_PENDING_INDEPENDENT_INPUT_VALIDATION"
            else:
                record["failure"] = "child/result/resource acceptance failed; no retry"
        except Exception as exc:
            record["error"] = {"type": type(exc).__name__, "message": str(exc)}
        record["supervisor_self_usage_before_receipt_serialization"] = snapshot(
            resource.getrusage(resource.RUSAGE_SELF))
        record["supervisor_scope"] = (
            "one separate metadata parent; its own peak RSS is not added to or substituted "
            "for child peak RSS; this is not a simultaneous total-task peak measurement")
        receipt.write(json.dumps(record, ensure_ascii=True, indent=2, allow_nan=False) + "\n")
        receipt.flush()
    return 0 if record["status"].startswith("EXECUTION_PASS") else 1


if __name__ == "__main__":
    sys.exit(main())
