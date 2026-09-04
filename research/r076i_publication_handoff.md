# R0.76I publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.76I-Step60`
- research label: `R0.76I`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.76H-Step59`
- cumulative recap required: `true`
- cumulative recap terminal release: `R0.76I-Step60`
- preceding recap terminal release: `R0.75W-Step48`
- formal scientific figure required: `false`
- core research commit:
  `0b73f68e072e573d9aaaa824e137e29a49d3cd67`

This handoff authorizes only R0.76I.  Do not read or publish later research
material.  Do not create or reuse a second publishing, reflection,
lessons-learned, usage-notes, temporary, or per-release task/system.  The
sole publisher must wait until `R0.76H-Step59` is deployed and online
verified, then append I and its cumulative recap to that same FIFO exactly
once.  R0.76I is complete only after its reader page, synchronized PDF, and
recap are all deployed and online verified; no R0.76J or later release may
enter the publication FIFO before that gate closes.  Afterward, ordinary
releases must retain the R0.76I recap byte-identically until the next
authorized milestone recap.

R0.76I is a substantial route change and positive conditional theorem, so
it triggers the next cumulative recap.  The recap must extend the frozen
R0.75W endpoint through R0.76I without silently rewriting earlier results.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `6277cb69dfad94cae89088c6a8c007967bdde97aceee7b19954d10ec53f6efce` | `research/r076i_chebyshev_scale_full_plateau_window.md` |
| `65adf8bc77f33c5d18184c612acc67246e48e7ad3c9059b85f269e92c9372dbe` | `research/r076i_chebyshev_scale_full_plateau_window_primary_audit.md` |
| `0ee0fbd75f9691e2ac898a57921f8a0574ba9af9ea652f85d0199856d7e3d423` | `research/r076i_report-source.md` |
| `f1475b2549490c3639c15a4fc103e704d0de98a518f50249b732a8e0a135d776` | `scripts/r076i_chebyshev_scale_full_plateau_window_fixtures.json` |
| `26485db072bf886fae88f0737546d7090f77b9b23e55c356bf8affe6aeba1da5` | `scripts/r076i_chebyshev_scale_full_plateau_window_expected.json` |
| `a14e7fe3bc3b118232328a6d9e4d9d4cedb1e685c057483e12416725024af538` | `scripts/r076i_chebyshev_scale_full_plateau_window_certificate.py` |
| `5e1ead81eb0f036d41addf2dd203527c3ae49aa497d483002a3973b69d88225c` | `scripts/r076i_chebyshev_scale_full_plateau_window_certificate_independent.rb` |
| `d23b771cd0e7c5253ba592f9efd2e7c0c2396cd928641f6463559b2b20953458` | `scripts/r076i_chebyshev_scale_full_plateau_window_qa.sh` |
| `6ae521f88a1e6116f466641bde60939e458b043b43ca025a10a83001613c590b` | `research/r076i_chebyshev_scale_full_plateau_window_certificate.json` |
| `b5d1f7b0e36f724522bc5b18442bad97ffe778e7be6ca579c0ca0bd89d9d061c` | `research/r076i_chebyshev_scale_full_plateau_window_certificate_report.md` |
| `f8c735e654031b8d5ae7029879086bf95086e7745317b7faa0e6750151093b4d` | `research/r076i_chebyshev_scale_full_plateau_window_independent_audit.md` |
| `7f709110b3191508541367846c9ef0358016cfcb91c160e00b9db123664dd34a` | `research/r076i_chebyshev_scale_full_plateau_window_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

R0.76E gave a frequency-uniform full-plateau estimate for exact real
constant shears, but paid `exp(Cq)` and therefore retained the frozen
negative logarithmic rate only for `q=o(L^2)`.

R0.76I uses a newly located endpoint extrapolation result for arbitrary
real-frequency sparse Fourier sums without frequency separation.  The full
plateau observes almost the entire interval between the two collar caps;
after normalization, each unobserved exterior gap has size

\[
 \Delta_a=\frac{\delta+\delta_0}{a-\delta_0}=O(a^{-1}).
\]

More precisely, retain the frozen geometry, cutoffs, and scaling `a=pL`,
and fix

\[
 q\in\mathbb N,\quad q\ge1,\qquad
 1\le n_1<\cdots<n_q\le2n_1,
 \quad n_j\in\mathbb N,
 \quad A_j\ge0,\quad \phi_j,B\in\mathbb R,
\]

with the exact real constant shear `u=(0,B,F(t,x_2))`, where

\[
 F(t,x_2)=\sum_{j=1}^q A_je^{-n_j^2t}
 \cos(n_jx_2-\phi_j-n_jBt).
\]

There are frozen constants `C_I<infinity` and `L_I<infinity`, independent
of `q`, `R`, the frequencies, amplitudes, phases, and `B`, such that every
frozen `L>=L_I` obeying the large-scale gate
`a>=delta+2delta_0` satisfies the estimates below.

The resulting spatial cost is

\[
 q^2\exp\!\left(12\sqrt2q\sqrt{\Delta_a}\right),
\]

not `exp(Cq)`.  A separate complex one-sided endpoint inequality makes the
final time trace polynomial in `q`.  Rebuilding all four rows of the exact
complete-real energy identity yields

\[
 |\mathcal T_{\boldsymbol n,R}|
 \le C_Ia^{2/3}R^{-1/3}q^7
 \exp\!\left(12\sqrt2q\sqrt{\Delta_a}\right)
 (M_{\boldsymbol n,R}^{\rm plat})^{2/3}.
\]

After the frozen normalization, `R` cancels and the admissible sufficient
window expands to

\[
 q(L)=o(L^{5/2}),
\]

which includes mode counts comparable with `L^2`.  The retained exact
normalized rate remains

\[
 -\frac2{11907}.
\]

In the normalized variables

\[
 p_{\boldsymbol n,R}^{\rm plat}
 :=R^{-2}\omega M_{\boldsymbol n,R}^{\rm plat},
 \qquad
 \mathfrak X_{\boldsymbol n,R}
 :=\frac\omega R[\mathcal T_{\boldsymbol n,R}]_+,
\]

the full theorem is

\[
 \mathfrak X_{\boldsymbol n,R}
 \le C_Ia^{2/3}q^7\omega^{1/3}
 \exp\!\left(12\sqrt2q\sqrt{\Delta_a}\right)
 \bigl(p_{\boldsymbol n,R}^{\rm plat}\bigr)^{2/3}.
\]

This closes the former `exp(Cq)` barrier only inside the exact one-band
constant-shear family.  It is a meaningful route improvement, not an
arbitrary Navier--Stokes theorem.

## Imported literature input and status

The principal new input is:

- Ruizhe Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*,
  [arXiv:2607.10501v1](https://arxiv.org/abs/2607.10501v1),
  submitted 2026-07-11.

Proposition 4.2 states, for at most `N` arbitrary real frequencies and
`0<=d<=1`,

\[
 |g(1+d)|
 \le\sqrt{\frac{9A_{\rm fr}}2}\,N
 \exp(3\sqrt2N\sqrt d)\|g\|_{L^2[-1,1]},
 \qquad A_{\rm fr}\le8191.
\]

This is a 34-page arXiv v1 preprint and is not represented as peer reviewed.
The local proof verifies the proposition's statement, constants, class, and
rescaling but does not reproduce its Hardy-space proof.  The composed
R0.76I theorem must therefore be labelled **CONDITIONAL-LITERATURE**.

The other inputs are from T. Erdelyi, *Inequalities for exponential sums*,
[journal record](https://www.mathnet.ru/eng/sm8670), *Sbornik:
Mathematics* 208:3 (2017), 433--464:

- journal Theorem 2.3, the pure-imaginary endpoint Nikolskii inequality;
- journal Theorem 2.20, the Markov estimate with
  `108N^5+sum(mu_j^2)`;
- equation (1.2), recording the Kós `E_N^+` estimate
  `abs(f(0))<=2N norm(f)_(L2[0,1])`.

Equation (1.5) records a sharper `pi N/2` form, but the proof retains the
sufficient `2N` constant.

## Full-plateau geometry

Set

\[
 e_a=1-\frac{\delta_0}{a},\qquad
 E_a=[-e_a,e_a],\qquad
 I_a=\left[-1-\frac\delta a,1+\frac\delta a\right].
\]

Under `z=e_ax`, the outer endpoint becomes
`(1+delta/a)/e_a=1+Delta_a`.  Reflection gives the same left gap.  On
`E_a` the exact shell cross-section is `4 pi a delta_0`, hence

\[
 M_{\boldsymbol n,R}^{\rm plat}
 \ge4\pi\delta_0a^2R^5
 \int_0^4\int_{E_a}|G|^3.
\]

At fixed time, the `q` positive real cosine modes create at most `2q`
complex branches.  Squaring Zhang Proposition 4.2 and using Hölder gives

\[
 \|G(s)\|_{L^\infty(I_a)}^2
 \le Cq^2e^{\Phi_a}h(s)^{2/3},
 \qquad
 \Phi_a=12\sqrt2q\sqrt{\Delta_a}.
\]

No frequency gap, amplitude lower bound, phase restriction, or drift bound
is used.

## Polynomial derivative and terminal rows

Erdelyi's Markov estimate, after mapping the uniformly bounded `I_a` to
`[0,1]`, gives

\[
 \|G_z(s)\|_{L^\infty(I_a)}^2
 \le C(q^7+q^3\alpha^2)e^{\Phi_a}h(s)^{2/3}.
\]

For the terminal row, reverse the last unit of heat time:

\[
 G(4-r,z)=\sum_{j,\sigma}
 c_{j,\sigma}(z)e^{\gamma_{j,\sigma}r},
 \qquad
 \gamma_{j,\sigma}=(\kappa_j/a)^2+i\sigma v\kappa_j.
\]

Every exponent has positive real part.  The Kós/Erdelyi endpoint estimate
then gives

\[
 h(4)\le64q^3H,\qquad h(4)^{2/3}\le16q^2H^{2/3}.
\]

This step is what removes the residual terminal `exp(Cq)` loss.

## Four-row energy ledger

With `mathcal E(s)=int Xi_aG^2`, the inherited exact identity is

\[
 \begin{aligned}
 v\int_0^4\zeta\int W_aG^2
 &=\zeta(4)\mathcal E(4)-\int_0^4\zeta'\mathcal E\,ds\\
 &\quad-a^{-2}\int_0^4\zeta\int\Xi_a''G^2
 +2a^{-2}\int_0^4\zeta\int\Xi_a|G_z|^2.
 \end{aligned}
\]

The terminal, cutoff, curvature, and gradient rows cost respectively

\[
 q^4,\qquad q^2,\qquad a^{-1}q^2,\qquad
 q^7+a^0q^3[q\log(q+1)]^{4/3},
\]

times the common `exp(Phi_a)H^(2/3)` envelope.  For `q>=1` they are all
absorbed by `Cq^7exp(Phi_a)H^(2/3)`.  There is no division by the drift
`v`.

## Asymptotic ledger

Since `a=pL`,

\[
 \frac{\Phi_a}{L^2}
 =O\!\left(\frac{q(L)}{L^{5/2}}\right).
\]

Under `q=o(L^(5/2))`, both this term and `7log(q)/L^2` vanish.  The
normalization cancels the raw `R^(-1/3)` payment exactly, and
`omega^(1/3)` leaves the rate `-2/11907`.

## Sharpness and claim boundary

Zhang Proposition 8.4 gives matching exponential scale, up to polynomial
factors, in the full sparse-Fourier class only for
`N>=2` and `N^(-2)<=Delta<=1`.  Its lower witness is a confluent complex
sum, not the real conjugate-paired dyadic heat-shear class used here.
Do not publish that lower result as sharpness of R0.76I.

Publish only the following hierarchy:

- **LITERATURE:** the three imported exponential-sum inequalities.
- **PROVED LOCALLY:** geometry, bilateral rescaling, derivative and terminal
  consequences, four-row reconstruction, physical powers, and asymptotic
  implication.
- **CONDITIONAL-LITERATURE:** the composite boxed R0.76I theorem.
- **FINITE COMPUTATION:** exact ledgers and source-byte certificates only.
- **OPEN:** an independent proof of Zhang Proposition 4.2, sharp polynomial
  dependence, a matching lower bound in the exact-shear class, multiple
  dyadic bands, nonconstant shear, arbitrary nonlinear packets,
  arbitrary-field E.24, Version-M extraction, fixed deletion,
  suitable-weak transfer, regularity, and singularity.

The exact shear remains `u=(0,B,F(t,x_2))`.  When `B!=0`, its constant
background has not been placed in the frozen mean-zero, inversion-paired
Version-M subclass.  Do not state an unconditional Version-M consequence.

No simulation or formal scientific figure belongs to this release.  No
novelty or priority claim is authorized.  **NOT CLAY.**

## Certificate and clean-archive boundary

The primary analytic audit and two independent mathematical lanes report
PASS with zero blockers.  Python and Ruby independently report 129/129
finite assertions.  Both reject all 129 named mutations and fail closed on
an unknown mutation.  Python output is byte-stable under
`PYTHONHASHSEED=0,1,42`.  Both implementations agree on exact arithmetic,
the ordered mutation inventory, bindings, and freeze state.

The core inventory is exactly twelve files.  A clean `git archive` of core
commit `0b73f68e...` reran the complete QA successfully.  Finite
certificates bind exact rational samples, powers, signs, tags, source
status, hashes, and claim boundaries; they are not the continuum proof and
do not validate the imported 34-page preprint.

## Reader-facing and recap requirements

Create one bilingual reader note and synchronized PDF in the established
compact, restrained, retro research style.  Preserve all theorem
quantifiers and display **CONDITIONAL-LITERATURE**, **LITERATURE**,
**PROVED LOCALLY**, **FINITE COMPUTATION**, **OPEN**, and **NOT CLAY**
prominently.

The cumulative recap must extend the prior R0.75W recap through R0.76I.  It
must distinguish:

1. R0.76E's old `exp(Cq)` / `q=o(L^2)` uniform barrier;
2. R0.76F--H's explicit-packet lower/flux/candidate-killing sequence;
3. R0.76I's literature-enabled `exp(O(q/sqrt(a)))` upper bound and
   `q=o(L^(5/2))` exact-shear window;
4. the remaining gap to nonlinear arbitrary-field extraction.

Add the twelve frozen research artifacts, source links, route and homepage
entries, exact release metadata, and tests.  Run desktop/mobile,
light/dark, Chinese/English, PDF, formula, link, and GitHub Pages checks.
Online deployment and byte verification remain solely the publication
task's responsibility.

Do not add a figure, simulation, unconditional theorem, full-class
sharpness claim for the dyadic shear subclass, later-version content, or a
second publication task.
