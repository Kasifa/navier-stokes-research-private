from collections import defaultdict
from itertools import product
from fractions import Fraction


def derivative(terms, j):
    out = defaultdict(int)
    for (a, n), c in terms.items():
        if a[j]:
            b = list(a)
            b[j] -= 1
            out[(tuple(b), n)] += c * a[j]
        b = list(a)
        b[j] += 1
        out[(tuple(b), n + 2)] -= c * n
    return {k: v for k, v in out.items() if v}


def expected(ids):
    out = defaultdict(int)
    a = [0, 0, 0]
    for i in ids:
        a[i] += 1
    out[(tuple(a), 9)] += 105
    for r in range(4):
        for s in range(r + 1, 4):
            if ids[r] == ids[s]:
                a = [0, 0, 0]
                for j in range(4):
                    if j not in (r, s):
                        a[ids[j]] += 1
                out[(tuple(a), 7)] -= 15
    for i, j, k, l in [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]:
        if ids[i] == ids[j] and ids[k] == ids[l]:
            out[((0, 0, 0), 5)] += 3
    return {k: v for k, v in out.items() if v}


for ids in product(range(3), repeat=4):
    actual = {((0, 0, 0), 1): 1}
    for j in ids:
        actual = derivative(actual, j)
    assert actual == expected(ids), (ids, actual, expected(ids))
assert Fraction(1, 29**2) < Fraction(1, 100)
assert -12 + Fraction(105, 100) < -10
assert -Fraction(5, 2) - 8 - Fraction(3, 2) == -12
print(
    'PASS: 81 Cartesian fourth-derivative components, exact rational cone bound, '
    'and D pairing coefficient -12.'
)
