# Sharpness section proof audit

Date: 2026-09-05. Source: research/r076k_real_dyadic_edge_sharpness.md in
navier-stokes-r074m. Output: sections/sharpness.tex. This is a source-proof
audit; no continuum statement is inferred from finite computation.

## Included results and checks

| Manuscript result | Check | Boundary |
| --- | --- | --- |
| Real dyadic lower bounds | Confluence, endpoint phase alignment, Chebyshev identity, norms <= 8 and <= 16, exterior subinterval length d/8 | Supremum statement, fixed q and d; no attainment |
| L2 endpoint q/sqrt(2) | Legendre orthogonality gives K(1)=||K||2^2=q^2/2 | q positive modes become 2q complex branches |
| L3 endpoint 2^(-1/3) q^(2/3) | ||K||3^3 <= ||K||infty ||K||2^2 <= q^4/4 | Squared lower power q^(4/3) is not optimality proof |
| Integer slice | Exact amplitudes prepay heat and phases prepay transport at s_* | Every prescribed s_* has its own packet |
| Navier--Stokes equation | div u=0; only third component evolves, F_t+B F_y=F_yy | Smooth periodic exact class; not finite-energy R3 data |
| Growing degree | Complex segment bound plus coefficient recurrence; eta q^2 6^q -> 0 | Sufficient range q=o(L^2), not the full upper q=o(L^(5/2)) window |
| Evolution away from s_* | Conjugate A^(-2) D^2-cD by e^(i M x) | No persistence or signed full-clock conclusion |

## Supplementary analytic strengthening

The earlier note used a small-spacing condition to guarantee nonzero
transformed coefficients. The manuscript proves the stronger assertion
for every positive spacing when the polynomial is real-rooted:

`b_j(eta) = p^(j)(i/eta) / (j! (i eta)^j)`.

All derivatives of a real-rooted polynomial are real-rooted by Rolle's
theorem. Hence their values at the nonreal point i/eta are nonzero.
The Legendre endpoint kernel has n simple roots in (-1,1): its reproducing
identity implies orthogonality to degree < n for the positive weight
1-x. The standard sign-change argument is supplied in full.

This removes the coefficient-nonvanishing part of the old conservative
7^q condition. The independent approximation estimate uses
(9/4)(1+sqrt(2)) < 6 and gives eta q^2 6^q -> 0. It does not establish
any high-degree heat-time transfer. No originality claim is made for
these elementary supplementary facts.

## Details repaired or made explicit

1. Realification is not an inclusion R_q subset T_q; the count is 2q.
2. The fixed carrier M=1 is needed for the exterior subinterval estimate.
3. Ratios pass to a nonzero limiting polynomial times cosine; convergence
   does not assert that the supremum is attained.
4. The exact phase is -theta-arg(b_j)-n_j B R^2 s_*.
5. The physical dyadic condition is n_0 >= q-1 with n_j=n_0+j.
6. The current manuscript does not inherit the old claim that q^2 is the
   best known L3 endpoint upper power. Erdelyi's p>2 theorem gives q^(5/3).
7. Signed two-cap single-slice algebra from the source is not needed to
   prove the displayed spatial theorem and is not promoted to a full-clock
   result. The complete evolution problem is handled separately.

## Remaining audit boundary

The manuscript reproduces the analytic proofs. The root agent should
check cross-section notation, bibliography keys and the final compiled
cross-references. No Git commit, PDF compilation, website change or
external publication was performed by this subtask.
