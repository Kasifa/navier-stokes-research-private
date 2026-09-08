"""Fixed read-only comparison worker; never evolves a state or calls an FFT.

CLI: --run-id trajectory_comparison --output-dir ABS --source-lock ABS.
NumPy's first import, source/input hashing, all vector arithmetic and output are
inside this fifth scientific worker. Only Band is used from the reviewed kernel;
no trajectory or other scientific worker is imported. The separate supervisor
owns the unique invocation, whole-child 180-second timeout, 6-GiB posthoc RSS
and 64-MiB all-output acceptance. Failures/partial evidence are retained.

This author previously wrote the independent numerical reference without reading
the kernel. For this later comparison task, Band's coordinate projection was
read. This comparison is not a blind second numerical trajectory or an NS
error certificate. There are no fitted tolerances or convergence verdicts.
"""

import sys

sys.dont_write_bytecode = True

import time

PROCESS_START = time.monotonic()

import argparse
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import traceback
import zipfile


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = HERE.relative_to(ROOT).as_posix() + "/"
RUN_ID = "trajectory_comparison"
INPUT_SHA = "3f51705fbd934ce76d503c1c856566405ee3deb1760474b1c73ef6a6f481c61f"
CONTRACT_SHA = "0886f1f992e7a6285e02ffd3c48650dca197d9ced3c1f8bd21a021711307447b"
DRIVER_SCHEMA_SHA = "36d143eb65b267e890f37666ac0688963c0f0ed1d706f23b7923d7d652e173e7"
KERNEL_SHA = "1b29e919cf5faefe1e4a5193fee0f7e0fdd11901d8aed7b3e5ade752cd23f175"
OUTPUT_LIMIT = 64 * 1024**2
SPECS = {
    "trajectory128_256": (128, 42, 256, 900, 2 * 1024**3),
    "trajectory160_256": (160, 53, 256, 1500, 3 * 1024**3),
    "trajectory128_512": (128, 42, 512, 1800, 4 * 1024**3),
    "trajectory160_512": (160, 53, 512, 3000, 5 * 1024**3),
}
GROUPS = (
    ("time_128", "trajectory128_256", "trajectory128_512", "TIME", 2),
    ("time_160", "trajectory160_256", "trajectory160_512", "TIME", 2),
    ("space_256", "trajectory128_256", "trajectory160_256", "SPACE", 1),
    ("space_512", "trajectory128_512", "trajectory160_512", "SPACE", 1),
)
REQUIRED = {PREFIX + name for name in (
    "compare_trajectories.py", "trajectory_driver.py", "run_trajectory.py",
    "numerical_kernel.py", "TRAJECTORY_CONTRACT.md", "TRAJECTORY_CONTRACT_DRAFT.md",
    "input-preparation.json", "input-acceptance.json", "numerical-acceptance.json",
    "numerical-source-lock.json", "run_numerical.py", "numerical_experiment.py",
    "numerical_reference.py", "NUMERICAL_EXECUTION_CONTRACT.md")}
VECTOR_NAMES = ("U", "G", "W", "h0", "h1", "h2", "e1", "e2")
NORM_NAMES = ("h0", "h1", "h2", "G", "W", "e1", "e2")
NPZ_KEYS = {"U", "G", "W", "band1_modes", "band2_modes", "metadata_json"}
COMPACT_SCALARS = (
    "a0", "mean_hermitian_norm", "divergence_max_abs",
    "conjugacy_component_max_abs", "c3_component_max_abs", "max_component_abs",
    "divergence_normalized", "conjugacy_normalized", "c3_normalized")
U_SCALARS = COMPACT_SCALARS + (
    "energy_normalized", "viscous_dissipation_normalized", "off_cube_a0", "cube_face_a0")
np = None


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, name, minimum=0):
    require(type(value) is int and value >= minimum, name + ": integer range")
    return value


def finite_scalar(value, name):
    require(type(value) in (int, float) and math.isfinite(value), name + ": nonfinite/non-number")
    return value


def finite_tree(value, name):
    if isinstance(value, dict):
        for key, item in value.items():
            finite_tree(item, name + "." + key)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            finite_tree(item, name + "[" + str(index) + "]")
    elif type(value) is float:
        require(math.isfinite(value), name + ": nonfinite JSON float")
    elif value is not None:
        require(type(value) in (str, bool, int), name + ": unsupported JSON value")


def reject_constant(value):
    raise ValueError("nonfinite JSON constant: " + value)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key: " + key)
        result[key] = value
    return result


def decode_json(raw):
    result = json.loads(raw, parse_constant=reject_constant, object_pairs_hook=unique_object)
    finite_tree(result, "JSON")
    return result


def encode_json(value):
    finite_tree(value, "output")
    return (json.dumps(value, sort_keys=True, ensure_ascii=True, allow_nan=False,
                       separators=(",", ":")) + "\n").encode("ascii")


def file_record(path):
    require(path.is_absolute() and path.resolve(strict=True) == path and path.is_file(),
            "input must be a regular absolute non-symlink file: " + str(path))
    digest, size = hashlib.sha256(), 0
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            size += len(chunk)
            digest.update(chunk)
    return {"bytes": size, "sha256": digest.hexdigest()}


def safe_relative(name):
    require(isinstance(name, str) and bool(name) and "\\" not in name, "relative path text")
    relative = PurePosixPath(name)
    require(not relative.is_absolute() and ".." not in relative.parts
            and relative.as_posix() == name, "unnormalized relative path")
    return name


class Inputs:
    """Whole-file start fingerprints, never scientific arrays."""

    def __init__(self):
        self.records = {}
        self.line_positions = {}

    def check(self, path, expected=None):
        current = file_record(path)
        if expected is not None:
            require(current == expected, "input bytes/SHA mismatch: " + str(path))
        if path in self.records:
            require(current == self.records[path], "input changed: " + str(path))
        else:
            self.records[path] = current
        return current

    def json(self, path):
        self.check(path)
        return decode_json(path.read_bytes())

    def jsonl(self, path):
        self.check(path)
        require(path.stat().st_size <= OUTPUT_LIMIT, "node/index JSONL exceeds 64 MiB")
        values, positions = [], [0]
        with path.open("rb") as handle:
            for line in handle:
                require(bool(line.strip()), "blank JSONL record")
                values.append(decode_json(line))
                positions.append(positions[-1] + len(line))
        self.line_positions[path] = positions
        return values

    def finish(self):
        rows = []
        for path in sorted(self.records):
            current = file_record(path)
            require(current == self.records[path], "final input bytes changed: " + str(path))
            rows.append({"path": path.relative_to(ROOT).as_posix(), **current})
        return rows


def load_sources(path, inputs):
    record = inputs.check(path)
    lock = inputs.json(path)
    require(type(lock.get("schema")) is int and lock["schema"] == 1, "source-lock schema")
    bindings = lock.get("bindings")
    require(isinstance(bindings, list) and bool(bindings), "source-lock bindings")
    expected = {}
    for item in bindings:
        name, digest = safe_relative(item["path"]), item["sha256"]
        require(name not in expected and isinstance(digest, str)
                and re.fullmatch(r"[0-9a-f]{64}", digest), "source binding identity")
        expected[name] = digest
    require(REQUIRED <= set(expected), "source-lock missing required bindings")
    require(expected[PREFIX + "input-preparation.json"] == INPUT_SHA, "original input binding")
    require(expected[PREFIX + "TRAJECTORY_CONTRACT.md"] == CONTRACT_SHA, "final contract binding")
    require(expected[PREFIX + "trajectory_driver.py"] == DRIVER_SCHEMA_SHA, "reviewed driver schema binding")
    require(expected[PREFIX + "numerical_kernel.py"] == KERNEL_SHA, "reviewed Band kernel binding")
    records = {}
    for name, digest in expected.items():
        current = inputs.check(ROOT / name)
        require(current["sha256"] == digest, "source SHA mismatch: " + name)
        records[name] = current
    return record["sha256"], expected, records


def fraction(value, name):
    require(isinstance(value, dict) and set(value) == {"numerator", "denominator"},
            name + ": fraction schema")
    n, d = value["numerator"], value["denominator"]
    require(isinstance(n, str) and re.fullmatch(r"-?(0|[1-9][0-9]*)", n)
            and isinstance(d, str) and re.fullmatch(r"[1-9][0-9]*", d), name + ": fraction text")
    result = Fraction(int(n), int(d))
    require(str(result.numerator) == n and str(result.denominator) == d,
            name + ": fraction must be canonical")
    return result


def qrecord(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def check_float_record(record, exact, name):
    require(isinstance(record, dict), name + ": missing time record")
    require(fraction(record["exact"], name + ".exact") == exact, name + ": exact time")
    hexadecimal = record["float_hex"]
    require(isinstance(hexadecimal, str), name + ": float hex type")
    converted = float.fromhex(hexadecimal)
    require(math.isfinite(converted) and converted.hex() == hexadecimal
            and float(exact).hex() == hexadecimal, name + ": binary64 conversion")
    readback = Fraction.from_float(converted)
    require(fraction(record["readback"], name + ".readback") == readback, name + ": readback")
    error = readback - exact
    require(fraction(record["signed_conversion_error"], name + ".signed") == error
            and fraction(record["absolute_conversion_error"], name + ".absolute") == abs(error),
            name + ": conversion error")
    return converted


def check_time(record, j, m, T, name):
    exact = Fraction(j, m) * T
    check_float_record(record, exact, name)
    accumulated = j * Fraction.from_float(float(T / m))
    require(fraction(record["step_accumulation_exact"], name + ".accumulation") == accumulated,
            name + ": step accumulation")
    require(fraction(record["step_accumulation_signed_error"], name + ".accumulation_signed")
            == accumulated - exact, name + ": accumulation signed error")
    require(fraction(record["step_accumulation_absolute_error"], name + ".accumulation_absolute")
            == abs(accumulated - exact), name + ": accumulation absolute error")
    return exact


def expected_completion(m):
    return {"completed_steps": m, "expected_steps": m, "checkpoint_count": m // 32 + 1,
            "node_count": m + 1, "fft_batched_api_calls": 36 * m,
            "fft_scalar_3d_transforms": 108 * m}


def check_source_rows(rows, expected, source_records):
    require(isinstance(rows, list) and len(rows) == len(expected), "receipt source rows count")
    seen = set()
    for item in rows:
        name = item["path"]
        require(name in expected and name not in seen, "receipt source path coverage")
        seen.add(name)
        require(item.get("match") is True and item.get("expected_sha256") == expected[name]
                and item.get("sha256") == expected[name]
                and item.get("bytes") == source_records[name]["bytes"], "receipt source binding")
    require(seen == set(expected), "receipt source map incomplete")


def inventory(directory, inputs):
    require(directory.resolve(strict=True) == directory and directory.is_dir(), "run directory path")
    rows = []
    for path in sorted(directory.rglob("*")):
        require(not path.is_symlink(), "symlink in trajectory artifacts")
        if path.is_dir():
            continue
        require(path.is_file(), "non-file trajectory artifact")
        name = path.relative_to(directory).as_posix()
        if name != "execution.json":
            rows.append({"path": name, **inputs.check(path)})
    return rows


def check_trajectory_receipt(run_id, lock_sha, expected, source_records, inputs):
    N, K, m, seconds, max_output = SPECS[run_id]
    directory = HERE / "numerical-runs" / run_id
    receipt_path = directory / "execution.json"
    receipt = inputs.json(receipt_path)
    result = inputs.json(directory / "result.json")
    for record in (receipt, result):
        require(record.get("status") == "PASS" and record.get("run_id") == run_id
                and record.get("source_lock_sha256") == lock_sha, "trajectory identity/PASS/lock")
    require(receipt.get("worker_output_status") == "PASS"
            and type(receipt.get("returncode")) is int and receipt["returncode"] == 0
            and receipt.get("child_reaped") is True and receipt.get("timed_out") is False
            and type(receipt.get("scientific_execution_count")) is int
            and receipt["scientific_execution_count"] == 1
            and receipt.get("sources_unchanged") is True
            and receipt.get("worker_identity_and_source_maps_match") is True
            and receipt.get("worker_completion_counts_match") is True
            and receipt.get("non_output_gates_pass") is True, "trajectory completion/identity gate")
    require(receipt.get("source_lock_after_sha256") == lock_sha, "receipt final lock")
    check_source_rows(receipt["sources_before"], expected, source_records)
    check_source_rows(receipt["sources_after"], expected, source_records)
    require(result.get("source_hashes_start") == expected and result.get("source_hashes_end") == expected,
            "worker start/end source maps")
    require(integer(result.get("pid"), "worker pid", 1) == receipt["pid"]
            and integer(result.get("supervisor_pid"), "parent pid", 1)
            == receipt["supervisor_runtime"]["pid"]
            and integer(result.get("scientific_worker_invocations"), "worker invocations", 1) == 1,
            "worker process identity")
    counts = expected_completion(m)
    for key, value in counts.items():
        require(type(result.get(key)) is int and result[key] == value, "trajectory count: " + key)
    require(receipt["worker_completion_counts"] == counts, "receipt completion count map")
    for key, value in (("N", N), ("K", K), ("m", m)):
        require(type(result.get(key)) is int and result[key] == value, "trajectory result " + key)
    require(result.get("input_sha256") == INPUT_SHA and result.get("completion_verified") is True,
            "same original input and completed driver")
    require(result.get("loop_and_checkpoint_coverage_verified") is True
            and result.get("classification") == "EXPLORATORY_FINITE_GALERKIN_TRAJECTORY_NOT_TRUE_NS_GATES"
            and result.get("actual_NS_existence_to_T_certified") is False
            and result.get("actual_NS_source_gates_certified") is False
            and result.get("energy_quadrature_performed") is False
            and result.get("automatic_resume_or_retry") is False, "trajectory scope labels")
    budget = {"seconds": seconds, "rss_bytes": 6 * 1024**3, "output_bytes": max_output}
    require(receipt["budget"] == budget and receipt["budget_pass"] == {
        "wall_time": True, "rss": True, "output_bytes": True}, "trajectory resource acceptance")
    wall = finite_scalar(receipt["child_wall_seconds"], "child wall")
    usage = receipt["children_after_reap"]
    rss = integer(usage["peak_rss_bytes"], "child peak RSS")
    require(0 <= wall <= seconds and rss <= budget["rss_bytes"], "actual resource bounds")
    require(receipt["supervisor_runtime"]["platform"] == "darwin"
            and usage["ru_maxrss_unit"] == "bytes" and usage["ru_maxrss_raw"] == rss,
            "Darwin CHILDREN RSS units")
    previous = receipt["children_before"]
    require(previous["user_seconds"] == 0 and previous["system_seconds"] == 0
            and previous["ru_maxrss_raw"] == 0, "fresh trajectory supervisor")
    current = inventory(directory, inputs)
    require(current == receipt["artifact_inventory_before_receipt"], "trajectory artifact inventory")
    total = sum(item["bytes"] for item in current) + inputs.records[receipt_path]["bytes"]
    require(total == receipt["output_total_bytes_including_execution_receipt"]
            and total <= max_output, "trajectory total output bytes")
    names = {item["path"] for item in current}
    require({"result.json", "nodes.jsonl", "checkpoints.jsonl", "stdout.log", "stderr.log"} <= names,
            "required trajectory artifacts missing")
    return {"id": run_id, "N": N, "K": K, "m": m, "directory": directory,
            "result": result, "receipt": receipt,
            "artifact_map": {item["path"]: {"bytes": item["bytes"], "sha256": item["sha256"]}
                             for item in current},
            "receipt_evidence": {"run_id": run_id, "execution": inputs.records[receipt_path],
                                 "result": inputs.records[directory / "result.json"],
                                 "counts": counts, "child_wall_seconds": wall,
                                 "child_peak_rss_bytes": rss, "output_bytes": total}}


def array_finite(value, name):
    require(bool(np.isfinite(value).all()), name + ": nonfinite array")


def mode_norms(field):
    # Hermitian norm per Fourier mode; no bilinear dot or real projection.
    value = np.sqrt(np.sum(np.abs(field)**2, axis=0, dtype=np.float64))
    array_finite(value, "Hermitian mode norms")
    return value


def a0(field):
    result = float(np.sum(mode_norms(field), dtype=np.float64))
    finite_scalar(result, "A0")
    return result


def component_max(field):
    result = 0.0 if field.size == 0 else float(np.max(np.abs(field)))
    finite_scalar(result, "max complex component")
    return result


def compare_vector(left, right):
    require(left.shape == right.shape, "vector shapes differ")
    array_finite(left, "left vector")
    array_finite(right, "right vector")
    difference = left - right
    left_a0, right_a0, delta_a0 = a0(left), a0(right), a0(difference)
    denominator = max(left_a0, right_a0)
    relative = None if denominator == 0.0 else delta_a0 / denominator
    if relative is not None:
        finite_scalar(relative, "relative A0 difference")
    return {"left_A0": left_a0, "right_A0": right_a0, "difference_A0": delta_a0,
            "difference_max_component_abs": component_max(difference),
            "relative_difference_A0": relative,
            "relative_status": "BOTH_ZERO_FLOAT" if denominator == 0.0 else "DEFINED_FLOAT",
            "left_nonzero_float": bool(np.any(left != 0)),
            "right_nonzero_float": bool(np.any(right != 0))}


def geometry(N, K):
    axis = np.arange(N, dtype=np.int64)
    axis[axis >= N // 2] -= N
    absolute = np.abs(axis)
    maximum = np.maximum(np.maximum(absolute[:, None, None], absolute[None, :, None]),
                         absolute[None, None, :])
    return {"outside": maximum > K, "shell": (maximum > 42) & (maximum <= 53),
            "common_indices": np.arange(-42, 43, dtype=np.int64) % N}


def common_cube(field, indices):
    return field[:, indices[:, None, None], indices[None, :, None], indices[None, None, :]]


def projected_vectors(state, bands):
    U, G, W = state["U"], state["G"], state["W"]
    h0, h1, h2 = (band.gather(U) for band in bands)
    require(G.shape == h1.shape and W.shape == h2.shape, "history and projected band shapes")
    return {"U": U, "G": G, "W": W, "h0": h0, "h1": h1, "h2": h2,
            "e1": h1 - G, "e2": h2 - W}


def scalar_difference(left, right):
    if left is None or right is None:
        return {"left": left, "right": right, "signed_difference": None,
                "absolute_difference": None,
                "status": "BOTH_NULL" if left is None and right is None else "ONE_NULL"}
    finite_scalar(left, "left recorded scalar")
    finite_scalar(right, "right recorded scalar")
    difference = left - right
    finite_scalar(difference, "recorded scalar difference")
    return {"left": left, "right": right, "signed_difference": difference,
            "absolute_difference": abs(difference), "status": "DEFINED_FLOAT"}


class Outputs:
    def __init__(self, directory):
        self.directory = directory
        self.progress_handle = (directory / "progress.jsonl").open("xb")

    def progress(self, **fields):
        record = {"elapsed_seconds": time.monotonic() - PROCESS_START, **fields}
        self.progress_handle.write(encode_json(record))
        self.progress_handle.flush()

    def write(self, name, value):
        raw = encode_json(value)
        require(len(raw) <= OUTPUT_LIMIT, "single JSON exceeds output budget")
        path = self.directory / name
        with path.open("xb") as handle:
            handle.write(raw)
            handle.flush()
        return file_record(path)

    def close(self):
        self.progress_handle.close()


def expected_normalization(K):
    return {"dtype": "complex128", "component_axis": 0, "fft_norm": "forward",
            "frequency_order": "signed_numpy_fft", "retained_cube": K,
            "band_order": "lexicographic_all_signed_integer_modes",
            "a0": "sum_hermitian_mode_norms", "energy": "normalized_fourier_half_l2_squared",
            "viscosity": 1}


def check_fft_counts(counts, j, N):
    require(isinstance(counts, dict), "FFT count map")
    expected = {}
    for size in (32, 64, N):
        for direction, batches in (("ifftn", 8 * j), ("fftn", 4 * j)):
            key = direction + ":" + "x".join((str(size),) * 3)
            expected[key] = {"batched_api_calls": batches, "scalar_3d_transforms": 3 * batches}
    # Driver schema includes the six zero entries also at accepted index zero.
    require(counts == expected, "per-grid completed FFT counts")
    for item in counts.values():
        for value in item.values():
            integer(value, "FFT counter")


def check_metadata(meta, run, j, T, lock_sha):
    require(isinstance(meta, dict) and type(meta.get("schema")) is int and meta["schema"] == 1,
            "checkpoint metadata schema")
    for key, value in (("N", run["N"]), ("K", run["K"]), ("m", run["m"]), ("j", j)):
        require(type(meta.get(key)) is int and meta[key] == value, "checkpoint identity " + key)
    require(meta.get("run_id") == run["id"] and meta.get("input_sha256") == INPUT_SHA
            and meta.get("source_lock_sha256") == lock_sha, "checkpoint source identity")
    m = run["m"]
    check_float_record(meta["T"], T, "checkpoint T")
    check_float_record(meta["a"], T / 2, "checkpoint a")
    check_float_record(meta["h"], T / m, "checkpoint h")
    exact = check_time(meta["time"], j, m, T, "checkpoint time")
    require(meta["time"] == run["nodes"][j]["time"], "checkpoint/node time record differs")
    require(integer(meta["next_index"], "next_index") == j, "next accepted index")
    reset = meta["half_reset"]
    expected_reset = {"count": int(j > m // 2), "performed": j > m // 2,
                      "due_at_next_step": j == m // 2,
                      "next_phase": None if j == m else int(j >= m // 2)}
    require(reset == expected_reset, "half reset/next-phase metadata")
    require(type(reset["count"]) is int and type(reset["performed"]) is bool
            and type(reset["due_at_next_step"]) is bool, "half reset types")
    counters = meta["counters"]
    require(set(counters) == {"accepted_steps", "rhs_calls", "fft_counts"}
            and integer(counters["accepted_steps"], "accepted steps") == j
            and integer(counters["rhs_calls"], "rhs calls") == 4 * j, "checkpoint counters")
    check_fft_counts(counters["fft_counts"], j, run["N"])
    require(meta["normalization"] == expected_normalization(run["K"]), "checkpoint normalization")
    positions = meta["journal_positions_before_checkpoint"]
    require(set(positions) == {"counts", "bytes"}, "checkpoint journal metadata")
    for kind in ("counts", "bytes"):
        require(set(positions[kind]) == {"nodes.jsonl", "progress.jsonl", "checkpoints.jsonl"},
                "checkpoint journal paths")
    for name, prefix in run["journal_positions"].items():
        count = integer(positions["counts"][name], "journal prefix count")
        size = integer(positions["bytes"][name], "journal prefix bytes")
        require(count < len(prefix) and prefix[count] == size, "journal prefix boundary")
    require(positions["counts"]["nodes.jsonl"] == j + 1
            and positions["counts"]["checkpoints.jsonl"] == j // 32,
            "checkpoint journal before-index position")
    return exact


def check_diagnostics(record, scalar_names, name):
    require(isinstance(record, dict) and set(record) == set(scalar_names) | {"finite", "scale"},
            name + ": diagnostic keys")
    require(record["finite"] is True, name + ": finite flag")
    for key in scalar_names:
        require(finite_scalar(record[key], name + "." + key) >= 0, name + ": negative magnitude")
    scale = record["scale"]
    require(isinstance(scale, dict)
            and set(scale) == {"coefficient", "frequency", "frequency_domain"}, name + ": scale schema")
    require(finite_scalar(scale["coefficient"], name + ".scale.coefficient") >= 0
            and finite_scalar(scale["frequency"], name + ".scale.frequency") >= 0
            and isinstance(scale["frequency_domain"], str) and bool(scale["frequency_domain"]),
            name + ": scale values")
    require(scale["frequency_domain"] == ("retained_cube" if name == "U" else "complete_band"),
            name + ": frequency-domain label")


def check_gate_flags(node, j, m):
    applicable = j >= m // 2
    first_nonpositive = node["F1"] <= 0 if applicable else None
    second_nonpositive = node["F2"] <= 0 if applicable else None
    nonzero = node["nonzero_float"]
    first_nonzero = (nonzero["G"] and nonzero["h1"]) if applicable else None
    second_nonzero = (nonzero["W"] and nonzero["h2"]) if applicable else None
    expected = {
        "first_contract_applicable": applicable,
        "second_contract_endpoint_applicable": j == m,
        "second_window_started": applicable,
        "first_sampled_nonpositive": first_nonpositive,
        "second_sampled_nonpositive": second_nonpositive,
        "first_source_target_nonzero_float": first_nonzero,
        "second_source_target_nonzero_float": second_nonzero,
        "first_sampled_conditions_met": (first_nonpositive and first_nonzero) if applicable else None,
        "second_sampled_conditions_met": (second_nonpositive and second_nonzero) if applicable else None,
    }
    require(isinstance(node["gate_flags"], dict) and node["gate_flags"] == expected,
            "stored sampled/applicability flags inconsistent")
    for key, value in node["gate_flags"].items():
        require(value is None or type(value) is bool, "sampled flag type: " + key)
    require(node["e2_scope"] == ("NUMERICAL_POST_SOURCE_WINDOW" if applicable else "PRE_SOURCE_WINDOW"),
            "e2 applicability label")


def load_indices(run, inputs, T):
    m = run["m"]
    nodes = inputs.jsonl(run["directory"] / "nodes.jsonl")
    require(len(nodes) == m + 1, "all accepted nodes must be present")
    for j, node in enumerate(nodes):
        require(isinstance(node, dict) and set(node) == {
            "j", "m", "time", "norms", "F1", "F2", "U", "G", "W", "nonzero_float",
            "gate_flags", "e2_scope"},
            "node schema")
        require(type(node["j"]) is int and node["j"] == j
                and type(node["m"]) is int and node["m"] == m, "accepted node index")
        check_time(node["time"], j, m, T, "accepted node time")
        require(isinstance(node["norms"], dict) and set(node["norms"]) == set(NORM_NAMES),
                "all seven recorded norms")
        for name, value in node["norms"].items():
            require(finite_scalar(value, "norm " + name) >= 0, "negative stored A0")
        check_diagnostics(node["U"], U_SCALARS, "U")
        check_diagnostics(node["G"], COMPACT_SCALARS, "G")
        check_diagnostics(node["W"], COMPACT_SCALARS, "W")
        finite_scalar(node["F1"], "F1")
        if j < m // 2:
            require(node["F2"] is None, "F2 must be null before source window")
        else:
            finite_scalar(node["F2"], "F2")
        nonzero = node["nonzero_float"]
        require(isinstance(nonzero, dict) and set(nonzero) == set(VECTOR_NAMES),
                "nonzero float labels coverage")
        for name in VECTOR_NAMES:
            # Producer labels componentwise any(field != 0), not A0 != 0:
            # very small nonzero components could underflow in a squared norm.
            require(type(nonzero[name]) is bool, "nonzero floating label type")
        check_gate_flags(node, j, m)
    run["nodes"] = nodes
    rows = inputs.jsonl(run["directory"] / "checkpoints.jsonl")
    expected_indices = tuple(range(0, m + 1, 32))
    require(len(rows) == len(expected_indices), "checkpoint index count")
    checkpoints, seen_files = {}, set()
    for row, j in zip(rows, expected_indices):
        require(isinstance(row, dict) and set(row) == {"j", "file", "bytes", "sha256"}
                and type(row["j"]) is int and row["j"] == j, "checkpoint index sequence/schema")
        name = safe_relative(row["file"])
        require(name not in seen_files and name.endswith(".npz"), "checkpoint filename identity")
        seen_files.add(name)
        record = {"bytes": integer(row["bytes"], "checkpoint bytes", 1), "sha256": row["sha256"]}
        require(record == run["artifact_map"].get(name), "checkpoint receipt/index binding")
        require(record["bytes"] <= (128 if run["N"] == 128 else 224) * 1024**2,
                "per-checkpoint byte limit")
        checkpoints[j] = {"path": run["directory"] / name, "record": record}
    require(seen_files == {name for name in run["artifact_map"] if name.endswith(".npz")},
            "unindexed/missing checkpoint archive")
    require({0, m // 2, m} <= set(checkpoints), "checkpoint 0/a/T coverage")
    run["checkpoints"] = checkpoints
    run["loaded_checkpoints"] = set()
    result = run["result"]
    check_float_record(result["T"], T, "result T")
    check_float_record(result["a"], T / 2, "result a")
    check_float_record(result["h"], T / m, "result h")
    require(result["normalization"] == expected_normalization(run["K"]), "result normalization")
    for label, j in (("initial", 0), ("half", m // 2), ("final", m)):
        require(result[label + "_node"] == nodes[j], "result accepted-node copy differs")
    artifacts = result["artifacts"]
    require(artifacts["nodes"] == "nodes.jsonl" and artifacts["progress"] == "progress.jsonl"
            and artifacts["checkpoints_index"] == "checkpoints.jsonl"
            and artifacts["checkpoints"] == rows, "result artifact index")
    for label, j in (("initial", 0), ("half", m // 2), ("final", m)):
        require(artifacts[label + "_checkpoint"] == rows[j // 32], "result checkpoint copy differs")
    progress = inputs.jsonl(run["directory"] / "progress.jsonl")
    require(bool(progress), "missing progress records")
    run["journal_positions"] = {}
    for name in ("nodes.jsonl", "progress.jsonl", "checkpoints.jsonl"):
        positions = inputs.line_positions[run["directory"] / name]
        require(type(result["journal_counts"][name]) is int
                and result["journal_counts"][name] == len(positions) - 1
                and type(result["journal_bytes"][name]) is int
                and result["journal_bytes"][name] == positions[-1], "final journal count/bytes")
        run["journal_positions"][name] = positions
    require(integer(result["rhs_calls"], "final rhs calls") == 4 * m
            and integer(result["half_reset_count"], "final reset count") == 1,
            "completed callbacks/reset")
    check_fft_counts(result["fft_counts"], m, run["N"])


def archive_headers(path, run, bands):
    expected = {"U": ((3, run["N"], run["N"], run["N"]), np.dtype("complex128")),
                "G": ((3, bands[1].size), np.dtype("complex128")),
                "W": ((3, bands[2].size), np.dtype("complex128")),
                "band1_modes": ((bands[1].size, 3), np.dtype("int64")),
                "band2_modes": ((bands[2].size, 3), np.dtype("int64"))}
    headers = {}
    with zipfile.ZipFile(path, "r") as archive:
        members = archive.infolist()
        require(len(members) == len(NPZ_KEYS)
                and {item.filename for item in members} == {key + ".npy" for key in NPZ_KEYS},
                "NPZ must contain exactly six named NPY members")
        for item in members:
            require(not item.is_dir() and not (item.flag_bits & 1), "invalid/encrypted archive member")
            key = item.filename[:-4]
            with archive.open(item, "r") as handle:
                version = np.lib.format.read_magic(handle)
                if version == (1, 0):
                    shape, fortran, dtype = np.lib.format.read_array_header_1_0(handle)
                elif version == (2, 0):
                    shape, fortran, dtype = np.lib.format.read_array_header_2_0(handle)
                else:
                    raise ValueError("unexpected NPY format version")
                header_bytes = handle.tell()
            require(not dtype.hasobject and type(fortran) is bool, "NPY object/order header")
            if key == "metadata_json":
                require(shape == () and dtype.kind == "U" and 0 < dtype.itemsize <= OUTPUT_LIMIT,
                        "metadata_json must be scalar bounded Unicode")
            else:
                require((shape, dtype) == expected[key], "checkpoint dtype/shape: " + key)
            elements = math.prod(shape)
            require(item.file_size == header_bytes + elements * dtype.itemsize,
                    "NPY uncompressed size/header mismatch")
            headers[key] = {"shape": list(shape), "dtype": dtype.str, "fortran_order": fortran}
    return headers


def load_checkpoint(run, j, bands, T, lock_sha, inputs):
    item = run["checkpoints"][j]
    path = item["path"]
    inputs.check(path, item["record"])
    headers = archive_headers(path, run, bands)  # No array payload is loaded before headers.
    with np.load(path, allow_pickle=False) as archive:
        require(set(archive.files) == NPZ_KEYS, "NPZ key map changed")
        raw_metadata = archive["metadata_json"]
        require(raw_metadata.shape == () and raw_metadata.dtype.kind == "U", "metadata payload type")
        meta = decode_json(raw_metadata.item())
        exact = check_metadata(meta, run, j, T, lock_sha)
        for key, band in (("band1_modes", bands[1]), ("band2_modes", bands[2])):
            modes = archive[key]
            require(modes.dtype == np.dtype("int64") and modes.shape == band.modes.shape
                    and np.array_equal(modes, band.modes), "complete lexicographic band mode ordering")
        state = {}
        for key in ("U", "G", "W"):
            value = archive[key]
            require(value.dtype == np.dtype("complex128")
                    and list(value.shape) == headers[key]["shape"], "state payload dtype/shape")
            array_finite(value, key)
            state[key] = value
    run["loaded_checkpoints"].add(j)
    return state, {"run_id": run["id"], "j": j, "time_exact": qrecord(exact),
                   "file": path.relative_to(ROOT).as_posix(), **item["record"], "headers": headers}


class FFTGuard:
    """Fail closed on every public NumPy FFT transform entry point."""

    def __init__(self):
        self.attempted_api_calls = 0
        self.completed_api_calls = 0
        self.completed_scalar_3d_transforms = 0
        self.installed = {}
        for name in ("fft", "ifft", "fft2", "ifft2", "fftn", "ifftn", "rfft", "irfft",
                     "rfft2", "irfft2", "rfftn", "irfftn", "hfft", "ihfft"):
            require(callable(getattr(np.fft, name)), "FFT guard entry point missing")
            def prohibited(*args, _name=name, **kwargs):
                self.attempted_api_calls += 1
                raise RuntimeError("FFT prohibited in comparison worker: " + _name)
            self.installed[name] = prohibited
            setattr(np.fft, name, prohibited)

    def finish(self):
        require(all(getattr(np.fft, name) is function for name, function in self.installed.items()),
                "FFT guards changed")
        require(self.attempted_api_calls == 0, "FFT call attempted during comparison")
        return {"attempted_api_calls": self.attempted_api_calls,
                "completed_batched_api_calls": self.completed_api_calls,
                "completed_scalar_3d_transforms": self.completed_scalar_3d_transforms,
                "guarded_entry_points": sorted(self.installed)}


def compare_scalar_nodes(left, right, j, k, T, group):
    a, b = left["nodes"][j], right["nodes"][k]
    exact_a, exact_b = Fraction(j, left["m"]) * T, Fraction(k, right["m"]) * T
    require(exact_a == exact_b, "scalar common nodes are not the same exact time")
    scalars = {}
    for name in NORM_NAMES:
        scalars["A0." + name] = scalar_difference(a["norms"][name], b["norms"][name])
    for name in ("F1", "F2"):
        scalars[name] = scalar_difference(a[name], b[name])
    for name in U_SCALARS:
        scalars["U." + name] = scalar_difference(a["U"][name], b["U"][name])
    for name in ("coefficient", "frequency"):
        scalars["U.scale." + name] = scalar_difference(
            a["U"]["scale"][name], b["U"]["scale"][name])
    require(a["e2_scope"] == b["e2_scope"], "common-time e2 scope differs")
    return {"group": group, "left_run": left["id"], "right_run": right["id"],
            "left_j": j, "right_j": k, "time_exact": qrecord(exact_a),
            "left_time_float_hex": a["time"]["float_hex"],
            "right_time_float_hex": b["time"]["float_hex"], "scalars": scalars,
            "left_gate_flags": a["gate_flags"], "right_gate_flags": b["gate_flags"],
            "left_nonzero_float": a["nonzero_float"], "right_nonzero_float": b["nonzero_float"],
            "left_U_finite": a["U"]["finite"], "right_U_finite": b["U"]["finite"],
            "left_U_frequency_domain": a["U"]["scale"]["frequency_domain"],
            "right_U_frequency_domain": b["U"]["scale"]["frequency_domain"],
            "e2_scope": a["e2_scope"],
            "interpretation": "RECORDED_SAMPLES_ONLY_NO_CONVERGENCE_OR_TRUE_NS_GATE"}


def compare_checkpoint_pair(left, right, j, k, kind, group, bands, geometries,
                            T, lock_sha, inputs):
    # State ownership is local to this function: neither caller nor outputs
    # retain U/G/W arrays after this single pair has been converted to scalars.
    state_a, evidence_a = load_checkpoint(left, j, bands, T, lock_sha, inputs)
    state_b, evidence_b = load_checkpoint(right, k, bands, T, lock_sha, inputs)
    require(evidence_a["time_exact"] == evidence_b["time_exact"], "checkpoint common exact time")
    vectors_a, vectors_b = projected_vectors(state_a, bands), projected_vectors(state_b, bands)
    for vectors, run, index in ((vectors_a, left, j), (vectors_b, right, k)):
        for name in VECTOR_NAMES:
            require(bool(np.any(vectors[name] != 0)) == run["nodes"][index]["nonzero_float"][name],
                    "checkpoint componentwise nonzero label differs from node")
    grid_a, grid_b = geometries[left["N"]], geometries[right["N"]]
    U_a, U_b = state_a["U"], state_b["U"]
    domains = {"left_full_grid_A0": a0(U_a), "right_full_grid_A0": a0(U_b),
               "left_outside_own_retained_cube_A0": a0(U_a[:, grid_a["outside"]]),
               "right_outside_own_retained_cube_A0": a0(U_b[:, grid_b["outside"]]),
               "left_retained_K": left["K"], "right_retained_K": right["K"]}
    if kind == "SPACE":
        require(left["N"] == 128 and right["N"] == 160, "fixed spatial orientation")
        vectors_a["U"] = common_cube(U_a, grid_a["common_indices"])
        vectors_b["U"] = common_cube(U_b, grid_b["common_indices"])
        shell = U_b[:, grid_b["shell"]]
        norms = mode_norms(shell)
        domains.update(
            U_comparison_domain="COMMON_SIGNED_CUBE",
            common_signed_cube_axis_min=-42, common_signed_cube_axis_max=42,
            right_retained_shell="42 < max(abs(k_i)) <= 53",
            right_retained_shell_A0=a0(shell),
            right_retained_shell_max_coefficient_hermitian_norm=float(np.max(norms)),
            right_retained_shell_max_component_abs=component_max(shell))
    else:
        require(kind == "TIME" and left["N"] == right["N"], "fixed temporal orientation")
        domains["U_comparison_domain"] = "FULL_FFT_GRID_INCLUDING_OUTSIDE_RETAINED_CUBE"
    vector_rows = {}
    actual_vector_count = 0
    for name in VECTOR_NAMES:
        vector_rows[name] = compare_vector(vectors_a[name], vectors_b[name])
        vector_rows[name]["comparison_shape"] = list(vectors_a[name].shape)
        vector_rows[name]["domain"] = (
            domains["U_comparison_domain"] if name == "U" else "COMPLETE_SHARED_BAND")
        actual_vector_count += 1
    require(actual_vector_count == 8, "eight complete vectors not compared")
    return {"group": group, "kind": kind, "left": evidence_a, "right": evidence_b,
            "actual_vectors_compared": actual_vector_count, "vectors": vector_rows, "U_domains": domains,
            "left_gate_flags": left["nodes"][j]["gate_flags"],
            "right_gate_flags": right["nodes"][k]["gate_flags"],
            "e2_scope": left["nodes"][j]["e2_scope"],
            "difference_orientation": "LEFT_MINUS_RIGHT",
            "relative_zero_rule": "max(left_A0,right_A0)==0 gives null/BOTH_ZERO_FLOAT",
            "maximum_difference_definition": "maximum absolute complex component, not mode norm",
            "interpretation": "FINITE_COMPLEX_ARRAY_COMPARISON_NOT_AN_NS_ERROR_BOUND"}


def fixed_comparisons(runs, bands, T, lock_sha, inputs, outputs, result):
    geometries = {N: geometry(N, K) for N, K in ((128, 42), (160, 53))}
    vector_rows, scalar_rows, groups = [], [], []
    for group, left_id, right_id, kind, multiplier in GROUPS:
        left, right = runs[left_id], runs[right_id]
        require(right["m"] == multiplier * left["m"], "fixed group index mapping")
        vector_count = scalar_count = 0
        vector_indices, scalar_indices = [], []
        outputs.progress(event="group_start", group=group, kind=kind)
        for j in range(left["m"] + 1):
            k = multiplier * j
            scalar_rows.append(compare_scalar_nodes(left, right, j, k, T, group))
            scalar_indices.append([j, k])
            scalar_count += 1
            result["scalar_node_pairs"] += 1
        for j in range(0, left["m"] + 1, 32):
            k = multiplier * j
            outputs.progress(event="checkpoint_pair_start", group=group, left_j=j, right_j=k,
                             completed_checkpoint_pairs=result["checkpoint_pairs"])
            row = compare_checkpoint_pair(left, right, j, k, kind, group, bands,
                                          geometries, T, lock_sha, inputs)
            vector_rows.append(row)  # Only scalars/header/byte evidence, no arrays.
            vector_indices.append([j, k])
            vector_count += 1
            result["checkpoint_pairs"] += 1
            outputs.progress(event="checkpoint_pair_complete", group=group, left_j=j, right_j=k,
                             completed_checkpoint_pairs=result["checkpoint_pairs"])
        required_endpoints = [[0, 0], [left["m"] // 2, right["m"] // 2], [left["m"], right["m"]]]
        require(all(pair in vector_indices and pair in scalar_indices for pair in required_endpoints),
                "group lacks 0/a/T coverage")
        require(vector_count == left["m"] // 32 + 1 and scalar_count == left["m"] + 1,
                "group count incomplete")
        groups.append({"group": group, "kind": kind, "left_run": left_id, "right_run": right_id,
                       "checkpoint_pairs": vector_count, "scalar_node_pairs": scalar_count,
                       "checkpoint_indices": vector_indices, "scalar_indices": scalar_indices,
                       "zero_a_T_indices": required_endpoints, "interpolation_performed": False})
        result["comparison_groups"] += 1
        outputs.progress(event="group_complete", group=group, checkpoint_pairs=vector_count,
                         scalar_node_pairs=scalar_count)
    require(result["comparison_groups"] == 4 and result["checkpoint_pairs"] == 44
            and result["scalar_node_pairs"] == 1284, "fixed final comparison totals")
    require(len(vector_rows) == result["checkpoint_pairs"]
            and len(scalar_rows) == result["scalar_node_pairs"], "output row counters")
    unique_checkpoints = 0
    for run in runs.values():
        require(run["loaded_checkpoints"] == set(run["checkpoints"]),
                "not every indexed checkpoint received header/payload validation")
        unique_checkpoints += len(run["loaded_checkpoints"])
    require(unique_checkpoints == 52, "unique full-checkpoint coverage")
    result["unique_input_checkpoints_validated"] = unique_checkpoints
    return groups, vector_rows, scalar_rows


def final_directory_names(runs):
    for run in runs.values():
        current = set()
        for path in run["directory"].rglob("*"):
            require(not path.is_symlink(), "new symlink in input run")
            if path.is_dir():
                continue
            require(path.is_file(), "input artifact type changed")
            current.add(path.relative_to(run["directory"]).as_posix())
        require(current == set(run["artifact_map"]) | {"execution.json"},
                "input run acquired/lost artifacts during comparison")


def main():
    global np
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", choices=(RUN_ID,), required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--source-lock", type=Path, required=True)
    args = parser.parse_args()
    directory = args.output_dir
    require(directory.is_absolute() and directory.resolve(strict=True) == directory
            and directory == HERE / "numerical-runs" / RUN_ID and directory.is_dir(),
            "output must be the fresh fixed supervisor-owned directory")
    require(not (directory / "result.json").exists(), "existing result; no overwrite/retry")
    require(set(path.name for path in directory.iterdir()) <= {
        "execution.json", "stdout.log", "stderr.log"}, "comparison output directory is not fresh")
    result = {"schema": 1, "status": "FAIL", "run_id": args.run_id,
              "pid": os.getpid(), "supervisor_pid": os.getppid(),
              "scientific_worker_invocations": 1, "source_lock_sha256": None,
              "source_hashes_start": {}, "source_hashes_end": {},
              "comparison_groups": 0, "checkpoint_pairs": 0, "scalar_node_pairs": 0,
              "fft_batched_api_calls": 0, "fft_scalar_3d_transforms": 0,
              "completion_verified": False,
              "classification": "FIXED_FINITE_GALERKIN_READ_ONLY_COMPARISON",
              "actual_NS_error_bound_certified": False,
              "actual_NS_source_gates_certified": False,
              "convergence_threshold_or_verdict": None, "new_trajectory_performed": False,
              "interpolation_performed": False, "automatic_retry_or_resume": False}
    inputs, outputs, runs, expected, guard = Inputs(), None, {}, None, None
    try:
        require(Path.cwd().resolve() == ROOT, "worker must run in the reverse worktree")
        require(args.source_lock.is_absolute() and ROOT in args.source_lock.parents,
                "source lock must be an absolute file in this worktree")
        outputs = Outputs(directory)
        outputs.progress(event="source_and_receipt_validation_start")
        lock_sha, expected, source_records = load_sources(args.source_lock, inputs)
        result["source_lock_sha256"] = lock_sha
        result["source_hashes_start"] = {name: row["sha256"] for name, row in source_records.items()}
        original = inputs.json(HERE / "input-preparation.json")
        T = fraction(original["fixed_observation"]["T"], "original T")
        require(T > 0 and fraction(original["fixed_observation"]["a"], "original a") == T / 2,
                "original fixed T/a")
        result["input_sha256"] = INPUT_SHA
        result["T_exact"], result["a_exact"] = qrecord(T), qrecord(T / 2)
        for run_id in SPECS:
            outputs.progress(event="trajectory_input_validation_start", input_run=run_id)
            run = check_trajectory_receipt(run_id, lock_sha, expected, source_records, inputs)
            load_indices(run, inputs, T)
            runs[run_id] = run
            outputs.progress(event="trajectory_input_validation_complete", input_run=run_id,
                             node_count=len(run["nodes"]), checkpoint_count=len(run["checkpoints"]))
        result["prerequisite_receipts"] = [run["receipt_evidence"] for run in runs.values()]
        outputs.progress(event="first_numpy_import_start")
        import numpy as numpy_module
        np = numpy_module
        require(sys.platform == "darwin" and np.__version__ == "2.3.5", "fixed platform/NumPy backend")
        guard = FFTGuard()
        from numerical_kernel import Band
        require(Path(sys.modules["numerical_kernel"].__file__).resolve()
                == HERE / "numerical_kernel.py", "kernel import identity")
        result["runtime"] = {"executable": sys.executable, "python": sys.version,
                             "platform": sys.platform, "numpy": np.__version__,
                             "first_import_inside_worker": True}
        bands = (Band(4, 8), Band(8, 16), Band(16, 32))
        outputs.progress(event="vector_comparisons_start")
        groups, vectors, scalars = fixed_comparisons(
            runs, bands, T, lock_sha, inputs, outputs, result)
        result["groups"] = groups
        result["artifacts"] = {
            "vector-comparisons.json": outputs.write("vector-comparisons.json",
                {"schema": 1, "run_id": RUN_ID, "rows": vectors}),
            "scalar-comparisons.json": outputs.write("scalar-comparisons.json",
                {"schema": 1, "run_id": RUN_ID, "rows": scalars}),
        }
        # Array locals belonged to a finished pair; the remaining tables are
        # ordinary scalar/metadata values. Whole input bytes are re-read now.
        outputs.progress(event="final_input_byte_validation_start")
        final_directory_names(runs)
        final_inputs = inputs.finish()
        final_map = {row["path"]: row["sha256"] for row in final_inputs}
        result["source_hashes_end"] = {name: final_map[name] for name in expected}
        require(result["source_hashes_end"] == expected, "final source map differs")
        result["artifacts"]["input-byte-evidence.json"] = outputs.write("input-byte-evidence.json",
            {"schema": 1, "all_input_bytes_unchanged": True, "files": final_inputs,
             "scope": "all source bindings and all four trajectory run artifacts, including receipts"})
        result["fft_guard"] = guard.finish()
        result["fft_batched_api_calls"] = result["fft_guard"]["completed_batched_api_calls"]
        result["fft_scalar_3d_transforms"] = result["fft_guard"]["completed_scalar_3d_transforms"]
        require(result["fft_batched_api_calls"] == 0 and result["fft_scalar_3d_transforms"] == 0,
                "comparison performed an FFT")
        result["all_input_bytes_unchanged"] = True
        result["completion_verified"] = True
        result["status"] = "PASS"
        outputs.progress(event="comparison_complete", comparison_groups=result["comparison_groups"],
                         checkpoint_pairs=result["checkpoint_pairs"],
                         scalar_node_pairs=result["scalar_node_pairs"])
    except BaseException as error:
        result.update(status="FAIL", completion_verified=False,
                      error={"type": type(error).__name__, "message": str(error),
                             "traceback": traceback.format_exc()})
        if guard is not None:
            result["fft_attempted_api_calls_on_failure"] = guard.attempted_api_calls
        if expected is not None:
            try:
                result["source_hashes_end"] = {
                    name: file_record(ROOT / name)["sha256"] for name in expected}
            except BaseException as source_error:
                result["source_hashes_end_error"] = repr(source_error)
        if outputs is not None:
            try:
                outputs.progress(event="comparison_failed", error=result["error"])
            except BaseException:
                pass  # Original failure is preserved in result.json below.
    finally:
        if outputs is not None:
            outputs.close()
        result["worker_seconds_to_result_serialization"] = time.monotonic() - PROCESS_START
        result["timing_scope"] = (
            "worker import/read/hash/arithmetic/output to this serialization; "
            "supervisor separately measures full child creation-through-reap lifecycle")
        raw = encode_json(result)
        prior_bytes = sum(path.stat().st_size for path in directory.rglob("*") if path.is_file())
        if prior_bytes + len(raw) > OUTPUT_LIMIT:
            result.update(status="FAIL", completion_verified=False, worker_output_budget_exceeded=True)
            raw = encode_json(result)  # Preserve the failure even if the final budget is exceeded.
        with (directory / "result.json").open("xb") as handle:
            handle.write(raw)
        print(json.dumps({"status": result["status"], "run_id": RUN_ID,
                          "completion_verified": result["completion_verified"]}), flush=True)
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
