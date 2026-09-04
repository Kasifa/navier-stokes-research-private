# R0.75U publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.75U-Step46`
- research label: `R0.75U`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75T-Step45`
- cumulative recap required: `false`
- formal scientific figure required: `false`
- core research commit:
  `4bc33028aa27e6f47fb3464022a500556f3e34e4`

This handoff authorizes only R0.75U.  Do not read or publish R0.75V or later
material.  Do not create or reuse a second publishing, recap, reflection,
lessons-learned, usage-notes, or temporary task/system.  The sole publisher
must wait until R0.75T-Step45 has been deployed and verified, then append U
exactly once in the same FIFO task.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `f9fb331cf880b20f3b407fe66453bce71517ac1ef2af4fa0863c00325c1022a4` | `research/r075u_two_harmonic_difference_frequency_payment.md` |
| `3687decf19ff49016e101a174d066b355689dcca7a4dc36a941b84994b118d6a` | `research/r075u_two_harmonic_difference_frequency_payment_primary_audit.md` |
| `d0e9356a162b683a33c5b4c49692a62962d2a9c63cccba9eb9d84040aaf4a01f` | `research/r075u_report-source.md` |
| `c654b79a1b3b69078df01000c43fee54fdff39ea64c7bc47e206b114dc20b0c6` | `scripts/r075u_two_harmonic_difference_frequency_payment_fixtures.json` |
| `381e80ca54eee51fb3aab823837f0bfdc28e84353e02c8f41fceed261d6aec12` | `scripts/r075u_two_harmonic_difference_frequency_payment_expected.json` |
| `040474723e1380ac6983c1fe165b910aa94751f7b8884cb7d015848d990a77a3` | `scripts/r075u_two_harmonic_difference_frequency_payment_certificate.py` |
| `77f2b4a6bbf389c54694dfdbf8759264ed10c89cfa2e9d085378f084810f263b` | `scripts/r075u_two_harmonic_difference_frequency_payment_certificate_independent.rb` |
| `26ab61750ecb1bfb5961479543fe32bc2338ae0bccfcf7c977cc26f71165c318` | `scripts/r075u_two_harmonic_difference_frequency_payment_qa.sh` |
| `87e6eb73c58a695a88ddc81948ddfea8257cb3844a1e4412068c28985ee28f5a` | `research/r075u_two_harmonic_difference_frequency_payment_certificate.json` |
| `3d0774651733e2f803cf3b679a0c8ba36a50029a27e88366c5d8bee2344d8b0d` | `research/r075u_two_harmonic_difference_frequency_payment_certificate_report.md` |
| `659dacda5aa67c502b3b6db315d06e9aed8cf4aa8fcd06aa45967b8de57950f8` | `research/r075u_two_harmonic_difference_frequency_payment_independent_audit.md` |
| `180b9301689a510544c8a4b3bf74c3625767cd9f89cb84c4069c1cd56ea8132e` | `research/r075u_two_harmonic_difference_frequency_payment_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

R0.75T proves sharp collar coercivity for one two-harmonic dyadic pair and
identifies a scalar defect that measures cancellation between the two waves.
R0.75U proves that the same defect pays the low difference-frequency row of
the exact signed flux over the complete clock.

Let

\[
 \begin{aligned}
 F(t,x_2)&=A_t\cos(kx_2-\phi_t)+C_t\cos(mx_2-\psi_t),\\
 A_t&=Ae^{-k^2t},\quad C_t=Ce^{-m^2t},\\
 \phi_t&=\phi+kBt,\quad\psi_t=\psi+mBt,
 \end{aligned}
\]

where `A,C>=0`, `1<=m<k<=2m`, `d=k-m`, and `maR>=C_0`.  For the exact
difference-frequency component

\[
 \mathcal D_{k,m,R}
 =\frac B2J_{d,R}\int_0^{T_R}\eta_R(t)A_tC_t
 \sin(\phi_t-\psi_t)\,dt,
\]

R0.75U proves, uniformly in the frequencies, amplitudes, phases, and shear
speed `B`,

\[
 \boxed{
 |\mathcal D_{k,m,R}|
 \le Ca^{2/3}R^{-1/3}
 \bigl(M_{k,m,R}^{\rm plat}\bigr)^{2/3}.}
\]

With

\[
 p_{k,m,R}^{\rm plat}=R^{-2}\omega M_{k,m,R}^{\rm plat},
 \qquad
 \mathfrak X_{k,m,R}^{\rm diff}
 =\frac\omega R[\mathcal D_{k,m,R}]_+,
\]

the normalized estimate is

\[
 \boxed{
 \mathfrak X_{k,m,R}^{\rm diff}
 \le Ca^{2/3}\omega^{1/3}
 \bigl(p_{k,m,R}^{\rm plat}\bigr)^{2/3}.}
\]

Every power of `R` cancels.  The exact logarithmic `L^2` coefficient remains

\[
 \lim_{L\to\infty}\frac1{L^2}
 \log(a^{2/3}\omega^{1/3})=-\frac2{11907}<0.
\]

The central analytic ingredient is a weighted moving-phase lemma.  If
`zeta(0)=0`, `0<=zeta<=1`, and `|zeta'|<=C_eta`, then for every
`Lambda>=0`, `sigma in R`, and phase `alpha`,

\[
 \left|\sigma\int_0^4\zeta(s)e^{-\Lambda s}
 \sin(\alpha+\sigma s)\,ds\right|
 \le C\left(\int_0^4e^{-3\Lambda s/2}h(s)^3\,ds\right)^{2/3},
\]

where

\[
 h(s)=\min\{1,\operatorname {dist}
 (\alpha+\sigma s,\pi+2\pi\mathbb Z)\}.
\]

The estimate is uniform across slow and fast phase motion and weak and strong
heat damping.  It is proved analytically; fixed-grid fast-phase quadrature is
explicitly excluded because it can alias the oscillations.

## Proof and certificate boundary

The analytic proof has five exact pieces:

1. the radial sine coefficient obeys `|J_(n,R)|/n<=Ca^2R^3` for every
   integer `n>=1`;
2. the phase-distance cubic moment on the effective heat interval supplies
   the sharp `tau^(2/3)q^2` lower scale;
3. the slow low-heat, slow high-heat, and fast bounded-variation regimes
   prove the weighted moving-phase lemma uniformly in `B`;
4. time nondimensionalization cancels the amplitude product exactly and
   produces the factor `d^(-1)R^(-4/3)`;
5. the radial quotient and R0.75T collar mass then give the stated
   `a^(2/3)R^(-1/3)` estimate and the normalized scale-free bound.

If `AC=0`, the difference-frequency component vanishes, so no division by a
zero amplitude is used.  The main and primary audits report PASS with zero
blockers.  The frozen finite suite reports Python 16/16, Ruby 17/17,
rejection of all 61 named mutation families by both implementations,
fail-closed rejection of unknown mutations, byte stability under
`PYTHONHASHSEED=0,1,42`, and regeneration stability.  Finite checks bind the
algebra and release ledger; they are not represented as numerical proof of
the continuum phase lemma.

The bounded primary-source report supplies adjacent context only.  No
external theorem is imported into the proof, and no completeness, novelty,
or priority claim is made.

## Claim boundary

R0.75U pays only the difference-frequency component of one exact diffusive
two-harmonic dyadic pair with `maR>=C_0`.  The exact shear
`u=(0,B,F(t,x_2))` is smooth and unforced, but its nonzero constant
background has not been shown to belong to the frozen mean-zero,
inversion-paired Version-M subclass.  The Version-M consequence is therefore
conditional on the same realized-subclass and ledger-alignment hypotheses as
R0.75S and applies only when `F` is an actual component of that velocity.

The two self-frequency rows `2k,2m` and the sum-frequency row `k+m` remain
open as a combined block.  Hence R0.75U is not a complete two-harmonic signed
flux theorem.  Low-carrier pairs, three or more harmonics, arbitrary packets,
inter-packet aggregation, nonconstant or vertically dependent shear,
projection from a larger velocity, arbitrary-field E.24, complete Version-M
extraction, fixed deletion, suitable-weak transfer, regularity, and
singularity remain open.  **NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75U research page and a synchronized downloadable
PDF.  Expose all twelve frozen source, audit, certificate, and QA artifacts.
Update the homepage, latest-research count, research review, literature
review, navigation, version ledger, global notes index, English translation,
and formal archive through U.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; render desktop and mobile views; verify there is no overflow or raw
TeX leakage.  Commit and push only U, wait for the GitHub Pages workflow to
succeed, and compare every declared online object byte-for-byte with the
release commit.  A successful push or workflow alone is not deployment proof.

Do not add a cumulative recap, scientific figure, simulation, DNS change,
complete two-mode theorem, or second task.  The release is complete only when
R0.75U-Step46 is deployed and verified online, after T and before V.
