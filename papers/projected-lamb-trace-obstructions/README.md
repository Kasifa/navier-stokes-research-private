# Projected-Lamb heat packing and trace obstructions

This directory is a self-contained arXiv-style LaTeX manuscript.

## Files

- `main.tex`: manuscript source;
- `references.bib`: bibliography;
- `figures/local-trace.pdf`: archived vector figure for the localized heat-trace obstruction;
- `figures/internal-entry.pdf`: archived vector figure for the positive-time internal-entry construction.

The two figures are regenerated from the certified data and plotting routines
in `figures/r071f-local-trace/` and `figures/r071t-internal-entry/`; only the
internal release labels are omitted in the manuscript versions.

## Build

The source uses only standard arXiv TeX Live packages. A conventional build is

```text
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

Tectonic may also be used:

```text
tectonic main.tex --keep-logs --keep-intermediates
```

## Claim boundary

The paper proves heat-bulk and localization estimates, sharp trace
obstructions, a smooth positive-time shell-entry construction, and a scaling
no-go theorem for one specific bare payment. It does not prove global
regularity, construct a singularity, or bound the remaining occupation
measure from the Leray energy inequality.
