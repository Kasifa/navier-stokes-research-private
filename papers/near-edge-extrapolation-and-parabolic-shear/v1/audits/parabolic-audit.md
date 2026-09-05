# Parabolic proof audit

Audit date: 2026-09-05.  This review reconstructs the argument in
`sections/parabolic.tex` from its formulas.  The earlier R0.76L audit
labels and its finite Python/Ruby certificates are not used as proof of
the continuum statements.

## Result

The family-specific R0.76L conclusion can be retained after expanding
the proof and correcting its asymptotic quantifier.  Four results are
proved in the paper section:

1. `thm:heat-edge`: a joint growing-degree/shrinking-edge Gaussian
   Laplace limit and a second, smaller fixed-displacement logarithmic
   ratio.  Uniformity is explicit on compact positive-time and bounded
   displacement sets.
2. `lem:heat-terminal`: exact positive coefficients, quantitative time
   and displacement logarithmic derivative bounds, and a global spatial
   derivative majorant.  These convert a terminal value into a time
   interval of width `(1+mu^2)^(-1)` without an exponential loss.
3. `prop:dynamic-confluence`: exact nonzero consecutive integer modes,
   the correct complex heat conjugation, and a uniform absolute transfer
   error `exp(-9 L^2/40000 + o(L^2))` over the entire clock and the
   required spatial region.
4. `thm:parabolic-shear`: eventual positive paired collar flux over the
   entire clock, an upper and a lower bound using the full plateau
   denominator, and the normalized logarithmic rate `-2/11907`.

The paper theorem is restricted to the explicitly specified initial
coefficients, negative drift, cutoffs, and even degree sequences with
`m/sqrt(A) -> infinity` and `m/A^2 -> 0`.  There is no general packet
bound and no result about a limiting Navier--Stokes solution.

## Source-to-proof correspondence

Source: `/Users/kasifa/Documents/Math/navier-stokes-r074m/research/r076l_parabolic_edge_smoothing_complete_clock.md`.

| Source formulas | Paper result | Fresh analytic check |
| --- | --- | --- |
| L.14--L.29 | `thm:heat-edge` | Gaussian monomial identity; strict unique saddle; uniform tail and tilted-tail estimates; signed interior and remote negative exterior |
| L.30--L.37, L.57 | `lem:heat-terminal` | Differentiated Chebyshev ODE; positive double sum; conditional geometric tail; Gegenbauer generating-function coefficient majorant |
| L.38--L.47 | `prop:dynamic-confluence` | Taylor coefficient identity; real-rootedness; exact Fourier conjugation; finite-dimensional polynomial Duhamel estimate with growing degree |
| L.48--L.55 | `thm:parabolic-shear`, paired sign and time comparison | Both opposed caps retained; transfer error negligible relative to both cap values; whole early clock absorbed using `F4 > F3` |
| L.56--L.62 | `thm:parabolic-shear`, full plateau bounds | Full difference-of-disks cross section; global upper payment; positive terminal outer-strip lower payment |
| L.8, L.63--L.66 | exact dimensional identities and normalized rate | Direct three-dimensional integration and algebra, including cancellation of constant background terms |

R0.76K is used only as motivation and as the origin of the polynomial
confluence construction.  The new parabolic section repeats the needed
coefficient construction and proves its growing-degree transfer, so it
does not assume K's fixed-slice confluence estimate applies dynamically.

## Corrections and clarifications made for the manuscript

- The source asserts that an eventual `L0` depends only on the fixed
  cutoffs and beta while allowing arbitrary sequences satisfying two
  unquantified little-o limits.  Such a sequence-independent onset is
  not justified: convergence can be delayed arbitrarily.  The paper
  keeps constants `c,C` depending on the fixed data and allows the
  eventual threshold to depend on the degree sequence.  A uniform
  threshold would require specified quantitative degree envelopes.
- `exp(Theta(mu))` describes the exponential part of the residual
  bounds.  The logarithm of the entire quotient is only asserted to be
  `Theta(mu)` when `log(A)=o(mu)`, so polynomial geometry factors cannot
  silently dominate in slowly growing degree sequences.
- The full plateau payment is the integral of `|F|^3` over the whole
  shell and the whole time interval.  It is not `|u|^3`; the constant
  drift is not included in that payment.  This is stated explicitly.
- The exact shear is a smooth finite-energy solution on the torus for
  each finite parameter.  Its periodic extension to all of R^3 has
  infinite total energy.  The argument asserts no uniformly bounded
  energy family or limiting weak solution.
- The paper states the cutoff properties used by the sign argument:
  nonnegative spatial bump, positive exterior subcap, nonnegative time
  cutoff, and a fixed terminal interval where the time cutoff equals
  one.  The latter is indispensable for the stated terminal lower bound.
- The endpoint derivative majorant is proved via a generating function
  rather than left as an unnamed classical inequality.
- The source's duplicated line in L.50 and stray `qquad` tokens are not
  carried into the paper.

## Sign audit

The heat generator is `+D^2`; on a real Fourier mode it produces
`exp(-n^2 t)`.  The imaginary carrier shift in the conjugated polynomial
formula is `+2 i M s/A^2`.  Replacing it with a negative shift would not
reproduce the exact Fourier damping.

The transport is `y-Bt` with `B<0`.  In polynomial coordinates the
positive cap has displacement `r+delta0+gamma*s` and its reflected
negative partner has `r+delta0-gamma*s`.  The positive cap is larger at
times in `[3,4]`.  Since the integrated radial weight is negative on the
positive cap and the drift is negative, the paired signed contribution
is positive.  Early times are not assumed to have this sign; their
absolute contribution is estimated and absorbed quantitatively.

The physical energy-flux integral includes `|u|^2 u`.  The terms
containing a derivative in x3 and the constant `B^3` term integrate to
zero.  The surviving integral is the stated quadratic `F` flux, with
factor `a^2 R^3/2`.

## Dynamic transfer audit

On degree-at-most-m polynomials, the exact generator after
`w=(exp(i eta x)-1)/(i eta)` is

`L_eta = (1+i eta w)^2 D_w^2 + i eta (1+i eta w) D_w`.

It preserves the polynomial space.  The norm difference from `D_w^2`
is `O(eta m^2)`.  Weighted coefficient norms give the explicit error

`eta * poly(m,A) * exp(C m + C m^2/A^2)`.

Every complex evaluation remains in a smaller disk than the coefficient
radius.  The real drift is retained.  The carrier, scalar damping,
imaginary displacement, and nonlinear coordinate error are each included.
The error tends to zero because `eta = A exp(-9 L^2/40000)` and
`m=o(A^2)`, not because the degree is held fixed.

## Unproved directions excluded from theorems

- Degrees comparable to or larger than A^2, including the formal
  `m ~ kappa A^4` saddle, are outside both the edge asymptotic and the
  available exact-transfer estimate.
- The stated Chebyshev family does not optimize over all one-band
  packets.  A negative normalized rate for this family is not a uniform
  obstruction theorem.
- The construction does not lie in an additionally imposed mean-zero,
  inversion-paired subclass unless that is proved separately.
- The finite diagnostic quadrature and algebraic certificates are not
  needed to prove any theorem in this section.  They provide no missing
  continuum, uniformity, or sign argument.

## Checks still owned by manuscript integration

The parent manuscript must unify duplicated geometry and notation with
the full-frequency upper-bound section, preserve the `|F|^3` payment
definition, and retain the terminal cutoff requirement for the lower
theorem.  Bibliography cross-checking and PDF compilation are outside
this section audit.  None of the labels here by itself certifies novelty
or priority; those require separate literature comparison.
