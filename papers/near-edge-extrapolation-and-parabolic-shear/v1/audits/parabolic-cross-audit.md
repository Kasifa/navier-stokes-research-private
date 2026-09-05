# Independent cross-audit of the parabolic section

Date: 2026-09-05. File inspected: `sections/parabolic.tex`, 555-line version. This audit was carried out independently of the section's author. The displayed proof was checked directly; no old PASS result or numerical certificate was used as a substitute for an argument. Line numbers below refer to that version.

## Disposition

No fatal gap was found in `thm:heat-edge`, `prop:dynamic-confluence`, or `thm:parabolic-shear` as stated. The complete-clock theorem can be included in the paper with its current degree range and its explicit algebraic factors. The extra condition `mu/log A -> infinity` must remain attached to the assertion that the unnormalized quotient diverges. The normalized coefficient-rate conclusion does not need that extra condition.

The scope is narrow and should remain so: one particular even-degree, start-specified Chebyshev family in consecutive integer modes, with constant drift and no uniform bound on the full velocity's energy. This audit does not establish a uniform complete-clock lower bound over all finite-mode shears, a growing-degree theorem for `m` comparable to `A^2`, or a novelty claim.

## Counterexample-oriented checks

### 1. Slow degree growth and the smaller tilt scale (lines 16–129)

A natural possible failure is to subtract two errors of size `o(mu^2)` and mistakenly conclude an error of size `o(mu)`. The proof avoids that problem by tilting the same probability measure.

- The joint regime is equivalent to `mu -> infinity` and `mu/A -> 0`: `mu^3=m^2/A` and `mu/A=(m/A^2)^(2/3)`.
- On substituting `y=mu z`, the exponent is `mu^2 Phi_s(z)+o(mu^2)` locally uniformly, since `m sqrt(mu/A)=mu^2` and the relative error in the arcosh expansion is `O(mu/A)`.
- Direct differentiation gives `z_s=2^(1/3) s^(2/3)` and `Phi_s(z_s)=3 2^(-4/3) s^(1/3)`. Thus the leading constants in lines 30–38 are correct.
- For every fixed epsilon, the unique maximum is uniformly isolated on a compact positive time interval. Uniform convergence of the phase eventually preserves a positive fraction of that gap even when `mu/A` tends to zero arbitrarily slowly. No rate such as `mu^2/A -> 0` is needed.
- The added logarithmic tilt is `c mu z/(2s)`, of order `mu` on compact sets, while the concentration loss is of order `mu^2`. The Gaussian tail dominates this tilt uniformly for bounded positive and negative `c`.
- On the concentration neighborhood, the exact tilt lies between `exp(c z_s mu/(2s) +/- C epsilon mu)`. The complementary tilted integral is exponentially negligible. This establishes the `o(mu)` ratio estimate directly, including negative coordinates. The constant is `G_s=z_s/(2s)=2^(-2/3)s^(-1/3)`.
- A sequence such as `mu=log log A`, which invalidates casual claims that logarithmic algebraic losses are negligible compared with `mu`, still satisfies the proof of both heat-edge limits. The later theorem correctly adds a separate condition when it asserts divergence of the entire quotient.

### 2. The remote negative exterior (lines 113–128)

For `-2A<=y<=0`, the Chebyshev argument lies in `[-1,1]`, so its Gaussian contribution has absolute value at most one. For `y=-2A-u`, parity gives the exterior magnitude `cosh(m arcosh(1+u/A))`. For all bounded `c` and sufficiently large `A`,

`(2A+u+c)^2 >= (A+u)^2`.

Also `m arcosh(1+u/A) <= sqrt(2) mu^(3/2) sqrt(u)`. Young's inequality with powers four and four-thirds gives

`sqrt(2) mu^(3/2) sqrt(u) <= u^2/(8s1) + C mu^2`.

Combining these bounds leaves precisely an integrable `-u^2/(8s1)` term and a negative `-A^2/(4s1)` term. Since `mu=o(A)`, that exterior is negligible even after allowing its entire infinite integration range. It cannot cancel the positive saddle. Positivity of `Q` is therefore established uniformly on the claimed compact time and coordinate sets.

### 3. Positive coefficients and terminal width (lines 132–191)

The recurrence for `D_k=T_m^(k)(1)` follows by differentiating `(1-x^2)T_m''-xT_m'+m^2T_m=0` exactly `k` times. At `x=1` it gives

`(2k+1)D_(k+1)=(m^2-k^2)D_k`.

The double series uses `c^ell s^j A^(-ell-2j)/(ell! j!)`, with derivative order `ell+2j`, and is correct. At a fixed `ell`, the ratio of successive `j` terms is bounded by

`s m^4/[A^2 (j+1)(4j+1)(4j+3)] <= C mu^6/(j+1)^3`.

After `J=C(1+mu^2)` the ratio is at most one half. A geometric tail then bounds the mean index by `J+2`, independently of how irregular the earlier weights are. This proves the logarithmic time derivative bound. The identity `partial_c^2 Q=partial_s Q` is correct under the stated normalization; the moment identity and Cauchy–Schwarz prove the coordinate derivative bound on `c>=c0>0`.

All later uses of this derivative lemma have coordinates bounded away from zero. In particular, `c_-+4 gamma_L` and `delta0+4 gamma_L` are positive fixed-order coordinates. The time window `(1+mu^2)^(-1)` therefore loses only a fixed multiplicative factor. The proof does not require a time interval of fixed positive width.

The majorant uses a genuine bound for all derivatives on `[-1,1]`. The Gegenbauer generating function argument proves it, and parity extends the bound to the negative exterior. Thus it controls earlier times and the full plateau, not only the positive edge saddle.

### 4. Finite-eta transfer and complex evaluation (lines 200–286)

Several sign and growth checks were made independently:

- `w_eta(x)=i/eta+e^(i eta x)/(i eta)`, so the coefficient formula for `b_j` in line 212 has the correct signs.
- Rolle's theorem places every zero of each nonconstant derivative of `T_m` on the real axis. Evaluation at `i/eta` is nonzero. The highest derivative is constant. Hence every one of the `m+1` positive frequencies actually occurs.
- The Fourier identity for conjugating heat by a carrier has the **positive** imaginary shift `+2iMt`. On an individual mode it multiplies the amplitude by `exp(-(M+j eta)^2 t)`, exactly the physical decay `exp(-(m+j)^2 R^2 s)`.
- The real drift is `vs/e_a`, which equals `B R^2 s/(AR)`. It remains in the comparison polynomial and is not discarded with the small imaginary shift.
- The chain rule gives `L_eta=(1+i eta w)^2 D_w^2+i eta(1+i eta w)D_w`. This preserves the degree-at-most-`m` polynomial space. In the coefficient norm with radius four, multiplication by `w` and differentiation have the expected weights; the claimed operator perturbation bound `C eta m^2` follows term by term.
- The Duhamel estimate uses the bound `exp(Ct m^2)` for both semigroups and `||T_m||_4 <= C4^m`. Its exponent therefore contains both `Cm` and `Cm^2/A^2`; neither can silently be dropped.
- For real `|x|<=2`, the real drift is `O(1/A)`, the carrier `M=mAR` tends to zero exponentially, and the imaginary displacement is even smaller. All intermediate evaluation points remain strictly inside the radius-four coefficient disk. The estimates for replacing `w_eta(z)` by `z` therefore apply also to those complex points.
- Since `m=o(A^2)` and `A` is comparable to `L`, both `m` and `m^2/A^2` are `o(L^2)`. Thus the total error is `exp(-9L^2/40000+o(L^2))`, as stated, uniformly for the whole clock.

Optional exposition improvement at lines 249–266: write the semigroup chain-rule identity explicitly,

`e^(t D_x^2)[T_m(w_eta(x))] = (e^(t L_eta)T_m)(w_eta(x))`.

It follows by the finite-dimensional evolution equation, and is already implied by the text's phrase “exact polynomial generator.” Adding it would make the transition to Duhamel immediately checkable. This is not a missing assumption or a blocking defect.

### 5. Complete-clock signed pairing (lines 403–467)

For even `m`, heat preserves the evenness of `T_m`. At the two opposed cap coordinates, the comparison values are exactly

`2 Q(s,r+delta0+gamma_L s)` and `2 Q(s,r+delta0-gamma_L s)`.

The signs of the real drift are correct. Uniform tilt gives a positive logarithmic ratio throughout `3<=s<=4`, including those `r` for which the second coordinate is negative. Both fields are eventually positive there. The exponentially small absolute finite-eta error is negligible compared with both, so it preserves their ordering. Since `W_a` is odd, nonpositive on the positive cap and `v<0`, their paired signed contribution is nonnegative over this entire later interval.

The terminal lower integral retains a fixed radial subinterval of width `2h`, while `dz=dr/a` cancels the `a` size of `W_a`. This yields the factor `(beta/A)(1+mu^2)^(-1)`, not an extra factor of `a`.

The sign on earlier times need not be known. The global majorant bounds its total absolute contribution by `(C beta/A) Q(3,C1)^2`. The terminal value has leading logarithmic gain `(F4-F3)mu^2`, which dominates the inverse terminal width `1+mu^2`. Consequently the early integral cannot reverse the final positive sign. No part of `[0,4]` is omitted from the signed flux.

### 6. Full plateau and dimensional factors (lines 367–401, 469–531)

The full velocity flux reduces exactly to the oscillatory-component flux: the term with `partial_3 phi_L` integrates to zero in `x3`, and the constant `B^3 partial_2 phi_L` term integrates to zero on the torus. Thus the numerator used here agrees with the reduced flux defined in the upper-bound section.

The exact dimension changes are

`T_L=(a^2 R^3/2) S`, and `M_L=a R^5 K`.

For the upper plateau payment, the projection has `|x|<=1+2delta0/A`; adding the maximal transport gives the coordinate `c_p+4 gamma_L`. The entire cross-sectional area is at most `4 pi a delta0`, over an interval of bounded `z` length, so `K<=Ca Q(4,c_p+4gamma_L)^3` includes both outer caps and the full clock.

For the lower payment, the strip in lines 485–487 lies genuinely inside the outer half of the plateau. There, `a z=a+c-delta0` is between `a` and `a+delta0/2`. Its area is at least `pi a delta0`; multiplying by `dz=dc/a` cancels this `a`. Hence `K>=c h_mu Q(4,delta0+4gamma_L)^3` has the correct algebraic factor. It is only a lower bound on the full denominator, which is sufficient for the upper quotient estimate.

The exact quotient is

`R^(1/3) T_L/M_L^(2/3) = (a^(4/3)/2) S/K^(2/3)`.

Combining the two payments gives, respectively, `beta a^(2/3)/(A(1+mu^2))` and `beta a^(4/3)(1+mu^2)^(2/3)/A`. The exponent difference in the lower bound is `2 G4 Delta_c mu=2^(-1/3)Delta_c mu`. All powers and this constant agree with the theorem.

### 7. Divergence and normalization (lines 348–360, 518–542)

The algebraic factors have logarithms of size `O(log A)` because `mu=o(A)`. Therefore an assertion that the complete unnormalized logarithm is `Theta(mu)` needs `log A=o(mu)`. The current statement includes that restriction exactly where needed. Without it the displayed two-sided estimates, eventual positive flux, and normalized rate remain valid, but unnormalized divergence is not concluded.

The normalization identity is exact:

`X_L/p_L^(2/3)=omega^(1/3) R^(1/3) T_L/M_L^(2/3)`.

The remaining quotient has logarithm squeezed between terms of size `O(mu+log A)=o(L^2)`. Thus its normalized logarithmic contribution is zero, and `omega=exp(-2L^2/3969)` supplies exactly `-2/11907`. This argument works for the full degree range in the statement.

## Integration advice

- Keep the even-degree hypothesis, the fixed positive drift parameter `beta`, and the cutoff positive on an outer cap.
- Keep the distinction between the oscillatory-component payment and the full velocity's cubic mass.
- Preserve the explicit algebraic prefactors and the `mu/log A` condition; they prevent a false claim for very slowly growing degrees.
- Treat the heat-edge proof and finite-eta transfer as analytic results. Finite numerical samples would add illustrations but are unnecessary to justify these statements.
- The main theorem is ready for integration with the upper and fixed-slice sections, subject to the parent task's final notation and compilation checks.
