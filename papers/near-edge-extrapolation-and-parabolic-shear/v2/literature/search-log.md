# Search and verification log

Date: 2026-09-06. Scope: bounded follow-up of the exact v1 heat-edge theorem
and the time/spatial inputs. Search-result snippets supplied leads only;
mathematical comparisons used the primary documents listed below.

## Inputs and source checks

Read the full revision brief and full 2026-09-05 due-diligence report. Read v1
`sections/parabolic.tex`, `literature/source-audit.md`, and `references.bib`.
Read the current research/publishing protocol and isolated repository rules.
No publication queue, shared recovery index or mainline working tree was
modified. A quick memory-registry keyword search found no direct source for
this follow-up and was not used as mathematical evidence.

Primary texts opened and checked:

| Source | Locations checked | Result |
|---|---|---|
| [Erdelyi arXiv v1](https://arxiv.org/html/1602.02315v1) | Introduction classes, Thm 3.1, Lemma 12.5 | Required complex-decay class and constants verified |
| [Zhang arXiv v1](https://arxiv.org/html/2607.10501v1) | Thm 1.1, §2 conventions, Prop 4.2/proof, Prop 7.1 | Near-edge domain, prefactor, exponent and attribution verified |
| [Hile--Stanoyevitch](https://ejde.math.txstate.edu/Volumes/2001/28/hile.pdf) | Introduction, Thm 1, (2.18) | General polynomial heat history; no matching joint endpoint estimate |
| [Batahan--Shehata](https://scientificadvances.co.in/admin/img_data/849/images/%5B4%5D%20JMSAA%207100121348%20S.%20Raed%20Batahan%20and%20A%20Shehata%20%5B47-59%5D.pdf) | §§1,3, especially (3.1),(3.5) | Fixed negative heat parameter; U rather than T |
| [Khan](https://www.technoskypub.com/wp-content/uploads/2023/09/3-V2N2-P3-W-Certain-results-for-the-Hermite.pdf) | (1.1),(1.4), §3; rendered pp.88--89 | Printed identity has n=1 normalization inconsistency |
| [DLMF 16.11](https://dlmf.nist.gov/16.11) | All three subsections and equations | Fixed-parameter model vs. terminating family distinguished |
| [DLMF 16.2](https://dlmf.nist.gov/16.2) | Terminating p>q+1 discussion | Termination convention checked |
| [DLMF 18.5](https://dlmf.nist.gov/18.5) | (18.5.1)--(18.5.2) | Standard T/U normalization |
| [DLMF 8.4](https://dlmf.nist.gov/8.4) | (8.4.10)--(8.4.11) | Truncated exponential/incomplete-gamma identity |
| [Paris 2018](https://arxiv.org/pdf/1809.08794v2) | §§1--2; version record | Uniform Gauss family and saddle/pole transition |
| [Paris 2021](https://arxiv.org/pdf/2004.01945v2) | §§1--2; version record | Uniform Gauss family and saddle/endpoint transition |

## Query batches

The following literal queries were issued to the web search tool. Multiple
queries in a batch sometimes returned combined results; the log does not
pretend that each search exhausted all indexed results.

Initial heat/object pass:

1. `"Chebyshev" "heat" "asymptotic" polynomial edge`
2. `"terminating" "4F2" asymptotic`
3. `"Hermite-Chebyshev" "asymptotic"`

The results mostly concerned numerical heat solvers, ordinary Hermite
polynomials called Chebyshev--Hermite, and nonlinear Hermite--Chebyshev
approximation. These are not evidence of a matching heat-edge theorem.

Terminating/generalized hypergeometric pass:

1. `"terminating hypergeometric" "asymptotic" "large"`
2. `"4F2" "large" hypergeometric asymptotic`
3. `"Chebyshev" "heat polynomials"`
4. `"hypergeometric" "4F2" asymptotics Chebyshev`
5. `"uniform asymptotic" "terminating" hypergeometric Paris`
6. `"heat-evolved" "Chebyshev"`
7. `"Chebyshev" "Gaussian convolution" polynomial asymptotics`

No matching terminating four-upper/two-lower heat-edge theorem was identified.
General terminating-function results in Rydberg transition calculations and
uniform Gauss hypergeometric asymptotics were returned; the latter supplied
an actionable primary-source lead.

Adaptive follow-up of that lead:

1. `"uniform asymptotic" "hypergeometric" "large parameters" Temme 2003`
2. `"4F2" Chebyshev Hermite polynomial heat`
3. `"heat-evolved Chebyshev" edge`

Paris's two primary arXiv texts were then opened. Their displayed parameter
paths were compared to the terminating 4F2 parameters, not merely their
abstract keywords. The specific mismatch is recorded in `novelty-update.md`.
No claim about transformations that were not investigated is made.

## Reproducibility and stopping

Publisher PDF bytes used for the operational-formula checks were downloaded
to `/tmp/paper-edge-literature`. Only their metadata and SHA-256 values are
retained in this repository. Khan's pp.88--89 were additionally rendered with
the bundled pypdfium2 runtime because the web PDF text had ambiguous formula
layout. Full copyrighted sources and rendered pages are not redistributed.

The exact-source checks completed, the significant Khan inconsistency was
reported to the manuscript agent, and the remaining terminating-function
priority risk is explicitly bounded. Search stopped at that point. This was
not a paid database search, exhaustive backward/forward citation trace, or
independent human review.
