# R0.76G publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.76G-Step58`
- research label: `R0.76G`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.76F-Step57`
- cumulative recap required: `false`
- retained recap terminal release: `R0.75W-Step48`
- formal scientific figure required: `false`
- core research commit:
  `17b366e477c46d11b4caa5e2026381bbf08e7d62`

This handoff authorizes only R0.76G.  Do not read or publish later material.
Do not create or reuse a second publishing, recap, reflection,
lessons-learned, usage-notes, or temporary task/system.  The sole publisher
must wait until R0.76F-Step57 has been deployed and verified, then append
R0.76G exactly once in the same FIFO task.  The cumulative recap through W
must remain byte-identical.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `20f32790b53f2b0f5cb39b7071bd2cda96ddb4e15f75211e1682f4ba37dd0bb2` | `research/r076g_complete_clock_central_fibre_flux_lower_bound.md` |
| `af47153c4e1f4c5749f68c3f89d7533c5d95f3c0c6f15b0c775a9e35317c807e` | `research/r076g_complete_clock_central_fibre_flux_lower_bound_primary_audit.md` |
| `3aea1d04dce4987c3883c1b93bec04e714ee17b540fb6a99546d084efa326f74` | `research/r076g_report-source.md` |
| `32e1dcf71a77ba0d28e3924fcb7e7aeb4d2840aa08ba2b2e352bb4d20d0464af` | `scripts/r076g_complete_clock_central_fibre_flux_lower_bound_fixtures.json` |
| `0a2d3d086381029941310ae502b4cf9462e025d0c75e62dd87c07334728a6ba8` | `scripts/r076g_complete_clock_central_fibre_flux_lower_bound_expected.json` |
| `0afbee1f11de12cefc85aee64cbdb8c92925ad2db33cdae8d0582b79dbc01f85` | `scripts/r076g_complete_clock_central_fibre_flux_lower_bound_certificate.py` |
| `ea5036ffed18ce5d1ff33addeff6086ab3603bcedf2373ca6dec7ca3e4963fa2` | `scripts/r076g_complete_clock_central_fibre_flux_lower_bound_certificate_independent.rb` |
| `4fdbce0ab1b3b81dd87a07d4852c9b00ba3b3e6790e714f26124aabf2784ff1e` | `scripts/r076g_complete_clock_central_fibre_flux_lower_bound_qa.sh` |
| `dcca5611f40b5de9cfcc76fccc3ed35a0219a8baedbb488574223809686c652d` | `research/r076g_complete_clock_central_fibre_flux_lower_bound_certificate.json` |
| `f77d2e636e65ff07f662adc72fa16f13ab4edb57addf8422536fa67a0b36660c` | `research/r076g_complete_clock_central_fibre_flux_lower_bound_certificate_report.md` |
| `c034a9d3f01e784733fd35052ec4b9574c9ee4596ad44e466d07a78773953a68` | `research/r076g_complete_clock_central_fibre_flux_lower_bound_independent_audit.md` |
| `d12f43049dc3bf151708561a0e8129a0c49d2dd0ca470e008818763519e2ae53` | `research/r076g_complete_clock_central_fibre_flux_lower_bound_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

R0.76F showed that the spatial observation row inherited by R0.76E must
lose exponentially in the number of modes, but its realizing example had
zero drift and hence zero transport flux.  R0.76G closes precisely that
gap for the intermediate central-fibre payment: the obstruction survives a
nonzero drift, the entire frozen clock, and the fully integrated signed
collar flux.

Retain

\[
 a=\frac{32}{63}L,\qquad
 R=e^{-9L^2/40000},\qquad
 \omega=e^{-2L^2/3969},
\]

and set

\[
 m=\left\lfloor\frac{a^2}{1024}\right\rfloor,
 \qquad q=2m+1,qquad \varepsilon=aR,qquad \beta=\frac1{100}.
\]

The explicit real packet is

\[
 f_L(x_2)=A\left(2\sin\frac{x_2+aR/2}{2}\right)^{2m}
 \cos\bigl(3m(x_2+aR/2)\bigr).
\]

Its positive frequencies are exactly `2m,2m+1,...,4m`, so there are
`q=2m+1` modes and the dyadic endpoint equality is `4m=2(2m)`.

Choose the constant drift

\[
 B=-\frac{\beta a}{R},\qquad
 F_L(t,x_2)=e^{t\partial_2^2}f_L(x_2-Bt).
\]

Then `u_L=(0,B,F_L(t,x_2))` is an exact real smooth unforced
three-dimensional Navier--Stokes shear with constant pressure.

## Complete-clock theorem

Translate the frozen absolute clock `61R^2--65R^2` to `0--4R^2`.  In the
scaled variables put

\[
 G_L(s,z)=F_L(R^2s,aRz),\qquad
 H_L=\int_0^4\!\int_{-1/2}^{1/2}|G_L(s,z)|^3\,dzds,
\]

and

\[
 \mathcal S_L=-\beta\int_0^4\!\zeta(s)
 \int_{\mathbb R}W_a(z)|G_L(s,z)|^2\,dzds,
 \qquad
 W_a(z)=-2\pi az\vartheta(a(|z|-1)).
\]

The frozen cutoff satisfies `zeta=1` on the terminal interval `(3,4)`.
For all sufficiently large `L`,

\[
 \boxed{
 \frac{\mathcal S_L}{H_L^{2/3}}
 \ge c_*\beta\left(\frac97\right)^{4m}.}
\]

This is a lower bound for the complete signed flux itself.  It is neither
an absolute-value majorant nor a single-time observation.  Moreover,

\[
 \frac{q(L)}{L^2}\longrightarrow\frac2{3969}>0,
\]

so the complete central-fibre row has an `exp(cq)` obstruction along an
explicit quadratic mode sequence.

## Proof mechanism and exact constants

For a standard real Gaussian `Z`, write

\[
 X=z+\beta s+\frac12+\frac{\sqrt{2s}}aZ.
\]

The periodic heat kernel gives the exact expectation

\[
 G_L(s,z)=A\,\mathbb E\left[
 \left(2\sin\frac{\varepsilon X}{2}\right)^{2m}
 \cos(3m\varepsilon X)\right].
\]

Minkowski's inequality yields

\[
 |G_L(s,z)|\le A\varepsilon^{2m}
 \left(|z+\beta s+1/2|+\frac{4\sqrt m}{a}\right)^{2m}.
\]

On `3/2<=z+beta s+1/2<=8/5`, the sine and carrier errors vanish uniformly
because `m epsilon^2 -> 0` and `m epsilon -> 0`.  Splitting at `|X|=3`
and using

\[
 \mathbb E[|X|^{2m};|X|>3]
 \le\left(\frac95\right)^{2m}\sqrt2\,e^{-49a^2/800}
 =o\bigl((3/2)^{2m}\bigr)
\]

gives `G_L >= (A/2) epsilon^(2m)(3/2)^(2m)` on a fixed subcap during
the whole terminal unit interval.

The central window uses the exact comparison

\[
 \frac{26}{25}+\frac18=\frac{233}{200}<\frac76.
\]

The positive cap is favourable because both the scaled drift and `W_a`
are negative there.  The negative cap is the only adverse contribution;
its base is at most `2/3`, so its ratio to the favourable base `3/2`
decays as `(4/9)^(4m)` and is absorbed.  Dividing the retained flux lower
bound by the central `L^3` upper bound gives the base `9/7` above.

## Frozen normalized consequence

Define only the central-fibre proxy

\[
 M_L^I=a^2R^5H_L,qquad
 p_L^I=R^{-2}\omega M_L^I,qquad
 \mathfrak X_L=\frac\omega R[\mathcal T_L]_+,qquad
 \mathcal T_L=\frac{a^2R^3}{2}\mathcal S_L.
\]

Then

\[
 \liminf_{L\to\infty}\frac1{L^2}
 \log\frac{\mathfrak X_L}{(p_L^I)^{2/3}}
 \ge\frac{4\log(9/7)}{3969}-\frac2{11907}
 >\frac2{35721}>0.
\]

The strict sign uses `log(1+x)>x/(1+x)` at `x=2/7`; no decimal
approximation is needed.

## Full-plateau non-transfer boundary

`M_L^I` is not the full physical three-dimensional plateau mass.  The
actual plateau contains fibres adjacent to the transition cap.  For the
same packet, the initial static envelope contrast between the outer cap
point `z_o=1+s_*/a` and the nearby robust plateau fibre
`z_p=1-3delta_0/a` is only, with
`E_L(z)=(2sin(epsilon(z+1/2)/2))^(2m)`,

\[
 \log\frac{E_L(z_o)}{E_L(z_p)}\le C_{\delta_0,s_*}\frac ma,
\]

not order `m`.  This does not prove a complete spacetime upper bound for
the full-plateau quotient.  It proves only that the central-fibre lower
bound cannot be substituted into R0.76E as a counterexample to its final
physical estimate.

Do not publish this result as a matching lower bound against
`M_(n,R)^plat`, a counterexample to R0.76E/E.24/Version-M, or a result about
regularity or singularity.  The constant background has not been embedded
in the frozen mean-zero inversion-paired Version-M subclass.

## Source and claim boundary

The source report records primary literature on heat observability,
thickness, small-time geometric cost, and Turan--Nazarov/Remez propagation.
Those results explain adjacent exponential observation costs but do not
state the signed shrinking-collar functional above.  The proof imports no
observability theorem; it uses the explicit periodic Gaussian expectation
and elementary moment estimates.  A bounded collision search is not a
novelty or priority proof.

Still open are the matching mode dependence against the full physical
plateau, the optimal exponential base, arbitrary packets, nonconstant
shears, Version-M membership and extraction, arbitrary-field E.24, fixed
deletion, suitable-weak transfer, regularity, and singularity.
**NOT CLAY.**

## Proof and certificate boundary

The primary mathematical audit and a separate final reread report PASS
with zero blockers.  Python and Ruby independently report 120/120 finite
assertions.  Both reject all 120 named mutations and fail closed on an
unknown mutation.  Python output is byte-stable under
`PYTHONHASHSEED=0,1,42`; their exact rational sections and ordered mutation
inventories agree.  Ruby 2.6 compatibility was exercised on this host, and
all declared fixture and expected-value fields are covered.

The core inventory is exactly twelve files.  A clean archive of commit
`17b366e4...` reran the complete QA successfully.  The finite certificates
bind source bytes, the clock and frequency ledgers, exact rational
comparisons, source boundaries, and claim boundaries.  They are not the
continuum proof of the Gaussian limiting lemma.

## Recap and figure boundary

R0.75W remains the terminal milestone recap.  R0.76G is a focused analytic
route-obstruction note, not a cumulative phase recap.  Do not update the
recap.  Preserve its HTML and PDF byte-for-byte and label the terminal
release exactly as `R0.75W-Step48`.

No simulation, DNS result, formal scientific figure, or decorative plot is
claimed or required for R0.76G.

## Publication and deployment QA

Publish one bilingual R0.76G research page and synchronized downloadable
PDF.  Expose all twelve frozen research, audit, source, certificate, and QA
artifacts.  Update the homepage, latest-research count, navigation, research
and literature reviews, version ledger, global notes index, English
translation, and formal archive through R0.76G while keeping the
latest-recap endpoint at R0.75W.

Run structural, equation, internal-link, asset, recap-preservation, and
forbidden-future-version tests; render desktop and mobile views; verify no
overflow or raw TeX leakage.  Commit and push only R0.76G, wait for GitHub
Pages to succeed, and compare every declared online object byte-for-byte
with the release commit.  A push or green workflow alone is not deployment
proof.

Do not add a figure, simulation, full-plateau lower bound,
arbitrary-packet claim, unconditional Version-M claim, regularity claim,
recap change, or second task.  The release is complete only when
R0.76G-Step58 is deployed and verified online, after F and before any later
release.
