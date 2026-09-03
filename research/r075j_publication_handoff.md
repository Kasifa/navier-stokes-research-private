# R0.75J Step 35 frozen publication handoff

## Release identity and queue order

- release id: R0.75J-Step35
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75I-Step34`
- queue rule: hold until R0.75I is verified, then append exactly once to the
  same FIFO task; never create or reuse any other publishing, recap,
  reflection, lessons-learned, usage-notes, or temporary task/system
- frozen research/certificate commit:
  `6c81786ea2977234de1ebb3286334d418fa0090b`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75J. Do not read or publish R0.75K or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `960e3cbc18ac8207253a8802da215b3eac07a714ddbcc7209985f27a00c9ff4d` | `research/r075j_mean_zero_adjoint_flux_obstruction.md` |
| `f2de2d439d428ccd2885f7d3fc333496cb9753896c772a54df04622e4c52c76e` | `research/r075j_mean_zero_adjoint_flux_obstruction_primary_audit.md` |
| `1d195b0bc6760a4458fd3b4f7d11c5c892ca259c88aa5de3b014b4986ad166ca` | `research/r075j_report-source.md` |
| `754d585bab0b194adaa3f945dc8b14950e3c078564f38dc63919cf733fcfea2c` | `scripts/r075j_mean_zero_adjoint_flux_obstruction_fixtures.json` |
| `6c32cd1ff38895c5e3b0a580ad9a5e789fc3d9d8e672ba6644dceeb29befe5b8` | `scripts/r075j_mean_zero_adjoint_flux_obstruction_expected.json` |
| `79e1fe204992b86f495c6d9c2f77084714ad905844776019befc2cc0c0577fd4` | `research/r075j_mean_zero_adjoint_flux_obstruction_certificate.json` |
| `ac258fd160fd1c9a9d96b4daebd8d4ce56df0c47d1fc667b8387347801f1629f` | `research/r075j_mean_zero_adjoint_flux_obstruction_certificate_report.md` |
| `945be036b61a9682c31e18e3502ddedc4947b2caae2ee5b1c40927bd62bf638c` | `research/r075j_mean_zero_adjoint_flux_obstruction_independent_audit.md` |
| `ca26acda3a20d3e641d1cf0d859382bb726e893f389494eaacd4402c78466895` | `research/r075j_mean_zero_adjoint_flux_obstruction_qa_report.md` |
| `390964c4116ece9002114d399b2c715fc7835cf7407f3788c426bc6c1d6b7d1f` | `scripts/r075j_mean_zero_adjoint_flux_obstruction_certificate.py` |
| `d84e7997c08f4ca11f88072217f7b0117bf1bd78db07fdc558a4e47e595f8147` | `scripts/r075j_mean_zero_adjoint_flux_obstruction_certificate_independent.rb` |
| `66b6bbe3ba5efc3ffc4d89fc733f36bd32f198574ab2131da332ac7fb4209a3b` | `scripts/r075j_mean_zero_adjoint_flux_obstruction_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0. Certificate QA: Python 19/19, Ruby 24/24, 84/84 negative
mutation families rejected independently by each implementation, unknown
mutations fail closed, `PYTHONHASHSEED=0,1,42` byte stability, and complete
regeneration byte stability.

## Result and exact boundary

For

\[
 \mathcal L=\partial_t+b(t,x_3)\partial_2-\Delta_{23},
 \qquad
 \mathcal L^*=-\partial_t-b(t,x_3)\partial_2-\Delta_{23},
\]

the physical signed collar source

\[
 a=\eta_R b\partial_2\xi
\]

has zero `(x_2,x_3)` mean at every fixed `(t,x_1)`.  Its exact
zero-terminal adjoint

\[
 \mathcal L^*\psi=a,
 \qquad \psi(t_2)=0
\]

therefore also has zero mean.  Unless `a` is identically zero, continuity
forces `psi` to change sign.

For a real passive solution, exact duality is

\[
 \boxed{
 \mathcal T_{\xi,\eta}(F,b)
 =\frac12\int\psi(s)|F(s)|^2
 -\int_s^{t_2}\!\int\psi|\nabla_{23}F|^2.}
\]

The negative part of `psi` creates a positive weighted dissipation term in
an upper bound.  Thus exact signed-source inversion moves the H.28 target
dissipation rather than removing it.

Adding a constant `C>=||psi_-||_infinity` makes the weight nonnegative but
does not create exact information.  The added contribution is

\[
 \frac C2(E(s)-E(t_2))-CD=0,
 \qquad E(s)-E(t_2)=2D.
\]

If the favorable dissipation is then discarded, the unpaid surcharge is
`CD`, the global energy drop, not a local cubic payment.

The obstruction does not rule out all adjoint methods.  A nonnegative
majorant satisfying

\[
 a\le\mathcal L^*\Phi,
 \qquad \Phi\ge0,
 \qquad \Phi(t_2)\ge0
\]

does give

\[
 \mathcal T_{\xi,\eta}(F,b)
 \le\frac12\int\Phi(s)|F(s)|^2.
\]

The missing theorem is an independent payment of this initial
occupation/source row by frozen Version-M atoms with the required positive
`R` gain.  Replacing `a` by `a_+` makes positivity available but changes
the signed source and does not prove that payment.

The finite certificate locks the formal-adjoint signs, zero mean,
all-positive-time `eta` in a coherent rational Fourier fixture, terminal
data and sign change, dual endpoint/dissipation signs, constant-shift
cancellation, `CD` surcharge, majorant direction, and the distinction
between `a`, `a_+`, and `|a|`.

A paid positive majorant, transition and periodic geometry, E.24,
complete-clock extraction, fixed deletion, suitable-weak transfer,
regularity, and singularity remain **OPEN**. This is not a blanket no-go
for resolvent or Feynman--Kac methods. The bounded primary-source screen
makes no completeness, novelty, or priority claim. **NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75J research page and synchronized downloadable
PDF, expose every frozen audit/certificate/source artifact, and update the
homepage, latest-research count, navigation, version ledger, and global
index through J. Do not update the cumulative recap at this non-major
milestone and do not invent a formal figure, simulation, DNS result,
positive-majorant payment, or literature-completeness claim.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; desktop/mobile render inspection; GitHub Pages workflow verification;
and online byte-identity checks. Report the site commit, workflow run,
page/PDF/object counts, and deployed-byte verdict. No second task is
authorized. **NOT CLAY.**
