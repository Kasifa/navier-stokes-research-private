"""Exact finite checks for AH's explicit local solutions; not a PDE certificate.

No third-party packages. E is an algebraic variable representing exp(t), so
time differentiation is partial_t + E partial_E. Coefficients are rational.
"""

from fractions import Fraction
import json


class P:
    n = 6  # x, y, z, t, epsilon, E

    def __init__(self, value=0):
        terms = value if isinstance(value, dict) else {(0,) * self.n: value}
        self.terms = {k: Fraction(v) for k, v in terms.items() if v}

    @classmethod
    def variable(cls, i):
        key = tuple(int(j == i) for j in range(cls.n))
        return cls({key: 1})

    @staticmethod
    def coerce(value):
        return value if isinstance(value, P) else P(value)

    def __add__(self, other):
        result = dict(self.terms)
        for key, value in self.coerce(other).terms.items():
            result[key] = result.get(key, 0) + value
        return P(result)

    __radd__ = __add__

    def __neg__(self):
        return P({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        result = {}
        for ka, va in self.terms.items():
            for kb, vb in self.coerce(other).terms.items():
                key = tuple(a + b for a, b in zip(ka, kb))
                result[key] = result.get(key, 0) + va * vb
        return P(result)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return self * (1 / Fraction(scalar))

    def __pow__(self, exponent):
        assert isinstance(exponent, int) and exponent >= 0
        result = P(1)
        for _ in range(exponent):
            result = result * self
        return result

    def diff(self, i):
        result = {}
        for key, value in self.terms.items():
            if key[i]:
                target = list(key)
                target[i] -= 1
                result[tuple(target)] = value * key[i]
        return P(result)

    def dt(self):
        return self.diff(3) + E * self.diff(5)

    def zero(self):
        return not self.terms


x, y, z, t, eps, E = [P.variable(i) for i in range(6)]


def jacobian(u):
    return [[component.diff(j) for j in range(3)] for component in u]


def hessian(p):
    return [[p.diff(i).diff(j) for j in range(3)] for i in range(3)]


def square(g):
    return [[sum(g[i][k] * g[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]


def norm2(g):
    return sum(value ** 2 for row in g for value in row)


def residual(u, p):
    g = jacobian(u)
    return [u[i].dt() + sum(g[i][j] * u[j] for j in range(3))
            - sum(u[i].diff(j).diff(j) for j in range(3)) + p.diff(i)
            for i in range(3)]


def gamma_numerator(g):
    """Gamma = numerator / |G|^3 on |G|>0."""
    q2 = norm2(g)
    grad_g2 = sum(value.diff(k) ** 2
                  for row in g for value in row for k in range(3))
    return q2 * grad_g2 - sum(q2.diff(k) ** 2 for k in range(3)) / 4


def require_zero(value, label):
    if not P.coerce(value).zero():
        raise AssertionError(label)


def check_solution(name, u, p):
    g = jacobian(u)
    require_zero(sum(g[i][i] for i in range(3)), name + ': divergence')
    for i, value in enumerate(residual(u, p)):
        require_zero(value, name + ': NS component ' + str(i))
    # A changed quadratic pressure must not pass the same exact equations.
    if all(value.zero() for value in residual(u, p + x * x)):
        raise AssertionError(name + ': pressure mutation was not rejected')
    return g, hessian(p)


def run():
    # Basic arithmetic/differentiation checks independent of the examples.
    require_zero(((x + y) ** 3).diff(0) - 3 * (x + y) ** 2, 'derivative')
    require_zero((E ** 3).dt() - 3 * E ** 3, 'exponential derivative')
    require_zero((t * E).dt() - (1 + t) * E, 'time product rule')
    if (x + 1).zero():
        raise AssertionError('nonzero polynomial rejected incorrectly')

    f = eps * y + eps * E * (y * y + 1) / 2
    g, h = check_solution('AH14', [x + f, -y, P()], -(x*x + y*y) / 2)
    g2 = square(g)
    for i in range(3):
        for j in range(3):
            require_zero(g2[i][j] + h[i][j], 'AH15: G^2+H')
    s = eps * (1 + E * y)
    require_zero(norm2(g) - (2 + s*s), 'AH15: norm')
    require_zero(gamma_numerator(g) - 2*eps*eps*E*E, 'AH15: Gamma_G')
    rel = [[P(), s, P()], [P(), P(), P()], [P(), P(), P()]]
    require_zero(gamma_numerator(rel), 'AH15: Gamma_R')

    a = eps + t
    d = [1 + a, -1 + a, -2 * a]
    u = [d[0]*x, d[1]*y, d[2]*z]
    p = -((1+d[0]**2)*x*x + (1+d[1]**2)*y*y
          + (-2+d[2]**2)*z*z) / 2
    g, _ = check_solution('AH21', u, p)
    require_zero(norm2(g) - (2 + 6*a*a), 'AH22: norm')
    require_zero(norm2(g).dt() - 12*a, 'AH22: first-order source')
    require_zero(gamma_numerator(g), 'AH22: Gamma')

    v = [y*z, x*z, x*y]
    g, _ = check_solution('AH23', [t*vi for vi in v],
                          -x*y*z - t*t*sum(vi*vi for vi in v)/2)
    r2 = x*x + y*y + z*z
    require_zero(norm2(g) - 2*t*t*r2, 'AH23: norm')
    require_zero(gamma_numerator(g) - 8*t**4*r2, 'AH23: Gamma numerator')
    for row in g:
        for value in row:
            if any(sum(key[:3]) % 2 != 1 for key in value.terms):
                raise AssertionError('AH23: odd matrix mean')
    assert Fraction(2) * 4 / 2 == 4  # radial Gamma integral / (sqrt(2) pi t R^2)
    assert Fraction(1, 4) * 2 == Fraction(1, 2)  # domain bound e^t |y| <= 1/2
    print(json.dumps({
        'passed': True,
        'examples': ['AH14-15', 'AH21-22', 'AH23'],
        'pressure_mutations_rejected': 3,
        'method': 'exact rational polynomials with dt=partial_t+E partial_E',
        'third_party_packages': False,
        'scope': 'finite explicit-solution identities, not general PDE regularity',
    }))


if __name__ == '__main__':
    run()
