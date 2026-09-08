#!/usr/bin/env python3
"""One bounded difference-response certificate; prepare/read only until authorized.

No old script is imported or called. The only Fourier calculation is the full
12 x 12 ordered first gate, filtered to the six fixed differences. The root
algorithm is MP.1--7; the window is MP.10 / DR.8, never DI.15.
"""
import time

ENTRY_TIME = time.perf_counter()

import argparse
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys

WALL_SECONDS = 60
RSS_BYTES = 256 * 1024 * 1024
OUTPUT_BYTES = 1024 * 1024
NEW_BISECTIONS = 32
WORKTREE = Path('/Users/kasifa/Documents/Math/navier-stokes-reverse')
HERE = WORKTREE / 'research/reverse/cyclic-difference-response'
OLD = WORKTREE / 'research/reverse/cyclic-six-carrier'
A_SHA = '9329464c09faa50558bc090b3af8c3ec6f074619e01a9fe2d5eb6d0f1c079ae6'
B_SHA = '6fd933ebd18bdf8b129f7cabdbf1f02438de3fd95f9720b18e41887815f31bcb'
TEXT_SHA = {
    'CONTRACT.md': 'a1b50ab4293c9d6132a874ed574b7843d0deae672a8928f73d1b9dcc7c09fed6',
    'METHOD_PREFLIGHT.md': 'f2c7d90186f083601cab5bc5411d5c60826b963d6ed29efe9e4dfde5e149c316',
    'ANALYSIS.md': 'fdf1a250da8a8f02e3343000f206e9f4f45fe159fb7b7352171d4e08b0fe3367',
    'INDEPENDENT.md': '68957784dd943eca6968973aeb61a49e4453a3410b816c67e59d4f61384eedc4',
    'CONTRACT_REVIEW.md': '791c80270135a1a08e6aea43840cdde8dd5faa0ddc71c6c767d8f3efcc892a73',
    'ANALYSIS_REVIEW.md': '02288305451808829feace3ac1f97480ee7cf1f918e011cbbe5a2c9f1cc7080c',
    'INDEPENDENT_REVIEW.md': 'f8db95b2549d02c9f28fc84fa8d78ef65c235c646743015194a452a18b4a8b04',
}


class NotCertified(Exception):
    pass


class Inconsistent(NotCertified):
    pass


def require(ok, reason):
    if not ok:
        raise Inconsistent(reason)


def snapshot():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    rss = usage.ru_maxrss if sys.platform == 'darwin' else usage.ru_maxrss * 1024
    return {'wall_seconds_since_entry': time.perf_counter() - ENTRY_TIME,
            'RSS_SELF_bytes': rss, 'user_CPU_seconds': usage.ru_utime,
            'system_CPU_seconds': usage.ru_stime}


def check_budget():
    sample = snapshot()
    if sample['wall_seconds_since_entry'] >= WALL_SECONDS:
        raise NotCertified('WALL_LIMIT_EXCEEDED')
    if sample['RSS_SELF_bytes'] > RSS_BYTES:
        raise NotCertified('SELF_RSS_TARGET_EXCEEDED')


def alarm_handler(signum, frame):
    raise NotCertified('WALL_LIMIT_SIGNAL')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def poly(values):
    values = tuple(F(x) for x in values) or (F(0),)
    while len(values) > 1 and values[-1] == 0:
        values = values[:-1]
    return values


ZERO, ONE, ALPHA = poly((0,)), poly((1,)), poly((0, 1))


def degree(p):
    return -1 if p == ZERO else len(p) - 1


def add(a, b):
    return poly((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                for i in range(max(len(a), len(b))))


def scale(a, c):
    return poly(c * x for x in a)


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    check_budget()
    result = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return poly(result)


def power(a, n):
    require(n >= 0, 'negative polynomial power')
    result = ONE
    for unused in range(n):
        result = mul(result, a)
    return result


def derivative(a):
    return poly(i * a[i] for i in range(1, len(a)))


def divide(a, b):
    require(b != ZERO, 'polynomial division by zero')
    remainder = a
    quotient = [F(0)] * max(1, degree(a) - degree(b) + 1)
    while remainder != ZERO and degree(remainder) >= degree(b):
        check_budget()
        shift = degree(remainder) - degree(b)
        coefficient = remainder[-1] / b[-1]
        quotient[shift] += coefficient
        remainder = sub(remainder, (F(0),) * shift + scale(b, coefficient))
    quotient = poly(quotient)
    require(add(mul(quotient, b), remainder) == a, 'long division identity')
    return quotient, remainder


def evaluate(a, x):
    check_budget()
    result = F(0)
    for c in reversed(a):
        result = result * x + c
    return result


def encode_poly(a):
    return {'coefficients_low_to_high': [str(x) for x in a], 'degree': degree(a)}


def decode_poly(record):
    p = poly(record['coefficients_low_to_high'])
    require(record['degree'] == degree(p), 'stored polynomial degree mismatch')
    return p


def extended_gcd(a, b):
    left, right = a, b
    x0, x1, y0, y1 = ONE, ZERO, ZERO, ONE
    steps = []
    while right != ZERO:
        check_budget()
        quotient, remainder = divide(left, right)
        steps.append({'left': encode_poly(left), 'right': encode_poly(right),
                      'quotient': encode_poly(quotient), 'remainder': encode_poly(remainder)})
        left, right = right, remainder
        x0, x1 = x1, sub(x0, mul(quotient, x1))
        y0, y1 = y1, sub(y0, mul(quotient, y1))
    require(left != ZERO, 'gcd of two zero polynomials outside domain')
    monic_multiplier = 1 / left[-1]
    d = scale(left, monic_multiplier)
    bezout_a, bezout_b = scale(x0, monic_multiplier), scale(y0, monic_multiplier)
    quotient_a, rem_a = divide(a, d)
    quotient_b, rem_b = divide(b, d)
    require(rem_a == rem_b == ZERO, 'gcd is not common divisor')
    require(add(mul(bezout_a, a), mul(bezout_b, b)) == d, 'Bezout identity failed')
    return d, {'inputs': [encode_poly(a), encode_poly(b)], 'D_monic': encode_poly(d),
               'input_quotients_by_D': [encode_poly(quotient_a), encode_poly(quotient_b)],
               'Bezout_A': encode_poly(bezout_a), 'Bezout_B': encode_poly(bezout_b),
               'Euclid_steps': steps,
               'final_monic_multiplier_not_Sturm_scaling': str(monic_multiplier),
               'three_gcd_identities_verified': True}


def sturm_new(d):
    require(d != ZERO and d[-1] == 1, 'local Sturm input must be nonzero monic')
    chain = [d]
    record = {'input': encode_poly(d), 'S0_multiplier': '1',
              'S1_positive_multiplier_of_derivative': '1', 'steps': []}
    if degree(d) == 0:
        record.update(polynomials=[encode_poly(d)], constant_root_count=0)
        return chain, record
    chain.append(derivative(d))
    while True:
        check_budget()
        quotient, remainder = divide(chain[-2], chain[-1])
        if remainder == ZERO:
            require(degree(chain[-1]) == 0, 'local gcd divisor was not square-free')
            record['terminal_quotient'] = encode_poly(quotient)
            record['terminal_remainder'] = encode_poly(ZERO)
            break
        following = scale(remainder, -1)
        record['steps'].append({'quotient': encode_poly(quotient),
                                'positive_multiplier': '1', 'next': encode_poly(following)})
        chain.append(following)
    record['polynomials'] = [encode_poly(p) for p in chain]
    return chain, record


def endpoint(chain, x):
    values = [evaluate(p, x) for p in chain]
    signs = [(value > 0) - (value < 0) for value in values]
    nonzero = [sign for sign in signs if sign]
    changes = sum(a != b for a, b in zip(nonzero, nonzero[1:]))
    return {'x': str(x), 'values': [str(v) for v in values],
            'signs': signs, 'variation_after_deleting_zeros': changes}


def root_count(chain, a, b):
    require(a < b, 'root interval must be nonempty (a,b]')
    ea, eb = endpoint(chain, a), endpoint(chain, b)
    return {'interval': [str(a), str(b)], 'ownership': '(a,b]',
            'left_endpoint': ea, 'right_endpoint': eb,
            'count': ea['variation_after_deleting_zeros'] - eb['variation_after_deleting_zeros']}


def interval_horner(p, a, b):
    require(a <= b, 'invalid closed enclosure')
    low, high = F(0), F(0)
    steps = []
    for coefficient in reversed(p):
        check_budget()
        products = (low * a, low * b, high * a, high * b)
        low, high = min(products) + coefficient, max(products) + coefficient
        steps.append({'coefficient': str(coefficient),
                      'four_products': [str(v) for v in products],
                      'result': [str(low), str(high)]})
    return low, high, steps


# Sparse formal polynomials in (alpha,v,w), with rational coefficients.
def formal(terms):
    return {tuple(exponent): F(c) for exponent, c in terms.items() if c}


def fadd(a, b):
    result = dict(a)
    for exponent, c in b.items():
        result[exponent] = result.get(exponent, F(0)) + c
    return formal(result)


def fscale(a, c):
    return formal({exponent: c * x for exponent, x in a.items()})


def fmul(a, b):
    check_budget()
    result = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            exponent = tuple(x + y for x, y in zip(ea, eb))
            result[exponent] = result.get(exponent, F(0)) + ca * cb
    return formal(result)


def fsum(values):
    result = {}
    for value in values:
        result = fadd(result, value)
    return result


def fdot(k, vector):
    return fsum(fscale(c, x) for x, c in zip(k, vector))


def encode_formal(p):
    return [{'alpha_v_w_exponents': list(e), 'coefficient': str(c)}
            for e, c in sorted(p.items())]


def encode_vector(vector):
    return [encode_formal(p) for p in vector]


def substitute(p, v, w):
    result = ZERO
    for (ia, iv, iw), coefficient in p.items():
        term = mul(power(ALPHA, ia), mul(power(v, iv), power(w, iw)))
        result = add(result, scale(term, coefficient))
    return result


def rotate(x, times=1):
    for unused in range(times % 3):
        x = (x[2], x[0], x[1])
    return x


def negate(k):
    return tuple(-x for x in k)


def norm_squared(k):
    return sum(x * x for x in k)


def new_coefficients(report, v, w, Q):
    one = formal({(0, 0, 0): 1})
    alpha = formal({(1, 0, 0): 1})
    vf, wf = formal({(0, 1, 0): 1}), formal({(0, 0, 1): 1})
    low, high = ({}, one, alpha), (fadd(fscale(vf, 3), fscale(wf, 5)),
                                  fscale(vf, -2), fscale(wf, -2))
    modes = []
    for kind, frequency, vector in [('low', (1, 0, 0), low), ('high', (2, 3, 5), high)]:
        for j in range(3):
            for sign in (1, -1):
                k = rotate(frequency, j)
                k = k if sign == 1 else negate(k)
                amplitude = rotate(vector, j)
                require(fdot(k, amplitude) == {}, 'initial transversality')
                modes.append({'kind': kind, 'rotation': j, 'sign': sign,
                              'k': k, 'amplitude': amplitude})
    require(len({m['k'] for m in modes}) == 12, 'initial support not twelve distinct modes')
    by_k = {m['k']: m['amplitude'] for m in modes}
    require(all(by_k[negate(k)] == amp for k, amp in by_k.items()), 'real initial conjugacy')
    targets = [rotate((-3, 1, 2), j) for j in range(3)]
    targets += [negate(k) for k in targets]
    require(len(set(targets)) == 6, 'six differences not distinct')
    totals = {k: ({}, {}, {}) for k in targets}
    matched = {k: 0 for k in targets}
    data = {'formal_ring': 'Q[alpha,v,w], sparse exponent triples',
            'all_initial_phases': 'real; negative frequency is conjugate, not independent',
            'initial_modes': [{'k': list(m['k']), 'kind': m['kind'],
                               'amplitude': encode_vector(m['amplitude'])} for m in modes],
            'ordered_candidates': [], 'ordered_contributions': []}
    report['new_coefficients'] = data
    count = 0
    for ir, first in enumerate(modes):
        for js, second in enumerate(modes):
            check_budget()
            count += 1
            r, s = first['k'], second['k']
            k = tuple(x + y for x, y in zip(r, s))
            keep = k in totals
            data['ordered_candidates'].append({'first_mode': ir, 'second_mode': js,
                                               'sum': list(k), 'selected': keep})
            if not keep:
                continue
            dot = fdot(s, first['amplitude'])
            raw = tuple(fmul(dot, z) for z in second['amplitude'])
            square = norm_squared(k)
            require(square == 14, 'difference heat rate mismatch')
            matrix = tuple(tuple(F(int(i == j)) - F(k[i] * k[j], square)
                                 for j in range(3)) for i in range(3))
            projected = tuple(fsum(fscale(raw[j], matrix[i][j]) for j in range(3))
                              for i in range(3))
            require(fdot(k, projected) == {}, 'ordered projected vector not transverse')
            # B=-i P(raw); reporting G with physical phase +i requires G=-P(raw).
            g_term = tuple(fscale(z, -1) for z in projected)
            totals[k] = tuple(fadd(x, y) for x, y in zip(totals[k], g_term))
            matched[k] += 1
            data['ordered_contributions'].append({
                'first_mode': ir, 'second_mode': js, 'r': list(r), 's': list(s), 'target': list(k),
                'ordered_dot': encode_formal(dot), 'raw_vector': encode_vector(raw),
                'Leray_matrix': [[str(c) for c in row] for row in matrix],
                'projected_vector_with_phase_minus_i': encode_vector(projected),
                'G_contribution_with_phase_plus_i': encode_vector(g_term),
                'input_heat_rates': [norm_squared(r), norm_squared(s)], 'output_heat_rate': square})
            require(norm_squared(r) == norm_squared(s) == 38, 'unexpected initial birth pair')
    require(count == 144 and all(n == 2 for n in matched.values()), 'full ordered pair exhaustion')
    factor = fmul(fadd(fscale(vf, 3), fscale(wf, 2)), fadd(vf, fscale(wf, 3)))
    expected_base = tuple(fscale(factor, F(4 * x, 7)) for x in (-1, 19, -11))
    rows, quotients = [], []
    for index, k in enumerate(targets):
        check_budget()
        j, sign = index % 3, (1 if index < 3 else -1)
        expected = tuple(fscale(z, sign) for z in rotate(expected_base, j))
        vector = totals[k]
        require(vector == expected, 'computed full vector disagrees with reviewed factor')
        require(fdot(k, vector) == {}, 'full target transversality')
        require(all(ia == 0 and iv + iw == 2 for z in vector for ia, iv, iw in z),
                'formal coefficient is not alpha-independent homogeneous quadratic')
        normalized = tuple(substitute(z, v, w) for z in vector)
        require(all(degree(z) <= 6 for z in normalized), 'new alpha degree exceeds six')
        reductions = []
        for z in normalized:
            h, rem = divide(z, Q)
            reductions.append({'original_f': encode_poly(z), 'Q_quotient': encode_poly(h),
                               'remainder': encode_poly(rem), 'identity_verified': True})
        rows.append({'target': list(k), 'physical_phase': '+i', 'formal_G': encode_vector(vector),
                     'normalized_G': [encode_poly(z) for z in normalized], 'reductions_mod_Q': reductions})
        quotients.append(normalized)
    for j in range(3):
        require(totals[targets[j + 3]] == tuple(fscale(z, -1) for z in totals[targets[j]]),
                'negative conjugacy identity')
        require(totals[targets[j]] == rotate(totals[targets[0]], j), 'rotation identity')
    data.update(candidate_count=count, matched_ordered_count=sum(matched.values()),
                all_six_rows=rows, reviewed_factor=encode_formal(factor),
                full_vector_factor_rotation_conjugacy_transversality_verified=True,
                exact_common_heat_factor={'input_rate': 76, 'output_rate': 14, 'difference': 62,
                                          'formula': '(exp(-14t)-exp(-76t))/62',
                                          'heat_error_bound_from_ANALYSIS': '0<=t-J(t)<=45t^2'})
    return quotients[0]


def old_interfaces(report, a_data, b_data):
    catalog = {record['id']: record for record in b_data['polynomials']}
    def bp(index):
        return decode_poly(catalog[index])
    primary = a_data['primary_matrices']
    matrix = [[decode_poly(z) for z in row] for row in primary['M_first_two_Z_rows']]
    P = decode_poly(primary['P_determinant'])
    require(P == sub(mul(matrix[0][0], matrix[1][1]), mul(matrix[0][1], matrix[1][0])),
            'stored original determinant identity')
    r, s = matrix[0]
    require([r, s, P] == [bp(6), bp(7), bp(12)], 'A/B original r,s,P mismatch')
    Q = bp(13)
    require(degree(P) == 6 and Q[-1] == 1 and scale(P, 1 / P[-1]) == Q, 'fixed Q interface')
    require(b_data['original_inputs']['P'] == 12 and
            b_data['original_inputs']['M_unscaled'][0] == [6, 7], 'old original IDs')
    root = b_data['roots'][0]
    require(b_data['selected_root_index'] == root['index'] == 0, 'old root selection')
    require(root['initial_node'] == root['current_node'] == 13 and
            root['cumulative_bisection_depth'] == 7, 'old root node/depth interface')
    require(root['normalization']['original_r_s'] == [6, 7] and
            root['normalization']['original_row_index'] == 0, 'original row was replaced')
    require(root['normalized_polynomials']['v'] == 62 and root['normalized_polynomials']['w'] == 6,
            'original normalized polynomial IDs')
    v, w = scale(s, -1), r
    require(v == bp(62) and w == bp(6), 'original amplitudes changed')
    node = next(n for n in b_data['isolation_nodes'] if n['id'] == 13)
    a, b = F('-75/32'), F('-125/64')
    require(node['interval'] == [str(a), str(b)] and node['depth'] == 7 and node['count'] == 1,
            'fixed half-open interval interface')
    old_chain = b_data['sturm_chains'][0]
    ids = old_chain['polynomials']
    chain = [bp(index) for index in ids]
    c0, c1 = F(old_chain['S0_multiplier']), F(old_chain['S1_positive_multiplier_of_derivative'])
    require(old_chain['input'] == 13 and c0 == 1 and c1 > 0, 'old Q chain start')
    require(chain[0] == Q and chain[1] == scale(derivative(Q), c1), 'old Q derivative identity')
    steps = old_chain['negative_remainder_steps']
    require(len(steps) == len(chain) - 2, 'old Q chain length')
    chain_certificate = {'input': encode_poly(Q), 'old_chain_id': 0, 'old_polynomial_ids': ids,
                         'S0_multiplier': str(c0), 'S1_positive_multiplier_of_derivative': str(c1),
                         'polynomials': [encode_poly(z) for z in chain], 'steps': []}
    for i, record in enumerate(steps):
        check_budget()
        quotient, remainder = divide(chain[i], chain[i + 1])
        c = F(record['positive_multiplier'])
        require(c > 0 and quotient == bp(record['quotient']), 'old Q quotient/positive scale')
        require(chain[i + 2] == bp(record['next']) == scale(remainder, -c), 'old Q negative remainder')
        chain_certificate['steps'].append({'quotient': encode_poly(quotient),
                                           'positive_multiplier': str(c), 'next': encode_poly(chain[i + 2])})
    terminal, remainder = divide(chain[-2], chain[-1])
    require(degree(chain[-1]) == 0 and remainder == bp(old_chain['terminal_remainder']) == ZERO and
            terminal == bp(old_chain['terminal_quotient']), 'old Q terminal constant identity')
    chain_certificate.update(terminal_quotient=encode_poly(terminal), terminal_remainder=encode_poly(remainder),
                             square_free_Q_verified_by_terminal_constant=True)
    counted = root_count(chain, a, b)
    require(counted['count'] == 1 and counted['left_endpoint']['variation_after_deleting_zeros'] == 4 and
            counted['right_endpoint']['variation_after_deleting_zeros'] == 3, 'fixed root endpoint count')
    window = b_data['selected_window']
    A, bb, T = F(window['Abar']), F(window['bbar']), F(window['T'])
    Aalpha, Uv, Uw, UV1 = (F(window[name]) for name in ('Aalpha', 'Uv', 'Uw', 'UV1'))
    ell, Ebar, Dfirst = (F(window[name]) for name in ('ell', 'Ebar', 'Dfirst'))
    require(A == 6 * (1 + Aalpha + UV1 + 2 * Uv + 2 * Uw) and bb == 28 * A,
            'old norm definition interface')
    require(Ebar == 80 * A**4 * 7**5 + 3 * A * bb**4 and
            Dfirst == 2 * (1 + Aalpha**2) + 2 * A * bb**2, 'old budget definition interface')
    require(all(x > 0 for x in (A, bb, T, ell, Ebar, Dfirst)), 'old positive constants')
    old_times = (1 / (2 * bb), ell / (8 * Ebar), 1 / (2 * Dfirst))
    require(list(old_times) == [F(x) for x in window['three_time_candidates_in_contract_order']] and
            T == min(old_times) and bb * T <= F(1, 2), 'old T was replaced or budget failed')
    require(window['selected_root_index'] == 0 and window['final_root_node'] == 13,
            'old window root selection')
    report['old_interface'] = {
        'P': encode_poly(P), 'r_original': encode_poly(r), 's_original': encode_poly(s),
        'Q_global_not_minimal_polynomial': encode_poly(Q), 'v_minus_s': encode_poly(v), 'w_r': encode_poly(w),
        'old_root_index': 0, 'old_node': 13, 'old_depth': 7, 'interval': [str(a), str(b)],
        'old_IDs': {'P': 12, 'Q': 13, 'r': 6, 's': 7, 'v': 62, 'w': 6},
        'Q_chain_endpoint_certificate': counted,
        'inherited_selected_window_values': {name: window[name] for name in
            ('Abar', 'bbar', 'T', 'Aalpha', 'Uv', 'Uw', 'UV1', 'ell', 'Ebar', 'Dfirst')},
        'field_identities_verified_not_old_Fourier_reexecution': True}
    report['Sturm_chains'] = [chain_certificate]
    return Q, v, w, chain, a, b, A, bb, T


def classify_and_bound(report, fs, Q, chain, a, b):
    report['coordinate_zero_tests'] = []
    first = None
    for j, f in enumerate(fs):
        check_budget()
        quotient, rem = divide(f, Q)
        d, certificate = extended_gcd(Q, rem)
        if d == Q:
            local_chain, chain_index = chain, 0
        else:
            local_chain, chain_record = sturm_new(d)
            chain_index = len(report['Sturm_chains'])
            report['Sturm_chains'].append(chain_record)
        counted = root_count(local_chain, a, b)
        require(counted['count'] in (0, 1), 'gcd count not zero or one in fixed root interval')
        is_zero = counted['count'] == 1
        point_value = None
        if evaluate(Q, b) == 0:
            point_value = evaluate(f, b)
            require((point_value == 0) == is_zero, 'endpoint root exact value disagrees with gcd count')
        report['coordinate_zero_tests'].append({
            'coordinate_one_based': j + 1, 'original_f': encode_poly(f), 'Q_quotient': encode_poly(quotient),
            'remainder': encode_poly(rem), 'gcd_certificate': certificate, 'Sturm_chain': chain_index,
            'count_certificate': counted, 'zero_at_fixed_root': is_zero,
            'right_endpoint_root_exact_f_value': None if point_value is None else str(point_value)})
        if not is_zero:
            first = j
            break
    if first is None:
        report['certificate_status'] = 'FULL-TWO-LEAF-ZERO-CERTIFIED'
        report['root_coordinate_scope'] = 'All three tested zero; common heat factor gives first response only.'
        return None
    report['coefficient_nonzero_certified'] = True
    report['first_nonzero_coordinate_one_based'] = first + 1
    report['root_coordinate_scope'] = 'Only coordinates through first nonzero classified; all six full symbolic vectors retained.'
    report['certificate_status'] = 'NONZERO-COEFFICIENT-CERTIFIED / WINDOW-NOT-CERTIFIED'
    path, trace = [], []
    report['new_bisection_path'], report['closed_enclosure_trace'] = path, trace
    report['new_bisections_started'] = report['new_bisections_completed'] = 0
    n = 0
    while True:
        check_budget()
        is_point = evaluate(Q, b) == 0
        lo_input = b if is_point else a
        low, high, steps = interval_horner(fs[first], lo_input, b)
        separated = high < 0 or low > 0
        trace.append({'new_bisection_count': n, 'old_depth': 7, 'combined_depth': 7 + n,
                      'root_interval': [str(a), str(b)], 'ownership': '(a,b]',
                      'exact_right_endpoint_root': is_point,
                      'closed_input': [str(lo_input), str(b)], 'Horner_steps': steps,
                      'closed_output': [str(low), str(high)], 'strictly_avoids_zero': separated})
        if separated:
            delta = min(abs(low), abs(high))
            require(delta > 0, 'invalid coordinate lower endpoint')
            return {'coordinate_one_based': first + 1, 'original_polynomial': encode_poly(fs[first]),
                    'final_interval': [str(a), str(b)], 'closed_enclosure': [str(low), str(high)],
                    'delta': str(delta), 'd_two_mode_pair': str(2 * delta),
                    'new_bisection_count': n, 'old_depth': 7, 'combined_depth': 7 + n}
        require(not is_point, 'nonzero gcd contradicted by exact point value')
        if n == NEW_BISECTIONS:
            raise NotCertified('32_SHARED_NEW_BISECTIONS_EXHAUSTED_WITHOUT_COORDINATE_LOWER_BOUND')
        n += 1
        report['new_bisections_started'] = n
        middle = (a + b) / 2
        left = root_count(chain, a, middle)
        right = root_count(chain, middle, b)
        require(left['count'] in (0, 1) and right['count'] in (0, 1) and
                left['count'] + right['count'] == 1, 'same-root midpoint partition count')
        midpoint_zero = evaluate(Q, middle) == 0
        if midpoint_zero:
            require(left['count'] == 1, 'midpoint root must belong to left child')
        child = (a, middle) if left['count'] == 1 else (middle, b)
        path.append({'new_bisection_count': n, 'parent_interval': [str(a), str(b)],
                     'midpoint': str(middle), 'midpoint_is_Q_root': midpoint_zero,
                     'left_count_certificate': left, 'right_count_certificate': right,
                     'kept_interval': [str(x) for x in child],
                     'kept_side': 'left' if left['count'] else 'right', 'combined_depth': 7 + n})
        report['new_bisections_completed'] = n
        a, b = child


def new_window(report, bound, A, b, T):
    d = F(bound['d_two_mode_pair'])
    Q0 = 315 * A**2 + 2 * A * b**2
    C0 = F(32, 7) * A**2 * b**6
    candidates = (T, F(1), d / (2 * Q0), d / (8 * C0))
    require(all(x > 0 for x in (d, Q0, C0) + candidates), 'MP.10 positivity')
    tau = min(candidates)
    budgets = []
    for label, left, right in [('tau<=T_star', tau, T), ('tau<=1', tau, F(1)),
                                ('Q0*tau<=d/2', Q0 * tau, d / 2), ('C0*tau<=d/8', C0 * tau, d / 8)]:
        slack = right - left
        require(slack >= 0, 'MP.11 budget failed: ' + label)
        budgets.append({'name': label, 'left': str(left), 'right': str(right), 'slack': str(slack)})
    report['new_window'] = {
        'interface': 'MP.10 / DR.8, not DI.15', 'Abar_unchanged': str(A), 'bbar_unchanged': str(b),
        'T_star_unchanged': str(T), 'd': str(d), 'Q0': str(Q0), 'C0': str(C0),
        'four_candidates_in_contract_order': [str(x) for x in candidates],
        'tau': str(tau), 'minimum_attaining_indices_zero_based': [i for i, x in enumerate(candidates) if x == tau],
        'positive_constants_and_candidates_verified': True, 'exact_budgets': budgets,
        'same_d_for_each_signed_pair_by_verified_rotation_conjugacy': True,
        'norm': 'A0=sum of Hermitian Euclidean Fourier-vector norms',
        'conditional_conclusion': 'For each pair and total E_-, 0<t<=tau: P_E u nonzero and ||H||<=||P_E u||/4.',
        'H_may_be_zero_no_division_by_H': True, 'original_T_star_not_replaced': True}
    report['certificate_status'] = 'DIFFERENCE-WINDOW-CERTIFIED'


def scientific_stage(report, a_data, b_data):
    Q, v, w, chain, a, b, A, bb, T = old_interfaces(report, a_data, b_data)
    fs = new_coefficients(report, v, w, Q)
    bound = classify_and_bound(report, fs, Q, chain, a, b)
    if bound is not None:
        report['new_coordinate_lower_bound'] = bound
        new_window(report, bound, A, bb, T)


def json_bytes(report):
    return (json.dumps(report, ensure_ascii=True, sort_keys=True, indent=2) + '\n').encode('utf-8')


def main():
    output = HERE / 'exact-difference-output.json'
    # Exclusive creation reserves the one original output. A killed process can
    # leave an incomplete file; that is not subsequently fabricated as success.
    with output.open('xb') as stream:
        report = {'schema': 'cyclic-difference-response-main-v1', 'execution_status': 'not_started',
                  'certificate_status': 'NOT-CERTIFIED', 'scientific_execution_count_in_this_invocation': 0,
                  'scientific_stage_completed': False, 'coefficient_nonzero_certified': False,
                  'mathematical_acceptance': 'pending_non_author_certificate_and_scope_review',
                  'limits': {'wall_seconds_from_entry': WALL_SECONDS, 'RSS_SELF_target_bytes': RSS_BYTES,
                             'output_bytes_strictly_below': OUTPUT_BYTES, 'shared_new_bisections': NEW_BISECTIONS},
                  'scope': 'Same fixed datum, six differences, first gate and MP.10 arithmetic only; no later restart or regeneration theorem.',
                  'provenance': {'argv': list(sys.argv), 'source_commit_not_checked_by_git': True},
                  'resource_scope': 'SELF only. Deadline starts just after importing time at entry and includes input reading, science, rechecks and first full serialization. Final resource fields, final serialization and disk write are excluded. RSS is sampled with a high-water SELF value, not a full-lifecycle hard memory guarantee.'}
        uname = os.uname()
        report['environment'] = {'python_version': sys.version, 'python_executable': sys.executable,
                                 'os_uname': dict(zip(('sysname', 'nodename', 'release', 'version', 'machine'), uname)),
                                 'visible_logical_CPUs': os.cpu_count(), 'scientific_workers': 1,
                                 'scientific_threads': 1, 'external_processes_started': 0,
                                 'third_party_libraries': []}
        checks = []
        signal.signal(signal.SIGALRM, alarm_handler)
        try:
            remaining = WALL_SECONDS - (time.perf_counter() - ENTRY_TIME)
            if remaining <= 0:
                raise NotCertified('WALL_EXHAUSTED_BEFORE_INPUT')
            signal.setitimer(signal.ITIMER_REAL, remaining)
            parser = argparse.ArgumentParser(description=__doc__)
            parser.add_argument('--source-commit', required=True)
            parser.add_argument('--contract-sha', required=True)
            args = parser.parse_args()
            require(len(args.source_commit) == 40 and all(x in '0123456789abcdef' for x in args.source_commit),
                    'source commit must be a parent-supplied full hash')
            require(args.contract_sha == TEXT_SHA['CONTRACT.md'], 'contract argument mismatch')
            require(Path.cwd().resolve() == WORKTREE and Path(__file__).resolve() == HERE / 'exact_difference.py',
                    'must run the assigned source in the unique reverse worktree')
            source_bytes = Path(__file__).read_bytes()
            checks.append((Path(__file__), sha(source_bytes)))
            report['provenance'].update(source_path=str(Path(__file__).resolve()), source_sha256=sha(source_bytes),
                                        source_commit_parent_supplied=args.source_commit, input_bindings={})
            for name, expected in TEXT_SHA.items():
                check_budget()
                if expected is None:
                    raise NotCertified('EXECUTION_INTERFACE_REVIEW_NOT_YET_BOUND: ' + name)
                path = HERE / name
                data = path.read_bytes()
                require(sha(data) == expected, 'text binding mismatch: ' + name)
                checks.append((path, expected))
                report['provenance']['input_bindings'][name] = {'path': str(path), 'sha256': expected}
            old_data = []
            for name, expected in [('exact-coefficients-output.json', A_SHA), ('exact-roots-output.json', B_SHA)]:
                check_budget()
                path = OLD / name
                data = path.read_bytes()
                require(sha(data) == expected, 'old input binding mismatch: ' + name)
                old_data.append(json.loads(data))
                checks.append((path, expected))
                report['provenance']['input_bindings'][name] = {'path': str(path), 'sha256': expected}
            report['resources_before_scientific_entry'] = snapshot()
            check_budget()
            report['execution_status'] = 'running'
            report['scientific_execution_count_in_this_invocation'] = 1
            scientific_stage(report, old_data[0], old_data[1])
            report['scientific_stage_completed'] = True
            for path, expected in checks:
                check_budget()
                require(sha(path.read_bytes()) == expected, 'input/source changed during run: ' + str(path))
            report['execution_status'] = 'completed'
        except (Exception, SystemExit) as error:
            report['execution_status'] = 'not_certified'
            report['certificate_status'] = ('INCONSISTENT-CERTIFICATE / NOT-CERTIFIED'
                                             if isinstance(error, Inconsistent) else 'NOT-CERTIFIED')
            report['failure'] = {'type': type(error).__name__, 'reason': str(error)}
            if report['coefficient_nonzero_certified']:
                report['partial_status'] = 'NONZERO-COEFFICIENT-CERTIFIED / WINDOW-NOT-CERTIFIED'
        try:
            report['resources_before_first_full_serialization'] = snapshot()
            first = json_bytes(report)
            after = snapshot()
            check_budget()
            if len(first) >= OUTPUT_BYTES:
                raise NotCertified('FIRST_OUTPUT_LIMIT_EXCEEDED')
        except Exception as error:
            after = snapshot()
            report['execution_status'] = 'not_certified'
            report['certificate_status'] = 'NOT-CERTIFIED'
            report['serialization_or_budget_failure'] = {'type': type(error).__name__, 'reason': str(error)}
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
        report['resources_after_first_full_serialization_attempt'] = after
        final = json_bytes(report)
        if len(final) >= OUTPUT_BYTES:
            report = {key: report[key] for key in
                      ('schema', 'provenance', 'environment', 'limits', 'resource_scope', 'scientific_execution_count_in_this_invocation',
                       'scientific_stage_completed', 'coefficient_nonzero_certified', 'resources_after_first_full_serialization_attempt')}
            report.update(execution_status='not_certified', certificate_status='NOT-CERTIFIED',
                          failure={'reason': 'FINAL_OUTPUT_LIMIT_EXCEEDED', 'attempted_bytes': len(final)},
                          full_new_mathematical_certificate_preserved=False)
            final = json_bytes(report)
        require(len(final) < OUTPUT_BYTES, 'bounded failure receipt exceeds output budget')
        stream.write(final)
    summary = {key: report[key] for key in ('execution_status', 'certificate_status',
               'scientific_execution_count_in_this_invocation', 'scientific_stage_completed')}
    summary.update(output_path=str(output), output_sha256=sha(final), output_bytes=len(final))
    print(json.dumps(summary, sort_keys=True))
    return 0 if report['execution_status'] == 'completed' else 2


if __name__ == '__main__':
    sys.exit(main())
