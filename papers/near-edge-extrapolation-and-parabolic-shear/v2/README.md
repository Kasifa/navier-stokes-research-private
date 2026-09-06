# Heat-evolved Chebyshev edges and localized fluxes of sparse Fourier shears

Independent research revision v2, 6 September 2026. Author: **C. K. Zeng**.
ORCID: **0009-0002-5402-3374**. Baseline: `0a212f4e140e0c9875e740cb8ee23be32a5c05dd`.

Start with [成果说明.md](成果说明.md) for the Chinese result summary and
[main.tex](main.tex) for the English manuscript. The new uniform error
bounds and normalized second-kind extension are proved in
[quantitative-edge.tex](sections/quantitative-edge.tex), with a complete
Chinese proof in [research/quantitative-edge.md](research/quantitative-edge.md).

The revision includes the fixed-initial-data full-interval shear argument,
frame and amplitude-normalization analysis, an attributed temporal upper
bound and explicit temporal order witness. See
[RESPONSE_TO_DUE_DILIGENCE.md](RESPONSE_TO_DUE_DILIGENCE.md),
[provenance.md](provenance.md), and [audits/final-audit.md](audits/final-audit.md).
The bounded primary-source search is recorded under `literature/`.
Automated independent reviews do not constitute human peer review.

## Build without a new reader PDF

Run `PAPER_TECTONIC=/path/to/tectonic sh build-xdv.sh` with Tectonic 0.16.9
or a compatible engine. The script generates XDV, bibliography and logs
under ignored `tmp/build/`, then checks source and compilation structure.
It does not run PDF conversion. A TeX engine may download its standard
resources on its first run. No submission service is called.

The complete source archive keeps `v2/` and the required historical
`v1/` dependencies as sibling directories. The retained scientific figure
is referenced through `../v1/figures/heat-edge/figure.pdf`; it is a historical
vector figure, not a new reader PDF. All old manuscript PDFs remain in v1.
No new manuscript visual-render review is claimed for this source delivery.

## Reproduce finite checks

```sh
python3 checks/verify_revision.py
python3 ../v1/checks/verify_algebra.py
python3 ../v1/figures/heat-edge/plot.py --check
python3 checks/source_quality.py
```

The first two use exact standard-library arithmetic. The historical
figure check requires NumPy (verified with 2.3.5). Their outputs are
archived under `audits/`; none is a proof of a continuum limit.
`checks/package_release.py` writes or verifies a non-self-referential
source manifest and, after commit, creates the local release archive
and receipt. Its `--freeze` mode refuses a dirty tracked worktree.

## Boundaries and ownership

The full-velocity decay is for the original amplitude normalization.
The manuscript also proves its dependence on amplitude rescaling and
a vanishing result for bounded drift with the same initial shape.
The optimal error order, matching general dynamic upper/lower bounds,
and wider profile classes remain open. **NOT CLAY.**

This branch changes only the new v2 directory. The research sources and
v1 remain frozen; no shared mainline index or publication queue is read
or edited. No push, public deployment, journal submission or arXiv upload
is performed. Once complete, the frozen package is handed once to the
fixed research task for registration under the authorized single-paper
exception.
