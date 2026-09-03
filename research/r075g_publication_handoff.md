# R0.75G Step 32 frozen publication handoff

## Release identity and queue order

- release id: R0.75G-Step32
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75F-Step31`
- queue rule: hold until R0.75F is verified, then append exactly once to the
  same FIFO task; never create or reuse any other publishing, recap,
  reflection, lessons-learned, usage-notes, or temporary task/system
- frozen research/certificate commit:
  `b4ec164eeae4ec79be3c517da98321b62294d991`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75G. Do not read or publish R0.75H or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `f2b3424dddb7eee5938200c3433cd012a1820564e43ad446e0c88d8dfa39ff41` | `research/r075g_signed_flux_gain_threshold.md` |
| `4717b365e5a4dc1bff169db51708a8a74fe51e6dd414a9a68a448813d95541aa` | `research/r075g_signed_flux_gain_threshold_primary_audit.md` |
| `2722d2801945a2ee074b0a9c4a973f592849ae012ddd4c264b7fea5ad76e9896` | `research/r075g_report-source.md` |
| `6bcf72a52763b04f98c21109fabbd570aa552cfe472280cff7ff4a0738eb0c9a` | `scripts/r075g_signed_flux_gain_threshold_fixtures.json` |
| `03b3475a3f8e82cb986e63ef52af6fdb899ac200b70024661c379542356b6ab0` | `scripts/r075g_signed_flux_gain_threshold_expected.json` |
| `72cf4415368aa527699b4e1d23a11ff91dc41247a0474b0bc33845f90214be32` | `research/r075g_signed_flux_gain_threshold_certificate.json` |
| `8a7d42b877481593278ffd60ac98c0ce3dd11f4f242c96db96f561f41dac8744` | `research/r075g_signed_flux_gain_threshold_certificate_report.md` |
| `5e33e561d9d84d2acda364fffe988a7eeee769c1a24b27d6fce01f4159c005d2` | `research/r075g_signed_flux_gain_threshold_independent_audit.md` |
| `15e50c29f8dd007249389b7c365630349eb690da400ac01123f2d1555f8941dc` | `research/r075g_signed_flux_gain_threshold_qa_report.md` |
| `c08eb7f02b49864d5f46ba4fc7f14b5f815f03fa712a0ccb373e933be6f46cee` | `scripts/r075g_signed_flux_gain_threshold_certificate.py` |
| `c2d11ff71dd683a15cbb97892c028b3e861e47bde5e18cedd602d9967430da3c` | `scripts/r075g_signed_flux_gain_threshold_certificate_independent.rb` |
| `65add9d4c0b8b6569315b1cdb7e664a91c28bc60d1204cec028d8adbbb2e9190` | `scripts/r075g_signed_flux_gain_threshold_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0. Certificate QA: Python 16/16, Ruby 18/18, 57/57 negative
mutations rejected independently by each implementation, unknown mutations
fail closed, `PYTHONHASHSEED=0,1,42` byte stability, and regeneration byte
stability. Independent fixtures cover exponent arithmetic, amplitude
homogeneity, a smooth periodic pure-transport endpoint identity, and a
single unwrapped rational occupation calculation.

## Result and exact boundary

Suppose an independent dynamical estimate improves the R0.75D absolute
flux bound to

\[
 \mathfrak X_{\xi,R}(F,b)
 \le C R^\alpha p_b^{1/3}p_F^{2/3}.
\]

For the frozen common shear,

\[
 p_b\le C L^2\omega R^{-3},
 \qquad
 p_b^{1/3}\le C L^{2/3}\omega^{1/3}R^{-1}.
\]

Therefore the remaining coefficient has exponential rate

\[
 \frac{(1-\alpha)\rho}{4}-\frac{c_\gamma}{12},
\]

and is strictly decaying exactly when

\[
 \boxed{
 \alpha>\alpha_*
 :=1-\frac{c_\gamma}{3\rho}
 =\frac{27163}{107163}
 \approx0.2534736803.}
\]

At equality the exponential rate is zero but the residual factor
`L^(2/3)` grows, so this unrefined sufficient estimate requires a strict
inequality. The two diagnostic powers lie on opposite sides:

\[
 \begin{aligned}
 \alpha=\frac13&:\quad
 \frac\rho6-\frac{c_\gamma}{12}
 =-\frac{4279}{238140000}<0,\\
 \alpha=\frac14&:\quad
 \frac{3\rho}{16}-\frac{c_\gamma}{12}
 =\frac{1489}{1905120000}>0.
 \end{aligned}
\]

Hence `R^(1/3)` would close E.24 by this route, while `R^(1/4)` would not.
This is a conditional theorem about the strength needed from a new input;
the gain itself is not proved.

If a future interaction atom satisfies

\[
 \mathfrak X_{\xi,R}
 \le C(p_b^{\rm int})^{1/3}p_F^{2/3},
 \qquad
 p_b^{\rm int}\le C R^\beta p_b,
\]

then `alpha=beta/3` and the exact residence threshold is

\[
 \boxed{
 \beta>\beta_*=\frac{27163}{35721}
 \approx0.7604210408.}
\]

A single unwrapped crossing of an `O(R)` interval at speed comparable to
`R^(-2)` lasts `O(R^3)`, an `O(R)` fraction of the full `O(R^2)` window.
This formally gives `beta=1` and `alpha=1/3`, but it is only a kinematic
benchmark. Diffusion, recrossing, spherical geometry, shear-transition
bands, periodic copies, and the payment bound for the interaction atom
remain to be proved.

The correlation ratio is invariant under `F -> A F`, so amplitude scaling
cannot create the missing gain. The pure-transport fixture verifies a
positive flux and endpoint half-energy difference of `1/32`; with diffusion
restored, using the same energy identity would be the R0.75F circularity.

G.1, G.18, the `R^(1/3)` target G.24, E.24, complete-clock extraction,
fixed deletion, suitable-weak transfer, regularity, and singularity remain
**OPEN**. The bounded primary-source screen makes no completeness, novelty,
or priority claim. **NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75G research page and synchronized downloadable
PDF, expose every frozen audit/certificate/source artifact, and update the
homepage, latest-research count, navigation, version ledger, and global
index through G. Do not update the cumulative recap at this non-major
milestone and do not invent a formal figure, simulation, DNS result, or
literature-completeness claim.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; desktop/mobile render inspection; GitHub Pages workflow verification;
and online byte-identity checks. Report the site commit, workflow run,
page/PDF/object counts, and deployed-byte verdict. No second task is
authorized. **NOT CLAY.**
