# R0.75X publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.75X-Step49`
- research label: `R0.75X`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75W-Step48`
- cumulative recap required: `false`
- retained recap terminal release: `R0.75W-Step48`
- formal scientific figure required: `false`
- core research commit:
  `a97e197521b4efc0e3450f34cda5e646a2560d57`

This handoff authorizes only R0.75X.  Do not read or publish R0.75Y or later
material.  Do not create or reuse a second publishing, recap, reflection,
lessons-learned, usage-notes, or temporary task/system.  The sole publisher
must wait until R0.75W-Step48 and its milestone recap have been deployed and
verified, then append X exactly once in the same FIFO task.  The cumulative
recap through W must remain byte-identical.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `8e0c412528578c15d807b33b64f0996e62a2dabe2ebd58fa297f67c093929763` | `research/r075x_fixed_finite_mode_low_carrier_payment.md` |
| `8fffbf0c8ad50d5765c734f8e5627ce0dbe0d6b2aad4bcb26aa5c298f6143b2c` | `research/r075x_fixed_finite_mode_low_carrier_payment_primary_audit.md` |
| `8fa756c7efe2660dbc5eeb51e2a11d10dce58f36f4c0d0f757000be1447b7f34` | `research/r075x_report-source.md` |
| `de231e977d9a2551222f0a4f0a8ebcb65490f76574bc4fa494db480e2b61a0e9` | `scripts/r075x_fixed_finite_mode_low_carrier_payment_fixtures.json` |
| `879ff3458050e712048654eb91623a00e5436a22f12c6b814fb137aa8af96311` | `scripts/r075x_fixed_finite_mode_low_carrier_payment_expected.json` |
| `926dbcd704645d61392349437b10049c33b7ad8d77703e462ac3c784510190b4` | `scripts/r075x_fixed_finite_mode_low_carrier_payment_certificate.py` |
| `521d2026b6f27c466087b51663f7d3ca46bf9e84c3f51378fc403e05833b5ca1` | `scripts/r075x_fixed_finite_mode_low_carrier_payment_certificate_independent.rb` |
| `a94b5c96e600cdd9ea5c9ad8975bad5003058c067de079c495d27df7fcab7d7f` | `scripts/r075x_fixed_finite_mode_low_carrier_payment_qa.sh` |
| `717ce6ba1dcf4db39015db85c450bb1e2b7b31ff89e6b42ffb2bc30f31e3af05` | `research/r075x_fixed_finite_mode_low_carrier_payment_certificate.json` |
| `8725b6d6db67640fe20f1708d0942d994b174eaab0527828a0e0653aeb1c3701` | `research/r075x_fixed_finite_mode_low_carrier_payment_certificate_report.md` |
| `a1075d0ef321805a5d5d77be465820c85bd4ef820545531d983bab93094debf1` | `research/r075x_fixed_finite_mode_low_carrier_payment_independent_audit.md` |
| `a35de008fb5195331153ed8fddfc5ba1bd064d19e423f2309bf44685cc05f183` | `research/r075x_fixed_finite_mode_low_carrier_payment_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

Fix `q>=1` and let

\[
 1\le n_1<n_2<\cdots<n_q\le2n_1.
\]

For the exact diffusive shear

\[
 F(t,x_2)=\sum_{j=1}^q A_je^{-n_j^2t}
 \cos(n_jx_2-\phi_j-n_jBt),
 \qquad A_j\ge0,\quad B\in\mathbb R,
\]

assume the low-carrier condition `n_1aR<C_0`.  Then, for every fixed
`q`,

\[
 \boxed{
 |\mathcal T_{\boldsymbol n,R}|
 \le C_q a^{2/3}R^{-1/3}
 \bigl(M_{\boldsymbol n,R}^{\rm plat}\bigr)^{2/3}.}
\]

The constant depends on `q`, `C_0`, and the frozen profiles, but not on
`R`, the frequencies, their gaps, amplitudes, phases, or `B`.  With the
frozen normalization,

\[
 \boxed{
 \mathfrak X_{\boldsymbol n,R}
 \le C_qa^{2/3}\omega^{1/3}
 \bigl(p_{\boldsymbol n,R}^{\rm plat}\bigr)^{2/3},
 \qquad
 \lim_{L\to\infty}\frac1{L^2}
 \log(a^{2/3}\omega^{1/3})=-\frac2{11907}.}
\]

For fixed `q`, `C_q` has no `L^2`-scale logarithmic cost.  No uniform
estimate as `q` grows is claimed.

## Proof and certificate boundary

The analytic proof has six pieces:

1. scale to `G_s+vG_z-a^(-2)G_zz=0`, with all
   `0<alpha_j<=2C_0`;
2. prove a uniform fixed-`q` local observation estimate for
   `prod_j(partial_z^2+alpha_j^2)g=0` by compactness of its `2q`-state
   companion matrices, including repeated roots and the degree-`2q-1`
   polynomial limit;
3. apply the Turan--Nazarov measurable-set inequality to the at-most-`2q`
   temporal exponential terms, producing a right-endpoint `L^3` trace
   independent of imaginary frequencies and exponent gaps;
4. use the same compact radial primitive and exact local energy identity as
   W, without dividing by shear speed, amplitude, frequency, or gap;
5. pay the endpoint, cutoff, heat, and localized-gradient rows together by
   `C_qH^(2/3)`;
6. use the exact plateau mass
   `M_plat>=4*pi*delta_0*a^2*R^5*H` to recover the physical and normalized
   estimates.

The main proof, primary mathematical audit, and final independent reread
report PASS with zero mathematical and release blockers.  The frozen finite
suite reports Python 18/18, Ruby 19/19, rejection of all 90 named mutation
families by both implementations, fail-closed unknown mutations, byte
stability under `PYTHONHASHSEED=0,1,42`, regeneration stability, 36/36
equation tags and displays, and exact six-dimensional companion,
transport-identity, and scale fixtures.  Finite checks bind algebra,
structure, and source bytes; they are not represented as proof of the
continuum compactness or Turan--Nazarov lemmas.

The bounded primary-source report identifies Nazarov's original record and
the Friedland--Yomdin primary restatement.  No completeness, novelty, or
priority claim is made.

## Claim boundary

R0.75X proves only the low-carrier estimate for every fixed finite real
harmonic family in one dyadic band.  It does not give quantitative control
of the spatial observation constant when `q=q(L)`, prove the high-carrier
sector for three or more modes, or override the growing-packet outer-cap
obstruction of R0.75R.

The exact field embeds in the smooth unforced shear `u=(0,B,F(t,x_2))`,
but the nonzero constant background has not been shown to belong to the
frozen mean-zero, inversion-paired Version-M subclass.  Any Version-M
consequence remains conditional on the same measurement row, weight,
realized-subclass, actual-component, and ledger-alignment hypotheses.

Arbitrary packets, inter-packet aggregation, nonconstant or vertically
dependent shear, projection from a larger velocity, arbitrary-field E.24,
complete Version-M extraction, fixed deletion, suitable-weak transfer,
regularity, and singularity remain open.  **NOT CLAY.**

## Recap and figure boundary

R0.75W already supplied the milestone recap closing the full-frequency
two-harmonic branch.  X is the first fixed-finite-mode low-carrier extension,
but the high-carrier `q>=3` half and all growing-`q` control remain open.
Do not update the cumulative recap.  Preserve the W recap HTML and PDF
byte-for-byte and label its terminal release exactly as `R0.75W-Step48`.

The proof is analytic.  Do not create a formal scientific figure,
simulation, DNS result, or decorative plot for X.

## Publication and deployment QA

Publish one bilingual R0.75X research page and synchronized downloadable
PDF.  Expose all twelve frozen source, audit, certificate, and QA artifacts.
Update the homepage, latest-research count, navigation, research and
literature reviews, version ledger, global notes index, English translation,
and formal archive through X while keeping the latest-recap endpoint at W.

Run structural, equation, internal-link, asset, recap-preservation, and
forbidden-future-version tests; render desktop and mobile views; verify there
is no overflow or raw TeX leakage.  Commit and push only X, wait for the
GitHub Pages workflow to succeed, and compare every declared online object
byte-for-byte with the release commit.  A successful push or workflow alone
is not deployment proof.

Do not add a figure, simulation, arbitrary-packet claim, regularity claim,
recap change, or second task.  The release is complete only when
R0.75X-Step49 is deployed and verified online, after W and before Y.
