#!/usr/bin/env python3
"""Fixed Hermite segment primary residual audit. Default is byte preflight only.

No science is run without --run and a runtime pin of the root source review.
Internal workers require a source-bound request and the actual parent PID.
No FFT, integration, new node, subdivision, parameter change, or retry.
"""
from __future__ import annotations

import time
ENTRY_STARTED = time.monotonic()

import argparse
import ast
import datetime as dt
from fractions import Fraction
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import platform
import resource
import shlex
import signal
import subprocess
import sys
import traceback

HERE = Path(__file__).resolve().parent
WORKTREE = HERE.parents[2]
OUT = HERE / "one-segment-residual-trial-01"
EXTERNAL_STDOUT = HERE / "one-segment-residual-primary.stdout.log"
EXTERNAL_STDERR = HERE / "one-segment-residual-primary.stderr.log"
Q, QP, JH, J = 1 << 52, 1 << 96, 2048, 35937
BASE, HALF, DIGIT = 1 << 248, 1 << 247, 31
LEFT_DIGITS, RIGHT_DIGITS, PRODUCT_DIGITS = 89843, 125780, 215622
PRODUCT_BYTES = 6684282
LABELS = ("1", "2", "3", "12", "13", "23")
CONTRACT = "ONE_SEGMENT_RESIDUAL_EXECUTION_CONTRACT.md"
PROOFS = {
    "C1_RESIDUAL_CONTRACT.md": "a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251",
    "CONTINUOUS_RESIDUAL_COST_PREFLIGHT.md": "0c7ea4b3d33d152f298058a909e446505150d1004529f1a4518c2e1fedc7f796",
    "FULL_NODAL_RESIDUAL_CONTRACT.md": "f3c5327e59931a2e638c039078f78175f4138c53eec139cc57c1ae5fd2cb513b",
    "FULL_NODAL_RESIDUAL_OUTCOME.md": "223c963e10ae14c93a231901dfe1554b8c61b63324537ebc250ddb7ae15d32ee",
    "FULL_NODAL_RESIDUAL_FINAL_REVIEW.md": "6d191cdb7be53601617754769b55b50be6346e5abfc2ca93083bf0518be7bc69",
    "ONE_SEGMENT_RESIDUAL_INCREMENT_PREFLIGHT.md": "9934d16ec106aa99739f70cfa5d643840322f12766faf2f3f2b979f20ae46c61",
    "ONE_SEGMENT_RESIDUAL_INCREMENT_INDEPENDENT_REVIEW.md": "956d20ae6941bfce62cf2e35588bc5e775c09fd38a6c462c685bf2120642a784",
    "ONE_SEGMENT_RESIDUAL_DENOMINATOR_LEMMA.md": "de6b150813559e6d0856b3df8db77491c9a3da4cad1f07a3d94282cd29642104",
    "ONE_SEGMENT_RESIDUAL_DENOMINATOR_INDEPENDENT_DERIVATION.md": "a9d6b288917eb98123afce1bd0f07bf879e530b53701ad9eb9e00f4c5a099171",
    "one-segment-denominator-root-acceptance.json": "faedd5aa722f51541afc38ffe7a42f5ab323b22f9a8e73933f21ad2a48a63f63",
    "CONTROL_FAMILY_NODE_COMPATIBILITY.md": "4f37255af866f4bdeb8f2be9e11a4be76c70a90c994904c2b9934c537b0dac12",
    CONTRACT: "7687786631b17cb9f8e21b3f9723f3eeb8d6e16cf3415a246544cb5c4df9d8eb",
    "ONE_SEGMENT_RESIDUAL_EXECUTION_INDEPENDENT_REVIEW.md": "92af668f2a3fdfe081eb99123af63d781a7e2de90fbba158c70c852b9d868afc",
}
INPUTS = {
    "node-trial-01/manifest.json": "5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd",
    "node-trial-01/modes.npy": "f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896",
    "node-trial-01/block-01280-01343.npz": "abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e",
    "kronecker-block-trial-02/c96-centers.i112le.bin": "c16d26dcbea14b63614d192da27a8b268fa49e689a02fb15499601cc1b611c9e",
    "kronecker-block-trial-02/tensor12-complex.i240le.bin": "795ce995481d41b1fd4c6810101b62d37b187a268eaba992e97ef6f3f79ca0e6",
    "full-nodal-residual-trial-01/tensor-11.i240le.bin": "da3267a95820b39d2c0500c46adc40b98f5a991c6b918ad20110baea9957862a",
    "full-nodal-residual-trial-01/tensor-13.i240le.bin": "e24a6e9ef33331197c3763a85eaabca2ee20ae1ab08953c50a89020eba8ffb13",
    "full-nodal-residual-trial-01/tensor-22.i240le.bin": "eba9e7c39633b7ac3d9362d0745bc6b22a116d79894f5c15498478132c457b40",
    "full-nodal-residual-trial-01/tensor-23.i240le.bin": "0bbc711ff8b8c60f375e569a0db42b700db5a98f3f8d65cc22ed878a49e17ec3",
    "full-nodal-residual-trial-01/tensor-33.i240le.bin": "b879c212204a6745aa3a68f638c1cd9bd8378ea3d40f9ca5161b620e57061584",
    "full-nodal-residual-trial-01/V.i512le.bin": "f1540ec031c880f998885fadc196384f6d7c0ab402c33cbdae0e7535d1b82a82",
    "full-nodal-independent-trial-01/residual-hat-fractions.i256-u256le.bin": "6054a0cbe5a3c91946b3d65acd38b32c720f8da575dbec0dddd79e6a49122ab5",
    "full-nodal-independent-trial-01/result.json": "e637e7fcde5f2fa8ac7cf55d635ada579f6fae189ebf903b6a7a018c351e393b",
    "full-nodal-agreement.json": "f2ccad0d3a963e1a0bdbf0e9695e2979271807201ef3427964b2a11052511ed8",
}
CONFIG = {
    "node_indices": [1280, 1281], "time_denominator": 2048,
    "Q": Q, "QP": QP, "viscosity": 1, "G_count": 4912, "H_count": J,
    "time_degree_center": 3, "time_degree_Df": 5,
    "time_degree_W": 6, "time_degree_S": 12,
    "spatial_radix": 33, "time_stride": J, "coefficient_bits": 248,
    "root_fractional_bits": 128, "worker_labels": list(LABELS),
    "worker_count": 6, "products_per_worker": 3, "new_real_products": 18,
    "left_digits": LEFT_DIGITS, "right_digits": RIGHT_DIGITS,
    "product_digits": PRODUCT_DIGITS, "product_bytes": PRODUCT_BYTES,
    "scalar_bytes": {"n": 10, "b": 12, "new_C": 15, "e": 10, "Df": 31, "W": 34, "S": 68},
    "expected_binary_bytes": 288713460, "wall_seconds": 600,
    "total_peak_rss_bytes": 2 * 1024**3, "output_bytes": 512 * 1024**2,
    "metadata_reserve_bytes": 16 * 1024**2,
    "small_integer_bit_guard": 8192, "rss_sample_period_seconds": 8,
    "progress_period_seconds": 8, "helper_timeout_seconds": 2,
    "worker_termination_grace_seconds": 2,
    "gamma_factor": [3584, 1023], "existing_threshold_lower": [2, 8085825],
    "run_directory": str(OUT), "external_stdout": str(EXTERNAL_STDOUT),
    "external_stderr": str(EXTERNAL_STDERR),
    "stdio_launch_requirement": "root creates both external logs exclusively (xb or shell noclobber)",
    "FFT": False, "integration": False, "subdivision": False, "retry": False,
}


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("ascii")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def valid_hash(value):
    return isinstance(value, str) and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def pin(path, expected):
    if not valid_hash(expected) or sha(path) != expected:
        raise ValueError("invalid or mismatched actual SHA: " + str(path))


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def launch():
    argv = getattr(sys, "orig_argv", None)
    return {"command": shlex.join(argv or [sys.executable, *sys.argv]),
            "command_source": "sys.orig_argv" if argv else "reconstructed argv",
            "executable": sys.executable, "python": sys.version}


def rat(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def pair_fraction(value):
    return Fraction(int(value[0]), int(value[1]))


def rss_bytes(usage):
    raw = int(usage.ru_maxrss)
    return raw if sys.platform == "darwin" else raw * 1024


def self_peak():
    return rss_bytes(resource.getrusage(resource.RUSAGE_SELF))


def config_hash():
    return hashlib.sha256(canonical({"config": CONFIG, "proofs": PROOFS, "inputs": INPUTS})).hexdigest()


def total_output_bytes():
    total = 0
    paths = list(OUT.iterdir()) if OUT.exists() else []
    paths.extend((EXTERNAL_STDOUT, EXTERNAL_STDERR))
    for path in paths:
        try:
            if path.is_file():
                total += path.stat().st_size
        except FileNotFoundError:
            pass  # Atomic rename raced this observation; final census is quiescent.
    return total


def require_stdio_files():
    for fd, path in ((1, EXTERNAL_STDOUT), (2, EXTERNAL_STDERR)):
        actual, wanted = os.fstat(fd), path.stat()
        if (actual.st_dev, actual.st_ino) != (wanted.st_dev, wanted.st_ino):
            raise ValueError("--run requires complete stdio redirected to " + str(path))


def preflight(for_run=False, review_path=None, review_sha=None):
    if sys.version_info < (3, 10) or sys.platform not in ("darwin", "linux") or not hasattr(os, "wait4"):
        raise RuntimeError("Python >=3.10 and POSIX wait4 on macOS/Linux required")
    source = Path(__file__).read_bytes()
    source.decode("ascii")
    compile(ast.parse(source), str(Path(__file__)), "exec")
    for name, expected in {**PROOFS, **INPUTS}.items():
        pin(HERE / name, expected)
    source_sha = hashlib.sha256(source).hexdigest()
    review = None
    if review_path is not None or review_sha is not None:
        if review_path is None or review_sha is None:
            raise ValueError("source-review path and SHA must be supplied together")
        path = Path(review_path).resolve()
        if not path.is_relative_to(HERE):
            raise ValueError("runtime source review must be in this reverse research directory")
        pin(path, review_sha)
        review_text = path.read_text()
        if source_sha not in review_text or PROOFS[CONTRACT] not in review_text:
            raise ValueError("runtime review must explicitly bind this source and final execution contract")
        review = {"path": str(path), "sha256": review_sha,
                  "code_and_contract_hashes_present": True,
                  "root_full_review_is_an_external_human_agent_attestation": True}
    if for_run:
        if review is None:
            raise ValueError("root source review runtime pin required before exclusive claim")
        require_stdio_files()
    return {"status": "STATIC_PINS_PASS_AWAITING_ROOT_UNIQUE_EXECUTION" if review else "STATIC_PINS_PASS_SOURCE_REVIEW_NOT_BOUND",
            "scientific_execution": False, "config": CONFIG, "config_sha256": config_hash(),
            "source_sha256": source_sha, "proof_sha256": PROOFS, "input_sha256": INPUTS,
            "runtime_root_source_review": review, "fixed_pin_count": len(PROOFS)+len(INPUTS),
            "output_directory_exists": OUT.exists(),
            "scope": "one fixed original-reference Hermite segment, not an NS trajectory"}


class BudgetStop(RuntimeError):
    pass


def width(value, bits):
    if abs(value) >= 1 << bits:
        raise AssertionError("strict a priori scalar width failed: " + str(bits))


def get_int(data, index, size, signed=True):
    return int.from_bytes(data[size*index:size*(index+1)], "little", signed=signed)


def encode_ints(values, size, count, bits):
    data = bytearray(size*count)
    used = 0
    for used, value in enumerate(values, 1):
        if used > count:
            raise AssertionError("too many fixed integer fields")
        width(value, bits)
        data[size*(used-1):size*used] = value.to_bytes(size, "little", signed=True)
    if used != count:
        raise AssertionError("wrong fixed integer count")
    return data


class Context:
    def __init__(self, started, filename, identity):
        self.started = started
        self.filename = filename
        self.last_progress = started
        self.temporary_serial = 0
        self.record = {"identity": identity, "pid": os.getpid(), "parent_pid": os.getppid(),
                       "launch": launch(), "started_at_utc": utc(), "execution_status": "RUNNING",
                       "maximum_small_integer_bits_observed": 0, "artifacts": {}, "stage": "starting"}

    def observation(self):
        return {"wall_seconds_from_parent_entry": time.monotonic()-self.started,
                "self_peak_rss_bytes": self_peak(), "all_output_bytes": total_output_bytes()}

    def check(self, stage=None):
        if stage is not None:
            self.record["stage"] = stage
        obs = self.observation()
        if (obs["wall_seconds_from_parent_entry"] >= CONFIG["wall_seconds"]
                or obs["self_peak_rss_bytes"] > CONFIG["total_peak_rss_bytes"]
                or obs["all_output_bytes"] > CONFIG["output_bytes"]):
            raise BudgetStop("observed resource limit: " + json.dumps(obs))
        now = time.monotonic()
        if now-self.last_progress >= CONFIG["progress_period_seconds"]:
            self.last_progress = now
            self.checkpoint()
            print(json.dumps({"progress": self.record["identity"], "stage": self.record["stage"], "resources": obs}), flush=True)
        return obs

    def guard(self, *values):
        size = max((abs(value).bit_length() for value in values), default=0)
        self.record["maximum_small_integer_bits_observed"] = max(size, self.record["maximum_small_integer_bits_observed"])
        if size > CONFIG["small_integer_bit_guard"]:
            raise BudgetStop("small arithmetic exceeded fixed 8192-bit guard")

    def atomic(self, name, data, final=False, new=False):
        path = OUT / name
        if path.parent != OUT or (new and path.exists()):
            raise FileExistsError("artifact overwrite or invalid output path: " + name)
        cap = CONFIG["output_bytes"]-(0 if final else CONFIG["metadata_reserve_bytes"])
        if total_output_bytes()+len(data) > cap and not final:
            raise BudgetStop("output cap including temporary bytes and failure-log reserve")
        self.temporary_serial += 1
        temp = OUT / (name+".tmp."+str(os.getpid())+"."+str(self.temporary_serial))
        with temp.open("xb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        temp.replace(path)

    def checkpoint(self, final=False):
        self.record["resources_before_this_atomic_record_write"] = self.observation()
        data = canonical(self.record)+b"\n"
        self.atomic(self.filename, data, final=final)
        if (OUT/self.filename).read_bytes() != data:
            raise AssertionError("actual canonical metadata record byte readback: " + self.filename)

    def artifact(self, name, data, schema):
        self.check()
        self.atomic(name, data, new=True)
        reread = (OUT / name).read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if reread != data or hashlib.sha256(reread).hexdigest() != digest:
            raise AssertionError("full archive byte readback failed: " + name)
        self.record["artifacts"][name] = {"bytes": len(data), "sha256": digest,
                                         "schema": schema, "actual_byte_readback": True}
        self.check()
        return reread


class ParentContext(Context):
    def __init__(self, started, info):
        super().__init__(started, "run.json", "parent")
        self.record["preflight"] = info
        self.children = {}
        self.handles = []
        self.child_peaks = {}
        self.last_sample = started-100
        self.sampling = False
        self.latest_sample = {"sampled_process_rss_bytes": 0, "including_sampling_helper_peak_bytes": 0}
        self.record["child_processes"] = []
        self.record["rss_samples"] = []

    def peak_sum(self):
        return self_peak()+sum(self.child_peaks.values())

    def observation(self):
        value = super().observation()
        value["parent_plus_all_child_highwater_sum_bytes"] = self.peak_sum()
        value["latest_simultaneous_rss_upper_observation_bytes"] = self.latest_sample["including_sampling_helper_peak_bytes"]
        return value

    def reap(self, pid, options=os.WNOHANG):
        child = self.children[pid]
        if child["done"]:
            return True
        found, status, usage = os.wait4(pid, options)
        if not found:
            return False
        child["done"] = True
        child["process"].returncode = os.waitstatus_to_exitcode(status)
        peak = rss_bytes(usage)
        self.child_peaks[pid] = max(self.child_peaks.get(pid, 0), peak)
        item = child["record"]
        item.update({"exit_code": child["process"].returncode, "reaped_with_wait4": True,
                     "wait4_peak_rss_bytes": peak, "finished_at_utc": utc(),
                     "user_cpu_seconds": usage.ru_utime, "system_cpu_seconds": usage.ru_stime})
        return True

    def spawn(self, command, label, kind, stdout_name, stderr_name):
        out = (OUT / stdout_name).open("xb")
        self.handles.append(out)
        err = (OUT / stderr_name).open("xb")
        self.handles.append(err)
        proc = subprocess.Popen(command, cwd=WORKTREE, stdout=out, stderr=err, env=os.environ.copy())
        item = {"pid": proc.pid, "parent_pid": os.getpid(), "kind": kind, "label": label,
                "command": shlex.join(command), "started_at_utc": utc(),
                "stdout_file": stdout_name, "stderr_file": stderr_name, "stdio_direct_to_files_no_pipes": True}
        self.record["child_processes"].append(item)
        self.children[proc.pid] = {"process": proc, "record": item, "done": False, "handles": (out, err)}
        self.child_peaks[proc.pid] = 0
        return proc.pid

    def helper(self, command, label):
        number = sum(c["record"]["kind"] == "helper" for c in self.children.values())
        stem = "helper-"+str(number).zfill(3)+"-"+label
        pid = self.spawn(command, label, "helper", stem+".stdout.log", stem+".stderr.log")
        deadline = min(self.started+CONFIG["wall_seconds"], time.monotonic()+CONFIG["helper_timeout_seconds"])
        while not self.reap(pid):
            if time.monotonic() >= deadline:
                try:
                    os.kill(pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                self.reap(pid, 0)
                raise BudgetStop("bounded OS helper deadline: " + label)
            time.sleep(0.02)
        child = self.children[pid]
        for stream in child["handles"]:
            stream.flush()
            os.fsync(stream.fileno())
        if child["process"].returncode != 0:
            raise RuntimeError("OS helper failed; full stderr retained: " + stem)
        return (OUT / (stem+".stdout.log")).read_text(), pid

    def sample_rss(self):
        self.sampling = True
        try:
            active = [pid for pid, c in self.children.items() if not c["done"] and c["record"]["kind"] == "worker"]
            pids = [os.getpid(), *active]
            output, helper_pid = self.helper(["/bin/ps", "-o", "pid=,rss=", "-p", ",".join(map(str, pids))], "rss")
            rows = {}
            for line in output.splitlines():
                fields = line.split()
                if len(fields) != 2:
                    raise ValueError("unexpected ps PID/RSS output")
                pid, rss_kib = map(int, fields)
                if pid not in pids or rss_kib < 0:
                    raise ValueError("unexpected sampled PID or RSS")
                rows[pid] = rss_kib*1024
                if pid != os.getpid():
                    self.child_peaks[pid] = max(self.child_peaks[pid], rows[pid])
            if os.getpid() not in rows:
                raise ValueError("parent RSS was not observed")
            for pid in active:
                self.reap(pid)
                if pid not in rows and not self.children[pid]["done"]:
                    raise ValueError("live worker RSS observation missing")
            helper_peak = self.child_peaks[helper_pid]
            self.latest_sample = {"at_utc": utc(), "wall_seconds": time.monotonic()-self.started,
                                  "sampled_pid_rss_bytes": {str(k): v for k, v in rows.items()},
                                  "sampled_process_rss_bytes": sum(rows.values()),
                                  "sampling_helper_pid": helper_pid, "sampling_helper_peak_bytes": helper_peak,
                                  "including_sampling_helper_peak_bytes": sum(rows.values())+helper_peak,
                                  "semantics": "co-sampled parent/workers plus conservative wait4 peak of the sampling helper"}
            self.record["rss_samples"].append(self.latest_sample)
            self.last_sample = time.monotonic()
        finally:
            self.sampling = False

    def check(self, stage=None):
        # No polling method that reaps children may be used: wait4 owns all exits.
        if not self.sampling and time.monotonic()-self.last_sample >= CONFIG["rss_sample_period_seconds"]:
            self.sample_rss()
        for pid, child in self.children.items():
            if child["record"]["kind"] == "worker":
                self.reap(pid)
                if child["done"] and child["process"].returncode != 0:
                    raise RuntimeError("fixed worker failed: " + child["record"]["label"])
        value = super().check(stage)
        if (value["parent_plus_all_child_highwater_sum_bytes"] > CONFIG["total_peak_rss_bytes"]
                or value["latest_simultaneous_rss_upper_observation_bytes"] > CONFIG["total_peak_rss_bytes"]):
            raise BudgetStop("aggregate parent/worker/helper RSS limit: " + json.dumps(value))
        return value

    def stop_and_reap_all(self):
        errors = []
        for pid, child in self.children.items():
            if not child["done"]:
                try:
                    os.kill(pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
                except Exception as exc:
                    errors.append({"operation": "terminate", "pid": pid, "error": repr(exc)})
        until = time.monotonic()+CONFIG["worker_termination_grace_seconds"]
        while any(not c["done"] for c in self.children.values()) and time.monotonic() < until:
            for pid in self.children:
                try:
                    self.reap(pid)
                except Exception as exc:
                    errors.append({"operation": "grace-period wait4", "pid": pid, "error": repr(exc)})
            time.sleep(0.02)
        for pid, child in self.children.items():
            if not child["done"]:
                try:
                    os.kill(pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                except Exception as exc:
                    errors.append({"operation": "kill", "pid": pid, "error": repr(exc)})
                try:
                    self.reap(pid, 0)
                except Exception as exc:
                    errors.append({"operation": "wait4", "pid": pid, "error": repr(exc)})
        for stream in self.handles:
            try:
                stream.flush()
                os.fsync(stream.fileno())
            except Exception as exc:
                errors.append({"operation": "flush child stdio", "file": str(stream.name), "error": repr(exc)})
            finally:
                try:
                    stream.close()
                except Exception as exc:
                    errors.append({"operation": "close child stdio", "file": str(stream.name), "error": repr(exc)})
        self.record["all_child_exits_collected_with_wait4"] = all(c["done"] for c in self.children.values())
        self.record["child_highwater_bytes_by_pid"] = {str(k): v for k, v in self.child_peaks.items()}
        self.record["all_child_stdio"] = []
        for child in self.children.values():
            for key in ("stdout_file", "stderr_file"):
                path = OUT/child["record"][key]
                try:
                    self.record["all_child_stdio"].append({"file": path.name, "bytes": path.stat().st_size,
                                                           "sha256": sha(path)})
                except Exception as exc:
                    errors.append({"operation": "child log byte binding", "file": str(path), "error": repr(exc)})
        self.record["cleanup_errors"] = errors
        if errors:
            raise RuntimeError("one or more child cleanup/log errors; all collected in run record")


def fixed_modes():
    return [p for p in itertools.product(range(-8, 9), repeat=3) if p != (0, 0, 0)]


def check_field(field, modes, opposite, divergence):
    for n, p in enumerate(modes):
        row, other = field[n], field[opposite[n]]
        if any(row[2*j] != other[2*j] or row[2*j+1] != -other[2*j+1] for j in range(3)):
            raise AssertionError("full original-G field conjugacy")
        if divergence and any(sum(p[j]*row[2*j+d] for j in range(3)) for d in (0, 1)):
            raise AssertionError("full original-G exact divergence")


def read_fixed_field(data, layers, size):
    if len(data) != layers*4912*6*size:
        raise ValueError("fixed original-G integer field length")
    return [[tuple(get_int(data, (r*4912+n)*6+d, size) for d in range(6))
             for n in range(4912)] for r in range(layers)]


def signal_stop(signum, frame):
    raise BudgetStop("deadline or stop signal " + str(signum))


def arm_deadline(started):
    for sig in (signal.SIGALRM, signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, signal_stop)
    remaining = CONFIG["wall_seconds"]-(time.monotonic()-started)
    if remaining <= 0:
        raise BudgetStop("parent-entry deadline already exhausted")
    signal.setitimer(signal.ITIMER_REAL, remaining)


def worker_main(label, request_sha):
    if label not in LABELS:
        raise ValueError("invalid fixed worker label")
    request_path = OUT / "worker-request.json"
    pin(request_path, request_sha)
    request = json.loads(request_path.read_text())
    claim = json.loads((OUT / "RUN_CLAIM.json").read_text())
    if (request["parent_pid"] != os.getppid() or claim["pid"] != os.getppid()
            or request["labels"] != list(LABELS) or request["config_sha256"] != config_hash()
            or request["source_sha256"] != sha(Path(__file__))
            or not math.isfinite(request["started_monotonic"])):
        raise ValueError("internal worker request/source/actual parent mismatch")
    with (OUT / ("worker-"+label+".claim.json")).open("x") as stream:
        stream.write(canonical({"pid": os.getpid(), "parent_pid": os.getppid(),
                                "request_sha256": request_sha, "label": label}).decode("ascii")+"\n")
    ctx = Context(request["started_monotonic"], "worker-"+label+".json", "worker-"+label)
    ctx.record.update({"request_sha256": request_sha, "source_sha256": request["source_sha256"],
                       "config_sha256": config_hash(), "products": [], "large_real_products": 0})
    arm_deadline(ctx.started)
    try:
        ctx.checkpoint()
        for path, expected in request["worker_input_sha256"].items():
            pin(Path(path), expected)
        c0_path = HERE / "kronecker-block-trial-02/c96-centers.i112le.bin"
        new_path = OUT / "new-C.i120le.bin"
        C = read_fixed_field(c0_path.read_bytes(), 1, 14)+read_fixed_field(new_path.read_bytes(), 3, 15)
        modes = fixed_modes()
        positions = {p: n for n, p in enumerate(modes)}
        opposite = [positions[tuple(-x for x in p)] for p in modes]
        for r, field in enumerate(C):
            check_field(field, modes, opposite, False)
            for row in field:
                for value in row:
                    width(value, 109 if r == 0 else 112)
        selected = tuple(int(x)-1 for x in label)
        exponents = [(p[0]+8)+33*(p[1]+8)+1089*(p[2]+8) for p in modes]

        def pack_input(right, imaginary):
            count = RIGHT_DIGITS if right else LEFT_DIGITS
            positive, negative = bytearray(DIGIT*count), bytearray(DIGIT*count)
            for r in range(4 if right else 3):
                field = C[r if right else r+1]
                factor = 2 if right and r == 0 else 1
                for n, row in enumerate(field):
                    value = factor*sum(row[2*j+imaginary] for j in selected)
                    width(value, 113)
                    destination = positive if value >= 0 else negative
                    offset = DIGIT*(r*J+exponents[n])
                    destination[offset:offset+DIGIT] = abs(value).to_bytes(DIGIT, "little")
                    if n % 512 == 0:
                        ctx.check("packing fixed inputs")
            result = int.from_bytes(positive, "little")-int.from_bytes(negative, "little")
            if abs(result).bit_length() >= 8*DIGIT*count:
                raise AssertionError("whole signed input width")
            return result

        left_re, left_im = pack_input(False, 0), pack_input(False, 1)
        right_re, right_im = pack_input(True, 0), pack_input(True, 1)
        pairs = ((left_re, right_re, "real*real"), (left_im, right_im, "imag*imag"),
                 (left_re+left_im, right_re+right_im, "(real+imag)*(real+imag)"))
        decoded = []
        for product_index, (left, right, formula) in enumerate(pairs):
            descriptors = []
            for value, count in ((left, LEFT_DIGITS), (right, RIGHT_DIGITS)):
                data = value.to_bytes(DIGIT*count, "little", signed=True)
                descriptors.append({"signed_width_bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                                    "sign": (value > 0)-(value < 0), "absolute_bit_length": abs(value).bit_length()})
            del data
            ctx.record["next_product"] = {"index": product_index, "formula": formula, "inputs": descriptors}
            ctx.check("before product " + str(product_index))
            ctx.checkpoint()
            tick = time.monotonic()
            product = left*right
            elapsed = time.monotonic()-tick
            ctx.record["large_real_products"] += 1
            ctx.check("after product " + str(product_index))
            if abs(product).bit_length() >= 8*PRODUCT_BYTES:
                raise AssertionError("whole signed product width")
            raw = product.to_bytes(PRODUCT_BYTES, "little", signed=True)
            name = "df-"+label+"-product-"+str(product_index)+".signed-le.bin"
            reread = ctx.artifact(name, raw, "one whole signed fixed 6684282-byte integer; not individual balanced digits")
            del raw
            positive, negative = bytearray(PRODUCT_BYTES), bytearray(PRODUCT_BYTES)
            values, carry = [], 0
            for i in range(PRODUCT_DIGITS):
                offset = DIGIT*i
                t = int.from_bytes(reread[offset:offset+DIGIT], "little")+carry
                if t >= HALF:
                    value, carry = t-BASE, 1
                else:
                    value, carry = t, 0
                width(value, 242)
                values.append(value)
                target = positive if value >= 0 else negative
                target[offset:offset+DIGIT] = abs(value).to_bytes(DIGIT, "little")
                if i % 512 == 0:
                    ctx.check("linear decode and signed-buffer repack")
            if carry != int(product < 0):
                raise AssertionError("signed terminal carry; t==BASE is permitted")
            repacked = int.from_bytes(positive, "little")-int.from_bytes(negative, "little")
            if repacked != product:
                raise AssertionError("full linear positive/negative-buffer repack mismatch")
            ctx.record["products"].append({"index": product_index, "formula": formula, "inputs": descriptors,
                                           "file": name, "sha256": ctx.record["artifacts"][name]["sha256"],
                                           "multiplication_wall_seconds": elapsed,
                                           "absolute_bit_length": abs(product).bit_length(), "negative": product < 0,
                                           "decoded_coefficients": PRODUCT_DIGITS, "terminal_carry": carry,
                                           "terminal_quotient": 0, "full_linear_repack_equal": True})
            decoded.append(values)
            del positive, negative, reread, repacked, product
            ctx.checkpoint()
            print(json.dumps({"worker": label, "products_completed": len(decoded), "resources": ctx.observation()}), flush=True)
        data = bytearray(PRODUCT_DIGITS*2*DIGIT)
        for i in range(PRODUCT_DIGITS):
            re = decoded[0][i]-decoded[1][i]
            im = decoded[2][i]-decoded[0][i]-decoded[1][i]
            width(re, 244)
            width(im, 244)
            other = (i//J)*J+(J-1-i % J)
            if (re != decoded[0][other]-decoded[1][other]
                    or im != -(decoded[2][other]-decoded[0][other]-decoded[1][other])):
                raise AssertionError("full Df time-layer conjugacy")
            if i % J == (J-1)//2 and im:
                raise AssertionError("Df zero spatial mode imaginary part")
            data[2*DIGIT*i:DIGIT*(2*i+1)] = re.to_bytes(DIGIT, "little", signed=True)
            data[DIGIT*(2*i+1):2*DIGIT*(i+1)] = im.to_bytes(DIGIT, "little", signed=True)
            if i % 512 == 0:
                ctx.check("combining all signed Df coefficients")
        filename = "df-"+label+".i248le.bin"
        reread = ctx.artifact(filename, data, "[time degree 0..5,H kx-fastest,real/imag]; 31-byte signed; integer Df")
        del data
        for i in range(PRODUCT_DIGITS):
            if (get_int(reread, 2*i, DIGIT) != decoded[0][i]-decoded[1][i]
                    or get_int(reread, 2*i+1, DIGIT) != decoded[2][i]-decoded[0][i]-decoded[1][i]):
                raise AssertionError("all archived Df integer fields")
            if i % 512 == 0:
                ctx.check("Df full integer readback")
        del reread, decoded, pairs, C
        for path, expected in request["worker_input_sha256"].items():
            pin(Path(path), expected)
        pin(Path(__file__), request["source_sha256"])
        if ctx.record["large_real_products"] != 3:
            raise AssertionError("fixed products per worker")
        ctx.record.pop("next_product", None)
        ctx.record["Df"] = {"file": filename, "complete_complex_outputs": PRODUCT_DIGITS,
                             "conjugacy_and_zero_mode_imaginary_part": True,
                             "full_archived_integer_readback": True}
        ctx.record["execution_status"] = "VERIFIED_FINALIZING"
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL, 0)
        ctx.record["execution_status"] = "STOP" if isinstance(exc, BudgetStop) else "FAILED"
        ctx.record["error"] = {"type": type(exc).__name__, "message": str(exc)}
        traceback.print_exc(file=sys.stderr)
        sys.stderr.flush()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        obs = ctx.observation()
        over = (obs["wall_seconds_from_parent_entry"] >= CONFIG["wall_seconds"]
                or obs["self_peak_rss_bytes"] > CONFIG["total_peak_rss_bytes"]
                or obs["all_output_bytes"] > CONFIG["output_bytes"])
        if over:
            ctx.record["execution_status"] = "STOP"
            ctx.record["final_budget_overrun"] = obs
        elif ctx.record["execution_status"] == "VERIFIED_FINALIZING":
            ctx.record["execution_status"] = "WORKER_COMPLETE"
        ctx.record["finished_at_utc"] = utc()
        ctx.checkpoint(final=True)
        obs = ctx.observation()
        if (ctx.record["execution_status"] == "WORKER_COMPLETE"
                and (obs["wall_seconds_from_parent_entry"] >= CONFIG["wall_seconds"]
                     or obs["all_output_bytes"] > CONFIG["output_bytes"]
                     or obs["self_peak_rss_bytes"] > CONFIG["total_peak_rss_bytes"])):
            ctx.record["execution_status"] = "STOP"
            ctx.record["final_budget_overrun"] = obs
            ctx.checkpoint(final=True)
    print(json.dumps({"worker": label, "status": ctx.record["execution_status"],
                      "record_sha256": sha(OUT/ctx.filename), "post_write_observation": ctx.observation()}), flush=True)
    return 0 if ctx.record["execution_status"] == "WORKER_COMPLETE" else 1


def reconstruct(ctx):
    import numpy as np  # Only explicit parent science entry reaches this import.
    ctx.record["environment"]["numpy"] = np.__version__
    ctx.record["environment"]["numpy_path"] = np.__file__
    manifest = json.loads((HERE/"node-trial-01/manifest.json").read_text())
    physical = {"scale": 1, "viscosity": 1, "rho": 1, "grid": 27, "cutoff": 8,
                "time_denominator": 2048, "steps": 5120, "nodes": 5121, "quantization_denominator": Q}
    if (manifest["status"] != "CANDIDATE_NODES_COMPLETE_NOT_NS_CERTIFIED"
            or any(manifest["config"].get(k) != v for k, v in physical.items())):
        raise ValueError("original fixed node manifest status or configuration")
    modes = fixed_modes()
    mode_array = np.load(HERE/"node-trial-01/modes.npy", allow_pickle=False)
    if (mode_array.dtype.str != "<i8" or mode_array.shape != (4912, 3)
            or [tuple(int(x) for x in row) for row in mode_array] != modes
            or hashlib.sha256(memoryview(mode_array).cast("B")).hexdigest() != manifest["modes"]["array_sha256"]):
        raise ValueError("fixed complete original mode array/order/hash")
    blocks = [b for b in manifest["blocks"] if b["first_node"] <= 1280 and b["last_node"] >= 1281]
    if len(blocks) != 1 or blocks[0]["file"] != "block-01280-01343.npz":
        raise ValueError("two fixed existing nodes not in the unique locked block")
    block, raw = blocks[0], {}
    keys = {"node_index", "time_numerator", "time_denominator", "quantization_denominator", "value_q52", "slope_q52"}
    with np.load(HERE/"node-trial-01"/block["file"], allow_pickle=False) as archive:
        if set(archive.files) != keys or set(block["arrays"]) != keys:
            raise ValueError("original block keys")
        for name in sorted(keys):
            array = archive[name]
            descriptor = {"shape": list(array.shape), "dtype": array.dtype.str, "nbytes": array.nbytes,
                          "data_sha256": hashlib.sha256(memoryview(array).cast("B")).hexdigest()}
            if descriptor != block["arrays"][name] or array.dtype.str != "<i8":
                raise ValueError("whole original array data hash/schema: " + name)
            if name in ("value_q52", "slope_q52"):
                if array.shape != (64, 4912, 3, 2):
                    raise ValueError("original value/slope array shape")
                raw[name] = array[:2].copy()
            elif name in ("node_index", "time_numerator"):
                if array.tolist() != list(range(1280, 1344)):
                    raise ValueError("original node/time numerators")
            elif array.tolist() != ([2048] if name == "time_denominator" else [Q]):
                raise ValueError("original time or Q denominator")
            del array
            ctx.check("authenticating original arrays; using only rows 0,1")
    positions = {p: i for i, p in enumerate(modes)}
    opposite = [positions[tuple(-x for x in p)] for p in modes]
    squares = [sum(x*x for x in p) for p in modes]
    lcm = math.lcm(*squares)
    common_D = 2*Q*lcm
    width(common_D, 225)
    nfields = []
    for node in range(2):
        for key in ("value_q52", "slope_q52"):
            encoded, field = raw[key][node], []
            for i, p in enumerate(modes):
                zr, zi = [], []
                for a in range(3):
                    ar, ai = int(encoded[i, a, 0]), int(encoded[i, a, 1])
                    br, bi = int(encoded[opposite[i], a, 0]), int(encoded[opposite[i], a, 1])
                    for value in (ar, ai, br, bi):
                        width(value, 63)  # Promoted first; no int64 abs or addition.
                    zr.append(ar+br)
                    zi.append(ai-bi)
                dotr = sum(p[a]*zr[a] for a in range(3))
                doti = sum(p[a]*zi[a] for a in range(3))
                row = tuple(x for a in range(3) for x in
                            (squares[i]*zr[a]-p[a]*dotr, squares[i]*zi[a]-p[a]*doti))
                for value in row:
                    width(value, 73)
                ctx.guard(*row)
                field.append(row)
                if i % 128 == 0:
                    ctx.check("exact two-node conjugate average and Leray numerator")
            check_field(field, modes, opposite, True)
            nfields.append(field)
    del raw, mode_array
    ndata = encode_ints((v for f in nfields for row in f for v in row), 10, 4*4912*6, 73)
    nread = ctx.artifact("original-n.i80le.bin", ndata,
                         "[node0,node1] each [value,slope],G,3,real/imag; numerator over 2*Q*s")
    if read_fixed_field(nread, 4, 10) != nfields:
        raise AssertionError("all original projected numerator readback")
    del ndata, nread
    b = [[], [], [], []]
    for i in range(4912):
        c0, d0, c1, d1 = [field[i] for field in nfields]
        rows = [tuple(JH*x for x in c0), d0,
                tuple(3*JH*(c1[a]-c0[a])-2*d0[a]-d1[a] for a in range(6)),
                tuple(2*JH*(c0[a]-c1[a])+d0[a]+d1[a] for a in range(6))]
        for a in range(6):
            if (rows[0][a] != JH*c0[a] or rows[1][a] != d0[a]
                    or sum(row[a] for row in rows) != JH*c1[a]
                    or rows[1][a]+2*rows[2][a]+3*rows[3][a] != d1[a]):
                raise AssertionError("original Hermite endpoint/physical slope identity")
        for r, row in enumerate(rows):
            for value in row:
                width(value, 88)
            b[r].append(row)
        if i % 128 == 0:
            ctx.check("exact original Hermite power coefficients")
    for field in b:
        check_field(field, modes, opposite, True)
    bdata = encode_ints((v for f in b for row in f for v in row), 12, 4*4912*6, 88)
    bread = ctx.artifact("hermite-b.i96le.bin", bdata,
                         "[power0..3,G,3,real/imag]; original exact a=b/(2^64*s)")
    if read_fixed_field(bread, 4, 12) != b:
        raise AssertionError("all original Hermite numerator readback")
    del nfields, bdata, bread
    c0 = read_fixed_field((HERE/"kronecker-block-trial-02/c96-centers.i112le.bin").read_bytes(), 1, 14)[0]
    C, errors, Mnum, enum, ties = [c0, [], [], []], [[], [], [], []], [0]*4, [0]*4, [0]*4
    for r in range(4):
        for i, row in enumerate(b[r]):
            denominator = (1 << 64)*squares[i]
            result, errrow = [], []
            for a, numerator in enumerate(row):
                q, remainder = divmod(QP*numerator, denominator)
                rounded = q+int(2*remainder > denominator or (2*remainder == denominator and q % 2 != 0))
                center = c0[i][a] if r == 0 else rounded
                error = QP*numerator-center*denominator
                if (center != rounded or 2*abs(error) > denominator
                        or (2*abs(error) == denominator and center % 2 != 0)):
                    raise AssertionError("exact nearest-even rounding witness")
                width(center, 109 if r == 0 else 112)
                width(error, 71)
                result.append(center)
                errrow.append(error)
                factor = lcm//squares[i]
                if factor*squares[i] != lcm:
                    raise AssertionError("exact mode LCM quotient")
                Mnum[r] += abs(numerator)*factor
                enum[r] += abs(error)*factor
                ties[r] += int(2*abs(error) == denominator)
                ctx.guard(QP*numerator, denominator*center, Mnum[r], enum[r])
            if r:
                C[r].append(tuple(result))
            errors[r].append(tuple(errrow))
            if i % 128 == 0:
                ctx.check("all four coefficient rounding witnesses and weighted exact sums")
        check_field(C[r], modes, opposite, False)
    cdata = encode_ints((v for f in C[1:] for row in f for v in row), 15, 3*4912*6, 112)
    cread = ctx.artifact("new-C.i120le.bin", cdata, "[power1..3,G,3,real/imag]; integer QP96 centers; old C0 not copied")
    if read_fixed_field(cread, 3, 15) != C[1:]:
        raise AssertionError("all new C integer readback")
    edata = encode_ints((v for f in errors for row in f for v in row), 10, 4*4912*6, 71)
    eread = ctx.artifact("rounding-e.i80le.bin", edata,
                         "[power0..3,G,3,real/imag]; signed e=QP*b-C*(2^64*s)")
    if read_fixed_field(eread, 4, 10) != errors:
        raise AssertionError("all rounding-error numerator readback")
    del cdata, cread, edata, eread, C, errors
    Mden = (1 << 64)*lcm
    M = [Fraction(value, Mden) for value in Mnum]
    delta = [Fraction(value, Mden*QP) for value in enum]
    old = json.loads((HERE/"full-nodal-independent-trial-01/result.json").read_text())
    if M[0] != pair_fraction(old["input_connection"]["M"]) or delta[0] != pair_fraction(old["input_connection"]["delta"]):
        raise AssertionError("old exact M0/delta0 connection")
    Mstar, dstar = sum(M, Fraction(0)), sum(delta, Fraction(0))
    E = {j: 28**(j+1)*(2*Mstar*dstar+dstar*dstar) for j in (0, 2)}
    if not (Mstar < 1 << 32 and dstar < Fraction(1, 1 << 80)
            and E[0] < Fraction(1, 1 << 41) and E[2] < Fraction(1, 1 << 31)):
        raise AssertionError("already-proved whole-segment input error a priori bounds")
    for v in [*M, *delta, Mstar, dstar, *E.values()]:
        ctx.guard(v.numerator, v.denominator)
    ctx.record["reconstruction"] = {
        "original_array_descriptor_hashes": block["arrays"], "used_node_indices": [1280, 1281],
        "logical_original_raw_scalars_checked_after_promotion": 117888,
        "D_from_NR1_fixed_modes": str(common_D), "mode_lcm": str(lcm),
        "Hermite_common_denominator_for_M_delta_only": str(Mden),
        "original_fields_exact_divergence_conjugacy_and_Hermite_endpoints": True,
        "center_conjugacy": True, "center_divergence_assumed": False,
        "auxiliary_center_cross_segment_C1_assumed": False,
        "M_numerators": list(map(str, Mnum)), "delta_numerators": list(map(str, enum)),
        "ties_per_power": ties, "M": [rat(x) for x in M], "delta": [rat(x) for x in delta],
        "M_star": rat(Mstar), "delta_star": rat(dstar), "E_star": {str(j): rat(E[j]) for j in (0, 2)},
        "old_M0_delta0_exactly_equal": True, "all_reconstruction_binary_integer_readback": True}
    ctx.checkpoint()
    return {"modes": modes, "positions": positions, "squares": squares,
            "b": b, "D": common_D, "E": E, "old_result": old}


def dispatch_workers(ctx, info):
    request = {"parent_pid": os.getpid(), "started_monotonic": ctx.started, "labels": list(LABELS),
               "source_sha256": info["source_sha256"], "config_sha256": config_hash(),
               "worker_input_sha256": {
                   str(HERE/"kronecker-block-trial-02/c96-centers.i112le.bin"):
                       INPUTS["kronecker-block-trial-02/c96-centers.i112le.bin"],
                   str(OUT/"new-C.i120le.bin"): ctx.record["artifacts"]["new-C.i120le.bin"]["sha256"]}}
    ctx.atomic("worker-request.json", canonical(request)+b"\n", new=True)
    if json.loads((OUT/"worker-request.json").read_text()) != request:
        raise AssertionError("worker request actual JSON readback")
    request_sha = sha(OUT/"worker-request.json")
    pids = []
    for label in LABELS:
        command = [sys.executable, "-B", str(Path(__file__).resolve()), "--worker", label,
                   "--request-sha256", request_sha]
        pids.append(ctx.spawn(command, label, "worker", "worker-"+label+".stdout.log", "worker-"+label+".stderr.log"))
    ctx.record["worker_request"] = {"file": "worker-request.json", "sha256": request_sha}
    ctx.checkpoint()

    while any(not ctx.children[pid]["done"] for pid in pids):
        for pid in pids:
            ctx.reap(pid)
        ctx.check("six independent fixed polarization workers")
        time.sleep(0.1)
    collected = {}
    for label, pid in zip(LABELS, pids, strict=True):
        child = ctx.children[pid]
        for stream in child["handles"]:
            stream.flush()
            os.fsync(stream.fileno())
        path = OUT/("worker-"+label+".json")
        record = json.loads(path.read_text())
        if (record["execution_status"] != "WORKER_COMPLETE" or record["pid"] != pid
                or record["parent_pid"] != os.getpid() or record["source_sha256"] != info["source_sha256"]
                or record["config_sha256"] != config_hash() or record["request_sha256"] != request_sha
                or record["large_real_products"] != 3 or len(record["products"]) != 3):
            raise AssertionError("completed worker identity/source/scope mismatch")
        reported_peak = record["resources_before_this_atomic_record_write"]["self_peak_rss_bytes"]
        ctx.child_peaks[pid] = max(ctx.child_peaks[pid], reported_peak)
        expected_names = {"df-"+label+".i248le.bin", *(
            "df-"+label+"-product-"+str(i)+".signed-le.bin" for i in range(3))}
        if set(record["artifacts"]) != expected_names:
            raise AssertionError("fixed worker artifact set")
        for name, descriptor in record["artifacts"].items():
            expected_size = PRODUCT_BYTES*(2 if name.endswith(".i248le.bin") else 1)
            if (descriptor["bytes"] != expected_size or (OUT/name).stat().st_size != expected_size
                    or not descriptor["actual_byte_readback"]):
                raise AssertionError("full worker artifact size/readback")
            pin(OUT/name, descriptor["sha256"])
            if name in ctx.record["artifacts"]:
                raise AssertionError("worker artifact collision")
            ctx.record["artifacts"][name] = descriptor
        collected[label] = {"pid": pid, "record_file": path.name, "record_sha256": sha(path),
                            "products": record["products"], "Df": record["Df"],
                            "wait4_peak_rss_bytes": child["record"]["wait4_peak_rss_bytes"]}
        ctx.check("parent validating completed worker archives")
    ctx.record["workers"] = collected
    ctx.record["new_real_products_completed"] = sum(len(c["products"]) for c in collected.values())
    if ctx.record["new_real_products_completed"] != 18:
        raise AssertionError("complete fixed 18-product scope")
    ctx.checkpoint()


def assemble_W(ctx, original):
    dfs = {label: (OUT/("df-"+label+".i248le.bin")).read_bytes() for label in LABELS}
    if any(len(data) != PRODUCT_DIGITS*2*DIGIT for data in dfs.values()):
        raise ValueError("complete six Df file lengths")
    oldV = (HERE/"full-nodal-residual-trial-01/V.i512le.bin").read_bytes()
    oldrho = (HERE/"full-nodal-independent-trial-01/residual-hat-fractions.i256-u256le.bin").read_bytes()
    if len(oldV) != J*6*64 or len(oldrho) != J*6*64:
        raise ValueError("old complete V/phase archive lengths")
    output_modes = [(x, y, z) for z in range(-16, 17) for y in range(-16, 17) for x in range(-16, 17)]
    data = bytearray(7*J*6*34)
    zero = (0, 0, 0, 0, 0, 0)
    parity_scalars = old_divisions = 0
    for index, k in enumerate(output_modes):
        s = sum(x*x for x in k)
        commonD = original["D"]
        constant = []
        for a in range(6):
            v = get_int(oldV, 6*index+a, 64)
            w, remainder = divmod(v, commonD)
            if remainder:
                raise AssertionError("full old V/D exact scalar division")
            width(w, 263)
            old_divisions += 1
            offset = 64*(6*index+a)
            nr = int.from_bytes(oldrho[offset:offset+32], "little", signed=True)
            dr = int.from_bytes(oldrho[offset+32:offset+64], "little")
            if dr <= 0 or (s and w*dr != nr*s*QP*QP) or (not s and (w or nr or dr != 1)):
                raise AssertionError("old W0 matches exact phase-bearing independent residual")
            ctx.guard(v, w, dr, nr)
            constant.append(w)
            offset = 34*(6*index+a)
            data[offset:offset+34] = w.to_bytes(34, "little", signed=True)
        if any(sum(k[j]*constant[2*j+d] for j in range(3)) for d in (0, 1)):
            raise AssertionError("old constant W divergence")
        source_index = original["positions"].get(k)
        for m in range(1, 7):
            raw = {label: tuple(get_int(values, 2*((m-1)*J+index)+d, DIGIT) for d in (0, 1))
                   for label, values in dfs.items()}
            for row in raw.values():
                for value in row:
                    width(value, 244)
            tensor = {(0, 0): raw["1"], (1, 1): raw["2"], (2, 2): raw["3"]}
            for first, second, label in ((0, 1, "12"), (0, 2, "13"), (1, 2, "23")):
                values = []
                for d in (0, 1):
                    numerator = raw[label][d]-raw[str(first+1)][d]-raw[str(second+1)][d]
                    value, rem = divmod(numerator, 2)
                    if rem:
                        raise AssertionError("complete polarization coefficient parity")
                    width(value, 245)
                    parity_scalars += 1
                    values.append(value)
                tensor[(first, second)] = tuple(values)
            if source_index is None:
                U = zero
            else:
                bm = original["b"][m][source_index] if m <= 3 else zero
                bn = original["b"][m+1][source_index] if m+1 <= 3 else zero
                U = tuple((1 << 128)*(JH*(m+1)*bn[a]+s*bm[a]) for a in range(6))
            F = tuple(sum(k[j]*tensor[tuple(sorted((j, ell)))][d] for j in range(3))
                      for ell in range(3) for d in (0, 1))
            dotF = tuple(sum(k[j]*F[2*j+d] for j in range(3)) for d in (0, 1))
            N = tuple(s*F[2*j+d]-k[j]*dotF[d] for j in range(3) for d in (0, 1))
            W = tuple(value for j in range(3) for value in (U[2*j]-N[2*j+1], U[2*j+1]+N[2*j]))
            for row, bits in ((U, 228), (F, 251), (N, 262), (W, 263)):
                for value in row:
                    width(value, bits)
                ctx.guard(*row)
            if not s and (any(U) or any(N) or any(W)):
                raise AssertionError("zero mode handled without dividing by s")
            for row in (U, N, W):
                if any(sum(k[j]*row[2*j+d] for j in range(3)) for d in (0, 1)):
                    raise AssertionError("full U/N/W divergence identity")
            for a, value in enumerate(W):
                offset = 34*((m*J+index)*6+a)
                data[offset:offset+34] = value.to_bytes(34, "little", signed=True)
        if index % 512 == 0 or index == J-1:
            ctx.record["W_outputs_processed"] = index+1
            ctx.check("complete signed W assembly including G-outside modes")
    if old_divisions != J*6 or parity_scalars != 6*J*3*2:
        raise AssertionError("full old-phase and polarization scope")
    reread = ctx.artifact("W.i272le.bin", data,
                         "[power0..6,H kx-fastest,3,real/imag]; signed 34-byte W; rho=W/(s*QP^2); zero mode zero")
    del data, dfs, oldV, oldrho
    for m in range(7):
        for index, k in enumerate(output_modes):
            row = tuple(get_int(reread, (m*J+index)*6+a, 34) for a in range(6))
            other = tuple(get_int(reread, (m*J+J-1-index)*6+a, 34) for a in range(6))
            if any(row[2*j] != other[2*j] or row[2*j+1] != -other[2*j+1] for j in range(3)):
                raise AssertionError("all archived W coefficients conjugacy")
            if any(sum(k[j]*row[2*j+d] for j in range(3)) for d in (0, 1)):
                raise AssertionError("all archived W coefficients divergence")
            if k == (0, 0, 0) and any(row):
                raise AssertionError("archived W zero mode")
            if index % 512 == 0:
                ctx.check("full W archive projection/conjugacy readback")
    ctx.record["W_connection"] = {
        "old_V_exact_divisions": old_divisions, "old_phase_fraction_scalars_equal": old_divisions,
        "old_constant_convolution_recomputed": False,
        "polarization_even_real_imag_numerators": parity_scalars,
        "all_U_N_W_divergence_and_W_conjugacy": True,
        "full_modes": J, "time_coefficients": 7, "old_constant_error_added_separately": False}
    ctx.checkpoint()
    return reread, output_modes


def square_coefficients(rows):
    # All ordered time pairs, including both r!=s orders.
    return [sum(rows[r][a]*rows[m-r][a] for r in range(max(0, m-6), min(6, m)+1) for a in range(6))
            for m in range(13)]


def norms_and_bernstein(ctx, original, wdata, output_modes):
    sdata = bytearray(13*J*68)
    for index in range(J):
        rows = [tuple(get_int(wdata, (r*J+index)*6+a, 34) for a in range(6)) for r in range(7)]
        coefficients = square_coefficients(rows)
        for m, value in enumerate(coefficients):
            width(value, 532)
            ctx.guard(value)
            offset = 68*(m*J+index)
            sdata[offset:offset+68] = value.to_bytes(68, "little", signed=True)
        if index % 512 == 0:
            ctx.check("signed degree12 S from actual archived W")
    sread = ctx.artifact("S.i544le.bin", sdata,
                         "[power0..12,H kx-fastest]; 68-byte SIGNED per-mode squared-polynomial coefficient; may be negative")
    del sdata
    A2, A0lo, A0hi, inexact = [0]*13, [0]*13, [0]*13, [0]*13
    negative_counts = [0]*13
    for index, k in enumerate(output_modes):
        s = sum(x*x for x in k)
        rows = [tuple(get_int(wdata, (r*J+index)*6+a, 34) for a in range(6)) for r in range(7)]
        independently_read_W_square = square_coefficients(rows)
        for m in range(13):
            value = get_int(sread, m*J+index, 68)
            if (value != independently_read_W_square[m]
                    or value != get_int(sread, m*J+J-1-index, 68)):
                raise AssertionError("all archived signed S vs full W/time pairs and opposite mode")
            width(value, 532)
            negative_counts[m] += int(value < 0)
            if not s:
                if value:
                    raise AssertionError("signed S zero spatial mode")
                continue
            quotient, remainder = divmod(value, s*s)
            if not (0 <= remainder < s*s and quotient*s*s+remainder == value):
                raise AssertionError("signed mathematical floor/ceil Euclidean witness")
            A2[m] += value
            A0lo[m] += quotient
            A0hi[m] += quotient+int(remainder != 0)
            inexact[m] += int(remainder != 0)
            ctx.guard(A2[m], A0lo[m], A0hi[m])
        if index % 512 == 0:
            ctx.check("complete signed S readback, zero-order floor/ceil and exact H2 sum")
    if any(A0hi[m]-A0lo[m] != inexact[m] or not 0 <= inexact[m] <= 35936 for m in range(13)):
        raise AssertionError("all signed power-coefficient interval widths")
    denominator = QP**4
    q2 = [Fraction(x, denominator) for x in A2]
    q0lo = [Fraction(x, denominator) for x in A0lo]
    q0hi = [Fraction(x, denominator) for x in A0hi]
    old = original["old_result"]
    if (q2[0] != pair_fraction(old["intervals"]["2"]["center_norm_square"])
            or not q0lo[0] <= pair_fraction(old["intervals"]["0"]["center_norm_square"]) <= q0hi[0]):
        raise AssertionError("constant signed-square coefficient connects to old exact center norms")
    weights = [[Fraction(math.comb(m, ell), math.comb(12, ell)) for ell in range(m+1)] for m in range(13)]

    def transform(values):
        return [sum((weights[m][ell]*values[ell] for ell in range(m+1)), Fraction(0)) for m in range(13)]

    b2, b0lo, b0hi = transform(q2), transform(q0lo), transform(q0hi)
    for m in range(13):
        actual_width = b0hi[m]-b0lo[m]
        propagated_width = sum((weights[m][ell]*Fraction(inexact[ell], denominator) for ell in range(m+1)), Fraction(0))
        if (actual_width != propagated_width or actual_width < 0
                or actual_width > Fraction(13*35936, denominator)):
            raise AssertionError("Bernstein interval width must propagate, not remain the power width")
    bounds = {0: max(Fraction(0), *b0hi), 2: max(Fraction(0), *b2)}
    P = 1 << 128
    root_records, rbar = {}, {}
    for j in (0, 2):
        argument = bounds[j]
        numerator, denom = argument.numerator, argument.denominator
        scaled = P*P*numerator
        quotient, remainder = divmod(scaled, denom)
        lower = math.isqrt(quotient)
        upper = lower+int(lower*lower*denom != scaled)
        if not (lower*lower*denom <= scaled < (lower+1)*(lower+1)*denom and scaled <= upper*upper*denom):
            raise AssertionError("128-bit root containment of actual rational Bernstein bound")
        ctx.guard(scaled, quotient, remainder, lower*lower*denom, upper*upper*denom)
        rbar[j] = Fraction(upper, P)+original["E"][j]
        root_records[str(j)] = {
            "argument_is_Bernstein_upper_bound_not_actual_norm_square": True,
            "argument": rat(argument), "scale": str(P), "scaled_numerator": str(scaled),
            "quotient": str(quotient), "remainder": str(remainder),
            "floor_numerator": str(lower), "ceil_numerator": str(upper),
            "true_rational_square_equality": lower*lower*denom == scaled,
            "root_lower": rat(Fraction(lower, P)), "root_upper": rat(Fraction(upper, P)),
            "E_star_added_once": rat(original["E"][j]), "original_residual_segment_upper": rat(rbar[j]),
            "root_lower_is_NOT_a_residual_lower_bound": True}
    gamma = Fraction(3584, 1023)*max(rbar[2], 64*rbar[0])
    threshold = Fraction(2, 8085825)
    gamma_state = ("SEGMENT_UPPER_BOUND_WITHIN_EXISTING_SUFFICIENT_THRESHOLD" if gamma < threshold
                   else "NOT_CERTIFIED_BY_THIS_UPPER_BOUND")
    for value in [*q2, *q0lo, *q0hi, *b2, *b0lo, *b0hi, *rbar.values(), gamma]:
        ctx.guard(value.numerator, value.denominator)
    result = {
        "schema": "one-fixed-segment-primary-residual-bounds-v1",
        "status": "PRIMARY_ONE_SEGMENT_BOUNDS_COMPUTED_PENDING_INDEPENDENT_REVIEW",
        "admission_requires_final_run_completion_within_budget": True,
        "scope": "same original reference on [1280/2048,1281/2048] only; not NS/global or all-window certificate",
        "source_sha256": ctx.record["preflight"]["source_sha256"], "config_sha256": config_hash(),
        "source_commit": ctx.record["source_commit"],
        "complete_signed_S": {"A2": list(map(str, A2)), "A0_floor_sums": list(map(str, A0lo)),
                               "A0_ceil_sums": list(map(str, A0hi)), "noninteger_counts": inexact,
                               "negative_coefficient_counts": negative_counts, "denominator": str(denominator),
                               "all_W_to_S_readback_equal": True, "old_constant_norm_connection": True},
        "power_coefficients": {"2_exact": [rat(x) for x in q2],
                               "0_lower": [rat(x) for x in q0lo], "0_upper": [rat(x) for x in q0hi]},
        "Bernstein": {"degree": 12, "weights": [[rat(x) for x in row] for row in weights],
                      "2_exact": [rat(x) for x in b2], "0_lower": [rat(x) for x in b0lo],
                      "0_upper": [rat(x) for x in b0hi],
                      "0_actual_widths": [rat(hi-lo) for lo, hi in zip(b0lo, b0hi, strict=True)],
                      "0_propagated_width_bound": rat(Fraction(13*35936, denominator))},
        "root_bounds": root_records,
        "original_residual_segment_upper": {str(j): rat(rbar[j]) for j in (0, 2)},
        "fixed_control_interface": {"gamma_factor": rat(Fraction(3584, 1023)), "Gamma_I": rat(gamma),
                                    "existing_sufficient_threshold_lower": rat(threshold), "status": gamma_state,
                                    "new_epsilon_selected": False, "derivative_or_other_segment_bounds_certified": False},
        "reconstruction": ctx.record["reconstruction"], "W_connection": ctx.record["W_connection"],
        "large_real_products": 18, "new_center_time_coefficients": [1, 2, 3],
        "old_constant_convolution_recomputed": False,
        "input_sha256": INPUTS, "proof_sha256": PROOFS,
    }
    ctx.check("complete degree12 Bernstein, 128-bit roots, single input-error addition and fixed Gamma test")
    return result


def over_budget(obs):
    return (obs["wall_seconds_from_parent_entry"] >= CONFIG["wall_seconds"]
            or obs["self_peak_rss_bytes"] > CONFIG["total_peak_rss_bytes"]
            or obs["all_output_bytes"] > CONFIG["output_bytes"]
            or obs.get("parent_plus_all_child_highwater_sum_bytes", 0) > CONFIG["total_peak_rss_bytes"]
            or obs.get("latest_simultaneous_rss_upper_observation_bytes", 0) > CONFIG["total_peak_rss_bytes"])


def flush_outer_stdio():
    for stream in (sys.stdout, sys.stderr):
        stream.flush()
        os.fsync(stream.fileno())


def execute(info):
    # All byte pins and the runtime root review were checked before this claim.
    # An existing directory, including an empty one, is never reused.
    OUT.mkdir(exist_ok=False)
    ctx = ParentContext(ENTRY_STARTED, info)
    with (OUT/"RUN_CLAIM.json").open("x") as stream:
        stream.write(canonical({"pid": os.getpid(), "parent_pid": os.getppid(),
                                "started_at_utc": utc(), "started_monotonic": ENTRY_STARTED,
                                "source_sha256": info["source_sha256"],
                                "config_sha256": info["config_sha256"], "launch": launch(),
                                "runtime_root_source_review": info["runtime_root_source_review"]}).decode("ascii")+"\n")
        stream.flush()
        os.fsync(stream.fileno())
    ctx.record.update({"source_sha256": info["source_sha256"], "config_sha256": info["config_sha256"],
                       "environment": {"platform": platform.platform(), "machine": platform.machine(),
                                       "logical_cpu_count": os.cpu_count(), "python": sys.version,
                                       "executable": sys.executable,
                                       "thread_environment": {key: os.environ.get(key) for key in
                                           ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                                            "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")}},
                       "arithmetic": "exact Python integers/Fraction; NumPy only reads original NPY/NPZ",
                       "worker_start": "six Popen fresh Python interpreters; no array or integer IPC",
                       "resource_semantics": "observed limits, not OS prevention of transient allocation; wait4 owns every child exit",
                       "timer_semantics": "first module monotonic timestamp after importing time; includes preflight and finalization",
                       "independent_review_or_comparison_completed_by_this_run": False})
    try:
        arm_deadline(ENTRY_STARTED)
        ctx.checkpoint()
        source_commit, _ = ctx.helper(["git", "rev-parse", "HEAD"], "git-head")
        source_commit = source_commit.strip()
        if len(source_commit) != 40 or any(c not in "0123456789abcdef" for c in source_commit):
            raise ValueError("invalid actual reverse worktree source commit")
        ctx.record["source_commit"] = source_commit
        ctx.record["source_commit_cwd"] = str(WORKTREE)
        if sys.platform == "darwin":
            cpu, _ = ctx.helper(["/usr/sbin/sysctl", "-n", "machdep.cpu.brand_string"], "cpu")
            ctx.record["environment"]["cpu"] = cpu.strip()
        else:
            ctx.record["environment"]["cpu"] = platform.processor()
        ctx.atomic("source-snapshot.py", Path(__file__).read_bytes(), new=True)
        config_data = canonical(info)+b"\n"
        ctx.atomic("config-and-bindings.json", config_data, new=True)
        if (OUT/"config-and-bindings.json").read_bytes() != config_data:
            raise AssertionError("actual canonical configuration snapshot byte readback")
        if sha(OUT/"source-snapshot.py") != info["source_sha256"]:
            raise AssertionError("actual source snapshot byte readback")
        ctx.record["metadata_snapshots"] = {
            "source-snapshot.py": {"sha256": info["source_sha256"], "bytes": (OUT/"source-snapshot.py").stat().st_size,
                                   "actual_byte_readback": True},
            "config-and-bindings.json": {"sha256": sha(OUT/"config-and-bindings.json"), "bytes": len(config_data),
                                         "actual_byte_readback": True}}
        ctx.check("fixed source, configuration, environment and input pins accepted")
        original = reconstruct(ctx)
        dispatch_workers(ctx, info)
        wdata, modes = assemble_W(ctx, original)
        result = norms_and_bernstein(ctx, original, wdata, modes)
        result.update({"source_commit": source_commit, "source_sha256": info["source_sha256"],
                       "config_sha256": info["config_sha256"],
                       "runtime_root_source_review": info["runtime_root_source_review"],
                       "artifacts": ctx.record["artifacts"]})
        ctx.atomic("result.json", canonical(result)+b"\n", new=True)
        if json.loads((OUT/"result.json").read_text()) != result:
            raise AssertionError("full result JSON actual readback")
        ctx.record["result"] = {"file": "result.json", "sha256": sha(OUT/"result.json"),
                                "actual_readback": True, "scope": result["status"]}
        for name, descriptor in ctx.record["artifacts"].items():
            if (OUT/name).stat().st_size != descriptor["bytes"]:
                raise AssertionError("final complete binary size: " + name)
            pin(OUT/name, descriptor["sha256"])
            ctx.check("final full binary archive byte bindings")
        binary_bytes = sum(d["bytes"] for d in ctx.record["artifacts"].values())
        if binary_bytes != CONFIG["expected_binary_bytes"] or len(ctx.record["artifacts"]) != 30:
            raise AssertionError("fixed complete 30 binary files / 288713460 bytes")
        ctx.record["complete_binary_bytes"] = binary_bytes
        for name, expected in {**PROOFS, **INPUTS}.items():
            pin(HERE/name, expected)
            ctx.check("final unchanged input and reviewed mathematical sources")
        pin(Path(__file__), info["source_sha256"])
        review = info["runtime_root_source_review"]
        pin(Path(review["path"]), review["sha256"])
        ctx.record["final_input_source_review_bindings_unchanged"] = True
        ctx.record["execution_status"] = "VERIFIED_FINALIZING"
        ctx.check("all finite arithmetic and source bindings finished; collecting all child resources")
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL, 0)
        ctx.record["execution_status"] = "STOP" if isinstance(exc, BudgetStop) else "FAILED"
        ctx.record["error"] = {"type": type(exc).__name__, "message": str(exc)}
        traceback.print_exc(file=sys.stderr)
        sys.stderr.flush()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        try:
            ctx.stop_and_reap_all()
        except BaseException as exc:
            ctx.record["execution_status"] = "FAILED"
            ctx.record["cleanup_error"] = {"type": type(exc).__name__, "message": str(exc)}
            traceback.print_exc(file=sys.stderr)
        flush_outer_stdio()
        final_obs = ctx.observation()
        if over_budget(final_obs):
            ctx.record["execution_status"] = "STOP"
            ctx.record["final_budget_overrun"] = final_obs
        elif ctx.record["execution_status"] == "VERIFIED_FINALIZING":
            if not ctx.record.get("all_child_exits_collected_with_wait4", False):
                ctx.record["execution_status"] = "FAILED"
                ctx.record["error"] = {"type": "IncompleteResources", "message": "not every child exit was collected"}
            else:
                ctx.record["execution_status"] = "PRIMARY_COMPLETE_PENDING_INDEPENDENT_REVIEW"
        ctx.record["finished_at_utc"] = utc()
        ctx.record["final_observation_before_last_record_write"] = final_obs
        ctx.record["output_census_before_last_record_write"] = [
            {"file": p.name, "bytes": p.stat().st_size}
            for p in sorted(OUT.iterdir()) if p.is_file()]
        ctx.record["external_stdio_before_last_record_write"] = [
            {"file": str(p), "bytes": p.stat().st_size, "sha256": sha(p),
             "scope": "prefix before this final record and final stdout, not a self hash"}
            for p in (EXTERNAL_STDOUT, EXTERNAL_STDERR)]
        ctx.checkpoint(final=True)
        after_write = ctx.observation()
        if over_budget(after_write):
            ctx.record["execution_status"] = "STOP"
            ctx.record["final_budget_overrun"] = after_write
            ctx.checkpoint(final=True)
    final = {"status": ctx.record["execution_status"], "run_file": str(OUT/"run.json"),
             "run_sha256": sha(OUT/"run.json"), "result": ctx.record.get("result"),
             "post_record_write_observation": ctx.observation(),
             "stdout_size_excludes_this_final_line": True}
    print(json.dumps(final, sort_keys=True), flush=True)
    flush_outer_stdio()
    after_stdout = ctx.observation()
    if over_budget(after_stdout):
        ctx.record["execution_status"] = "STOP"
        ctx.record["final_budget_overrun_including_previous_final_stdout"] = after_stdout
        ctx.checkpoint(final=True)
        print(json.dumps({"status": "STOP", "run_sha256": sha(OUT/"run.json"),
                          "post_record_write_observation": ctx.observation(),
                          "supersedes_earlier_final_line": True}), flush=True)
        flush_outer_stdio()
    return 0 if ctx.record["execution_status"] == "PRIMARY_COMPLETE_PENDING_INDEPENDENT_REVIEW" else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choices = parser.add_mutually_exclusive_group()
    choices.add_argument("--run", action="store_true", help="one scientific run, only after root source review")
    choices.add_argument("--check-only", action="store_true", help="syntax/config/fixed byte SHA only (default)")
    choices.add_argument("--describe", action="store_true", help="same read-only byte preflight, with complete configuration")
    choices.add_argument("--worker", choices=LABELS, help=argparse.SUPPRESS)
    parser.add_argument("--request-sha256", help=argparse.SUPPRESS)
    parser.add_argument("--source-review", help="actual root source review path, within this research directory")
    parser.add_argument("--source-review-sha256", help="actual fixed SHA of the root source review")
    args = parser.parse_args()
    if args.worker:
        if args.request_sha256 is None or args.source_review is not None or args.source_review_sha256 is not None:
            raise ValueError("internal worker only accepts the source-bound parent request")
        return worker_main(args.worker, args.request_sha256)
    if args.request_sha256 is not None:
        raise ValueError("request SHA only belongs to an internal parent-bound worker")
    info = preflight(args.run, args.source_review, args.source_review_sha256)
    if not args.run:
        info["launch"] = launch()
        print(json.dumps(info, sort_keys=True), flush=True)
        return 0
    return execute(info)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyboardInterrupt, Exception) as error:
        traceback.print_exc(file=sys.stderr)
        sys.stderr.flush()
        print(json.dumps({"status": "STARTUP_OR_RECORD_WRITE_FAILED", "type": type(error).__name__,
                          "message": str(error), "launch": launch(),
                          "scientific_completion_admitted": False}), flush=True)
        raise SystemExit(1)
