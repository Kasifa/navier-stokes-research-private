# Upper-bound scientific audit

Date: 2026-09-05. Scope: R0.76J and the complete-clock/full-plateau implication, including the time-weighted lemma in the previous 148-line draft. This audit rechecked the calculations from the source proofs; old PASS files and source hashes were not treated as mathematical evidence.

## Files read

- `navier-stokes-r074m/research/r076j_local_edge_extrapolation_reconstruction.md`
- `navier-stokes-r074m/research/r076i_chebyshev_scale_full_plateau_window.md`
- The model, collar geometry and complete-real energy identity in `navier-stokes-arxiv-paper/papers/exact-shear-flux-obstructions/main.tex`.
- The previous `v1/main.tex` time-weighted lemma.

The proposed integrated section is `sections/upper-bound.tex`. It is self-contained apart from the two explicitly stated published exponential-sum inequalities and standard Fourier Plancherel, Minkowski and Hölder. Required bibliography keys: `Zhang2026` and `Erdelyi2017`. Required theorem environments: `theorem`, `lemma`, `remark`. It uses standard AMS/LaTeX notation and no private macros. Main labels are `thm:ub-edge`, `lem:ub-delay`, `thm:ub-flux`, and `rem:ub-window`.

## Result

The original J statement survives the audit:

`|T| <= C a^(2/3) R^(-1/3) q^7 exp(20 sqrt(2) q sqrt(Delta_a)) M^(2/3)`.

Here `Delta_a=(delta+delta0)/(a-delta0)`, the flux uses the full `[0,4R^2]` clock, and `M` is the unweighted cubic mass on the full physical plateau over that clock. The constant is independent of all amplitudes, phases, drift `B`, scale `R`, absolute carrier frequencies and frequency separation. The band condition `n_q <= 2 n_1` remains essential to the temporal rescaling.

The section also keeps the sharper polynomial coefficient directly implied by the proof:

`q^4 + q^7/a^2 + q^(13/3)`.

This is bounded by `3 q^7` when `a,q>=1`. It is a modest supplementary consequence of the improved temporal lemma, not a claim that the polynomial power is optimal.

## Detailed checks and improvements

1. **Half-plane basis.** With `Re zeta_j>0`, the rational basis has unit boundary norm, vanishing evaluation against each earlier kernel, and nonzero triangular residue. The conjugations in the kernels and Blaschke factors are consistent for an inner product linear in its first variable. Distinctness is imposed only after merging repeated exponents.
2. **Volterra majorant.** The positive and negative time bounds follow from a subset expansion. Each `ell`-fold convolution supplies a simplex factor `t^ell/ell!`; no frequency gap is divided out. With a common real part `beta/2`, this gives the exact Laguerre majorant in J.
3. **Finite-range estimate.** At `y>=25N`, `-y+4 sqrt(Ny)<=-y/5`. The relative tail is at most `5N exp(-5N)<1/20` for every `N>=1`. Thus `I_beta <= (20/19) I_[0,25N/beta]`. No specialized finite-range theorem is imported.
4. **Edge constant.** Setting `beta=25N/2` and squaring the Laguerre bound gives exponent `10 sqrt(2) N sqrt(d)` in the squared inequality and hence `5 sqrt(2) N sqrt(d)` in the norm inequality. The prefactor is `sqrt(250/19) N`.
5. **Interior observation.** A bilateral endpoint theorem alone does not establish an interior supremum. The paper includes the missing-in-a-short-summary argument: apply the zero-gap endpoint inequality to the left and right subintervals, multiply by their lengths, and add. This recovers the same `250 N^2/(19e)` bound at every interior point.
6. **Time-weighted lemma.** The previous draft's proof is correct. For rates in `[1,4]`, the basis bound is `8N exp(-2t+4 sqrt(8Nt)) I_infty`; the choice `S=128N` makes the exponent at most `-t`. Integrating gives `I_infty<=2I_S`. The essential norm step is on the fixed initial interval `[0,S]`, not `[0,T]`. Therefore the loss is `N^(4/3)`, uniformly for every `T>0` and arbitrary imaginary parts. Replacing `I_S` by `I_T` would introduce an unjustified `T^(1/3)` factor. The integrated section keeps this issue explicit.
7. **High-carrier scaling.** With `lambda=(n_1R)^2`, the rescaling `t=lambda s` gives `K_(4lambda)=lambda H`, and the weighted bound is `lambda int eta h^(2/3) <= C N^(4/3) lambda^(-1/3) H^(2/3)`. Both powers of `lambda` were rederived. For `lambda<=1`, ordinary Hölder is sufficient.
8. **Spatial derivative.** Affine scaling of the Markov input gives squared derivative loss `C(q^5+q alpha^2)`. Multiplication by the observation loss `q^2 exp(Phi)` gives `C(q^7+q^3 alpha^2) exp(Phi)`. The interval length is bounded above and below under the stated lower bound on `a`.
9. **Terminal row.** Time reversal on `[3,4]` gives positive-real-part exponents, which satisfy precisely the Kós hypothesis. The endpoint inequality yields `h(4)<=64q^3 H` and `h(4)^(2/3)<=16q^2 H^(2/3)`.
10. **Geometry.** The derivative of the radial cross-sectional mass is exactly `-2 pi y vartheta(|y|/R-a)`. The cutoff need not be even as a function of its radial displacement: its composition with `|y|` is even, so `W_a` is odd and has zero integral. This makes `Xi_a` compactly supported. Its second derivative has `L1` size `O(a)`, not `O(a^2)`.
11. **Complete energy identity.** All four signs in the real-square identity were rederived from `Q_s+vQ_z-a^(-2)Q_zz=-2a^(-2)|G_z|^2`. The initial face vanishes only because `eta(0)=0`. The terminal face is retained and estimated. Absolute values are taken after the real-square identity.
12. **Full mass conversion.** On `|z|<=1-delta0/a`, the plateau cross section has area `4 pi a delta0 R^2`; with `dt dx2=aR^3 ds dz`, the mass is at least `4 pi delta0 a^2 R^5 H`. The flux factor is `a^2 R^3/2`. Their quotient gives exactly `a^(2/3) R^(-1/3)`.
13. **Quantifiers.** The upper theorem allows every `q>=1`, every amplitude and phase, every drift, and every dyadic carrier satisfying the torus chart condition. The shrinking-gap mode-window statement is a separate asymptotic consequence. Its negative rate is the rate of the upper-bound coefficient, not an equality for every solution's flux.

## Primary literature checks

The author's PDF was read directly on 2026-09-05:

- Tamás Erdélyi, *Inequalities for exponential sums*, author manuscript: https://people.tamu.edu/~terdelyi/papers-online/sums_rev.pdf
- Publication metadata: *Sbornik: Mathematics* 208 (2017), 433–464, DOI `10.1070/SM8670`; https://www.mathnet.ru/php/archive.phtml?jrnid=sm&option_lang=eng&paperid=8670&wshow=paper

The author PDF equation (1.2), page 2, explicitly gives `|f(0)|<=2n ||f||L2[0,1]` for exponential sums whose exponents have nonnegative real parts. Its Theorem 9.1, page 10, explicitly gives the `108n^5 + sum lambda_k^2` Markov inequality. The journal version renumbers the latter as Theorem 2.20 according to the frozen research source; because the journal PDF fetch timed out in this audit, the manuscript states the exact formula and attributes the paper without relying on that unverified renumbering. The underlying inequality itself was checked in the first-party author text.

Zhang's metadata and current public entry were checked at https://arxiv.org/abs/2607.10501. The near-edge proof is attributed to its approach. No theorem from this preprint is used as an unchecked step: the basis, tail cutoff, Laguerre majorant and endpoint derivation are all included locally. The bibliography should identify it as a preprint and should not claim independent discovery of the near-edge scale.

## Remaining boundaries

- No numerical calculation proves the continuum estimates; this section is analytic.
- The upper theorem concerns the exact one-band shear model. It does not extend to arbitrary nonlinear packets or suitable weak solutions.
- No full-clock lower bound matching `exp(c q sqrt(Delta_a))` follows from the fixed-slice lower construction. That distinction must remain in the abstract and conclusion.
- The temporal lemma removes an avoidable logarithmic factor from the older proof; no originality or optimality claim is made for the lemma.
- The local coefficient-rate formulation uses an arbitrary `gamma>0`. The historical constant `-2/11907` corresponds to `gamma=2/3969` and carries no independent PDE meaning.

No blocking gap was found in the stated upper theorem. Compilation and cross-section integration are owned by the parent task and were not performed by this audit.
