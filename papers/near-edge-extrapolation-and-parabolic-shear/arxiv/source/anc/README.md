# Ancillary code and data

These materials accompany *Heat-evolved Chebyshev edges and localized
fluxes of sparse Fourier shears*, by C. K. Zeng.

Run from the root of the extracted source archive:

```sh
python3 -B anc/checks/verify_revision.py
python3 -B anc/checks/verify_algebra.py
python3 -B anc/heat-edge/plot.py --check
```

The first two commands use Python's standard library and exact rational
arithmetic. The revision suite compares independent representations of
Chebyshev endpoint derivatives and heat evolution, the temporal order
witness, and normalization identities. It has 1192 positive checks and
239 negative controls. The retained algebra suite has 1725 positive
checks and 141 negative controls. Some constants in the retained suite
belong to its earlier baseline; the revision suite checks the updated
coefficient separately. These finite checks are not proofs of the
asymptotic theorems and do not establish optimality or regularity.

The plotting command requires NumPy; the recorded environment uses
Python 3.12 and NumPy 2.3.5. It reproduces all 16 rows in
`anc/heat-edge/data.csv` and the reference `figure.svg`, and prints the
two-resolution and tail-truncation comparison. The vector figure
included in the paper is `figures/heat-edge.pdf`.

The diagnostic concerns the positive first-kind exterior integral.
It illustrates qualitative limits, not the new error bounds or the
second-kind extension. Binary64 quadrature is not an interval enclosure.
The proofs in the manuscript provide the continuum arguments.

`plot.py --check` does not modify the reference data. The optional
`--formal` mode regenerates the CSV and SVG and writes run logs locally.
The PDF figure is supplied directly, so no graphics conversion is
required to compile the paper.
