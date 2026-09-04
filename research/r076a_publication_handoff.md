# R0.76A publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.76A-Step52`
- research label: `R0.76A`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75Z-Step51`
- cumulative recap required: `false`
- retained recap terminal release: `R0.75W-Step48`
- formal scientific figure required: `false`
- core research commit:
  `1f15e31b56c37a6a3941a1c4961321b7b1745e6c`

This handoff authorizes only R0.76A.  Do not read or publish later material.
Do not create or reuse a second publishing, recap, reflection,
lessons-learned, usage-notes, or temporary task/system.  The sole publisher
must wait until R0.75Z-Step51 has been deployed and verified, then append
R0.76A exactly once in the same FIFO task.  The cumulative recap through W
must remain byte-identical.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `d23532f84702be1630daa0b8d56d02242571dd8a1f8024c59a7f71bec30f26eb` | `research/r076a_complete_clock_localized_current_sign_obstruction.md` |
| `0f7f56d32025f4cd86218f54dfcf5155675f316d2afecdd0007b13ad70240a8d` | `research/r076a_complete_clock_localized_current_sign_obstruction_primary_audit.md` |
| `0bbf94774c7d76e623c025a731e0238eca39080c4720a039f080afb038ecad8b` | `research/r076a_report-source.md` |
| `f3644b2a7a641bc92c6c1936f1c05cbed88a6a3e94e25d650c7258ce07b30a31` | `scripts/r076a_complete_clock_localized_current_sign_obstruction_fixtures.json` |
| `32d0f99d07d842bf6c9161698249c186c4d23d2f1f33e7f8bd7fc18804887697` | `scripts/r076a_complete_clock_localized_current_sign_obstruction_expected.json` |
| `7dfff7dfb26ccfb9399c0a9cc32a914d5e1d94f3a81ed172f4ec245343d43ab5` | `scripts/r076a_complete_clock_localized_current_sign_obstruction_certificate.py` |
| `5633861e614cba477f59e8ca4d6f52bc9c29e561178ae07117af53d83cc13366` | `scripts/r076a_complete_clock_localized_current_sign_obstruction_certificate_independent.rb` |
| `d34a0275f6b321c84db14fd47219701ef5a3caa53572b941f37343c88d680539` | `scripts/r076a_complete_clock_localized_current_sign_obstruction_qa.sh` |
| `cd09488885f0e31d95f94c7f46bf0c80b1ad476a438a3fa081d3ec83d4c2949c` | `research/r076a_complete_clock_localized_current_sign_obstruction_certificate.json` |
| `665e69226763e2df99615714829387309a3f66a1ec1e35b19f4af35d005c0d12` | `research/r076a_complete_clock_localized_current_sign_obstruction_certificate_report.md` |
| `cd5608262b4f9c35f30afec9af2a108621f4f89cf8f4a69d973e1e07b6ee670d` | `research/r076a_complete_clock_localized_current_sign_obstruction_independent_audit.md` |
| `fb8681c63bfa83bc26fadeb867c0c25c6167b28789bda9480e061dcdf0409a82` | `research/r076a_complete_clock_localized_current_sign_obstruction_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

Let the frozen radial profile satisfy

\[
 0\le\vartheta\le1,
 \qquad \vartheta=1\ \hbox{on }[-\delta_0,\delta_0],
 \qquad \operatorname {supp}\vartheta\subset(-\delta,\delta),
 \qquad 0<\delta_0<\delta,
\]

and set

\[
 W_a(z)=-2\pi az\vartheta(a(|z|-1)),
 \qquad
 \Xi_a(z)=\int_{-\infty}^{z}W_a(r)\,dr.
\]

For `a>=max(24,2 delta)`, the primitive is nonnegative and nonzero, with

\[
 \operatorname {supp}\Xi_a\subset[-3/2,3/2],
 \qquad
 \int_{\mathbb R}\Xi_a(z)\,dz\ge2\pi\delta_0.
\]

Fix `q=2`, `0<ell=aR<=1/11`, and choose

\[
 N=\left\lceil\frac{16}{\ell}\right\rceil,
 \qquad \alpha=N\ell,
 \qquad \beta=\ell.
\]

Then `16<=alpha<17`, while the adjacent scaled gap is `beta<16`; hence
`(N,N+1)` is an actual unresolved high-carrier cluster.  On the complete
scaled clock `0<=s<=4`, with scaled speed one, its exact envelope is

\[
 Z(s,z)=2-r(s)e^{i\beta(z-s)},
 \qquad
 r(s)=e^{-\mu s},
 \qquad
 \mu=\frac{2\alpha\beta+\beta^2}{a^2}.
\]

## Uniform localized sign obstruction

For

\[
 J=\operatorname {Im}(\overline Z\,\partial_zZ)
   =\beta r\bigl(r-2\cos(\beta(z-s))\bigr),
\]

the complete-clock damping and phase bounds give, everywhere on the support
of `Xi_a`,

\[
 \boxed{J\le-\frac9{16}\beta<0},
 \qquad
 \boxed{|\partial_zZ|^2+2\alpha J\le-\alpha\beta<0}.
\]

Therefore every nonnegative cutoff `zeta` with positive integral on `[0,4]`
satisfies

\[
 \int_0^4\!\zeta(s)e^{-2\alpha^2s/a^2}
 \int_{\mathbb R}\!\Xi_a(z)J(s,z)\,dzds<0.
\]

The same strict sign holds when `J` is replaced by
`|partial_z Z|^2+2 alpha J`.  This is a localized, full-clock statement,
not merely a negative value at one point.

There is no contradiction with

\[
 |i\alpha Z+\partial_zZ|^2
 =\alpha^2|Z|^2+|\partial_zZ|^2+2\alpha J\ge0,
\]

because the positive carrier-density row was omitted from the negative
correction.  Any joint multiplier route must retain that row.

## Exact boundary and significance

R0.76A rules out only the proof move that discards the localized carrier
current, or its correction row, by claiming nonnegativity from one-sided
offset spectrum.  It does not rule out a perturbative estimate, a localized
boundary-error estimate, a nonlocal signed estimate, or a joint
density/carrier cancellation.  Indeed, for this fixed-amplitude family the
scaled current row is at most `C ell/a^2=C R/a`.

This is not a counterexample to the two-mode collar-flux estimate.  R0.75W
already pays that exact `q=2` class.  A general localized current estimate
for arbitrary cluster coefficients, full Z-sector payment, cross-cluster
aggregation, growing packets, arbitrary-field E.24, complete Version-M
extraction, fixed deletion, suitable-weak transfer, regularity, and
singularity remain open.  The bounded source screen does not establish
completeness, novelty, or priority.  **NOT CLAY.**

## Proof and certificate boundary

The continuum proof consists of the primitive sign and mass argument, exact
integer-frequency classification, exact carrier-envelope differentiation,
uniform damping and phase bounds, and multiplication by nonnegative
spacetime weights.  The primary mathematical audit reports PASS with zero
mathematical and release blockers.

The finite suite independently recomputes exact rational geometry, scaling,
damping, phase, point current, correction density, PDE coefficient, and
full-gradient values.  It reports Python 15/15, Ruby 15/15, rejection of all
86 named mutations by both implementations, fail-closed unknown mutations,
byte stability under `PYTHONHASHSEED=0,1,42`, regeneration stability, and
34/34 equation tags and displays.  A clean archive of the core commit reran
the complete QA with PASS.  These finite checks bind arithmetic, structure,
source bytes, and claim boundaries; they are not represented as proof of the
continuum identities.

## Recap and figure boundary

R0.75W remains the terminal milestone recap.  R0.76A is a route-reduction
note, not a full cluster-payment theorem or a milestone closure.  Do not
update the cumulative recap.  Preserve the W recap HTML and PDF byte-for-byte
and label its terminal release exactly as `R0.75W-Step48`.

The result is analytic.  Do not create a formal scientific figure,
simulation, DNS result, or decorative plot for R0.76A.

## Publication and deployment QA

Publish one bilingual R0.76A research page and synchronized downloadable
PDF.  Expose all twelve frozen source, audit, certificate, and QA artifacts.
Update the homepage, latest-research count, navigation, research and
literature reviews, version ledger, global notes index, English translation,
and formal archive through R0.76A while keeping the latest-recap endpoint at
R0.75W.

Run structural, equation, internal-link, asset, recap-preservation, and
forbidden-future-version tests; render desktop and mobile views; verify there
is no overflow or raw TeX leakage.  Commit and push only R0.76A, wait for the
GitHub Pages workflow to succeed, and compare every declared online object
byte-for-byte with the release commit.  A successful push or workflow alone
is not deployment proof.

Do not add a figure, simulation, full-cluster-payment claim, regularity
claim, recap change, or second task.  The release is complete only when
R0.76A-Step52 is deployed and verified online, after Z and before any later
release.
