# R0.75T publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.75T-Step45`
- research label: `R0.75T`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75S-Step44`
- cumulative recap required: `false`
- formal scientific figure required: `false`
- core research commit:
  `985b09647f726c420593d4d7fd61b7e9d045a80d`

This handoff authorizes only R0.75T.  Do not read or publish R0.75U or later
material.  Do not create or reuse a second publishing, recap, reflection,
lessons-learned, usage-notes, or temporary task/system.  The sole publisher
must wait until R0.75S-Step44 has been deployed and verified, then append T
exactly once in the same FIFO task.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `822059f8a6248143ff3f36938a2333bee9f909b9166db951e227c426c2e8bc66` | `research/r075t_two_harmonic_collar_coercivity.md` |
| `97d804444737284d7ec40b3ce45389272b1a9f61d1901f7bcebf9ed0eab935e5` | `research/r075t_two_harmonic_collar_coercivity_primary_audit.md` |
| `c2255cdd07f2e490921d93ba7e62a809c0348a9e6136b7fd5537cf3799e4e8d8` | `research/r075t_report-source.md` |
| `939b04eeccb9c96b6d5cb21d49ebc48e7a8387dfccdc08afd2dfd6db77fd4393` | `scripts/r075t_two_harmonic_collar_coercivity_fixtures.json` |
| `cd58217667129d5a2f01dd2b315b86a934de1258be2eefab401f5b66efc127c5` | `scripts/r075t_two_harmonic_collar_coercivity_expected.json` |
| `75e31019f8fe05d35a025e727098e99ebe4e5d8eebd60865e559456650c3a439` | `scripts/r075t_two_harmonic_collar_coercivity_certificate.py` |
| `24ccdc21eca83d8cff18b3ae8a7e3ab293e92e4d765fc70008c9c3ca4f4ddb25` | `scripts/r075t_two_harmonic_collar_coercivity_certificate_independent.rb` |
| `1be6a16dc1bf7eb10900128c3e2b10005ba530e0a168460f8a5c2a3bb19b0fb3` | `scripts/r075t_two_harmonic_collar_coercivity_qa.sh` |
| `85a78058a71b6d381edc14336c05c608719f25b88bad39add88d1e4b853b8966` | `research/r075t_two_harmonic_collar_coercivity_certificate.json` |
| `863b6af73f397691b0b7af1a21c7caadd84f29817c47742d4e8553d2209298b9` | `research/r075t_two_harmonic_collar_coercivity_certificate_report.md` |
| `5b4f2e9d3c68b8f408e5737f5cb7769586e9934792ab110c1626b5e7dec2b50d` | `research/r075t_two_harmonic_collar_coercivity_independent_audit.md` |
| `96fec40029dda57bf6b3ce1a8e50616047b0c92a8462cf6e5b1776236dc837a9` | `research/r075t_two_harmonic_collar_coercivity_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

R0.75S proves complete-clock collar payment for one real harmonic, while
R0.75R shows that plateau-only cubic payment fails for a concentrating packet
with a growing number of modes.  R0.75T resolves the smallest spatial case
between those results: exactly two harmonics in one dyadic frequency band.

For

\[
 f(x_2)=A\cos(kx_2-\phi)+C\cos(mx_2-\psi),
 \qquad A,C\ge0,\quad 1\le m<k\le2m,
\]

set `d=k-m`, `ell=aR`, and

\[
 \begin{aligned}
 \delta_\pi&=\operatorname {dist}
 (\phi-\psi,\pi+2\pi\mathbb Z),\\
 q_{d,\ell}^2&=\min\{1,(d\ell)^2+\delta_\pi^2\},\\
 H_{d,\ell}^2&=(A-C)^2+ACq_{d,\ell}^2.
 \end{aligned}
\]

There is an absolute carrier threshold `C_0` and a positive constant
depending only on the frozen plateau width such that, whenever `maR>=C_0`,

\[
 \boxed{
 \int_{\mathcal S_{a,R}^{\rm plat}}|f(x_2)|^3\,dx
 \ge ca^2R^3H_{d,aR}^3.}
\]

The degeneracy is sharp.  If the amplitudes agree, the relative phase is the
cancelling phase `pi`, and `d aR` is small, both sides have cubic order in
`d aR`.  Thus two-wave destructive interference is represented by one
explicit scalar defect rather than an uncontrolled mode-count loss.

The geometric factor is exact.  On `|x_2|<=aR/2`, every transverse plateau
fibre has area

\[
 4\pi a\delta_0R^2.
\]

For the exact diffusive constant-shear pair with unequal amplitudes
`A_t=Ae^(-k^2t)` and `C_t=Ce^(-m^2t)`, the time-slice theorem gives

\[
 M_{k,m,R}^{\rm plat}
 \ge ca^2R^3\int_0^{T_R}H_{d,aR}(t)^3\,dt,
\]

where the cancelling-phase distance moves by `dBt`.  The proof does not
replace the unequal heat rates by a common dyadic factor.

The exact signed flux has four nonconstant frequencies:

\[
 \begin{aligned}
 \mathcal T_{k,m,R}
 &=\frac B4\int\eta
 [A_t^2J_{2k,R}\sin(2\phi_t)
  +C_t^2J_{2m,R}\sin(2\psi_t)]dt\\
 &\quad+\frac B2\int\eta A_tC_t
 [J_{d,R}\sin(\phi_t-\psi_t)
  +J_{k+m,R}\sin(\phi_t+\psi_t)]dt.
 \end{aligned}
\]

This identifies the remaining hard row: the low difference frequency `d`
has exactly the same moving phase as the defect in the cubic mass.

## Proof and certificate boundary

The analytic proof consists of four exact pieces:

1. central plateau fibres give the area `4 pi a delta_0 R^2`;
2. a regular two-dimensional basis remains uniformly coercive as the beat
   frequency tends to zero;
3. unresolved beats produce
   `(A-C)^2+AC[(d ell)^2+delta_pi^2]`, while resolved beats have a fixed Gram
   gap;
4. Holder converts the quadratic row to the cubic lower bound, and the exact
   heat solution may then be integrated time-slice by time-slice.

The primary and final independent mathematical audits report PASS with zero
blockers.  The frozen finite suite reports Python 14/14, Ruby 15/15,
rejection of all 52 named mutation families by both implementations,
fail-closed rejection of unknown mutations, byte stability under
`PYTHONHASHSEED=0,1,42`, and regeneration stability.  Finite probes bind the
algebraic ledger and are not represented as proof of the continuum
coercivity constants.

The bounded primary-source report gives adjacent context from sparse
Logvinenko--Sereda and torus scale-free observability results.  No external
theorem is imported into the proof, and no completeness, novelty, or
priority claim is made.

## Claim boundary

R0.75T proves only spatial collar coercivity for one two-harmonic dyadic pair
with `maR>=C_0`, plus its exact diffusive time-slice corollary and the
four-frequency flux identity.  It does **not** prove the weighted temporal
difference-frequency estimate, a complete two-harmonic signed-flux payment,
or any estimate for a low-carrier pair.

Three or more harmonics, arbitrary packets, inter-packet aggregation,
nonconstant or vertically dependent shear, projection from a larger
velocity, arbitrary-field E.24, complete Version-M extraction, fixed
deletion, suitable-weak transfer, regularity, and singularity remain open.
The result does not contradict R0.75R.  **NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75T research page and a synchronized downloadable
PDF.  Expose all twelve frozen source, audit, certificate, and QA artifacts.
Update the homepage, latest-research count, research review, literature
review, navigation, version ledger, global notes index, English translation,
and formal archive through T.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; render desktop and mobile views; verify there is no overflow or raw
TeX leakage.  Commit and push only T, wait for the GitHub Pages workflow to
succeed, and compare every declared online object byte-for-byte with the
release commit.  A successful push or workflow alone is not deployment
proof.

Do not add a cumulative recap, scientific figure, simulation, DNS change,
complete two-mode theorem, or second task.  The release is complete only when
R0.75T-Step45 is deployed and verified online, after S and before U.
