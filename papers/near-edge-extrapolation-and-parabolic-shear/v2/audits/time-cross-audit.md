# Independent mathematical audit of the time-weighted section

Date: 2026-09-06. Reviewer: the quantitative-edge subagent, which did not author `sections/time-weighted.tex`. This is an independent automated mathematical review within this task, not human peer review.

Audited source: `sections/time-weighted.tex`, SHA-256 `8b59ed97145ac07a710b87dbc6c964f9b974009ea97d6e5d4d6d43bf11bcb7ae`.

Result: **PASS; no mathematical correction required.** The explicit constant, scope of the literature inputs, all endpoint cases requested in the revision brief, and the final time rescaling have been checked.

## Primary-source check

I independently read the locally cached original HTML `/tmp/paper-edge-literature/Erdelyi2017.html`, obtained by the literature agent from [Erdélyi, arXiv:1602.02315v1](https://arxiv.org/html/1602.02315v1). The content SHA-256 is recorded in `literature/source-metadata.json`; the external source is not redistributed in this package.

- The Introduction defines E_n using complex coefficients and complex exponents, and E_n^- by nonpositive real parts.
- Theorem 3.1 states the weighted infinite-to-finite range inequality on [0,9n], with squared norm factor 1+8190 exp(−n/10). This is at most 8191.
- Lemma 12.5 applies to all E_n and gives the squared midpoint estimate n/δ times the L² integral on [y−δ,y+δ]. With δ=1, the length is two and the coefficient is n, as used in the revision.

For F(t)=e^t f(t), its exponents are 1−ζ_j, whose real parts are nonpositive under Re ζ_j≥1. Thus Theorem 3.1 gives J=∫e^t|f|²≤8191e^(9N)I_(9N). For h(t)=e^(t/2)f(t), Lemma 12.5 gives e^t|f(t)|²≤N J for t≥1. No upper bound on Re ζ_j or restriction on imaginary parts appears in either substitution. Coincident exponents can be merged; retaining the original N only weakens the bound.

## Mixed norm and explicit upper constant

The identity k(t)^(2/3)=|| |f(t,·)|² ||_(L^(3/2)(E)) gives the correct norm at each application of Minkowski. Hölder on [0,9N] yields ||I_(9N)||_(3/2)≤(9N)^(1/3)K_T^(2/3) for T≥36N. The tail integral of t exp(−t) from S to infinity is exactly (S+1)exp(−S). Hence the tail coefficient divided by N^(4/3) is

\[
 8191\,9^{1/3}(36N+1)e^{-27N}.
\]

The factor (36N+1)e^(−27N) decreases for N≥1 since its logarithmic derivative is 36/(36N+1)−27<0. At N=1 the displayed quantity is below one. An entirely elementary strict bound is 8191<2^13, 9^(1/3)<2², 37<2^6, and e^27>2^27, so the quantity is below 2^(21−27)<1. No numerical estimate is needed.

The initial interval uses Hölder with exponents 3 and 3/2, giving 4^(−1/3)(36N)^(4/3)K_T^(2/3). Thus C_*=4^(−1/3)36^(4/3)+1 is valid. For T<36N the initial argument covers the entire integral. K_T=0 causes no division in the upper proof and yields zero on the left as well.

## Exact lower witness

Expanding w(t)^k with the binomial theorem gives

\[
 b_j=(-1)^j\sum_{k=j}^{N-1}\frac{\binom{k}{j}}{k!\epsilon^k}
 =\frac{(-1)^j}{j!\epsilon^j}\sum_{h=0}^{N-1-j}
                    \frac1{\epsilon^h h!}.
\]

Every inner summand is positive, so every coefficient is nonzero. Since ε=N^(-2)>0, the N decay rates 1+jε are distinct. The upper endpoint satisfies (N−1)/N²≤1/4, equivalent to (N−2)²≥0. Therefore all rates belong to [1,5/4] for every N≥1.

For 0≤t≤N/2, integration of 1−e^(−εu)≤εu gives t−w(t)≤εt²/2≤1/8. The Poisson Markov estimate P(X≥N)≤w/N≤1/2 gives f_(0,N)(w)≥1/2. Consequently f_N≥(1/2)e^(−1/8)>1/4 on this interval. Since w≤t, termwise comparison gives 0<f_N≤f_(0,N)(t)≤1 on all t≥0. The cubic mass therefore lies in (0,N], and the numerator is at least (1/16)∫_0^(N/2)t dt=N²/128. Division gives the claimed N^(4/3)/128.

At N=1, ε=1, b0=1 and f1=e^(−t); every step remains valid. Scaling by K_N^(−1/3) gives unit cubic mass and preserves the quotient because numerator and denominator both scale quadratically. No assumption of uniformly bounded coefficients has been introduced; the abstract class permits the explicit large coefficients.

## Rescaling and claim boundary

For rates with real parts at least λ>0, setting t=λs transforms the cubic mass to λH and the weighted integral to λ²∫s h(s)^(2/3)ds. Therefore λ∫η(s)h(s)^(2/3)ds is at most C_*C_ηN^(4/3)λ^(−1/3)H^(2/3), exactly as written.

The order witness uses nearby real rates, not the squared integer rates together with spatial constraints of the shear family. It proves abstract temporal order optimality only. The section correctly declines claims about q^7 flux optimality, a sharp exponential constant, a dynamical transition, or a new literature-independent upper bound.

## Supplementary finite algebra check

A Python standard-library `fractions.Fraction` check compared the two coefficient formulas exactly for every j and N=1,…,32: all 528 coefficients agreed and were nonzero; the rate interval also passed for all 32 N values. This is an implementation cross-check only. The binomial derivation above is the proof for all N.

Reproduction core:

```python
from fractions import Fraction
from math import comb, factorial
for N in range(1, 33):
    eps = Fraction(1, N*N)
    for j in range(N):
        direct = sum(Fraction((-1)**j*comb(k,j), factorial(k))/eps**k
                     for k in range(j, N))
        formula = (Fraction((-1)**j, factorial(j))/eps**j
                   * sum(Fraction(1, factorial(h))/eps**h
                         for h in range(N-j)))
        assert direct == formula and formula != 0
    assert 1 + Fraction(N-1, N*N) <= Fraction(5, 4)
```
