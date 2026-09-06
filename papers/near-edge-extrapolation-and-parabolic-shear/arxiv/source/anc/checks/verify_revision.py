#!/usr/bin/env python3
"""Finite exact algebra for v2. These checks are not proofs of limits.

Independent monomial, endpoint-recurrence, binomial and hypergeometric
representations are compared. Mutations test that the checks discriminate.
No third-party dependency is needed.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import importlib.util
import json
import platform
import sys
import time

LEGACY = Path(__file__).resolve().with_name('verify_algebra.py')
spec = importlib.util.spec_from_file_location('legacy_fixture', LEGACY)
v1 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = v1
spec.loader.exec_module(v1)


def rising(a, j):
    out = F(1)
    for k in range(j):
        out *= a+k
    return out


def hyper_heat(m, A, s, kind='T', wrong_denominator=False):
    if kind == 'T':
        top = [F(-m, 2), F(1-m, 2), F(m, 2), F(m+1, 2)]
        bottom = [F(1, 4), F(3, 4)]
    else:
        top = [F(-m, 2), F(1-m, 2), F(m+2, 2), F(m+3, 2)]
        bottom = [F(3, 4), F(5, 4)]
    if wrong_denominator:
        bottom[0] += F(1, 2)
    total = F(0)
    for j in range(m//2+1):
        t = (s/A**2)**j / factorial(j)
        for a in top:
            t *= rising(a, j)
        for b in bottom:
            t /= rising(b, j)
        total += t
    return total


def unorm_coeff(m):
    out = [F(0)] * (m+1)
    for k in range(m//2+1):
        out[m-2*k] = F((-1)**k * comb(m-k, k) * 2**(m-2*k), m+1)
    return out


def unorm_endpoints(m):
    ds = [F(1)]
    for k in range(m):
        ds.append(ds[-1]*F((m-k)*(m+k+2), 2*k+3))
    return ds


def derivative_heat_from_endpoints(ds, A, s, c):
    return sum((ds[ell+2*j]*c**ell*s**j /
                (A**(ell+2*j)*factorial(ell)*factorial(j))
                for ell in range(len(ds))
                for j in range((len(ds)-1-ell)//2+1)), F(0))


def temporal_formula(N):
    eps = F(1, N*N)
    return [(-1)**j / (F(factorial(j))*eps**j) *
            sum((1/(eps**h*factorial(h)) for h in range(N-j)), F(0))
            for j in range(N)]


def temporal_expansion(N):
    eps = F(1, N*N)
    out = [F(0)]*N
    # Build successive powers of (1-z)/eps by polynomial multiplication.
    row = [F(1)]
    for k in range(N):
        for j, value in enumerate(row):
            out[j] += value/factorial(k)
        new = [F(0)]*(len(row)+1)
        for j, value in enumerate(row):
            new[j] += value/eps
            new[j+1] -= value/eps
        row = new
    return out


def main():
    start = time.perf_counter()
    checks = v1.Checks()
    for m in range(25):
        uc = unorm_coeff(m)
        ds = unorm_endpoints(m)
        for k in range(m+1):
            checks.equal('U_endpoint_recurrence', ds[k],
                         v1.derivative_value(uc, k, F(1)), (m, k))
        for A in (F(2), F(7, 2)):
            for s in (F(0), F(1, 3), F(4)):
                for c in (F(-2), F(0), F(3, 2)):
                    checks.equal('U_heat_two_representations',
                                 derivative_heat_from_endpoints(ds, A, s, c),
                                 v1.heat_by_gaussian_moments(uc, s/A**2, 1+c/A),
                                 (m, A, s, c))
                for kind, coeff in [('T', v1.chebyshev_closed(m)), ('U', uc)]:
                    expected = v1.heat_by_gaussian_moments(coeff, s/A**2, F(1))
                    checks.equal('terminating_hypergeometric',
                                 hyper_heat(m, A, s, kind), expected, (kind, m, A, s))
                    if m >= 2 and s:
                        checks.reject('mutated_hypergeometric_lower_parameter',
                                      hyper_heat(m, A, s, kind, True), expected,
                                      (kind, m, A, s))
        if m:
            checks.reject('mutated_U_normalization',
                          (m+1)*v1.derivative_value(uc, 0, F(1)), F(1), m)

    for N in range(1, 25):
        bs = temporal_formula(N)
        checks.equal('time_binomial_identity', bs, temporal_expansion(N), N)
        checks.equal('time_initial_value', sum(bs), F(1), N)
        checks.record('time_all_nonzero', all(x for x in bs), N)
        rates = [1+F(j, N*N) for j in range(N)]
        checks.record('time_decay_interval', len(set(rates)) == N and
                      min(rates) >= 1 and max(rates) <= F(5, 4), N)
        if N >= 2:
            checks.reject('mutated_coefficient_sign', [abs(x) for x in bs],
                          temporal_expansion(N), N)
    checks.equal('N1_witness', temporal_formula(1), [F(1)], 'N=1')
    checks.equal('time_lower_constant', F(1, 16)*F(1, 8), F(1, 128), 'N² factor')

    for a in (F(2), F(10), F(100)):
        for delta in (F(1, 3), F(1)):
            # Remove pi R^5: 4 time units times shell volume coefficient.
            vol = F(16, 3)*((a+delta)**3-(a-delta)**3)
            checks.equal('full_volume', vol, 32*delta*a*a*(1+delta**2/(3*a*a)), (a,delta))
    for gamma in (F(1), F(2, 3969)):
        for p in (F(1), F(32, 63)):
            for gap in (F(1), F(3, 2)):
                k2 = gamma**2*p/(2592*gap)  # (gamma/(36 sqrt2))² p/gap
                checks.equal('new_sufficient_threshold', 288*k2*gap/p,
                             (gamma/3)**2, (gamma,p,gap))
                checks.reject('mutated_old_threshold',
                              288*(gamma**2*p/(7200*gap))*gap/p,
                              (gamma/3)**2, (gamma,p,gap))
    checks.equal('new_flux_exponent', F(3)*2*2, F(12), 'square and 2q branches')
    checks.equal('full_velocity_R_power', F(1,3)+3-F(4,3), F(2), 'R²')
    checks.equal('full_velocity_rate', -2*F(9,40000), -F(9,20000), 'log rate')
    checks.equal('bounded_drift_R_power', F(1,3)+4-F(10,3), F(1), 'R')
    checks.equal('amplitude_lambda_R_error', 2*(-1+2), F(2), 'B/R^-2')
    result = {'status':'PASS','classification':'FINITE COMPUTATION',
              'scope':'Exact finite identities and targeted mutations; not asymptotic proofs',
              'python':platform.python_version(),'hardware':platform.machine(),
              'arithmetic':'Fraction, exact integers','workers':1,'random_seed':None,
              'elapsed_seconds':round(time.perf_counter()-start,3),
              'fixture_sha256':hashlib.sha256(LEGACY.read_bytes()).hexdigest(),
              'groups':checks.groups,
              'positive_checks':sum(g['positive'] for g in checks.groups.values()),
              'negative_checks':sum(g['negative'] for g in checks.groups.values())}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
