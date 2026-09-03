# R0.75F Step 31 frozen publication handoff

## Release identity and queue order

- release id: R0.75F-Step31
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75E-Step30`
- queue rule: hold until R0.75E is verified, then append exactly once to the
  same FIFO task; never create or reuse any other publishing, recap,
  reflection, lessons-learned, usage-notes, or temporary task/system
- frozen research/certificate commit:
  `be9a79a1d2b1fd2b7ee0e33f1f6e18f23b63958c`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75F. Do not read or publish R0.75G or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `f7a72ebfe0471e18c0d5d44bd3123491d7cd47a79293d1860c5d023c13acf440` | `research/r075f_modal_phase_integration_identity.md` |
| `4320ac5544b51888eb8088db98e500a9877ecfe9a984f156783cac096a27c99a` | `research/r075f_modal_phase_integration_identity_primary_audit.md` |
| `3838603ea143b2efe1e96995fac34d7e8565211dc91dd244ab01cf6d526f3481` | `research/r075f_report-source.md` |
| `107c59254b8f2e0ffa5e7a04ab8bdc97158191e99fca0f02ed08e0973c46fcf5` | `research/r075f_modal_phase_integration_identity_certificate.json` |
| `a756e4cf3e4d44012dde1588ca2150fb58c1669e6218e602aa2fba916b2c2834` | `research/r075f_modal_phase_integration_identity_certificate_report.md` |
| `eb7fac3ac148a41c43040c758028eb6552aa952639b54e0e1e47842604631fe8` | `research/r075f_modal_phase_integration_identity_independent_audit.md` |
| `f40a103b4b0a6cb85d684c7ff50d418402f857d8b77064d7f6c61139c77605f0` | `research/r075f_modal_phase_integration_identity_qa_report.md` |
| `c86d85bb468b9bd953247520e2de53cd18eb7362ef63dc60ae7895b01defb768` | `scripts/r075f_modal_phase_integration_identity_certificate.py` |
| `7499e5fa9544a805eb0675566224a77f4d99a196f3e1582a87bb4af724d269c2` | `scripts/r075f_modal_phase_integration_identity_certificate_independent.rb` |
| `b05e7eca1fae71955b27bc4fc6d3ddf1554f488dffe91cf081affe39c8e5932c` | `scripts/r075f_modal_phase_integration_identity_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0. Certificate QA: Python 16/16, Ruby 20/20, 43/43 negative
mutations rejected independently by each implementation, unknown mutations
fail closed, `PYTHONHASHSEED=0,1,42` byte stability, and regeneration byte
stability. The closed two-mode fixture computes the transport directly
from `i ell b g` before checking the time/vertical integrations by parts,
so the finite audit does not assume the identity it tests.

## Result and exact boundary

For `g_nm=f_n overline(f_m)` and `ell=m-n`, the exact modal-product
equation is

\[
 i\ell b g_{nm}
 =\partial_tg_{nm}-g_{nm}''
 +2f_n'\overline{f_m}'
 +(n^2+m^2)g_{nm}.
\]

After time and vertical integration by parts, the signed collar flux is
exactly

\[
 \boxed{
 \mathcal T_\xi
 =\mathcal E_{\rm off}
 -\mathcal A_{\rm off}
 +\mathcal D_{\rm off}.}
\]

Substitution into the full localized identity cancels every off-diagonal
endpoint, cutoff, and dissipation form and leaves

\[
 \boxed{
 \mathcal E_{\rm diag}+\mathcal D_{\rm diag}
 =\mathcal A_{\rm diag}.}
\]

Thus direct modal phase integration with no additional coercive estimate is
exactly the off-diagonal projection of the original energy identity. It
produces no independent sign, small factor, or observability bound.

Positivity of the cutoff also cannot repair the argument by itself. For
odd `N=2M+1`, the real Dirichlet/Fejer family

\[
 D_N=\sum_{k=-M}^{M}e^{ikx},\qquad
 a_N=D_N/\sqrt N,\qquad
 X_N=|D_N|^2/N^2
\]

satisfies

\[
 0\le X_N\le1,\qquad
 \langle X_N\rangle=1/N,\qquad
 \langle|a_N|^2\rangle=1,
\]

but

\[
 \frac{\langle X_N|a_N|^2\rangle}
 {\langle X_N\rangle\langle|a_N|^2\rangle}
 =\frac{2N+N^{-1}}3\longrightarrow\infty.
\]

The exact finite checks give `19/9`, `17/5`, and `33/7` for
`N=3,5,7`. This family is not the frozen geometric collar and is not a
counterexample to E.24. The result rules out only the circular phase
substitution and a positivity-only diagonal comparison. Genuine enhanced
dissipation, resolvent, pathwise, uncertainty, and payment-sensitive
estimates remain viable but unproved here.

The arbitrary-real cross-mode estimate E.24, complete-clock extraction,
fixed deletion, suitable-weak transfer, regularity, and singularity remain
**OPEN**. The bounded primary-source screen makes no completeness, novelty,
or priority claim. **NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75F research page and synchronized downloadable
PDF, expose every frozen audit/certificate/source artifact, and update the
homepage, latest-research count, navigation, version ledger, and global
index through F. Do not update the cumulative recap at this non-major
milestone and do not invent a formal figure, simulation, DNS result, or
literature-completeness claim.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; desktop/mobile render inspection; GitHub Pages workflow verification;
and online byte-identity checks. Report the site commit, workflow run,
page/PDF/object counts, and deployed-byte verdict. No second task is
authorized. **NOT CLAY.**
