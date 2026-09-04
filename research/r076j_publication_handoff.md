# R0.76J publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.76J-Step61`
- research label: `R0.76J`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.76I-Step60`
- cumulative recap required: `false`
- retained cumulative recap terminal release: `R0.76I-Step60`
- formal scientific figure required: `false`
- core research commit:
  `25d44e986d5283107816f910f89b94bceb1d5726`

This handoff authorizes only R0.76J.  The sole task titled `发布任务` owns
reader HTML, synchronized PDF, homepage/routes, GitHub Pages deployment,
retries, and online verification.  The research task must not perform,
supervise, poll, or report those operations.

Place this release in the existing FIFO behind `R0.76I-Step60`.  If I's
reader page, PDF, and cumulative recap are not yet deployed and online
verified, keep J queued; do not create another publisher or publication
system.  The research task may continue to later mathematics while the
queue is pending.  Append J exactly once after the I gate closes.

R0.76J does not trigger a new cumulative recap.  Retain the R0.76I recap
byte-identically and label its terminal coverage accurately.  Do not imply
that the recap already covers J.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `a3d67c8a27ef6ffb7068313732e8e8a08ba98931226df726ac4ee2140ab0f57f` | `research/r076j_local_edge_extrapolation_reconstruction.md` |
| `1b2a608c6ffe16c35489b95fd384f0f47a1d4a79b22491a7825ac53382a746d5` | `research/r076j_local_edge_extrapolation_reconstruction_primary_audit.md` |
| `371eac6e3f053d4ba51ded16f35024ba805d10c5a81c1f01879704ce583763c7` | `research/r076j_report-source.md` |
| `f0957b65e763339d1ff8cc029a13e13231b22b44dff8796b3b21883ffb352c31` | `scripts/r076j_local_edge_extrapolation_reconstruction_fixtures.json` |
| `9e5ad2f9bed318cd1232319240d2e574f070eda0364f97957df9c013f35878e8` | `scripts/r076j_local_edge_extrapolation_reconstruction_expected.json` |
| `ed969fa1730597ecf33bc530ec1e40509080730f0a59552a1309182cd698f771` | `scripts/r076j_local_edge_extrapolation_reconstruction_certificate.py` |
| `ab58a7e8d77434de9ef363b04c43a612d5b61e0504faf82299783f7ea1b171f3` | `scripts/r076j_local_edge_extrapolation_reconstruction_certificate_independent.rb` |
| `d6364ed1896264a21173b2feb6b98e9b34522686d6300bd8066ef9dda18f0538` | `scripts/r076j_local_edge_extrapolation_reconstruction_qa.sh` |
| `23db36bc873a47e1992c9650e5ea04c5c1874f2e2a0bd17b6353bcb4452be89f` | `research/r076j_local_edge_extrapolation_reconstruction_certificate.json` |
| `a6c140ca114e73d975eff57de1804d85ba59fa080720fd5ac17e05d1bf7896d2` | `research/r076j_local_edge_extrapolation_reconstruction_certificate_report.md` |
| `63231761c982914b79e9e3eac271e3602737222fae41b30ea347941eaad056c7` | `research/r076j_local_edge_extrapolation_reconstruction_independent_audit.md` |
| `0a59566aad669f72e9c013f1b4a02b3d35a8232fcd4a2a3781b458cc0e26cf8c` | `research/r076j_local_edge_extrapolation_reconstruction_qa_report.md` |

Every source byte must match this ledger before rendering.  The core
commit must resolve, and its changed-path set must equal these twelve rows
exactly.  Any mismatch is a release blocker.

## Publication synopsis

R0.76I enlarged the exact-shear full-plateau mode window from
`q=o(L^2)` to `q=o(L^(5/2))`, but its new endpoint extrapolation input was
Ruizhe Zhang's July 2026 arXiv v1 Proposition 4.2.  It therefore correctly
remains a historical **CONDITIONAL-LITERATURE** release.

R0.76J removes that conditional dependency.  It reconstructs the needed
edge theorem locally for every finite Fourier sum with complex
coefficients and arbitrary real frequencies, without a separation
hypothesis:

\[
 \max\{|g(1+d)|,|g(-1-d)|\}
 \le\sqrt{\frac{250}{19}}N
 e^{5\sqrt2N\sqrt d}\|g\|_{L^2[-1,1]},
 \qquad d\ge0.
\]

The proof builds the finite vertical-line Takenaka--Malmquist basis,
derives the negative-time Laguerre majorant used for exterior evaluation,
and then proves the positive-time companion

\[
 |\varphi_m(t)|
 \le\sqrt\alpha e^{-\alpha t/2}L_m(-\alpha t).
\]

That companion yields the fully local weighted-tail estimate

\[
 \int_0^\infty|F(t)|^2e^{-\alpha t}dt
 \le\frac{20}{19}\int_0^{25N/\alpha}
 |F(t)|^2e^{-\alpha t}dt.
\]

Choosing `alpha=25N/2` makes the cutoff exactly `2` and closes the finite
endpoint theorem without importing Zhang Proposition 4.2 or Erdelyi's
specialized infinite--finite range theorem.  The architecture is
attributed to Zhang; no independent-discovery or priority claim is made.

For the exact real one-band constant shear, the fibre has at most `2q`
complex branches.  Both the exterior and the entire observed interior are
therefore controlled by

\[
 \sup_{I_a}|G(s,z)|^2
 \le\frac{1000}{19e_a}q^2
 \exp\!\left(20\sqrt2q\sqrt{\Delta_a}\right)
 \int_{E_a}|G(s,z)|^2dz.
\]

Hölder and `e_a>=1/2` give the explicit observation constant `2000/19`.
Inserting this into the frozen R0.76I derivative, reverse-time endpoint,
four-row energy, plateau-mass, and physical-normalization chain proves

\[
 |\mathcal T_{\boldsymbol n,R}|
 \le C_Ja^{2/3}R^{-1/3}q^7
 e^{20\sqrt2q\sqrt{\Delta_a}}
 (M_{\boldsymbol n,R}^{\rm plat})^{2/3}.
\]

The local coefficient `5sqrt(2)` is less optimized than Zhang's
`3sqrt(2)`, but the scale is unchanged.  Since
`Delta_a=O(L^(-1))`, every `q=o(L^(5/2))` still retains the exact normalized
quadratic rate

\[
 -\frac2{11907}.
\]

This is the status change to emphasize: the same mode-count window and
rate are now supported by a locally complete edge proof, while the scope
remains an exact one-band constant shear.

## Source and claim boundary

The reader note must cite and distinguish:

- R. Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*,
  [arXiv:2607.10501v1](https://arxiv.org/abs/2607.10501v1): architecture
  and sharper-constant comparison only, not an imported theorem;
- T. Erdelyi, *Inequalities for exponential sums*,
  [journal record](https://www.mathnet.ru/eng/sm8670), *Sbornik:
  Mathematics* 208:3 (2017): the Markov input in the frozen downstream
  chain and the record of the Kós terminal endpoint inequality;
- S. R. Garcia and W. T. Ross,
  [*Model spaces: a survey*](https://arxiv.org/abs/1312.5018): historical
  background for Takenaka--Malmquist systems;
- P. Borwein, T. Erdelyi, and J. Zhang,
  [*Muentz systems and orthogonal Muentz--Legendre polynomials*](https://doi.org/10.1090/S0002-9947-1994-1227091-4):
  older algebraic ancestry, not a directly quoted exterior theorem.

Keep the following labels separate:

- **LITERATURE:** boundary Plancherel and the two frozen peer-reviewed
  downstream exponential-sum inputs;
- **PROVED LOCALLY:** J's finite basis, two Laguerre majorants, weighted
  tail, bilateral edge theorem, and scaled observation;
- **PROVED LOCALLY FROM ESTABLISHED LITERATURE:** the exact-shear flux
  theorem after the hash-bound R0.76I downstream insertion;
- **FINITE COMPUTATION:** exact constants, finite Laguerre samples,
  equation/reference inventories, mutations, hashes, and rate ledger;
- **OPEN:** optimal constants, a complete real dyadic heat-shear flux
  lower bound, multiple bands, nonconstant shear, arbitrary nonlinear
  packets, arbitrary-field E.24, Version-M extraction, fixed deletion,
  suitable-weak transfer, regularity, and singularity.

Do not state that the finite certificate proves the continuum theorem.
Do not silently relabel R0.76I as unconditional.  Do not claim novelty,
priority, arbitrary-field transfer, regularity, singularity, or a solution
of the millennium problem.  **NOT CLAY.**

## Publication deliverables

Use the established concise retro site style and the existing bilingual
reader-note conventions.  Produce one R0.76J reader page, its synchronized
PDF, route and homepage/progress entries derived from actual files, and
download links for the twelve frozen artifacts.  Preserve mathematical
symbols and the exact fractions above.  Verify desktop/mobile rendering,
HTML/PDF content parity, source links, route tests, and online bytes after
deployment.

No simulation or formal scientific figure belongs to this analytic
release.  Do not add a decorative plot or a new recap.  Publication is
complete only when the page and PDF are online verified by `发布任务`; the
research task does not wait for or report that state.
