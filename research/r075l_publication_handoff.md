# R0.75L Step 37 frozen publication handoff

## Release identity and queue order

- release id: R0.75L-Step37
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75K-Step36`
- queue rule: hold until R0.75K is verified, then append exactly once to the
  same FIFO task; never create or reuse any other publishing, recap,
  reflection, lessons-learned, usage-notes, or temporary task/system
- frozen research/certificate commit:
  `8eef1888735a7e08bd0e9c988e01677a197f437a`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75L. Do not read or publish R0.75M or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `52e25b2fdf1a224609c9e8fafa1c041b7f09a361f75f4b3e44ebcdddb756cdf5` | `research/r075l_single_harmonic_diffusive_signed_flux_gain.md` |
| `a7578e5370d182decc39f0da2f2fb581e5ef842ae7b914a120b5784bc32bd302` | `research/r075l_single_harmonic_diffusive_signed_flux_gain_primary_audit.md` |
| `a300de54b9fe06e94455a055bbb42bdce8ec7bb004080389a95412966a5b941a` | `research/r075l_report-source.md` |
| `0b9ba1f018b6e52414f20dee6687f5ff55c5ea0ef247ddbd905bc8c204245ad9` | `scripts/r075l_single_harmonic_diffusive_signed_flux_gain_fixtures.json` |
| `9178489eaf9f44c5b182b6080cce7212591b1a3dd86459ecbd82c1382b38db9a` | `scripts/r075l_single_harmonic_diffusive_signed_flux_gain_expected.json` |
| `318136308fb0b1e46046b6483269e70b0a2d57dc44be18616236a10c5271a567` | `research/r075l_single_harmonic_diffusive_signed_flux_gain_certificate.json` |
| `00c490616bdb6641a862152a315ac76861ff345d8654137dea1d5fce552b2772` | `research/r075l_single_harmonic_diffusive_signed_flux_gain_certificate_report.md` |
| `31a67ab57a7c3f591f3e4dbd446dada04720ed62170e7cd0773123acc8d20604` | `research/r075l_single_harmonic_diffusive_signed_flux_gain_independent_audit.md` |
| `387e80857b32e5048210b77a4a685be7a69c8f8e9f8da1514305a1ae96368e63` | `research/r075l_single_harmonic_diffusive_signed_flux_gain_qa_report.md` |
| `a521194d3ab26e23ffc13450244dcd92c52ac774bfb647348ebb2fac09c2571f` | `scripts/r075l_single_harmonic_diffusive_signed_flux_gain_certificate.py` |
| `50888ee85e72c472881eab10145020888eda1558a7a5eb067aaaf5c61b3c307c` | `scripts/r075l_single_harmonic_diffusive_signed_flux_gain_certificate_independent.rb` |
| `fa336a8dad20a400494eeb0b28a91bbb5077396238d094f5bf1621e367b7a175` | `scripts/r075l_single_harmonic_diffusive_signed_flux_gain_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0. Certificate QA: Python 19/19, Ruby 20/20, 120/120 negative
mutation families rejected independently by each implementation, unknown
mutations fail closed, `PYTHONHASHSEED=0,1,42` byte stability, and complete
regeneration byte stability.

## Result and exact boundary

R0.75K shows that a fixed positive adjoint entrance weight destroys the
high-frequency saving even when the physical signed flux vanishes. R0.75L
returns to that physical signed source and proves the first exact
diffusion-compatible frequency gain in the present route, for one real
constant-shear harmonic.

On `[0,T] times T`, let

\[
 \mathcal L_B=\partial_t+B\partial_2-\partial_2^2,
 \qquad
 F_k=Ae^{-k^2t}\cos(k(x_2-Bt)),
\]

where `A>0`, `B` is real, and `k>=1` is an integer. Then
`L_B F_k=0`. For smooth periodic real `xi`, measurable `0<=eta<=1`, and

\[
 \mathcal T_{k,\eta}
 :=\frac12\int_0^T\!\int_0^{2\pi}
 \eta(t)B\partial_2\xi(x_2)|F_k|^2\,dx_2dt,
\]

the zero spatial mode of `F_k^2` cancels against the periodic derivative
before any absolute value is taken. Only frequencies `+/-2k` remain, and

\[
 \boxed{
 |\mathcal T_{k,\eta}|
 \le \frac{A^2|B|V_\xi}{8k^2}
 (1-e^{-2k^2T}),
 }
\]

where `V_xi=int_0^(2pi)|partial_2 xi|`. The exact full-torus cubic mass is

\[
 M_k:=\int_0^T\!\int_0^{2\pi}|F_k|^3
 =\frac{8A^3}{9k^2}(1-e^{-3k^2T}).
\]

If `k^2T>=1`, eliminating `A` gives

\[
 \boxed{
 |\mathcal T_{k,\eta}|
 \le C_*|B|V_\xi k^{-2/3}M_k^{2/3},
 \qquad
 C_*:=\frac18
 \left(\frac9{8(1-e^{-3})}\right)^{2/3}.}
\]

Thus the saving is a genuine diffusion-compatible `k^(-2/3)` factor and
not an amplitude normalization artifact. In the target notation

\[
 p_k^{\rm tor}=R^{-2}\omega M_k,
 \qquad
 \mathfrak X_k^{\rm tor}=\frac\omega R[\mathcal T_{k,\eta}]_+,
\]

one obtains

\[
 \boxed{
 \mathfrak X_k^{\rm tor}
 \le C_*|B|V_\xi R^{1/3}\omega^{1/3}k^{-2/3}
 (p_k^{\rm tor})^{2/3}.}
\]

A separately paid threshold `k>=R^(-kappa)` would make the frequency
exponent strictly stronger than the R0.75G requirement precisely when

\[
 \boxed{
 \kappa>\frac{27163}{71442}
 \approx0.3802105204.}
\]

This last line is only an exponent diagnostic. The theorem is restricted
to one real harmonic under constant shear and uses a full-torus cubic
mass. It does not pay `|B|V_xi`, localize the cubic mass to the frozen
spherical collar, control multimode convolution, treat nonconstant shear,
or prove the low-frequency sector.

The certificate reconstructs the operator signs, exact passive
cancellation, modes `0,+/-2k`, diagonal cancellation before absolute
values, the time primitive, `int|cos(kx)|^3=8/3`, exact cubic mass,
amplitude homogeneity, `C_*`, target normalization, and the strict rational
frequency threshold. The exponential `e^(-3)` is used only through its
symbolic interval and never frozen to a floating-point equality.

G.1, E.24, the full Version-M estimate, complete-clock extraction, fixed
deletion, suitable-weak transfer, regularity, and singularity remain
**OPEN**. The bounded primary-source screen makes no completeness, novelty,
or priority claim. **NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75L research page and synchronized downloadable
PDF, expose every frozen audit/certificate/source artifact, and update the
homepage, latest-research count, navigation, version ledger, and global
index through L. Do not update the cumulative recap at this non-major
milestone and do not invent a formal figure, simulation, DNS result,
multimode theorem, collar estimate, or literature-completeness claim.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; desktop/mobile render inspection; GitHub Pages workflow verification;
and online byte-identity checks. Report the site commit, workflow run,
page/PDF/object counts, and deployed-byte verdict. No second task is
authorized. **NOT CLAY.**
