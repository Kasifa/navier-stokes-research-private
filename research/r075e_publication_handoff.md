# R0.75E Step 30 frozen publication handoff

## Release identity and queue order

- release id: R0.75E-Step30
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75D-Step29`
- queue rule: hold until R0.75D is verified, then append exactly once to the
  same FIFO task; never create or reuse any other publishing, recap,
  reflection, lessons-learned, or temporary task/system
- frozen research/certificate commit:
  `aeaf5e588f2e606ee7deb960dd1f05fa4198e442`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75E. Do not read or publish R0.75F or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `99529b8934412775e19a1b70784cddf3e62190b50c42669ccd34135a134c5049` | `research/r075e_horizontal_cross_mode_flux_reduction.md` |
| `da2778c1f0d5538981c517fccf75c96a635abbe7fae8833359c727dd2b301860` | `research/r075e_horizontal_cross_mode_flux_primary_audit.md` |
| `96577484d25745b419c30723c0af2d2873fbfff1f3340b79e1d7c9af71327199` | `research/r075e_report-source.md` |
| `682bdfadd6935e35c9ea85bfcfe9aa74ccbca8341f84791fe0885ee0f0e62946` | `research/r075e_horizontal_cross_mode_flux_reduction_certificate.json` |
| `6ffd2fb6601eae3e212ab1b989101eb6ca5e317cf4df9812a9926f6114ac79cf` | `research/r075e_horizontal_cross_mode_flux_reduction_certificate_report.md` |
| `a9d0b7410a6492ef699f1fbfc77906eb4bcadc1c9193887e8f3b8e5c5778d54c` | `research/r075e_horizontal_cross_mode_flux_reduction_independent_audit.md` |
| `14f344f5876b8d016da2fbe0fc465b8c1685738f9fea6dcefaf5c406195c89b5` | `research/r075e_horizontal_cross_mode_flux_reduction_qa_report.md` |
| `1d3eed137dc954bfcdfb6fe54ed6e1d3037f2bb18e297b3fb3264bbd8a2ad7ba` | `scripts/r075e_horizontal_cross_mode_flux_reduction_certificate.py` |
| `f6a85045c1737f7291441df9c9151d8f786510811f2333ec47843a8f16c2cb99` | `scripts/r075e_horizontal_cross_mode_flux_reduction_certificate_independent.rb` |
| `79065b938b264bc3422bed505f2f5a93f405fbb57bde2f598a7237bdba6d9ef1` | `scripts/r075e_horizontal_cross_mode_flux_reduction_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0. Certificate QA: Python 13/13, Ruby 16/16, 39/39 negative
mutations rejected independently by each implementation, unknown mutations
fail closed, and `PYTHONHASHSEED=0,1,42` byte stability. The finite Fourier
witness verifies the signed convolution normalization but is not a full
spacetime solution or a finite model of the geometric collar.

## Result and exact boundary

For

\[
 (\partial_t+b(t,x_3)\partial_2-\Delta_{23})F=0,
\]

the fixed physical collar cutoff produces the exact signed flux

\[
 \mathcal T_\xi
 =\pi\operatorname {Re}\sum_{n,m\in\mathbb Z}i(m-n)
 \int\eta_R b\,\Xi_{m-n}f_n\overline{f_m}.
\]

Every diagonal term \(n=m\) vanishes identically. Therefore the drift row
is a purely off-diagonal difference-frequency quantity, not a function of
the large background cubic atom alone.

If the horizontal Fourier support \(S\) satisfies

\[
 \Xi_{m-n}=0\qquad(n,m\in S,\ n\ne m),
\]

then the transport flux vanishes and

\[
 D_{k,R}^{{\rm out},F}
 \le C L^{2/3}\omega^{1/3}(P_R^M)^{2/3}.
\]

In particular, for every admissible real horizontal zero mode and all
sufficiently large \(L\),

\[
 \boxed{
 \partial_2F=0
 \Longrightarrow
 D_{k,R}^{{\rm out},F}\le C(P_R^M)^{2/3}}
\]

with no small-payment restriction and no D.23 interaction hypothesis. This
includes arbitrarily high vertical frequencies. Hence the earlier zero-mode
example obstructs only a horizontal-to-full Rayleigh inference; it is not
an obstruction to the target dissipation estimate.

The reality boundary is essential. A nonzero complex singleton also has
zero flux, but it is only an algebraic complexification, not a physical real
Navier--Stokes velocity. A nonzero real harmonic contains the pair
\(\{n,-n\}\); its difference frequency \(2n\) generally couples to the
cutoff, and shear rotates cosine and sine components. The certified exact
witness gives

\[
 \mathcal T_\xi/\pi=-\frac12\ne0
\]

for a real \(\{\pm1\}\) pair, while its diagonal terms and zero-mode flux
are exactly zero.

For a general real field, the exact remaining gate is

\[
 \mathfrak X_{\xi,R}(F,b)
 \le C(P_R^M)^{2/3},
\]

where \(\mathfrak X_{\xi,R}\) is the positive signed off-diagonal flux at
the target normalization. This bound is **OPEN**. The result does not close
general real cross-mode aggregation, complete-clock extraction, suitable-
weak transfer, fixed deletion, regularity, or singularity. The bounded
primary-source screen supports the neighboring mode/streamline/local-flux
mechanisms but makes no completeness, novelty, or priority claim.
**NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75E research page and synchronized downloadable
PDF, expose every frozen audit/certificate/source artifact, and update the
homepage, latest-research count, navigation, version ledger, and global
index through E. Do not update the cumulative recap at this non-major
milestone and do not invent a formal figure, simulation, DNS result, or
literature-completeness claim.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; desktop/mobile render inspection; GitHub Pages workflow verification;
and online byte-identity checks. Report the site commit, workflow run,
page/PDF/object counts, and deployed-byte verdict. No second task is
authorized. **NOT CLAY.**
