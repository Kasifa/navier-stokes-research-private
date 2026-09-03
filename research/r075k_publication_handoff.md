# R0.75K Step 36 frozen publication handoff

## Release identity and queue order

- release id: R0.75K-Step36
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75J-Step35`
- queue rule: hold until R0.75J is verified, then append exactly once to the
  same FIFO task; never create or reuse any other publishing, recap,
  reflection, lessons-learned, usage-notes, or temporary task/system
- frozen research/certificate commit:
  `69f3989c46f0ff09c8a20cb0c387625beae42d45`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75K. Do not read or publish R0.75L or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `9282fb30eb7517853759fb835579220e0da763974d5543e2fb260ec8ca6daebf` | `research/r075k_positive_majorant_high_frequency_trace_loss.md` |
| `401f12d9a5f35646638ae08446a1177a0b0485b9bbb54206702dee9fc7e7a4a2` | `research/r075k_positive_majorant_high_frequency_trace_loss_primary_audit.md` |
| `5a45521ecb5e85b69b077af9d4db3cbb1c52dc1b61cccf8fb3bbb9daabac7001` | `research/r075k_report-source.md` |
| `f15df9bf59d6a96151f84ae2fa11a12b3965820450fbad526d4f71f11a6f7328` | `scripts/r075k_positive_majorant_high_frequency_trace_loss_fixtures.json` |
| `5ad1107080ccf033e842521e8f985196357d6cb858f945b007a5df50c2a12d77` | `scripts/r075k_positive_majorant_high_frequency_trace_loss_expected.json` |
| `50e278d5307a85c515f1f879e7ff38438678b709e6a18c14791c60289c5c55eb` | `research/r075k_positive_majorant_high_frequency_trace_loss_certificate.json` |
| `2dee099eabc2a3db8a9ee48cc6c4a3f2b64cbc930444268d925b0ec70a376919` | `research/r075k_positive_majorant_high_frequency_trace_loss_certificate_report.md` |
| `107cfbaab6f29b596f9f9a3d6808e733f63d6cf9ec0dfd7c6b391391ca4cd92a` | `research/r075k_positive_majorant_high_frequency_trace_loss_independent_audit.md` |
| `4fb4a993a3d975a303717a98a2dc306291b9fcef4a2ac734c4d0e90273163c75` | `research/r075k_positive_majorant_high_frequency_trace_loss_qa_report.md` |
| `0093790920b5ed66fac3fbc808b1ea34e311124f201d54b60d71c3bd57f44661` | `scripts/r075k_positive_majorant_high_frequency_trace_loss_certificate.py` |
| `9caa3aa1b3ca13ff7cc8403a352c55089809ff237c0939c42cadcd8d11e52564` | `scripts/r075k_positive_majorant_high_frequency_trace_loss_certificate_independent.rb` |
| `a31c9c8f566d33f169f9a6b63a77770f104b74471efd8483549544ef10095212` | `scripts/r075k_positive_majorant_high_frequency_trace_loss_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0. Certificate QA: Python 19/19, Ruby 21/21, 100/100 negative
mutation families rejected independently by each implementation, unknown
mutations fail closed, `PYTHONHASHSEED=0,1,42` byte stability, and complete
regeneration byte stability.

## Result and exact boundary

R0.75J leaves a nonnegative adjoint majorant as a viable architecture but
does not pay its initial boundary row. R0.75K proves that the existing
local spacetime cubic atom alone cannot uniformly make that payment for a
fixed nontrivial nonnegative entrance weight.

On a constant-shear circle, take

\[
 \mathcal L=\partial_t+\partial_2-\partial_2^2,
 \qquad
 a=\partial_2(\sin x_2)=\cos x_2.
\]

The smooth source `q=1+cos x_2` is nonnegative and majorizes `a`. Its
zero-terminal adjoint solution is nonnegative, contains only frequencies
`0,+/-1` at the entrance, and has exact mass

\[
 \int_0^{2\pi}\Phi(0,x_2)\,dx_2=2\pi T.
\]

For every integer `k>=1`, the smooth real passive field

\[
 F_k(t,x_2)=A e^{-k^2t}\cos(k(x_2-t))
\]

satisfies `L F_k=0`. Fourier orthogonality gives the positive-majorant
boundary row

\[
 \boxed{
 B_k=\frac12\int\Phi(0)|F_k(0)|^2
 =\frac{A^2\pi T}{2},}
\]

independent of `k`. Its exact spacetime cubic mass is

\[
 M_k=\frac{8A^3}{9k^2}(1-e^{-3k^2T}),
\]

and therefore

\[
 \boxed{
 \frac{B_k}{M_k^{2/3}}
 \ge\frac{\pi T}{2}\left(\frac98\right)^{2/3}k^{4/3}
 \longrightarrow\infty.}
\]

The amplitude cancels exactly. For fixed `R,omega,T`, replacing `M_k` by
the local atom `p_k=R^(-2)omega M_k` changes only a fixed prefactor, so no
frequency-independent cubic payment exists for this entrance row.

The decisive boundary is that the target signed flux is nevertheless

\[
 \boxed{
 \mathcal T_k
 =\frac12\int_0^T\!\int_0^{2\pi}
 \cos x_2|F_k|^2=0}
\]

for every integer `k>=1`, because `|F_k|^2` has only frequencies
`0,+/-2k`. Positivity has introduced a zero mode absent from the signed
source, so the large boundary row measures proof loss rather than a large
physical flux.

More generally, every fixed continuous nonnegative entrance weight with
positive integral has a positive limiting pairing with `F_k(0)^2`; its
oscillatory row vanishes by Riemann--Lebesgue. The quantifier is fixed
weight first, then `k` tends to infinity.

Thus the result rules out only

\[
 \text{fixed nonnegative entrance weight}
 \quad+\quad
 \text{local spacetime cubic atom alone}.
\]

It does not rule out signed kernels, `F`-dependent or frequency-adapted
tests, payment by another genuinely available Version-M trace/frequency
row, or E.24 itself. The finite certificate locks every Fourier mode,
operator sign, exact moment, exponent, quantifier, and claim boundary.

Transition and periodic geometry, the full Version-M payment question,
E.24, complete-clock extraction, fixed deletion, suitable-weak transfer,
regularity, and singularity remain **OPEN**. The bounded primary-source
screen makes no completeness, novelty, or priority claim. **NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75K research page and synchronized downloadable
PDF, expose every frozen audit/certificate/source artifact, and update the
homepage, latest-research count, navigation, version ledger, and global
index through K. Do not update the cumulative recap at this non-major
milestone and do not invent a formal figure, simulation, DNS result,
E.24 counterexample, or literature-completeness claim.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; desktop/mobile render inspection; GitHub Pages workflow verification;
and online byte-identity checks. Report the site commit, workflow run,
page/PDF/object counts, and deployed-byte verdict. No second task is
authorized. **NOT CLAY.**
