# arXiv preparation audit

Date: 2026-09-06. Status: **LOCAL PREPARATION COMPLETE**.

This submission copy is derived from the research freeze
`ee014e3d8d332282b6e708aaa73dec23ed275b69`. It preserves the research
scope and does not claim arXiv server acceptance, publication or human
peer review. No account action or submission was performed.

## Manuscript and metadata

- Independent editorial review read the complete manuscript and then
  compared the actual submission copy. The title, author, ORCID and AI
  disclosure were retained. The abstract clarifies one initial datum
  for each member of the sequence; `D=d/dx` is defined in the introduction.
- The mathematical preservation gate confirms **36 formal statements
  and proof blocks** and **139 displayed-mathematics blocks** are byte-identical
  to frozen v2. The 100 labels and 108 references resolve. All ten
  bibliography entries are cited.
- Internal version history, absent audit references and obsolete delivery
  statements were replaced with reader-facing prose and actual ancillary
  data/code references. No stronger theorem, priority or regularity claim
  was introduced.
- Metadata title, authors and abstract are ASCII. The abstract is
  **1619 characters** and matches the manuscript after whitespace and
  the ASCII rendering of Erdelyi's accent. TXT/JSON fields agree.
- Comments state **25 pages, 1 figure**. MSC codes use commas. `math.CA`
  and `math.AP` are recommendations. Publication DOI, journal reference
  and report number are blank, and no license was selected for the author.

## Build and package

- Standard `article`, PDF figure and ordinary TeX Live packages; no custom
  journal/arXiv template, system font dependency, EPS conversion, shell
  escape, or hand-written `00README.json` is needed.
- Real pdfLaTeX and BibTeX from a local **TeX Live 2025** installation
  produced the final PDF. This is the 2025 final package repository,
  not arXiv's precise 2025-08-03 software snapshot.
- The ZIP contains **22 files**: the main manuscript, ten sections,
  bibliography source and generated BBL, one vector figure, and the
  ancillary README, requirements, verification scripts and figure data.
  No compiled manuscript, build log, hidden file or unrelated audit is
  included. All file names and TeX paths are self-contained.
- The actual ZIP was extracted to a fresh directory. Three pdfLaTeX
  passes used the supplied `main.bbl` without invoking BibTeX. The file
  recorder confirms only the extracted inputs and the TeX installation
  were read. Text and **all 25 rendered pages** match the final preview
  byte-for-byte. PDF binary hashes need not agree because of creation
  metadata; the rendered-page comparison was performed directly.
- No overfull boxes, missing glyphs or unresolved references were found.
  The single expected epstopdf notice says shell escape is disabled;
  this paper directly includes a PDF figure and needs no conversion.

## Finite reproducibility and visual checks

- Revision suite: **1192 positive + 239 negative controls**, PASS.
- Retained algebra suite: **1725 positive + 141 negative controls**, PASS.
- Figure: **16 data rows**, CSV and reference SVG reproduce, PASS.
  The finite algorithms are unchanged; the revision fixture path and
  an obsolete plotting docstring are the only ancillary code differences.
- All 25 pages were visually inspected: pages 1-12 by the root agent,
  pages 13-25 by an independent agent. The final bibliography pages
  24-25 were inspected again after correcting duplicate DOI text and
  preventing a single bibliography entry from splitting across pages.
  The other 23 final renders are unchanged from the reviewed set.
- Poppler lists **31 font objects**, including the figure fonts; all
  are embedded. PDF checks found no blank pages, out-of-page glyphs,
  unresolved `??`, JavaScript or encryption.

These finite checks do not prove continuum asymptotics. Mathematical
proofs and their established limitations remain in the manuscript.

## Evidence and remaining author actions

Machine-readable evidence is in `submission-validation.json`,
`archive-build.json`, `visual-qa.json`, the two algebra reports, and
`figure-check.json`. `pdf-fonts.txt` includes the figure's font objects.
`editorial.diff` records the manuscript changes. `source-manifest.json`
at the parent directory binds every uploaded file. Full local build and
render evidence remains under `tmp/` and is excluded from the upload.

The official policy review and actual-package review were performed by
a separate agent. The two issues it found (MSC separators and an unused
render-helper comment) were corrected and validated locally.

Actual submission still belongs to the author: account/endorsement,
license choice, final category choice, and inspection of the PDF built
by arXiv before submitting. No endorsement, moderation decision,
human specialist review or publication outcome is claimed.
