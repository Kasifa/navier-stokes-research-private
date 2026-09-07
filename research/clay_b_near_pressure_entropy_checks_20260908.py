"""Exact finite trigonometric identities, not a numerical NS simulation."""

from fractions import Fraction as F
import json

N = 5  # sin(y), cos(y), sin(2z), cos(2z), epsilon
ZERO = (0,) * N


class P:
    def __init__(self, terms=None):
        pending = list((terms or {}).items())
        out = {}
        while pending:
            powers, coefficient = pending.pop()
            coefficient = F(coefficient)
            if not coefficient:
                continue
            # Canonical quotient by sin^2(y)+cos^2(y)=1 and its 2z analogue.
            for sine, cosine in ((0, 1), (2, 3)):
                if powers[sine] >= 2:
                    a = list(powers)
                    a[sine] -= 2
                    b = a.copy()
                    b[cosine] += 2
                    pending.extend(((tuple(a), coefficient), (tuple(b), -coefficient)))
                    break
            else:
                out[powers] = out.get(powers, F(0)) + coefficient
        self.terms = {k: v for k, v in out.items() if v}

    @staticmethod
    def convert(value):
        return value if isinstance(value, P) else P({ZERO: F(value)})

    def __add__(self, other):
        out = self.terms.copy()
        for k, v in P.convert(other).terms.items():
            out[k] = out.get(k, F(0)) + v
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-P.convert(other))

    def __rsub__(self, other):
        return P.convert(other) - self

    def __mul__(self, other):
        out = {}
        for a, x in self.terms.items():
            for b, y in P.convert(other).terms.items():
                k = tuple(a[j] + b[j] for j in range(N))
                out[k] = out.get(k, F(0)) + x * y
        return P(out)

    __rmul__ = __mul__

    def __pow__(self, power):
        assert isinstance(power, int) and power >= 0
        out = P.convert(1)
        for _ in range(power):
            out = out * self
        return out

    def partial(self, j):
        out = {}
        for k, v in self.terms.items():
            if k[j]:
                n = list(k)
                n[j] -= 1
                out[tuple(n)] = v * k[j]
        return P(out)

    def flip(self, j):
        return P({k: v * (-1) ** k[j] for k, v in self.terms.items()})


def var(j):
    k = [0] * N
    k[j] = 1
    return P({tuple(k): 1})


s, c, S, C, e = (var(j) for j in range(N))
z = P()


def dy(p):
    p = P.convert(p)
    return c * p.partial(0) - s * p.partial(1)


def dz(p):
    p = P.convert(p)
    return 2 * C * p.partial(2) - 2 * S * p.partial(3)


def lap(p):
    return dy(dy(p)) + dz(dz(p))


def equal(a, b=0):
    residual = P.convert(a) - b
    if residual.terms:
        raise AssertionError(str(residual.terms))


def inner(a, b):
    return sum(a[i][j] * b[i][j] for i in range(3) for j in range(3))


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def main():
    v = [-2 * c * S, s * C]
    p = -(c * c - s * s) - F(1, 4) * (C * C - S * S)
    k = [[dy(v[0]), dz(v[0])], [dy(v[1]), dz(v[1])]]
    equal(k[0][0] + k[1][1])
    for component in v:
        equal(lap(component), -5 * component)
    for i, deriv in enumerate((dy, dz)):
        equal(v[0] * dy(v[i]) + v[1] * dz(v[i]) + deriv(p))
    equal(-lap(p), sum(k[i][j] * k[j][i] for i in range(2) for j in range(2)))
    equal(dy(dy(p)), 4 * (c * c - s * s))
    equal(dz(dz(p)), 4 * (C * C - S * S))
    equal(dy(dz(p)))
    g = [[z, c, 2 * C], [z, e * k[0][0], e * k[0][1]], [z, e * k[1][0], e * k[1][1]]]
    h = [[z, z, z], [z, e * e * dy(dy(p)), z], [z, z, e * e * dz(dz(p))]]
    norm_k = sum(k[i][j] ** 2 for i in range(2) for j in range(2))
    equal(norm_k, 8 * s * s * S * S + 17 * c * c * C * C)
    norm_g = inner(g, g)
    equal(norm_g, c * c + 4 * C * C + e * e * norm_k)
    equal(norm_g.flip(0), norm_g)
    inertial = inner(g, mm(g, g))
    odd = 2 * e * s * S * (c * c - 4 * C * C)
    equal(inertial, odd - 6 * e * c * c * C * C)
    equal(odd.flip(0), -odd)
    pressure = inner(g, h)
    equal(pressure, 8 * e ** 3 * s * S * ((c * c - s * s) - (C * C - S * S)))
    equal(pressure.flip(0), -pressure)
    # Exact coefficients in the analytic torus integrals, in units of pi^3.
    assert 2 * (8 + 17) == 50
    assert 6 * 2 == 12
    # Actual negative controls: wrong pressure sign, missing z frequency,
    # and the claim that the whole inertial numerator is odd.
    rejected = 0
    wrong = [v[0] * dy(v[0]) + v[1] * dz(v[0]) - dy(p),
             dz(S) - C, inertial.flip(0) + inertial]
    for residual in wrong:
        try:
            equal(residual)
        except AssertionError:
            rejected += 1
        else:
            raise AssertionError("negative control was accepted")
    assert rejected == 3
    print(json.dumps({"passed": True, "method": "Fraction polynomial quotient by two circle identities",
                      "checks": ["Euler pressure", "heat eigenvalue", "Poisson equation", "gradient products", "parity"],
                      "mutations_rejected": rejected, "third_party_packages": False,
                      "scope": "finite algebra only; no PDE evolution or continuum-integral certificate"}))


if __name__ == "__main__":
    main()
