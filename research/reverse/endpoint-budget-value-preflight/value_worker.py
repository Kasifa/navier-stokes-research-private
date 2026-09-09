"""One fixed numerical-value scout, never a rigorous bound or NS certificate.

Only the reviewed supervisor may launch this worker once. Scientific imports,
all 34 binary hashes, arrays, FFTs and serialisation belong to that lifecycle.
No original array is modified. Git/source-commit and live admission are external.
"""
import sys
sys.dont_write_bytecode = True
import argparse
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import resource
import time
import traceback
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ANN = ROOT / "research/reverse/annular-source-observation"
RUN_ID = "value-scout-160-512"
PYTHON = Path("/Users/kasifa/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3")
THREADS = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")
MIB = 1024**2
WORKER_LIMIT = 1024**3 - 16*MIB  # Reserve space for parent logs and final receipt.
JSON_LIMIT = 15*MIB  # Parent must still check the complete 16 MiB JSON budget.
PREFIX = HERE.relative_to(ROOT).as_posix() + "/"
OLD = ANN.relative_to(ROOT).as_posix() + "/"
FIXED = {
    PREFIX+"input-bindings.json": "4285c18b4def69ac450cb0c7f10f44f640aa34ce4364241fdb3dabf2a413ccd6",
    PREFIX+"budget_formulas.py": "e16b4a3d5eb32bcb578ebd01731d38a83c7374eec90b500324811d07ea79d883",
    PREFIX+"DESIGN.md": "9c6a9e660f2c1179b2ccf9dd79364b06e1ccfa65912bc9150ee1846325a0d7fd",
    PREFIX+"EXECUTION_CONTRACT_DRAFT.md": "b44b689db1066ced1632be7fd033ead81fa398b89f1194249190b0b00f0936f6",
    OLD+"numerical_kernel.py": "1b29e919cf5faefe1e4a5193fee0f7e0fdd11901d8aed7b3e5ade752cd23f175",
    OLD+"input-preparation.json": "3f51705fbd934ce76d503c1c856566405ee3deb1760474b1c73ef6a6f481c61f",
    OLD+"verify-input-output.json": "4ef16c30bb85b24f5ed6f6be973106764df26b33c3da0180ba4c531954fc32f1",
    OLD+"input-acceptance.json": "dbd34732c073507b6162a273fcf1ff6100cc3f723c24487ede079fba3f22d827"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local_path(name):
    p = PurePosixPath(name)
    require(not p.is_absolute() and ".." not in p.parts and str(p) == name,
            "noncanonical relative path")
    path = ROOT / name
    require(path.resolve() == path and path.is_file(), "missing/symlink/nonregular input")
    return path


def record(path):
    digest, size = hashlib.sha256(), 0
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(MIB), b""):
            digest.update(chunk)
            size += len(chunk)
    return {"bytes": size, "sha256": digest.hexdigest()}


def q(value):
    require(isinstance(value, dict) and set(value) == {"numerator", "denominator"},
            "rational record schema")
    require(all(isinstance(v, str) and re.fullmatch(r"-?(0|[1-9][0-9]*)", v)
                for v in value.values()), "rational integer strings")
    require(int(value["denominator"]) > 0, "nonpositive denominator")
    return Fraction(int(value["numerator"]), int(value["denominator"]))


def qr(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def conversion(value):
    f = float(value)
    require(math.isfinite(f), "nonfinite rational conversion")
    back = Fraction.from_float(f)
    return {"exact": qr(value), "float_hex": f.hex(), "float_ratio": qr(back),
            "signed_error": qr(back-value), "absolute_error": qr(abs(back-value))}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def lock_snapshot(path):
    require(path.is_absolute() and path.resolve() == path and path.is_file(), "source-lock path")
    raw = path.read_bytes()
    data = json.loads(raw)
    require(type(data.get("schema")) is int and data["schema"] == 1, "source-lock schema")
    rows = data.get("bindings")
    require(isinstance(rows, list) and rows, "empty source lock")
    maps = {}
    for row in rows:
        require(set(row) == {"path", "sha256", "bytes"}, "source binding schema")
        name = row["path"]
        require(name not in maps and Path(name).suffix in (".py", ".md", ".json", ".jsonl", ".txt"),
                "duplicate/binary source binding; NPZ/gzip must never enter parent source hashing")
        require(type(row["bytes"]) is int and row["bytes"] >= 0
                and re.fullmatch(r"[0-9a-f]{64}", row["sha256"]), "source identity")
        actual = record(local_path(name))
        require(actual == {"bytes": row["bytes"], "sha256": row["sha256"]}, "source changed: "+name)
        maps[name] = actual["sha256"]
    required = set(FIXED) | {PREFIX+"value_worker.py", PREFIX+"run_value.py"}
    require(required <= maps.keys(), "missing indispensable source")
    require(all(maps[name] == sha for name, sha in FIXED.items()), "fixed source identity differs")
    return maps, hashlib.sha256(raw).hexdigest()


def finite(np, *values):
    for value in values:
        require(bool(np.all(np.isfinite(value))), "nonfinite numerical value")


def inventory(directory):
    rows = []
    for path in sorted(directory.iterdir()):
        require(path.is_file() and not path.is_symlink(), "unexpected output entry")
        rows.append((path.name, path.stat().st_size))
    return rows


def room(directory, additional=0):
    rows = inventory(directory)
    require(sum(size for _, size in rows)+additional <= WORKER_LIMIT, "worker output reserve exceeded")
    require(sum(size for name, size in rows if ".json" in name) <= JSON_LIMIT,
            "worker JSON reserve exceeded")


def publish(directory, name, writer):
    final, temporary = directory/name, directory/(name+".tmp")
    require(not final.exists() and not temporary.exists(), "output already exists")
    with temporary.open("xb") as handle:
        writer(handle)
        handle.flush()
        os.fsync(handle.fileno())
    room(directory)
    os.link(temporary, final)  # Atomic no-overwrite endpoint; failure retains temporary.
    temporary.unlink()
    return {"path": name, **record(final)}


def write_json(directory, name, value):
    raw = (json.dumps(value, sort_keys=True, indent=2, allow_nan=False)+"\n").encode("ascii")
    require(len(raw) <= JSON_LIMIT, "single JSON too large")
    room(directory, len(raw))
    return publish(directory, name, lambda h: h.write(raw))


def write_npz(np, directory, name, **arrays):
    for a in arrays.values():
        require(isinstance(a, np.ndarray) and not a.dtype.hasobject, "invalid output array")
        finite(np, a)
    room(directory, sum(a.nbytes for a in arrays.values())+MIB)
    return publish(directory, name, lambda h: np.savez(h, **arrays))


class Journal:
    def __init__(self, directory, start):
        self.directory, self.start, self.count = directory, start, 0
        self.handle = (directory/"progress.jsonl").open("xb")

    def emit(self, event, **fields):
        raw = (json.dumps({"event": event, "elapsed_seconds": time.monotonic()-self.start,
                           **fields}, sort_keys=True, allow_nan=False)+"\n").encode("ascii")
        room(self.directory, len(raw))
        self.handle.write(raw)
        self.handle.flush()
        self.count += 1


def inputs():
    data = read_json(HERE/"input-bindings.json")
    require(data["schema"] == 1 and data["run_id"] == RUN_ID and data["trajectory_run_id"] == "trajectory160_512",
            "input mapping identity")
    require((data["N"], data["K"], data["segments"]) == (160, 53, 16), "fixed geometry changed")
    original = read_json(local_path(data["input_preparation"]))
    independent = read_json(local_path(data["input_verifier"]))
    acceptance = read_json(ANN/"input-acceptance.json")
    require(acceptance["status"] == "INPUT_VERIFIED" and independent["status"] == "VERIFIED",
            "original input is not accepted")
    require(data["T"] == original["fixed_observation"]["T"] == independent["mathematics"]["fixed_observation"]["T"],
            "three T objects differ")
    require(data["M2_interval"] == original["original_norm_bounds"]["M_squared_interval_normalized"]
            == independent["mathematics"]["initial_error_and_original_norm_bounds"]["M_squared_interval_normalized"],
            "three original M squared intervals differ")
    T, mlo, mhi = q(data["T"]), q(data["M2_interval"][0]), q(data["M2_interval"][1])
    require(T > 0 and mlo <= mhi and mhi >= 0, "time/norm interval domain")
    require(len(data["checkpoints"]) == 17, "not exactly seventeen checkpoints")
    for i, row in enumerate(data["checkpoints"]):
        expected = OLD+f"numerical-runs/trajectory160_512/checkpoint-{32*i:06d}.npz"
        require(row["endpoint_index"] == i and row["original_step_j"] == 32*i
                and row["path"] == expected and q(row["time_exact"]) == T*Fraction(i, 16), "checkpoint map/time")
        require(type(row["bytes"]) is int and re.fullmatch(r"[0-9a-f]{64}", row["sha256"]), "checkpoint identity")
    return data, T, max(Fraction(0), mlo), mhi


def load_U(np, path, binding):
    with zipfile.ZipFile(path) as archive:
        entries = archive.infolist()
        require(len(entries) == 6 and {e.filename for e in entries} == set(binding["npz_members"]), "NPZ members")
        require(all(not e.is_dir() and not(e.flag_bits & 1) for e in entries), "NPZ entry type")
        with archive.open("U.npy") as handle:
            version = np.lib.format.read_magic(handle)
            require(version in ((1, 0), (2, 0)), "NPY version")
            reader = np.lib.format.read_array_header_1_0 if version == (1, 0) else np.lib.format.read_array_header_2_0
            shape, order, dtype = reader(handle)
            offset = handle.tell()
        require(shape == (3,160,160,160) and not order and dtype == np.dtype("<c16")
                and not dtype.hasobject, "U header/dtype/order")
        require(archive.getinfo("U.npy").file_size == offset+196608000, "U member length")
    with np.load(path, allow_pickle=False) as archive:
        U = archive["U"]  # The sole decoded member; never G, W, modes or metadata_json.
    require(U.shape == shape and U.dtype == dtype and U.flags.c_contiguous, "decoded U shape/order")
    finite(np, U)
    return U, {"shape": list(shape), "dtype": dtype.str, "fortran_order": bool(order), "NPY_version": list(version)}


def mode_square(np, field):
    answer = np.zeros(field.shape[1:], dtype=np.float64)
    for component in field:
        answer += component.real**2 + component.imag**2
    return answer


def a0(np, field):
    value = float(np.sum(np.sqrt(mode_square(np, field))))
    require(math.isfinite(value), "nonfinite A0")
    return value


def diagnostics(np, grid, field):
    result = {"A0": a0(np, field), "mean": float(np.linalg.norm(field[:,0,0,0]))}
    dot = sum(grid.k[j]*field[j] for j in range(3))
    result["divergence_max"] = float(np.max(np.abs(dot)))
    del dot
    n = grid.negative_indices
    differences = []
    for component in field:
        partner = np.conj(component[n[:,None,None], n[None,:,None], n[None,None,:]])
        differences.append(float(np.max(np.abs(component-partner))))
        del partner
    result["conjugacy_component_max"] = differences
    finite(np, list(result.values())[:2], differences, result["divergence_max"])
    return result


def cube_indices(np, size):
    axis = np.arange(-53, 54, dtype=np.int64)
    index = axis % size
    return axis, (index[:,None,None], index[None,:,None], index[None,None,:])


def install_fft_counter(np, result):
    originals = {name: getattr(np.fft, name) for name in ("fftn", "ifftn")}
    result["fft_counts"] = {}
    def wrap(name):
        original = originals[name]
        def counted(field, *args, **kwargs):
            require(not args and field.shape in ((3,160,160,160),(3,216,216,216))
                    and kwargs == {"axes":(1,2,3), "norm":"forward"}, "unexpected FFT")
            key = f"{name}:{field.shape[1]}"
            result["fft_counts"][key] = result["fft_counts"].get(key, 0)+1
            result["fft_batched_api_calls"] += 1
            result["fft_scalar_3d_transforms"] += 3
            return original(field, **kwargs)
        return counted
    for name in originals:
        setattr(np.fft, name, wrap(name))
    return originals


def science(args, result, journal):
    import numpy as np
    require(np.__version__ == "2.3.5", "wrong NumPy version")
    require(Path(np.__file__).resolve() == (PYTHON.parent.parent/"lib/python3.12/site-packages/numpy/__init__.py").resolve(),
            "NumPy is not from the fixed bundled runtime")
    sys.path.insert(0, str(ANN))
    from numerical_kernel import FourierGrid, Band
    from budget_formulas import bernstein_segment, legendre_rule64, phi6
    require(Path(sys.modules["numerical_kernel"].__file__).resolve() == ANN/"numerical_kernel.py"
            and Path(sys.modules["budget_formulas"].__file__).resolve() == HERE/"budget_formulas.py",
            "imported dependency path differs from locked source")
    result["environment"]["numpy_version"] = np.__version__
    result["environment"]["numpy_file"] = np.__file__
    data, T, mlo, mhi = inputs()
    hq, h = T/16, float(T/16)
    require(math.isfinite(h) and h > 0, "physical Hermite segment length")
    result["time_conversions"] = {"T":conversion(T), "h":conversion(hq), "nodes":[],
                                  "kappa_delays":[], "PH_delay_scale":conversion(hq)}
    result["M_squared_interval"] = data["M2_interval"]
    result["M_lower_squared_conversion"] = conversion(mlo)
    Mminus = math.sqrt(float(mlo))
    require(math.isfinite(Mminus), "nonfinite original M lower approximation")
    result["M_lower_num"] = Mminus
    original_fft = install_fft_counter(np, result)
    try:
        grid, band0, band1 = FourierGrid(160,53), Band(4,8), Band(8,16)
        require(3*53 < 160 and 4*53 < 216, "alias geometry")
        for band in (band0, band1):
            require(band.modes.dtype == np.dtype("int64") and np.array_equal(band.modes, -band.modes[::-1]),
                    "full signed band symmetry")
            idx = band.indices(160)
            require(all(np.array_equal(grid.frequencies[idx[j]], band.modes[:,j]) for j in range(3)), "signed band indexing")
        require(np.array_equal(grid.frequencies[grid.negative_indices],
                               np.where(grid.frequencies == -80, -80, -grid.frequencies)), "negative FFT indices")
        lows, slopes, headers = [], [], []
        axis, ci = cube_indices(np, 160)
        result["input_hashes_before"], result["input_hashes_after"] = [], []
        for i, row in enumerate(data["checkpoints"]):
            journal.emit("checkpoint_start", endpoint_index=i, original_j=row["original_step_j"])
            path = local_path(row["path"])
            before = record(path)
            result["input_hashes_before"].append({"path":row["path"], **before})
            require(before == {"bytes":row["bytes"],"sha256":row["sha256"]}, "original input hash changed")
            U, header = load_U(np, path, data)
            headers.append(header)
            neg = grid.negative_indices
            partner = np.conj(U[:,neg[:,None,None],neg[None,:,None],neg[None,None,:]])
            symmetric = (U+partner)/2
            del partner
            X = grid.project(symmetric)
            del symmetric
            info = diagnostics(np, grid, X)
            info["projection_change_A0"] = a0(np, X-U)
            del U
            result["rhs160_calls"] += 1
            B = grid.rhs(X)
            finite(np, B)
            low, ds = band0.gather(X), band0.gather(B)
            ds += band0.laplacian[None,:]*low
            require(low.shape == ds.shape == (3,band0.size), "H0 common shape")
            finite(np, low, ds)
            lows.append(low); slopes.append(ds)
            if i == 16:
                Xlast, Blast = X[(slice(None),)+ci], B[(slice(None),)+ci]
                H1 = band1.gather(X)
                H = a0(np, H1)
            del X, B
            result["time_conversions"]["nodes"].append(conversion(T*Fraction(i,16)))
            journal.emit("checkpoint_complete", endpoint_index=i, diagnostics=info,
                         rhs160_calls=result["rhs160_calls"], fft_counts=dict(result["fft_counts"]))
            result["processed_checkpoints"] += 1
        h0, d0 = np.stack(lows), np.stack(slopes)
        del lows, slopes, low, ds
        controls, grams, ordered, explicit, endpoints = [], [], [], [], []
        for i in range(16):
            require(h0[i].shape == d0[i].shape == h0[i+1].shape == d0[i+1].shape == (3,band0.size),
                    "Bernstein input common full-H0 shape")
            parts = bernstein_segment(np, h0[i], d0[i], h0[i+1], d0[i+1], h)
            finite(np, *parts)
            for destination, value in zip((controls,grams,ordered,explicit,endpoints), parts):
                destination.append(value)
        controls, grams, ordered, explicit, endpoints = map(np.stack, (controls,grams,ordered,explicit,endpoints))
        V = np.max(ordered, axis=1)
        require(np.all(V >= 0), "negative segment maximum")
        radius = np.sqrt(-band1.laplacian)
        kappa = np.empty(16)
        for i in range(16):
            delay = T-T*Fraction(i+1,16)
            result["time_conversions"]["kappa_delays"].append(conversion(delay))
            kappa[i] = np.sum(np.exp(band1.laplacian*float(delay))*(-np.expm1(band1.laplacian*h))/radius)
        finite(np, kappa, V)
        require(np.all(kappa >= 0), "negative heat mass")
        result["H_num"], result["Ubar_num"] = H, float(H+0.75*np.sum(V*kappa))
        result["U_headers"] = headers
        result["artifacts"].append(write_npz(np, args.output_dir, "reconstruction.npz",
            H0=h0, H0_slopes=d0, H0_modes=band0.modes, H1_terminal=H1, H1_modes=band1.modes,
            controls=controls, grams=grams, q_ordered=ordered, q_explicit=explicit,
            q_difference=ordered-explicit, Hermite_endpoint_differences=endpoints, V=V, kappa=kappa))
        journal.emit("reconstruction_complete", Ubar_num=result["Ubar_num"])
        del h0, d0, H1, controls, grams, ordered, explicit, endpoints, V, kappa, parts
        del grid, ci  # No live 160 work grid or full 160 vector when 216 is created.
        grid = FourierGrid(216, None)
        require(grid.mask is None, "216 must be unmasked")
        _, ci = cube_indices(np,216)
        require(np.array_equal(grid.frequencies[axis % 216], axis), "216 integer embedding")
        X216 = np.zeros((3,216,216,216), dtype=np.complex128)
        X216[(slice(None),)+ci] = Xlast
        journal.emit("rhs216_start")
        result["rhs216_calls"] += 1
        B216 = grid.rhs(X216)
        del X216
        finite(np, B216)
        result["terminal_diagnostics"] = diagnostics(np,grid,B216)
        maxcoord = np.maximum(np.maximum(np.abs(grid.k[0]),np.abs(grid.k[1])),np.abs(grid.k[2]))
        selected = (maxcoord > 53) & (maxcoord <= 106)
        square = mode_square(np,B216)
        L2 = float(np.sum(square[selected]/grid.k2[selected]))
        tail = float(np.sum(np.sqrt(square[maxcoord > 106])))
        require(math.isfinite(L2) and L2 >= 0 and math.isfinite(tail), "terminal weighted norm/tail")
        result["L_squared_num"], result["outside_C106_A0_num"] = L2, tail
        difference = B216[(slice(None),)+ci]-Blast
        finite(np,difference)
        result["C53_difference_A0_num"] = a0(np,difference)
        result["artifacts"].append(write_npz(np,args.output_dir,"terminal-compact.npz",
            X_C53=Xlast,B160_C53=Blast,B216_minus_B160_C53=difference,cube_axis=axis))
        del Xlast, Blast, difference, selected, maxcoord, square, ci
        result["artifacts"].append(write_npz(np,args.output_dir,"full-B216.npz",B=B216,
                                            frequency_axis=grid.frequencies))
        del B216, grid
        journal.emit("rhs216_complete", L_squared_num=L2)
        result["rule64_calls"] += 1
        nodes, weights, P64, derivative = legendre_rule64(np)
        rho = (nodes+1)/2
        require(nodes.shape == weights.shape == rho.shape == (64,) and np.all((rho > 0)&(rho < 1)), "quadrature shape/domain")
        result["phi6_calls"] += 1
        phi, scaled, denominator = phi6(np,rho,h)
        result["phi6_calls"] += 1
        endpoint_phi, endpoint_scaled, endpoint_denominator = phi6(np,np.array([0.,1.]),h)
        finite(np,nodes,weights,P64,derivative,phi,scaled,denominator,endpoint_phi,endpoint_scaled,endpoint_denominator)
        require(np.all(phi >= 0), "negative Phi")
        endpoint_difference = endpoint_phi-np.array([0.,h/49])
        L = math.sqrt(L2)
        errors = L*np.sqrt(phi)
        # Exact Gauss nodes are not rational; only h conversion is exact-recorded.
        delays = h*(1-rho)
        kernels = np.array([np.sum(radius*np.exp(band1.laplacian*delay)) for delay in delays])
        integrand = kernels*errors*(2*Mminus+errors)
        terms = (h/2)*weights*integrand
        finite(np,delays,kernels,errors,integrand,terms,endpoint_difference)
        J = float(np.sum(terms))
        BF = math.sqrt(band1.size*h)*L/7
        PH = BF+1.25*J
        finite(np,J,BF,PH,result["Ubar_num"])
        require(J >= 0 and BF >= 0 and PH >= 0, "negative budget formula")
        result["budget_values"] = {"L_num":L,"N1":band1.size,"M_minus_num":Mminus,
            "c_b":0,"J_num":J,"B_BF_num":BF,"B_PH_num":PH,
            "Ubar_minus_B_BF_num":result["Ubar_num"]-BF,"Ubar_minus_B_PH_num":result["Ubar_num"]-PH,
            "Ubar_div_B_BF_num":result["Ubar_num"]/BF if BF else None,
            "Ubar_div_B_PH_num":result["Ubar_num"]/PH if PH else None}
        finite(np,[v for v in result["budget_values"].values() if v is not None])
        result["artifacts"].append(write_npz(np,args.output_dir,"quadrature.npz",
            nodes=nodes,weights=weights,P64_values=P64,derivative=derivative,rho=rho,
            phi=phi,scaled_legendre=scaled,denominator=denominator,delays=delays,kernels=kernels,
            e_star=errors,integrand=integrand,weighted_terms=terms,endpoint_rho=np.array([0.,1.]),
            endpoint_phi=endpoint_phi,endpoint_scaled=endpoint_scaled,endpoint_denominator=endpoint_denominator,
            endpoint_identity_differences=endpoint_difference))
        result["quadrature"] = {"nodes":64,"weights_sum_minus_2":float(np.sum(weights)-2),
                                "Phi_endpoint_differences":endpoint_difference.tolist(),"rule_generations":result["rule64_calls"]}
        journal.emit("formulas_complete", budget_values=result["budget_values"])
        for row in data["checkpoints"]:
            after = record(local_path(row["path"]))
            result["input_hashes_after"].append({"path":row["path"], **after})
            require(after == {"bytes":row["bytes"],"sha256":row["sha256"]}, "original input changed after use")
            journal.emit("input_after_hash", original_j=row["original_step_j"])
        require(result["fft_counts"] == {"ifftn:160":34,"fftn:160":17,"ifftn:216":2,"fftn:216":1}, "actual FFT counts")
        require((result["rule64_calls"],result["phi6_calls"]) == (1,2), "actual formula calls")
    finally:
        for name, original in original_fft.items():
            setattr(np.fft,name,original)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", choices=(RUN_ID,), required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--source-lock", type=Path, required=True)
    args = parser.parse_args()
    directory = HERE/"numerical-runs"/RUN_ID
    require(args.output_dir.is_absolute() and args.output_dir == directory
            and directory.resolve() == directory and directory.is_dir(), "supervised output directory")
    require({p.name for p in directory.iterdir()} <= {"stdout.log","stderr.log","execution.json.tmp"},
            "worker refuses an occupied scientific output directory")
    start = time.monotonic()
    result = {"schema":1,"status":"FAIL","run_id":RUN_ID,"pid":os.getpid(),"supervisor_pid":os.getppid(),
        "scientific_worker_invocations":0,"completion_verified":False,"processed_checkpoints":0,
        "rhs160_calls":0,"rhs216_calls":0,"fft_batched_api_calls":0,"fft_scalar_3d_transforms":0,
        "rule64_calls":0,"phi6_calls":0,"call_counter_scope":"Attempted calls; COMPLETED also requires every return and check",
        "source_lock_sha256":None,"source_hashes_start":{},"source_hashes_end":{},"artifacts":[],
        "classification":"NUMERICAL_VALUE_ONLY","NS_gate_or_lifespan_certified":False,
        "single_sided_bound_or_quadrature_error_certified":False,"automatic_retry":False}
    journal = Journal(directory,start)
    try:
        require(sys.version_info[:3] == (3,12,14) and sys.platform == "darwin", "wrong Python/platform")
        require(Path(sys.executable).resolve() == PYTHON.resolve(), "wrong fixed interpreter")
        require(all(os.environ.get(name) == "1" for name in THREADS), "five thread controls must equal 1")
        result["environment"] = {"python":sys.version,"executable":sys.executable,"uname":list(os.uname()),
                             "thread_environment":{name:os.environ.get(name) for name in THREADS}}
        maps, lock_sha = lock_snapshot(args.source_lock)
        result["source_hashes_start"], result["source_lock_sha256"] = maps, lock_sha
        journal.emit("scientific_stage_start")
        result["scientific_worker_invocations"] += 1
        science(args,result,journal)
        end_maps, end_sha = lock_snapshot(args.source_lock)
        result["source_hashes_end"] = end_maps
        require(maps == end_maps and lock_sha == end_sha, "sources/lock changed")
        require((result["processed_checkpoints"],result["rhs160_calls"],result["rhs216_calls"],
                 result["fft_batched_api_calls"],result["fft_scalar_3d_transforms"]) == (17,17,1,54,162),
                "completion counters")
        require(len(result["input_hashes_before"]) == len(result["input_hashes_after"]) == 17, "34 input hashes")
        result["completion_verified"] = True
        result["status"] = "COMPLETED_NUMERICAL_VALUE_ONLY"
        journal.emit("scientific_stage_complete")
    except BaseException:
        result["exception"] = traceback.format_exc()
        result["completion_verified"] = False
        result["status"] = "FAIL"
    finally:
        journal.handle.close()
        if result["status"] == "FAIL":
            try:
                result["source_hashes_end"], result["source_lock_end_sha256"] = lock_snapshot(args.source_lock)
            except BaseException:
                result["failed_end_source_check"] = traceback.format_exc()
        result["progress_events"] = journal.count
        result["artifacts"].append({"path":"progress.jsonl", **record(directory/"progress.jsonl")})
        usage = resource.getrusage(resource.RUSAGE_SELF)
        result["worker_resources_pre_result"] = {"user_seconds":usage.ru_utime,"system_seconds":usage.ru_stime,
            "peak_rss_bytes_Darwin":usage.ru_maxrss,"wall_seconds":time.monotonic()-start,
            "scope":"SELF before result serialisation; parent measures complete child lifecycle/RSS separately"}
    try:
        write_json(directory,"result.json",result)
    except BaseException:
        # A serialization/output-budget failure never inherits COMPLETED status.
        # Preserve any full result.json.tmp and all scientific files unchanged.
        result = {"schema":1,"status":"FAIL","run_id":RUN_ID,"pid":os.getpid(),
                  "supervisor_pid":os.getppid(),"scientific_worker_invocations":result["scientific_worker_invocations"],
                  "completion_verified":False,"result_serialization_failure":traceback.format_exc()}
        if not (directory/"result.json").exists():
            raw = (json.dumps(result,sort_keys=True,allow_nan=False)+"\n").encode("ascii")
            with (directory/"result.json").open("xb") as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
    print(json.dumps({"status":result["status"],"scientific_worker_invocations":result["scientific_worker_invocations"],
                      "completion_verified":result["completion_verified"]},sort_keys=True))
    return 0 if result["completion_verified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
