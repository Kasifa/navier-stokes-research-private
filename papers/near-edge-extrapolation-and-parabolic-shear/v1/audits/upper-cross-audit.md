# Cross-audit of the complete upper bound and main framing

Date: 2026-09-05. Reviewer: the sharpness/literature subtask, independent
of the author of `sections/upper-bound.tex`. This review read the complete
upper-bound section and current `main.tex`, and compared the parabolic
theorem and quantitative consequences when checking the abstract.
No source file outside this audit was changed during this cross-review.

## Assessment

No blocking mathematical gap was found in the upper-bound theorem as
stated. Its temporal lemma is uniform in both the number of terms and
the terminal interval length, with the claimed N^(4/3) dependence.
The physical a/R powers, the four energy-identity signs, and the two
literature inputs are consistent.

Two minor editorial changes are recommended before finalization:

1. State `R>0` explicitly in the geometric assumptions. Its role as a
   scale is clear, but the displayed assumptions currently only give
   an upper bound for `(a+delta)R`.
2. In the abstract's parabolic sentence, name the quotient
   `R^(1/3) T / (M^plat)^(2/3)` when describing the residual
   `exp(Theta(mu))` factor. The unnormalized flux also contains the
   common heat amplitude at scale exp(C mu^2). The current phrase
   "positive integrated collar flux has an edge-dependent ... factor"
   can be read correctly, but is less precise than the theorem.

These are wording/assumption-explicitness issues, not defects in the
proof. The parent task owns any resulting edits.

## Half-plane and spatial estimates

- Inner products are linear in the first variable. The kernel at w is
  `(s+conj(w))^(-1)` and evaluation takes place at `conj(zeta_l)`.
  The factor `s-conj(zeta_l)` therefore vanishes at exactly the point
  needed for orthogonality. The signs and conjugations are correct.
- With distinct zeta_j in the right half-plane, every pole is simple.
  The triangular residue numerator `-zeta_j-conj(zeta_r)` has strictly
  negative real part and is nonzero; its denominator is nonzero by
  distinctness. Merging repeated exponents is sufficient.
- Multiplication by each factor `(s-conj(zeta))/(s+zeta)` preserves the
  boundary L2 norm. Fourier Plancherel on the finite exponential span
  is enough; no unproved completeness statement for a general Hardy
  space is required.
- The inverse factor is `I-2 Re(zeta) V_zeta`. The nested Volterra
  simplex has volume `|t|^ell/ell!` also at negative times after
  absolute values. With a common real part beta/2, the exponential
  prefactor is independent of the particular subset.
- The Laguerre bound follows coefficientwise from the central binomial
  coefficient estimate. It uses no frequency separation.
- In the tail, `y>=25N` implies `4 sqrt(Ny)<=4y/5`. The relative
  remaining energy is at most `5N exp(-5N)`, whose maximum for integer
  N>=1 occurs at N=1 and is below 1/20. Hence the factor 20/19 is valid.
- Negative-time evaluation cancels the weight exactly. Setting
  beta=25N/2 gives squared prefactor 250 N^2/19 and squared exponent
  10 sqrt(2) N sqrt(d); the asserted square-root bound follows.
- The interior supremum is actually proved. Affine endpoint bounds on
  the two subintervals have constants proportional to inverse length;
  multiplying by those lengths and adding yields the same bound on
  the interior. Endpoint cases are treated by the original theorem.

## Time-weighted lemma

For rates with real parts in [1,4], every l-fold convolution is bounded
by exp(-t) t^l/l!, since the real decay of every kernel is at least one.
The factors 2 Re(zeta)<=8 give

`|f(t,z)|^2 <= 8N exp(-2t+4 sqrt(8Nt)) I_infinity(z)`.

At `S=128N`, the exponent is at most -t for every t>=S. The integrated
tail is less than one half of I_infinity, hence
`I_infinity<=2 I_S`. This step is valid for arbitrary finite coefficients,
including highly cancelling ones. The imaginary parts do not enter.

For T>=S, Minkowski in L^(3/2)(E), followed by time Hölder, gives
`||I_S||_(3/2) <= S^(1/3) K_T^(2/3)`. This use of the fixed initial
interval is decisive: the right side has no T^(1/3). The late contribution
is bounded by `16N S^(1/3)(S+1)e^(-S) K_T^(2/3)`, uniformly smaller
than C N^(4/3) K_T^(2/3). The initial contribution is at most
`4^(-1/3) S^(4/3) K_T^(2/3)`. For T<S it is already the whole integral.

Under t=lambda s, `k(t)=h(t/lambda)` and
`K_(4lambda)=lambda H`. The prefactor from ds and the cutoff is
lambda^(-1), so the final factor is lambda^(-1/3), exactly as written.
The high-carrier argument is valid even when 4lambda<128N, because
the lemma includes its short-interval case.

## Literature inputs

The pure-real-frequency spatial derivative formula agrees with
Erdelyi's first-party text (arXiv v1 Theorem 9.1): its square is bounded
by C(N^5+sum mu_j^2) times the squared supremum. The interval I_a has
length bounded above and below, so affine scaling introduces only fixed
constants. The two signs of each cosine contribute
`sum mu_j^2 <= 8q alpha^2`. Multiplication by the spatial observation
loss therefore gives `q^7+q^3 alpha^2`, as stated.

The terminal estimate uses `r -> G(4-r,z)` on r in [0,1]. Its exponents
have nonnegative real parts `(kappa_j/a)^2` and arbitrary imaginary
parts. This is exactly the class in the Kós estimate recorded as
Erdelyi equation (1.2). Cubing `4q ||f||2`, then using Hölder on a
unit interval, yields `h(4)<=64q^3 H` and `h(4)^(2/3)<=16q^2 H^(2/3)`.
The argument does not import the different real-exponent results of
Erdelyi 2007 or 2008.

## Geometry, energy signs, and physical scaling

The shell lies in a Euclidean coordinate chart because
`(a+delta)R<pi/2`. Its cutoff is smooth at the origin because
`a-delta>=2delta0>0` leaves a neighborhood on which it vanishes.
No evenness of vartheta as a function of radial displacement is needed.

At fixed y=x2, transverse polar integration gives
`J(y)=2pi int_|y|^infinity r vartheta(r/R-a) dr` and
`J'(y)=-2pi y vartheta(|y|/R-a)` on both signs of y.
Consequently `W_a=-2pi a z vartheta(a(|z|-1))` is odd. Its two
supports have length O(1/a), height O(a), and bounded L1 norm.
The primitive Xi_a is compactly supported in I_a, has bounded L1 and
supremum norms, and `||Xi_a''||1=O(a)`, as claimed.

For Q=G^2 the scalar equation is
`Q_s+v Q_z-a^(-2) Q_zz=-2a^(-2)|G_z|^2`.
With E=int Xi_a Q, integration by parts gives
`E'=v int W_a Q+a^(-2) int Xi_a'' Q-2a^(-2) int Xi_a |G_z|^2`.
Solving for the transport term and integrating against eta gives the
displayed terminal, eta-prime, negative second-derivative, and positive
gradient terms. Eta(0)=0 removes the initial term and eta(4) is retained.

The first three absolute bounds are q^4, q^2, and a^(-1)q^2. The gradient
bound is `q^7/a^2 + q^3 lambda`, before time integration. For lambda<=1
ordinary Hölder suffices; otherwise the temporal lemma gives
`q^(13/3) lambda^(-1/3) <= q^(13/3)`. This proves the refined sum
`q^4+q^7/a^2+q^(13/3)`; with a,q>=1 it is at most 3q^7.

The exact flux factor is `a^2 R^3/2`. The plateau cross-section on
`|z|<=1-delta0/a` is `4pi a delta0 R^2`, and
`dt dx2=aR^3 ds dz`. Thus
`M^plat>=4pi delta0 a^2 R^5 H`, and division by its two-thirds power
gives `a^(2/3) R^(-1/3)` exactly. All omitted constants depend only
on the fixed cutoff data and derivative of the time cutoff.

## Main manuscript quantifiers and claims

The abstract and introduction preserve the distinctions between the
uniform upper theorem, a spatial witness chosen at one time, and one
fixed initial datum over a complete clock. The cubic observation is
explicitly identified as the mass of F, excluding the constant drift.
The torus setting and infinite-energy periodic extension on R3 are clear.

Prior-work attribution for the edge scale is present and no general weak
solution criterion is asserted. The supplementary real-rooted coefficient
fact is described as an elementary strengthening. The boundary
q=o(L^(5/2)) concerns an upper-bound coefficient; the consequences section
does not turn its sufficient threshold into an actual transition.

The parabolic theorem keeps algebraic factors and adds the extra
condition mu/log(A)->infinity before claiming divergence of the
unweighted quotient. This is important when mu grows slowly. Except for
the abstract wording recommendation above, the framing respects it.

This review is analytic. No new numerical experiment, compilation,
commit or public release was performed.
