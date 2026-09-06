# Source and claim ledger

Research revision v2, 6 September 2026. Author: C. K. Zeng.
Release ID: `paper-heat-edge-v2-20260906`.

## Isolation and mandatory inputs

- Baseline: `0a212f4e140e0c9875e740cb8ee23be32a5c05dd`, frozen v1 in the paper worktree.
- Revision branch: `codex/heat-edge-paper-v2`.
- New worktree: `/Users/kasifa/Documents/Math/paper-edge-v2`.
- User's complete task brief and due-diligence report were read before revision, as was the current workflow's single-paper exception. Their path/hash record is in `input-provenance.json`.
- Research context helper was run once at the beginning; it exited 2 because the workflow hash had changed. Its stale next action was hidden. No shared recovery index was refreshed or used as this paper's next action.
- The root agent read the full frozen manuscript sources and the needed full J, K and L mathematical notes. Separate agents read the relevant primary sources and performed bounded literature/analytic audits. Current mainline working notes were not used as proved premises.
- No publication index or queue was read; no mainline worktree, plan, root Git repository or website was edited. The original paper worktree's modified AGENTS.md and untracked older-paper directory were left untouched.

## Frozen scientific antecedents

| Source | Commit | Mathematical source |
|---|---|---|
| J | `25d44e986d5283107816f910f89b94bceb1d5726` | `research/r076j_local_edge_extrapolation_reconstruction.md` |
| K | `8a89aee4fe0839de44e21a90ba827a9cc77b3062` | `research/r076k_real_dyadic_edge_sharpness.md` |
| L | `b234b63c24c7b19efc703367e23b092385066a1c` | `research/r076l_parabolic_edge_smoothing_complete_clock.md` |

The manuscript is self-contained apart from explicitly attributed external inequalities. It does not require these internal research labels to read a theorem or proof. Earlier stronger wording in research notes is not silently inherited: the sequence-dependent threshold, algebraic factors, and unproved high-degree directions have the corrected v1/v2 boundaries.

## Claim-level classification

| Label / object | Status | What the revision supplies | Boundary |
|---|---|---|---|
| thm:quantitative-edge | PROVED, substantive revision | Explicit uniform amplitude and displacement error bounds for T and normalized U | Sufficient orders; positive compact time; original joint range; no best-order claim |
| prop:edge-profile | PROVED, substantive revision | Quantitative profile criterion, both tails and displacement derivative restored | Requires every stated envelope/lower-bound condition |
| eq:terminating-hypergeometric | PROVED algebra, classical object | Exact coefficient derivation and comparison with 0F2 | No relative-equivalence claim; not a new special function |
| thm:heat-edge | PROVED, inherited and strengthened | Now an immediate corollary of the new quantitative theorem | Only allowed joint degree/scale sequences |
| lem:heat-terminal | PROVED, inherited | Positive endpoint series, derivative and global majorant | Terminal interval (1+mu²)^-1; positive coordinate for derivative bound |
| prop:dynamic-confluence | PROVED, inherited and re-audited | One explicit integer-mode initial profile, full-interval transfer | Exactly m+1 positive frequencies; growing coefficients allowed |
| thm:parabolic-shear | PROVED, inherited and re-audited | Complete signed flux, full plateau including caps, positive eventual numerator | One family; eventual threshold depends on sequence; divergence needs mu/log A→∞ |
| prop:galilean-frame | PROVED, classical transformation | Explicit comparison of fixed windows/frames | Does not set the original fixed-window flux to zero |
| prop:full-velocity-mass | PROVED, new manuscript consequence | Original-amplitude full-velocity rate -9/20000 | Not invariant under amplitude rescaling |
| prop:amplitude-scaling | PROVED, new boundary consequence | Monotone full-velocity quotient and explicit lambda=R^-2 recovery | No uniform energy bound; drift still large |
| prop:bounded-drift-shape | PROVED, bounded exploration | Vanishing quotient for same shape and bounded drift, any amplitude | Not all possible profiles |
| thm:ub-edge | LITERATURE | Zhang v1, full assumptions and elementary affine rescaling | Preprint; d∈[0,1]; arbitrary real frequencies |
| lem:ub-delay | LITERATURE COROLLARY | Erdelyi's two inequalities plus explicit mixed-norm derivation | Re decay≥1 only; no upper bound needed |
| prop:time-order | PROVED explicit construction | Exact N-term lower order N^(4/3)/128 | Abstract temporal class, not squared-integer shear class or q^7 optimality |
| thm:ub-flux | PROVED combination of literature inputs | Same full-time energy argument with 12sqrt2 exponent | One dyadic band, component mass, signed flux |
| thm:real-dyadic-lower / thm:integer-slice | LITERATURE + elementary adaptation | Short attributed appendix, realification/nonzero coefficients/integer realization | Prescribed slice can choose its own initial data |
| cor:critical-coefficient | PROVED algebraic consequence | Updated sufficient threshold after literature substitution | Not an actual phase transition |
| Retained figure / exact scripts | FINITE COMPUTATION | Fresh finite reruns and targeted mutations | Not proofs of continuum statements or novelty |
| Best error order, general Jacobi, dynamic matching, other bounded-drift profiles | OPEN | Precise stops recorded | Not silently assumed |
| General NS regularity or singularity | NOT CLAY | Explicitly excluded | No such theorem |

## Independent audits

The proof author wrote `quantitative-edge-self-audit.md`; this is identified as a self-review. A different agent wrote `quantitative-cross-audit.md` with independently recomputed constants and a bound on every omitted portion. The time chapter was written by the root agent and independently checked in `time-cross-audit.md`. The application author supplied its derivation/audit; the root agent independently checked the volume, R powers, rescaling sandwich, and bounded-drift bound. Another agent checked the final auxiliary spatial/upper argument. A dedicated source reader checked literature attribution and final scientific positioning.

The exact reviewed-source hashes and the two corrected scope ambiguities are retained in audit files. Final prose-only bibliography/layout adjustments are documented in the final audit. These are separate automated runs, not human peer review, a proof assistant, or novelty certification.

## Figure and PDF policy

The complete historical scientific figure package is retained at `../v1/figures/heat-edge/` and inventoried by `FIGURES.md` and the new source manifest. New reader PDFs are not created. XDV compilation checks the source, bibliography, references and TeX layout diagnostics; no visual review of a newly rendered reader manuscript is asserted.

## Release binding

The scientific source manifest hashes every delivered research file and inherited dependency and excludes itself and derived output directories. A clean local commit freezes those files. `output/release-receipt.json` is generated afterwards and binds the exact source commit, manifest and deterministic source archive hashes without an impossible self-referential commit hash.
