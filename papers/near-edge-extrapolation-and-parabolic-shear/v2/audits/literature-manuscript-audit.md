# Manuscript literature and claim audit

Date: 2026-09-06. Reviewer: a separate automated literature agent.
Scope: `main.tex`, `sections/literature-context.tex`,
`sections/discussion.tex`, `sections/upper-bound.tex`, and the citation keys
they use in `references.bib`. This is a source/claim audit, not human peer
review, a complete proof audit, or confirmation that the release is frozen.

## Result

**PASS for the stated literature and claim scope.** The one requested
imported-class clarification was repaired and verified: the displayed
Erdélyi Markov input now explicitly restricts the frequencies to real numbers
and identifies Theorem 9.1 in arXiv v1. The actual application already had
real frequencies. No unresolved source/claim issue remains in this snapshot;
the separate proof, code and release checks retain their own scope.

The audited abstract and introduction place the uniform heat-edge estimates
and second-family instance first. Spatial extrapolation, polynomial heat
evolution, Laplace's method and Gaussian tilting are attributed or identified
as established. The temporal upper bound is a literature corollary, and its
order witness is restricted to the abstract temporal class. The full spatial
plateau is distinguished from complete velocity mass. Amplitude and frame
qualifiers are explicit. No firstness, best error order, universal dynamic
optimality, or general Navier--Stokes regularity conclusion is asserted.

## Source checks

| Manuscript point | Audit |
|---|---|
| Hile--Stanoyevitch polynomial evolution | Theorem 1 and (2.18) are an appropriate primary reference. The general finite polynomial operation is not presented as new. |
| Batahan--Shehata operation | Theorem 3.1 uses the second-kind polynomial and a fixed negative heat parameter. The manuscript states those distinctions. |
| Khan two-variable history | The source is used only as history. Its printed n=1 normalization inconsistency is recorded, and no imported equality depends on it. |
| T/U formulas | DLMF (18.5.1)--(18.5.2) verify standard normalization. The second family in v2 is explicitly endpoint-normalized. |
| Terminating 4F2 identity | Direct endpoint recurrence gives the displayed parameters, argument and termination. The text labels this algebra, not an additional asymptotic theorem. |
| 0F2 leading model | The classical exponential factor is appropriate context. The coefficient-product calculation explains why a relative approximation does not follow. |
| DLMF applicability | §16.11(ii) excludes terminating upper parameters and does not cover p=q+2. §16.11(iii) has a different parameter path. The manuscript makes only this precise non-application claim. |
| Paris's uniform asymptotics | Both primary PDFs were accessible and downloaded. The parameter paths and §§1--2 were read directly; the full proofs of those papers were not independently rederived. Both concern specified 2F1 families rather than the displayed terminating 4F2 theorem. |
| Hall--Ho context | The publisher's open text, abstract and §1.1 were checked afresh. It studies large-degree polynomial root evolution; citing it as broader context is accurate. |
| Zhang near-edge input | Theorem 1.1/Proposition 4.2, v1: arbitrary real frequencies, complex coefficients, 0≤d≤1, unaveraged L2 norm; exponent 3√2 and the stated finite-range prefactor are correct. Reflection and affine scaling are explained. |
| Erdélyi Markov input | The displayed constant matches arXiv v1 Theorem 9.1. The requested real-frequency qualifier and precise theorem locator are present and verified. |
| Kós endpoint input | The attribution is preserved and the accessible equation (1.2) in Erdélyi is identified. The time reversal gives nonnegative real parts before application. The subscription Kós full text was not newly accessed. |
| Temporal scaling in upper application | The rescaled decay rates have real parts in [λ,4λ] for this dyadic class; the imported corollary needs only the lower bound λ. The scale λ=(α/a)² and the λ^(-1/3) factor are consistent with that corollary. |

The primary URLs, exact locators, query record and downloaded-source hashes
are in `literature/novelty-update.md`, `literature/search-log.md` and
`literature/source-metadata.json`. The full Paris 2021 PDF was available;
there is no source-access limitation to conceal. The claim comparison uses
its actual stated hypotheses, without claiming that every possible
hypergeometric transformation has been excluded.

## Citation and declaration checks

A deterministic extraction of citation keys from the four audited TeX files
found **zero missing keys and zero duplicate bibliography keys**.
`Paris2018` identifies arXiv:1809.08794v2, 14 October 2018.
`Paris2021` identifies arXiv:2004.01945v2, 25 April 2021, and preserves its
first-submission year 2020 in the note. Zhang is explicitly a preprint.

The author remains C. K. Zeng, with ORCID 0009-0002-5402-3374. The AI
assistance declaration distinguishes automated review from human review and
formal proof-assistant certification. Its assertion that separate automated
proof reviews were completed must be supported by the final proof-audit
artifacts; this source review alone does not establish that release condition.
The text expressly disclaims an exhaustive priority search and identifies
human specialist review as a future step.

## Audited snapshot

```
main.tex 4224cf8230b8249ea433e53d64591faea8b60e02096bfdd8270ff2295d2046ff
sections/literature-context.tex fbae1db6c862139a5dddf2a34e3b7b25990d35ce46b77f986885f99a8fc9b2e9
sections/discussion.tex d60679ece457e695ace2693af05f5a69a6e5473f287afdb810d7077c65f68c18
sections/upper-bound.tex 5878c9a176a11069cd9cac80fca67796688bb524abf66333526f53f02536ffaf
references.bib b2a90e65836497f2dc6a9803c89eecf572437ac8ba3a08bf98525c96741f7c64
```

Any subsequent mathematical or attribution change requires a scoped review
of that change; these hashes do not certify unexamined later edits.
