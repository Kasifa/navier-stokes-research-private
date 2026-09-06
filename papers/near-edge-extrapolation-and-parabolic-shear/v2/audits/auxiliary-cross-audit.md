# Independent audit of the compressed auxiliary estimates

Date: 2026-09-06. Reviewer role: application-audit subagent, separate
from the author of the v2 compression. This is automated mathematical
review, not human peer review or formal proof-assistant certification.

Scope: complete reads of `sections/upper-bound.tex`,
`sections/sharpness.tex`, and the referenced scaling in
`sections/time-weighted.tex`. The source locators and imported classes
were cross-checked against `v1/literature/source-audit.md` and the
current `audits/literature-manuscript-audit.md`. Primary-source retrieval
was already completed by the literature reviewer in this task; this
audit did not repeat a web search or claim new primary-text access.

Result: **PASS after one hypothesis-scope clarification**, independently
verified in the updated file. No unresolved mathematical issue remains
within this scope.

## Resolved coefficient-lemma clarification

The first compressed draft said that a fixed polynomial yielded exactly
`n+1` positive frequencies after realification, without explicitly
carrying its preceding real-rootedness condition into that sentence.
This could be read as an assertion for every real polynomial. Under
that reading, `p=x^2+1`, `eta=1`, `M=2` is a counterexample:
`b_0=p(i)=0`, and only two positive branches remain.

The author changed the sentence to begin:

> For a fixed real-rooted p, M>0, and real theta

That change was read directly and resolves the issue. All applications
already used real-rooted Chebyshev or Legendre-kernel polynomials, so
no downstream conclusion or constant needed alteration.

## Imported spatial estimate and the factor 12 sqrt(2)

The imported Zhang statement uses unaveraged `L2(-1,1)`, arbitrary
real frequencies, complex coefficients, no separation, and `0<=d<=1`.
The prefactor `C_Z=sqrt(9*8191/2)` and exponent `3 sqrt(2) N sqrt(d)`
match the recorded source verification. Reflection handles the left
endpoint. Scaling `x=e t` gives the factor `1/e` after squaring.

For an interior observation point, the endpoint estimate on its two
adjacent intervals produces `2 C_Z^2 N^2` times each interval's
integral after multiplication by that interval's length. Adding them
and dividing by `2e` proves the same interior constant. The actual
endpoints were already covered, so no zero-length interval is used.

The squared exterior estimate has exponent `6 sqrt(2) N sqrt(d)`.
A real cosine packet has at most `2q` complex branches, hence
`N=2q` gives exactly `12 sqrt(2) q sqrt(Delta_a)`.
This substitution improves the old constant `20 sqrt(2)` by using
the sharper imported inequality; it is not a new extrapolation theorem.

The geometric assumptions imply `a-delta0>=delta+delta0`, so
`Delta_a<=1`. They also imply `e_a>=1/2`, while the lengths of both
the observation and enlarged intervals are bounded above and below.
The imported near-edge range is therefore respected at every use.
Repeated frequencies or zero amplitudes can only decrease the number
of branches; using the original `N` or `q` weakens the upper bound.

## Derivatives, endpoint time face, and q powers

The Markov input is explicitly restricted to real spatial frequencies.
After mapping the spatial interval to `[0,1]`, its squared factor is
bounded by `C(q^5+q alpha^2)` because the interval length is bounded
and `sum(kappa_j^2+(-kappa_j)^2)<=8q alpha^2`.
Multiplication by the spatial observation factor `q^2` gives
`q^7+q^3 alpha^2` exactly as stated.

For fixed position, time reversal `r -> G(4-r,z)` gives exponents
with real parts `(kappa_j/a)^2>=0`, so the Kós input applies.
Its endpoint coefficient is `2N<=4q`; cubing gives `64q^3`.
Hölder on an interval of length one introduces no extra time factor.
Taking the two-thirds power then gives `16q^2` in the terminal
`h(4)` estimate. Complex conjugate branches may coincide at zero
drift; counting at most `2q` remains valid.

The first three terms in the energy identity contribute
`q^4+q^2+a^(-1)q^2`. The derivative term has two contributions:
`q^7/a^2` and `q^3 lambda`. For `lambda<=1`, the latter is
bounded by `Cq^3 H^(2/3)`. For `lambda>1`, the time corollary gives
`Cq^3(2q)^(4/3)lambda^(-1/3)H^(2/3)`, hence `Cq^(13/3)H^(2/3)`.
These are the displayed three refined powers. Since `a,q>=1`, the
smaller terms are absorbed and all three are at most `3q^7` together.

## Temporal scaling reference

The referenced equation `eq:ub-cutoff-time` exists in
`sections/time-weighted.tex` and needs only real decay parts at least
`lambda>0`. For the shear they actually lie in `[lambda,4lambda]`,
with `lambda=(alpha/a)^2=n_1^2 R^2`, so the hypotheses hold.

Writing the rescaled time function as `f(t)=G(t/lambda)` gives
`k(t)=h(t/lambda)` and `K_(4lambda)=lambda H`.
The cutoff bound `eta(s)<=||eta'||_infinity s` follows from
`eta(0)=0`. Consequently

`lambda integral eta(s)h(s)^(2/3) ds`

`<= C_eta lambda^(-1) integral_0^(4lambda) t k(t)^(2/3) dt`

`<= C_* C_eta N^(4/3) lambda^(-1/3) H^(2/3)`.

This checks both the reference and the inverse one-third power.
The absolute time decay and arbitrary imaginary parts are allowed by
the imported temporal result. No terminal-horizon factor is missing.

## Energy identity and dimensions

The transverse cutoff derivative, odd kernel `W_a`, and compact
primitive `Xi_a` are the same exact geometry as in the application
audit. Their norms have the stated orders: the cap widths are `O(1/a)`,
the kernel height is `O(a)`, and its derivative's `L1` norm is `O(a)`.

Multiplying the scalar energy equation by `Xi_a` and integrating gives
the displayed four terms with the correct signs. There is no initial
face because `eta(0)=0`. Sign assumptions on `eta'` are unnecessary;
its absolute norm is used. The resulting bound is uniform in drift.

The full plateau includes its caps. Restricting only for a lower bound
to `E_a` gives cross-sectional area `4 pi a delta0 R^2` and thus
`M>=4 pi delta0 a^2 R^5 H`. Combined with the exact numerator factor
`a^2 R^3/2`, this leaves powers `a^(2/3)R^(-1/3)`.
The shrinking-gap remark then follows from
`q sqrt(Delta_a)=o(L^2)` under `q=o(L^(5/2))`, and
`log(q)=O(log L)`. It concerns the coefficient's rate, not an attained
flux value or phase transition.

## Compressed spatial witnesses

The coefficient formula follows by Taylor expansion at `i/eta`.
Real-rootedness and Rolle's theorem make each derivative nonzero at
that nonreal point. Modulation has positive frequencies `M+j eta`;
they are distinct and in `[M,2M]` when `n eta<=M`. Realification
adds only their negative conjugates. The elementary bound
`|w_eta(x)-x|<=eta x^2/2` is valid for real `x` and gives compact
convergence for each fixed polynomial and carrier.

For the exterior witness `2T_(q-1)(x) cos(x-1-d)`, its squared
`L2` norm is at most `8`; its cubed `L3` norm is at most `16`,
whose two-thirds power is less than `8`. At `1+d`, the carrier is
one and the Chebyshev lower bound gives the claimed point ratio.
On the strip of length `d/8`, its squared carrier is at least `1/2`.
The squared field is therefore at least one-half of the exponential
factor, giving the integral factor `d/16`. Dividing by either squared
norm gives `d/128`. The use of `arcosh(1+x)>=sqrt(x)` is confined
to `0<=x<=1`, since `x=7d/8` and `d<=1`.

For the Legendre kernel, orthogonality gives
`K(1)=||K||_2^2=q^2/2`; the sup bound gives
`||K||_3^3<=q^4/4`. Its orthogonality with weight `1-x` follows
by applying the reproducing identity to `(1-x)r`, of degree at most
`q-1`, for every `r` of degree at most `q-2`. A polynomial of degree
`q-1` with fewer than that many sign changes in `(-1,1)` would
contradict this positive-weight orthogonality after multiplication by
its sign-changing factors. Thus the kernel has exactly that many
simple interior roots, licensing the coefficient lemma.

The carrier equals one at the endpoint and does not increase either
norm. The ratios are therefore at least `q/sqrt(2)` and
`2^(-1/3)q^(2/3)`. All conclusions are supremum statements along
confluence, so no attainment at positive confluence parameter is
asserted. The appendix correctly distinguishes the squared `L3`
lower power `q^(4/3)` from the available upper power `q^(5/3)`.

In the integer realization, the prescribed initial factor cancels
heat damping at time `R^2s_*`, and the chosen phase cancels advection
there. Substitution gives exactly the displayed carrier and
coefficient identity. `n_0>=q-1>=1` ensures positive integer
frequencies and the dyadic band. The statement permits initial data
depending on the prescribed time and explicitly does not use it as
a fixed-initial-data full-time lower bound.

## Finite exact arithmetic supplement

With Python rational arithmetic, the reviewer independently generated
Legendre polynomials from their three-term recurrence and checked
`K(1)`, `integral K^2`, and every required weighted orthogonality
identity for `q=2,...,9`: 52 exact identities passed.
Four further exact assertions checked the exponent `6*2=12`, the
power `3+4/3=13/3`, and the remaining powers of `a` and `R`.
These diagnostics do not replace the analytic all-degree arguments.

## Reviewed hashes after the resolved clarification

```
sections/upper-bound.tex 5878c9a176a11069cd9cac80fca67796688bb524abf66333526f53f02536ffaf
sections/sharpness.tex 70dfbc20c90bc2553437a2dedfc1b5d7a96a2b245b5455dc1687e214cae5be9b
sections/time-weighted.tex 8b59ed97145ac07a710b87dbc6c964f9b974009ea97d6e5d4d6d43bf11bcb7ae
```

Subsequent mathematical changes require a scoped update of this review.
