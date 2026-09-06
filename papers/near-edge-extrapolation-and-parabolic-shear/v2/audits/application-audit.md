# Exact-shear application audit

Date: 2026-09-06. Type: independent automated mathematical review within
the revision task. This is not human peer review or proof-assistant certification.

Scope: the original full-time implementation, its observation frame,
component/full-velocity denominators, and the three normalization consequences
added in `sections/frame-and-mass.tex`. No publication, submission, or shared
research-state mutation is part of this audit.

## Material read

- The complete revision brief and novelty due-diligence report dated 2026-09-06.
- The complete `v1/sections/parabolic.tex`, `v1/sections/upper-bound.tex`,
  `v1/main.tex`, and `v1/provenance.md` at the paper baseline
  `0a212f4e140e0c9875e740cb8ee23be32a5c05dd`.
- The complete frozen scientific source
  `research/r076l_parabolic_edge_smoothing_complete_clock.md`, read with
  `git show b234b63c24c7b19efc703367e23b092385066a1c:<path>` in
  `navier-stokes-r074m`. Later working notes were not used as premises.
- Applicable repository instructions and the current workspace workflow.

The audit found no substantive defect in the original dynamic transfer,
full spatial plateau, or eventual signed full-time lower bound. The old
statement's sequence-dependent onset and fixed-amplitude qualification
must remain explicit. The following checks explain this assessment.

## Dynamic transfer

1. The finite coefficients are
   `b_j=T_m^(j)(i/eta)/(j!(i eta)^j)`. Taylor expansion at `i/eta`
   produces the stated composition because
   `w_eta(x)=i/eta+exp(i eta x)/(i eta)`.
   Rolle's theorem gives nonvanishing for every positive `eta`, including
   the top derivative. Modulation moves the positive frequencies to
   `m,...,2m`; these are distinct and do not overlap their negatives.
2. Every physical Fourier term obeys the advection–heat equation.
   Divergence vanishes because the third component depends only on the
   second coordinate and the second component is constant.
3. On a test exponential `exp(i j eta x)`, the positive imaginary shift
   `+2 i M t_s` contributes `exp(-2 M j eta t_s)`.
   With scalar damping this gives exactly `exp(-(M+j eta)^2 t_s)`.
   A negative imaginary shift would be wrong; the manuscript has the
   correct sign.
4. On `w^k`, the transformed generator is exactly
   `k(k-1)w^(k-2)+i eta k(2k-1)w^(k-1)-eta^2 k^2w^k`.
   Hence it preserves degree at most `m`. Duhamel's formula applies to
   finite matrices with convergent exponentials.
5. The complex evaluation remains inside the stated nested coefficient
   disks. The real drift is retained; it is not absorbed into the error.
   The perturbations cost
   `eta poly(m,A) exp(Cm+Cm^2/A^2)`.
   Both `m=o(A^2)` and `m^2/A^2=o(A^2)` follow from the degree window.
   Since `A~(32/63)L`, the complete error is
   `exp(-9L^2/40000+o(L^2))`. Uniformity includes `s=0`.

## Exact geometry, signs, and time interval

1. Transverse integration gives
   `integral partial_2 phi = -2 pi y vartheta(|y|/R-a)`.
   The contributions involving `F partial_3 phi` vanish by integration
   in the third coordinate. The `B^3 partial_2 phi` contribution is a
   total derivative. These cancellations leave `B F^2/2` with the sign
   in the manuscript.
2. The dimensional relations are exactly
   `T=a^2 R^3 S/2`, `M_F=a R^5 K`.
   The plateau weight is the difference of two disks. It is not replaced
   by the central slab: the outer end caps remain in the definition.
3. On opposed collar caps, the ideal edge coordinates are
   `r+delta0 ± gamma_L s`, with `gamma_L=beta a/A>0`.
   Evenness requires the explicitly imposed even `m`.
   On `s in [3,4]`, the smaller squared cap is exponentially negligible
   relative to the larger, uniformly over the cutoff support.
   The sign of `v W_a` on the larger cap is positive.
4. A lower bound on one positive cap alone would not prove positivity
   of the signed integral. The proof additionally pairs every late-time
   cap and bounds the absolute contribution on the whole earlier
   interval `[0,3]` by the global majorant at time `3`.
   Its ratio to the terminal lower bound tends to zero because
   `F_4-F_3>0`, even after the cost `h_mu^(-1)=1+mu^2`.
5. The terminal box has time length `h_mu`; derivative bounds apply at
   positive edge coordinates. The decrease of the advected coordinate
   from time `4` is only a fixed multiple of `h_mu`, which changes the
   field by a bounded factor. The fixed cutoff is one on this box
   eventually.
6. The upper payment uses the supremum over the entire plateau and
   interval. The lower payment restricts the integral to an outer strip
   only as a proof step. Its cross-sectional area is bounded below by
   `c a`, and its `z` width is of order `1/a`; these factors cancel.
7. One initial Fourier datum is used for every time in `[0,4R^2]`.
   Neither this proof nor any new corollary substitutes prescribed-time
   inverse-heat witnesses.

## Positivity and quantifiers

The component mass is positive for each nonzero member: a finite
nonzero Fourier sum cannot vanish on an interval, and heat evolution
does not erase its nonzero coefficients. The plateau has positive volume.
The signed flux is positive only eventually along each allowed sequence.
No sequence-independent onset is inferred from convergence without a rate.

The full-velocity mass is strictly positive because the original drift
is nonzero. All logarithmic limits involving the signed flux are taken
after its sequence-dependent positivity threshold. Divergence of the
component quotient needs `mu/log A -> infinity`; the bare assumptions
`mu -> infinity`, `mu/A -> 0` do not imply that divergence.

## Complete-velocity normalization

The shell's spacetime volume is exactly

`V=32 pi delta0 a^2 R^5 (1+delta0^2/(3a^2))`.

The majorant on the full plateau yields `sup |F|=exp(o(L^2))` as an
upper scale, whereas `|B|=beta a/(AR)` is of exponential size
`exp(9L^2/40000+O(1))`. Thus the uniform ratio `sup |F|/|B|` tends
to zero. Consequently

`M_u=(1+o(1))32 pi delta0 beta^3 (a^5/A^3)R^2`.

The two-sided positive `S` and `K` estimates imply
`T=R^3 exp(o(L^2))` and `M_F=R^5 exp(o(L^2))`.
Combining the powers of `R` gives `1/3+3-4/3=2`; hence the full-velocity
quotient is `R^2 exp(o(L^2))` with exact quadratic rate `-9/20000`.
This confirms the due-diligence calculation for the original amplitudes.

The frame change is checked directly, rather than cited from analogy:
`H(t,y)=F(t,y+Bt)` satisfies `H_t=H_yy`; subtracting `B e_2`
leaves `(0,0,H)`. Its radial-window cubic transport flux integrates to
zero in coordinate 3. A fixed window in the new frame is translating
in the old frame, and the kinetic energy also changes on subtracting
the drift. There is no contradiction with the original positive flux.

## Additional boundary results

The new amplitude-rescaling proposition corrects a possible overreading
of the fixed-amplitude decay. For positive flux, its complete-velocity
quotient is nondecreasing in positive amplitude and converges to the
component quotient. The proof is the monotonicity and Minkowski inequality
for `||F^2+(B/lambda)^2||_(3/2)`; dominated convergence gives the
same limit, including zeros of `F`. For `B=0`, equality of the two
denominators holds but the actual radial shear flux is zero.

The explicit scaling `lambda_L=R^(-2)` makes the relative denominator
error at most `R^2 exp(o(L^2))`. Hence full-velocity amplification is
possible for the rescaled family when `mu/log A -> infinity`.
It retains huge drift and does not provide a uniform initial-energy
bound. It is not a general local-energy counterexample.

The bounded-drift proposition retains the same initial shape and proves
decay even after arbitrary amplitude rescaling. Uniform confluence still
holds, the full plateau lower bound survives, and the numerator carries
the additional factor `|B|R`. This excludes bounded-drift amplification
only for this shape and parameter regime. The general matching and
bounded-drift problems remain open; see `research/bounded-routes.md`.

## Finite arithmetic checks

Executed with local `python3` on 2026-09-06 using `fractions.Fraction`:

```python
from fractions import Fraction as F
assert F(1,3)+3-F(4,3) == 2
assert 2*F(-9,40000) == F(-9,20000)
assert F(1,3)+4-F(10,3) == 1
assert F(3)-F(2) == 1
assert 4*F(4,3)*6 == 32
assert 4*F(4,3)*2 == F(32,3)
for k in range(1,101):
    assert 2*k*(k-1)+k == k*(2*k-1)
    assert k*(k-1)+k == k*k
```

Result: six exact scale/volume assertions and 200 integer coefficient
assertions passed. These finite checks guard transcription and arithmetic;
the analytic identities for all degrees are proved above and in the paper.

Assessment: the reviewed application and new consequences are proved at
the level of the supplied analytic arguments. No claim of general
Navier–Stokes regularity, singularity, exhaustive novelty, or human peer
review follows from this audit.
