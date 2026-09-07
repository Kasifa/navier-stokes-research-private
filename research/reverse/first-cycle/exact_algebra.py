#!/usr/bin/env python3
"""PRIVATE_CORE. Exact finite jets of the full Fourier--Leray NS equation.

No spectral truncation is used: each finite polynomial convolution is exhausted.
Every rational is represented exactly; no floating-point physics is evaluated.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
import argparse
import json
from pathlib import Path


@dataclass(frozen=True)
class QI:
    re: F = F(0)
    im: F = F(0)

    def __add__(self, other):
        other = as_qi(other)
        return QI(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return QI(-self.re, -self.im)

    def __sub__(self, other):
        return self + -as_qi(other)

    def __mul__(self, other):
        other = as_qi(other)
        return QI(self.re*other.re-self.im*other.im,
                  self.re*other.im+self.im*other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_qi(other)
        d = other.re**2 + other.im**2
        return self * QI(other.re/d, -other.im/d)

    def conj(self):
        return QI(self.re, -self.im)

    def __bool__(self):
        return bool(self.re or self.im)

    def pack(self):
        return {"re": str(self.re), "im": str(self.im)}


def as_qi(x):
    return x if isinstance(x, QI) else QI(F(x))


ZERO = (QI(), QI(), QI())
MINUS_I = QI(F(0), F(-1))


def vec(a):
    return tuple(as_qi(v) for v in a)


def vadd(a, b):
    return tuple(x+y for x, y in zip(a, b))


def vmul(s, a):
    return tuple(s*x for x in a)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), QI())


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def p_leray(k, a):
    if not any(k):
        return a
    return vadd(a, vmul(-dot(a, k)/sum(x*x for x in k), vec(k)))


def prune(a):
    return {k: v for k, v in a.items() if any(v)}


def fadd(*fields):
    out = {}
    for field in fields:
        for k, v in field.items():
            out[k] = vadd(out.get(k, ZERO), v)
    return prune(out)


def fmul(s, field):
    return prune({k: vmul(s, v) for k, v in field.items()})


def component_l1_upper(field):
    """Bounds sum_k ||v_k||_2 by sum_{k,j} (|Re v_kj|+|Im v_kj|)."""
    return sum((abs(z.re)+abs(z.im) for v in field.values() for z in v), F(0))


def bilinear(a, b, target=None, project=True):
    out, contributions = {}, []
    for p, ap in sorted(a.items()):
        for q, bq in sorted(b.items()):
            k = tuple(x+y for x, y in zip(p, q))
            raw = vmul(dot(ap, q), bq)
            value = vmul(MINUS_I, p_leray(k, raw) if project else raw)
            out[k] = vadd(out.get(k, ZERO), value)
            if target == k:
                contributions.append({"p": p, "q": q,
                    "a_p": pack_vec(ap), "b_q": pack_vec(bq),
                    "a_p_dot_q": dot(ap, q).pack(),
                    "raw_before_projection": pack_vec(raw),
                    "contribution": pack_vec(value)})
    return prune(out), contributions


def B(a, b):
    return bilinear(a, b)[0]


def L(a, nu=F(1)):
    return prune({k: vmul(-nu*sum(x*x for x in k), v)
                  for k, v in a.items()})


def pack_vec(a):
    return [x.pack() for x in a]


def pack_field(a):
    return [{"k": k, "value": pack_vec(v)} for k, v in sorted(a.items())]


def allowed(a):
    return (not any(a.get((0, 0, 0), ZERO))
        and all(not dot(v, k) for k, v in a.items())
        and all(a.get(tuple(-x for x in k), ZERO)
                == tuple(z.conj() for z in v) for k, v in a.items()))


def cyclic_seed(amplitudes=(1, 1, 1)):
    a = {}
    for k, v, amplitude in zip(((1,0,0),(0,1,0),(0,0,1)),
                                 ((0,1,0),(0,0,1),(1,0,0)), amplitudes):
        a[k] = vmul(as_qi(amplitude), vec(v))
        a[tuple(-x for x in k)] = tuple(z.conj() for z in a[k])
    return a


def calculation():
    a = cyclic_seed()
    n = B(a, a)
    ba_n, bn_a = B(a, n), B(n, a)
    c = fadd(ba_n, bn_a)
    la = L(a)
    jet_terms = {"L2a": L(la), "LN": L(n),
                 "B_a_La": B(a, la), "B_La_a": B(la, a), "C": c}
    first = fadd(la, n)
    second = fadd(*jet_terms.values())
    b, d = first, second
    residual = {
        "t2": fadd(fmul(F(-1,2), L(d)), fmul(-1, B(b,b)),
                    fmul(F(-1,2), fadd(B(a,d), B(d,a)))),
        "t3": fmul(F(-1,2), fadd(B(b,d), B(d,b))),
        "t4": fmul(F(-1,4), B(d,d)),
    }
    candidates = [k for k in sorted(c) if k not in a and k not in n]
    target = (2, 1, 0) if (2, 1, 0) in candidates else candidates[0]
    first_target = (1,1,0)
    qtriple = ((2,1,0),(0,2,1),(1,0,2))
    gram = [[sum(x*y for x,y in zip(p,q)) for q in qtriple] for p in qtriple]
    determinant = sum(qtriple[0][i]*(qtriple[1][(i+1)%3]*qtriple[2][(i+2)%3]
                        -qtriple[1][(i+2)%3]*qtriple[2][(i+1)%3]) for i in range(3))
    pressure_target = (1,1,-1)
    n_no_leray = bilinear(a,a,project=False)[0]
    c_no_leray = fadd(bilinear(a,n_no_leray,project=False)[0],
                     bilinear(n_no_leray,a,project=False)[0])
    reduced_seed = {k:v for k,v in a.items() if k not in ((0,0,1),(0,0,-1))}
    reduced_n = B(reduced_seed,reduced_seed)
    reduced_b = fadd(L(reduced_seed),reduced_n)
    reduced_c = fadd(L(reduced_b),B(reduced_seed,reduced_b),B(reduced_b,reduced_seed))
    reduced_C = fadd(B(reduced_seed,reduced_n),B(reduced_n,reduced_seed))
    tagged = {}
    for name, left, right in (("B_a_N", a, n), ("B_N_a", n, a)):
        tagged[name] = bilinear(left, right, target)[1]
    results = {
        "schema": "ReverseNS-exact-fourier-jets-v1", "classification": "PRIVATE_CORE",
        "equation": "u'=L u+B(u,u); B_k(a,b)=-i P_k sum_{p+q=k}(a_p dot q)b_q",
        "torus": "(R/(2*pi*Z))^3", "viscosity": "1", "forcing": "0",
        "coefficient_convention": "u(x)=sum_k uhat(k) exp(i k dot x)",
        "seed_physical": "u0(x)=2*(cos(x3),cos(x1),cos(x2))",
        "seed_trials": 1, "spectral_truncation": False,
        "seed": pack_field(a), "N_Baa": pack_field(n), "C": pack_field(c),
        "B_N_a_full": pack_field(bn_a),
        "uprime0": pack_field(first), "usecond0": pack_field(second),
        "component_l1_upper_bounds": {"a": str(component_l1_upper(a)),
                                      "b": str(component_l1_upper(b)),
                                      "c": str(component_l1_upper(d)),
             **{name: str(component_l1_upper(f)) for name,f in residual.items()}},
        "residual_convention": "U'-LU-B(U,U)=t^2 r2+t^3 r3+t^4 r4; U=a+t b+t^2 c/2",
        "residual_coefficients": {name: pack_field(f) for name,f in residual.items()},
        "zero_first_nonzero_second_targets": [list(k) for k in candidates],
        "target": target, "target_a": pack_vec(a.get(target, ZERO)),
        "target_N": pack_vec(n.get(target, ZERO)),
        "target_C": pack_vec(c[target]),
        "target_uprime0": pack_vec(first.get(target, ZERO)),
        "target_usecond0": pack_vec(second[target]),
        "target_second_derivative_terms": {name: pack_vec(f.get(target, ZERO))
                                            for name, f in jet_terms.items()},
        "target_ordered_contributions": tagged,
        "first_target": {
            "k": first_target,
            "a": pack_vec(a.get(first_target,ZERO)),
            "N": pack_vec(n.get(first_target,ZERO)),
            "b": pack_vec(b.get(first_target,ZERO)),
            "c": pack_vec(d.get(first_target,ZERO)),
            "all_seed_pair_contributions": bilinear(a,a,first_target)[1]},
        "specific_three_mode_similarity_obstruction": {
            "q": qtriple, "frequency_gram": gram,
            "frequency_matrix_determinant": determinant,
            "gram_determinant": determinant**2,
            "positive_and_negative_second_derivative": [
                {"k": k, "c": pack_vec(d.get(k,ZERO))}
                for q in qtriple for k in (q,tuple(-x for x in q))],
            "scope": "Only this selected output triple cannot be a scalar times orthogonal image of the original orthonormal wavevectors. No exclusion of anisotropic, larger-packet, changed-profile, or other-seed mechanisms."},
        "pressure_projection_diagnostic": {
            "k": pressure_target,
            "C_full_leray": pack_vec(c.get(pressure_target,ZERO)),
            "C_without_leray": pack_vec(c_no_leray.get(pressure_target,ZERO)),
            "all_a_N_contributions": bilinear(a,n,pressure_target)[1],
            "all_N_a_contributions": bilinear(n,a,pressure_target)[1],
            "not_detected_by_target_only_comparison": c_no_leray[target] == c[target]},
        "globally_smooth_reduced_seed_negative_control": {
            "seed_physical": "a_red=(0,2*cos(x1),2*cos(x2))",
            "definition": "Delete only original seed modes +(0,0,1) and -(0,0,1); not a candidate search.",
            "seed": pack_field(reduced_seed),
            "j": first_target, "j_N": pack_vec(reduced_n.get(first_target,ZERO)),
            "j_c": pack_vec(reduced_c.get(first_target,ZERO)),
            "k": target, "k_C": pack_vec(reduced_C.get(target,ZERO)),
            "k_c": pack_vec(reduced_c.get(target,ZERO)),
            "j_and_k_observations_match_full_seed":
                reduced_n.get(first_target,ZERO)==n.get(first_target,ZERO)
                and reduced_c.get(first_target,ZERO)==d.get(first_target,ZERO)
                and reduced_C.get(target,ZERO)==c.get(target,ZERO)
                and reduced_c.get(target,ZERO)==d.get(target,ZERO),
            "invariant_class": "x3-independent triangular 2D3C: u=(0,2*exp(-nu*t)*cos(x1),w(t,x1,x2)); w solves a scalar linear advection-diffusion equation with smooth bounded coefficients.",
            "scope": "The selected two-generation observations alone do not distinguish the full 3D seed from this globally smooth class. This control is not a claim of global regularity for the full 3D seed."},
        "invariant_class_checks": {
            "support_spans_R3": True,
            "proof_no_invariant_spatial_direction": "n dot e_j=0 for j=1,2,3 implies n=0",
            "not_plane_supported_2d_or_2d3c": True,
            "not_constant_curl_eigenfield": True,
            "constant_curl_eigenfield_witness": {
                "k": [1,0,0], "a_k": pack_vec(a[(1,0,0)]),
                "curl_k": pack_vec(vmul(-MINUS_I, cross(vec((1,0,0)), a[(1,0,0)])))},
            "not_projected_nonlinearity_zero": bool(n),
            "not_single_direction_parallel_shear": True,
            "exhaustive_global_smooth_class_exclusion": False},
        "checks": {
            "seed_allowed": allowed(a), "N_allowed": allowed(n),
            "new_generation_advection_is_projected_gradient": not bn_a,
            "C_allowed": allowed(c), "first_allowed": allowed(first),
            "second_allowed": allowed(second),
            "target_absent_in_seed": target not in a,
            "target_absent_in_N": target not in n,
            "target_C_nonzero": any(c[target]),
            "target_second_equals_C": second[target] == c[target],
            "differentiated_equation_second_derivative": second == fadd(L(first),B(a,first),B(first,a)),
            "residual_constant_zero": fadd(b,fmul(-1,la),fmul(-1,n)) == {},
            "residual_linear_zero": fadd(d,fmul(-1,L(b)),fmul(-1,B(a,b)),fmul(-1,B(b,a))) == {},
            "pressure_projection_control_expected": c.get(pressure_target,ZERO) == ZERO and c_no_leray[pressure_target] == vec((2,2,-2)),
            "negative_control_removing_leray_detected": c_no_leray != c,
            "specific_triple_nonorthogonal": gram == [[5,2,2],[2,5,2],[2,2,5]],
            "reduced_seed_allowed": allowed(reduced_seed),
            "globally_smooth_control_same_jk_jets":
                reduced_n.get(first_target,ZERO)==n.get(first_target,ZERO)
                and reduced_c.get(first_target,ZERO)==d.get(first_target,ZERO)
                and reduced_C.get(target,ZERO)==c.get(target,ZERO)
                and reduced_c.get(target,ZERO)==d.get(target,ZERO),
            "unit_frequency_linear_jet_identity": second == fadd(a, {k:vmul(-sum(x*x for x in k)-2,v) for k,v in n.items()}, c)},
        "claim_boundary": "Exact algebraic jet only. Quantitative full-PDE remainder and novelty audit are separate. No singularity, uniform iteration, high-band relay dominance, or infinite cascade claim.",
    }
    assert all(results["checks"].values())
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("algebra-result.json"))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = json.dumps(calculation(), ensure_ascii=False, indent=2, sort_keys=True)+"\n"
    if args.check:
        assert args.output.read_text() == text, "certificate differs"
        print("PASS exact Fourier jets and byte-identical certificate")
    else:
        args.output.write_text(text)
        result = json.loads(text)
        print(json.dumps({"target": result["target"], "C": result["target_C"],
                          "counts": {k: len(result[k]) for k in ("seed", "N_Baa", "C")},
                          "checks": result["checks"]}))


if __name__ == "__main__":
    main()
