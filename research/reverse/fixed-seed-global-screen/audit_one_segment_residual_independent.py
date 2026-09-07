#!/usr/bin/env python3
"""One fixed Hermite segment: independent full direct convolution.

Default/check-only: ASCII, AST, config and actual SHA checks only.
Only --run loads scientific arrays. Never imports a primary scientific kernel.
The root launcher must create stdout/stderr logs exclusively (xb/noclobber).
This program's regular/empty checks cannot prove historical exclusive creation.
"""
import time

START = time.monotonic()

import argparse
import ast
import ctypes
from datetime import datetime, timezone
import fcntl
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import re
import resource
import signal
import stat
import sys
import threading
import traceback

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TREE = Path("/Users/kasifa/Documents/Math/navier-stokes-reverse")
OUT = HERE / "one-segment-residual-independent-trial-01"
G, J = 4912, 35937
Q, QP = 1 << 52, 1 << 96
HINV, MAX_BITS, ROOT_BITS = 2048, 8192, 128
WALL, RSS_LIMIT, FILE_LIMIT = 600.0, 2 << 30, 512 << 20
FAILURE_RESERVE, METADATA_LIMIT = 1 << 20, 8 << 20
SAMPLE_SECONDS, PROGRESS_ROWS = 0.2, 128
PAIRS = ((0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2))
TIME_PAIRS = tuple((r, s) for r in range(4) for s in range(4)
                   if (r, s) != (0, 0))
OLD = "full-nodal-independent-trial-01/"
ORIGINAL_CONFIG = "7649e366ee0fba6c5a051f0eecb45fc387a8bf91bc4bd06befa7e444e409f047"
INPUT_PINS = {
    "node-trial-01/manifest.json": "5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd",
    "node-trial-01/modes.npy": "f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896",
    "node-trial-01/block-01280-01343.npz": "abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e",
    "kronecker-direct-independent-trial-01/centers-independent.i112le.bin": "c16d26dcbea14b63614d192da27a8b268fa49e689a02fb15499601cc1b611c9e",
    "full-nodal-independent-trial-01/residual-hat-fractions.i256-u256le.bin": "6054a0cbe5a3c91946b3d65acd38b32c720f8da575dbec0dddd79e6a49122ab5",
    "full-nodal-independent-trial-01/result.json": "e637e7fcde5f2fa8ac7cf55d635ada579f6fae189ebf903b6a7a018c351e393b",
    "full-nodal-independent-trial-01/run.json": "b197dc3cf405e191a7f4b7ca5076e7f04b2c812c22f6610e878972ff9957039e",
    "full-nodal-agreement.json": "f2ccad0d3a963e1a0bdbf0e9695e2979271807201ef3427964b2a11052511ed8",
}
SOURCE_PINS = {
    "ONE_SEGMENT_RESIDUAL_INDEPENDENT_EXECUTION_PREFLIGHT.md": "fd77dcc9ac5f1ed822d3d14cd1eb8ca33eb242d5f2322f862b170bbbdf6ce8ea",
    "ONE_SEGMENT_RESIDUAL_INDEPENDENT_CONTRACT_ROOT_REVIEW.md": "8244f7b4d2137c71c60f169b022d5cf238bebef50b00692a40d48cb32e00fb24",
    "one-segment-execution-contract-root-bindings.json": "32ac48b07a681b1e5aaa9e26532f8b7d19020ab198fffc587e7261c7e54bd527",
    "ONE_SEGMENT_RESIDUAL_INCREMENT_PREFLIGHT.md": "9934d16ec106aa99739f70cfa5d643840322f12766faf2f3f2b979f20ae46c61",
    "ONE_SEGMENT_RESIDUAL_INCREMENT_INDEPENDENT_REVIEW.md": "956d20ae6941bfce62cf2e35588bc5e775c09fd38a6c462c685bf2120642a784",
    "ONE_SEGMENT_RESIDUAL_DENOMINATOR_LEMMA.md": "de6b150813559e6d0856b3df8db77491c9a3da4cad1f07a3d94282cd29642104",
    "ONE_SEGMENT_RESIDUAL_DENOMINATOR_INDEPENDENT_DERIVATION.md": "a9d6b288917eb98123afce1bd0f07bf879e530b53701ad9eb9e00f4c5a099171",
    "C1_RESIDUAL_CONTRACT.md": "a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251",
    "FULL_NODAL_INDEPENDENT_EXECUTION_CONTRACT.md": "61450a286e2f300f4444a29b45fa53fe93ec1b655fab3b4f03afb4261e93307c",
    "FULL_NODAL_RESIDUAL_FINAL_REVIEW.md": "6d191cdb7be53601617754769b55b50be6346e5abfc2ca93083bf0518be7bc69",
    "full-nodal-final-review-record.json": "2c7be5ae420978d9fbddd39a503b0814558bbef971f4e9bedd9efec12704d713",
    "FULL_NODAL_INDEPENDENT_CODE_REVIEW.md": "f6185da959f93adcca2ad77de6f66fa52fb063d559023db9e09c10f8f43a56aa",
    "audit_full_nodal_residual_independent.py": "6b65b6f536d77c544c8803832eadcf37c72568f951a9982edf40e73dbc272fbf",
}
THREAD_KEYS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
               "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS")
CONFIG = {
    "schema": "one-segment-independent-direct-config-v1",
    "segment_nodes": [1280, 1281], "time_denominator": HINV, "viscosity": 1,
    "Q": str(Q), "QP": str(QP), "G": G, "H": J, "workers": 6,
    "tensor_labels": ["11", "12", "13", "22", "23", "33"],
    "time_pairs": TIME_PAIRS, "spatial_pairs_per_time_pair": G * G,
    "new_gaussian_products": 6 * 15 * G * G,
    "new_scalar_products": 24 * 15 * G * G,
    "direct_gaussian_scalar_products": 4, "zero_skipping": False,
    "old_C0_self_convolution_recomputed": False, "FFT": False,
    "packing": False, "polarization": False, "integration": False,
    "main_new_scientific_input": False, "q_vector": "numpy.object Python integers",
    "process_start": "os.fork; no helper processes or threads",
    "delta_shape_per_tensor": [6, J, 2], "delta_width": 31,
    "W_shape": [7, J, 3, 2], "W_width": 34,
    "S_shape": [13, J], "S_width": 68,
    "AH_C_shape": [4, G, 3, 2], "AH_C_width": 16,
    "rounding_fields": ["floor_signed16", "remainder_unsigned2"],
    "binary_bytes": 169192128, "order": "time-major; H kx-fastest; little-endian",
    "norm_and_bernstein": "exact Fraction; all 13 signed power coefficients",
    "root_bits": ROOT_BITS, "integer_guard_bits": MAX_BITS,
    "whole_segment": True, "verification_subdivision": False, "epsilon": None,
    "wall_seconds": WALL, "simultaneous_rss_and_sum_highwater_bytes": RSS_LIMIT,
    "output_bytes": FILE_LIMIT, "metadata_bytes": METADATA_LIMIT,
    "failure_reserve_bytes": FAILURE_RESERVE, "sample_seconds": SAMPLE_SECONDS,
    "progress_rows": PROGRESS_ROWS, "retry": False,
    "stdio_launcher_requirement": "root creates both logs with xb/noclobber; no truncation",
}


class Failure(Exception):
    pass


def need(ok, message):
    if not ok:
        raise Failure(message)


def utc():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def file_sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ib(x, bits=MAX_BITS):
    need(type(x) is int and abs(x).bit_length() <= bits, "INTEGER_BIT_GUARD")
    return x


def fq(x):
    ib(x.numerator)
    ib(x.denominator)
    return x


def fp(x):
    return [str(x.numerator), str(x.denominator)]


def read_fraction(x):
    need(isinstance(x, list) and len(x) == 2, "FRACTION_SCHEMA")
    n, d = int(x[0]), int(x[1])
    need(d > 0 and math.gcd(n, d) == 1, "FRACTION_REDUCED")
    return fq(Fraction(n, d))


def qadd(x, y):
    # GCD-first addition keeps the Bernstein lcm denominator within DI.6 bounds.
    g = math.gcd(x.denominator, y.denominator)
    a, b = x.denominator // g, y.denominator // g
    n = ib(ib(x.numerator * b) + ib(y.numerator * a))
    d = ib(x.denominator * b)
    return fq(Fraction(n, d))


def pins_check():
    for name, pin in {**INPUT_PINS, **SOURCE_PINS}.items():
        need(re.fullmatch("[0-9a-f]{64}", pin), "INVALID_PIN: " + name)
        need(file_sha(HERE / name) == pin, "INPUT_SHA_MISMATCH: " + name)


def json_save(name, obj):
    data = canonical(obj)
    need(len(data) < METADATA_LIMIT, "SINGLE_METADATA_LIMIT")
    path = OUT / name
    with path.open("wb") as f:
        f.write(data)
        f.flush()
    back = path.read_bytes()
    need(back == data and json.loads(back) == json.loads(data), "JSON_READBACK")
    return {"file": name, "bytes": len(back), "sha256": digest(back)}


def highwater():
    need(sys.platform == "darwin", "DARWIN_RESOURCE_UNITS_REQUIRED")
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def checkout():
    # Read the worktree HEAD without spawning an unaccounted git subprocess.
    marker = (ROOT / ".git").read_text().strip()
    need(marker.startswith("gitdir: "), "WORKTREE_GITDIR")
    gd = Path(marker[8:])
    if not gd.is_absolute():
        gd = ROOT / gd
    gd = gd.resolve()
    head = (gd / "HEAD").read_text().strip()
    ref = "refs/heads/codex/ns-reverse"
    need(head == "ref: " + ref, "WRONG_REVERSE_BRANCH")
    common = (gd / (gd / "commondir").read_text().strip()).resolve()
    direct = common / ref
    if direct.exists():
        commit = direct.read_text().strip()
    else:
        matches = [x.split()[0] for x in (common / "packed-refs").read_text().splitlines()
                   if not x.startswith(("#", "^")) and x.endswith(" " + ref)]
        need(len(matches) == 1, "PACKED_HEAD_REF")
        commit = matches[0]
    need(re.fullmatch("[0-9a-f]{40}", commit), "HEAD_COMMIT")
    return {"root": str(ROOT), "branch": "codex/ns-reverse", "commit": commit,
            "method": "read-only worktree HEAD and loose/packed branch ref"}


class TaskInfo(ctypes.Structure):
    # macOS sys/proc_info.h PROC_PIDTASKINFO=4, six uint64 and twelve int32.
    _fields_ = [(x, ctypes.c_uint64) for x in
                ("virtual", "resident", "total_user", "total_system",
                 "threads_user", "threads_system")] + [
                    (x, ctypes.c_int32) for x in
                    ("policy", "faults", "pageins", "cow", "sent", "received",
                     "mach", "unix", "switches", "threads", "running", "priority")]


class Resources:
    def __init__(self):
        need(sys.platform == "darwin" and ctypes.sizeof(TaskInfo) == 96,
             "NATIVE_RSS_LAYOUT")
        self.lib = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)
        self.lib.proc_pidinfo.argtypes = [ctypes.c_int, ctypes.c_int,
                                         ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int]
        self.lib.proc_pidinfo.restype = ctypes.c_int
        self.children = {}
        self.samples = []
        self.peak = 0
        self.stage = "CLAIM"
        self.last = 0.0
        self.parent_start = utc()
        self.fatal = None
        self.cleanup_errors = []
        self.fork_preflight = None

    def task(self, pid):
        v = TaskInfo()
        ret = self.lib.proc_pidinfo(pid, 4, 0, ctypes.byref(v), ctypes.sizeof(v))
        need(ret == ctypes.sizeof(v), "MISSING_NATIVE_RSS: " + str(pid))
        return v

    def reap(self):
        for pid, item in self.children.items():
            if item.get("wait4") is not None:
                continue
            got, status, usage = os.wait4(pid, os.WNOHANG)
            if got:
                item["wait4"] = {"status": status, "exit_code": os.waitstatus_to_exitcode(status),
                                 "highwater_bytes": int(usage.ru_maxrss),
                                 "finished_at": utc()}
                item["observed_highwater_bytes"] = max(
                    item["observed_highwater_bytes"], int(usage.ru_maxrss))
                if os.waitstatus_to_exitcode(status) != 0:
                    self.fatal = "WORKER_FAILED: " + item["tensor"]

    def file_bytes(self):
        return self.file_observation()["all_output_bytes"]

    def file_observation(self):
        seen, directory, metadata = set(), 0, 0
        for p in OUT.rglob("*"):
            if p.is_file():
                s = p.stat()
                seen.add((s.st_dev, s.st_ino))
                directory += s.st_size
                if p.suffix in (".json", ".jsonl"):
                    metadata += s.st_size
        external, descriptors = 0, {}
        for fd in (1, 2):
            s = os.fstat(fd)
            item = {"regular_file": stat.S_ISREG(s.st_mode), "bytes": s.st_size}
            if item["regular_file"]:
                path = fcntl.fcntl(fd, 50, b"\0" * 1024).split(b"\0", 1)[0]
                item["path"] = os.fsdecode(path)
                if (s.st_dev, s.st_ino) not in seen:
                    seen.add((s.st_dev, s.st_ino))
                    external += s.st_size
            descriptors[str(fd)] = item
        return {"directory_bytes": directory, "external_stdout_stderr_bytes": external,
                "metadata_and_external_log_bytes": metadata + external,
                "all_output_bytes": directory + external, "descriptors": descriptors}

    def sample(self, force=False, enforce=True):
        now = time.monotonic()
        if not force and now - self.last < SAMPLE_SECONDS:
            if enforce:
                need(now - START <= WALL, "WALL_BUDGET")
            return
        self.last = now
        self.reap()
        parent_current = int(self.task(os.getpid()).resident)
        current = {str(os.getpid()): parent_current}
        for pid, item in self.children.items():
            if item.get("wait4") is None:
                try:
                    rss = int(self.task(pid).resident)
                except Failure:
                    self.reap()
                    need(item.get("wait4") is not None, "LOST_LIVE_CHILD_RSS")
                    continue
                current[str(pid)] = rss
                item["observed_highwater_bytes"] = max(item["observed_highwater_bytes"], rss)
        total = sum(current.values())
        self.peak = max(self.peak, total)
        highsum = highwater() + sum(x["observed_highwater_bytes"]
                                    for x in self.children.values())
        sample = {"utc": utc(), "elapsed": now - START, "stage": self.stage,
                  "rss_bytes_by_pid": current, "simultaneous_rss_bytes": total,
                  "highwater_sum_so_far_bytes": highsum, "output_bytes": self.file_bytes()}
        self.samples.append(sample)
        with (OUT / "resources.jsonl").open("ab") as f:
            f.write(canonical(sample))
        if enforce:
            need(not self.fatal, self.fatal or "WORKER_FAILED")
            need(now - START <= WALL, "WALL_BUDGET")
            need(total <= RSS_LIMIT and highsum <= RSS_LIMIT, "RSS_BUDGET")
            need(self.file_bytes() <= FILE_LIMIT - FAILURE_RESERVE, "OUTPUT_BUDGET")
            need(self.file_observation()["metadata_and_external_log_bytes"] <= METADATA_LIMIT,
                 "METADATA_LOG_BUDGET")

    def finish_children(self, terminate=False):
        if terminate:
            # Cleanup must visit every child even if another PID operation fails.
            # Nonblocking wait4 sweeps avoid one unreapable PID stalling all others.
            errors = {}

            def error(pid, operation, exc):
                key = (pid, operation, type(exc).__name__, str(exc))
                if key in errors:
                    errors[key]["attempts"] += 1
                else:
                    entry = {"pid": pid, "operation": operation,
                             "error": type(exc).__name__ + ": " + str(exc),
                             "first_observed_at": utc(), "attempts": 1}
                    errors[key] = entry
                    self.cleanup_errors.append(entry)

            def sweep(operation):
                for pid, item in self.children.items():
                    if item.get("wait4") is not None:
                        continue
                    try:
                        got, status, usage = os.wait4(pid, os.WNOHANG)
                        if got:
                            item["wait4"] = {"status": status,
                                             "exit_code": os.waitstatus_to_exitcode(status),
                                             "highwater_bytes": int(usage.ru_maxrss),
                                             "finished_at": utc()}
                            item["observed_highwater_bytes"] = max(
                                item["observed_highwater_bytes"], int(usage.ru_maxrss))
                    except BaseException as exc:
                        error(pid, operation, exc)

            for pid, item in self.children.items():
                if item.get("wait4") is None:
                    try:
                        os.kill(pid, signal.SIGTERM)
                    except ProcessLookupError:
                        pass
                    except BaseException as exc:
                        error(pid, "TERM", exc)
            end = time.monotonic() + 2.0
            while time.monotonic() < end:
                sweep("TERM_GRACE_WAIT4")
                if all(x.get("wait4") is not None for x in self.children.values()):
                    break
                try:
                    time.sleep(0.02)
                except BaseException as exc:
                    error(0, "TERM_GRACE_SLEEP", exc)
            # Send KILL to every remaining PID before further wait attempts.
            for pid, item in self.children.items():
                if item.get("wait4") is None:
                    try:
                        os.kill(pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    except BaseException as exc:
                        error(pid, "KILL", exc)
            end = time.monotonic() + 2.0
            while time.monotonic() < end:
                sweep("POST_KILL_WAIT4")
                if all(x.get("wait4") is not None for x in self.children.values()):
                    break
                try:
                    time.sleep(0.02)
                except BaseException as exc:
                    error(0, "POST_KILL_SLEEP", exc)
            sweep("FINAL_WAIT4")
            for pid, item in self.children.items():
                if item.get("wait4") is None:
                    error(pid, "FINAL_UNREAPED", Failure("kernel exit/resource record unavailable"))
            need(not errors, "CLEANUP_ERRORS_AFTER_ALL_PID_ATTEMPTS")
        need(all(x.get("wait4") is not None for x in self.children.values()),
             "CHILD_RESOURCE_ACCOUNTING_INCOMPLETE")

    def report(self):
        return {"parent": {"pid": os.getpid(), "started_at": self.parent_start,
                           "highwater_bytes": highwater()},
                "children": {str(k): v for k, v in self.children.items()},
                "fork_preflight": self.fork_preflight,
                "cleanup_errors": self.cleanup_errors,
                "simultaneous_rss_peak_bytes": self.peak,
                "all_process_highwater_sum_bytes": highwater() + sum(
                    x["observed_highwater_bytes"] for x in self.children.values()),
                "sample_interval_seconds": SAMPLE_SECONDS, "samples": len(self.samples),
                "rss_source": "macOS proc_pidinfo TASKINFO resident bytes",
                "highwater_source": "parent getrusage SELF; every child wait4 ru_maxrss bytes",
                "elapsed_seconds": time.monotonic() - START,
                "output_bytes": self.file_bytes(), "output_observation": self.file_observation()}


def progress(mon, stage, **fields):
    mon.stage = stage
    with (OUT / "progress.jsonl").open("ab") as f:
        f.write(canonical({"utc": utc(), "elapsed": time.monotonic() - START,
                           "stage": stage, **fields}))
    mon.sample(force=True)


def serialize_array(name, array, width, strict_limit, heartbeat):
    raw = bytearray(array.size * width)
    for i, value in enumerate(array.flat):
        v = int(value)
        need(abs(v) < strict_limit, "SERIALIZED_INTEGER_PRIOR: " + name)
        raw[i * width:(i + 1) * width] = v.to_bytes(width, "little", signed=True)
        if i % 8192 == 0:
            heartbeat()
    path = OUT / name
    with path.open("xb") as f:
        f.write(raw)
    back = path.read_bytes()
    need(back == raw, "BINARY_BYTE_READBACK: " + name)
    for i, value in enumerate(array.flat):
        v = int.from_bytes(back[i * width:(i + 1) * width], "little", signed=True)
        need(v == int(value) and abs(v) < strict_limit, "BINARY_SCALAR_READBACK")
        if i % 8192 == 0:
            heartbeat()
    return {"file": name, "sha256": digest(back), "bytes": len(back),
            "shape": list(array.shape), "width": width, "signed": True,
            "all_scalars_read_back": True}


def load_original(np, mon, log):
    manifest = json.loads((HERE / "node-trial-01/manifest.json").read_bytes())
    need(manifest["schema"] == "reverse-fixed-seed-nodes-v1" and
         manifest["status"] == "CANDIDATE_NODES_COMPLETE_NOT_NS_CERTIFIED",
         "ORIGINAL_MANIFEST_STATUS")
    need(manifest["config_sha256"] == ORIGINAL_CONFIG, "ORIGINAL_CONFIG_PIN")
    for key, value in {"viscosity": 1, "scale": 1, "rho": 1, "cutoff": 8,
                       "time_denominator": HINV, "quantization_denominator": Q,
                       "G_count": G, "steps": 5120, "nodes": 5121}.items():
        need(manifest["config"][key] == value, "ORIGINAL_CONFIG_FIELD: " + key)
    modes_array = np.load(HERE / "node-trial-01/modes.npy", allow_pickle=False)
    md = manifest["modes"]
    need(modes_array.dtype.str == md["dtype"] == "<i8" and
         list(modes_array.shape) == md["shape"] == [G, 3], "MODE_SCHEMA")
    need(digest(modes_array.tobytes(order="C")) == md["array_sha256"], "MODE_ARRAY_SHA")
    modes = [tuple(int(x) for x in row) for row in modes_array]
    expected = [(x, y, z) for x in range(-8, 9) for y in range(-8, 9)
                for z in range(-8, 9) if (x, y, z) != (0, 0, 0)]
    need(modes == expected, "FULL_G_MODE_ORDER")
    descs = [b for b in manifest["blocks"] if b["file"] == "block-01280-01343.npz"]
    need(len(descs) == 1, "BLOCK_UNIQUE")
    desc = descs[0]
    need((desc["first_node"], desc["last_node"], desc["node_count"]) ==
         (1280, 1343, 64), "BLOCK_NODE_RANGE")
    rows, checks = {}, {}
    with np.load(HERE / "node-trial-01/block-01280-01343.npz", allow_pickle=False) as block:
        need(set(block.files) == set(desc["arrays"]), "BLOCK_FIELDS")
        for key in sorted(block.files):
            a, d = block[key], desc["arrays"][key]
            need(a.dtype.str == d["dtype"] == "<i8" and
                 list(a.shape) == d["shape"] and a.nbytes == d["nbytes"], "ARRAY_SCHEMA")
            sh = digest(a.tobytes(order="C"))
            need(sh == d["data_sha256"], "ORIGINAL_ARRAY_SHA")
            checks[key] = {"sha256": sh, "shape": list(a.shape), "bytes": a.nbytes}
            if key in ("value_q52", "slope_q52"):
                need(a.shape == (64, G, 3, 2), "VALUE_SLOPE_SHAPE")
                rows[key] = a[:2].copy()
            elif key in ("node_index", "time_numerator"):
                need([int(v) for v in a] == list(range(1280, 1344)), "NODE_SEQUENCE")
            elif key == "time_denominator":
                need(a.shape == (1,) and int(a[0]) == HINV, "TIME_DENOMINATOR")
            elif key == "quantization_denominator":
                need(a.shape == (1,) and int(a[0]) == Q, "DATA_DENOMINATOR")
            else:
                raise Failure("UNEXPECTED_ARRAY_FIELD")
            mon.sample()
    need(set(rows) == {"value_q52", "slope_q52"}, "ORIGINAL_ROWS")
    log["original_array_bindings"] = checks
    return modes, rows


def projected_row(raw, modes, neg):
    result = []
    for i, k in enumerate(modes):
        vals = [int(v) for v in raw[i].flat]
        other = [int(v) for v in raw[neg[i]].flat]
        need(all(abs(v) < 1 << 63 for v in vals + other), "RAW_Q52_STRICT_RANGE")
        y = [Fraction(vals[a] + (other[a] if a % 2 == 0 else -other[a]), 2 * Q)
             for a in range(6)]
        s = sum(v * v for v in k)
        dots = [sum(k[j] * y[2 * j + z] for j in range(3)) for z in range(2)]
        result.append([fq(y[a] - k[a // 2] * dots[a % 2] / s) for a in range(6)])
    return result


def constraints(field, modes, neg):
    for i, k in enumerate(modes):
        for z in range(2):
            need(sum(k[j] * field[i][2 * j + z] for j in range(3)) == 0,
                 "EXACT_TRANSVERSE")
        for a in range(6):
            need(field[neg[i]][a] == (field[i][a] if a % 2 == 0 else -field[i][a]),
                 "EXACT_REALITY")


def reconstruct(np, modes, rows, mon, log):
    index = {k: i for i, k in enumerate(modes)}
    neg = [index[tuple(-v for v in k)] for k in modes]
    endpoints = {}
    for key, raw in rows.items():
        endpoints[key] = []
        for n in range(2):
            f = projected_row(raw[n], modes, neg)
            constraints(f, modes, neg)
            endpoints[key].append(f)
            progress(mon, "PROJECTED_ORIGINAL_ENDPOINT", array=key, node=1280 + n)
    c0, c1 = endpoints["value_q52"]
    d0, d1 = endpoints["slope_q52"]
    a = [[[] for _ in range(G)] for _ in range(4)]
    AH = np.empty((4, G, 6), dtype=object)
    C = np.empty((4, G, 6), dtype=object)
    witness = bytearray(4 * G * 6 * 18)
    M, delta = [Fraction(0) for _ in range(4)], [Fraction(0) for _ in range(4)]
    oldC = (HERE / "kronecker-direct-independent-trial-01/centers-independent.i112le.bin").read_bytes()
    need(len(oldC) == G * 6 * 14, "OLD_C_LENGTH")
    for i, k in enumerate(modes):
        s = sum(v * v for v in k)
        for v in range(6):
            coeff = (c0[i][v], d0[i][v] / HINV,
                     3 * (c1[i][v] - c0[i][v]) - (2 * d0[i][v] + d1[i][v]) / HINV,
                     2 * (c0[i][v] - c1[i][v]) + (d0[i][v] + d1[i][v]) / HINV)
            need(sum(coeff) == c1[i][v] and HINV * coeff[1] == d0[i][v] and
                 HINV * sum(r * coeff[r] for r in range(1, 4)) == d1[i][v],
                 "HERMITE_ENDPOINTS_AND_PHYSICAL_SLOPES")
            for r in range(4):
                x = fq(coeff[r])
                a[r][i].append(x)
                n = fq(x * (1 << 64) * s)
                need(n.denominator == 1 and abs(n.numerator) < 1 << 88, "AH_INTEGER")
                AH[r, i, v] = n.numerator
                scaled = fq(x * QP)
                floor, rem = divmod(scaled.numerator, scaled.denominator)
                rounded = floor + int(2 * rem > scaled.denominator or
                                      (2 * rem == scaled.denominator and floor % 2 != 0))
                need(abs(rounded) < 1 << 112, "CENTER_PRIOR")
                C[r, i, v] = rounded
                q, rr = divmod(n.numerator << 32, s)
                need(q == floor and Fraction(rr, s) == Fraction(rem, scaled.denominator),
                     "ROUNDING_COMMON_WITNESS")
                pos = ((r * G + i) * 6 + v) * 18
                witness[pos:pos + 16] = q.to_bytes(16, "little", signed=True)
                witness[pos + 16:pos + 18] = rr.to_bytes(2, "little")
                M[r] = qadd(M[r], abs(x))
                delta[r] = qadd(delta[r], abs(x - Fraction(rounded, QP)))
                if r == 0:
                    pos0 = (i * 6 + v) * 14
                    need(rounded == int.from_bytes(oldC[pos0:pos0 + 14], "little", signed=True),
                         "OLD_C0_FULL_CONNECTION")
        if i % 128 == 0:
            mon.sample()
    for r in range(4):
        constraints(a[r], modes, neg)
    old = json.loads((HERE / OLD / "result.json").read_bytes())
    oldrun = json.loads((HERE / OLD / "run.json").read_bytes())
    agree = json.loads((HERE / "full-nodal-agreement.json").read_bytes())
    need(oldrun["status"] == "COMPLETE_FULL_NODAL_INDEPENDENT", "OLD_RUN_COMPLETE")
    need(agree["status"] == "PASS_FROZEN_FULL_NODAL_ARCHIVE_COMPARISON" and
         agree["independent_run_sha256"] == INPUT_PINS[OLD + "run.json"], "OLD_AGREEMENT")
    need(old["schema"] == "full-nodal-independent-fraction-result-v1" and
         old["node"] == 1280 and old["viscosity"] == 1, "OLD_RESULT_IDENTITY")
    for name in ("source_sha256", "input_sha256", "checkout", "config_sha256"):
        need(old[name] == oldrun[name], "OLD_RUN_RESULT_CONNECTION")
    for name, pin in INPUT_PINS.items():
        if name in old["input_sha256"]:
            need(old["input_sha256"][name] == pin, "OLD_SHARED_INPUT_CONNECTION: " + name)
    need(old["input_sha256"]["node-trial-01/manifest.json"] ==
         INPUT_PINS["node-trial-01/manifest.json"], "OLD_ORIGINAL_CONNECTION")
    need(old["source_sha256"]["audit_full_nodal_residual_independent.py"] ==
         SOURCE_PINS["audit_full_nodal_residual_independent.py"], "OLD_SOURCE_CONNECTION")
    outputs = {x["file"]: x for x in oldrun["output_files"]}
    for name in ("result.json", "residual-hat-fractions.i256-u256le.bin"):
        need(outputs[name]["sha256"] == INPUT_PINS[OLD + name], "OLD_OUTPUT_CONNECTION")
    need(M[0] == read_fraction(old["input_connection"]["M"]) and
         delta[0] == read_fraction(old["input_connection"]["delta"]), "OLD_M_DELTA_CONNECTION")
    Msum, dsum = sum(M), sum(delta)
    need(Msum < 1 << 32 and dsum < Fraction(1, 1 << 80), "INPUT_PERTURBATION_PRIOR")
    E = {j: fq(28 ** (j + 1) * (2 * Msum * dsum + dsum * dsum)) for j in (0, 2)}
    artifacts = [serialize_array("hermite-AH.i128le.bin", AH.reshape(4, G, 3, 2),
                                 16, 1 << 88, mon.sample),
                 serialize_array("centers-c96.i128le.bin", C.reshape(4, G, 3, 2),
                                 16, 1 << 112, mon.sample)]
    path = OUT / "rounding-floor-rem.i128-u16le.bin"
    with path.open("xb") as f:
        f.write(witness)
    back = path.read_bytes()
    need(back == witness, "ROUND_WITNESS_BYTES")
    for r in range(4):
        for i, k in enumerate(modes):
            s = sum(v * v for v in k)
            for v in range(6):
                pos = ((r * G + i) * 6 + v) * 18
                q = int.from_bytes(back[pos:pos + 16], "little", signed=True)
                rr = int.from_bytes(back[pos + 16:pos + 18], "little")
                need(0 <= rr < s and (int(AH[r, i, v]) << 32) == q * s + rr,
                     "ROUND_WITNESS_READBACK")
                need(int(C[r, i, v]) == q + int(2 * rr > s or (2 * rr == s and q % 2)),
                     "ROUND_EVEN_READBACK")
            if i % 256 == 0:
                mon.sample()
    artifacts.append({"file": path.name, "bytes": len(back), "sha256": digest(back),
                      "all_117888_rounding_witnesses_read_back": True})
    log["input_connection"] = {"M": [fp(x) for x in M], "delta": [fp(x) for x in delta],
                               "M_sum": fp(Msum), "delta_sum": fp(dsum),
                               "E": {str(j): fp(E[j]) for j in E},
                               "old_C0_scalar_matches": G * 6,
                               "old_M0_delta0_equal": True, "old_rho_source": OLD}
    return a, C, E, artifacts, old


def worker(np, modes, C, pair):
    signal.signal(signal.SIGALRM, signal.SIG_DFL)
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    signal.setitimer(signal.ITIMER_REAL, 0)
    label = "".join(str(v + 1) for v in pair)
    start, rows_done = utc(), 0
    record = {"tensor": label, "pid": os.getpid(), "started_at": start, "status": "RUNNING"}

    def beat():
        need(time.monotonic() - START <= WALL, "WORKER_WALL")
        need(highwater() <= RSS_LIMIT, "WORKER_RSS")

    try:
        j, l = pair
        out = np.zeros((6, J, 2), dtype=object)
        positions = np.array([(k[0] + 8) + 33 * (k[1] + 8) + 1089 * (k[2] + 8)
                              for k in modes], dtype=np.int64)
        need(len(set(int(x) for x in positions)) == G, "INJECTIVE_Q_POSITIONS")
        for ip in range(G):
            targets = positions + positions[ip]
            for r, s in TIME_PAIRS:
                # Every q, including exact zeros, is multiplied. No G x G matrix.
                x, y = int(C[r, ip, 2 * j]), int(C[r, ip, 2 * j + 1])
                u, v = C[s, :, 2 * l], C[s, :, 2 * l + 1]
                out[r + s - 1, targets, 0] += x * u - y * v
                out[r + s - 1, targets, 1] += x * v + y * u
            rows_done = ip + 1
            beat()
            if rows_done % PROGRESS_ROWS == 0 or rows_done == G:
                with (OUT / ("worker-" + label + ".jsonl")).open("ab") as f:
                    f.write(canonical({"utc": utc(), "rows": rows_done,
                                       "gaussian_products": rows_done * G * 15,
                                       "elapsed": time.monotonic() - START,
                                       "highwater_bytes": highwater()}))
        artifact = serialize_array("delta-T" + label + ".i248le.bin", out,
                                   31, 1 << 245, beat)
        # Read the actual saved bytes for full conjugate checks; no new convolution.
        raw = (OUT / artifact["file"]).read_bytes()
        for m in range(6):
            for k in range(J):
                opposite = J - 1 - k
                vals = []
                for idx in (k, opposite):
                    off = ((m * J + idx) * 2) * 31
                    vals.append((int.from_bytes(raw[off:off + 31], "little", signed=True),
                                 int.from_bytes(raw[off + 31:off + 62], "little", signed=True)))
                need(vals[0][0] == vals[1][0] and vals[0][1] == -vals[1][1],
                     "DELTA_FULL_CONJUGATE")
            beat()
        record.update(status="COMPLETE_DIRECT_INCREMENT_TENSOR", artifact=artifact,
                      gaussian_products=15 * G * G, scalar_products=60 * G * G)
    except BaseException as e:
        record.update(status="FAILED", error=type(e).__name__ + ": " + str(e),
                      traceback=traceback.format_exc())
    record.update(finished_at=utc(), rows_completed=rows_done,
                  highwater_bytes=highwater(), elapsed=time.monotonic() - START)
    json_save("worker-" + label + "-result.json", record)
    os._exit(0 if record["status"] == "COMPLETE_DIRECT_INCREMENT_TENSOR" else 1)


def run_workers(np, modes, C, mon):
    python_threads = threading.active_count()
    native_threads = int(mon.task(os.getpid()).threads)
    mon.fork_preflight = {"utc": utc(), "pid": os.getpid(),
                         "python_active_count": python_threads,
                         "native_task_threadnum": native_threads}
    need(python_threads == 1 and native_threads == 1,
         "FORK_REQUIRES_SINGLE_NATIVE_THREAD")
    for pair in PAIRS:
        label = "".join(str(x + 1) for x in pair)
        blocked = signal.pthread_sigmask(signal.SIG_BLOCK,
                                         {signal.SIGALRM, signal.SIGTERM, signal.SIGINT})
        try:
            pid = os.fork()
            if pid == 0:
                # A child can never fall through into the supervisor's exception handler.
                try:
                    signal.pthread_sigmask(signal.SIG_SETMASK, blocked)
                    worker(np, modes, C, pair)
                except BaseException:
                    os._exit(3)
                finally:
                    os._exit(2)
            mon.children[pid] = {"tensor": label, "started_at": utc(), "wait4": None,
                                 "observed_highwater_bytes": 0}
        finally:
            signal.pthread_sigmask(signal.SIG_SETMASK, blocked)
    progress(mon, "SIX_DIRECT_WORKERS_RUNNING")
    while any(x["wait4"] is None for x in mon.children.values()):
        mon.sample(force=True)
        time.sleep(SAMPLE_SECONDS)
    mon.finish_children()
    artifacts = []
    for pid, item in mon.children.items():
        path = OUT / ("worker-" + item["tensor"] + "-result.json")
        d = json.loads(path.read_bytes())
        need(d["status"] == "COMPLETE_DIRECT_INCREMENT_TENSOR" and d["pid"] == pid,
             "WORKER_FINAL_RECORD")
        need(d["gaussian_products"] == 15 * G * G and d["rows_completed"] == G,
             "WORKER_PAIR_COUNT")
        need(0 < d["highwater_bytes"] <= item["wait4"]["highwater_bytes"],
             "WORKER_HIGHWATER_CONNECTION")
        item["worker_reported_highwater_bytes"] = d["highwater_bytes"]
        item["worker_report_sha256"] = digest(path.read_bytes())
        rec = d["artifact"]
        need(rec["bytes"] == 6 * J * 2 * 31 and file_sha(OUT / rec["file"]) == rec["sha256"],
             "WORKER_ARTIFACT_CONNECTION")
        artifacts.append(rec)
    progress(mon, "ALL_DIRECT_TENSORS_COMPLETE")
    return artifacts


def k_at(i):
    return (i % 33 - 16, (i // 33) % 33 - 16, i // 1089 - 16)


def signed_at(raw, pos, width):
    return int.from_bytes(raw[pos:pos + width], "little", signed=True)


def build_W(modes, a, mon):
    arrays = {}
    for pair in PAIRS:
        label = "".join(str(x + 1) for x in pair)
        raw = (OUT / ("delta-T" + label + ".i248le.bin")).read_bytes()
        need(len(raw) == 6 * J * 2 * 31, "DELTA_FILE_SIZE")
        arrays[pair] = raw
    old = (HERE / OLD / "residual-hat-fractions.i256-u256le.bin").read_bytes()
    need(len(old) == J * 6 * 64, "OLD_RHO_SIZE")
    mapping = {k: i for i, k in enumerate(modes)}
    target = OUT / "W.i272le.bin"
    rawW = bytearray(7 * J * 6 * 34)
    for ik in range(J):
        k = k_at(ik)
        s = sum(v * v for v in k)
        for m in range(7):
            if m == 0:
                rho = []
                for v in range(6):
                    off = (ik * 6 + v) * 64
                    n = signed_at(old, off, 32)
                    d = int.from_bytes(old[off + 32:off + 64], "little")
                    need(d > 0 and math.gcd(n, d) == 1, "OLD_RHO_REDUCED")
                    rho.append(Fraction(n, d))
            elif s == 0:
                rho = [Fraction(0)] * 6
            else:
                F = [0] * 6
                for j in range(3):
                    for l in range(3):
                        pair = (min(j, l), max(j, l))
                        off = (((m - 1) * J + ik) * 2) * 31
                        F[2 * l] += k[j] * signed_at(arrays[pair], off, 31)
                        F[2 * l + 1] += k[j] * signed_at(arrays[pair], off + 31, 31)
                dots = [sum(k[j] * F[2 * j + z] for j in range(3)) for z in range(2)]
                PF = [fq(Fraction(F[v]) - Fraction(k[v // 2] * dots[v % 2], s))
                      for v in range(6)]
                lin = [Fraction(0)] * 6
                if k in mapping:
                    ii = mapping[k]
                    for v in range(6):
                        lin[v] = fq((HINV * (m + 1) * a[m + 1][ii][v] if m < 3 else 0) +
                                    (s * a[m][ii][v] if m <= 3 else 0))
                rho = [fq(lin[v] + (PF[v - 1] if v % 2 else -PF[v + 1]) / (QP * QP))
                       for v in range(6)]
            for v, x in enumerate(rho):
                if not s:
                    need(x == 0, "RHO_ZERO_MODE")
                    w = 0
                else:
                    scaled = fq(x * s * QP * QP)
                    need(scaled.denominator == 1, "LOCAL_DENOMINATOR_CANCEL")
                    w = scaled.numerator
                need(abs(w) < 1 << 263, "W_PRIOR")
                off = ((m * J + ik) * 6 + v) * 34
                rawW[off:off + 34] = w.to_bytes(34, "little", signed=True)
        if ik % 128 == 0:
            mon.sample()
    with target.open("xb") as f:
        f.write(rawW)
    back = target.read_bytes()
    need(back == rawW, "W_BYTE_READBACK")
    for m in range(7):
        for ik in range(J):
            k, opposite = k_at(ik), J - 1 - ik
            vals = [signed_at(back, ((m * J + ik) * 6 + v) * 34, 34) for v in range(6)]
            other = [signed_at(back, ((m * J + opposite) * 6 + v) * 34, 34) for v in range(6)]
            need(all(abs(x) < 1 << 263 for x in vals), "W_READBACK_PRIOR")
            need(all(other[v] == (vals[v] if v % 2 == 0 else -vals[v]) for v in range(6)),
                 "W_FULL_CONJUGATE")
            need(all(sum(k[j] * vals[2 * j + z] for j in range(3)) == 0 for z in range(2)),
                 "W_FULL_TRANSVERSE")
            if ik == (J - 1) // 2:
                need(vals == [0] * 6, "W_ZERO_MODE")
            if m == 0 and ik != (J - 1) // 2:
                s = sum(x * x for x in k)
                for v in range(6):
                    off = (ik * 6 + v) * 64
                    n, d = signed_at(old, off, 32), int.from_bytes(old[off + 32:off + 64], "little")
                    need(Fraction(vals[v], s * QP * QP) == Fraction(n, d), "W0_OLD_RHO_READBACK")
            if ik % 256 == 0:
                mon.sample()
    progress(mon, "FULL_W_READ_BACK")
    return {"file": target.name, "bytes": len(back), "sha256": digest(back),
            "shape": [7, J, 3, 2], "width": 34, "all_scalars_read_back": True,
            "old_constant_connected": True, "complete_reality_transverse_zero": True}


def norm_polynomials(mon, old_result):
    W = (OUT / "W.i272le.bin").read_bytes()
    need(len(W) == 7 * J * 6 * 34, "W_NORM_SIZE")
    S = bytearray(13 * J * 68)
    q = {j: [Fraction(0) for _ in range(13)] for j in (0, 2)}
    products = 0
    for ik in range(J):
        w = [[signed_at(W, ((r * J + ik) * 6 + v) * 34, 34) for v in range(6)]
             for r in range(7)]
        coeff = [0] * 13
        for v in range(6):
            for r in range(7):
                for s in range(7):
                    coeff[r + s] += w[r][v] * w[s][v]
                    products += 1
        for m, value in enumerate(coeff):
            need(abs(value) < 1 << 532, "SIGNED_S_PRIOR")
            off = (m * J + ik) * 68
            S[off:off + 68] = value.to_bytes(68, "little", signed=True)
        if ik % 128 == 0:
            mon.sample()
    need(products == J * 6 * 49, "FULL_S_TIME_PAIR_COUNT")
    path = OUT / "S.i544le.bin"
    with path.open("xb") as f:
        f.write(S)
    back = path.read_bytes()
    need(back == S, "S_BYTE_READBACK")
    # Norms are accumulated from all decoded, signed stored S coefficients.
    for ik in range(J):
        s = sum(v * v for v in k_at(ik))
        for m in range(13):
            off = (m * J + ik) * 68
            v = signed_at(back, off, 68)
            need(abs(v) < 1 << 532, "S_READBACK_PRIOR")
            other = signed_at(back, (m * J + J - 1 - ik) * 68, 68)
            need(v == other, "S_CONJUGATE_MODE_EQUAL")
            if s == 0:
                need(v == 0, "S_ZERO_MODE")
            else:
                q[0][m] = qadd(q[0][m], Fraction(v, s * s * (1 << 384)))
                q[2][m] = qadd(q[2][m], Fraction(v, 1 << 384))
        if ik % 128 == 0:
            mon.sample()
    for j in (0, 2):
        need(q[j][0] == read_fraction(old_result["norm_square"][str(j)]),
             "OLD_EXACT_NORM_CONSTANT_CONNECTION")
    b = {}
    for j in (0, 2):
        b[j] = []
        for m in range(13):
            total = Fraction(0)
            for l in range(m + 1):
                total = qadd(total, fq(q[j][l] * Fraction(math.comb(m, l), math.comb(12, l))))
            b[j].append(total)
        need(max(b[j]) >= 0, "IMPOSSIBLE_NEGATIVE_SQUARE_BERNSTEIN")
    progress(mon, "EXACT_FRACTION_POLYNOMIALS_COMPLETE")
    artifact = {"file": path.name, "bytes": len(back), "sha256": digest(back),
                "shape": [13, J], "width": 68, "all_signed_coefficients_read_back": True}
    return q, b, artifact, products


def sqrt_interval(value):
    need(value >= 0, "ROOT_NONNEGATIVE")
    A, D = value.numerator, value.denominator
    scaled = ib(A << (2 * ROOT_BITS))
    z = math.isqrt(scaled // D)
    left, right = ib(z * z * D), ib((z + 1) * (z + 1) * D)
    need(left <= scaled < right, "ROOT_RATIONAL_BRACKET")
    exact = left == scaled
    upper = z if exact else z + 1
    return {"input": fp(value), "bits": ROOT_BITS, "scaled_numerator": str(scaled),
            "denominator": str(D), "floor_root": str(z), "ceil_root": str(upper),
            "true_rational_equality": exact,
            "lower": fp(Fraction(z, 1 << ROOT_BITS)),
            "upper": fp(Fraction(upper, 1 << ROOT_BITS))}


def scientific(np, mon, log):
    progress(mon, "ORIGINAL_ARRAY_LOAD")
    modes, rows = load_original(np, mon, log)
    a, C, E, artifacts, old = reconstruct(np, modes, rows, mon, log)
    del rows
    progress(mon, "EXACT_HERMITE_AND_CENTERS_COMPLETE")
    artifacts += run_workers(np, modes, C, mon)
    artifacts.append(build_W(modes, a, mon))
    q, b, rec, products = norm_polynomials(mon, old)
    artifacts.append(rec)
    bounds = {}
    for j in (0, 2):
        B = max(Fraction(0), *b[j])
        root = sqrt_interval(B)
        bounds[str(j)] = {"power_coefficients": [fp(x) for x in q[j]],
                          "bernstein_coefficients": [fp(x) for x in b[j]],
                          "maximum": fp(B), "root": root, "E": fp(E[j]),
                          "original_segment_upper": fp(qadd(read_fraction(root["upper"]), E[j])),
                          "root_lower_is_original_residual_lower": False}
    need(sum(x["bytes"] for x in artifacts) == CONFIG["binary_bytes"], "TOTAL_BINARY_LAYOUT")
    for x in artifacts:
        need(file_sha(OUT / x["file"]) == x["sha256"], "FINAL_SCIENTIFIC_ARTIFACT_SHA")
        mon.sample()
    result = {"schema": "one-segment-independent-direct-result-v1",
              "scope": "ONLY_FIXED_REFERENCE_COMPLETE_RESIDUAL_ON_I; NO_NS_CONCLUSION",
              "segment_nodes": [1280, 1281], "time_denominator": HINV,
              "new_gaussian_products": CONFIG["new_gaussian_products"],
              "new_scalar_products": CONFIG["new_scalar_products"],
              "squared_norm_integer_products": products, "bounds": bounds,
              "input_connection": log["input_connection"], "artifacts": artifacts,
              "source_sha256": log["source_sha256"], "input_sha256": INPUT_PINS,
              "config_sha256": log["config_sha256"], "checkout": log["checkout"],
              "primary_comparison": "NOT_PERFORMED", "epsilon_or_gamma": None}
    result_rec = json_save("result.json", result)
    log["artifacts"] = artifacts + [result_rec]
    progress(mon, "RESULT_SAVED_AND_READ_BACK")


def alarm_handler(signum, frame):
    raise Failure("SUPERVISOR_SIGNAL: " + str(signum))


def final_receipt(mon, run_sha):
    # Last flush/readback receipt observes stdout and all scientific/metadata logs.
    # No fsync or power-loss durability is claimed.
    # Account for this receipt's own exact size by a bounded size fixed point.
    observation = mon.report()
    parent_high = observation["parent"]["highwater_bytes"]
    base = observation["output_bytes"]
    record = {"schema": "one-segment-independent-final-receipt-v1",
              "status": "COMPLETE_FINAL_ACCOUNTING",
              "run_sha256": run_sha, "observed_after_stdout_flush": observation,
              "acceptance_also_requires": "matching run SHA, stdout connection and process exit 0",
              "persistence_scope": "flush/readback only; no power-loss durability claim",
              "receipt_bytes": 0, "all_output_bytes_including_receipt": base}
    for _ in range(8):
        size = len(canonical(record))
        if record["receipt_bytes"] == size:
            break
        record["receipt_bytes"] = size
        record["all_output_bytes_including_receipt"] = base + size
    data = canonical(record)
    need(len(data) == record["receipt_bytes"], "RECEIPT_SIZE_FIXED_POINT")
    need(base + len(data) <= FILE_LIMIT - FAILURE_RESERVE, "RECEIPT_OUTPUT_BUDGET")
    path = OUT / "final-receipt.json"
    with path.open("xb") as f:
        f.write(data)
        f.flush()
    need(path.read_bytes() == data, "FINAL_RECEIPT_READBACK")
    after = mon.report()
    need(after["output_bytes"] == record["all_output_bytes_including_receipt"],
         "FINAL_ALL_OUTPUT_OBSERVATION")
    need(after["parent"]["highwater_bytes"] == parent_high, "LATE_PARENT_HIGHWATER_CHANGE")
    need(after["all_process_highwater_sum_bytes"] <= RSS_LIMIT and
         after["simultaneous_rss_peak_bytes"] <= RSS_LIMIT and
         after["elapsed_seconds"] <= WALL and
         after["output_observation"]["metadata_and_external_log_bytes"] <= METADATA_LIMIT,
         "POST_RECEIPT_BUDGET")


def main():
    p = argparse.ArgumentParser(
        epilog="--run requires root-created exclusive xb/noclobber stdout/stderr logs. "
               "Regular/empty descriptor checks do not prove exclusive creation.")
    group = p.add_mutually_exclusive_group()
    group.add_argument("--run", action="store_true")
    group.add_argument("--check-only", action="store_true")
    p.add_argument("--code-review-file")
    p.add_argument("--code-review-sha256")
    args = p.parse_args()
    need(ROOT == TREE and Path.cwd().resolve().is_relative_to(ROOT), "REVERSE_TREE_ONLY")
    own = Path(__file__).read_bytes()
    own.decode("ascii")
    ast.parse(own.decode("ascii"), filename=str(__file__))
    need(sys.version_info >= (3, 10) and sys.flags.optimize == 0, "PYTHON_VERSION_OPTIMIZE")
    need(len(TIME_PAIRS) == 15 and CONFIG["new_gaussian_products"] == 2171496960 and
         CONFIG["new_scalar_products"] == 8685987840, "FIXED_CONFIG_COUNTS")
    own_sha, config_sha = digest(own), digest(canonical(CONFIG))
    if not args.run:
        pins_check()
        print(canonical({"status": "STATIC_PREFLIGHT_PASS_NOT_RUN",
                         "scientific_execution": False, "source_sha256": own_sha,
                         "config_sha256": config_sha, "pins": len(INPUT_PINS) + len(SOURCE_PINS),
                         "output_directory_exists": OUT.exists(),
                         "checks": ["ASCII", "AST", "fixed config", "actual SHA"]}).decode(), end="")
        return 0
    need(args.code_review_file and args.code_review_sha256, "ROOT_CODE_REVIEW_REQUIRED")
    review = Path(args.code_review_file).resolve()
    need(review.parent == HERE and review.suffix == ".md", "LOCAL_CODE_REVIEW_REQUIRED")
    need(re.fullmatch("[0-9a-f]{64}", args.code_review_sha256), "REVIEW_PIN_FORMAT")
    need(file_sha(review) == args.code_review_sha256, "ROOT_REVIEW_BYTE_PIN")
    rt = review.read_text()
    need(own_sha in rt and SOURCE_PINS["ONE_SEGMENT_RESIDUAL_INDEPENDENT_EXECUTION_PREFLIGHT.md"] in rt
         and "PASS" in rt, "ROOT_REVIEW_MUST_BIND_SOURCE_AND_CONTRACT")
    OUT.mkdir(exist_ok=False)
    log = {"schema": "one-segment-independent-direct-run-v1", "status": "CLAIMED_NOT_COMPLETE",
           "started_at": utc(), "command_argv": sys.argv, "working_directory": str(Path.cwd()),
           "source_sha256": {**SOURCE_PINS, Path(__file__).name: own_sha,
                             review.name: args.code_review_sha256},
           "input_sha256": INPUT_PINS, "config": CONFIG, "config_sha256": config_sha,
           "pid": os.getpid(), "stage": "CLAIM"}
    mon = None
    exit_code = 1
    try:
        json_save("claim.json", log)
        need(sys.platform == "darwin", "MACOS_ONLY_NATIVE_RESOURCES")
        need(all(stat.S_ISREG(os.fstat(fd).st_mode) for fd in (1, 2)),
             "RUN_REQUIRES_REGULAR_STDOUT_STDERR_LOG_FILES")
        need(all(os.fstat(fd).st_size == 0 for fd in (1, 2)),
             "RUN_REQUIRES_NEW_EMPTY_EXCLUSIVE_STDIO_LOGS")
        need(all(os.environ.get(k) == "1" for k in THREAD_KEYS), "SINGLE_THREAD_ENV_REQUIRED")
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.signal(signal.SIGTERM, alarm_handler)
        signal.setitimer(signal.ITIMER_REAL, max(0.001, WALL - (time.monotonic() - START)))
        mon = Resources()
        progress(mon, "FILE_BINDINGS")
        pins_check()
        log["checkout"] = checkout()
        need(file_sha(Path(__file__)) == own_sha, "SOURCE_CHANGED")
        import numpy as np
        log["environment"] = {"python": sys.version, "executable": sys.executable,
                              "numpy": np.__version__, "platform": platform.platform(),
                              "uname": list(platform.uname()), "logical_cpus": os.cpu_count(),
                              "thread_env": {k: os.environ[k] for k in THREAD_KEYS},
                              "arithmetic": "Python int + Fraction; NumPy object direct q vectors"}
        scientific(np, mon, log)
        mon.finish_children()
        pins_check()
        need(file_sha(Path(__file__)) == own_sha and checkout() == log["checkout"],
             "FINAL_SOURCE_OR_CHECKOUT_CHANGED")
        need(file_sha(review) == args.code_review_sha256, "FINAL_ROOT_REVIEW_SHA_CHANGED")
        mon.sample(force=True)
        log["status"] = "COMPLETE_FIXED_SEGMENT_INDEPENDENT_RESIDUAL"
        log["finished_at"] = utc()
        log["resources"] = mon.report()
        json_save("run.json", log)
        mon.sample(force=True)
        report = mon.report()
        need(report["all_process_highwater_sum_bytes"] <= RSS_LIMIT and
             report["simultaneous_rss_peak_bytes"] <= RSS_LIMIT, "FINAL_RESOURCE_BUDGET")
        log["post_write_observation"] = report
        json_save("run.json", log)
        mon.sample(force=True)
        final = mon.report()
        need(final["output_bytes"] <= FILE_LIMIT - FAILURE_RESERVE and
             final["elapsed_seconds"] <= WALL and
             final["all_process_highwater_sum_bytes"] <= RSS_LIMIT, "FINAL_BUDGET")
        run_sha = file_sha(OUT / "run.json")
        print(canonical({"run": str(OUT / "run.json"), "sha256": run_sha,
                         "status": log["status"], "before_stdout_observation": final,
                         "acceptance_also_requires": "final-receipt.json and process exit 0"}).decode(),
              end="", flush=True)
        mon.sample(force=True)
        final_receipt(mon, run_sha)
        signal.setitimer(signal.ITIMER_REAL, 0)
        exit_code = 0
    except BaseException as e:
        signal.setitimer(signal.ITIMER_REAL, 0)
        log.update(status="FAILED_COST_NOT_PAID", error=type(e).__name__ + ": " + str(e),
                   traceback=traceback.format_exc(), failed_at=utc(),
                   stage=mon.stage if mon else "STARTUP_BEFORE_RESOURCES")
        if mon:
            try:
                mon.finish_children(terminate=True)
            except BaseException as cleanup_error:
                log["resource_accounting_incomplete"] = str(cleanup_error)
            # Preserve all per-PID observations even when cleanup reports errors.
            log["cleanup_errors"] = mon.cleanup_errors
            log["child_accounts_after_cleanup"] = {str(k): v for k, v in mon.children.items()}
            try:
                mon.sample(force=True, enforce=False)
            except BaseException as sample_error:
                log["failure_resource_sample_error"] = str(sample_error)
            try:
                log["resources"] = mon.report()
            except BaseException as resource_error:
                log["failure_resource_report_error"] = str(resource_error)
        json_save("run.json", log)
        print(canonical({"run": str(OUT / "run.json"), "sha256": file_sha(OUT / "run.json"),
                         "status": log["status"], "error": log["error"]}).decode(), end="", flush=True)
    return exit_code


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BaseException as exc:
        if isinstance(exc, SystemExit):
            raise
        print(canonical({"status": "STARTUP_REJECTED_NOT_RUN",
                         "error": type(exc).__name__ + ": " + str(exc)}).decode(), end="", file=sys.stderr)
        sys.exit(1)
