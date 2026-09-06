# Bounded exploration of dynamic matching and drift normalization

Date: 2026-09-06. Status: analytic consequences completed; the general
matching and alternative-profile questions are left open at the stopping
point below. No large simulation was needed. This note concerns exact
linearizable shear families, not general Navier–Stokes regularity.

## Fixed initial datum and the comparison that is actually available

Write `mu=(m^2/A)^(1/3)`, with `mu -> infinity` and `mu/A -> 0`.
The same initial Chebyshev-confluent packet over the whole observation
interval obeys

`c beta a^(2/3)/(A(1+mu^2)) exp((2^(-1/3)Delta_c+o(1))mu)`

`<= R^(1/3) T/M_F^(2/3)`

`<= C beta a^(4/3)/A (1+mu^2)^(2/3) exp(Cmu)`.

The uniform estimate over all dyadic packets instead has the exponential
scale `exp(C q/sqrt(A))`; for the current `q=m+1`, this is
`exp(C mu^(3/2))`. The gap between `mu` and `mu^(3/2)` is not a
polynomial prefactor and cannot be closed by optimizing the displayed
powers of `a` and `mu`.

The known spatial witness realizes a chosen observation time by choosing
its initial data to include an inverse-heat factor. Repeating that at
different times changes the initial data. It does not give a lower bound
for one trajectory's complete signed integral with the same full plateau.
No such substitution is used in this revision.

One can make the family estimates more precise with a separate boundary
Laplace analysis of the cutoff and plateau weights. That would require
the cutoff's exact behavior near the outer end of its support; a smooth
compactly supported cutoff can vanish to arbitrarily high order there.
It would still describe this family, not attain the uniform
`mu^(3/2)` exponent. This route was therefore not pursued as a proposed
proof of general dynamic optimality.

## Complete velocity: a closed amplitude-scaling observation

For any fixed nonzero shear with positive flux, let `V` be its finite
spacetime observation volume. Replacing the one initial datum by
`lambda F(0)` gives `lambda F(t)` at every time because the scalar
evolution is linear. Flux scales by `lambda^2`; component cubic mass
scales by `lambda^3`. Hence the component quotient is unchanged.

For the complete velocity, after removing `lambda^3` from the mass,
the denominator's two-thirds power is

`D(lambda)=||F^2+(B/lambda)^2||_(L^(3/2))`.

Pointwise monotonicity and Minkowski give the complete proof:

`M_F^(2/3) <= D(lambda) <= M_F^(2/3)+(B/lambda)^2 V^(2/3)`.

Thus the full-velocity quotient is nondecreasing in `lambda`, is at most
the component quotient, and is at least that quotient divided by
`1+(B/lambda)^2(V/M_F)^(2/3)`. It tends to the component quotient.
Zeros of `F` cause no difficulty: for `lambda>=1`, dominated convergence
uses the integrable bound `(F^2+B^2)^(3/2)`. The result includes `B=0`
as equality of denominators; the radial transport flux is then zero.

For the explicit family, `V=R^5 exp(o(L^2))`,
`M_F=R^5 exp(o(L^2))`, and `|B|=R^(-1)exp(o(L^2))`.
The fully specified choice `lambda_L=R^(-2)` therefore makes the
denominator error factor `R^2 exp(o(L^2)) -> 0`.
If `mu/log A -> infinity`, the scaled full-velocity quotient diverges
with the component quotient. This is a fixed initial datum for each
member of the sequence; it is not a new datum at every time.

This result must accompany the original-amplitude full-velocity decay:
that decay is normalization dependent. The amplitude rescaling retains
`|B|~1/R`, and the global initial energies are not uniformly bounded.
It neither removes constant transport nor contradicts the stated
frequency-dependent component upper estimate or a general local-energy
theorem. Its role is to describe the denominator accurately.

## Bounded drift: a closed negative result for this shape

Now keep the same initial coefficients but let `|B_L|<=B_*` be bounded.
Allow any overall amplitude factor, which will cancel from the component
quotient. In the rescaled polynomial coordinate, advection shifts the
argument by `B_L R s/A`, rather than an amount of order `1/A`.
The degree-dependent transfer estimate is unchanged because its real
argument remains in a smaller fixed disk.

The exact cross section and `integral |W_a| <= C` give

`|T_L^(B)| <= C |B_L| a R^4 Q(4,C_1)^2`.

Choose the positive or negative outer plateau strip so that advection
increases its ideal edge coordinate. For even `m`, parity permits either
choice. On the terminal time interval of length
`h_mu=(1+mu^2)^(-1)`, the coordinate is at least `delta0`.
The positive heat series, terminal derivative bounds, and exponentially
small transfer error give

`M_F,L^(B) >= c a R^5 h_mu Q(4,delta0)^3`.

Only this proof step restricts integration: the observation remains the
whole plateau and full time interval. The uniform edge-ratio theorem
gives `Q(4,C_1)/Q(4,delta0) <= exp(Cmu)` after enlarging `C`.
Combining the two estimates proves

`R^(1/3)|T_L^(B)|/(M_F,L^(B))^(2/3)`

`<= C |B_L| R a^(1/3)(1+mu^2)^(2/3) exp(Cmu) -> 0`.

The final limit follows from `log R=-9L^2/40000`, `mu=o(L)`, and
`log a=O(log L)`. If `B_L=0`, the exact flux formula is identically
zero. For arbitrary positive amplitude rescaling the component quotient
is unchanged; replacing its denominator by the full velocity can only
decrease its absolute quotient. The conclusion therefore survives both
changes. This proves the bounded-drift proposition in the manuscript.

The pair-dominance argument from the original family cannot be reused
unchanged in this regime. Its edge separation is now
`2|B_L|Rs`, and the fixed positive coefficient of `mu` disappears.
The new argument above uses an absolute numerator bound, not an
unjustified limiting sign claim.

## Stopping record and open questions

Completed within this bounded exploration:

- The Galilean frame calculation and original-amplitude complete-velocity
  rate `-9/20000`.
- A quantitative amplitude-rescaling theorem, including the explicit
  `lambda_L=R^(-2)` full-velocity amplification consequence.
- A bounded-drift decay theorem for the same initial shape and degree
  window, valid under arbitrary amplitude rescaling.

Not proved:

- A matching upper and lower bound for the complete signed observable
  over all dyadic Fourier packets with one initial datum per trajectory.
- An alternative initial shape attaining comparable amplification with
  bounded drift, or a theorem excluding every such shape.
- Uniform initial-energy, general suitable-weak-solution, regularity,
  singularity, or high-degree statements outside `m=o(A^2)`.

Concrete obstacles are the gap in heat-evolved exponential scale, the
dependence of terminal spatial asymptotics on the cutoff shape, and the
loss of a fixed cap-tilt coefficient under bounded drift. No numerical
experiment can remove these proof obligations. Exploration stops here;
none of these unresolved problems blocks the proved error-bound and
finite-family revision objectives.
