# Near-edge extrapolation and parabolic smoothing in exact Navier-Stokes shear flows

**Status:** complete local review manuscript, version 1.0, 5 September 2026.
Author: **C. K. Zeng**. ORCID: **0009-0002-5402-3374**.

The PDF has 21 pages, 7 sections, complete theorem proofs, one three-panel
scientific figure, and five cited primary sources. This is a manuscript
for author and external expert review, not a claim of journal acceptance
or resolution of the Millennium Problem.

## Deliverables

- `output/pdf/near-edge-parabolic-shear.pdf`: locally compiled paper.
- `output/arxiv-source.zip`: the ten files needed to compile the paper.
- `output/complete-research-package.zip`: LaTeX, bibliography, figure
  data/code, provenance, supplementary-research record, checks and audits.
- `audits/final-audit.md`: integrated audit and unresolved external limits.
- `provenance.md`: theorem-to-source and claim-boundary map.
- `supplementary-research.md`: Chinese record of supplementary arguments
  and corrected claims.
- `source-manifest.json`: non-self-referential SHA-256 source manifest.

The old R0.76F-era manuscript remains untouched. The earlier 148-line
writing checkpoint is retained under `history/`. Later high-degree
working notes and the separate Clay-B research programme are not proved
inputs here.

## Mathematical scope

The uniform upper bound is for signed fluxes of exact periodic,
constant-drift, one-band finite shears. Its mass observes `|F|^3` on the
entire plateau and complete time interval; it is not the mass of the
full velocity including its constant drift.

Spatial lower witnesses fit one prescribed time. The complete-time
parabolic lower bound uses one particular Chebyshev family with
`m/sqrt(A) -> infinity` and `m/A^2 -> 0`. Its eventual threshold can
depend on the degree sequence. Algebraic prefactors remain in the
quotient; divergence additionally needs `mu/log(A) -> infinity`.

The general near-edge scale and polynomial confluence have prior
literature. Their source is stated explicitly. Novelty beyond that prior
work has not been certified by an exhaustive search or human peer review.

## Build

A current TeX distribution with the standard packages used in
`main.tex` is required. The verified local engine was Tectonic 0.16.9.

```sh
sh build.sh
```

If Tectonic is not on PATH, set `PAPER_TECTONIC` to its executable path
before invoking the script. Tectonic may download missing standard TeX
resources on the first run. A conventional alternative is
`latexmk -pdf main.tex`; the supplied `main.bbl` is also available for
services that do not run BibTeX. The remote arXiv processing service has
not been tested or contacted by this packaging operation.

## Checks

```sh
python3 checks/verify_algebra.py
python3 figures/heat-edge/plot.py --check
python3 checks/document_quality.py
python3 checks/package_release.py
```

The algebra checker uses only Python's standard library. The finite
figure check uses NumPy (verified here with 2.3.5). Document checks use
pypdf; optional contact sheets also use Pillow and externally rendered
Poppler PNGs. `verify_clean_build.py` compares a separately extracted
and compiled arXiv source package with the local build.

The 1,866 exact finite algebra checks and the 16-row numerical figure
check do not replace the written continuum and asymptotic proofs.
Separate automated analytic reviews and cross-reviews are documented
in `audits/`; independent human expert review is still outstanding.

## Ownership and release

The user's latest instruction asked the current task to finish this
paper directly. That bounded instruction covered scientific integration,
necessary supplements and local PDF/source delivery. The fixed research
task was informed and avoided concurrent manuscript edits.

No website update, arXiv upload, journal submission, author certification,
or new publication licence was performed. Any later website release
continues through the existing fixed `发布任务` and its FIFO queue.
