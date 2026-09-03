# R0.75N Step 39 frozen publication handoff

## Release identity and queue order

- release id: R0.75N-Step39
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75M-Step38`
- queue rule: hold until R0.75M is verified, then append exactly once to the
  same FIFO task; never create or reuse any other publishing, recap,
  reflection, lessons-learned, usage-notes, or temporary task/system
- frozen research/certificate commit:
  `90a0d654447ba40865797669e5e5ad21ad9baa54`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75N. Do not read or publish R0.75O or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `ba59a4df399d8580b35d8dbb3f0758f9d2ffcc7f97f1147e5804c428f3740318` | `research/r075n_radial_collar_averaged_wiener_row.md` |
| `c43c063b1c003be22782e7d8e1ce0b3f42cdd3ef4d01912c9de34c876d8c9aba` | `research/r075n_radial_collar_averaged_wiener_row_primary_audit.md` |
| `ae9d5d630ee0549193c016fcbc07c599b0c678fbaf9c15c5d3c7f24bdf18e27c` | `research/r075n_report-source.md` |
| `2dee2146f94f3fa6d0d0c5828d8d6f354f0856f620e1261a133c9a2c81f8a0cb` | `scripts/r075n_radial_collar_averaged_wiener_row_fixtures.json` |
| `31614fc11bc4355723fff7773bec8ab13bc44808ffffa0958c78ec1cfe2bba48` | `scripts/r075n_radial_collar_averaged_wiener_row_expected.json` |
| `891774ec5c7e747a4f9c172f0b71e4f6f2af40d8a983bc7c69ebbd1756f405d7` | `research/r075n_radial_collar_averaged_wiener_row_certificate.json` |
| `cad991130fb614d923c224a891001010119a746f9d32c1d17d0fbc5f6c56c0b5` | `research/r075n_radial_collar_averaged_wiener_row_certificate_report.md` |
| `779d359b62c2860a07e8889826d038d88cad8356af9c53ce31f5bfd1d85441b6` | `research/r075n_radial_collar_averaged_wiener_row_independent_audit.md` |
| `d45d0eef91dab59db773940e2b47caea282781671e186709d7c58f0111c4c4ef` | `research/r075n_radial_collar_averaged_wiener_row_qa_report.md` |
| `47256d34a25a188a32147e4cb9f0388819238f2c854e1e814612b9bfd217950e` | `scripts/r075n_radial_collar_averaged_wiener_row_certificate.py` |
| `63836294b2924433afa0e95d07baee6427446c7c26c14a34dcd9a5818e0fed56` | `scripts/r075n_radial_collar_averaged_wiener_row_certificate_independent.rb` |
| `568b7934a403e076fb51ae0f18b142547f621a1a514c6ced14e01635c540c66e` | `scripts/r075n_radial_collar_averaged_wiener_row_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0. Certificate QA: Python 16/16, Ruby 17/17, 107/107 negative
mutation families rejected independently by each implementation, unknown
mutations fail closed, `PYTHONHASHSEED=0,1,42` byte stability, and complete
regeneration byte stability.

## Result and exact boundary

R0.75M reduces the signed flux of one finite horizontal dyadic packet to
the Wiener row of the cutoff derivative, but does not determine that row
for the physical radial collar. R0.75N chooses one canonical smooth radial
representative allowed by the frozen outer-collar construction and proves
that horizontal averaging removes the apparent pointwise `R^(-1)` loss.

Retain

\[
 p=\frac{32}{63},\qquad a=pL,\qquad r=aR,
 \qquad 0<R\le1,
\]

and choose a fixed smooth profile `vartheta` supported in a normalized
radial collar. In the central torus chart set

\[
 \xi_{a,R}(x)=
 \vartheta\!\left(\frac{|x|-r}{R}\right)
 =\vartheta\!\left(\frac{|x|}{R}-a\right).
\]

Let `d_l(x_3)` be the horizontal Fourier coefficient of the `x_1`-averaged
`partial_2 xi`. With the R0.75E convention,

\[
 d_\ell(x_3)=i\ell\Xi_\ell(x_3),\qquad d_0=0.
\]

The principal coefficient theorem is

\[
 \boxed{
 \sum_{\ell\in\mathbb Z}
 \|d_\ell\|_{L^\infty_{x_3}}
 \le C_\vartheta a\le C_\vartheta L.}
\]

The supremum is inside the Fourier sum, so this is stronger than a
pointwise-in-`x_3` Wiener bound. If the cutoff is also averaged in `x_3`,
the corresponding row satisfies

\[
 \boxed{
 \sum_{\ell\in\mathbb Z}|D_\ell|
 \le C_\vartheta R a^2
 \le C_\vartheta L^2R.}
\]

The scale-correct sampling lemma behind both bounds is: for a uniformly
compactly supported family `h_z` with
`sup_z(||h_z||_1+||h_z''||_1)<=A`, every `nu>=1` obeys

\[
 R^\nu\sum_{\ell\in\mathbb Z}
 \sup_z|\widehat h_z(\ell R)|
 \le C R^{\nu-1}A.
\]

Low modes use the `L^1` bound and an `O(R^(-1))` count; high modes use two
integrations by parts and
`sum_(|ell|>R^(-1)) ell^(-2)<=CR`. Exact slice geometry, including the
tangency band, bounds the scaled two-dimensional shell by
`4*pi*a*delta`. Uniform first and third radial derivatives plus Fubini
then give the required `O(a)` row; the fully averaged three-dimensional
shell gives `O(a^2)` with an additional `R^2` Fourier prefactor.

At the frozen high-frequency threshold `K>=R^(-3/2)`, the result yields

\[
 \boxed{
 \left(\sum_\ell\|d_\ell\|_\infty\right)K^{-2/3}
 \le C_\vartheta LR,
 \qquad
 \left(\sum_\ell|D_\ell|\right)K^{-2/3}
 \le C_\vartheta L^2R^2.}
\]

This proves a selectable canonical geometric coefficient theorem only.
It does not prove the same bound for every previously unspecified cutoff,
extend the R0.75M time kernel through vertical diffusion or nonconstant
shear, replace the full-torus cubic mass by buffered collar atoms, sum
dyadic packets, or close low difference frequencies.

The certificate freezes the cutoff-choice boundary, central-chart and
periodization conditions, Fourier sign and `1/(2*pi)` normalization,
`d_0=0`, sum/sup order, low/high sample split, two-integration-by-parts
tail, spherical tangency cap, first/third radial derivative ledger,
`R`/`R^2` averaging factors, final rows, `K>=R^(-3/2)` diagnostic, tags,
displays, dependencies, and claim boundaries.

E.24, complete-clock extraction, fixed deletion, suitable-weak transfer,
regularity, and singularity remain **OPEN**. The bounded primary-source
screen makes no completeness, novelty, or priority claim. **NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75N research page and synchronized downloadable
PDF, expose every frozen audit/certificate/source artifact, and update the
homepage, latest-research count, navigation, version ledger, and global
index through N. Do not update the cumulative recap at this non-major
milestone and do not invent a formal figure, simulation, DNS result,
dynamical flux theorem, universal-cutoff theorem, collar-localization
theorem, or literature-completeness claim.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; desktop/mobile render inspection; GitHub Pages workflow verification;
and online byte-identity checks. Report the site commit, workflow run,
page/PDF/object counts, and deployed-byte verdict. No second task is
authorized. **NOT CLAY.**
