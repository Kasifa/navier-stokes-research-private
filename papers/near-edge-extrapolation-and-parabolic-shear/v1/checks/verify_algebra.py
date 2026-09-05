#!/usr/bin/env python3
"""Finite exact checks of manuscript identities; not a continuum proof.

Uses only Python's standard library. All mathematical comparisons use
Fraction arithmetic, including the real and imaginary parts of coefficients.
The script does not create or modify files.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from math import comb, factorial
import json
import time


@dataclass(frozen=True)
class QC:
    real: F = F(0)
    imag: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "real", F(self.real))
        object.__setattr__(self, "imag", F(self.imag))

    @staticmethod
    def of(value):
        return value if isinstance(value, QC) else QC(value)

    def __add__(self, other):
        other = self.of(other)
        return QC(self.real + other.real, self.imag + other.imag)

    __radd__ = __add__

    def __neg__(self):
        return QC(-self.real, -self.imag)

    def __sub__(self, other):
        return self + (-self.of(other))

    def __rsub__(self, other):
        return self.of(other) + (-self)

    def __mul__(self, other):
        other = self.of(other)
        return QC(self.real * other.real - self.imag * other.imag,
                  self.real * other.imag + self.imag * other.real)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.of(other)
        denominator = other.real**2 + other.imag**2
        if not denominator:
            raise ZeroDivisionError("exact complex division by zero")
        return QC((self.real * other.real + self.imag * other.imag) / denominator,
                  (self.imag * other.real - self.real * other.imag) / denominator)

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("QC powers require nonnegative integers")
        result, base = QC(1), self
        while exponent:
            if exponent & 1:
                result *= base
            base *= base
            exponent //= 2
        return result


ZERO = QC(0)


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == ZERO:
        poly.pop()
    return poly


def p_add(left, right):
    size = max(len(left), len(right))
    return trim([(left[k] if k < len(left) else ZERO)
                 + (right[k] if k < len(right) else ZERO)
                 for k in range(size)])


def p_scale(poly, scale):
    return trim([coefficient * scale for coefficient in poly])


def p_mul(left, right):
    result = [ZERO] * (len(left) + len(right) - 1)
    for j, a in enumerate(left):
        for k, b in enumerate(right):
            result[j+k] += a * b
    return trim(result)


def require_degree(m):
    if not isinstance(m, int) or m < 0:
        raise ValueError("degree must be a nonnegative integer")


def chebyshev_closed(m):
    """Closed monomial formula, independent of the three-term recurrence."""
    require_degree(m)
    if m == 0:
        return [F(1)]
    result = [F(0)] * (m + 1)
    for k in range(m // 2 + 1):
        power = m - 2*k
        result[power] = (F(m, 2) * (-1)**k
                         * F(factorial(m-k-1), factorial(k)*factorial(power))
                         * 2**power)
    return result


def chebyshev_composed_recurrence(m, eta):
    """T_m((Z-1)/(i eta)), built directly in the Fourier variable Z."""
    require_degree(m)
    eta = F(eta)
    if eta == 0:
        raise ValueError("eta must be nonzero")
    inverse = QC(1) / QC(0, eta)
    w = [-inverse, inverse]
    previous = [QC(1)]
    if m == 0:
        return previous
    current = w
    for _ in range(1, m):
        previous, current = current, p_add(p_scale(p_mul(w, current), 2),
                                          p_scale(previous, -1))
    return current


def derivative_value(coefficients, order, x):
    """Evaluate an actual monomial derivative, without endpoint recurrence."""
    total = QC(0) if isinstance(x, QC) else F(0)
    for degree in range(order, len(coefficients)):
        total += (coefficients[degree] * F(factorial(degree), factorial(degree-order))
                  * x**(degree-order))
    return total


def fourier_taylor(m, eta, wrong_center=False):
    """The manuscript coefficient formula, using closed monomial coefficients."""
    eta = F(eta)
    if eta == 0:
        raise ValueError("eta must be nonzero")
    coefficients = chebyshev_closed(m)
    center = QC(0, (-1 if wrong_center else 1) / eta)
    return trim([derivative_value(coefficients, j, center)
                 / (QC(factorial(j)) * QC(0, eta)**j) for j in range(m+1)])


def heat_by_derivatives(coefficients, tau, x):
    result = F(0)
    for j in range((len(coefficients)-1)//2 + 1):
        result += tau**j / factorial(j) * derivative_value(coefficients, 2*j, x)
    return result


def heat_by_gaussian_moments(coefficients, tau, x, variance_factor=2):
    """E[p(x+Z)]; Gaussian moments built recursively from the variance."""
    moments = [F(1), F(0)]
    for k in range(2, len(coefficients)):
        moments.append((k-1) * variance_factor * tau * moments[k-2])
    result = F(0)
    for degree, coefficient in enumerate(coefficients):
        result += coefficient * sum(F(comb(degree, k)) * x**(degree-k) * moments[k]
                                    for k in range(degree+1))
    return result


def endpoint_double_series(m, A, s, c):
    coefficients = chebyshev_closed(m)
    endpoints = [derivative_value(coefficients, k, F(1)) for k in range(m+1)]
    result = F(0)
    for ell in range(m+1):
        for j in range((m-ell)//2 + 1):
            result += (endpoints[ell+2*j] * c**ell * s**j
                       / (A**(ell+2*j) * factorial(ell) * factorial(j)))
    return result


class Checks:
    def __init__(self):
        self.groups = {}

    def record(self, group, condition, detail, negative=False):
        key = "negative" if negative else "positive"
        self.groups.setdefault(group, {"positive": 0, "negative": 0})
        if not condition:
            raise AssertionError(f"{group}: {detail}")
        self.groups[group][key] += 1

    def equal(self, group, actual, expected, detail):
        self.record(group, actual == expected, detail)

    def reject(self, group, actual, expected, detail):
        self.record(group, actual != expected, detail, negative=True)

    def raises(self, group, exception, function, detail):
        try:
            function()
        except exception:
            self.record(group, True, detail, negative=True)
        else:
            self.record(group, False, detail, negative=True)


def run():
    start = time.perf_counter()
    checks = Checks()

    # Zero degree, eta of different sizes, both degree parities.
    for m in range(17):
        for eta in (F(1, 7), F(1, 2), F(2, 3), F(3)):
            direct = chebyshev_composed_recurrence(m, eta)
            taylor = fourier_taylor(m, eta)
            checks.equal("finite_eta_coefficients", direct, taylor, (m, eta))
            checks.record("finite_eta_nonzero", all(z != ZERO for z in taylor),
                          (m, eta))
            if m:
                checks.reject("mutated_center", fourier_taylor(m, eta, True),
                              direct, (m, eta))

    for m in range(33):
        coefficients = chebyshev_closed(m)
        product = F(1)
        for k in range(m+1):
            checks.equal("endpoint_derivative_recurrence",
                         derivative_value(coefficients, k, F(1)), product, (m, k))
            product *= F(m*m-k*k, 2*k+1)
        checks.equal("endpoint_derivative_boundary", product, F(0), m)
        checks.equal("endpoint_derivative_boundary",
                     derivative_value(coefficients, m+1, F(1)), F(0), m)
        if m >= 2:
            wrong = F(m*m) * F(m*m+1, 3)
            checks.reject("mutated_endpoint_recurrence", wrong,
                          derivative_value(coefficients, 2, F(1)), m)

    for m in range(17):
        coefficients = chebyshev_closed(m)
        for tau in (F(0), F(1, 7), F(2)):
            for x in (F(-2), F(-1), F(0), F(1, 3), F(1), F(2)):
                checks.equal("heat_gaussian_moments",
                             heat_by_derivatives(coefficients, tau, x),
                             heat_by_gaussian_moments(coefficients, tau, x),
                             (m, tau, x))

    explicit = {
        0: lambda x, t: F(1),
        1: lambda x, t: x,
        2: lambda x, t: 2*x*x-1+4*t,
        3: lambda x, t: 4*x**3-3*x+24*t*x,
        4: lambda x, t: 8*x**4-8*x*x+1+(96*x*x-16)*t+96*t*t,
        5: lambda x, t: 16*x**5-20*x**3+5*x+(320*x**3-120*x)*t+960*x*t*t,
    }
    for m, expected in explicit.items():
        for x in (F(-1), F(0), F(2, 3), F(2)):
            for tau in (F(0), F(1, 5), F(3)):
                checks.equal("explicit_heat_polynomials",
                             heat_by_derivatives(chebyshev_closed(m), tau, x),
                             expected(x, tau), (m, tau, x))

    for m in range(13):
        for A in (F(1), F(3), F(7, 2)):
            for s in (F(0), F(1, 3), F(4)):
                for c in (F(-2), F(0), F(1), F(3, 2)):
                    checks.equal("scaled_endpoint_heat_series",
                                 endpoint_double_series(m, A, s, c),
                                 heat_by_gaussian_moments(chebyshev_closed(m),
                                                          s/A**2, 1+c/A),
                                 (m, A, s, c))

    for tau in (F(1, 7), F(1), F(4)):
        checks.reject("mutated_gaussian_variance",
                      heat_by_gaussian_moments(chebyshev_closed(2), tau, F(0), 1),
                      heat_by_derivatives(chebyshev_closed(2), tau, F(0)), tau)

    for m in (1, 2, 7):
        for j in (0, 1, 3):
            for eta in (F(1, 9), F(2, 3)):
                M = m*eta
                expected = -(M+j*eta)**2
                checks.equal("carrier_conjugation", -M*M-(j*eta)**2-2*M*j*eta,
                             expected, (m, j, eta))
                if j:
                    checks.reject("mutated_imaginary_shift", -M*M-(j*eta)**2+2*M*j*eta,
                                  expected, (m, j, eta))

    power_tests = {
        "physical_upper_a": (F(2)-F(2)*F(2, 3), F(2, 3)),
        "physical_upper_R": (F(3)-F(5)*F(2, 3), F(-1, 3)),
        "normalized_upper_R": (F(-1)-F(1, 3)+F(2)*F(2, 3), F(0)),
        "normalized_upper_omega": (F(1)-F(2, 3), F(1, 3)),
        "parabolic_quotient_a": (F(2)-F(2, 3), F(4, 3)),
        "parabolic_quotient_R": (F(1, 3)+3-F(10, 3), F(0)),
        "parabolic_lower_a": (F(4, 3)-F(2, 3), F(2, 3)),
        "parabolic_upper_h": (-F(2, 3), F(-2, 3)),
        "high_carrier_q": (F(3)+F(4, 3), F(13, 3)),
        "high_carrier_lambda": (F(-1)+F(2, 3), F(-1, 3)),
        "critical_mode_L": (F(5, 2)-F(1, 2)-2, F(0)),
        "edge_squared_prefactor": (F(250, 19)*4, F(1000, 19)),
        "edge_squared_exponent": (F(5)*2*2, F(20)),
        "F4_two_power": (-F(4, 3)+F(2, 3), -F(2, 3)),
        "G4_two_power": (-F(2, 3)-F(2, 3), -F(4, 3)),
        "squared_tilt_two_power": (F(1)-F(4, 3), -F(1, 3)),
        "frozen_rate": (-F(2, 3969)/3, -F(2, 11907)),
    }
    for name, (actual, expected) in power_tests.items():
        checks.equal("constants_and_powers", actual, expected, name)

    # Squaring positive quantities makes the sqrt(2) threshold exact rational algebra.
    for gamma in (F(1), F(2, 3969), F(3, 7)):
        for p in (F(32, 63), F(1), F(3)):
            for delta_sum in (F(1, 2), F(1), F(5, 3)):
                kappa_squared = gamma**2*p/(7200*delta_sum)
                rate_term_squared = 800*kappa_squared*delta_sum/p
                checks.equal("critical_threshold", rate_term_squared,
                             (gamma/3)**2, (gamma, p, delta_sum))
                checks.record("critical_threshold_sides",
                              800*(kappa_squared/4)*delta_sum/p < (gamma/3)**2,
                              (gamma, p, delta_sum, "below"))
                checks.record("critical_threshold_sides",
                              800*(4*kappa_squared)*delta_sum/p > (gamma/3)**2,
                              (gamma, p, delta_sum, "above"))
                checks.reject("mutated_threshold_sqrt2",
                              800*(gamma**2*p/(3600*delta_sum))*delta_sum/p,
                              (gamma/3)**2, (gamma, p, delta_sum))

    checks.raises("invalid_input_boundaries", ValueError,
                  lambda: chebyshev_closed(-1), "negative degree")
    checks.raises("invalid_input_boundaries", ValueError,
                  lambda: chebyshev_composed_recurrence(2, F(0)), "zero eta composition")
    checks.raises("invalid_input_boundaries", ValueError,
                  lambda: fourier_taylor(2, F(0)), "zero eta Taylor")
    checks.raises("invalid_input_boundaries", ZeroDivisionError,
                  lambda: QC(1)/QC(0), "complex division by zero")

    positive = sum(group["positive"] for group in checks.groups.values())
    negative = sum(group["negative"] for group in checks.groups.values())
    print(json.dumps({"status": "PASS", "arithmetic": "exact Fraction and rational complex",
                      "positive_checks": positive, "negative_checks": negative,
                      "total_checks": positive+negative, "groups": checks.groups,
                      "elapsed_seconds": round(time.perf_counter()-start, 3),
                      "scope": "finite algebra checks, not continuum or asymptotic proofs"},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    run()
