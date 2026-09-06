# Quantitative edge authoring-agent self-audit

Date: 2026-09-06. This is an automated self-audit by the agent that wrote the quantitative-edge proof; it is not an independent audit or human peer review.

Audited source snapshots:

- `sections/quantitative-edge.tex`: SHA-256 `db6888129f5481720b48b68fc0e5dd9cba322cd6cfe7f27f9403692b17ab7f4e`.
- `research/quantitative-edge.md`: SHA-256 `b8e65671f464cc741fb691e3c20181ab2270aa0a646dc1f0c1ff0c0ad641b9c2`.

Result: no mathematical defect identified. The following were recomputed directly rather than inferred from the qualitative v1 proof.

| Item | Check and conclusion |
|---|---|
| Joint range | All thresholds are fixed bounds on μ from below and ε=μ/A from above. No relation such as με→0, log A=o(μ²), or polynomial growth of A is used. |
| Common scale | n√ε=μ² is exact for either choice n=m or n=m+1. The saddle is z_s=2^(1/3)s^(2/3); F_s and G_s follow by direct differentiation. |
| Strong concavity | The exact second derivative is −(2z)^(-3/2)−1/(2s). It yields the global Gaussian envelope, including z=0 by continuity. |
| Local mass | The one-sided interval [z_s,z_s+1/μ] lies in J for μ≥1. Its length cancels the Gaussian Jacobian μ. The lower second derivative bound D_* and the bounded tilt loss have the correct signs. |
| Gaussian upper constant | Extending the quadratic upper bound to the full real line yields √(2s1/s0)e^(H_*), exactly V_*. |
| First-moment tail | The two-sided integral of |w| exp(−a_*μ²w²) outside radius r equals (a_*μ²)^(-1)exp(−a_*μ²r²). The chosen radius makes the excess moment at most μ^(-2). |
| Fine scale | The proof differentiates log I at every displacement c, then integrates the mean bound. It does not divide approximate common amplitudes. Negative displacements and c1=c2 are included. |
| Interior sign | Only an absolute value bound is used. The whole interior contributes at most 1; its c-derivative contributes at most 1/√(πs0). |
| Opposite exterior | After y=−2A−u, the envelope is bounded by exp(−A²/(8s1)−u²/(8s1)). The epsilon threshold is exactly sufficient for this bound. No parity or positivity assumption on that tail is required by the criterion. |
| Tail derivative | The factor (3A+u)/(2s0), the two Gaussian moments, and sup A exp(−A²/(8s1))=2√(s1/e) reproduce E1. |
| Positivity threshold | Four losses cost respectively F_*μ²/4, F_*μ²/4, F_*μ²/8, F_*μ²/8. The remaining F_*μ²/4 is κμ². The last threshold makes |R/I|≤1/2. |
| Relative derivative | The identity (log Q−log I)'=(R'−R(log I)')/(I+R) proves the exponentially small correction with the same |c2−c1| factor after integration. |
| U normalization | The exact denominator n sinh θ=μ²√(z(2+εz)) avoids any uncontrolled log n term. The local algebraic loss is μ^(-2), accounted for by b=2. |
| U counterexample | n_j=ceil(exp(j³)), A_j=n_j²/j³ has μ_j=j and ε_j=j⁴/n_j²→0, while log n_j/μ_j²~j. Thus the unnormalized common-amplitude obstruction is real. |
| Claims | Error orders are not declared optimal. No arbitrary Jacobi family, second-family dynamic shear realization, NS regularity conclusion, or priority claim is stated. |

Verification limitations: this is a written analytic audit, not a formal proof-assistant certificate. No numerical experiment is required for the validity of the proof. A separate agent must perform the independent theorem audit required by the revision brief.
