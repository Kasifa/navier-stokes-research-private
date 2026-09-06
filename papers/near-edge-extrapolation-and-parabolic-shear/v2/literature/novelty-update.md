# Bounded primary-source novelty update

Checked 2026-09-06 for the isolated v2 revision, starting from source commit
`0a212f4e140e0c9875e740cb8ee23be32a5c05dd`. This is an automated literature
audit, not human peer review or an exhaustive priority search. The task brief,
due-diligence report, v1 heat-edge proof and v1 source audit were read.

## Assessment to use in the manuscript

The polynomial heat operator, Chebyshev identities, Laplace's method and
Gaussian exponential tilting are established objects and methods. The spatial
extrapolation estimate is an attributed input. The time-weighted upper bound
is a direct corollary of existing exponential-sum inequalities. The explicit
lower witness completes the order statement for the abstract time class; its
particular formula is not presented as a priority claim.

The potentially additional content is the *combination of quantifiers* in the
joint heat-edge regime: a checkable common-amplitude error, a separately
controlled smaller displacement ratio, uniformity over positive compact time
intervals and bounded signed displacements, and a verified second polynomial
family. Transfer to one initial datum throughout the full time interval is a
separate application. None of the sources verified below states that same
combination. This finding does not rule out a more general theorem elsewhere.
The error order proved in v2 must not be called best possible without an
additional lower-error argument.

## Heat polynomials and operational formulas

- **Hile--Stanoyevitch (2001), Theorem 1 and (2.18), pp. 7--8.** Their operator
  is a finite sum of spatial derivatives with continuous time-dependent
  coefficients. The theorem constructs polynomial solutions for monomial
  initial data; without a zeroth-order term the expansion is finite. Constant
  coefficients give polynomial dependence on space and time. By linearity
  this includes heat evolution of any fixed Chebyshev polynomial. It supplies
  the object's history, not a degree-dependent uniform endpoint asymptotic.
  [Primary journal PDF](https://ejde.math.txstate.edu/Volumes/2001/28/hile.pdf).

- **Batahan--Shehata (2014), Theorem 3.1, (3.5), p. 54.** In their convention,
  the displayed operator is
  \(H U_n(x)=\exp(-D_x^2/4)U_n(2x)\), using second-kind Chebyshev polynomials.
  Thus there is a direct Hermite--Chebyshev operational predecessor, with a
  fixed negative heat parameter and scaled variable. Their finite identities
  do not state a joint degree/heat/endpoint limit or its displacement error.
  This sign difference is a precise comparison, not a claim that positive
  heat evolution is a new object.
  [Primary journal PDF](https://scientificadvances.co.in/admin/img_data/849/images/%5B4%5D%20JMSAA%207100121348%20S.%20Raed%20Batahan%20and%20A%20Shehata%20%5B47-59%5D.pdf).

- **Khan (2019), (1.1), (3.1), Theorem 3.1/(3.5), pp. 84, 88--89.** The paper
  prints a two-variable operational formula involving
  \(\exp((y/4)D_x^m)U_n(2x)\). However its printed definitions are inconsistent
  already at \(m=2,n=1\): (1.1) gives \(H_1^{(2)}(x,y)=x\), so (3.1) gives
  \(H U_1^{(2)}(x,y)=2x\), whereas (3.5) gives \(4x\). This was checked on
  rendered publisher pages, not inferred from garbled text extraction.
  Consequently do not import (3.5) as a verified identity, or equate its
  printed family to the v2 family without repairing conventions. It remains
  relevant bibliographic history. A finite heat expansion should be proved
  directly in v2. No joint heat-edge asymptotic is stated in this source.
  [Primary journal PDF](https://www.technoskypub.com/wp-content/uploads/2023/09/3-V2N2-P3-W-Certain-results-for-the-Hermite.pdf).

The standard identities for \(T_n\) and \(U_n\), including their normalization,
are [DLMF (18.5.1)--(18.5.2)](https://dlmf.nist.gov/18.5). In particular,
\(T_n(\cosh\theta)=\cosh(n\theta)\) and
\(U_n(\cosh\theta)=\sinh((n+1)\theta)/\sinh\theta\).

## Terminating hypergeometric comparison

**DLMF §16.11.** Equations (16.11.1), (16.11.3) give the exponential factor
\(\exp(\kappa z^{1/\kappa})\), \(\kappa=q-p+1\). For the fixed-parameter
\({}_0F_2\) comparison, \(\kappa=3\). Subsection (ii) expressly excludes
nonpositive integer upper parameters and treats \(p\le q+1\). Our terminating
\({}_4F_2\) has such a parameter and \(p=q+2\); that subsection does not
apply to it. Subsection (iii), (16.11.10)--(16.11.11), instead has a fixed
argument and specified common positive shifts of upper/lower parameters.
These are not the four oppositely growing upper parameters and vanishing
argument here. See also [§16.2(iv)](https://dlmf.nist.gov/16.2) on the
terminating \(p>q+1\) case.
[Primary reference](https://dlmf.nist.gov/16.11).

The following is a direct algebraic comparison, not a theorem attributed to
DLMF. For \(\mu^3=m^2/A\), the endpoint identity is

\[
 Q_{m,A}(s,0)={}_4F_2\left(-m/2,(1-m)/2,m/2,(m+1)/2;
                 1/4,3/4;s/A^2\right).
\]

It follows by applying the endpoint derivative recurrence in v1 to the finite
heat series. Relative to the \(j\)-th coefficient of
\({}_0F_2(;1/4,3/4;s\mu^6/16)\), its coefficient is multiplied by

\[
 R_{m,j}=\prod_{k=0}^{2j-1}\left(1-\frac{k^2}{m^2}\right),
 \qquad 0\le2j\le m.
\]

For \(2j\le m/2\), the elementary logarithm estimate gives

\[
 \log R_{m,j}=-\frac{(2j-1)2j(4j-1)}{6m^2}
               +O(j^5/m^4).
\]

At \(j\asymp\mu^2\), \(j/m\asymp\sqrt{\mu/A}\to0\), but the logarithmic
coefficient loss is of size \(\mu^3/A=\mu^2(\mu/A)\). It may diverge in the
stated regime. Therefore coefficient confluence does **not** justify claiming
that the two entire sums have ratio tending to one. The leading model
exponent is \(3(s\mu^6/16)^{1/3}\); this explains the amplitude constant
without proving the needed terminating-series uniform estimate or the
smaller displacement ratio.

**Nearby uniform asymptotics checked.** Paris, arXiv:1809.08794v2, §2, studies
\({}_2F_1(a+\epsilon\lambda,m;c+\lambda;x)\), \(\epsilon>1\), fixed positive
integer \(m\), near a saddle/pole transition. Paris, arXiv:2004.01945v2, §2,
allows real fixed \(b>0\) in place of \(m\), with \(0<x<1\) and a
saddle/endpoint transition near \(\epsilon x=1\). Their specific Gauss
families and parameter paths do not match this terminating \({}_4F_2\).
They document that uniform saddle analysis is standard; no exclusion claim
about all transformations or all generalized hypergeometric literature follows.
[2018 primary text](https://arxiv.org/pdf/1809.08794v2),
[2021 primary text](https://arxiv.org/pdf/2004.01945v2).

## The time upper bound: precise imported statements

Use explicit **arXiv v1 numbering**, rather than unverified journal numbering.
Erdélyi's introduction defines \(E_n^-\) by complex coefficients and exponents
with \(\Re\lambda_j\le0\). Theorem 3.1 gives

\[
 \int_0^\infty |g|^2e^{-t}\,dt
 \le (1+8190e^{-n/10})\int_0^{9n}|g|^2e^{-t}\,dt,
 \quad g\in E_n^-.
\]

Lemma 12.5 applies to **all** complex exponential sums \(E_n\):

\[
 |h(y)|^2\le(n/\delta)\int_{y-\delta}^{y+\delta}|h(t)|^2\,dt.
\]

No frequency separation, bounded imaginary parts, or upper real-part bound
is required. Repeated exponents can be merged; applying the bound with the
original larger \(N\) is harmless.
[Primary text, introduction, Theorem 3.1 and Lemma 12.5](https://arxiv.org/html/1602.02315v1).

Here is the manuscript-specific deduction, independently checked. Put
\(g=e^tf\) and \(h=e^{t/2}f\), where
\(f=\sum c_j e^{-\zeta_jt}\), \(\Re\zeta_j\ge1\), and let
\(I=\int_0^{9N}|f|^2\). Then

\[
 J=\int_0^\infty e^t|f|^2\le8191e^{9N}I,
 \qquad |f(t)|^2\le Ne^{-t}J\quad(t\ge1).
\]

For \(k(t)=\int_E|f(t,z)|^3d\nu\), \(K_T=\int_0^Tk\), Minkowski and Hölder
give \(\|I\|_{3/2}\le(9N)^{1/3}K_T^{2/3}\) when \(T\ge36N\). Splitting at
\(S=36N\), the initial interval contributes at most
\(4^{-1/3}S^{4/3}K_T^{2/3}\); the tail contributes at most

\[
 8191N(9N)^{1/3}(36N+1)e^{-27N}K_T^{2/3}.
\]

For \(T<36N\) only the initial Hölder estimate is needed. Thus an absolute
constant works (even \(76N^{4/3}\) is sufficient). This is a literature
corollary with a direct mixed-norm deduction, not an independent new upper
inequality. The elementary truncated exponential witness in the brief shows
order sharpness only in the abstract exponential class. Its incomplete-gamma
identity is standard [DLMF (8.4.10)--(8.4.11)](https://dlmf.nist.gov/8.4).

## The spatial input and constant

Zhang's arXiv:2607.10501v1 Theorem 1.1 and Proposition 4.2/(23) concern
at most \(N\) real frequencies and complex coefficients, with repetitions
merged and no separation condition. Norms here are unaveraged. For
\(0\le d\le1\),

\[
 |g(1+d)|\le\sqrt{9A_{\rm fr}/2}\,N
 e^{3\sqrt2N\sqrt d}\|g\|_{L^2[-1,1]},\qquad A_{\rm fr}\le8191.
\]

The prefactor is below \(192N\). Reflection supplies the left edge; an affine
interval change must retain its length factor. The all-\(x\ge1\) statement
has a different polynomial prefactor. Propositions 7.1 and 8.4 contain the
confluent Chebyshev point and exterior-energy witnesses. They should be
attributed as antecedents, not counted again as separate principal results.
For \(q\) real positive modes, count \(2q\) complex branches. Cite this source
as a preprint.
[Primary text](https://arxiv.org/html/2607.10501v1).

## Remaining risk and stop condition

The exact required sources and their coverage gaps have been checked. Two
focused terminating-hypergeometric search rounds and follow-up verification
returned adjacent Gauss hypergeometric asymptotics, not a matching theorem.
Exact-phrase searches are weak evidence because notation and terminology
vary. MathSciNet/zbMATH citation tracing, full verification of Luke's book,
and a domain expert's review remain outside this bounded audit. No claim of
being first, exhaustive coverage, or publication readiness is warranted.
The next useful step is to prove and independently audit the specific v2
estimates, then compare their final hypotheses against this table.

## Abstract and contribution audit at the revision checkpoint

The current v2 abstract, introduction, quantitative theorem statement,
frame/mass propositions and discussion were compared on 2026-09-06. The
abstract places the two-scale quantitative estimate first, labels the error
orders nonoptimal, and confines the temporal order lower bound to the abstract
class. The introduction attributes spatial extrapolation and polynomial heat
evolution and expressly avoids a priority claim. The second-kind effective
degree and endpoint normalization agree with the theorem statement. The
amplitude-rescaling qualifier agrees with the full-velocity discussion.
No unsupported firstness, universal flux optimality, or general NS-regularity
claim was identified in that snapshot. This is a claim/attribution review;
the analytic proof and numerical checks require their separate audits.

Snapshot SHA-256 values:

```
main.tex: 4224cf8230b8249ea433e53d64591faea8b60e02096bfdd8270ff2295d2046ff
sections/quantitative-edge.tex: db6888129f5481720b48b68fc0e5dd9cba322cd6cfe7f27f9403692b17ab7f4e
sections/discussion.tex: d60679ece457e695ace2693af05f5a69a6e5473f287afdb810d7077c65f68c18
sections/frame-and-mass.tex: 5543032f29cbf3b5b580cbe39c71103d24859c122008bd0813149aa9b806e50d
```

The discussion's statement that separate automated reviews checked the new
proofs is a delivery condition: it is justified only once those review
artifacts exist and any reported issues are resolved. It is not evidence
provided by the literature search itself.
