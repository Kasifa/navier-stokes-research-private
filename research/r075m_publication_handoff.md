# R0.75M Step 38 frozen publication handoff

## Release identity and queue order

- release id: R0.75M-Step38
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75L-Step37`
- queue rule: hold until R0.75L is verified, then append exactly once to the
  same FIFO task; never create or reuse any other publishing, recap,
  reflection, lessons-learned, usage-notes, or temporary task/system
- frozen research/certificate commit:
  `decc558786108fd1ce4a7f86d906d12c4eb61a25`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75M. Do not read or publish R0.75N or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `13434bbc15eabecd5a695eceef01a7d63415e96511b14c29cc8abcd1297c7bf7` | `research/r075m_dyadic_packet_diffusive_flux_gain.md` |
| `2b5ee050c09e3be925143c12c29082c3fe562a83b9a2d2669511a2bb1684d7dc` | `research/r075m_dyadic_packet_diffusive_flux_gain_primary_audit.md` |
| `f8ed7af8ef5051b0efa73177d0530562917d55dfa6476b00b8f871db0da99d67` | `research/r075m_report-source.md` |
| `b93d727b4bf0729af2064e51fbc0c1450d98806c9b92fe11727b4d5423fa157f` | `scripts/r075m_dyadic_packet_diffusive_flux_gain_fixtures.json` |
| `cef1705998bc935448f371d6f389d46059b59e99bf230bd75dad0489fb85a4f4` | `scripts/r075m_dyadic_packet_diffusive_flux_gain_expected.json` |
| `1794cee5294ed55a41697f74d6a4b0bbb5e31e59b3a74ed11f277d0ae8e17423` | `research/r075m_dyadic_packet_diffusive_flux_gain_certificate.json` |
| `cd2882d59ec90471d1e74cb135426490c46863fbf6e6df3db3532926aaa5002f` | `research/r075m_dyadic_packet_diffusive_flux_gain_certificate_report.md` |
| `507fdbb899f0e74abccc0477405949ca07f9379d4b20ce20ab3bd87e63a76881` | `research/r075m_dyadic_packet_diffusive_flux_gain_independent_audit.md` |
| `b7513c9ee3660a21473f7ea87a19d4ae0f70aa6a99ceb88b397d159e7a56bad0` | `research/r075m_dyadic_packet_diffusive_flux_gain_qa_report.md` |
| `8a55852a3eabcf8989feadcb25cb178db57b1dccbd2249e73d48e61e7755811b` | `scripts/r075m_dyadic_packet_diffusive_flux_gain_certificate.py` |
| `6436063bc4ec623dfc27d7fc3edee8ee6751784f8a43ecdd5aa1b4170b35dd1b` | `scripts/r075m_dyadic_packet_diffusive_flux_gain_certificate_independent.rb` |
| `9e61cb0e57f4116e371beda1d6709ca479ea146538758287d6451b2641e87cf2` | `scripts/r075m_dyadic_packet_diffusive_flux_gain_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0. Certificate QA: Python 19/19, Ruby 20/20, 130/130 negative
mutation families rejected independently by each implementation, unknown
mutations fail closed, `PYTHONHASHSEED=0,1,42` byte stability, and complete
regeneration byte stability.

## Result and exact boundary

R0.75L proves a `k^(-2/3)` physical signed-flux gain for one exact real
harmonic. R0.75M proves that arbitrary finite interference inside one
dyadic horizontal packet does not destroy that exponent and introduces no
separate packet-cardinality loss.

Work on `[0,T] times T` with constant shear

\[
 \mathcal L_B=\partial_t+B\partial_2-\partial_2^2.
\]

For `K>=1`, let `Lambda_K={n in Z:K<=|n|<=2K}` and take

\[
 F_0(x_2)=\sum_{n\in\Lambda_K}c_ne^{inx_2},
 \qquad c_{-n}=\overline{c_n},
\]

with exact passive evolution

\[
 F(t,x_2)=\sum_{n\in\Lambda_K}
 c_ne^{-n^2t}e^{in(x_2-Bt)}.
\]

For a smooth periodic real cutoff `xi`, define

\[
 d_\ell=\frac1{2\pi}\int_0^{2\pi}\partial_2\xi(x_2)
 e^{-i\ell x_2}\,dx_2,
 \qquad
 \mathcal W_\xi=\sum_{\ell\in\mathbb Z}|d_\ell|.
\]

Periodicity gives `d_0=0`, so the diagonal is deleted before absolute
values. The exact modal kernel, its `1/(n^2+m^2)` time bound, Schur's test,
and Parseval give

\[
 \boxed{
 |\mathcal T_{K,\eta}|
 \le\frac{|B|\mathcal W_\xi}{4K^2}E_0,
 \qquad E_0=\int_0^{2\pi}|F_0|^2.}
\]

There is no explicit count of modes. For `K^2T>=1`, the upper packet edge
and the interval `0<=t<=1/(8K^2)` imply

\[
 M_K:=\int_0^T\!\int_0^{2\pi}|F|^3
 \ge\frac{e^{-3/2}}{8(2\pi)^{1/2}}K^{-2}E_0^{3/2}.
\]

Eliminating the initial energy proves

\[
 \boxed{
 |\mathcal T_{K,\eta}|
 \le e(2\pi)^{1/3}|B|\mathcal W_\xi
 K^{-2/3}M_K^{2/3}.}
\]

The cutoff row is finite without higher regularity loss:

\[
 \mathcal W_\xi
 \le C\left(
 \|\partial_2\xi\|_{L^2}
 +\|\partial_2^2\xi\|_{L^2}\right).
\]

With the full-torus diagnostic atom
`p_K^tor=R^(-2)omega M_K`, the normalized estimate is

\[
 \boxed{
 \mathfrak X_K^{\rm tor}
 \le e(2\pi)^{1/3}|B|\mathcal W_\xi
 R^{1/3}\omega^{1/3}K^{-2/3}
 (p_K^{\rm tor})^{2/3}.}
\]

A separately paid packet threshold `K>=R^(-kappa)` gives an exponent
strictly stronger than the R0.75G requirement only when

\[
 \boxed{
 \kappa>\frac{27163}{71442}
 \approx0.3802105204.}
\]

The result is restricted to one finite real dyadic packet, one-dimensional
constant shear, and the full-torus cubic mass. It does not sum different
packets, calibrate the frozen radial cutoff's Wiener row, localize the mass
to Version-M collar atoms, treat vertical/nonconstant-shear dynamics, or
close the low difference-frequency sector.

The certificate freezes the Fourier convention, `2*pi` spatial pairing,
`pi B` modal kernel, diagonal cancellation, Schur row and column sums,
Parseval factor `1/4`, short-time heat and Holder constants, exact energy
inversion, Wiener/Sobolev row, target normalization, strict rational
threshold, tags, displays, dependencies, and claim boundaries.

E.24, complete-clock extraction, fixed deletion, suitable-weak transfer,
regularity, and singularity remain **OPEN**. The bounded primary-source
screen makes no completeness, novelty, or priority claim. **NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75M research page and synchronized downloadable
PDF, expose every frozen audit/certificate/source artifact, and update the
homepage, latest-research count, navigation, version ledger, and global
index through M. Do not update the cumulative recap at this non-major
milestone and do not invent a formal figure, simulation, DNS result,
inter-packet theorem, collar localization, or literature-completeness
claim.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; desktop/mobile render inspection; GitHub Pages workflow verification;
and online byte-identity checks. Report the site commit, workflow run,
page/PDF/object counts, and deployed-byte verdict. No second task is
authorized. **NOT CLAY.**
