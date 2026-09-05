# Theorem-to-source map

Version: first complete local review manuscript, 5 September 2026.
Author: C. K. Zeng. No public release or external submission is performed.

## Frozen inputs

The repository `/Users/kasifa/Documents/Math/navier-stokes-r074m` contains
the following verified source commits. The current manuscript does not
use that repository's later working notes as proved premises.

| Input | Verified commit | File |
| --- | --- | --- |
| J: reconstructed near-edge bound and full-plateau flux | `25d44e986d5283107816f910f89b94bceb1d5726` | `research/r076j_local_edge_extrapolation_reconstruction.md` |
| K: real dyadic spatial witnesses | `8a89aee4fe0839de44e21a90ba827a9cc77b3062` | `research/r076k_real_dyadic_edge_sharpness.md` |
| L: corrected parabolic calculation | `b234b63c24c7b19efc703367e23b092385066a1c` | `research/r076l_parabolic_edge_smoothing_complete_clock.md` |
| L: associated finite checks | `2f3e0f466cc38fd2b61f2c79773352d95b2464e1` | certificate checkpoint; not a continuum proof |
| L: source handoff | `a5edefb014ebc6dd13ce052aad196ff5115b9629` | source/figure handoff |

The previous 148-line manuscript is preserved as
`history/checkpoint-fe77466d-main.tex` from paper-repository commit
`fe77466d5ec8cde66f08d95734d77e9374417c73`.
The separate older manuscript `papers/exact-shear-flux-obstructions/`
is not modified or replaced.

## Claim ledger

“Analytic proof” below means the manuscript contains the argument and
separate automated review runs checked it. It does not mean formal proof
assistant verification, independent human peer review, or guaranteed novelty.

| Paper label | Evidence and provenance | Boundary |
| --- | --- | --- |
| `thm:ub-edge` | Analytic reconstruction of J; Zhang 2026 is explicit prior work | General scale and proof architecture are not claimed new |
| `lem:ub-delay` | Supplementary analytic proof, retaining the fixed initial interval `S=128N` | Uniform in the terminal horizon; not a numerical tail fit |
| `thm:ub-flux` | J reconstructed with the time lemma, literature inequalities, four-row identity and exact 3D weights | Signed flux; one dyadic band; full region but only `|F|^3` in mass |
| `thm:real-dyadic-lower` | K and known Chebyshev/Legendre witnesses, adapted to real dyadic packets | Supremal slice bounds, not whole-time optimality |
| `lem:confluent-real-rooted`, `lem:kernel-real-rooted` | Full analytic arguments; strengthened all-positive-eta nonvanishing | Nonvanishing alone is not a growing-degree approximation |
| `thm:integer-slice` | K integer realization with explicit heat and drift phases | Initial amplitudes may depend on the prescribed observation time |
| `lem:growing-degree-slice` | Supplementary coefficient-norm proof of `C eta q^2 6^q` | Sufficient range; not a sharp threshold |
| `thm:heat-edge` | L reconstructed with compact-uniform saddle and tilted-tail proof | `sqrt(A) << m << A^2`; not the high-degree working branch |
| `lem:heat-terminal` | Positive coefficient recurrence, moment bound, derivative majorant | Terminal interval is `(1+mu^2)^(-1)` |
| `prop:dynamic-confluence` | Full finite-dimensional semigroup and Duhamel argument | One explicit consecutive-integer-mode family |
| `thm:parabolic-shear` | L with explicit sign pairing, early-time absorption, full caps, algebraic factors | Sequence-dependent eventual onset; divergence needs `mu/log A -> infinity` |
| `cor:critical-coefficient` | Supplementary exact rescaling and limit calculation | Decay of a proved upper coefficient, not an actual phase transition |
| Figure 1 | Archived L data and scientific figure, regenerated in memory by `plot.py --check` | 16 finite binary64 data rows, not an interval certificate |

## Dependencies

The proof has two distinct branches. They meet only in the comparison
section; no static lower bound is silently promoted to a dynamic one.

```text
Zhang / Erdelyi / Kos + local basis proof
    -> edge upper bound + time-weighted decay
    -> uniform full-plateau signed-flux upper bound
    -> sufficient critical coefficient

Chebyshev / Legendre + coefficient identity
    -> real dyadic spatial lower witnesses
    -> prescribed-time integer shear slices

Chebyshev heat convolution + uniform tilted saddle
    -> terminal-layer control + dynamic integer transfer
    -> paired signed flux + entire plateau mass
    -> family-specific complete-time quotient
```

## Figure provenance

The included `figures/heat-edge/` package is copied from the scientific
L figure package `figures/r076l-parabolic-edge/fig-r076l-parabolic-edge/`.
Its original manifest and caption are retained as provenance; the paper
caption explains the finite tilt trend and the legend's degree exponent.
The copied vector PDF has SHA-256
`6de47c8df62ae35fc85e5b1ca2010038dd505d2e15b39caaa1f765b30cf4e7ea`.
The figure is not a new simulation of Navier-Stokes flow.

## Excluded claims

No global regularity theorem, finite-time blow-up construction, general
suitable-weak-solution criterion, high-degree M theorem, exhaustive novelty
search, journal acceptance, or arXiv acceptance is claimed.
