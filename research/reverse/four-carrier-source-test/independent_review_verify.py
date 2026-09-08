#!/usr/bin/env python3
"""One bounded, read-only verification of the stopped independent certificate.

This is a nonauthor certificate check, not a third research derivation.
Explicit ordered trees/permutations replace subset dynamic programming;
cross products implement Leray; polynomial division replaces quadratic classes.
No source module is imported, no input file is overwritten, no chart is changed.
"""
from fractions import Fraction as R
from itertools import combinations, permutations
from functools import reduce
from math import gcd
from pathlib import Path
import hashlib
import json
import os
import resource
import signal
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
OUT = HERE / "independent_review_verify-output.json"
BOUND = {
    "CONTRACT.md": "7b8769fe6eb84fcaad86cde7b65e5debf79801b30f9c2ae41e0e2758c0968456",
    "INDEPENDENT_ALGEBRA.md": "a87cdef2cc2517e391ee193c3ad17b0e6776af3d7b8dff8f0427c2b063e08d1a",
    "independent_subset.py": "e588da476addd56f092fea94b8f0315a0eb7df3e304d9fba3e51071d17c35f6c",
    "independent-output.json": "de084e897e08c7faa48dd49dbb00af61f0449587b34e8a4890711c4a176a0bc7",
}
FREQ = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 3, 5))
LEAF = "*"
PAIR = (LEAF, LEAF)
SHAPES = {
    1: (LEAF,),
    2: (PAIR,),
    3: ((PAIR, LEAF), (LEAF, PAIR)),
    4: (((PAIR, LEAF), LEAF), ((LEAF, PAIR), LEAF),
        (PAIR, PAIR), (LEAF, (PAIR, LEAF)), (LEAF, (LEAF, PAIR))),
}


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), R(0))


def cross(x, y):
    return (x[1] * y[2] - x[2] * y[1],
            x[2] * y[0] - x[0] * y[2],
            x[0] * y[1] - x[1] * y[0])


def plus(x, y):
    return tuple(a + b for a, b in zip(x, y))


def name(shape):
    return "*" if shape == LEAF else "(" + name(shape[0]) + "," + name(shape[1]) + ")"


def one_tree(shape, labels, seeds):
    if shape == LEAF:
        j = next(labels)
        return FREQ[j], seeds[j], 1
    p, x, left_size = one_tree(shape[0], labels, seeds)
    q, y, right_size = one_tree(shape[1], labels, seeds)
    k = plus(p, q)
    size = left_size + right_size
    assert dot(k, k) > 0 and dot(p, x) == dot(q, y) == 0
    # k cross (y cross k) / |k|^2 is exactly P_k y.
    transverse = cross(k, cross(y, k))
    factor = dot(x, q) / (dot(k, k) * (size - 1))
    value = tuple(factor * z for z in transverse)
    assert dot(k, value) == 0
    return k, value, size


def trim(p):
    p = list(map(R, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def padd(p, q):
    return trim([(p[i] if i < len(p) else R(0)) +
                 (q[i] if i < len(q) else R(0))
                 for i in range(max(len(p), len(q)))])


def pmul(p, q):
    ans = [R(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            ans[i + j] += a * b
    return trim(ans)


def pmod(p, f):
    p = trim(p)
    while len(p) >= len(f) and p != [R(0)]:
        shift, factor = len(p) - len(f), p[-1] / f[-1]
        p = padd(p, [R(0)] * shift + [-factor * z for z in f])
    return p


def peval(p, x):
    value = R(0)
    for coefficient in reversed(p):
        value = value * x + coefficient
    return value


def algebra_element(item):
    return trim([R(item["constant"]), R(item["theta"])])


def verify():
    for filename, expected in BOUND.items():
        assert hashlib.sha256((HERE / filename).read_bytes()).hexdigest() == expected
    source = json.loads((HERE / "independent-output.json").read_text())
    assert source["execution_status"] == "completed"
    assert source["source_sha256"] == BOUND["independent_subset.py"]
    assert source["contract_sha256"] == BOUND["CONTRACT.md"]
    data = source["result"]
    assert data["initial_frequencies"] == [list(p) for p in FREQ]
    assert data["receiver"] == [3, 4, 6] and data["shape_count"] == 5
    assert data["alpha_probes"] == [0, 1, -1]
    table = data["evaluations"]
    assert set(table) == {"alpha=" + str(a) + ",basis=" + b
                          for a in (0, 1, -1) for b in ("v", "w")}
    counts = {"subset_records": 0, "shape_records": 0, "ordered_terms": 0}
    recomputed = {}
    for alpha in (0, 1, -1):
        for basis in ("v", "w"):
            seeds = (tuple(map(R, (0, 1, alpha))), tuple(map(R, (0, 0, 1))),
                     tuple(map(R, (1, 0, 0))),
                     tuple(map(R, (3, -2, 0) if basis == "v" else (5, 0, -2))))
            assert all(dot(p, u) == 0 for p, u in zip(FREQ, seeds))
            item = table["alpha=" + str(alpha) + ",basis=" + basis]
            expected_labels = [labels for n in (1, 2, 3, 4)
                               for labels in combinations(range(4), n)]
            assert set(item["subsets"]) == {
                ",".join(str(j + 1) for j in labels) for labels in expected_labels}
            all_shapes = {}
            for labels in expected_labels:
                key = ",".join(str(j + 1) for j in labels)
                stored = item["subsets"][key]
                freq = tuple(sum(FREQ[j][i] for j in labels) for i in range(3))
                assert stored["frequency"] == list(freq)
                assert set(stored["ordered_shape_sums"]) == {name(s) for s in SHAPES[len(labels)]}
                counts["subset_records"] += 1
                for shape in SHAPES[len(labels)]:
                    total = (R(0), R(0), R(0))
                    for ordering in permutations(labels):
                        k, term, size = one_tree(shape, iter(ordering), seeds)
                        assert k == freq and size == len(labels)
                        total = plus(total, term)
                        counts["ordered_terms"] += 1
                    assert total == tuple(map(R, stored["ordered_shape_sums"][name(shape)]))
                    all_shapes[(labels, name(shape))] = total
                    counts["shape_records"] += 1
            root = (0, 1, 2, 3)
            pure = all_shapes[(root, name((PAIR, PAIR)))]
            mixed = tuple(sum(all_shapes[(root, name(s))][i]
                              for s in SHAPES[4] if s != (PAIR, PAIR)) for i in range(3))
            assert pure == tuple(map(R, item["W_stripped"]))
            assert mixed == tuple(map(R, item["M_stripped"]))
            recomputed[(alpha, basis)] = (all_shapes, mixed, pure)
    for basis in ("v", "w"):
        zero, one, minus = (recomputed[(a, basis)][0] for a in (0, 1, -1))
        assert all(minus[key] == tuple(2 * a - b for a, b in zip(zero[key], one[key]))
                   for key in zero)
    matrices = []
    for index, key in ((1, "M_3_by_2"), (2, "W_3_by_2")):
        matrix = [[list(map(R, cell)) for cell in row] for row in data[key]]
        assert len(matrix) == 3 and all(len(row) == 2 for row in matrix)
        for i in range(3):
            for j, basis in enumerate(("v", "w")):
                constant = recomputed[(0, basis)][index][i]
                slope = recomputed[(1, basis)][index][i] - constant
                assert matrix[i][j] == [constant, slope]
        for j in range(2):
            assert padd(padd([3 * x for x in matrix[0][j]],
                             [4 * x for x in matrix[1][j]]),
                        [6 * x for x in matrix[2][j]]) == [R(0)]
        matrices.append(matrix)
    m, wmat = matrices
    det = padd(pmul(m[0][0], m[1][1]), [-z for z in pmul(m[0][1], m[1][0])])
    assert det == list(map(R, data["determinant_ascending"]))
    f = list(map(R, data["determinant_primitive_ascending"]))
    assert f == list(map(R, (37138824124764, 104767331941035, 73555298559275)))
    assert reduce(gcd, (int(x) for x in f)) == 1
    assert det == [x / 1821870225 for x in f]
    c, b, a = f
    disc = b * b - 4 * a * c
    assert disc == 49164655493328292519326825
    lower_sqrt = 7011751242972
    assert lower_sqrt ** 2 < disc < (lower_sqrt + 1) ** 2
    assert data["determinant_kind"] == "QUADRATIC_TWO_IRRATIONAL"
    roots = data["root_certifications"]
    assert len(roots) == 2
    intervals = ((R(-b - lower_sqrt - 1, 2 * a), R(-b - lower_sqrt, 2 * a)),
                 (R(-b + lower_sqrt, 2 * a), R(-b + lower_sqrt + 1, 2 * a)))
    for j, cert in enumerate(roots):
        description = cert["root"]
        assert list(map(R, description["minimal_polynomial_ascending"])) == f
        assert R(description["discriminant"]) == disc
        interval = tuple(map(R, description["isolation_open"]))
        assert interval == intervals[j] and interval[0] < interval[1]
        assert peval(f, interval[0]) * peval(f, interval[1]) < 0
        assert cert["rank"] == 1 and len(cert["trials"]) == 1
        # Each first-row entry is a nonzero rational affine polynomial.
        # Irreducibility of f makes both nonzero at both real embeddings.
        assert len(trim(m[0][0])) == len(trim(m[0][1])) == 2
        trial = cert["trials"][0]
        kernel = [algebra_element(z) for z in trial["normalized_kernel_v_w"]]
        assert len(kernel) == 2 and kernel[0] == [R(1)]
        residual = [pmod(padd(pmul(row[0], kernel[0]), pmul(row[1], kernel[1])), f)
                    for row in m]
        supplied = [pmod(padd(pmul(row[0], kernel[0]), pmul(row[1], kernel[1])), f)
                    for row in wmat]
        assert residual == [[R(0)]] * 3
        assert residual == [algebra_element(z) for z in trial["M_stripped"]]
        assert supplied == [algebra_element(z) for z in trial["W_stripped"]]
        assert supplied[0] != [R(0)] and len(supplied[0]) == 2
        assert trial["W_nonzero"] is True and cert["passed_algebra"] is True
    assert intervals[0][1] < intervals[1][0]
    assert data["selected_root_index_zero_based"] == 0
    assert data["outcome"] == "ALGEBRA_PASS_ONLY"
    return {"verdict": "PASS_FIXED_CERTIFICATE_ONLY", "counts": counts,
            "all_six_probe_records_exact": True, "both_full_matrices_exact": True,
            "irreducible_two_root_certificate_exact": True,
            "both_normalized_kernels_and_full_W_exact": True,
            "no_positive_time_NS_claim": True}


def deadline(signum, frame):
    raise TimeoutError("Single verification exceeded 60 seconds")


def main():
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, deadline)
    signal.alarm(60)
    record = {"review_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "input_bindings": BOUND,
              "command": "/usr/bin/python3 research/reverse/four-carrier-source-test/independent_review_verify.py",
              "environment": {"python": sys.version, "executable": sys.executable,
                              "uname": list(os.uname()), "logical_cpu_count": os.cpu_count(),
                              "scientific_workers": 1, "scientific_threads": 1,
                              "arithmetic": "Fraction and exact integers",
                              "third_party_libraries": [], "subprocesses_started_by_verifier": 0},
              "scope": "One fixed stopped certificate; no new probes, chart or timestep"}
    status = 0
    try:
        record["verification"] = verify()
        record["execution_status"] = "completed"
    except Exception:
        status = 1
        record["execution_status"] = "NOT_CERTIFIED"
        record["error"] = traceback.format_exc()
    finally:
        signal.alarm(0)
        usage = resource.getrusage(resource.RUSAGE_SELF)
        peak = usage.ru_maxrss if sys.platform == "darwin" else 1024 * usage.ru_maxrss
        record["resources"] = {"wall_seconds_before_serialization": time.perf_counter() - started,
                               "self_user_cpu_seconds": usage.ru_utime,
                               "self_system_cpu_seconds": usage.ru_stime,
                               "self_peak_resident_bytes": peak,
                               "metadata_only": True, "not_process_tree_resource_accounting": True}
        if peak >= 256 * 1024 * 1024:
            status = 1
            record["execution_status"] = "NOT_CERTIFIED_RESOURCE_LIMIT"
        text = json.dumps(record, ensure_ascii=False, indent=2) + "\n"
        if len(text.encode("utf-8")) >= 1024 * 1024:
            status = 1
            text = json.dumps({"execution_status": "NOT_CERTIFIED_OUTPUT_LIMIT",
                               "review_source_sha256": record["review_source_sha256"]}) + "\n"
        OUT.write_text(text, encoding="utf-8")
        print(json.dumps({"execution_status": record["execution_status"],
                          "verification": record.get("verification"), "resources": record["resources"],
                          "output_sha256": hashlib.sha256(OUT.read_bytes()).hexdigest()}, indent=2))
    return status


if __name__ == "__main__":
    sys.exit(main())
