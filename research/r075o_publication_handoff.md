# R0.75O Step 40 frozen publication handoff

## Release identity and queue order

- release id: R0.75O-Step40
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75N-Step39`
- queue rule: hold until R0.75N is verified, then append exactly once to the
  same FIFO task; never create or reuse any other publishing, recap,
  reflection, lessons-learned, usage-notes, or temporary task/system
- frozen research/certificate commit:
  `9ad6873ca91c756309d009ffba142e4545f6c4c3`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75O. Do not read or publish R0.75P or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `3efb39d2624cf5b5a0e7f348f6cde2ef2416eca900f1aa3ecc90a6ad734849a9` | `research/r075o_vertical_diffusion_packet_gain.md` |
| `27f9341f93bd2b031dbd3fd0e8d745788d5ff36a085ddb8be4ef8e1c5553e69b` | `research/r075o_vertical_diffusion_packet_gain_primary_audit.md` |
| `9d2c234b0ba2a33b0f573a7933c26bcc751db6fe85919f2e146a0e6a18128c2b` | `research/r075o_report-source.md` |
| `46dff6097c3a052dc968f1c712c3421105ea5be51d3c905c492cc463cc04f0ad` | `scripts/r075o_vertical_diffusion_packet_gain_fixtures.json` |
| `228ac56e500a32b1f7c64c04d4110c78c4105c4d2a997fa8b108bd7449d59833` | `scripts/r075o_vertical_diffusion_packet_gain_expected.json` |
| `71a737b18d67cd01d494abfd0485b42fd78fce9a8bc2085931e17e2aa4be8055` | `research/r075o_vertical_diffusion_packet_gain_certificate.json` |
| `32267743fcfea2a88c5b971912db9f18dd76725b39bba5bf674bd920a8573379` | `research/r075o_vertical_diffusion_packet_gain_certificate_report.md` |
| `51fc9e834dbdc525b2c75c9430a87d1e8504666f7a65b0ac9e86a22baeb7dac7` | `research/r075o_vertical_diffusion_packet_gain_independent_audit.md` |
| `69a48e0ced0ce74d8d68a94bc6df0bfb35416c35257870f9db73e39e718ec8ad` | `research/r075o_vertical_diffusion_packet_gain_qa_report.md` |
| `a92864e15193139d2bfe4dd352c8a398bbe2dc2942fa0e3c2820331cb45f6e05` | `scripts/r075o_vertical_diffusion_packet_gain_certificate.py` |
| `33d0c8d15b34e8638160548b287f4db3acbae734b4523f09a700d0c66650f917` | `scripts/r075o_vertical_diffusion_packet_gain_certificate_independent.rb` |
| `084cf638304a98360aecbcefb1d074f8d67aef00c1fb2c49bfd3602db4b8496e` | `scripts/r075o_vertical_diffusion_packet_gain_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0. Certificate QA: Python 19/19, Ruby 20/20, 132/132 negative
mutation families rejected independently by each implementation, unknown
mutations fail closed, `PYTHONHASHSEED=0,1,42` byte stability, and complete
regeneration byte stability.

## Result and exact boundary

R0.75M proves a `K^(-2/3)` flux gain for one horizontal packet without a
vertical variable. R0.75N proves the coefficientwise `x_3`-uniform Wiener
row of the canonical radial collar. R0.75O combines these inputs for the
constant-shear equation

\[
 (\partial_t+B\partial_2-\Delta_{23})F=0
 \quad\hbox{on }[0,T]\times\mathbb T^2.
\]

For horizontal Fourier support `K<=|n|<=2K`, define

\[
 \mathcal W_\infty
 :=\sum_{\ell\in\mathbb Z}
 \|d_\ell\|_{L^\infty_{x_3}},
\]

where `d_l(x_3)` is the horizontal Fourier coefficient of the
`x_1`-averaged cutoff derivative. The vertical heat semigroup is an `L^2`
contraction. A difference-frequency Schur estimate therefore proves, with
no upper restriction on vertical frequencies,

\[
 \boxed{
 |\mathcal T_{K,\eta}^{(2)}|
 \le\frac{|B|\mathcal W_\infty}{4K^2}E_0.}
\]

The exact `1/4` comes from the physical `1/2` flux prefactor, the
`2*pi` horizontal pairing, the row bound `1/(2K^2)`, and horizontal
Parseval.

For the finite real-admissible two-dimensional packet

\[
 \Gamma_K=\{(n,j)\in\mathbb Z^2:
 K\le|n|\le2K,\ n^2+j^2\le4K^2\},
\]

and `K^2T>=1`, the short interval `0<=t<=1/(8K^2)` gives

\[
 M_K^{(2)}
 \ge\frac{e^{-3/2}}{16\pi}K^{-2}E_0^{3/2}.
\]

Consequently

\[
 \boxed{
 |\mathcal T_{K,\eta}^{(2)}|
 \le e(2\pi)^{2/3}|B|\mathcal W_\infty
 K^{-2/3}(M_K^{(2)})^{2/3}.}
\]

For the canonical R0.75N radial collar,
`mathcal W_infty<=C_vartheta L`. With

\[
 p_{K,23}^{\rm tor}=R^{-2}\omega M_K^{(2)},
 \qquad
 \mathfrak X_{K,23}^{\rm tor}
 =\frac\omega R[\mathcal T_{K,\eta}^{(2)}]_+,
\]

the normalized estimate becomes

\[
 \mathfrak X_{K,23}^{\rm tor}
 \le C_\vartheta|B|L
 R^{1/3}\omega^{1/3}K^{-2/3}
 (p_{K,23}^{\rm tor})^{2/3}.
\]

If `|B|<=C_BR^(-2)` and `K>=R^(-kappa)`, the exact strict threshold for
decay of the coefficient is

\[
 \boxed{
 \kappa>\frac12\left(5-\frac{c_\gamma}{\rho}\right)
 =\frac{98605}{71442}.}
\]

The frozen `kappa=3/2` lies above this threshold and leaves

\[
 L\omega^{1/3}R^{-2/3}
 =L\exp\!\left(-\frac{4279}{238140000}L^2\right)
 \longrightarrow0.
\]

Thus the constant-shear, total-frequency-capped packet is bounded against
its own full-`T^2` two-thirds atom with a uniform coefficient for large
`L`. That atom is not the smaller Version-M collar payment.

The certificate freezes the flux sign and `pi*B` factor, diagonal
cancellation, vertical heat contraction, Schur row and column bounds,
horizontal Parseval, `T^2` Holder factor, the total-frequency and time
hypotheses, exact energy inversion, radial-collar Wiener row,
normalization, strict rational threshold, frozen exponential margin,
tags, displays, dependencies, and claim boundaries.

Collar localization, nonconstant shear, inter-packet summation, low
horizontal differences, removal of the total upper-frequency cap, E.24,
complete-clock extraction, fixed deletion, suitable-weak transfer,
regularity, and singularity remain **OPEN**. The bounded primary-source
screen makes no completeness, novelty, or priority claim. **NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75O research page and synchronized downloadable
PDF, expose every frozen audit/certificate/source artifact, and update the
homepage, latest-research count, navigation, version ledger, and global
index through O. Do not update the cumulative recap at this non-major
milestone and do not invent a formal figure, simulation, DNS result,
Version-M localization theorem, nonconstant-shear theorem, inter-packet
theorem, or literature-completeness claim.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; desktop/mobile render inspection; GitHub Pages workflow verification;
and online byte-identity checks. Report the site commit, workflow run,
page/PDF/object counts, and deployed-byte verdict. No second task is
authorized. **NOT CLAY.**
