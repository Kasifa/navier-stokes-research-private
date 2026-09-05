# Finite exact algebra checks

Date: 2026-09-05. Script: `checks/verify_algebra.py`.

The checks support the finite algebra in the manuscript. They do not prove the uniform limits, saddle estimates, infinite-dimensional inequalities, eventual positivity for an arbitrary degree sequence, or the main PDE statements. Those conclusions use the written analytic proofs and the separate scientific audits.

## Execution

Working directory:

`/Users/kasifa/Documents/Math/navier-stokes-arxiv-paper/papers/near-edge-extrapolation-and-parabolic-shear/v1`

Command:

```sh
python3 checks/verify_algebra.py
```

Observed interpreter: Python 3.9.6. The script uses only the standard library. Every mathematical comparison uses `fractions.Fraction`; complex coefficients are represented by two rational components. Elapsed time is the only floating-point quantity, and it is not used in any mathematical check. No tolerance or stochastic sample is used. The script writes only its JSON report to standard output.

Result: **PASS**, exit code 0. There were **1,866 checks: 1,725 positive checks and 141 negative checks**. The reported elapsed time was 0.600 seconds on this run.

Script SHA-256:

`d8c33940c53334d1726823511aff27cc8c2b722db0150dde35e37e802db44fb6`

## Coverage and exact counts

| Check family | Positive | Negative |
|---|---:|---:|
| Finite-eta coefficient identity | 68 | 0 |
| Nonzero coefficients in the sampled degrees | 68 | 0 |
| Endpoint derivative recurrence | 561 | 0 |
| Degree-end derivative boundaries | 66 | 0 |
| Heat derivatives versus Gaussian moments | 306 | 0 |
| Explicit heat polynomials of degrees zero through five | 72 | 0 |
| Scaled endpoint double series | 468 | 0 |
| Carrier conjugation sign | 18 | 0 |
| Constants and scaling powers | 17 | 0 |
| Critical coefficient equality | 27 | 0 |
| Below/above critical coefficient comparisons | 54 | 0 |
| Mutated finite-eta Taylor center | 0 | 64 |
| Mutated endpoint recurrence | 0 | 31 |
| Mutated Gaussian variance | 0 | 3 |
| Mutated imaginary shift sign | 0 | 12 |
| Missing square-root-of-two threshold factor | 0 | 27 |
| Invalid-input boundaries | 0 | 4 |
| **Total** | **1,725** | **141** |

Each table entry counts one explicit equality, inequality, detected mutated identity, or expected exception. Vector coefficient equality counts as one check per parameter case, rather than one check for every coefficient. This convention is also used by the script's JSON counter.

## Independent constructions

For the finite-eta identity, one implementation applies the three-term Chebyshev recurrence directly to the polynomial `(Z-1)/(i eta)` in the Fourier variable `Z`. The other constructs the monomial coefficients from the closed factorial formula for `T_m`, differentiates those coefficients directly, and evaluates the manuscript formula

`b_j = T_m^(j)(i/eta)/(j! (i eta)^j)`.

Thus the two compared sides do not share either a polynomial-composition routine or a Chebyshev recurrence. Degrees `m=0,...,16` and `eta=1/7,1/2,2/3,3` were checked. Both parity classes, zero degree, small and larger rational eta were included. These are exact finite samples, not a claim that eta values of this size fall in the paper's asymptotic regime.

For the endpoint recurrence, the closed monomial polynomial is differentiated at one and compared with the product recurrence

`D_(k+1) = (m^2-k^2)/(2k+1) D_k`.

Degrees zero through 32, every derivative order through the degree, the zero factor at the final recurrence step, and the derivative just beyond the degree were checked.

For heat evolution, one implementation sums actual even derivatives with coefficients `tau^j/j!`. The other computes the monomial expectation against Gaussian moments generated recursively by `moment[k]=(k-1) 2 tau moment[k-2]`. Degrees zero through 16 were checked at three nonnegative heat times and six signed rational evaluation points. Explicit independently typed degree-zero-through-five heat formulas provide a third comparison at 72 parameter cases.

The endpoint double series was compared with the Gaussian-moment implementation for degrees zero through 12, `A=1,3,7/2`, `s=0,1/3,4`, and `c=-2,0,1,3/2`. This covers the zero-time boundary, negative and zero displacement, and fractional physical scaling.

## Signs, powers, and threshold

On individual Fourier modes the conjugation was checked as the exact quadratic identity

`-M^2-(j eta)^2-2 M j eta = -(M+j eta)^2`.

The wrong imaginary-shift sign is rejected whenever both the carrier and shifted mode are nonzero; the `j=0` boundary is tested separately as a positive equality.

The scaling checks include the powers `a^(2/3) R^(-1/3)` in the upper theorem, cancellation of `R` under normalization, the surviving `omega^(1/3)`, the `a^(4/3)` quotient conversion, the lower plateau power, the `q^(13/3)` high-carrier term, the `lambda^(-1/3)` onset factor, and the critical growth power `L^(5/2)`.

The numeric constants are checked with rational arithmetic, including the squared near-edge prefactor, the doubling of the exponent after squaring and counting both frequency branches, the powers of two in `F_4`, `G_4`, and `2G_4`, and `(2/3969)/3=2/11907`.

For the critical coefficient, all quantities are positive, so equality and strict comparisons can be tested after squaring. The threshold

`kappa^2 = gamma^2 p0/[7200 (delta+delta0)]`

is compared with the squared positive term `800 kappa^2 (delta+delta0)/p0` and `(gamma/3)^2`. There are 27 rational choices of `gamma,p0,delta+delta0`; each has an equality check and strict checks at one quarter and four times the threshold square. These checks verify the formula for the sufficient upper-bound coefficient, not a sharp threshold for the actual flux.

## Negative controls and limits

Negative controls deliberately reverse the Taylor center, replace `m^2-k^2` by `m^2+k^2`, use Gaussian variance `tau` instead of `2 tau`, reverse the imaginary heat-carrier shift, and remove the threshold's square-root-of-two factor. All 137 mutated identity cases were detected. Four further checks confirm rejection of negative degree, zero eta in both coefficient constructions, and division by exact complex zero.

The script reads no manuscript source text and performs no string-presence checks. It therefore checks the mathematical formulas independently of their typesetting, while the document-level notation and formula correspondence remain the responsibility of the scientific and compilation audits. The finite parameter ranges are explicit and are not extrapolated into unproved continuum claims.
