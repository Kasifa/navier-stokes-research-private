# Scientific figure inventory

One historical figure is retained unchanged from v1, originally frozen with the L source package. No new scientific simulation figure or reader PDF is created.

- Location: `../v1/figures/heat-edge/`.
- Source: `b234b63c24c7b19efc703367e23b092385066a1c`; original manifest, caption, code, configuration, data and diagnostic logs retained.
- Exports: vector PDF/SVG, 600 dpi PNG; original width 178 mm, height 72 mm.
- Current repeat: `plot.py --check` PASS, all 16 data rows and regenerated SVG match. Report: `audits/retained-figure-check.json`.
- Current visual check: existing grayscale PNG viewed in full on 2026-09-06; labels, distinct markers, limit lines and all three panels legible. This was a screen inspection of the inherited graphic, not a fresh print-size layout review of the v2 manuscript. Historical final-size/grayscale review remains in the inherited `qa-report.md`.
- Boundary: the plotted positive exterior integral illustrates the qualitative first-kind limits. It is not an interval certificate, proof of the new error bounds, verification of U, or a PDE simulation.

| File | Bytes | SHA-256 |
|---|---:|---|
| `figure.pdf` | 71783 | `6de47c8df62ae35fc85e5b1ca2010038dd505d2e15b39caaa1f765b30cf4e7ea` |
| `figure.svg` | 12650 | `5e9061d5b76b03c60d58cac98320513dc442b7a595604ee9c59697b2e4190662` |
| `figure.png` | 472120 | `a5bff2596a6bf9ab0becc41cba0a985744c3b31878c6b11281ca2f4cf891fc75` |
| `data.csv` | 4679 | `bbc7139237a9120d91284c0ddb80c0c73aa93708bb4a8f778f38e1d24d18c96d` |
| `plot.py` | 19619 | `079a32963e6f9bf72771b647683e83d6264e3c1c365ae0004ac58f29b48ba8a2` |
| `config.json` | 466 | `ec613babd5ff988c732bbd9881962e93dc6e5ef2821832eb22a069b843fece28` |
| `manifest.json` | 5463 | `c6c6e5e6ab980eddf254ec2462b73bc99cc351c05069adb6fb0aefd52719f29f` |
