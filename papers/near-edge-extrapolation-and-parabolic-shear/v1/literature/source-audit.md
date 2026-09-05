# Source audit

Checked on 2026-09-05. This is a bounded verification of sources needed by
the J/K/L manuscript, not an exhaustive priority search. Formulae were
checked against primary texts, not copied from earlier project summaries.

## Zhang 2026

The [official arXiv record](https://arxiv.org/abs/2607.10501v1) confirms
Ruizhe Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*,
arXiv:2607.10501v1, submitted 11 July 2026. It is a preprint; the record
does not establish journal acceptance.

The [primary HTML text](https://arxiv.org/html/2607.10501v1) was read at
Sections 2--4 and 7. Proposition 4.2 applies to arbitrary real frequencies,
complex coefficients, no separation, and 0 <= d <= 1. Its upper constant
is sqrt(9 A_fr/2) k exp(3 sqrt(2) k sqrt(d)), with A_fr <= 8191.
Proposition 7.1 gives the confluent Chebyshev lower construction. The
Legendre endpoint construction is also present in Appendix A.

Overlap is substantial: J follows the weighted-half-line, orthogonal-basis,
Laguerre architecture and reconstructs the finite-range step. K adapts
the known confluence mechanism to real, conjugate-paired dyadic packets
and integer heat-shear slices. Neither the general edge scale nor the
polynomial-to-Fourier mechanism should be claimed as a new discovery.
The paper proves its own required estimates, with attribution; it does
not assume Zhang's theorem as an unproved input.

## Erdelyi 2017

The [journal record](https://www.mathnet.ru/eng/sm8670) verifies *Sbornik:
Mathematics* 208(3), 433--464, DOI 10.1070/SM8670. Formula-level checks used
the [author's text](https://people.tamu.edu/~terdelyi/papers-online/sums_rev.pdf)
and [arXiv v1](https://arxiv.org/html/1602.02315v1).

For T_N (real frequencies, complex coefficients), Theorem 2.3 gives
||f||_infinity <= (pi N/2) ||f||_2 on [0,1]. Theorem 9.1 gives the
derivative factor (1+epsilon_N)(108 N^5 + sum mu_j^2)^(1/2).
Theorem 2.10 gives C_p N^(1/2+1/p) for p>2; p=3 therefore gives the
squared endpoint upper power N^(5/3), better than a coarse N^2.
Equation (1.2) records Kós's 2N endpoint bound for complex exponents
with nonnegative real parts; (1.5) records the pi N/2 refinement.

The journal's reported renumbering to Theorem 2.20 was not independently
read from the inaccessible journal PDF. Use the displayed formula or the
explicitly named arXiv numbering. Do not extend a T_N derivative estimate
to arbitrary complex exponents. Real cosine packets count as 2q branches.

## Kos 2008

The [Springer publisher record](https://link.springer.com/article/10.1007/s10474-007-6176-5)
confirms G. Kós, *Two Turán type inequalities*, *Acta Mathematica
Hungarica* 119 (2008), 219--226, published online 14 March 2008.
The DOI's `007` segment is not the publication year.
The abstract includes complex exponents with nonnegative real parts.
The subscription full text was not accessed here; the exact 2N L2
endpoint formula is verified through Erdelyi's explicit equation (1.2).
Consequently cite both the original attribution and the accessible
formula source when using that constant. Reversing the time coordinate
must be shown before applying this result to a decaying shear packet.

## Erdelyi 2007 and 2008: different frequency classes

The [Elsevier record](https://www.sciencedirect.com/science/article/pii/S0001870806000478)
verifies the final title *Markov--Nikolskii type inequalities for exponential
sums on finite intervals*, *Advances in Mathematics* 208(1), 135--146
(15 January 2007), DOI 10.1016/j.aim.2006.02.003.
The [author manuscript](https://people.tamu.edu/~terdelyi/papers-online/AIM-288.pdf)
defines a real span with real exponents. Its Descartes-system bounds do
not license the oscillatory, purely imaginary frequency estimate needed
in J. It is background only.

The [Cambridge chapter record](https://www.cambridge.org/core/books/number-theory-and-polynomials/newmans-inequality-for-increasing-exponential-sums/99573EF08C9C8D386C899C2B0FC10BCA)
and [author manuscript](https://people.tamu.edu/~terdelyi/papers-online/LMS_rev.pdf)
verify *Newman's inequality for increasing exponential sums*, in
*Number Theory and Polynomials*, LMS Lecture Note Series 352, 127--141,
print year 2008, DOI 10.1017/CBO9780511721274.010. The 2010 date is
online publication. The new lower bounds concern real positive
exponents and increasing sums. This chapter is not an input for a
complex-frequency terminal or spatial estimate.

## Other provenance

[Chen and Price, ICALP 2019](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2019.36)
is the published clustered-signal paper cited by Zhang for the earlier
Chebyshev motivation. Its publisher confirms volume 132, article 36,
pages 36:1--36:13, DOI 10.4230/LIPIcs.ICALP.2019.36.
No theorem from it is needed by the manuscript's proofs.

Borwein--Erdelyi--Zhang's *Müntz systems and orthogonal Müntz--Legendre
polynomials* is verified in the [author's bibliography](https://people.tamu.edu/~terdelyi/papers-online/list.html)
and [AMS volume index](https://www.ams.org/journals/tran/1994-346-02/tran-346-2-print-matter.pdf):
*Transactions of the AMS* 342 (1994), 523--542. The DOI is
10.1090/S0002-9947-1994-1227091-4. It supplies historical context for
the orthogonal exponential basis, not an imported unproved premise.

## Additional sources used in the integrated manuscript

The official [Singh--Sridhar arXiv record](https://arxiv.org/abs/1101.5507)
confirms the exact-plane-shear background and the journal publication
as *The European Physical Journal Plus* 132(9), article 403 (2017),
DOI 10.1140/epjp/i2017-11659-5. The simple triangular shear in this
manuscript is checked directly; its existence is not claimed as new.

The [Hall--Ho publisher text](https://link.springer.com/article/10.1007/s11005-025-01946-9)
confirms Brian C. Hall and Ching-Wei Ho, *The heat flow conjecture for
polynomials and random matrices*, *Letters in Mathematical Physics*
115, article 60 (2025), published 26 May 2025. Its Section 1.1 gives
the terminating heat-operator series on polynomial initial data. The
present manuscript cites that paper as broader polynomial-heat context,
not as proof of its local Chebyshev-edge or signed-flux asymptotics.

The bibliography's article numbers 403 and 60 are not page ranges.
The compact PDF bibliography retains DOI links for journal papers and
an explicit versioned arXiv link and preprint label for Zhang.

## Implemented source-related corrections

- Attribute the near-edge proof architecture and confluence explicitly.
- Label Zhang as a preprint, not a published theorem.
- Keep all norms as unaveraged integrals; [0,1] to [-1,1] introduces
  the appropriate length factor.
- Use 2q complex branches for q real positive modes.
- Correct the L3 endpoint discussion: the demonstrated lower power is
  q^(4/3), while a literature upper power q^(5/3) is already available.
- Keep the lower-bound conclusion at a prescribed time; no full-clock
  flux sharpness or general Navier--Stokes regularity conclusion follows.
