# R0.76H publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.76H-Step59`
- research label: `R0.76H`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.76G-Step58`
- cumulative recap required: `false`
- retained recap terminal release: `R0.75W-Step48`
- formal scientific figure required: `false`
- core research commit:
  `6f3ea9599de24902d6ddbfdcc45d1df7614fe31e`

This handoff authorizes only R0.76H.  Do not read or publish later material.
Do not create or reuse a second publishing, recap, reflection,
lessons-learned, usage-notes, or temporary task/system.  The sole publisher
must process H after G in the existing FIFO.  The cumulative recap through W
must remain byte-identical.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `11490112a1893400a1099dd9f45b906ce78d7dab1ebcf549eaa7870241dc0ef4` | `research/r076h_full_plateau_absorption_for_shifted_packet.md` |
| `91e1f31f3adf19a9f352a8cd6defc8988971e51f0905e4a634f949223992c58d` | `research/r076h_full_plateau_absorption_for_shifted_packet_primary_audit.md` |
| `3e706ae12caace1118f941f92c85bc0a1a11ed4a6e158acf7258918a67616d87` | `research/r076h_report-source.md` |
| `035ff9b04f61c11744668c51e6fd8ef1e35da93de85fab2bd9b971acca79747d` | `scripts/r076h_full_plateau_absorption_for_shifted_packet_fixtures.json` |
| `f80cc1d8b6673a6f18069d6756f605de821ac661561d11295a40c468532e083b` | `scripts/r076h_full_plateau_absorption_for_shifted_packet_expected.json` |
| `65cd03fa1420eaffbf1a0e795d178b13b46829f79811963a724f2c25a9c72b2f` | `scripts/r076h_full_plateau_absorption_for_shifted_packet_certificate.py` |
| `4b1d72ad23b82eb48eef6df96d98bb904aa8f72e4932724ac72557c881c46cb3` | `scripts/r076h_full_plateau_absorption_for_shifted_packet_certificate_independent.rb` |
| `eea1b5f41b4c3959d1bdab214dc4c3b07fa05a0ca0f9a659c7ed8fa4fc565a02` | `scripts/r076h_full_plateau_absorption_for_shifted_packet_qa.sh` |
| `452e46b75a10d7fcb637d85234e1d3f76c471cd4ea1cec6b69b568260a8ff55e` | `research/r076h_full_plateau_absorption_for_shifted_packet_certificate.json` |
| `d9c80bc4af24f7f55046e2b5d13484841d3c430232c586913c10b23cbd425267` | `research/r076h_full_plateau_absorption_for_shifted_packet_certificate_report.md` |
| `f3d301f7b29cd1d5ceb89604d4b14d306e3f1fb47c35a5cce1cd689fc8b16fbd` | `research/r076h_full_plateau_absorption_for_shifted_packet_independent_audit.md` |
| `bff6f11944ce50a875ad5395576b55a0d777f2df41a61f969558c755732cb54c` | `research/r076h_full_plateau_absorption_for_shifted_packet_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

R0.76G proved that one explicit shifted-binomial heat shear creates an
exponentially large complete signed collar flux relative to a central-fibre
proxy.  R0.76H closes the deliberately open physical-denominator check for
that same packet.

The conclusion reverses the apparent candidate: fibres in the full
three-dimensional plateau lie only \(O(1/a)\) from the favourable cap and
absorb its exponential contrast at cost \(\exp(O(m/a))\), not
\(\exp(O(m))\).  The normalized full-plateau quotient therefore decays at
the exact frozen rate.

This is a rigorous candidate-killing result.  It confirms G's central-fibre
theorem and simultaneously proves that G is not a full-plateau
counterexample.

## Frozen packet and physical functionals

Retain

\[
 a=\frac{32}{63}L,\qquad
 R=e^{-9L^2/40000},\qquad
 \omega=e^{-2L^2/3969},
\]

\[
 m=\left\lfloor\frac{a^2}{1024}\right\rfloor,\qquad
 q=2m+1,\qquad \varepsilon=aR,\qquad \beta=\frac1{100}.
\]

With \(y=x_2+aR/2\), set

\[
 f_L(x_2)=A\left(2\sin\frac y2\right)^{2m}\cos(3my),\qquad
 B=-\frac{\beta a}{R},
\]

\[
 F_L(t,x_2)=e^{t\partial_2^2}f_L(x_2-Bt),\qquad
 G_L(s,z)=F_L(R^2s,aRz).
\]

This remains the exact smooth unforced Navier--Stokes shear
\(u=(0,B,F_L(t,x_2))\).  The full frozen plateau mass and signed flux are

\[
 M_L^{\rm plat}
 =\int_0^{4R^2}\int_{\mathcal S_{a,R}^{\rm plat}}
 |F_L(t,x_2)|^3\,dxdt,
\]

\[
 \mathcal S_L=-\beta\int_0^4\zeta(s)
 \int_{\mathbb R}W_a(z)|G_L(s,z)|^2\,dzds,\qquad
 \mathcal T_L=\frac{a^2R^3}{2}\mathcal S_L.
\]

## Exact plateau geometry

The dimensionless \((x_1,x_3)\) cross-section is

\[
 \mathcal A_a(z)
 =\pi\left([(a+\delta_0)^2-a^2z^2]_+
 -[(a-\delta_0)^2-a^2z^2]_+\right).
\]

Consequently,

\[
 M_L^{\rm plat}
 =aR^5\int_0^4\int_{\mathbb R}
 \mathcal A_a(z)|G_L(s,z)|^3\,dzds.
\]

On the inner adjacent strip

\[
 J_{a,p}=
 \left[1-\frac{3\delta_0}{a},1-\frac{2\delta_0}{a}\right],
\]

the area is exactly \(4\pi a\delta_0\).  If

\[
 P_L=\int_0^4\int_{J_{a,p}}|G_L(s,z)|^3\,dzds,
\]

then

\[
 M_L^{\rm plat}\ge4\pi\delta_0a^2R^5P_L.
\]

## Adjacent-strip absorption theorem

For a standard Gaussian \(Z\), define

\[
 \mathcal M_{m,s}(w)
 =\mathbb E\left|w+\frac{\sqrt{2s}}aZ\right|^{2m}.
\]

The moment has the exact nonnegative expansion

\[
 \mathcal M_{m,s}(w)
 =\sum_{\ell=0}^m
 \frac{(2m)!}{(2m-2\ell)!\ell!}
 \left(\frac{s}{a^2}\right)^\ell w^{2m-2\ell}.
\]

On the cap and adjacent strip, \(7/5\le w\le8/5\).  The exact heat
representation gives the uniform relative comparison

\[
 \frac12A\varepsilon^{2m}\mathcal M_{m,s}(w)
 \le G_L(s,z)
 \le A\varepsilon^{2m}\mathcal M_{m,s}(w).
\]

Moreover,

\[
 \left|\partial_w\log\mathcal M_{m,s}(w)\right|
 \le\frac{10m}{7}.
\]

Cap and strip points are at distance at most
\(D/a=(\delta+3\delta_0)/a\).  Thus

\[
 \boxed{
 \frac{[\mathcal S_L]_+}{P_L^{2/3}}
 \le C\beta a^{2/3}
 \exp\left(\frac{20D}{7}\frac ma\right).}
\]

The physical consequence is

\[
 \boxed{
 \frac{[\mathcal T_L]_+}{(M_L^{\rm plat})^{2/3}}
 \le C\beta a^{4/3}R^{-1/3}\exp\left(C\frac ma\right).}
\]

## Matching boxes and exact exponent

Let

\[
 s_0=4-\frac1a,\qquad
 w_*=\frac{77}{50},\qquad
 w_0=w_*-\frac{4\delta_0+\beta}{a},\qquad
 K_0=\mathcal M_{m,s_0}(w_0).
\]

Terminal plateau and positive-cap boxes give

\[
 cR^5A^3\varepsilon^{6m}K_0^3
 \le M_L^{\rm plat}
 \le Ca^2e^{Ca}R^5A^3\varepsilon^{6m}K_0^3,
\]

\[
 c\beta a^{-1}A^2\varepsilon^{4m}K_0^2
 \le\mathcal S_L
 \le C\beta e^{Ca}A^2\varepsilon^{4m}K_0^2.
\]

The adverse negative cap is absorbed because

\[
 Ca\left(\frac{2}{3w_0}\right)^{4m}=o(1),
\]

so the complete signed flux is strictly positive for large \(L\).
Therefore

\[
 c\beta a^{-1/3}e^{-Ca}R^{-1/3}
 \le
 \frac{\mathcal T_L}{(M_L^{\rm plat})^{2/3}}
 \le
 C\beta a^2e^{Ca}R^{-1/3}.
\]

The raw and normalized rates are exactly

\[
 \lim_{L\to\infty}\frac1{L^2}
 \log\frac{\mathcal T_L}{(M_L^{\rm plat})^{2/3}}
 =\frac3{40000},
\]

\[
 \boxed{
 \lim_{L\to\infty}\frac1{L^2}
 \log\frac{\mathfrak X_L}{(p_L^{\rm plat})^{2/3}}
 =-\frac2{11907}<0.}
\]

The factor \(R^{1/3}\) in the normalization cancels the raw
\(R^{-1/3}\) growth exactly; \(\omega^{1/3}\) supplies the remaining
negative rate.

## Claim and source boundary

Publish the theorem only for the explicit R0.76G shifted-binomial packet.
It does not improve R0.76E's uniform \(\exp(Cq)\) loss, prove a
subexponential arbitrary-packet inequality, or rule out every possible
cap-localized packet.  It does not establish E.24, Version-M extraction,
fixed deletion, suitable-weak transfer, regularity, or singularity.

The proof imports no external observability or Remez theorem.  Established
heat-observability and exponential-polynomial papers remain context only.
The bounded source search is not a novelty or priority proof.
**NOT CLAY.**

## Proof and certificate boundary

The primary audit and two independent mathematical rereads report PASS with
zero blockers.  Python and Ruby independently report 126/126 finite
assertions.  Both reject all 126 named mutations and fail closed on an
unknown mutation.  Python output is byte-stable under
`PYTHONHASHSEED=0,1,42`; both implementations produce identical exact
rational sections and ordered mutation inventories.

The core inventory is exactly twelve files.  A clean archive of commit
`6f3ea959...` reran the complete QA successfully.  Finite certificates bind
source bytes, exact geometry, powers, moments, rates, source boundaries, and
claim boundaries.  They are not the continuum proof of the uniform
Gaussian-moment comparison.

## Recap and figure boundary

R0.75W remains the terminal milestone recap.  R0.76H is a focused
candidate-killing note, not a cumulative phase recap.  Do not update the
recap.  Preserve its HTML and PDF byte-for-byte and label the terminal
release exactly as `R0.75W-Step48`.

No simulation, DNS result, formal scientific figure, or decorative plot is
claimed or required for R0.76H.

## Publication and deployment QA

Publish one bilingual R0.76H research page and synchronized downloadable
PDF.  Expose all twelve frozen research, audit, source, certificate, and QA
artifacts.  Update the homepage, latest-research count, navigation, research
and literature reviews, version ledger, global notes index, English
translation, and formal archive through H while keeping the latest-recap
endpoint at R0.75W.

Run structural, equation, internal-link, asset, recap-preservation, and
forbidden-future-version tests; render desktop and mobile views; verify no
overflow or raw TeX leakage.  Commit and push only H, wait for GitHub Pages
to succeed, and compare every declared online object byte-for-byte with the
release commit.  A push or green workflow alone is not deployment proof.

Do not add a figure, simulation, arbitrary-packet theorem, unconditional
Version-M claim, regularity claim, recap change, or second task.  The
release is complete only when `R0.76H-Step59` is deployed and verified
online, after G and before any later release.
