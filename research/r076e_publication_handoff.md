# R0.76E publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.76E-Step56`
- research label: `R0.76E`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.76D-Step55`
- cumulative recap required: `false`
- retained recap terminal release: `R0.75W-Step48`
- formal scientific figure required: `false`
- core research commit:
  `0e929c4066f2111545afa4683b363edac8440825`

This handoff authorizes only R0.76E.  Do not read or publish later material.
Do not create or reuse a second publishing, recap, reflection,
lessons-learned, usage-notes, or temporary task/system.  The sole publisher
must wait until R0.76D-Step55 has been deployed and verified, then append
R0.76E exactly once in the same FIFO task.  The cumulative recap through W
must remain byte-identical.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `1494cb7e3863ef934f87746412f2a64ef98f78deb5ce81be3cece7d5a7571ca4` | `research/r076e_linear_modal_entropy_window.md` |
| `5ce8fb3f2f2f487002b0e391db49855edb3cff72574058e26150813d69615d27` | `research/r076e_linear_modal_entropy_window_primary_audit.md` |
| `10e506fa9d250b14d9f42f6eac7c2c83cfca934a85a2da6e223cd473f21e0c12` | `research/r076e_report-source.md` |
| `9b5b0a7d88fe31d4156a7fbc8f73b52a9b5a8271437ee1be867970cec244cf47` | `scripts/r076e_linear_modal_entropy_window_fixtures.json` |
| `af6c1fd49d57945306f5f97a99f160a8fcbaec21bce887b78fe74e0bbe4d4f80` | `scripts/r076e_linear_modal_entropy_window_expected.json` |
| `57e629e0952131928e738501ee14f525daf3e2ac5fcb3b37fe02b118d7fb0f6c` | `scripts/r076e_linear_modal_entropy_window_certificate.py` |
| `e5f340e181b96a45d202ec88e5d98d71744b2ed23008e579c8c705c88fc30bdd` | `scripts/r076e_linear_modal_entropy_window_certificate_independent.rb` |
| `76859a4f6fc86652957336a096ec06c73f643cfac0e46df38e1c38bad1b9fee0` | `scripts/r076e_linear_modal_entropy_window_qa.sh` |
| `73daf5a6fe12096b29b87704a667e45c994cd2233244e6f2f8daba987b471245` | `research/r076e_linear_modal_entropy_window_certificate.json` |
| `8e3937b7b5843b49c53fbbc6b3cc0490a139b1c2ff2e469bb64758f112d11f31` | `research/r076e_linear_modal_entropy_window_certificate_report.md` |
| `bc5ed58d5a47a1c847ea626c85da49078a19ed148323c72eaf3d452b90ad3842` | `research/r076e_linear_modal_entropy_window_independent_audit.md` |
| `0afdabc3805121ef593c1c2741b12d6011821a0cc98c7b07b76306c7f24ef631` | `research/r076e_linear_modal_entropy_window_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

Fix

\[
 q\in\mathbb N,\quad q\ge1,\qquad
 1\le n_1<\cdots<n_q\le2n_1,\qquad
 n_j\in\mathbb N,\qquad
 A_j\ge0,\quad \phi_j,B\in\mathbb R,
\]

and the exact real constant-shear family

\[
 F(t,x_2)=\sum_{j=1}^q A_je^{-n_j^2t}
 \cos(n_jx_2-\phi_j-n_jBt).
\]

R0.76D proved the complete signed collar-flux estimate with loss
`exp(Cq log(q+1))`.  R0.76E reorganizes the stable heat clock and improves
that loss to `exp(Cq)`:

\[
 \boxed{
 |\mathcal T_{\boldsymbol n,R}|
 \le e^{C_*q}a^{2/3}R^{-1/3}
 \bigl(M_{\boldsymbol n,R}^{\rm plat}\bigr)^{2/3}.}
\]

The constants are independent of `q`, `R`, the frequencies, amplitudes,
phases, and `B` after the frozen profiles and sufficiently large-`L` gate
are fixed.  The factor `exp(C_*q)` is part of the estimate and must not be
suppressed.

With

\[
 p_{\boldsymbol n,R}^{\rm plat}
 =R^{-2}\omega M_{\boldsymbol n,R}^{\rm plat},
 \qquad
 \mathfrak X_{\boldsymbol n,R}
 =\frac\omega R[\mathcal T_{\boldsymbol n,R}]_+,
\]

the normalized consequence is

\[
 \boxed{
 \mathfrak X_{\boldsymbol n,R}
 \le e^{C_*q}a^{2/3}\omega^{1/3}
 \bigl(p_{\boldsymbol n,R}^{\rm plat}\bigr)^{2/3}.}
\]

This is an implication from the absolute-flux estimate, not a logical
equivalence, because the normalized quantity uses the positive part.

## Linear modal-entropy window

Every integer-valued count satisfying

\[
 q(L)=o(L^2)
\]

retains the exact frozen rate

\[
 \limsup_{L\to\infty}L^{-2}
 \log\!\left[e^{C_*q(L)}a^{2/3}\omega^{1/3}\right]
 =-\frac2{11907}.
\]

This strictly enlarges the R0.76D condition
`q(L)log(q(L)+1)=o(L^2)`.  For example, the scale
`q(L)` comparable with `L^2/log L` meets the new little-o condition but not
the old one.  The conclusion remains nonuniform in `q` and is not an
arbitrary-packet estimate.

## Delayed stable heat clock

For a complex exponential polynomial

\[
 Q(\tau)=\sum_{r=1}^Nc_re^{\mu_r\tau},
 \qquad -4\le\operatorname {Re}\mu_r\le-1,
\]

put

\[
 k(\tau)=\int_I|Q(\tau;z)|^3dz,
 \qquad K_U=\int_0^Uk(\tau)d\tau.
\]

The centered Turan--Nazarov estimate inherited from D gives, with
`m=2(N-1)`,

\[
 k(\tau)^{2/3}
 \le D_0^{2N}(1+\tau)^me^{-2\tau}K_1^{2/3}.
\]

Choose one absolute `C_0` and split at

\[
 S_N=C_0N\log(N+1),
 \qquad
 D_0^{2N}2^mS_N^{m+1}e^{-2S_N}\le1.
\]

The main note proves that one sufficiently large `C_0` works for every
`N>=1`.  Holder pays the early interval using the full `K_T`:

\[
 \int_0^{\min\{T,S_N\}}\tau k(\tau)^{2/3}d\tau
 \le4^{-1/3}S_N^{4/3}K_T^{2/3}.
\]

Only the region where the polynomial-exponential tail is decreasing uses
the centered estimate.  Therefore

\[
 \boxed{
 \int_0^T\tau k(\tau)^{2/3}d\tau
 \le C[N\log(N+1)]^{4/3}K_T^{2/3}.}
\]

The previous factorial came from controlling the entire tail by `K_1`.
R0.76E does not claim a new Turan--Nazarov theorem.

## Last-unit endpoint and carrier ledger

A half-measure Chebyshev subset of `[T-1,T]` and Turan--Nazarov give

\[
 |Q(T;z)|^3
 \le D_1^{3N}\int_{T-1}^T|Q(r;z)|^3dr.
\]

For `4<=T<=S_N`, the fixed-unit factor and `S_N/T>=1` give an `exp(CN)`
bound.  For `T>=S_N`, tail monotonicity and the stronger power `m+1` above
give the same result:

\[
 \boxed{
 k(T)^{2/3}\le e^{CN}T^{-2/3}K_T^{2/3}.}
\]

When `lambda>1`, the heat clock has `T=4lambda` and `K_T=lambda H`.
The endpoint powers cancel exactly, while the cutoff onset gives

\[
 \lambda\int_0^4\zeta(s)h(s)^{2/3}ds
 \le C[q\log(q+1)]^{4/3}
 \lambda^{-1/3}H^{2/3}.
\]

No positive carrier power remains.  The bounded branch `lambda<=1` stays on
the original fixed clock.

## Complete-real energy and scaling

The cutoff is explicitly `zeta(s)=eta_R(R^2s)`, with
`zeta(0)=0`, `|zeta'|<=C_eta`, and `zeta(s)<=C_eta s`.  The complete-real
identity is formed before absolute values.  The spatial derivative row gives

\[
 a^{-2}(\alpha+q)^2
 \le C\left(\lambda+\frac{q^2}{a^2}\right).
\]

The terminal estimate, weighted onset, and Holder pay all four energy rows.
The factors `D^(4q)`, `exp(Cq)`, `q^2`, and
`[q log(q+1)]^(4/3)` are absorbed into `exp(C_*q)`.

The exact physical flux and mass prefactors are `a^2R^3v/2` and at least
`4pi delta_0a^2R^5H`.  Eliminating `H` yields
`a^(2/3)R^(-1/3)M^(2/3)`; normalization cancels `R` and leaves the frozen
rate `-2/11907`.

## Source and claim boundary

The proof imports the same two approximation-theory inputs as R0.76D:

1. Nazarov's positive-measure Turan--Nazarov inequality, with the
   Friedland--Yomdin restatement; and
2. Erdelyi's point derivative inequality for complex pure-imaginary sums.

The delayed split, last-unit endpoint, carrier accounting, complete-real
energy payment, physical conversion, and growing-window corollary are local
deductions.  Adjacent pointwise Remez/Nikolskii estimates were checked but
not imported because their exponent or endpoint hypotheses do not match the
complex past-only endpoint used here.  The bounded search is not evidence of
literature completeness, novelty, priority, or sharpness.

R0.75R remains compatible.  It concerns an arbitrary packet with an
exponential-scale mode count and a different short clock, far outside
`q=o(L^2)`.  R0.76E stays inside one exact constant-shear dyadic family.

The result does not apply to a Fourier projection of a larger velocity.
Arbitrary packets, nonconstant or vertically dependent shear,
arbitrary-field E.24, complete Version-M extraction, fixed deletion,
suitable-weak transfer, regularity, and singularity remain open.  When
`B!=0`, the constant background has not been shown to belong to the frozen
mean-zero, inversion-paired Version-M subclass.  **NOT CLAY.**

## Proof and certificate boundary

The independent counterexample-first audit and primary audit both report
PASS with zero mathematical and release blockers.  The audit corrected 18
TeX escapes, made the flux and normalization definitions self-contained,
replaced a false equivalence by implication, defined `K_U` and `zeta`, and
expanded the uniform-`C_0` argument before the core was frozen.

The exact fixture has `q=3`, `N=6`, `m=10`, `S=96`, `lambda=4`, `T=16`,
gradient coefficient `257/64`, weighted lambda exponent `-1/3`, endpoint
exponent zero, and frozen rate `-2/11907`.  With sample `D_0=2`, the strict
integer comparison `e>2` and `96<2^7` put the sample tail below `2^(-93)`.
This finite sample checks only the exponent ledger.

Python and Ruby each report 135/135 assertions, identical 6/6 exact
sections, rejection of all 135 named mutations, fail-closed unknown
mutations, and regeneration stability.  Python is byte-stable under
`PYTHONHASHSEED=0,1,42`.  The main note has E.1--E.34, 38/38 display pairs,
and four intentional unnumbered displays.  The core inventory is exactly
twelve files, and a clean archive reran the complete QA with a byte-identical
QA report.

These computations bind finite arithmetic, structure, source bytes, and
claim boundaries.  They are not proof of Turan--Nazarov, Erdelyi, or the
analytic flux theorem.

## Recap and figure boundary

R0.75W remains the terminal milestone recap.  R0.76E is an ordinary analytic
note release.  Do not update the cumulative recap.  Preserve its HTML and
PDF byte-for-byte and label the terminal release exactly as
`R0.75W-Step48`.

No simulation, DNS result, formal scientific figure, or decorative plot is
claimed or required for R0.76E.

## Publication and deployment QA

Publish one bilingual R0.76E research page and synchronized downloadable
PDF.  Expose all twelve frozen research, audit, source, certificate, and QA
artifacts.  Update the homepage, latest-research count, navigation, research
and literature reviews, version ledger, global notes index, English
translation, and formal archive through R0.76E while keeping the
latest-recap endpoint at R0.75W.

Run structural, equation, internal-link, asset, recap-preservation, and
forbidden-future-version tests; render desktop and mobile views; verify no
overflow or raw TeX leakage.  Commit and push only R0.76E, wait for GitHub
Pages to succeed, and compare every declared online object byte-for-byte
with the release commit.  A push or green workflow alone is not deployment
proof.

Do not add a figure, simulation, arbitrary-packet claim, unconditional
Version-M claim, regularity claim, recap change, or second task.  The release
is complete only when R0.76E-Step56 is deployed and verified online, after D
and before any later release.
