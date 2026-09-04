# R0.75Y publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.75Y-Step50`
- research label: `R0.75Y`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75X-Step49`
- cumulative recap required: `false`
- retained recap terminal release: `R0.75W-Step48`
- formal scientific figure required: `false`
- core research commit:
  `cb150f97a6c2595066360c0d4c6aca3c4062bdbe`

This handoff authorizes only R0.75Y.  Do not read or publish R0.75Z or later
material.  Do not create or reuse a second publishing, recap, reflection,
lessons-learned, usage-notes, or temporary task/system.  The sole publisher
must wait until R0.75X-Step49 has been deployed and verified, then append Y
exactly once in the same FIFO task.  The cumulative recap through W must
remain byte-identical.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `74790f910b596c86b204291d997ef723cabbc85d14a89e3fe900814fcd88b0a6` | `research/r075y_strongly_separated_multimode_flux_payment.md` |
| `f7e1feedd1fa359877554eff4fa20c470f727ae7743c990136525ad22d6cdf3b` | `research/r075y_strongly_separated_multimode_flux_payment_primary_audit.md` |
| `e6d6b1ed2830b46fc901a9ab09ef368f258f13dfc8c0961076baedd5b46e1589` | `research/r075y_report-source.md` |
| `45448bf75c867b3f9654db79c77ae52b9bd35d7e781b240f564a9d871faab32b` | `scripts/r075y_strongly_separated_multimode_flux_payment_fixtures.json` |
| `324e92dd32d6e1ca76b22c47a201206e1c924e1100b92de1c8429ffd17ac25d3` | `scripts/r075y_strongly_separated_multimode_flux_payment_expected.json` |
| `126e97f7d248c7d5516b927816fed3cb3269b59fd2d0def3ec410d4502e7d078` | `scripts/r075y_strongly_separated_multimode_flux_payment_certificate.py` |
| `69c1dfdd9149fc89a0c14407a9373f03e418cfd0b3c5b2fda1d9a96261141e70` | `scripts/r075y_strongly_separated_multimode_flux_payment_certificate_independent.rb` |
| `dc73c406ac40d6b64f7f9164cf0d4cf494bbb3eddc31ff5f69a662da00316517` | `scripts/r075y_strongly_separated_multimode_flux_payment_qa.sh` |
| `2c74a9bf2bd9b1f24dd66fdc330bd4dd814d63ec1bce36e7efa1e337cfa4fdfe` | `research/r075y_strongly_separated_multimode_flux_payment_certificate.json` |
| `cd3b1bf9aff7b326c92a1e40a0f3ae0fc363e734be7d859e6a7d6c62fae7a0a7` | `research/r075y_strongly_separated_multimode_flux_payment_certificate_report.md` |
| `e45e30a34253905b24acafdf18b9dfcf3d6ffd6163cd38996a1c4991335c8d21` | `research/r075y_strongly_separated_multimode_flux_payment_independent_audit.md` |
| `f2a49eafe9317aba8bdb582b4f0e0852e8cb7603fb8a415ec3df78ed5be5e67a` | `research/r075y_strongly_separated_multimode_flux_payment_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

Let

\[
 1\le n_1<\cdots<n_q\le2n_1,\qquad \ell=aR,
\]

and define the minimum signed-spectrum gap by

\[
 \delta_{\boldsymbol n}
 =\min\!\left(
 \{2n_1\}\cup\{n_j-n_i:1\le i<j\le q\}
 \right).
\]

For the exact diffusive real shear

\[
 F(t,x_2)=\sum_{j=1}^q A_je^{-n_j^2t}
 \cos(n_jx_2-\phi_j-n_jBt),
\]

assume the strong separation condition

\[
 \ell\delta_{\boldsymbol n}\ge8q.
\]

Then the complete signed collar flux satisfies

\[
 \boxed{
 |\mathcal T_{\boldsymbol n,R}|
 \le Cq^2a^{2/3}R^{-1/3}
 \bigl(M_{\boldsymbol n,R}^{\rm plat}\bigr)^{2/3}.}
\]

The constant `C` depends only on the frozen radial profile, plateau width,
and time cutoff.  All mode-count dependence is the displayed `q^2`.
After frozen normalization,

\[
 \boxed{
 \mathfrak X_{\boldsymbol n,R}
 \le Cq^2a^{2/3}\omega^{1/3}
 \bigl(p_{\boldsymbol n,R}^{\rm plat}\bigr)^{2/3}.}
\]

For fixed `q`, and more generally when `\log q=o(L^2)` while the strong
separation condition continues to hold, the exact `L^2`-scale coefficient
is `-2/11907`.  The growing-`q` statement concerns an increasingly sparse
class: for `q>=2` the assumptions force
`n_1aR>=8q(q-1)`.

## Proof and certificate boundary

The proof has four quantitative pieces:

1. expanding the cosine sum into the `2q` signed frequencies
   `\{\pm n_j\}` and retaining the exact off-diagonal Gram factor
   `2/|\lambda-\mu|`;
2. using `aR\,\delta_{\boldsymbol n}\ge8q` to leave more than one half of
   the diagonal Gram mass, hence
   `int_(I_ell)|F|^3>=ell S(t)^3/8`;
3. proving a phase-free complete-clock lemma by a slow/fast oscillation
   split and one time integration by parts, with the onset
   `eta_R(0)=0` and physical factor `R^(-4/3)/r` retained;
4. expanding the flux into exactly
   `q+2 binom(q,2)=q^2` self, difference, and sum rows, applying
   `|J_(r,R)|/r<=Ca^2R^3` to each, and using the exact plateau fibre mass
   `M_plat>=(pi delta_0/2)a^2R^3 int S^3`.

The continuum proof and primary audit report PASS with zero mathematical
and release blockers.  The finite suite reports Python 17/17, Ruby 18/18,
rejection of all 85 named mutation families by both implementations,
fail-closed unknown mutations, byte stability under
`PYTHONHASHSEED=0,1,42`, regeneration stability, 39/39 equation tags and
displays, and exact `q=3` Gram, row-count, and scale fixtures.  Finite checks
bind algebra, structure, and source bytes; they are not represented as proof
of the continuum Gram or complete-clock lemmas.

The bounded source report treats separated-frequency `L^2` observability as
classical context.  Its two retained arXiv records are contextual only; no
external theorem is imported.  No completeness, novelty, or priority claim
is made.

## Claim boundary

R0.75Y proves only the strongly separated exact common-shear family.  It
does not cover unresolved high-carrier clusters
`aR\,\delta_{\boldsymbol n}<8q`, weaken the separation condition, or
control the consecutive-frequency outer-cap packet of R0.75R.

The exact field embeds in the smooth unforced shear `u=(0,B,F(t,x_2))`,
but the nonzero constant background has not been shown to lie in the frozen
mean-zero, inversion-paired Version-M subclass.  Any Version-M consequence
remains conditional on the same measurement row, weight, realized subclass,
actual component, and ledger alignment.

Arbitrary packets, inter-packet aggregation, nonconstant or vertically
dependent shear, projection from a larger velocity, arbitrary-field E.24,
complete Version-M extraction, fixed deletion, suitable-weak transfer,
regularity, and singularity remain open.  **NOT CLAY.**

## Recap and figure boundary

R0.75W remains the terminal milestone recap.  Y is a new separated-sector
theorem, but unresolved clusters still contain the central multimode
difficulty.  Do not update the cumulative recap.  Preserve the W recap HTML
and PDF byte-for-byte and label its terminal release exactly as
`R0.75W-Step48`.

The proof is analytic.  Do not create a formal scientific figure,
simulation, DNS result, or decorative plot for Y.

## Publication and deployment QA

Publish one bilingual R0.75Y research page and synchronized downloadable
PDF.  Expose all twelve frozen source, audit, certificate, and QA artifacts.
Update the homepage, latest-research count, navigation, research and
literature reviews, version ledger, global notes index, English translation,
and formal archive through Y while keeping the latest-recap endpoint at W.

Run structural, equation, internal-link, asset, recap-preservation, and
forbidden-future-version tests; render desktop and mobile views; verify
there is no overflow or raw TeX leakage.  Commit and push only Y, wait for
the GitHub Pages workflow to succeed, and compare every declared online
object byte-for-byte with the release commit.  A successful push or workflow
alone is not deployment proof.

Do not add a figure, simulation, arbitrary-packet claim, regularity claim,
recap change, or second task.  The release is complete only when
R0.75Y-Step50 is deployed and verified online, after X and before Z.
