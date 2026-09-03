# R0.75C Step 28 frozen publication handoff

## Release identity and queue order

- release id: R0.75C-Step28
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75B-Step27`
- queue rule: hold until R0.75B is verified, then append exactly once to the
  same FIFO task; never use the archived same-name task or create a separate
  publishing, recap, reflection, or “lessons learned” task/system
- frozen research/certificate commit:
  `08d2e6e2e8abfead79d8ee47ee63156b5984672a`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75C.  Do not read or publish R0.75D or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `1f72f3c9d9d348f86188206690ce714df28aed661a9192c7b53bc1e5921f2f89` | `research/r075c_background_shear_packing_false_positive.md` |
| `b3e1bc0b8e321e2a1bce0dafc74d21ad1f81048b63ab93f42f56e2c2a0760368` | `research/r075c_background_shear_packing_false_positive_primary_audit.md` |
| `d57a3d6d400dcd805c09e34ef7c2bec8b4abb35e8478a1e275f3a1324552355f` | `research/r075c_background_shear_packing_false_positive_certificate.json` |
| `5f91ed6b135a196849b26635a505ab809528c593db846e65a41569e13f166f50` | `research/r075c_background_shear_packing_false_positive_certificate_report.md` |
| `842b87327598c5458cc24937ea8def035886b9134221e77612bc778a2a3f4b8b` | `research/r075c_background_shear_packing_false_positive_independent_audit.md` |
| `13f047fef4fb5934885d78a32f7ffcdc9a7e71eaa58b6afdbf92a965cc0c1afe` | `research/r075c_background_shear_packing_false_positive_qa_report.md` |
| `2c75ae98b5ffb4c7c7b4c911758656db47ea349ec91e8c823d9309641853d010` | `scripts/r075c_background_shear_packing_false_positive_certificate.py` |
| `b9b8202a2d82cb5a735051cffe2ed4428f307f38c54e67a413adbd9ce20ea76b` | `scripts/r075c_background_shear_packing_false_positive_certificate_independent.rb` |
| `2282c525858c552c4151e4e5f65a83d3098a1d34f5afd50b02a44455fbbe98bb` | `scripts/r075c_background_shear_packing_false_positive_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0.  Certificate QA: Python 8/8, Ruby 9/9, 18/18 and 19/19 negative
mutations rejected, 36 unique tags and resolved references, and
`PYTHONHASHSEED=0,1,42` byte stability.  The certificate is finite exact
arithmetic/structure evidence only.

## Result and exact boundary

For the saturation-shear solution with no passive packet,

\[
 u^{\rm sh}=(0,b,0),\qquad
 b=B e^{t\partial_3^2}g_R,
\]

the outer-collar cubic mass is comparable on all
\(N\asymp R^{-1}\) short blocks.  Hence

\[
 N_{\rm eff}^{\rm sh}\asymp R^{-1},
 \qquad
 \lim_{L\to\infty}\frac{\log N_{\rm eff}^{\rm sh}}{L^2}
 =\frac\rho4.
\]

It violates the sufficient R0.75B packing threshold by

\[
 \frac\rho4-\frac{4279}{79380000}
 =\frac{27163}{158760000}>0.
\]

But the actual shear dissipation remains paid.  Spherical-collar slice
geometry and the one-dimensional BV heat estimate give

\[
 \int_{61R^2}^{65R^2}
 \|\partial_3\theta_R(t)\|_2^2\,dt\le CR,
\]

and therefore, for the same frozen shear even after adding an arbitrary
passive component \(F\),

\[
 \boxed{
 D_{k,R}^{{\rm out},b}
 \le C\omega^{1/3}L^{-1/3}(P_R^M)^{2/3}
 =o((P_R^M)^{2/3}).}
\]

The interpretation is precise:

- the claim that the B.44 threshold must hold universally is **DISPROVED**;
- B.44 remains a valid sufficient condition whenever it happens to hold;
- a total-velocity cubic packing count can falsely flag persistent,
  low-frequency background shear;
- the direct full outer-dissipation estimate B.45 is **NEITHER PROVED NOR
  DISPROVED**;
- only the passive row
  \[
  D_{k,R}^{{\rm out},F}
  =\frac\omega R\int\eta_R\xi_k^R|\nabla_{23}F|^2
  \]
  remains after the shear row is paid;
- full \(K\), fixed deletion, suitable-weak extension and regularity remain
  **OPEN / NOT CLAY**.

Do not describe R0.75C as a Navier--Stokes counterexample.  It is a rigorous
counterexample to one proposed **auxiliary universal packing condition** and
a route-pruning lemma inside an exact smooth family.  No novelty or priority
claim is authorized.

## Publication and deployment QA

Publish one bilingual R0.75C research page and synchronized downloadable PDF,
expose the frozen audit/certificate artifacts, and update homepage,
latest-research count, navigation, version ledger, and global index through C.
Do not update the cumulative recap at this non-major milestone and do not
invent a formal figure, simulation, or literature-completeness claim.

Run structural, equation, internal-link, and asset tests; desktop/mobile
render inspection; GitHub Pages workflow verification; and online byte
identity checks.  Report the site commit, workflow run, page/PDF/object
counts, and deployed-byte verdict.  No second task is authorized.
**NOT CLAY.**
