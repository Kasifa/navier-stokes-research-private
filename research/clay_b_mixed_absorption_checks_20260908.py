"""Exact finite Fourier checks for MA.12-14; not an NS solver or PDE certificate."""

from fractions import Fraction as F
import json


ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def clean(p):
    return {k: v for k, v in p.items() if v != ZERO}


def add(*polys):
    result = {}
    for p in polys:
        for k, v in p.items():
            result[k] = cadd(result.get(k, ZERO), v)
    return clean(result)


def scale(p, c):
    return clean({k: cmul(v, (F(c), F(0))) for k, v in p.items()})


def mul(p, q):
    result = {}
    for k, v in p.items():
        for ell, w in q.items():
            mode = tuple(a + b for a, b in zip(k, ell))
            result[mode] = cadd(result.get(mode, ZERO), cmul(v, w))
    return clean(result)


def derivative(p, direction):
    return clean({k: cmul(v, (F(0), F(k[direction]))) for k, v in p.items()})


def laplacian(p):
    return clean({k: cmul(v, (-F(sum(n * n for n in k)), F(0)))
                  for k, v in p.items()})


def trig(n, direction, sine=False):
    k = [0, 0, 0]
    k[direction] = n
    k = tuple(k)
    minus = tuple(-v for v in k)
    if sine:
        return {k: (F(0), -F(1, 2)), minus: (F(0), F(1, 2))}
    return {k: (F(1, 2), F(0)), minus: (F(1, 2), F(0))}


def value_at_zero_line(p, y_pi=False):
    total = ZERO
    for k, v in p.items():
        assert k[2] == 0
        factor = -1 if y_pi and k[1] % 2 else 1
        total = cadd(total, cmul(v, (F(factor), F(0))))
    assert total[1] == 0
    return total[0]


def equal(p, q):
    assert not add(p, scale(q, -1)), "nonzero exact Fourier residual"


def real(p):
    for k, v in p.items():
        assert p.get(tuple(-n for n in k), ZERO) == (v[0], -v[1])


def pressure_formula(wrong_frequency=False, drop_sine=False):
    result = {}
    for m, sign_m in ((1, 1), (3, -1)):
        for n, sign_n, sine_n in ((1, 1, 1), (2, -1, -F(1, 2))):
            denominator = m * m + (1 if wrong_frequency else n * n)
            term = scale(trig(n, 0), sign_n)
            if not drop_sine:
                term = add(term, scale(trig(n, 0, True), sine_n))
            result = add(result, scale(mul(trig(m, 1), term), F(2 * sign_m, denominator)))
    return result


def main():
    f = add(trig(1, 1, True), scale(trig(3, 1, True), -F(1, 3)))
    g = add(trig(1, 0, True), scale(trig(2, 0, True), -F(1, 2)),
            scale(trig(1, 0), -1), scale(trig(2, 0), F(1, 4)))
    velocity = [f, g, {}]
    gradient = [[derivative(v, j) for j in range(3)] for v in velocity]
    equal(add(*(gradient[i][i] for i in range(3))), {})
    for v in velocity:
        assert v.get((0, 0, 0), ZERO) == ZERO
        real(v)
    source = add(*(mul(gradient[i][j], gradient[j][i])
                   for i in range(3) for j in range(3)))
    equal(source, scale(mul(derivative(f, 1), derivative(g, 0)), 2))
    assert source.get((0, 0, 0), ZERO) == ZERO
    inverse_pressure = {k: cmul(v, (F(1, sum(n * n for n in k)), F(0)))
                        for k, v in source.items()}
    pressure = pressure_formula()
    equal(pressure, inverse_pressure)
    equal(scale(laplacian(pressure), -1), source)
    real(pressure)
    assert pressure.get((0, 0, 0), ZERO) == ZERO
    acceleration = [add(*(mul(velocity[j], gradient[i][j]) for j in range(3)),
                        derivative(pressure, i)) for i in range(3)]
    for y_pi, sign in ((False, 1), (True, -1)):
        for row in gradient:
            for entry in row:
                assert value_at_zero_line(entry, y_pi) == 0
                for j in range(3):
                    assert value_at_zero_line(derivative(entry, j), y_pi) == 0
        assert [value_at_zero_line(a, y_pi) for a in acceleration] == [sign * F(36, 65), F(0), F(0)]
        assert value_at_zero_line(derivative(derivative(gradient[0][1], 1), 1), y_pi) == sign * 8
    assert value_at_zero_line(derivative(derivative(gradient[1][0], 0), 0)) == 3
    assert value_at_zero_line(derivative(derivative(derivative(gradient[1][0], 0), 0), 0)) == 3
    rejected = []
    for label, wrong_pressure in (
        ("wrong pressure sign", scale(pressure, -1)),
        ("wrong x-frequency denominator", pressure_formula(wrong_frequency=True)),
        ("dropped sine pressure", pressure_formula(drop_sine=True)),
    ):
        try:
            equal(scale(laplacian(wrong_pressure), -1), source)
        except AssertionError:
            rejected.append(label)
        else:
            raise AssertionError("negative control incorrectly accepted: " + label)
    assert len(rejected) == 3
    print(json.dumps({
        "status": "PASS", "arithmetic": "exact Gaussian rational Fourier coefficients",
        "checks": ["real mean-zero divergence-free velocity", "canonical Poisson solution",
                   "two quadratic gradient zeros", "opposite acceleration values"],
        "acceleration_x_at_zero_lines": ["36/65", "-36/65"],
        "negative_controls_rejected": rejected,
        "scope": "Finite algebra only; no flat-cutoff, evolution, integral-divergence or Clay certification."
    }, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
