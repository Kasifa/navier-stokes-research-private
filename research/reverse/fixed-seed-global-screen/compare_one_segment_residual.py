#!/usr/bin/env python3
"""Data-only full comparison of two frozen, fixed Hermite-segment archives.

Default and --check-only perform syntax/configuration/byte-pin checks only.
No producer, spatial convolution, Fourier solver or scientific kernel is imported.
The independent final pins and resource lock must exist before --run is admitted.
"""
import time
START = time.monotonic()

import argparse
import ast
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import resource
import shlex
import signal
import stat
import struct
import sys
import traceback

HERE = Path(__file__).resolve().parent
TREE = HERE.parents[2]
PRIMARY = HERE / "one-segment-residual-trial-01"
INDEPENDENT = HERE / "one-segment-residual-independent-trial-01"
OUT = HERE / "one-segment-residual-comparison-trial-01"
STDOUT = HERE / "one-segment-residual-comparison.stdout.log"
STDERR = HERE / "one-segment-residual-comparison.stderr.log"
G, H, QP, P = 4912, 35937, 1 << 96, 1 << 128
LABELS = ("11", "12", "13", "22", "23", "33")
CONTRACT = "ONE_SEGMENT_RESIDUAL_COMPARISON_CONTRACT.md"
FIXED_PINS = {
    CONTRACT: "e6a39b644953609429d5d2560dad500026f2db31dca6f40bd52dfe47bccc86db",
    "ONE_SEGMENT_RESIDUAL_COMPARISON_INDEPENDENT_REVIEW.md": "76be831347a8dcd4e4cf16721ad695497e88ab98d8a4c19f4a2fe91a20a6ac4e",
    "audit_one_segment_residual.py": "f8f871684d68303de24a8901abb35266969d2f978d218ca9d14cd16ce45fac63",
    "ONE_SEGMENT_RESIDUAL_PRIMARY_ROOT_SOURCE_REVIEW.md": "3f135b81485b55189da141dedc9af10aab10bc23a9ebfad0433660a1b390328a",
    "ONE_SEGMENT_RESIDUAL_PRIMARY_SYSTEM_REVIEW.md": "349d47827bb6411862e3740a865a05207fa364d87634c95ed0a519a4e53bcdcf",
    "one-segment-primary-root-execution-acceptance.json": "c4c8ea70c33918ddea1d7cce74b89e7e97e99ff9be7aa3f74e73e3633562770b",
    "one-segment-residual-trial-01/run.json": "869be6550d833d7021b130915c0ecb69e22545d8c4c03f4e99c790f15ba6a500",
    "one-segment-residual-trial-01/result.json": "85eed24be3ce08d92761d6a5a4eab22eff046d1ad2b0c26ca89a817a0ab5baf8",
    "one-segment-residual-primary.stdout.log": "4093d5723c69f46dfbd40f89cfd27d92c43f13fe85704c9a6c0bb0dcd33a1dbb",
    "one-segment-residual-primary.stderr.log": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
}
# Filled only after the root reported the actual unique independent run/exit.
INDEPENDENT_FINAL_PINS = {
    "audit_one_segment_residual_independent.py": "1e9c9ee576049bd444ed07e858175b113bdb09d3719f1ab69820a3536564ca79",
    "one-segment-residual-independent-trial-01/run.json": "85ef60b89269eb2aacde9d054ef7eb055b22495e8cc3e6662094b14d557fc082",
    "one-segment-residual-independent-trial-01/result.json": "08db4607d178a5d69bbec053eeb21563f00dcc9d75faeddb91ff74d47616c9b9",
    "one-segment-residual-independent-trial-01/final-receipt.json": "7066e7c7499e5b57a392eb2408a0a0f63315cb4dcbd77db8a54154ef2353d1a9",
    "one-segment-independent-root-execution-acceptance.json": "5265d2ebe8a3af7bd822ecdcef2f68a6e20a567f4d84135af2ccabd10f154c49",
    "ONE_SEGMENT_RESIDUAL_INDEPENDENT_ROOT_SOURCE_REVIEW.md": "4b88d9e462d3a63deda294ce50e66427a2eb951e909a80206b1e0f4e9f44c36b",
    "ONE_SEGMENT_RESIDUAL_INDEPENDENT_SYSTEM_REVIEW.md": "4130f8232b7282dbfd4168ea71d1ea666e563b99a6348f2dac10fd4e1d1e687a",
    "one-segment-residual-independent.stdout.log": "2041297784132306beaa216b490a430159a4f83cf02ebacc74b42f6a94fdf7ea",
    "one-segment-residual-independent.stderr.log": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
}
INDEPENDENT_ACCEPTANCE = "one-segment-independent-root-execution-acceptance.json"
# One fixed engineering stop gate; no measured-runtime guarantee or retry.
RESOURCE_LOCK = {"wall_seconds": 120, "rss_bytes": 256*1024**2, "output_bytes": 8*1024**2}
# The producers used implicit platform helpers absent from their own accounting.
# The actual scope supplement, independent review and audit are all pinned.
# This admits only the limited arithmetic comparison, never producer cost closure.
ARITHMETIC_ONLY_SUPPLEMENT_PINS = {
    "ONE_SEGMENT_COMPARISON_RESOURCE_GAP_ADDENDUM.md": "212df48b07648511024524ab746d41ec3e419914cb111862ae3569663ccf9355",
    "ONE_SEGMENT_HIDDEN_HELPER_RESOURCE_AUDIT.md": "c971a90e0c7d230bd25df1dd80b2e27c74b9af089ad6194099e217e981a77c87",
    "ONE_SEGMENT_COMPARISON_RESOURCE_GAP_INDEPENDENT_REVIEW.md": "36141219e713ed8a72cb1c6cef9609d00e86aed36f7fd7d80e242d0331562e06",
}
PRODUCER_RESOURCE_EVIDENCE_COMPLETE = False
SUCCESS = "ARITHMETIC_AGREEMENT_WITH_PRODUCER_RESOURCE_EVIDENCE_GAP"
CONFIG = {
    "schema": "fixed-segment-data-only-comparison-v1", "segment": [1280, 1281, 2048],
    "G": G, "H": H, "QP": str(QP), "root_fractional_bits": 128,
    "tensor_labels": list(LABELS), "tensor_scalars": 2587464,
    "W_scalars": 1509354, "S_scalars": 467181,
    "new_center_scalars": 88416, "original_power_scalars": 117888,
    "actual_mutations": 7, "synthetic_boundary_mutations": 2,
    "integer_guard_bits": 8192, "progress_seconds": 8,
    "output_directory": str(OUT), "stdout": str(STDOUT), "stderr": str(STDERR),
    "single_process": True, "PDE": False, "FFT": False,
    "spatial_convolution": False, "full_W_square_recomputed": False,
    "retry": False, "new_parameters": False,
}


class Mismatch(Exception):
    pass


class LimitStop(Exception):
    pass


def need(condition, code):
    if not condition:
        raise Mismatch(code)


def utc():
    return datetime.now(timezone.utc).isoformat()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
                       allow_nan=False)+"\n").encode("ascii")


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def valid_hash(value):
    return isinstance(value, str) and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def validate_digest(actual, expected, label):
    need(valid_hash(actual) and valid_hash(expected), "SHA_FORMAT: "+label)
    need(actual == expected, "SHA_MISMATCH: "+label)


def inside(path):
    path = Path(path).resolve()
    need(path.is_relative_to(HERE), "PATH_OUTSIDE_REVERSE_RESEARCH")
    return path


def integer(value):
    number = int(value)
    need(abs(number).bit_length() <= CONFIG["integer_guard_bits"], "SMALL_INTEGER_GUARD")
    return number


def fraction(value):
    if isinstance(value, dict):
        n, d = integer(value["numerator"]), integer(value["denominator"])
    else:
        need(isinstance(value, list) and len(value) == 2, "FRACTION_SCHEMA")
        n, d = integer(value[0]), integer(value[1])
    need(d > 0 and math.gcd(n, d) == 1, "FRACTION_NOT_CANONICAL")
    return Fraction(n, d)


def fp(value):
    return [str(value.numerator), str(value.denominator)]


def signed(data, index, width):
    return int.from_bytes(data[index*width:(index+1)*width], "little", signed=True)


def k_at(index):
    return (index % 33-16, (index//33) % 33-16, index//1089-16)


def validate_equal(left, right, label):
    need(left == right, "SCALAR_MISMATCH: "+label)


def validate_tensor(label, primary_values, independent_value):
    if label[0] == label[1]:
        need(len(primary_values) == 1, "DIAGONAL_SCHEMA")
        value = primary_values[0]
    else:
        need(len(primary_values) == 3, "POLARIZATION_SCHEMA")
        numerator = primary_values[2]-primary_values[0]-primary_values[1]
        value, remainder = divmod(numerator, 2)
        need(remainder == 0, "POLARIZATION_ODD_NUMERATOR")
    validate_equal(value, independent_value, "TENSOR_"+label)
    return value


def validate_containment(lower, actual, upper, label, width_limit=None):
    need(lower <= actual <= upper, "INTERVAL_EXCLUDES_EXACT_VALUE: "+label)
    if width_limit is not None:
        need(upper-lower <= width_limit, "INTERVAL_WIDTH: "+label)


def validate_floor(value, divisor, lower, upper):
    need(divisor > 0, "FLOOR_DIVISOR")
    need(lower*divisor <= value < (lower+1)*divisor, "SIGNED_FLOOR")
    need((upper-1)*divisor < value <= upper*divisor, "SIGNED_CEIL")
    need(upper-lower == int(value % divisor != 0), "FLOOR_CEIL_WIDTH")


def validate_root(value, scale, lower, upper):
    need(value >= 0 and scale > 0, "ROOT_DOMAIN")
    n, d = value.numerator*scale*scale, value.denominator
    need(lower >= 0 and lower*lower*d <= n < (lower+1)*(lower+1)*d, "ROOT_TRUE_RATIONAL_FLOOR")
    need(upper == lower+int(lower*lower*d != n), "ROOT_TRUE_RATIONAL_CEIL")
    return lower*lower*d == n


def final_locks_ready():
    required = {
        "audit_one_segment_residual_independent.py",
        "one-segment-residual-independent-trial-01/run.json",
        "one-segment-residual-independent-trial-01/result.json",
        "one-segment-residual-independent-trial-01/final-receipt.json",
        INDEPENDENT_ACCEPTANCE,
    }
    return (set(ARITHMETIC_ONLY_SUPPLEMENT_PINS) == {
                "ONE_SEGMENT_COMPARISON_RESOURCE_GAP_ADDENDUM.md",
                "ONE_SEGMENT_HIDDEN_HELPER_RESOURCE_AUDIT.md",
                "ONE_SEGMENT_COMPARISON_RESOURCE_GAP_INDEPENDENT_REVIEW.md"}
            and required.issubset(INDEPENDENT_FINAL_PINS)
            and isinstance(RESOURCE_LOCK, dict)
            and all(isinstance(RESOURCE_LOCK.get(k), (int, float)) and RESOURCE_LOCK[k] > 0
                    for k in ("wall_seconds", "rss_bytes", "output_bytes")))


def config_sha():
    return hashlib.sha256(canonical({"config": CONFIG, "resources": RESOURCE_LOCK,
                                      "producer_resource_evidence_complete": PRODUCER_RESOURCE_EVIDENCE_COMPLETE,
                                      "pins": {**FIXED_PINS, **INDEPENDENT_FINAL_PINS, **ARITHMETIC_ONLY_SUPPLEMENT_PINS}})).hexdigest()


def preflight(run=False, review=None, review_sha=None):
    need(sys.version_info >= (3, 10) and sys.flags.optimize == 0, "PYTHON_VERSION_OR_OPTIMIZATION")
    need(TREE == Path("/Users/kasifa/Documents/Math/navier-stokes-reverse"), "REVERSE_TREE_ONLY")
    raw = Path(__file__).read_bytes()
    raw.decode("ascii")
    compile(ast.parse(raw), str(Path(__file__)), "exec")
    bindings = {}
    for name, expected in {**FIXED_PINS, **INDEPENDENT_FINAL_PINS, **ARITHMETIC_ONLY_SUPPLEMENT_PINS}.items():
        actual = file_sha(inside(HERE/name))
        validate_digest(actual, expected, name)
        bindings[name] = actual
    if INDEPENDENT_FINAL_PINS:
        for path, descriptor in byte_only_transitive_pins().items():
            if descriptor["bytes"] is not None:
                need(Path(path).stat().st_size == descriptor["bytes"], "STATIC_TRANSITIVE_LENGTH")
            actual = file_sha(path)
            validate_digest(actual, descriptor["sha256"], path)
            bindings[str(Path(path).relative_to(HERE))] = actual
    review_binding = None
    if review is not None or review_sha is not None:
        need(review is not None and review_sha is not None, "REVIEW_PAIR_REQUIRED")
        path = inside(review)
        validate_digest(file_sha(path), review_sha, path.name)
        content = path.read_text()
        need(hashlib.sha256(raw).hexdigest() in content and FIXED_PINS[CONTRACT] in content,
             "SOURCE_REVIEW_MUST_BIND_CURRENT_CODE_AND_CONTRACT")
        review_binding = {"path": str(path), "sha256": review_sha}
    if run:
        need(final_locks_ready(), "REVIEWED_ARITHMETIC_ONLY_SUPPLEMENT_OR_FINAL_LOCKS_PENDING")
        need(review_binding is not None, "ROOT_FULL_SOURCE_REVIEW_REQUIRED")
        for fd, path in ((1, STDOUT), (2, STDERR)):
            actual, target = os.fstat(fd), path.stat()
            need((actual.st_dev, actual.st_ino) == (target.st_dev, target.st_ino), "EXCLUSIVE_STDIO_REDIRECTION_REQUIRED")
            need(stat.S_ISREG(actual.st_mode) and actual.st_size == 0,
                 "ROOT_MUST_CREATE_EMPTY_REGULAR_STDIO_WITH_XB_OR_NOCLOBBER")
    status = ("STATIC_FIXED_PINS_PASS_ARITHMETIC_ONLY_AWAITING_ROOT_UNIQUE_RUN" if review_binding
              else "STATIC_FIXED_PINS_PASS_ARITHMETIC_ONLY_SOURCE_REVIEW_NOT_BOUND")
    if not final_locks_ready():
        status = "STATIC_FIXED_PINS_VALID_FINAL_LOCKS_PENDING"
    return {"status": status,
            "data_comparison_executed": False, "final_locks_ready": final_locks_ready(),
            "source_sha256": hashlib.sha256(raw).hexdigest(), "config_sha256": config_sha(),
            "producer_resource_evidence_complete": PRODUCER_RESOURCE_EVIDENCE_COMPLETE,
            "certificate_ready": False, "release_ready": False,
            "fixed_bindings": bindings, "resource_lock": RESOURCE_LOCK, "config": CONFIG,
            "runtime_root_source_review": review_binding, "output_directory_exists": OUT.exists()}


class Monitor:
    def __init__(self):
        self.last = START
        self.stage = "source bindings"
        self.bindings = {}

    def observation(self):
        rss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        if sys.platform != "darwin":
            rss *= 1024
        paths = list(OUT.iterdir()) if OUT.exists() else []
        size = sum(p.stat().st_size for p in paths if p.is_file())
        size += sum(p.stat().st_size for p in (STDOUT, STDERR) if p.exists())
        return {"elapsed_seconds": time.monotonic()-START, "peak_rss_bytes": rss,
                "all_output_bytes": size, "single_process_no_children": True}

    def check(self, stage=None):
        if stage:
            self.stage = stage
        value = self.observation()
        if (value["elapsed_seconds"] >= RESOURCE_LOCK["wall_seconds"]
                or value["peak_rss_bytes"] > RESOURCE_LOCK["rss_bytes"]
                or value["all_output_bytes"] > RESOURCE_LOCK["output_bytes"]):
            raise LimitStop("COMPARISON_RESOURCE_LIMIT: "+json.dumps(value))
        if time.monotonic()-self.last >= CONFIG["progress_seconds"]:
            self.last = time.monotonic()
            print(json.dumps({"stage": self.stage, "resources": value}), flush=True)
        return value

    def bind(self, path, expected, size=None):
        path = inside(path)
        name = str(path.relative_to(HERE))
        if name in self.bindings:
            validate_digest(self.bindings[name]["sha256"], expected, name)
            if size is not None:
                need(self.bindings[name]["bytes"] == size, "REPEATED_BINDING_SIZE")
            return
        actual_size = path.stat().st_size
        if size is not None:
            need(actual_size == size, "FILE_LENGTH: "+name)
        actual = file_sha(path)
        validate_digest(actual, expected, name)
        self.bindings[name] = {"sha256": actual, "bytes": actual_size}
        self.check()


def load_json(path):
    return json.loads(Path(path).read_bytes())


def read_modes():
    raw = (HERE/"node-trial-01/modes.npy").read_bytes()
    need(raw[:6] == b"\x93NUMPY" and raw[6:8] == b"\x01\x00", "ORIGINAL_NPY_VERSION")
    length = struct.unpack("<H", raw[8:10])[0]
    header = ast.literal_eval(raw[10:10+length].decode("latin1"))
    need(header == {"descr": "<i8", "fortran_order": False, "shape": (G, 3)}, "ORIGINAL_NPY_HEADER")
    payload = raw[10+length:]
    need(len(payload) == G*3*8, "ORIGINAL_MODE_BYTES")
    modes = list(struct.iter_unpack("<qqq", payload))
    expected = [p for p in itertools.product(range(-8, 9), repeat=3) if p != (0, 0, 0)]
    need(modes == expected, "FULL_ORIGINAL_G_ORDER")
    return modes


def check_primary_recorded_observations(obs):
    # These are historical observations of the tracked set, not a proof that
    # implicit platform helpers were included. The producer gap remains explicit.
    need(obs["wall_seconds_from_parent_entry"] < 600
         and obs["all_output_bytes"] <= 512*1024**2
         and obs["self_peak_rss_bytes"] <= 2*1024**3
         and obs["parent_plus_all_child_highwater_sum_bytes"] <= 2*1024**3
         and obs["latest_simultaneous_rss_upper_observation_bytes"] <= 2*1024**3,
         "PRIMARY_RECORDED_OBSERVATIONS_OUT_OF_RECORDED_LIMIT")


def check_independent_recorded_observations(obs):
    # Verify consistency of the six tracked workers only; do not infer that the
    # set contains every historical descendant process.
    need(obs["elapsed_seconds"] <= 600 and obs["output_bytes"] <= 512*1024**2
         and obs["all_process_highwater_sum_bytes"] <= 2*1024**3
         and obs["simultaneous_rss_peak_bytes"] <= 2*1024**3
         and obs["output_observation"]["metadata_and_external_log_bytes"] <= 8*1024**2,
         "INDEPENDENT_RECORDED_OBSERVATIONS_OUT_OF_RECORDED_LIMIT")
    children = obs["children"]
    need(len(children) == 6 and not obs["cleanup_errors"], "INDEPENDENT_CHILD_ACCOUNTING")
    for child in children.values():
        need(child["wait4"]["exit_code"] == 0 and child["wait4"]["highwater_bytes"] > 0,
             "INDEPENDENT_ACTUAL_WAIT4")
    need(obs["parent"]["highwater_bytes"]+sum(c["observed_highwater_bytes"] for c in children.values())
         == obs["all_process_highwater_sum_bytes"], "INDEPENDENT_HIGHWATER_SUM")


def archive_sources(mon):
    for name, expected in {**FIXED_PINS, **INDEPENDENT_FINAL_PINS, **ARITHMETIC_ONLY_SUPPLEMENT_PINS}.items():
        mon.bind(HERE/name, expected)
    mr, mp = load_json(PRIMARY/"run.json"), load_json(PRIMARY/"result.json")
    ir, ip = load_json(INDEPENDENT/"run.json"), load_json(INDEPENDENT/"result.json")
    ma = load_json(HERE/"one-segment-primary-root-execution-acceptance.json")
    ia = load_json(HERE/INDEPENDENT_ACCEPTANCE)
    need(mr["execution_status"] == "PRIMARY_COMPLETE_PENDING_INDEPENDENT_REVIEW"
         and mp["schema"] == "one-fixed-segment-primary-residual-bounds-v1"
         and mp["status"] == "PRIMARY_ONE_SEGMENT_BOUNDS_COMPUTED_PENDING_INDEPENDENT_REVIEW",
         "PRIMARY_COMPLETE_SCOPE")
    need(ir["status"] == "COMPLETE_FIXED_SEGMENT_INDEPENDENT_RESIDUAL"
         and ip["schema"] == "one-segment-independent-direct-result-v1"
         and ip["segment_nodes"] == [1280, 1281] and ip["time_denominator"] == 2048,
         "INDEPENDENT_COMPLETE_SCOPE")
    need(ma["observed_exec_exit_code"] == 0 and ia["observed_exec_exit_code"] == 0,
         "ROOT_ATTESTED_ACTUAL_PROCESS_EXIT_ZERO")
    for rec, prefix in ((ma, "one-segment-residual-trial-01/"),
                        (ia, "one-segment-residual-independent-trial-01/")):
        for name in ("run", "result"):
            validate_digest(rec[name+"_sha256"], {**FIXED_PINS, **INDEPENDENT_FINAL_PINS}[prefix+name+".json"],
                            "root actual exit acceptance "+name)
    need(mr["source_commit"] == mp["source_commit"] == ma["source_commit"]
         == "31f7f4e382732fb9e20cc0a50293b19d056d2fb3", "PRIMARY_SOURCE_COMMIT")
    need(mr["source_sha256"] == mp["source_sha256"] == ma["source_sha256"]
         == FIXED_PINS["audit_one_segment_residual.py"], "PRIMARY_SOURCE_BYTES")
    need(ir["source_sha256"] == ip["source_sha256"] and ir["input_sha256"] == ip["input_sha256"]
         and ir["checkout"] == ip["checkout"] and ir["config_sha256"] == ip["config_sha256"],
         "INDEPENDENT_RUN_RESULT_SOURCE")
    need(ir["source_sha256"]["audit_one_segment_residual_independent.py"]
         == INDEPENDENT_FINAL_PINS["audit_one_segment_residual_independent.py"], "INDEPENDENT_SOURCE_BYTES")
    need(ir["checkout"]["commit"] == ia["source_commit"] == "616b7ec2f3f6e0578bf07b9ced2ad6ccb1bc9cc9"
         and ia["source_sha256"] == INDEPENDENT_FINAL_PINS["audit_one_segment_residual_independent.py"],
         "INDEPENDENT_ROOT_EXECUTION_SOURCE")
    cfg = mr["preflight"]["config"]
    need(cfg["node_indices"] == [1280, 1281] and cfg["time_denominator"] == 2048
         and cfg["QP"] == QP and cfg["viscosity"] == 1 and cfg["G_count"] == G and cfg["H_count"] == H,
         "PRIMARY_FIXED_CONFIGURATION")
    cfg = ir["config"]
    need(cfg["segment_nodes"] == [1280, 1281] and cfg["time_denominator"] == 2048
         and integer(cfg["QP"]) == QP and cfg["viscosity"] == 1 and cfg["G"] == G and cfg["H"] == H,
         "INDEPENDENT_FIXED_CONFIGURATION")
    validate_digest(hashlib.sha256(canonical(cfg)).hexdigest(), ir["config_sha256"], "independent config")
    need(mp["config_sha256"] == mr["config_sha256"] == "d67fb54134a11fb93ca56e4ed8bafe6094840e5d4e327a2a90a1f4479c051372",
         "PRIMARY_FIXED_CONFIG_SHA")
    for collection in (mp["input_sha256"], mp["proof_sha256"], ir["input_sha256"], ir["source_sha256"]):
        for name, expected in collection.items():
            mon.bind(HERE/name, expected)
    for name in ("node-trial-01/manifest.json", "node-trial-01/modes.npy", "node-trial-01/block-01280-01343.npz"):
        validate_digest(mp["input_sha256"][name], ip["input_sha256"][name], "shared original "+name)
    for key in ("source_sha256", "config_sha256"):
        need(mr["preflight"][key] == mp[key], "PRIMARY_PREFLIGHT_CONNECTION")
    review = mr["preflight"]["runtime_root_source_review"]
    need(review == mp["runtime_root_source_review"], "PRIMARY_RUNTIME_REVIEW_CONNECTION")
    mon.bind(review["path"], review["sha256"])
    need(mr["all_child_exits_collected_with_wait4"] and not mr["cleanup_errors"], "PRIMARY_ALL_TRACKED_CHILDREN_COLLECTED")
    for child in mr["child_processes"]:
        need(child["exit_code"] == 0 and child["reaped_with_wait4"] and child["wait4_peak_rss_bytes"] > 0,
             "PRIMARY_ACTUAL_CHILD_EXIT")
    for descriptor in mr["all_child_stdio"]:
        mon.bind(PRIMARY/descriptor["file"], descriptor["sha256"], descriptor["bytes"])
    for descriptor in mr["metadata_snapshots"].values():
        need(descriptor["actual_byte_readback"], "PRIMARY_METADATA_READBACK")
    for name, descriptor in mr["metadata_snapshots"].items():
        mon.bind(PRIMARY/name, descriptor["sha256"], descriptor["bytes"])
    need(mr["artifacts"] == mp["artifacts"] and len(mp["artifacts"]) == 30
         and mr["complete_binary_bytes"] == 288713460 and mr["new_real_products_completed"] == 18,
         "PRIMARY_COMPLETE_BINARY_SET")
    for name, descriptor in mp["artifacts"].items():
        need(descriptor["actual_byte_readback"], "PRIMARY_ALL_BINARY_READBACK")
        mon.bind(PRIMARY/name, descriptor["sha256"], descriptor["bytes"])
        need(ma["binary_bindings"][name] == {"bytes": descriptor["bytes"], "sha256": descriptor["sha256"]},
             "PRIMARY_ROOT_BINARY_ACCEPTANCE")
    need(sum(x["bytes"] for x in mp["artifacts"].values()) == 288713460, "PRIMARY_BINARY_SIZE_SUM")
    for label, record in mr["workers"].items():
        mon.bind(PRIMARY/record["record_file"], record["record_sha256"])
        worker = load_json(PRIMARY/record["record_file"])
        need(worker["execution_status"] == "WORKER_COMPLETE" and worker["large_real_products"] == 3,
             "PRIMARY_POLARIZATION_WORKER")
    need(set(mr["workers"]) == {"1", "2", "3", "12", "13", "23"}, "PRIMARY_SIX_WORKERS")
    ind_artifacts = {x["file"]: x for x in ip["artifacts"]}
    need(len(ind_artifacts) == 11 and sum(x["bytes"] for x in ind_artifacts.values()) == 169192128,
         "INDEPENDENT_COMPLETE_BINARY_SET")
    need({x["file"]: x for x in ir["artifacts"] if x["file"] != "result.json"} == ind_artifacts,
         "INDEPENDENT_RUN_RESULT_ARTIFACTS")
    for name, descriptor in ind_artifacts.items():
        mon.bind(INDEPENDENT/name, descriptor["sha256"], descriptor["bytes"])
        if name == "rounding-floor-rem.i128-u16le.bin":
            need(descriptor["all_117888_rounding_witnesses_read_back"], "INDEPENDENT_ROUNDING_ARCHIVE_READBACK")
        elif name == "S.i544le.bin":
            need(descriptor["all_signed_coefficients_read_back"], "INDEPENDENT_SIGNED_S_READBACK")
        else:
            need(descriptor["all_scalars_read_back"], "INDEPENDENT_ALL_SCALARS_READBACK")
        need(ia["binary_bindings"][name] == {"bytes": descriptor["bytes"], "sha256": descriptor["sha256"]},
             "INDEPENDENT_ROOT_BINARY_ACCEPTANCE")
    for child in ir["resources"]["children"].values():
        name = "worker-"+child["tensor"]+"-result.json"
        mon.bind(INDEPENDENT/name, child["worker_report_sha256"])
        worker = load_json(INDEPENDENT/name)
        need(worker["status"] == "COMPLETE_DIRECT_INCREMENT_TENSOR" and worker["rows_completed"] == G,
             "INDEPENDENT_DIRECT_WORKER")
    check_primary_recorded_observations(mr["resources_before_this_atomic_record_write"])
    check_primary_recorded_observations(ma["final_observation"])
    check_independent_recorded_observations(ir["resources"])
    check_independent_recorded_observations(ir["post_write_observation"])
    receipt = load_json(INDEPENDENT/"final-receipt.json")
    need(receipt["status"] == "COMPLETE_FINAL_ACCOUNTING"
         and receipt["run_sha256"] == INDEPENDENT_FINAL_PINS["one-segment-residual-independent-trial-01/run.json"],
         "INDEPENDENT_FINAL_RECEIPT")
    check_independent_recorded_observations(receipt["observed_after_stdout_flush"])
    need(receipt["receipt_bytes"] == (INDEPENDENT/"final-receipt.json").stat().st_size,
         "INDEPENDENT_RECEIPT_ACTUAL_SIZE")
    need(receipt["observed_after_stdout_flush"] == ia["final_receipt_observation"],
         "INDEPENDENT_ROOT_RECEIPT_OBSERVATION")
    for acceptance, root, prefix in ((ma, PRIMARY, "primary"), (ia, INDEPENDENT, "independent")):
        external_total = 0
        for kind in ("stdout", "stderr"):
            path = HERE/("one-segment-residual-"+prefix+"."+kind+".log")
            mon.bind(path, acceptance[kind]["sha256"], acceptance[kind]["bytes"])
            external_total += path.stat().st_size
        actual_total = external_total+sum(p.stat().st_size for p in root.iterdir() if p.is_file())
        need(actual_total == acceptance["actual_all_output_bytes_after_exit"] <= 512*1024**2,
             "ACTUAL_FROZEN_ARCHIVE_AND_STDIO_TOTAL")
    need(receipt["all_output_bytes_including_receipt"] == ia["actual_all_output_bytes_after_exit"],
         "ACTUAL_INDEPENDENT_RECEIPT_TOTAL")
    independent_stdout = load_last_json(HERE/"one-segment-residual-independent.stdout.log")
    need(independent_stdout["status"] == ir["status"]
         and independent_stdout["sha256"] == receipt["run_sha256"], "INDEPENDENT_LAST_STDOUT")
    check_independent_recorded_observations(independent_stdout["before_stdout_observation"])
    main_stdout = load_last_json(HERE/"one-segment-residual-primary.stdout.log")
    need(main_stdout["status"] == mr["execution_status"]
         and main_stdout["run_sha256"] == FIXED_PINS["one-segment-residual-trial-01/run.json"], "PRIMARY_LAST_STDOUT")
    check_primary_recorded_observations(main_stdout["post_record_write_observation"])
    need(mp["complete_signed_S"]["all_W_to_S_readback_equal"] and mp["complete_signed_S"]["old_constant_norm_connection"],
         "PRIMARY_SQUARE_READBACK_SOURCE")
    need(ip["squared_norm_integer_products"] == H*6*49 and ip["primary_comparison"] == "NOT_PERFORMED",
         "INDEPENDENT_FULL_SQUARE_AND_NO_PRIMARY_REUSE")
    return mr, mp, ir, ip


def load_last_json(path):
    lines = Path(path).read_text().splitlines()
    need(bool(lines), "MISSING_LAST_STDOUT")
    return json.loads(lines[-1])


def compare_tensors(mon, witnesses):
    count = 0
    for label in LABELS:
        a, b = label
        names = [a] if a == b else [a, b, label]
        primary = [(PRIMARY/("df-"+name+".i248le.bin")).read_bytes() for name in names]
        independent = (INDEPENDENT/("delta-T"+label+".i248le.bin")).read_bytes()
        need(all(len(x) == 6*H*2*31 for x in [*primary, independent]), "FULL_TENSOR_LENGTH")
        for i in range(6*H*2):
            values = tuple(signed(x, i, 31) for x in primary)
            target = signed(independent, i, 31)
            value = validate_tensor(label, values, target)
            if value != 0 and a != b and "tensor" not in witnesses:
                witnesses["tensor"] = {"label": label, "scalar_index": i,
                                       "primary_values": list(map(str, values)), "independent_value": str(target)}
            count += 1
            if i % 2048 == 0:
                mon.check("full polarization-to-direct tensor comparison: "+label)
        del primary, independent
    need(count == CONFIG["tensor_scalars"], "FULL_TENSOR_COUNT")
    return count


def compare_vector_and_square(mon, witnesses):
    counts, aggregates = {}, None
    for name, width, total, label in (("W.i272le.bin", 34, 7*H*6, "W"),
                                      ("S.i544le.bin", 68, 13*H, "S")):
        left, right = (PRIMARY/name).read_bytes(), (INDEPENDENT/name).read_bytes()
        need(len(left) == len(right) == total*width, "FULL_"+label+"_LENGTH")
        if label == "S":
            aggregates = {"A2": [0]*13, "floor": [0]*13, "ceil": [0]*13, "inexact": [0]*13}
        for i in range(total):
            value, target = signed(left, i, width), signed(right, i, width)
            validate_equal(value, target, label)
            if value != 0 and label not in witnesses and (label != "W" or i % 2 == 1):
                witnesses[label] = {"scalar_index": i, "left": str(value), "right": str(target)}
            mode = (i//6) % H if label == "W" else i % H
            if mode == (H-1)//2:
                need(value == 0, label+"_ZERO_MODE")
            if label == "S" and mode != (H-1)//2:
                m, k = i//H, k_at(mode)
                s = sum(v*v for v in k)
                lo, rem = divmod(value, s*s)
                hi = lo+int(rem != 0)
                validate_floor(value, s*s, lo, hi)
                aggregates["A2"][m] += value
                aggregates["floor"][m] += lo
                aggregates["ceil"][m] += hi
                aggregates["inexact"][m] += int(rem != 0)
            if i % 2048 == 0:
                mon.check("full signed "+label+" comparison")
        counts[label] = total
        del left, right
    return counts, aggregates


def compare_coefficients(mon, witnesses, modes):
    b = (PRIMARY/"hermite-b.i96le.bin").read_bytes()
    ah = (INDEPENDENT/"hermite-AH.i128le.bin").read_bytes()
    main_c = (PRIMARY/"new-C.i120le.bin").read_bytes()
    ind_c = (INDEPENDENT/"centers-c96.i128le.bin").read_bytes()
    old_c = (HERE/"kronecker-block-trial-02/c96-centers.i112le.bin").read_bytes()
    e = (PRIMARY/"rounding-e.i80le.bin").read_bytes()
    floor_rem = (INDEPENDENT/"rounding-floor-rem.i128-u16le.bin").read_bytes()
    expected = ((b, 4*G*6*12), (ah, 4*G*6*16), (main_c, 3*G*6*15),
                (ind_c, 4*G*6*16), (old_c, G*6*14), (e, 4*G*6*10), (floor_rem, 4*G*6*18))
    need(all(len(data) == n for data, n in expected), "FULL_ORIGINAL_AND_CENTER_FORMATS")
    new_count = 0
    for i in range(4*G*6):
        r, local = divmod(i, G*6)
        mode = local//6
        s = sum(x*x for x in modes[mode])
        bm, bi = signed(b, i, 12), signed(ah, i, 16)
        validate_equal(bm, bi, "ORIGINAL_POWER_NUMERATOR_SAME_2^64_s_DENOMINATOR")
        ci = signed(ind_c, i, 16)
        cm = signed(old_c, local, 14) if r == 0 else signed(main_c, (r-1)*G*6+local, 15)
        validate_equal(cm, ci, "CENTER")
        if r:
            new_count += 1
            if cm and "center" not in witnesses:
                witnesses["center"] = {"power": r, "local_scalar": local, "left": str(cm), "right": str(ci)}
        need(signed(e, i, 10) == QP*bm-ci*(1 << 64)*s, "PRIMARY_ROUNDING_WITNESS_CONNECTION")
        off = i*18
        lo = int.from_bytes(floor_rem[off:off+16], "little", signed=True)
        rem = int.from_bytes(floor_rem[off+16:off+18], "little")
        need(0 <= rem < s and (bi << 32) == lo*s+rem, "INDEPENDENT_ROUNDING_DIVISION")
        need(ci == lo+int(2*rem > s or (2*rem == s and lo % 2)), "INDEPENDENT_NEAREST_EVEN")
        if i % 2048 == 0:
            mon.check("complete original four coefficients, fixed centers and archived witnesses")
    need(new_count == CONFIG["new_center_scalars"], "FULL_NEW_CENTER_COUNT")
    return {"original_power_scalars": 4*G*6, "new_center_scalars": new_count,
            "old_center_scalars": G*6, "rounding_witnesses_connected": 4*G*6}


def bernstein(power):
    need(len(power) == 13, "DEGREE12_POWER_LENGTH")
    return [sum((Fraction(math.comb(m, l), math.comb(12, l))*power[l]
                 for l in range(m+1)), Fraction(0)) for m in range(13)]


def root_record(primary, record, expected_argument):
    if primary:
        argument = fraction(record["argument"])
        scale, lo, hi = integer(record["scale"]), integer(record["floor_numerator"]), integer(record["ceil_numerator"])
        lower, upper = fraction(record["root_lower"]), fraction(record["root_upper"])
        exact = record["true_rational_square_equality"]
        need(record["root_lower_is_NOT_a_residual_lower_bound"]
             and record["argument_is_Bernstein_upper_bound_not_actual_norm_square"], "PRIMARY_ROOT_SCOPE")
    else:
        argument = fraction(record["input"])
        need(record["bits"] == 128, "INDEPENDENT_ROOT_BITS")
        scale, lo, hi = P, integer(record["floor_root"]), integer(record["ceil_root"])
        lower, upper = fraction(record["lower"]), fraction(record["upper"])
        exact = record["true_rational_equality"]
        need(integer(record["denominator"]) == argument.denominator, "INDEPENDENT_ROOT_DENOMINATOR")
    need(argument == expected_argument and scale == P, "ROOT_ARGUMENT_FROM_ALL_BERNSTEIN")
    actual_exact = validate_root(argument, scale, lo, hi)
    need(exact == actual_exact and lower == Fraction(lo, P) and upper == Fraction(hi, P), "ROOT_RECORDED_INTERVAL")
    scaled = argument.numerator*P*P
    need(integer(record["scaled_numerator"]) == scaled, "ROOT_SCALED_NUMERATOR")
    if primary:
        q, r = divmod(scaled, argument.denominator)
        need(integer(record["quotient"]) == q and integer(record["remainder"]) == r, "PRIMARY_ROOT_DIVISION")
    return lower, upper


def compare_bounds(mon, mp, ip, aggregates, witnesses):
    pm, pi = mp["reconstruction"], ip["input_connection"]
    M = [fraction(x) for x in pm["M"]]
    delta = [fraction(x) for x in pm["delta"]]
    need(len(M) == len(delta) == 4 and M == [fraction(x) for x in pi["M"]]
         and delta == [fraction(x) for x in pi["delta"]], "ALL_FOUR_M_DELTA")
    Msum, dsum = sum(M, Fraction(0)), sum(delta, Fraction(0))
    need(fraction(pm["M_star"]) == fraction(pi["M_sum"]) == Msum
         and fraction(pm["delta_star"]) == fraction(pi["delta_sum"]) == dsum, "M_DELTA_SUMS")
    E = {j: 28**(j+1)*(2*Msum*dsum+dsum*dsum) for j in (0, 2)}
    for j in (0, 2):
        need(fraction(pm["E_star"][str(j)]) == fraction(pi["E"][str(j)]) == E[j], "SAME_COMPLETE_INPUT_ERROR")
    complete = mp["complete_signed_S"]
    need([integer(x) for x in complete["A2"]] == aggregates["A2"]
         and [integer(x) for x in complete["A0_floor_sums"]] == aggregates["floor"]
         and [integer(x) for x in complete["A0_ceil_sums"]] == aggregates["ceil"]
         and complete["noninteger_counts"] == aggregates["inexact"], "COMPLETE_SIGNED_S_AGGREGATES")
    den = QP**4
    need(integer(complete["denominator"]) == den, "EXACT_SQUARE_DENOMINATOR")
    mq2 = [Fraction(v, den) for v in aggregates["A2"]]
    mq0lo = [Fraction(v, den) for v in aggregates["floor"]]
    mq0hi = [Fraction(v, den) for v in aggregates["ceil"]]
    need(mq2 == [fraction(x) for x in mp["power_coefficients"]["2_exact"]]
         and mq0lo == [fraction(x) for x in mp["power_coefficients"]["0_lower"]]
         and mq0hi == [fraction(x) for x in mp["power_coefficients"]["0_upper"]], "PRIMARY_S_TO_POWER_COEFFICIENTS")
    iq = {j: [fraction(x) for x in ip["bounds"][str(j)]["power_coefficients"]] for j in (0, 2)}
    need(mq2 == iq[2] and len(iq[0]) == 13, "FULL_H2_EXACT_POWER_COEFFICIENTS")
    for m in range(13):
        validate_containment(mq0lo[m], iq[0][m], mq0hi[m], "ZERO_ORDER_POWER_"+str(m), Fraction(35936, den))
        if (iq[0][m] != 0 and mq0lo[m] < mq0hi[m] and "interval" not in witnesses):
            witnesses["interval"] = {"power": m, "lower": fp(mq0lo[m]),
                                     "actual": fp(iq[0][m]), "upper": fp(mq0hi[m])}
    mb2, mb0lo, mb0hi = bernstein(mq2), bernstein(mq0lo), bernstein(mq0hi)
    ib = {j: bernstein(iq[j]) for j in (0, 2)}
    need(mb2 == ib[2], "FULL_H2_EXACT_BERNSTEIN")
    for key, values in (("2_exact", mb2), ("0_lower", mb0lo), ("0_upper", mb0hi)):
        need(values == [fraction(x) for x in mp["Bernstein"][key]], "PRIMARY_BERNSTEIN_TRANSFORM_"+key)
    for j in (0, 2):
        need(ib[j] == [fraction(x) for x in ip["bounds"][str(j)]["bernstein_coefficients"]],
             "INDEPENDENT_BERNSTEIN_TRANSFORM")
    need(mp["Bernstein"]["degree"] == 12 and len(mp["Bernstein"]["weights"]) == 13,
         "BERNSTEIN_WEIGHT_SCHEMA")
    widths = []
    for m in range(13):
        row = [Fraction(math.comb(m, l), math.comb(12, l)) for l in range(m+1)]
        need(row == [fraction(x) for x in mp["Bernstein"]["weights"][m]], "ALL_BERNSTEIN_WEIGHTS")
        validate_containment(mb0lo[m], ib[0][m], mb0hi[m], "ZERO_ORDER_BERNSTEIN_"+str(m), Fraction(13*35936, den))
        propagated = sum((row[l]*(mq0hi[l]-mq0lo[l]) for l in range(m+1)), Fraction(0))
        need(mb0hi[m]-mb0lo[m] == propagated, "SIGNED_WIDTH_PROPAGATION")
        widths.append(propagated)
    need(widths == [fraction(x) for x in mp["Bernstein"]["0_actual_widths"]]
         and fraction(mp["Bernstein"]["0_propagated_width_bound"]) == Fraction(13*35936, den),
         "RECORDED_BERNSTEIN_WIDTHS")
    rbmain, rbind, rootmain, rootind = {}, {}, {}, {}
    for j in (0, 2):
        max_main = max(Fraction(0), *(mb0hi if j == 0 else mb2))
        max_ind = max(Fraction(0), *ib[j])
        need(fraction(ip["bounds"][str(j)]["maximum"]) == max_ind, "INDEPENDENT_BERNSTEIN_MAXIMUM")
        rootmain[j] = root_record(True, mp["root_bounds"][str(j)], max_main)
        rootind[j] = root_record(False, ip["bounds"][str(j)]["root"], max_ind)
        rbmain[j], rbind[j] = rootmain[j][1]+E[j], rootind[j][1]+E[j]
        need(fraction(mp["root_bounds"][str(j)]["E_star_added_once"]) == E[j]
             and fraction(ip["bounds"][str(j)]["E"]) == E[j], "E_ADDED_ONCE")
        need(fraction(mp["original_residual_segment_upper"][str(j)]) == rbmain[j]
             and fraction(mp["root_bounds"][str(j)]["original_residual_segment_upper"]) == rbmain[j]
             and fraction(ip["bounds"][str(j)]["original_segment_upper"]) == rbind[j], "ORIGINAL_SEGMENT_UPPER_FROM_ROOT_PLUS_E")
        need(ip["bounds"][str(j)]["root_lower_is_original_residual_lower"] is False,
             "INDEPENDENT_ROOT_LOWER_SCOPE")
    need(rootmain[2] == rootind[2] and rbmain[2] == rbind[2] and rbmain[0] >= rbind[0],
         "H2_EQUAL_H0_ENCLOSURE_ORDER")
    factor, threshold = Fraction(3584, 1023), Fraction(2, 8085825)
    gamma_main = factor*max(rbmain[2], 64*rbmain[0])
    gamma_ind = factor*max(rbind[2], 64*rbind[0])
    def classification(value):
        return ("SEGMENT_UPPER_BOUND_WITHIN_EXISTING_SUFFICIENT_THRESHOLD" if value < threshold
                else "NOT_CERTIFIED_BY_THIS_UPPER_BOUND")
    need(gamma_main >= gamma_ind, "GAMMA_ENCLOSURE_ORDER")
    interface = mp["fixed_control_interface"]
    need(fraction(interface["gamma_factor"]) == factor
         and fraction(interface["existing_sufficient_threshold_lower"]) == threshold
         and fraction(interface["Gamma_I"]) == gamma_main
         and interface["status"] == classification(gamma_main)
         and interface["new_epsilon_selected"] is False, "PRIMARY_RECORDED_GAMMA")
    need(ip["epsilon_or_gamma"] is None, "INDEPENDENT_GAMMA_IS_DERIVED_BY_COMPARISON_NOT_PRESTORED")
    mon.check("complete exact norms, containment, Bernstein, roots and fixed Gamma interface")
    return {"M": [fp(x) for x in M], "delta": [fp(x) for x in delta], "E": {str(j): fp(E[j]) for j in (0, 2)},
            "H2_power_and_Bernstein_equal": True, "H0_power_and_Bernstein_contained": True,
            "power_coefficients_compared_each_order": 13, "Bernstein_coefficients_compared_each_order": 13,
            "H0_Bernstein_interval_widths": [fp(x) for x in widths],
            "original_segment_upper_main": {str(j): fp(rbmain[j]) for j in (0, 2)},
            "original_segment_upper_independent": {str(j): fp(rbind[j]) for j in (0, 2)},
            "Gamma_main": fp(gamma_main), "Gamma_independent_derived_here": fp(gamma_ind),
            "Gamma_main_status": classification(gamma_main), "Gamma_independent_status": classification(gamma_ind),
            "same_threshold_status": classification(gamma_main) == classification(gamma_ind),
            "allowed_difference": "independent may pass while wider primary bound is not certified",
            "new_epsilon_selected": False, "full_window_or_NS_claim": False}


def mutation_controls(witnesses, source_witness):
    actual, synthetic = [], []
    required = {"tensor", "W", "S", "center", "interval"}
    need(required.issubset(witnesses), "MISSING_ACTUAL_NONZERO_MUTATION_WITNESS")

    def rejected(collection, name, validator, baseline, mutated, evidence):
        validator(*baseline)
        try:
            validator(*mutated)
        except Mismatch as exc:
            collection.append({"name": name, "validator": validator.__name__,
                               "baseline_passed": True, "mutation_rejected": True,
                               "actual_error": str(exc), "evidence": evidence})
        else:
            raise Mismatch("MUTATION_NOT_REJECTED: "+name)

    t = witnesses["tensor"]
    values, target = tuple(map(integer, t["primary_values"])), integer(t["independent_value"])
    need(target != 0, "TENSOR_WITNESS_NONZERO")
    baseline = (t["label"], values, target)
    rejected(actual, "actual_new_tensor_component", validate_tensor, baseline,
             (t["label"], values, target+1), t)
    odd = (*values[:2], values[2]+1)
    rejected(actual, "actual_polarization_odd_numerator", validate_tensor, baseline,
             (t["label"], odd, target), t)
    for key, name in (("W", "actual_W_imaginary_phase"), ("S", "actual_signed_S"),
                      ("center", "actual_new_center")):
        w = witnesses[key]
        left, right = integer(w["left"]), integer(w["right"])
        need(left != 0, "ACTUAL_SCALAR_WITNESS_NONZERO")
        rejected(actual, name, validate_equal, (left, right, key), (left+1, right, key), w)
    w = witnesses["interval"]
    lower, truth, upper = fraction(w["lower"]), fraction(w["actual"]), fraction(w["upper"])
    need(truth != 0, "ACTUAL_INTERVAL_WITNESS_NONZERO")
    if lower < truth:
        bad_lower, bad_upper = lower, (lower+truth)/2
    elif truth < upper:
        bad_lower, bad_upper = (truth+upper)/2, upper
    else:
        raise Mismatch("NO_ACTUAL_STRICT_INTERVAL_SHRINK_WITNESS")
    need(lower <= bad_lower <= bad_upper <= upper and (bad_lower, bad_upper) != (lower, upper),
         "MUTATION_MUST_BE_A_TRUE_ORIGINAL_SUBINTERVAL")
    evidence = {**w, "mutated_lower": fp(bad_lower), "mutated_upper": fp(bad_upper),
                "one_original_endpoint_unchanged": True, "strict_original_subinterval": True}
    rejected(actual, "actual_zero_order_interval_excludes_truth", validate_containment,
             (lower, truth, upper, "mutated interval", Fraction(35936, QP**4)),
             (bad_lower, truth, bad_upper, "mutated interval", Fraction(35936, QP**4)), evidence)
    good = source_witness["sha256"]
    bad = ("1" if good[0] == "0" else "0")+good[1:]
    rejected(actual, "actual_source_sha_mismatch", validate_digest,
             (good, good, source_witness["file"]), (good, bad, source_witness["file"]), source_witness)
    rejected(synthetic, "negative_floor_toward_zero_is_wrong", validate_floor,
             (-3, 2, -2, -1), (-3, 2, -1, -1),
             {"synthetic": True, "fraction": ["-3", "2"], "correct_floor": -2, "correct_ceil": -1})
    rejected(synthetic, "square_floor_does_not_mean_exact_rational_root", validate_root,
             (Fraction(9, 8), 2, 2, 3), (Fraction(9, 8), 2, 2, 2),
             {"synthetic": True, "argument": ["9", "8"], "scale": 2,
              "floor_scaled_argument": 4, "true_scaled_argument": ["9", "2"]})
    need(len(actual) == 7 and len(synthetic) == 2, "FIXED_MUTATION_COUNTS")
    return {"actual_nonzero_archive_mutations": actual, "synthetic_boundary_mutations": synthetic,
            "all_same_validator_baselines_passed_and_mutations_rejected": True,
            "frozen_files_modified": False}


def byte_only_transitive_pins():
    """Read metadata paths/hashes/sizes only; never decode a scientific integer."""
    requests = {}
    def add(path, expected, size=None):
        path = str(inside(path))
        need(valid_hash(expected), "TRANSITIVE_SHA_FORMAT")
        if path in requests:
            validate_digest(requests[path]["sha256"], expected, "consistent transitive pin")
            if requests[path]["bytes"] is not None and size is not None:
                need(requests[path]["bytes"] == size, "TRANSITIVE_SIZE_CONFLICT")
            if size is None:
                size = requests[path]["bytes"]
        requests[path] = {"sha256": expected, "bytes": size}
    mr, mp = load_json(PRIMARY/"run.json"), load_json(PRIMARY/"result.json")
    ir, ip = load_json(INDEPENDENT/"run.json"), load_json(INDEPENDENT/"result.json")
    for collection in (mp["input_sha256"], mp["proof_sha256"], ir["input_sha256"], ir["source_sha256"]):
        for name, expected in collection.items():
            add(HERE/name, expected)
    for name, descriptor in mp["artifacts"].items():
        add(PRIMARY/name, descriptor["sha256"], descriptor["bytes"])
    for descriptor in ip["artifacts"]:
        add(INDEPENDENT/descriptor["file"], descriptor["sha256"], descriptor["bytes"])
    for name, descriptor in mr["metadata_snapshots"].items():
        add(PRIMARY/name, descriptor["sha256"], descriptor["bytes"])
    for record in mr["workers"].values():
        add(PRIMARY/record["record_file"], record["record_sha256"])
    for descriptor in mr["all_child_stdio"]:
        add(PRIMARY/descriptor["file"], descriptor["sha256"], descriptor["bytes"])
    for child in ir["resources"]["children"].values():
        add(INDEPENDENT/("worker-"+child["tensor"]+"-result.json"), child["worker_report_sha256"])
    review = mr["preflight"]["runtime_root_source_review"]
    add(review["path"], review["sha256"])
    return requests


def checkout():
    # Read-only source location; no subprocess or shared-worktree modification.
    marker = (TREE/".git").read_text().strip()
    need(marker.startswith("gitdir: "), "WORKTREE_GITDIR")
    gd = Path(marker[8:])
    if not gd.is_absolute():
        gd = TREE/gd
    head = (gd/"HEAD").read_text().strip()
    need(head == "ref: refs/heads/codex/ns-reverse", "REVERSE_BRANCH")
    common = (gd/(gd/"commondir").read_text().strip()).resolve()
    ref = "refs/heads/codex/ns-reverse"
    loose = common/ref
    if loose.exists():
        commit = loose.read_text().strip()
    else:
        records = [line.split() for line in (common/"packed-refs").read_text().splitlines()
                   if line and not line.startswith(("#", "^"))]
        matches = [items[0] for items in records if len(items) == 2 and items[1] == ref]
        need(len(matches) == 1, "UNIQUE_REVERSE_PACKED_REF")
        commit = matches[0]
    need(len(commit) == 40 and all(c in "0123456789abcdef" for c in commit), "SOURCE_COMMIT_FORMAT")
    return {"root": str(TREE), "branch": "codex/ns-reverse", "commit": commit,
            "method": "read-only worktree HEAD and loose/packed ref; no subprocess"}


def write_json(name, value, exclusive=False):
    path = OUT/name
    need(path.parent == OUT and (not exclusive or not path.exists()), "NO_OUTPUT_OVERWRITE")
    raw = canonical(value)
    if exclusive:
        with path.open("xb") as stream:
            stream.write(raw)
            stream.flush()
    else:
        temp = OUT/(name+".tmp")
        with temp.open("xb") as stream:
            stream.write(raw)
            stream.flush()
        temp.replace(path)
    need(path.read_bytes() == raw, "ACTUAL_RESULT_JSON_BYTE_READBACK")
    return {"file": name, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def exceeded(observation):
    return (observation["elapsed_seconds"] >= RESOURCE_LOCK["wall_seconds"]
            or observation["peak_rss_bytes"] > RESOURCE_LOCK["rss_bytes"]
            or observation["all_output_bytes"] > RESOURCE_LOCK["output_bytes"])


def alarm(signum, frame):
    raise LimitStop("COMPARISON_DEADLINE_OR_STOP_SIGNAL: "+str(signum))


def execute(info):
    OUT.mkdir(exist_ok=False)
    mon = Monitor()
    log = {"schema": "fixed-segment-full-comparison-run-v1", "status": "RUNNING",
           "producer_resource_complete": False, "resource_complete": False,
           "certificate_ready": False, "release_ready": False,
           "pid": os.getpid(), "started_at_utc": utc(), "source_sha256": info["source_sha256"],
           "config_sha256": info["config_sha256"], "preflight": info,
           "command": shlex.join(getattr(sys, "orig_argv", [sys.executable, *sys.argv])),
           "environment": {"python": sys.version,
                           "os_uname": {key: getattr(os.uname(), key) for key in
                                        ("sysname", "nodename", "release", "version", "machine")},
                           "logical_cpu_count": os.cpu_count(), "single_process": True,
                           "arithmetic": "standard-library exact integers/Fraction over existing data only"}}
    write_json("claim.json", log, exclusive=True)
    try:
        for sig in (signal.SIGALRM, signal.SIGTERM, signal.SIGINT):
            signal.signal(sig, alarm)
        remaining = RESOURCE_LOCK["wall_seconds"]-(time.monotonic()-START)
        if remaining <= 0:
            raise LimitStop("ENTRY_BUDGET_EXHAUSTED_BEFORE_COMPARISON")
        signal.setitimer(signal.ITIMER_REAL, remaining)
        log["checkout"] = checkout()
        source = Path(__file__).read_bytes()
        with (OUT/"source-snapshot.py").open("xb") as stream:
            stream.write(source)
        need((OUT/"source-snapshot.py").read_bytes() == source, "COMPARATOR_SOURCE_SNAPSHOT_READBACK")
        write_json("configuration.json", info, exclusive=True)
        mr, mp, ir, ip = archive_sources(mon)
        modes = read_modes()
        witness = {}
        tensor_count = compare_tensors(mon, witness)
        ws_count, aggregate = compare_vector_and_square(mon, witness)
        coefficient_counts = compare_coefficients(mon, witness, modes)
        bounds = compare_bounds(mon, mp, ip, aggregate, witness)
        source_name = "audit_one_segment_residual.py"
        source_witness = {"file": source_name, "sha256": mon.bindings[source_name]["sha256"],
                          "actual_file_byte_binding_completed": True}
        controls = mutation_controls(witness, source_witness)
        result = {"schema": "fixed-segment-complete-data-comparison-v1",
                  "status": SUCCESS,
                  "admission_requires_comparison_process_exit_zero_and_final_receipt": True,
                  "scope": "same fixed original Hermite segment [1280/2048,1281/2048] only; no NS/full-window conclusion",
                  "source_sha256": info["source_sha256"], "config_sha256": info["config_sha256"],
                  "checkout": log["checkout"], "counts": {"tensor_scalars": tensor_count,
                      "W_scalars": ws_count["W"], "S_scalars": ws_count["S"], **coefficient_counts},
                  "mapping": "D_j -> deltaT_jj; (D_jl-D_j-D_l)/2 -> deltaT_jl; all six time layers and full H",
                  "tensor_W_S_centers_original_coefficients": "ALL_SCALARS_EQUAL",
                  "norms_and_fixed_control_interface": bounds, "mutation_controls": controls,
                  "actual_nonzero_witnesses": witness, "bindings": mon.bindings,
                  "spatial_kernel_or_solver_invocations": 0, "independent_productions_repeated": 0,
                  "whole_W_square_recomputed": False,
                  "resource_complete": False, "certificate_ready": False, "release_ready": False,
                  "producer_resource_complete": False,
                  "producer_resource_evidence": "implicit platform helpers were not fully accounted; historical root resource PASS is not inherited",
                  "main_run_sha256": FIXED_PINS["one-segment-residual-trial-01/run.json"],
                  "independent_run_sha256": INDEPENDENT_FINAL_PINS["one-segment-residual-independent-trial-01/run.json"]}
        log["result"] = write_json("comparison.json", result, exclusive=True)
        mon.check("all complete data objects and actual mutations verified")
        # Re-read all source/input/archive bytes after validation, not merely cached hashes.
        for name, descriptor in mon.bindings.items():
            path = HERE/name
            validate_digest(file_sha(path), descriptor["sha256"], "final unchanged "+name)
            need(path.stat().st_size == descriptor["bytes"], "FINAL_SOURCE_SIZE_CHANGED")
            mon.check("final immutable archive byte bindings")
        validate_digest(file_sha(Path(__file__)), info["source_sha256"], "comparator source")
        review = info["runtime_root_source_review"]
        validate_digest(file_sha(review["path"]), review["sha256"], "root comparator source review")
        need(checkout() == log["checkout"], "COMPARATOR_SOURCE_COMMIT_CHANGED")
        log["status"] = SUCCESS
        log["resource_complete"] = False
        log["producer_resource_complete"] = False
        log["certificate_ready"] = False
        log["release_ready"] = False
        log["producer_resource_evidence_gap"] = True
        log["counts"] = result["counts"]
        log["actual_mutations_rejected"] = 7
        log["synthetic_boundary_mutations_rejected"] = 2
    except BaseException as error:
        signal.setitimer(signal.ITIMER_REAL, 0)
        log["status"] = "STOP" if isinstance(error, LimitStop) else "FAILED"
        log["error"] = {"type": type(error).__name__, "message": str(error), "stage": mon.stage}
        traceback.print_exc(file=sys.stderr)
        sys.stderr.flush()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        log["finished_at_utc"] = utc()
        log["resources_before_run_record_write"] = mon.observation()
        if exceeded(log["resources_before_run_record_write"]):
            log["status"] = "STOP"
        write_json("run.json", log)
        obs = mon.observation()
        if exceeded(obs):
            log["status"] = "STOP"
            log["final_budget_overrun"] = obs
            write_json("run.json", log)
    final = {"status": log["status"], "run_sha256": file_sha(OUT/"run.json"),
             "result": log.get("result"), "post_run_write_observation": mon.observation(),
             "resource_complete": False, "certificate_ready": False, "release_ready": False,
             "producer_resource_complete": False,
             "admission_also_requires": "process exit zero and matching final-receipt.json"}
    print(json.dumps(final, sort_keys=True), flush=True)
    sys.stderr.flush()
    receipt = {"schema": "fixed-segment-comparison-final-receipt-v1", "status": log["status"],
               "run_sha256": final["run_sha256"], "result": log.get("result"),
               "resource_complete": False, "certificate_ready": False, "release_ready": False,
               "producer_resource_complete": False,
               "observed_after_stdout_flush": mon.observation(),
               "external_stdio": {str(p): {"bytes": p.stat().st_size, "sha256": file_sha(p)} for p in (STDOUT, STDERR)},
               "receipt_bytes": 0, "all_output_bytes_including_receipt": 0}
    base = mon.observation()["all_output_bytes"]
    for _ in range(8):
        size = len(canonical(receipt))
        if size == receipt["receipt_bytes"]:
            break
        receipt["receipt_bytes"] = size
        receipt["all_output_bytes_including_receipt"] = base+size
    need(len(canonical(receipt)) == receipt["receipt_bytes"], "RECEIPT_SIZE_FIXED_POINT")
    write_json("final-receipt.json", receipt, exclusive=True)
    after = mon.observation()
    late_error = None
    if exceeded(after):
        log["status"] = "STOP"
        late_error = "FINAL_COMPARISON_BUDGET_OVERRUN"
    elif after["all_output_bytes"] != receipt["all_output_bytes_including_receipt"]:
        log["status"] = "FAILED"
        late_error = "FINAL_RECEIPT_OUTPUT_SIZE"
    elif after["peak_rss_bytes"] != receipt["observed_after_stdout_flush"]["peak_rss_bytes"]:
        log["status"] = "FAILED"
        late_error = "LATE_COMPARISON_PEAK_NOT_RECORDED_IN_RECEIPT"
    if late_error is not None:
        log["final_receipt_failure"] = {"reason": late_error, "actual_observation": after}
        write_json("run.json", log)
        print(json.dumps({"status": log["status"], "run_sha256": file_sha(OUT/"run.json"),
                          "invalidates_earlier_receipt": True, "resources": mon.observation(),
                          "producer_resource_complete": False, "resource_complete": False,
                          "certificate_ready": False, "release_ready": False}), flush=True)
        return 1
    return 0 if log["status"] == SUCCESS else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--run", action="store_true")
    mode.add_argument("--check-only", action="store_true")
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
    except (Exception, KeyboardInterrupt) as exc:
        traceback.print_exc(file=sys.stderr)
        sys.stderr.flush()
        print(json.dumps({"status": "ENTRY_OR_FINAL_RECORD_FAILED", "type": type(exc).__name__,
                          "message": str(exc), "complete_comparison_admitted": False,
                          "producer_resource_complete": False, "resource_complete": False,
                          "certificate_ready": False, "release_ready": False}), flush=True)
        raise SystemExit(1)
