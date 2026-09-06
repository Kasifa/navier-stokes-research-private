# Independent editorial review of the arXiv preparation

Reviewed on 6 September 2026. Read `main.tex` and all ten `sections/*.tex` in `/Users/kasifa/Documents/Math/paper-edge-v2/papers/near-edge-extrapolation-and-parabolic-shear/v2`, together with the bibliography. This is an editorial and self-containment review of the completed mathematical work, not a new proof audit or a finding of arXiv endorsement. The frozen v2 source has not been changed.

## Overall judgment

The title accurately names the two central objects. The manuscript has a coherent research-paper structure: quantitative theorem and criterion, special-function context, full-interval realization, normalization analysis, auxiliary upper bound, limitations, and supporting appendices. The existing abstract is substantively accurate (approximately 210 whitespace-delimited words; 1,594 TeX characters). It distinguishes the amplitude and displacement scales, the normalized second-kind extension, component mass versus complete velocity mass, and the temporal comparison. It makes no regularity or optimal-flux claim. Keep the title and author/ORCID information. The abstract can remain with the one clarification below; an explicit error formula is optional.

No mathematical statement needs modification for editorial preparation. The material needing correction is the manuscript's dependence on local research-version history and omitted audit files, plus its now-obsolete statement that no PDF is generated.

## Necessary for this standalone submission draft

1. `sections/discussion.tex:48–55`: replace the complete final paragraph (including its heading). It currently describes an internal second version, the novelty-assessment response, local ledgers, no new PDF, and no arXiv submission. Those statements belong in a local preparation receipt, not the submitted paper. If the upload includes the indicated ancillary materials, use:

```tex
\paragraph{Reproducibility.}
The ancillary materials contain exact finite verification scripts,
the data and plotting code for Figure~\ref{fig:edge-diagnostic}, and
instructions for reproducing the computations. These computations
support the stated finite checks; the asymptotic conclusions follow
from the proofs in the paper.
```

If those materials are not included, remove this paragraph rather than promise an absent supplement. Preserve the existing computer and AI assistance disclosure at lines 37–46: its author-responsibility sentence and separation from human review/formal certification are accurate and appropriate.

2. `sections/literature-context.tex:14–15`: delete the sentence beginning `The source audit records...`, leaving `are verified directly.` as the end of the paragraph. The audit is not a reader-accessible citation in the submitted manuscript; the asserted normalization issue is not used in any proof. Removing this sentence preserves the historical attribution to Khan and the explicit statement that none of those operational formulas is imported as a proof input. Alternatively, retaining the criticism would require placing the precise degree-one calculation and equation citation in the paper; that expansion is unnecessary for the present task.

3. `sections/upper-bound.tex:36–41`: replace the full paragraph with:

```tex
The cited result is a preprint theorem; the argument below uses only
the range $d\le1$. Corollary~\ref{lem:ub-delay} supplies the temporal
input, and \eqref{eq:ub-cutoff-time} gives its rescaled form.
```

4. `sections/upper-bound.tex:275–276`: retain the mathematical normalization and remove the unpublished-note dependency:

```tex
assert that a particular flux attains that rate. For the normalization
$\gamma=2/3969$, the rate is $-2/11907$.
```

5. `sections/sharpness.tex:114–115`: delete the final two lines referring to growing-degree slice estimates in `the first version`. The preceding three sentences already state the relevant distinction and give a complete cross-reference to the present dynamic proof.

6. `sections/diagnostic.tex:4–6`: replace with:

```tex
Figure~\ref{fig:edge-diagnostic} illustrates the three limiting constants
for the positive exterior integral used in
Theorem~\ref{thm:heat-edge}. Write
```

The word `illustrates` is more accurate than `checks`: the manuscript already carefully says that finite data do not certify the limit. Keep all numerical caveats in the caption.

7. `sections/diagnostic.tex:21`: the sibling-version dependency `../v1/figures/heat-edge/figure.pdf` must become a path to the identically copied figure inside the submission directory, e.g. `figures/heat-edge.pdf`. This is packaging self-containment, with no image change.

8. Remaining local-history terms in `sections/diagnostic.tex`: at line 34 replace `the archived legend` by `the figure legend`; at line 39 replace `The archived calculation` by `The calculation`; at lines 42–44, if the corresponding files are actually in the ancillary package, use:

```tex
integration interval. The plotting source, parameters, all 16 data
rows, and the numerical comparison report are included in the
ancillary materials. The two-resolution and tail-truncation comparisons measure
```

Replace lines 49–51 by:

```tex
This figure illustrates the qualitative limits rather than the
quantitative error bounds or the second-kind extension. The accompanying
exact algebra checks verify finite identities; neither type of
computation certifies a continuum limit.
```

9. `sections/consequences.tex:4–6`: replace the manuscript-history introduction by:

```tex
This appendix records the dependence of the estimates on an external
exponential normalization and compares the static and parabolic scales.
```

## Small recommended clarifications

1. `main.tex:56–58`: replace the three lines with:

```tex
An explicit sequence of consecutive-integer-frequency shears transfers
the first-kind profile over the full time interval, using one initial
datum for each member of the sequence. Its signed collar-flux quotient retains an
```

Then remove the old `Its signed collar-flux quotient retains an` at line 58 if the replacement spans that text. The purpose is to avoid the isolated abstract suggesting one initial datum common to every member of the growing sequence. The introduction and theorem already state the correct quantifiers.

2. Define `D` when introducing the polynomial heat operation, preferably `D=d/dx` in the introduction after the display at lines 89–93. It is standard notation, so this is a clarity improvement rather than a substantive blocker.

3. `main.tex:110`: change `\paragraph{What is being added.}` to `\paragraph{Main results.}`.

4. `sections/discussion.tex:30–35`: move the human-specialist-review recommendation to the local author checklist. Inside the paper use only:

```tex
The special-function comparison concerns the stated primary sources
and parameter regimes. It does not exclude more general results in
the terminating hypergeometric literature.
```

This removes a submission-process instruction without weakening the acknowledged boundary of the search. The AI disclosure can still explicitly state that automated checks are not human peer review.

5. In `sections/quantitative-edge.tex:43`, `For auditability` can become `For explicit parameter control`; in `sections/literature-context.tex:72`, `checked second-family instance` can become `second-family instance`. These are optional style changes, not blockers.

6. The standalone paper need not compare current constants with an unpublished earlier draft. In `sections/consequences.tex:64–69`, a compact replacement is:

```tex
This is a sufficient range for the proved upper-bound coefficient.
Neither equality in \eqref{eq:critical-kappa} nor its failure establishes
a change in the actual flux. The numerical constants come from the cited
extrapolation input. The spatial witnesses in
Section~\ref{sec:sharpness} do not supply a matching time-integrated
lower bound for this growing-mode boundary.
```

The useful mathematical conclusion remains identical; the local 5/3 improvement receipt stays in the research audit.

## Keep unchanged

- The explicit hypotheses and uniformity qualifiers of all theorems, including sequence-dependent eventuality, positivity, and the additional condition `mu/log A -> infinity` for divergence.
- The distinction between the entire plateau and the complete velocity, the amplitude restoration, and the bounded-drift scope.
- The negative normalized rates and their origin in a chosen external weight.
- The second-kind normalization example and its restriction against arbitrary Jacobi claims.
- The attributed preprint status and version-specific imported inequalities.
- The lack of optimal error orders, matched dynamic upper/lower bounds, or general Navier–Stokes regularity claims.
- The author identity and truthful AI/computer-assistance disclosure. No affiliation or contact information should be invented.

The current bibliography is readable and all ten entries are cited. Source comments about a `source-audit.md` file and `candidate additions` are internal metadata comments, so they do not affect the reader PDF; cleaning those comments in the submission copy is harmless. Ensure that the chosen upload includes the generated `.bbl` when the build workflow needs it, and do not include two independent copies of the same bibliography entries.
