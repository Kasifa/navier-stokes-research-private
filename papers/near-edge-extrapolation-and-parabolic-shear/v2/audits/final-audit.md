# Independent v2 research-package audit

Date: 6 September 2026. Release: `paper-heat-edge-v2-20260906`.
Status: **research content and required local quality gates complete**.
The clean source commit and deterministic archive hashes are bound after
commit in `output/release-receipt.json`.

## Scope achieved

All five priority-one requirements and the two required priority-two
research items in the user brief are implemented. The English paper has
11 TeX source files, 100 labels, 106 reference uses and 10 cited bibliography
entries. It compiles to 25 XDV pages. The new theorem gives explicit
uniform two-scale errors throughout the original joint range, with a
profile criterion verified for the first and endpoint-normalized second
Chebyshev families. The complete fixed-initial-data first-kind shear
argument is preserved and re-audited.

The manuscript also includes the original-amplitude full-velocity decay,
the explicit amplitude-rescaling dependence, and a same-shape bounded-drift
vanishing proposition. The temporal upper bound is identified as a
literature corollary and its abstract N^(4/3) order has an explicit lower
construction. Spatial prehistory is compressed and attributed.

The best error orders, general Jacobi parameters, matching dynamic bounds
for the general Fourier class, and other bounded-drift profiles remain
open. This is not a claim of general Navier–Stokes regularity or singularity,
exhaustive novelty, or journal suitability certified by a human expert.

## Proof review

- `quantitative-cross-audit.md`: an agent other than the proof author
  independently recomputed the strong-concavity bound, first-moment tail,
  all explicit constants/threshold budgets, omitted negative-region
  integral and derivative, exact displacement-difference factor, and T/U
  profile hypotheses. PASS. Final source hash is recorded there.
- `quantitative-edge-self-audit.md`: separate author self-check, explicitly
  not counted as independent peer review. The later change to two prose
  sentences was independently checked against the old hash and does not
  change any mathematics.
- `time-cross-audit.md`: independently checks the two primary Erdelyi
  hypotheses, 36N split, explicit absolute constant, coefficient expansion,
  nonzero terms, rates [1,5/4], N=1, horizon N and normalization. PASS.
- `application-audit.md` and `research/bounded-routes.md`: complete
  dynamic-transfer, paired-sign, early-time absorption, full-cap mass and
  normalization arguments. The root agent additionally recalculated
  V=32 pi delta0 a² R⁵(1+delta0²/(3a²)), M_u~|B|³V, the R² rate,
  the L^(3/2) amplitude sandwich and bounded-drift R power. PASS.
- `auxiliary-cross-audit.md`: independently checks the revised 12sqrt2
  exponent, 2q branches, all q and lambda powers, full geometry and the
  compressed classical witness proofs. PASS.
- `literature-manuscript-audit.md`: primary-source attribution and
  contribution boundaries checked. PASS. Later changes to main.tex were
  only an emergency-stretch layout setting; bibliography changes supplied
  an explicit n.d. year for the continuously updated DLMF, rendered the
  same long publisher URL as a named hyperlink, and removed an uncited
  background entry. Source metadata and mathematical statements did not
  change. The final source inventory is in `source-quality.json`.

The root agent read the quantitative proof in full and independently
checked the local-window normalization, the four deductions used in the
threshold, the U denominator identity and the non-normalized counterexample.
No unresolved mathematical blocker was found within this task's scope.
Automated analytic reviews are not human peer review or formal proof-assistant
verification and do not guarantee an exhaustive novelty determination.

## Issues found and resolved

1. The imported Markov inequality now explicitly assumes real frequencies
   and identifies Theorem 9.1 in arXiv v1. Its actual application already
   met that condition.
2. The exact nonzero-frequency assertion in the compressed coefficient
   lemma now explicitly inherits the real-rooted hypothesis. Without it,
   p=x²+1 at eta=1 is a counterexample to nonvanishing of every coefficient.
3. A Chinese Markdown transcription initially lost inline math escapes
   and contained control characters. It was rewritten with literal math
   delimiters, checked against the TeX proof, and passed the file gate.
4. Two TeX line-overflow warnings and an empty-year bibliography warning
   were corrected. The final build has none of the checked warning classes.

These issues and their remedies were not replaced by numerical evidence.
The normalized-U result does not silently promote unnormalized U: the
counterexample to that promotion remains in the manuscript.

## Fresh finite and source checks

| Check | Actual result | Boundary |
|---|---|---|
| `checks/verify_revision.py` | PASS, 1192 positive + 239 negative/mutation checks | Exact finite Fraction arithmetic; not an asymptotic proof |
| historical `verify_algebra.py` | PASS, 1725 positive + 141 negative checks | Fresh rerun of retained dynamic/algebra identities; historical constants remain identified as baseline |
| historical `plot.py --check` | PASS, 16 rows, data.csv and SVG reproduced | Finite binary64 quadrature only |
| new source quality gate | PASS, 11 TeX files, 100 unique labels, 106 references, 10 cited keys, no missing/unused keys | Static source and compile diagnostics |
| Tectonic 0.16.9 | PASS, 25-page XDV; no overfull box, missing character, unresolved reference or BibTeX warning | No new reader PDF and no new visual manuscript review |
| independent extracted source-ZIP build | PASS, 14 compile inputs exact; AUX, BBL and XDV byte-identical to the reference | Local only-cached build; not remote arXiv |

Reports are `revision-algebra.json`, `baseline-algebra.json`,
`retained-figure-check.json`, `source-quality.json`, and `archive-build.json`.
Full compilation diagnostics are retained under `logs/`.
The current figure was viewed in full as a grayscale image; its inherited
final-size review and all PDF/SVG/600-dpi PNG/data assets are preserved.
It is not presented as a new diagnostic of the quantitative error bounds.
No DGX workload was needed for these short analytic/finite checks.

## Repository, freeze and handoff

The original paper worktree still has HEAD
`0a212f4e140e0c9875e740cb8ee23be32a5c05dd` and the same pre-existing
modified AGENTS.md/untracked older-paper directory. Only the v2 directory
is staged on `codex/heat-edge-paper-v2`; all tracked v1 bytes remain those
of the baseline. No root-Math commit, mainline worktree/index update,
publication queue access, push or deployment is part of this revision.

The source manifest excludes itself and derived outputs. After the clean
source commit, the packager re-verifies the manifest and restricts every
changed path to v2, then verifies every archive member byte-for-byte.
The receipt supplies the exact commit and output hashes. No automatic
journal/arXiv submission or public release is authorized by this package.
One return to the fixed research task is the final registration action;
that task alone owns any later publication handoff.
