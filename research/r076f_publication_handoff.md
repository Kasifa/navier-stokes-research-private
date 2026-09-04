# R0.76F publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.76F-Step57`
- research label: `R0.76F`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.76E-Step56`
- cumulative recap required: `false`
- retained recap terminal release: `R0.75W-Step48`
- formal scientific figure required: `false`
- core research commit:
  `ff0254315b2fc4f2aaab1ee6f3f2ddcaaeac7366`

This handoff authorizes only R0.76F.  Do not read or publish later material.
Do not create or reuse a second publishing, recap, reflection,
lessons-learned, usage-notes, or temporary task/system.  The sole publisher
must wait until R0.76E-Step56 has been deployed and verified, then append
R0.76F exactly once in the same FIFO task.  The cumulative recap through W
must remain byte-identical.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `48204fcbf8fe9af3f0fdc7720844c3dd8362d8767caf73de016eda7250b70973` | `research/r076f_exponential_spatial_observation_lower_bound.md` |
| `abcaa220c56d1f90c4b34061191e7cd009b8d911be3f83d705e95aa51b4d84cc` | `research/r076f_exponential_spatial_observation_lower_bound_primary_audit.md` |
| `5e3939710dcfefcbc08b93761d8cdda1e655656a1bcd404b63fcea251ffd5e1e` | `research/r076f_report-source.md` |
| `1b11049ab482eb9b6d6b99cfdabfb4cd0a34ac4f483e3e69c5ec178dce752b5a` | `scripts/r076f_exponential_spatial_observation_lower_bound_fixtures.json` |
| `9703be8236b77e556085f9b358f4128ace4e32920a5391ebc1e2a900b232d37a` | `scripts/r076f_exponential_spatial_observation_lower_bound_expected.json` |
| `2882146fba7376d1f2d83d324c816b763729c59443fa4cb1f5fbcc47778c6994` | `scripts/r076f_exponential_spatial_observation_lower_bound_certificate.py` |
| `191b7ee7c0e7ed9157a33606c0ed00e3d0bd1db374260b26d8d5d5b64807bf32` | `scripts/r076f_exponential_spatial_observation_lower_bound_certificate_independent.rb` |
| `ba4fb4db589a502fa28f4f4d307a46b046b5fe253e12e57487c5da0c52d51546` | `scripts/r076f_exponential_spatial_observation_lower_bound_qa.sh` |
| `0558eab8a7ce5ae36e1614fe0c2184debfa8550c655a86baab590fbb9ee6f259` | `research/r076f_exponential_spatial_observation_lower_bound_certificate.json` |
| `7de8bb9ce8b59704c4097616a14e09366c8cc9031acf2e2692b51bce9a785ea0` | `research/r076f_exponential_spatial_observation_lower_bound_certificate_report.md` |
| `8b90a9ab9b60a17f6e5cfc097f658c80ce4cb410142d72123b72bef6895ab7de` | `research/r076f_exponential_spatial_observation_lower_bound_independent_audit.md` |
| `6cf856c79f89e759eec05f51a8aa80e5abad4c7f04bc743aea26b6d8933eb13d` | `research/r076f_exponential_spatial_observation_lower_bound_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

R0.76E supplies an upper spatial-observation constant of order `exp(Cq)`
for exact real shears with `q` positive modes in one dyadic band.  R0.76F
shows that exponential order is unavoidable for this observation step.

Fix

\[
 q\in\mathbb N,\qquad q\ge2,
 \qquad 0<\delta\le\frac{2\pi}{3},
 \qquad I=[-1/2,1/2],\quad J=[-3/2,3/2].
\]

There are nonnegative amplitudes and real phases for the frequencies

\[
 n_j=q+j-1,
 \qquad 1\le j\le q,
 \qquad n_q=2q-1\le2n_1,
\]

such that the real trigonometric polynomial

\[
 g_{q,\delta}(z)
 =\sum_{j=1}^qA_j\cos(n_j\delta z-\phi_j)
\]

satisfies

\[
 \boxed{
 \frac{
  \|g_{q,\delta}\|_{L^\infty(J)}
  +(q\delta+q)^{-1}\|g_{q,\delta}'\|_{L^\infty(J)}
 }{
  \|g_{q,\delta}\|_{L^3(I)}
 }
 \ge2^{q-1}.}
\]

Consequently a constant uniform or polynomial in `q` cannot replace the
exponential factor in the inherited observation geometry.

## Exact construction and proof

Set `z_*=3/2` and

\[
 H_{q,\delta}(z)
 =e^{iq\delta z}(1-e^{i\delta z})^{q-1}.
\]

Choose `theta` so that `e^(i theta)H(z_*)=|H(z_*)|` and take the real part.
The binomial expansion gives exactly `q` nonnegative amplitudes
`A_(k+1)=binom(q-1,k)` and phases `phi_(k+1)=-theta-kpi` at the positive
integer frequencies `q,...,2q-1`.

On `I`, the modulus is at most

\[
 \left(2\sin\frac\delta4\right)^{q-1},
\]

whereas the aligned endpoint in `J` has modulus

\[
 \left(2\sin\frac{3\delta}{4}\right)^{q-1}.
\]

For `x=delta/4` in `(0,pi/6]`,

\[
 \frac{\sin(3x)}{\sin x}=3-4\sin^2x\ge2.
\]

The interval `I` has length one, so the sup estimate also bounds its
`L^3` norm with no omitted measure factor.  The nonnegative derivative row
can only increase the ratio.

## Exact-shear and asymptotic consequence

Choose `a,R>0` with `delta=aR`, set `B=0`, and use the amplitudes and phases
above in the exact heat shear.  Then the scaled initial fibre is precisely
`g_(q,delta)` and `alpha=qdelta`.  The field embeds as the smooth unforced
solution `u=(0,0,F(t,x_2))` with constant pressure.

If `C_q` denotes any uniform coefficient in the inherited spatial row, then

\[
 \log C_q\ge(q-1)\log2.
\]

Thus optimizing the same observation step cannot replace `exp(Cq)` by a
polynomial.  If `q(L)/L^2` stays positively bounded below along a
subsequence, the observation loss changes the normalized exponential
coefficient there; merely sharpening this row cannot retain the exact
`-2/11907` coefficient.  A small quadratic density could still leave a
negative total exponent, which is a different assertion.

## Source and claim boundary

The general sharpness of the order exponent in measurable Turan--Nazarov
estimates is already known.  Exact trigonometric Remez constants also grow
exponentially with degree for fixed geometry.  The source report records
Nazarov's original paper, Friedland's 2026 preprint, and the
Tikhonov--Yuditskii sharp circle theorem.  R0.76F makes no novelty,
priority, or optimal-base claim.

The local result is only the explicit restriction of the obstruction to
the real positive-frequency dyadic shear fibres and fixed nested intervals
used in R0.76E.  It does not prove an exponential lower bound for the
complete signed collar flux.  Indeed, the realizing example uses `B=0`, so
that complete transport flux vanishes.  A different proof using full
space--time cancellation remains possible.

The result does not address arbitrary packets, nonconstant shear,
arbitrary-field E.24, complete Version-M extraction, fixed deletion,
suitable-weak transfer, regularity, or singularity.  **NOT CLAY.**

## Proof and certificate boundary

The primary audit and an independent counterexample-first reread report
PASS with zero blockers.  The latter checked the endpoint equality factor
at `q=2, delta=2pi/3`, the `delta`-to-zero limit, the real phase mapping,
the dyadic band, the exact-shear embedding, and the no-full-flux boundary.
It also detected a fixture-only `q-delta` typo; the frozen fixture now says
`q*delta`, and both certificate implementations enforce the correction.

Python and Ruby each report 83/83 assertions.  Both reject all 83 named
mutations and fail closed on an unknown mutation.  Python output is
byte-stable under `PYTHONHASHSEED=0,1,42`; the exact sections agree between
the two implementations.  The core inventory is exactly twelve files, and
a clean archive of commit `ff025431...` reran the complete QA successfully.

These finite checks bind the source bytes, dyadic and binomial ledgers,
sample triple-angle identity, and claim boundary.  They are not proof of
the continuum norm inequality, imported Remez theorems, or Navier--Stokes
embedding.

## Recap and figure boundary

R0.75W remains the terminal milestone recap.  R0.76F is a focused analytic
route-obstruction note, not a cumulative phase recap.  Do not update the
recap.  Preserve its HTML and PDF byte-for-byte and label the terminal
release exactly as `R0.75W-Step48`.

No simulation, DNS result, formal scientific figure, or decorative plot is
claimed or required for R0.76F.

## Publication and deployment QA

Publish one bilingual R0.76F research page and synchronized downloadable
PDF.  Expose all twelve frozen research, audit, source, certificate, and QA
artifacts.  Update the homepage, latest-research count, navigation, research
and literature reviews, version ledger, global notes index, English
translation, and formal archive through R0.76F while keeping the
latest-recap endpoint at R0.75W.

Run structural, equation, internal-link, asset, recap-preservation, and
forbidden-future-version tests; render desktop and mobile views; verify no
overflow or raw TeX leakage.  Commit and push only R0.76F, wait for GitHub
Pages to succeed, and compare every declared online object byte-for-byte
with the release commit.  A push or green workflow alone is not deployment
proof.

Do not add a figure, simulation, complete-flux lower bound, arbitrary-packet
claim, unconditional Version-M claim, regularity claim, recap change, or
second task.  The release is complete only when R0.76F-Step57 is deployed
and verified online, after E and before any later release.
