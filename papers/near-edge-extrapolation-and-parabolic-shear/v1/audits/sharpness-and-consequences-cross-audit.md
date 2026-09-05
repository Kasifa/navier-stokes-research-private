# Independent cross-review of sharpness and consequences

Date: 2026-09-05.

Reviewed `sections/sharpness.tex`, `sections/consequences.tex`, the
corresponding statements in `main.tex`, `sections/diagnostic.tex`, and
the diagnostic's calculation code and archived rows.  The proofs were
checked directly; earlier source-audit verdicts were not treated as
correctness evidence.

## Result and requested integration edits

No mathematical error was found that invalidates the stated spatial
lower bounds, the coefficient nonvanishing strengthening, the
quantitative growing-degree approximation, the exact prescribed-time
realization, or the consequences of the upper coefficient.  Three
small statement edits should be made before final integration:

1. In `thm:integer-slice`, explicitly fix an arbitrary real phase
   `theta`.  The displayed identity currently uses theta without
   quantifying it.  In its final convergence assertion specify
   **every fixed M>0**.  The formulas and proof already establish
   these universal choices.
2. In `cor:critical-coefficient`, explicitly inherit the fixed spatial
   and time cutoffs and the admissible choice of R(L) from
   `thm:ub-flux`.  In particular, the chart condition must continue
   to hold, and the cutoff norm entering C must not depend on L.
   With these inherited hypotheses, the rate calculation is correct.
3. In the final sharpness paragraph, specify that the Jacobian factor
   `e_a^(-1/2)` compares the same physical observation window:
   `x in [-1,1]` corresponds to `z in [-e_a,e_a]`, and the observed
   point is mapped to `z=e_a*x_*`.  The factor alone is not correct
   if the z norm is instead taken on the different window `[-1,1]`.

The diagnostic caption also has a minor grammatical ambiguity: use
"m is the positive even integer nearest to A^sigma".  The code really
uses `max(2,2*round(A^sigma/2))`, matching the intended meaning.

## Real dyadic lower bounds

For n=q-1, the confluent limit with p=T_n, carrier M=1 and phase
`-(1+d)` is `g0(x)=2 T_n(x) cos(x-(1+d))`.  On `[-1,1]` its squared
L2 norm is at most 8 and its cubed L3 norm at most 16.

At x=1+d the carrier is exactly one and
`T_n(1+d) >= exp(n arcosh(1+d))/2`.  Dividing by `2 sqrt(2)` yields
the displayed pointwise constant `1/(2 sqrt(2))`.  The elementary
comparison `arcosh(1+d)>=sqrt(d)` is valid for `0<=d<=1`.

On the interval `[1+7d/8,1+d]`, of length d/8, the squared carrier
is at least 1/2.  Consequently the exterior integral is at least
`(d/16) exp(2 n sqrt(7d/8))`.  Division by 8 gives d/128 in L2;
the same constant works for L3 because `16^(2/3)<8`.  The same
confluent sequence proves both exterior claims.  There is no hidden
change to normalized-average norms.

For the endpoint kernel K_n, Legendre orthogonality gives
`K_n(1)=||K_n||_2^2=q^2/2`, while `||K_n||_infinity<=q^2/2`.
Thus `||K_n||_3^3<=q^4/4`.  The carrier is one at the observation
endpoint and cannot increase either norm, giving exactly
`q/sqrt(2)` and `2^(-1/3) q^(2/3)`.

The remark about the squared L3 upper power was independently checked
against [Erdelyi's arXiv text, Theorem 2.10](https://arxiv.org/html/1602.02315v1).
Its dimension exponent is `1/2+1/p`; p=3 and squaring give 5/3.
The interval rescaling and the replacement N=2q affect constants but
not this exponent.  The manuscript correctly does not call the
demonstrated lower exponent 4/3 optimal.

## Coefficients and real roots

The identity
`w_eta = i/eta + exp(i eta x)/(i eta)` gives
`b_j=p^(j)(i/eta)/(j! (i eta)^j)` exactly.  For a real-rooted p,
all nonconstant derivatives are real-rooted and hence nonzero at the
strictly nonreal point i/eta.  The top derivative is constant and
nonzero.  This proves nonvanishing for every eta>0, not just at small
eta.  It does not assert a uniform lower bound on coefficient size.

The proof that K_n has n simple roots in (-1,1) is valid.  Its
reproducing identity makes it orthogonal to all lower-degree
polynomials for the positive weight (1-x).  Multiplying by its
distinct sign-changing factors contradicts that orthogonality unless
there are n such roots.  Degree n then forces all those roots to be
simple and excludes every other root.  Chebyshev real-rootedness is
immediate from its explicit roots.

Realification gives q distinct positive frequencies M+j eta and their
conjugate negative partners.  The condition `(q-1) eta<=M` puts the
positive frequencies in a closed dyadic band.  This correctly counts
q positive cosines versus 2q exponential branches.

## Growing degree

The Chebyshev and Legendre coefficient recurrences are bounded by
`S_(n+1)<=2 S_n+S_(n-1)`, so their absolute coefficient sums are at
most `(1+sqrt(2))^n`.  Summing the Legendre kernel yields
`S(q^(-1)K_(q-1))<=(q/2)(1+sqrt(2))^(q-1)`.

On `|x|<=2`, `|w_eta(x)-x|<=2 eta<=1/4`.  The connecting segment
lies in the complex disk of radius 9/4.  The derivative majorant is
therefore `C q^2 ((9/4)(1+sqrt(2)))^q`, and its base is strictly
less than 6.  The carrier error has size at most 4 eta and the
polynomial factor is bounded by `C q 6^q`.  Together these prove
the displayed `C eta q^2 6^q` absolute error.

Smallness of this error implies `q eta->0`, which ensures
`ceil(1/eta)>=q-1` eventually.  Coefficient nonvanishing requires no
further condition.  For eta=AR with the stated scaling, its logarithm
is `-rho L^2/4+q log(6)+O(log L+log q)`, proving both the o(L^2)
range and the strict limsup range stated in the lemma.

The passage to spatial lower orders is valid even when the degree
grows.  The normalized kernel has bounded L2 norm and endpoint value
of order q; the Chebyshev family has bounded interior norms and a
strict positive lower amplitude on the chosen exterior subinterval.
A uniform error tending to zero therefore preserves the lower bounds
with fixed reduced constants.  This is an absolute-error argument,
not an unjustified fixed-degree convergence argument.

## Prescribed-time heat realization

The proposed amplitude is `2|b_j| exp(n_j^2 R^2 s_*)`.  At the selected
time it exactly cancels damping.  Substituting
`phi_j=-theta-arg(b_j)-n_j B R^2 s_*` cancels transport as well, leaving
`2 Re(exp(i theta+i n0 eta x) p(w_eta(x)))`.  The sign of this phase
is correct.  There is no uniform bound on prepaid amplitudes, and no
such bound is claimed.

Each term solves the scalar transport-diffusion equation, and the
displayed velocity solves the vector equations with constant pressure.
The requirement `n0>=q-1` gives the exact integer dyadic constraint.
The quantifier remains "for each prescribed time, construct a packet";
the text does not substitute "one packet works for every time".

The evolution formula away from s_* has the correct positive imaginary
shift `+2 i M_eta tau/A^2`, scalar damping, and real transport shift.
It holds for this finite sum, including earlier finite times.  It does
not turn the static polynomial profile into a time-persistent witness.

## Upper-coefficient consequence and heat scales

In `cor:critical-coefficient`, exact substitution gives the coefficient
`C a^(2/3) q^7 omega^(1/3) exp(20 sqrt(2) q sqrt(Delta_a))`.
For `q/L^(5/2)->kappa`, the non-polynomial rate is exactly

`-gamma/3+20 sqrt(2) kappa sqrt((delta+delta0)/p0)`.

The logarithm of q is O(log L), including kappa=0, because q is a
positive integer and the ratio has a finite limit.  Thus no omitted
polynomial term contributes to the quadratic logarithmic rate.  Solving
for strict negativity gives the stated factor `gamma/(60 sqrt(2))`.
The manuscript correctly treats this as a sufficient range for its
proved coefficient, not as an actual transition of the flux.

For the power-law family m~A^sigma, the three powers
`A^(sigma-1/2)`, `A^((2sigma-1)/3)`, and
`A^((4sigma-2)/3)` are correct.  The interval `1/2<sigma<2` implies
both mu->infinity and mu/A->0.  The distinction between a uniform
upper-coefficient rate and the attained rate of one explicit family
is stated correctly.  The warning concerning mu growing slower than
log A is necessary and is present.

## Main text and diagnostic scope

The abstract and introduction distinguish prescribed-slice witnesses
from the complete-time family, retain the degree range, exclude the
constant drift from the payment, and do not make a general weak-solution
claim.  No distortion of the parabolic theorem was found.

The diagnostic evaluates log(cosh) stably and uses a Gaussian penalty
with variance 2s, matching the positive exterior integral.  Its degree
rounding and all sixteen data rows match the stated four A values and
four exponents.  In particular the sigma=0.75 tilt error moves away from
zero across the displayed sequence, as the caption explicitly says.
The code and caption correctly treat this as a finite diagnostic, not
a rigorous enclosure or a proof of a limiting or PDE statement.

This review did not modify any manuscript source.  The requested
statement edits are left to the parent integrator.
