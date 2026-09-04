# R0.76K publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.76K-Step62`
- research label: `R0.76K`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.76J-Step61`
- cumulative recap required: `false`
- retained cumulative recap terminal release: `R0.76I-Step60`
- formal scientific figure required: `false`
- simulation required: `false`
- core research commit:
  `8a89aee4fe0839de44e21a90ba827a9cc77b3062`

This handoff authorizes only R0.76K.  The sole task titled `发布任务` owns
reader HTML, synchronized PDF, homepage/routes, GitHub Pages deployment,
retries, and online verification.  The research task must not perform,
supervise, poll, or report those operations.

Place this release in the existing FIFO behind `R0.76J-Step61`.  If J's
reader page and PDF are not yet deployed and online verified, keep K
queued; do not create another publisher or publication system.  The
research task may continue to later mathematics while the queue is
pending.  Append K exactly once after the J gate closes.

R0.76K does not trigger a cumulative recap.  Retain the R0.76I recap
byte-identically and label its terminal coverage accurately.  Do not imply
that the recap already covers J or K.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `e293a3aa3e9c1dde443ed7a8c07afd2c709d3855d8b469b38033b04d71116bf2` | `research/r076k_real_dyadic_edge_sharpness.md` |
| `36a26cb421a108127b516e47a0008625d67ec43a1d009a14bef9d7684ef03671` | `research/r076k_real_dyadic_edge_sharpness_primary_audit.md` |
| `21dbd71aae07ecbe910d4bcefbf6e1caccc3cddc41171a57ffd239c6eed34f3e` | `research/r076k_report-source.md` |
| `16acf468a6722ee1e66e36a855fdd1e84e56bdc3519e6e2326d6bec0a3b82518` | `scripts/r076k_real_dyadic_edge_sharpness_fixtures.json` |
| `8f32d96856fdf5d0a86030737f5bf049b227f976661089ed6d31d4a41a1c5b50` | `scripts/r076k_real_dyadic_edge_sharpness_expected.json` |
| `c05ab480973a418e69cb40984b1da5c7210c5e4916e2fa1d6fb6281a9b53d1d9` | `scripts/r076k_real_dyadic_edge_sharpness_certificate.py` |
| `893b0b5e18e3a3fca06ef10e7879e361894dafbb845d09264373e92f116210bb` | `scripts/r076k_real_dyadic_edge_sharpness_certificate_independent.rb` |
| `5968f4b6a08d982c4345165e7fc0bc04c33dca66ab7cf8c1dba0be30a5212a79` | `scripts/r076k_real_dyadic_edge_sharpness_qa.sh` |
| `4d5247ca82869758c01a398f9a4858bfce87e3bd7ab3ad2a37eac0e6bdea7f1d` | `research/r076k_real_dyadic_edge_sharpness_certificate.json` |
| `43131539e1fd4105fe0215739003b7819379e87d44ddab4aa772a40bcc47daaa` | `research/r076k_real_dyadic_edge_sharpness_certificate_report.md` |
| `7d87a4b543051e08cc6a348c5b7f261cd433fdf8efba4986ed01514c13c78b1a` | `research/r076k_real_dyadic_edge_sharpness_independent_audit.md` |
| `b888919d4f1992c22e5206d6350983dbd89885df29bb62b3408b581298c511ec` | `research/r076k_real_dyadic_edge_sharpness_qa_report.md` |

Every source byte must match this ledger before rendering.  The core
commit must resolve, and its changed-path set must equal these twelve rows
exactly.  Any mismatch is a release blocker.

## Publication synopsis

R0.76J supplied a locally complete upper extrapolation estimate.  R0.76K
asks whether its characteristic edge factor is merely an artefact of the
larger complex-frequency class.  It is not: the lower scale already occurs
for real cosine packets with `q` positive frequencies in one dyadic band.
For every `q>=2` and `0<d<=1`, the note proves

\[
 \sup_{0\ne g\in\mathcal R_q^{\rm dyad}}
 \frac{|g(1+d)|}{\|g\|_{L^2[-1,1]}}
 \ge \frac1{2\sqrt2}
 e^{(q-1)\operatorname {arcosh}(1+d)}
 \ge\frac1{2\sqrt2}e^{(q-1)\sqrt d}.
\]

One and the same fixed-carrier witness gives the exterior interval bound

\[
 \sup_{0\ne g\in\mathcal R_q^{\rm dyad}}
 \frac{\int_1^{1+d}|g(t)|^2dt}
      {\int_{-1}^1|g(t)|^2dt}
 \ge\frac d{128}
 e^{2(q-1)\sqrt{7d/8}},
\]

and the same safe constant for the denominator
`(int_[-1,1]|g|^3)^(2/3)`.  At `d=0`, the Legendre Christoffel kernel gives

\[
 \sup_{0\ne g\in\mathcal R_q^{\rm dyad}}
 \frac{|g(1)|}{\|g\|_{L^2[-1,1]}}
 \ge\frac q{\sqrt2}.
\]

The confluent construction is made real by conjugate pairing.  Its `q`
positive cosine modes therefore correspond to `2q` complex branches;
the reader page must not relabel this as a complex `T_q` inclusion.

For every prescribed scaled time `s_*` and constant shear parameter `B`,
the note chooses consecutive positive integer modes and compensates heat
damping and transport phase exactly, obtaining

\[
 G(s_*,e_ax)=2\operatorname {Re}\left[
 e^{i\theta}e^{iM_Lx}
 p\!\left(\frac{e^{i\eta_Lx}-1}{i\eta_L}\right)
 \right].
\]

This is an existence statement for a packet depending on the prescribed
pair `(s_*,B)`, not one packet realizing the identity at all times.  A
uniform coefficient estimate closes the exact integer-slice construction
whenever

\[
 \eta_Lq(L)^27^{q(L)}\longrightarrow0.
\]

It covers every `q(L)=o(L^2)` and, more generally,
`limsup q(L)/L^2<rho/(4 log 7)`.  It does not cover the entire R0.76J upper
window `q=o(L^(5/2))`; this is an open proof gap, not a counterexample.

The signed two-cap algebra also closes at the selected slice.  With a
fixed negative transport velocity and

\[
 U_m(x)=2T_m(x)\cos(x-\pi/4),
\]

paired collar points satisfy

\[
 U_m(x_r)^2-U_m(-x_r)^2
 =4\sin(2x_r)T_m(x_r)^2\ge0.
\]

The paired term is strictly positive on the chosen exterior subcap.  That
favourable subcap retains an `exp(2 Gamma_m)` spatial contrast, up to
polynomial factors, against the two-thirds power of the full-plateau
spatial `L3` density.  This closes the signed single-slice algebra only.

The exact clock evolution identifies the obstruction to a free spacetime
upgrade.  Heat conjugation replaces the terminal polynomial by
`e^(tau A^(-2)D^2)T_m`, while the exact backward calculation gives

\[
 \left|\left(e^{-(T/A^2)D^2}T_{2n}\right)(0)\right|
 \ge e^{cTm^2/A^2}
 \qquad(m=o(A^2)).
\]

In the overlap `A^(3/2)<<m=o(A^2)`, this parabolic cost already exceeds the
cap gap `Gamma_m=O(m/sqrt(A))`.  The result rules out a cost-free bridge
from the selected terminal slice; it does not rule out every possible
packet and does not prove a matching complete-clock signed-flux lower
bound against full plateau mass.

## Source and claim boundary

The reader note must cite and distinguish:

- R. Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*,
  [arXiv:2607.10501v1](https://arxiv.org/abs/2607.10501v1): Proposition
  7.1 supplies the earlier complex confluent Chebyshev architecture;
- X. Chen and E. Price, *Estimating the Frequency of a Clustered Signal*,
  [ICALP 2019 publisher record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2019.36): historical clustered-Fourier motivation;
- [NIST DLMF Section 18.3](https://dlmf.nist.gov/18.3) and
  [Section 18.6](https://dlmf.nist.gov/18.6): standard Legendre
  orthogonality and endpoint normalization.

Keep these labels separate:

- **LITERATURE:** the complex confluent architecture and classical
  orthogonal-polynomial facts;
- **PROVED LOCALLY:** real dyadic lower bounds, endpoint lower bounds,
  exact integer heat-shear slice, `q=o(L^2)` varying-degree range, signed
  two-cap slice identity, exact semigroup formula, and backward warning;
- **FINITE COMPUTATION:** exact rational coefficients, two independent
  integer-slice routes, heat-prepayment exponents, finite-eta semigroup
  rows, backward/forward sign controls, mutations, hashes, and equation
  inventory;
- **OPEN:** the complete-clock signed flux relative to full plateau,
  `L3` endpoint optimality, the full `q=o(L^(5/2))` lower range, multiple
  bands, nonconstant shear, arbitrary nonlinear packets, arbitrary-field
  E.24, Version-M extraction, fixed deletion, suitable-weak transfer,
  regularity, and singularity.

The bounded primary-source search did not locate the exact combined
real/dyadic/integer-heat-shear statement, but this absence is not evidence
of novelty or priority.  Do not claim a full flux theorem, priority,
arbitrary-field transfer, regularity, singularity, or a solution of the
millennium problem.  **NOT CLAY.**

## Publication deliverables

Use the established concise retro site style and existing bilingual
reader-note conventions.  Produce one R0.76K reader page, its synchronized
PDF, route and homepage/progress entries derived from actual files, and
download links for the twelve frozen artifacts.  Preserve the exact
fractions, quantifiers, mode-count convention, and open boundaries above.
Verify desktop/mobile rendering, HTML/PDF content parity, source links,
route tests, and online bytes after deployment.

No simulation or formal scientific figure belongs to this analytic
release.  Do not add a decorative plot or a new recap.  Publication is
complete only when the page and PDF are online verified by `发布任务`; the
research task does not wait for or report that state.
