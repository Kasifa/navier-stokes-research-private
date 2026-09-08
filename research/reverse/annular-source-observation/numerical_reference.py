"""Independent, fixed-test references; no execution has been performed by author.

Source fixture: KERNEL_TEST_DRAFT.md, read in full before writing this file,
SHA256 ebfb3ba36d8773cffe4569045b984104d115afdae88e3b8160a4a250d547c66d.
Toy data and nonlinearities: parent's explicit fixed test instructions.
The numerical_kernel.py production source has not been read or imported.

ordered_rhs uses rational real/imaginary pairs for the complete ordered Fourier
sum. Only the returned physical coefficients are converted to complex once.
reference_step instead uses ordinary binary64 complex arithmetic and math.exp
for a fixed toy integrating-factor RK4. It is a code-consistency reference,
not an interval computation, an NS trajectory, or a rigorous time-error bound.
This module has no standalone test runner; the separately reviewed driver owns
any future execution and resource accounting. Importing/running before that
approval is not authorized by this file.
"""

from fractions import Fraction
import math


def _qpair(value):
    """Interpret supplied complex components as their exact binary rationals."""
    if isinstance(value, Fraction):
        return value, Fraction(0)
    if type(value) is int:
        return Fraction(value), Fraction(0)
    z = complex(value)
    if not (math.isfinite(z.real) and math.isfinite(z.imag)):
        raise ValueError("nonfinite reference input coefficient")
    return Fraction.from_float(z.real), Fraction.from_float(z.imag)


def _qadd(z, w):
    return z[0] + w[0], z[1] + w[1]


def _qscale(z, real):
    return real * z[0], real * z[1]


def _qmul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def _qminus_i(z):
    return z[1], -z[0]


def _qdot(frequency, vector):
    value = (Fraction(0), Fraction(0))
    for component, coefficient in zip(frequency, vector):
        value = _qadd(value, _qscale(coefficient, component))
    return value


def _frequency(value):
    result = tuple(value)
    if len(result) != 3 or any(type(x) is not int for x in result):
        raise ValueError("frequency must be a triple of Python integers")
    return result


def _qrecord(value):
    return {"numerator": str(value.numerator),
            "denominator": str(value.denominator)}


def _pair_record(value):
    return {"real": _qrecord(value[0]), "imaginary": _qrecord(value[1])}


def _vector_record(vector):
    return [_pair_record(z) for z in vector]


def _physical_complex(value):
    return complex(float(value[0]), float(value[1]))


def source_fixture(which):
    """Return exactly the H0 or H1 fixture, including both conjugate negatives.

    The four input coefficients are dyadic and exactly representable in
    binary64. No mode or polarization is drawn from numerical_kernel.py.
    """
    if which == "H0":
        denominator = 8
        rows = [((7, 1, 0), (1, -7, 1), (Fraction(1), Fraction(1, 2))),
                ((6, 0, 1), (1, 1, -6), (Fraction(1), Fraction(-1, 4)))]
    elif which == "H1":
        denominator = 16
        rows = [((15, 1, 0), (1, -15, 1), (Fraction(1), Fraction(1, 2))),
                ((14, 0, 1), (1, 1, -14), (Fraction(1), Fraction(-1, 4)))]
    else:
        raise ValueError("only the fixed H0 and H1 source fixtures are allowed")
    modes = {}
    for frequency, direction, phase in rows:
        exact = [_qscale(phase, Fraction(component, denominator))
                 for component in direction]
        modes[frequency] = [_physical_complex(z) for z in exact]
        modes[tuple(-k for k in frequency)] = [
            _physical_complex((z[0], -z[1])) for z in exact]
    return modes


def ordered_rhs(modes, *, return_evidence=False):
    """Compute complete sum -i P_k[(f_p dot q) f_q], k=p+q.

    The dot product is bilinear: no conjugate is inserted into a summand.
    Negative modes must be present in the caller's dictionary if required.
    Every ordered pair is included. k=0 is explicitly zero. The returned dict
    contains every pair-sum label, including exact-zero coefficients, and k=0.
    All other lattice labels mean exactly zero, so a target-band caller should
    use result.get(k, [0j, 0j, 0j]) and compare its whole prescribed band.

    return_evidence=True returns (result, evidence). Evidence has only JSON-
    compatible rational/integer/string/list/dict fields. Exact ordered terms
    and exact final coefficients remain distinct from rounded output complex.
    There is no FFT, grid cut-off, band projection, or Galerkin truncation here.
    """
    if not isinstance(modes, dict):
        raise TypeError("modes must be a frequency-to-vector dictionary")
    exact_modes = {}
    for key, coefficients in modes.items():
        k = _frequency(key)
        vector = list(coefficients)
        if len(vector) != 3:
            raise ValueError("every Fourier coefficient must have three components")
        exact_modes[k] = [_qpair(z) for z in vector]
    keys = sorted(exact_modes)
    zero = (Fraction(0), Fraction(0))
    accumulated = {(0, 0, 0): [zero, zero, zero]}
    terms = []
    for p in keys:
        fp = exact_modes[p]
        for q in keys:
            fq = exact_modes[q]
            k = tuple(p[j] + q[j] for j in range(3))
            scalar = _qdot(q, fp)
            raw = [_qmul(scalar, coefficient) for coefficient in fq]
            radius_squared = sum(component * component for component in k)
            radial_dot = _qdot(k, raw)
            if radius_squared == 0:
                projected = [zero, zero, zero]
            else:
                projected = [
                    _qadd(raw[j], _qscale(radial_dot,
                                         Fraction(-k[j], radius_squared)))
                    for j in range(3)]
            term = [_qminus_i(z) for z in projected]
            if k not in accumulated:
                accumulated[k] = [zero, zero, zero]
            accumulated[k] = [_qadd(previous, addition)
                              for previous, addition in zip(accumulated[k], term)]
            if return_evidence:
                terms.append({
                    "p": list(p), "q": list(q), "k": list(k),
                    "bilinear_fp_dot_q": _pair_record(scalar),
                    "raw_vector": _vector_record(raw),
                    "k_dot_raw": _pair_record(radial_dot),
                    "k_squared": radius_squared,
                    "Leray_projected_vector": _vector_record(projected),
                    "minus_i_projected_term": _vector_record(term),
                })
    result = {k: [_physical_complex(z) for z in accumulated[k]]
              for k in sorted(accumulated)}
    if not return_evidence:
        return result
    evidence = {
        "scope": "fixed-fixture ordered convolution reference, no NS certificate",
        "arithmetic": "Fraction real/imaginary pairs until final complex conversion",
        "ordered_pair_count": len(keys) * len(keys),
        "input_modes": [
            {"k": list(k), "coefficient": _vector_record(exact_modes[k]),
             "k_dot_coefficient": _pair_record(_qdot(k, exact_modes[k]))}
            for k in keys],
        "all_ordered_terms": terms,
        "output_exact": [
            {"k": list(k), "coefficient": _vector_record(accumulated[k]),
             "k_dot_coefficient": _pair_record(_qdot(k, accumulated[k]))}
            for k in sorted(accumulated)],
        "zero_mode_convention": "explicitly zero",
        "unlisted_output_labels": "exactly zero",
        "floating_output_is_not_an_interval_enclosure": True,
    }
    return result, evidence


def toy_initial_state():
    """Fixed toy input; this is not any Fourier coefficient of the actual a_*."""
    return {
        "U": [complex(1 / 4, 1 / 8), complex(1 / 2, -1 / 4)],
        "G": [complex(3, 4)],
        "W": [complex(5, 6)],
    }


def _toy_block(values, size, label):
    result = [complex(z) for z in values]
    if len(result) != size:
        raise ValueError(label + " has the wrong toy block length")
    if any(not (math.isfinite(z.real) and math.isfinite(z.imag)) for z in result):
        raise ValueError(label + " contains a nonfinite toy coefficient")
    return result


def _blocks(flat):
    return {"U": list(flat[:2]), "G": [flat[2]], "W": [flat[3]]}


def _toy_nonlinearity(physical, phase):
    u0, u1 = physical[0], physical[1]
    return [u0 * u1, u0 * u0, u0 * u0, phase * u1 * u1]


def reference_step(U, G, W, phase):
    """One ordinary RK4 step for Y(theta)=exp(-theta L) X(t+theta).

    phase is exactly 0 or 1; h is fixed at 1/64. L is (-1,-4,-9,-16).
    U has two complex entries, G and W one each. Their initial values may be
    either the prescribed toy initial state or the preceding toy step output.
    All four physical stage states, nonlinearities, and transformed derivatives
    are returned. The implementation deliberately uses the transformed ODE,
    not a transcription of the folded production update formula.

    For this toy, N_U=(U[0]*U[1],U[0]**2), N_G=U[0]**2 and
    N_W=phase*U[1]**2. G and W are history variables; they do not feed N.
    Nonzero initial G/W still undergo their own linear heat evolution.
    Returned finite precision values are code-comparison references only.
    """
    if type(phase) is not int or phase not in (0, 1):
        raise ValueError("phase must be the fixed integer 0 or 1")
    initial = (_toy_block(U, 2, "U") + _toy_block(G, 1, "G")
               + _toy_block(W, 1, "W"))
    h = 1 / 64
    linear = (-1, -4, -9, -16)
    stages = []

    def transformed_rhs(theta, transformed, stage_number):
        physical = [math.exp(theta * eigenvalue) * y
                    for eigenvalue, y in zip(linear, transformed)]
        nonlinear = _toy_nonlinearity(physical, phase)
        derivative = [math.exp(-theta * eigenvalue) * n
                      for eigenvalue, n in zip(linear, nonlinear)]
        stages.append({
            "stage": stage_number, "theta": theta,
            "Y": _blocks(transformed), "X": _blocks(physical),
            "N_X": _blocks(nonlinear), "dY_dtheta": _blocks(derivative),
        })
        return derivative

    k1 = transformed_rhs(0.0, initial, 1)
    y2 = [x + (h / 2) * k for x, k in zip(initial, k1)]
    k2 = transformed_rhs(h / 2, y2, 2)
    y3 = [x + (h / 2) * k for x, k in zip(initial, k2)]
    k3 = transformed_rhs(h / 2, y3, 3)
    y4 = [x + h * k for x, k in zip(initial, k3)]
    k4 = transformed_rhs(h, y4, 4)
    final_y = [initial[j] + (h / 6) * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j])
               for j in range(4)]
    final_x = [math.exp(h * eigenvalue) * y
               for eigenvalue, y in zip(linear, final_y)]
    if any(not (math.isfinite(z.real) and math.isfinite(z.imag)) for z in final_x):
        raise ValueError("nonfinite toy reference result")
    output = _blocks(final_x)
    output.update({
        "h": h, "phase": phase, "linear_diagonal": list(linear),
        "initial": _blocks(initial), "stages": stages,
        "Y_final": _blocks(final_y),
        "scope": "binary64 toy consistency reference, not rigorous NS time error",
    })
    return output


def reference_boundary_pair():
    """One phase-0 then one phase-1 toy step; reset only W at the boundary.

    This prescribed pair starts with W=0. U/G at the boundary are the actual
    first toy step outputs and are preserved, not reset to original values.
    The separate single-step phase tests should use toy_initial_state() with
    its nonzero W, so they also exercise the W homogeneous history term.
    """
    initial = toy_initial_state()
    first_input = {"U": list(initial["U"]), "G": list(initial["G"]), "W": [0j]}
    first = reference_step(first_input["U"], first_input["G"], first_input["W"], 0)
    second_input = {"U": list(first["U"]), "G": list(first["G"]), "W": [0j]}
    second = reference_step(second_input["U"], second_input["G"], second_input["W"], 1)
    return {
        "first_input": first_input, "phase0_step": first,
        "boundary_input": second_input, "phase1_step": second,
        "boundary_rule": "preserve U/G and replace only W by zero",
        "scope": "two fixed toy steps only; not a two-stage NS supply certificate",
    }


if __name__ == "__main__":
    raise SystemExit("No standalone execution: use only the separately reviewed driver.")
