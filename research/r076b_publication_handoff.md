# R0.76B publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.76B-Step53`
- research label: `R0.76B`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.76A-Step52`
- cumulative recap required: `false`
- retained recap terminal release: `R0.75W-Step48`
- formal scientific figure required: `false`
- core research commit:
  `b31c53a5e48e2de56088ac2715a95000a64e2c9a`

This handoff authorizes only R0.76B.  Do not read or publish later material.
Do not create or reuse a second publishing, recap, reflection,
lessons-learned, usage-notes, or temporary task/system.  The sole publisher
must wait until R0.76A-Step52 has been deployed and verified, then append
R0.76B exactly once in the same FIFO task.  The cumulative recap through W
must remain byte-identical.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `a8a4cc853ec1029cb52afee724a4a783da156bd57de5399c58a7f42e2ab0306d` | `research/r076b_moderate_carrier_fixed_mode_flux_payment.md` |
| `0a6314c454021da284bbf157de36d6c2bd1683d600a21c8394f723acc26aa447` | `research/r076b_moderate_carrier_fixed_mode_flux_payment_primary_audit.md` |
| `362fcf898a533efaf4072c876dba09f4231c131ad1c48d48efc92c52215428fc` | `research/r076b_report-source.md` |
| `1f9b3df9cb8ff3f9d22250ce425b837d40268829bf18cb3e12b3f7d2dca64bf2` | `scripts/r076b_moderate_carrier_fixed_mode_flux_payment_fixtures.json` |
| `4533edf290e07f1fddc5df1b9ef1655a5623f4a3714e840b1c402cdf3b8db3f1` | `scripts/r076b_moderate_carrier_fixed_mode_flux_payment_expected.json` |
| `b4ec0ba8fbbe9033dcec3254a1acc3a4f7e662fe320c4697f253f575aa98863a` | `scripts/r076b_moderate_carrier_fixed_mode_flux_payment_certificate.py` |
| `0b53934fc132eda0c51a5885d8b50089b74897aeaff1373e1033bc825c43e849` | `scripts/r076b_moderate_carrier_fixed_mode_flux_payment_certificate_independent.rb` |
| `dd4d802ce353c9698323cc2ad600df35794cce4796cf9457a63786165be47756` | `scripts/r076b_moderate_carrier_fixed_mode_flux_payment_qa.sh` |
| `d825624473f176c054134a75a47cb63fee65f7fe3bfe946ae505522a9c3c053e` | `research/r076b_moderate_carrier_fixed_mode_flux_payment_certificate.json` |
| `5ae840453141f3059b94459996f7aaf808766fe3367ea433251343de128f938e` | `research/r076b_moderate_carrier_fixed_mode_flux_payment_certificate_report.md` |
| `1962313e8898dd6cdbafa9f1b543712d3660c25521c039e5311b21629bb1f6bf` | `research/r076b_moderate_carrier_fixed_mode_flux_payment_independent_audit.md` |
| `7ec49c58e8eb209af2e836155b0126f8257e61b89f8742d04331ae31dc628f6d` | `research/r076b_moderate_carrier_fixed_mode_flux_payment_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

Fix an integer `q>=1`, with integer frequencies and real phases satisfying

\[
 n_1,\ldots,n_q\in\mathbb N,
 \qquad 1\le n_1<\cdots<n_q\le2n_1,
 \qquad \phi_j\in\mathbb R,
\]

and take the exact diffusive constant-shear family

\[
 F(t,x_2)=\sum_{j=1}^q A_j e^{-n_j^2t}
 \cos(n_jx_2-\phi_j-n_jBt),
 \qquad A_j\ge0,\quad B\in\mathbb R.
\]

For every fixed `q` and all sufficiently large frozen `L`, R0.76B proves for
the frozen complete-clock collar flux and plateau cubic mass that the
inverse-radius condition

\[
 n_1R\le1
\]

implies

\[
 \boxed{
 |\mathcal T_{\boldsymbol n,R}|
 \le C_q a^{2/3}R^{-1/3}
 \bigl(M_{\boldsymbol n,R}^{\rm plat}\bigr)^{2/3}.}
\]

The constant depends on fixed `q` and the frozen profiles, but not on `R`,
the frequencies, amplitudes, phases, or constant speed `B`.

## High-carrier observation mechanism

With

\[
 \kappa_j=n_jaR,\qquad \alpha=\kappa_1,\qquad v=BR/a,
\]

R0.75X pays `alpha<8q`.  The new branch is
`8q<=alpha<=a`.  After `x=alpha z`, every spatial exponent lies in the
compact set `+-i[1,2]`.  A half-measure Chebyshev subset of `alpha I` and
Turan--Nazarov on `alpha J^+` have length ratio at most eight.  A compact
companion-ODE argument on unit windows then gives

\[
 \|G(s)\|_{L^\infty(J)}
 +\alpha^{-1}\|G_z(s)\|_{L^\infty(J)}
 \le C_q\left(\int_I|G(s,z)|^3dz\right)^{1/3}.
\]

At each fixed `z`, `G` is a temporal exponential polynomial with at most
`2q` terms and exponents

\[
 -\kappa_j^2/a^2\pm i\kappa_jv.
\]

Since `kappa_j<=2alpha<=2a`, the real parts lie in `[-4,0]`.  A second
Turan--Nazarov application gives the carrier-, speed-, collision-, and
gap-independent terminal trace `h(4)<=C_qH`.

## Complete-real-field energy payment

The proof does not isolate the analytic density or estimate a standalone
carrier block.  The complete real field satisfies

\[
 (G^2)_s+v(G^2)_z-a^{-2}(G^2)_{zz}
 =-2a^{-2}|G_z|^2.
\]

For the nonnegative frozen primitive `Xi_a`, `W_a=Xi_a'`, and
`E=int Xi_aG^2`, the exact full-clock identity is

\[
 \begin{aligned}
 v\int_0^4\zeta\int W_aG^2
 &=\zeta(4)E(4)-\int_0^4\zeta'E\,ds\\
 &\quad-a^{-2}\int_0^4\zeta\int\Xi_a''G^2
 +2a^{-2}\int_0^4\zeta\int\Xi_a|G_z|^2.
 \end{aligned}
\]

The frozen onset `zeta(0)=0` removes the initial endpoint.  The spatial
observation pays the gradient row with the exact factor

\[
 a^{-2}\alpha^2=(\alpha/a)^2\le1.
\]

Thus self terms, differences, sums, and all cross terms in `G^2` are
reassembled before absolute values.  No spectral separation and no
localized-current sign are used.

## Scale normalization and significance

The exact cross section and plateau fibre give

\[
 \mathcal T_{\boldsymbol n,R}
 =\frac{a^2R^3}{2}v\int_0^4\zeta\int W_aG^2,
 \qquad
 M_{\boldsymbol n,R}^{\rm plat}
 \ge4\pi\delta_0a^2R^5H.
\]

Therefore the dimensionless bound is

\[
 \boxed{
 \mathfrak X_{\boldsymbol n,R}
 \le C_q a^{2/3}\omega^{1/3}
 \bigl(p_{\boldsymbol n,R}^{\rm plat}\bigr)^{2/3},
 \qquad
 \lim_{L\to\infty}L^{-2}\log(a^{2/3}\omega^{1/3})
 =-\frac2{11907}.}
\]

For every fixed `q`, this closes the complete exact-shear carrier range
`n_1<=R^{-1}` and repairs the R0.76A localized-current obstruction within
that range by retaining the full real square.

## Exact boundary

The theorem is not uniform as `q` grows.  The ultra-high sector `n_1R>1`,
arbitrary growing packets, nonconstant or vertically dependent shear,
projection from a larger velocity, arbitrary-field E.24, complete Version-M
extraction, fixed deletion, suitable-weak transfer, regularity, and
singularity remain open.  The exact shear has a nonzero constant background
that has not been placed in the frozen mean-zero Version-M subclass.  Any
Version-M consequence is conditional on the same velocity component and the
same measurement row.  The bounded source screen establishes neither
completeness, novelty, nor priority.  **NOT CLAY.**

## Proof and certificate boundary

The continuum proof consists of two Turan--Nazarov applications, a local
compact companion-ODE derivative estimate, the complete-real-square energy
identity, and exact physical scaling.  The primary and adversarial audits
report PASS with zero mathematical and release blockers after a required
quantifier repair explicitly added `n_j in N` and `phi_j in R`.

The finite suite independently recomputes the exact `q=3`, `alpha=a`,
`n_1R=1` endpoint family, window ratios, temporal real-part bounds, pointwise
scaled PDE, polynomial energy identity, and scale ledger.  It reports Python
15/15, Ruby 15/15, rejection of all 123 named mutations by both
implementations, fail-closed unknown mutations, byte stability under
`PYTHONHASHSEED=0,1,42`, regeneration stability, and 41/41 equation tags and
displays.  A clean archive of the repaired core commit reran the complete QA
with PASS.  These finite checks bind arithmetic, structure, source bytes, and
claim boundaries; they are not represented as proof of the continuum
observation lemmas.

## Recap and figure boundary

R0.75W remains the terminal milestone recap.  R0.76B is a fixed-dimensional
exact-shear closure, not the arbitrary-field or Version-M closure.  Do not
update the cumulative recap.  Preserve the W recap HTML and PDF byte-for-byte
and label its terminal release exactly as `R0.75W-Step48`.

The result is analytic.  Do not create a formal scientific figure,
simulation, DNS result, or decorative plot for R0.76B.

## Publication and deployment QA

Publish one bilingual R0.76B research page and synchronized downloadable
PDF.  Expose all twelve frozen source, audit, certificate, and QA artifacts.
Update the homepage, latest-research count, navigation, research and
literature reviews, version ledger, global notes index, English translation,
and formal archive through R0.76B while keeping the latest-recap endpoint at
R0.75W.

Run structural, equation, internal-link, asset, recap-preservation, and
forbidden-future-version tests; render desktop and mobile views; verify there
is no overflow or raw TeX leakage.  Commit and push only R0.76B, wait for the
GitHub Pages workflow to succeed, and compare every declared online object
byte-for-byte with the release commit.  A successful push or workflow alone
is not deployment proof.

Do not add a figure, simulation, arbitrary-packet claim, unconditional
Version-M claim, regularity claim, recap change, or second task.  The release
is complete only when R0.76B-Step53 is deployed and verified online, after A
and before any later release.
