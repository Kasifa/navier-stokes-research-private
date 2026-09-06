# Independent cross-audit of the quantitative edge theorem

Date: 2026-09-06. Reviewer role: application-audit subagent, separate from
the quantitative-proof author. This is independent automated review within
one assisted research task, not independent human peer review or formal
proof-assistant verification.

Reviewed file: `sections/quantitative-edge.tex`.
SHA-256 at review:
`fd091c50680d13c762da81ef4f388914293f11156c4c25f944f3b04a2b02dddb`.

Scoped layout update, 2026-09-06: the profile proposition's concluding
sentence was split into “The conclusions ... hold.” and “Constants
may also depend on ...” to resolve a line overflow. The constant
dependencies and mathematical assertion are unchanged. Reverting only
those two wording lines in memory reproduced the previously audited
SHA-256 exactly:
`db6888129f5481720b48b68fc0e5dd9cba322cd6cfe7f27f9403692b17ab7f4e`.
The updated hash above therefore incorporates only this verified prose
and line-break change; the mathematical review was not unnecessarily
expanded or repeated.

Assessment: the stated quantitative amplitude and displacement estimates,
the general profile proposition, and both Chebyshev verifications follow
from the supplied hypotheses with the displayed constants and thresholds.
No mathematical correction was required by this audit. The error orders
are sufficient estimates; their optimality has not been proved.

## Rate geometry and local lower bound

For `psi(z)=sqrt(2z)`, direct differentiation gives
`psi''(z)=-(2z)^(-3/2)`. Thus
`Phi_s''=-(2z)^(-3/2)-(2s)^(-1) <= -(2s1)^(-1)`.
Integrating from the unique stationary point gives the stated global
quadratic loss `(z-z_s)^2/(4s1)`, including `z=0` by continuity.
Solving the stationary equation gives
`z_s=2^(1/3)s^(2/3)`, `F_s=3*2^(-4/3)s^(1/3)`, and
`z_s/(2s)=G_s=2^(-2/3)s^(-1/3)`.

The interval `[z_s,z_s+1/mu]` lies inside `J=[z_-,z_++1]` for
`mu>=1`. On that interval the absolute curvature is at most `D_*`.
The scaled quadratic loss is at most `D_*/2`; the absolute linear
tilt loss is at most `C0/(2s0)`. The Gaussian change of measure has
a factor `mu`, and the interval length is `1/mu`, so those factors
cancel. This gives exactly

`I >= L_* mu^(-b) exp(Bcal-d mu^2 epsilon)`.

No hidden power of `mu`, or dependence on an unchosen saddle interval,
is missing from `L_*`.

## Gaussian envelope and first moment

Young's inequality costs exactly

`C0^2 s1/(2s0^2)=H_*`

when the retained quadratic coefficient is `mu^2/(8s1)`. Extending
the resulting Gaussian integral to the real line gives the factor
`sqrt(2s1/s0)`, confirming `V_*`.

Dividing the global upper envelope by the local lower bound gives
the stated normalized density upper bound

`K_* mu^(b+1) exp(d mu^2 epsilon) exp(-a_* mu^2(z-z_s)^2)`.

For any `r>=0`, the first absolute moment outside distance `r` is at
most

`(K_*/a_*) mu^(b-1) exp(d mu^2 epsilon-a_* mu^2 r^2)`.

This uses the exact integral of `|x| exp(-a_* mu^2 x^2)` over both
tails, not a probability estimate without moment control. Substitution
of the displayed `r^2` cancels `d mu^2 epsilon`, leaves the power
`mu^(b-1-(b+1))=mu^(-2)`, and leaves a constant at most one because
`(K_*/a_*) exp(-log_+(K_*/a_*))<=1`. Hence
`E|Z-z_s|<=rho` as claimed.

The bound is valid under each displaced Gaussian measure, including
negative displacements. Differentiation under the integral is justified
by the global exterior envelope and Gaussian decay. It gives

`mu^(-1) partial_c log I = (E Z-c/mu)/(2s)`.

This establishes the fine-scale error without taking a ratio of two
coarse amplitude approximations.

## Signed interior and negative exterior, including derivatives

The profile hypotheses cover the whole real line. The middle interval
has absolute Gaussian integral at most one. Its derivative is bounded
by the integral of the absolute derivative of a full Gaussian,
`1/sqrt(pi s0)`.

For the negative exterior `y=-2A-u`, the threshold gives `A>=C0`
because `A=mu/epsilon`, `epsilon<=1`, and `mu>=C0`.
Therefore `2A+u+c>=A+u`. Splitting the Gaussian penalty gives

`-A^2/(4s1)+H_tail mu^2-u^2/(8s1)`.

Here `H_tail=F_(2s1)` is exactly the maximum of
`sqrt(2z)-z^2/(8s1)`. The threshold
`epsilon<=1/sqrt(8s1 H_tail)` makes
`H_tail mu^2<=A^2/(8s1)`, leaving both negative quadratics in the
proof. The resulting Gaussian integral is bounded by the second term
of `E0`.

The absolute derivative multiplier is at most `(3A+u)/(2s0)`.
The three displayed elementary integrals/supremum are correct:
`sqrt(2 pi s1)`, `4s1`, and `2 sqrt(s1/e)`.
Multiplication by `3A`, division by the Gaussian prefactor, and
addition of the middle contribution produce exactly `E1`.
Neither the remainder nor its derivative needs a favorable sign.

These derivative estimates are necessary: control of the remainder's
value alone would give an additive ratio error that need not vanish
when the two displacements coincide.

## Thresholds and passage to the signed logarithm

All threshold constants are fixed from the profile and compact sets
before choosing `mu,A`. There is no implicit threshold depending on
the value it is meant to bound. The lower exponential budget is

`1 - 1/4 - 1/4 - 1/8 - 1/8 = 1/4`.

The first two losses are `d epsilon` and the linear displacement term.
The remaining losses bound `b log mu` using `log mu<=mu` and then
the constant `log_+(1/L_*)+C0^2/(4s0)`. This verifies
`I>=exp(kappa mu^2)`, with `kappa=F_*/4`.
The final threshold ensures `E0 exp(-kappa mu^2)<=1/2`.
Thus the signed convolution is positive and its logarithm is defined.

The bound `rho<=rho_*` uses only `epsilon<=1`, `mu>=1`, and
`log mu<=mu^2`. Consequently `|partial_c log I|<=mu M_*`.
The exact difference formula for the two logarithmic derivatives is

`partial_c log Q - partial_c log I`

`= (partial_c Remainder - Remainder partial_c log I)/(I+Remainder)`.

Using `E0,E1`, `I>=exp(kappa mu^2)`, and `mu>=1` gives the
displayed `E2` after division by `mu`. Integrating the derivative
estimate over the segment between `c1,c2` gives an error proportional
to `|c2-c1|`. In particular the error is exactly zero at `c1=c2`;
there is no leftover displacement-independent remainder.

At `c=0`, the direct upper/lower bounds on `I`, together with
`|log Q-log I|<=2E0 exp(-kappa mu^2)`, give the explicit amplitude
error. The simpler orders follow by elementary bounds on `r` and
`exp(-kappa mu^2)`. No relation such as `epsilon mu -> 0` is imposed.

## First- and second-kind verification

Integrating the derivative of `arcosh(1+u)` proves the three displayed
bounds. In particular the linear tangent bound on `(1+t/2)^(-1/2)`
produces the coefficient `1/12`; it is valid even when that lower
bound becomes negative. On the fixed interval `J`, multiplying by
`n` and using `n sqrt(epsilon)=mu^2` gives
`d=sqrt(2)Z^(3/2)/12`.

For `T_n`, `cosh(n theta)` is between `exp(n theta)/2` and
`exp(n theta)`. Parity and the classical trigonometric definition
give the two-sided envelope and interior bound.

For `U_(n-1)/n`, the finite exponential sum gives positivity and the
global envelope; its trigonometric counterpart gives the interior
bound, including endpoints by continuity. The exact identity

`n sinh(theta)=mu^2 sqrt(z(2+epsilon z))`

eliminates dependence on `n` in the local prefactor. On `J`,
`n theta>=mu^2 h_*>=1` with the stated `mu0`.
The inequality
`sinh(n theta)>=((1-exp(-2))/2)exp(n theta)`
then gives the claimed `k mu^(-2)` lower bound. This verifies every
profile hypothesis with constants independent of `n,A`.

The normalization remark is also correct: for
`n_j=ceil(exp(j^3))`, `A_j=n_j^2/j^3`, one has exactly `mu_j=j`
and `epsilon_j=j^4/n_j^2 -> 0`, but
`log(n_j)/mu_j^2 ~ j`. Thus normalization removes a real obstruction
in the original unrestricted joint range. No general Jacobi or
second-kind Navier–Stokes realization is inferred from this verification.

## Supplementary finite checks

Local `python3` independently checked three exact rational identities
for the `1/12` coefficient, lower-exponent threshold budget, and
negative-tail split. It also checked 66 finite identities/inequalities:
the three arcosh inequalities at eight nonnegative points, both saddle
constants at five positive times, and the normalized second-kind
exponential formula plus its envelope for four degrees and four
hyperbolic arguments. All passed.

These checks are transcription diagnostics. The all-parameter claims
rest on the analytic inequalities reviewed above, not on the finite
samples. No claim of best error order, exhaustive literature coverage,
or external peer approval is made.
