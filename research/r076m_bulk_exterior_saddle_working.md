# R0.76M working note -- bulk-exterior saddle for the ideal heat polynomial

Status: **WORKING ANALYTIC DERIVATION; independent review and literature
collision check pending.** This note is not a frozen release and is not
part of the R0.76L-Step63 handoff.

## 1. The next question

R0.76L closes its explicit family in the window sqrt(A) << m = o(A^2).
Its Section 10 predicts a different saddle at m comparable with A^4.
The first task is to prove that prediction for the ideal forward heat
polynomial before attempting the exact integer-shear transfer.

Let m be even, let A tend to infinity, and suppose

\[
 \frac m{A^4}\longrightarrow\kappa\in(0,\infty).
\]

Retain the ideal object from R0.76L L.14--L.16,

\[
 Q_{m,A}(s,c)=
 \frac1{\sqrt{4\pi s}}\int_{\mathbb R}
 T_m\left(1+\frac yA\right)e^{-(y-c)^2/(4s)}\,dy.
\]

All estimates below are uniform for s in a fixed compact interval
[s_0,s_1] contained in (0,infinity), c in a fixed bounded real interval,
and m/A^4 in a fixed compact subinterval of (0,infinity).

The provisional conclusions are

\[
 Q_{m,A}(s,c)=
 \left(\frac1{2\sqrt2}+o(1)\right)
 e^{\Phi_{s,c}(Y_{s,c})},
 \qquad
 \Phi_{s,c}(y)=m\operatorname{arcosh}(1+y/A)
             -\frac{(y-c)^2}{4s},\quad y>0,
\]

where Y is the unique positive critical point of this phase, and

\[
 \frac{Y_{s,c}}{A^2}\longrightarrow\sqrt{2s\kappa},
 \qquad
 \frac1{A^2}\log\frac{Q_{m,A}(s,c_2)}{Q_{m,A}(s,c_1)}
 \longrightarrow(c_2-c_1)\sqrt{\frac{\kappa}{2s}}.
\]

These statements concern the ideal heat polynomial at fixed positive
scaled times. They do not establish an exact integer-shear estimate,
complete-clock signed flux, or full-plateau payment.

## 2. Exact saddle equation and strict concavity

For y>0,

\[
 \Phi'_{s,c}(y)
 =\frac{m}{\sqrt{y(y+2A)}}-\frac{y-c}{2s},
\]

and

\[
 \Phi''_{s,c}(y)
 =-\frac{m(y+A)}{[y(y+2A)]^{3/2}}-\frac1{2s}
 <-\frac1{2s}.
\]

The derivative tends to positive infinity as y decreases to zero and
to negative infinity as y tends to infinity. Therefore there is exactly
one positive critical point Y, and it is the global maximum. It satisfies
Y>c and

\[
 (Y-c)\sqrt{Y(Y+2A)}=2sm.
\]

This is the saddle of the positive exponential component of the
Chebyshev cosine-hyperbolic formula. It is not being identified with the
finite-m saddle of the full cosine-hyperbolic integrand.

Put K=sqrt(2sm). For each fixed epsilon in (0,1), evaluate the left side
of the saddle equation at (1-epsilon)K and (1+epsilon)K. Since A/K tends
to zero and c/K tends to zero, its ratio to K^2 tends respectively to
(1-epsilon)^2 and (1+epsilon)^2, uniformly in the stated compact ranges.
Strict monotonicity for y>max(c,0) then gives Y/K tending to one.

For c=0 the equation has the exact squared form

\[
 Y^3(Y+2A)=4s^2m^2.
\]

The squared equation is used only together with Y>0 and the positive
unsquared equation, so it introduces no extraneous branch.

## 3. The centered integral has a Gaussian limit

For each bounded real r,

\[
 \Phi''_{s,c}(Y+r)\longrightarrow-\frac1s.
\]

Indeed Y is asymptotic to sqrt(2sm), A/Y tends to zero, and
m/Y^2 tends to 1/(2s). Taylor's formula and Phi'(Y)=0 give

\[
 \Phi_{s,c}(Y+r)-\Phi_{s,c}(Y)
 \longrightarrow-\frac{r^2}{2s}.
\]

Strict concavity also gives a global bound, valid whenever Y+r>0,

\[
 \Phi_{s,c}(Y+r)-\Phi_{s,c}(Y)
 \le-\frac{r^2}{4s}\le-\frac{r^2}{4s_1}.
\]

Extend the centered integrand by zero for r<=-Y. The bound is integrable
on the real line. Dominated convergence, with a compact-parameter
subsequence argument for uniformity, proves

\[
 e^{-\Phi_{s,c}(Y)}
 \int_0^\infty e^{\Phi_{s,c}(y)}\,dy
 =\sqrt{2\pi s}+o(1).
\]

This argument also supplies uniform exponential moments for bounded
tilts of r, because exp(C|r|-r^2/(4s_1)) is integrable. Unlike the edge
regime, the centered physical y-width is of order one here; the saddle
location itself grows like A^2.

## 4. Recovering the complete ideal heat polynomial

On y>=0, write

\[
 T_m(1+y/A)
 =\frac12 e^{m\operatorname{arcosh}(1+y/A)}
  +\frac12 e^{-m\operatorname{arcosh}(1+y/A)}.
\]

After the Gaussian normalization, the integral of the second term is
at most 1/2. The first term has the leading coefficient

\[
 \frac{\sqrt{2\pi s}}{2\sqrt{4\pi s}}=\frac1{2\sqrt2}.
\]

Its phase tends to positive infinity uniformly. For example, evaluating
the phase at y=A^2 gives a term of size m log A, whereas the Gaussian
penalty is of order A^4. With m/A^4 bounded above and below by positive
constants, the first term grows faster than any fixed exponential in
A^4.

On the middle interval -2A<=y<=0, the Chebyshev argument is in [-1,1],
so the absolute normalized contribution is at most one.

On the remaining interval write y=-2A-u with u>=0. Since m is even,
the Chebyshev factor equals T_m(1+u/A). Its Gaussian kernel relative to
the positive-u kernel is exactly

\[
 \exp\left(
 -\frac{(u+2A+c)^2-(u-c)^2}{4s}
 \right)
 =\exp\left(-\frac{(A+c)(A+u)}s\right).
\]

For bounded c and sufficiently large A this is at most
exp(-A^2/(2s_1)), uniformly in u>=0. The left-exterior contribution is
therefore exponentially small relative to the positive-exterior one.
The bounded middle contribution is also negligible. These estimates
yield the provisional Q asymptotic in Section 1 and eventual positivity.

## 5. The coordinate ratio without subtracting large numerics

Define the maximal phase V(s,c)=Phi_{s,c}(Y_{s,c}). The critical point
is smooth in c because Phi'' is strictly negative. Differentiation at
the maximum gives the exact envelope identity

\[
 \partial_c V(s,c)=\frac{Y_{s,c}-c}{2s}.
\]

Consequently,

\[
 V(s,c_2)-V(s,c_1)
 =\int_{c_1}^{c_2}\frac{Y_{s,c}-c}{2s}\,dc.
\]

The uniform saddle limit gives the ratio law in Section 1 after division
by A^2. The prefactor 1/(2sqrt(2)) cancels, and the uniform relative
o(1) remainder contributes o(1) to the logarithmic difference. This
avoids subtracting two numerical values of order A^4 log A to extract
a difference of order A^2.

At s=4 and a positive fixed gap Delta_c, the ideal squared ratio has
coefficient

\[
 \frac1{A^2}\log
 \left(\frac{Q_{m,A}(4,c+\Delta_c)}{Q_{m,A}(4,c)}\right)^2
 \longrightarrow\Delta_c\sqrt{\frac\kappa2}.
\]

This is the ideal fixed-time mechanism behind R0.76L L.71. It does not
yet justify using that coefficient for physical signed flux divided by
full spacetime plateau mass.

## 6. Remaining gates before a research release

1. Review the uniformity and the complete-polynomial remainder argument,
   and check primary-source overlap for this bulk asymptotic.
2. Obtain terminal-time control with a time width of order 1/m, using
   the positive terminating heat series and its exact moment bound.
3. Replace the earlier coarse fixed-radius coefficient-norm transfer:
   at m comparable with A^4 its exp(Cm) factor overwhelms the available
   exponentially small frequency spacing. A new relative estimate is
   required; the smallness of eta*m alone does not prove it.
4. Check the real part, carrier, negative-cap pairing, adverse early
   times, and the full physical plateau before drawing a conclusion
   about the normalized Navier--Stokes quantity.
5. Produce the required finite checks and independent analytic audit,
   then decide whether the candidate threshold survives. Only a
   completed research freeze will be handed to the publication task.

No DGX job is needed for this first analytic step. Directly sampling
enormous Chebyshev values would obscure the coordinate ratio and would
not resolve the missing exact-shear estimate. **NOT CLAY.**
