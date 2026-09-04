# R0.76G publication handoff -- independent audit

## Frozen object

- Handoff: `research/r076g_publication_handoff.md`
- Audited SHA-256:
  `2f1811e02b4fc6685dd543ae9844382f3bac077df58d9bae9395f49864a2c1ea`
- Verdict: **PASS**
- Mathematical blockers: **0**
- Release blockers: **0**

## Release identity and queue audit

- The release is exactly `R0.76G-Step58` and its logical predecessor is
  exactly `R0.76F-Step57`.
- The only authorized publication task is
  `01a06480-0532-7fd0-bdf0-57571465a2d4`, titled `发布任务`.
- The contract requires G to enter that same FIFO exactly once after F has
  been deployed and verified.  It forbids a second publisher, recap task,
  reflection task, usage-notes task, or temporary publishing system.
- `cumulative recap required=false`; the retained recap endpoint is
  `R0.75W-Step48` and must stay byte-identical.
- `formal scientific figure required=false`; no simulation, DNS, or
  decorative plot belongs to this analytic release.

## Commit and ledger integrity

Core commit `17b366e477c46d11b4caa5e2026381bbf08e7d62` resolves as a
commit with parent `52ee189e3dfaa2ea0924ed44cd2e1196b2ec3a5b`, the commit
freezing the F handoff.

The core changes exactly twelve paths.  The changed-path set equals the
twelve-row handoff ledger, with no missing or extra file.  For each row,

\[
 \text{ledger SHA}
 =\text{current-file SHA}
 =\text{core-blob SHA}.
\]

Result: **12/12 PASS**.

The principal frozen hashes are:

- Main theorem:
  `20f32790b53f2b0f5cb39b7071bd2cda96ddb4e15f75211e1682f4ba37dd0bb2`
- Primary audit:
  `af47153c4e1f4c5749f68c3f89d7533c5d95f3c0c6f15b0c775a9e35317c807e`
- Source report:
  `3aea1d04dce4987c3883c1b93bec04e714ee17b540fb6a99546d084efa326f74`
- QA report:
  `d12f43049dc3bf151708561a0e8129a0c49d2dd0ca470e008818763519e2ae53`

## Mathematical theorem audit

The handoff retains the exact asymptotic scales
`a=(32/63)L`, `R=exp(-9L^2/40000)`, and
`omega=exp(-2L^2/3969)`.  With

\[
 m=\left\lfloor\frac{a^2}{1024}\right\rfloor,
 qquad q=2m+1,qquad \varepsilon=aR,qquad \beta=\frac1{100},
\]

the real packet has positive frequency support exactly
`{2m,2m+1,...,4m}`.  Hence it has `q` positive modes, no zero mode, and
the exact dyadic equality `4m=2(2m)`.

For `B=-beta a/R`, the shear `u=(0,B,F(t,x_2))` is divergence free and its
only nonlinear term is `(0,0,B partial_2 F)`.  The transported heat equation
therefore embeds it as a smooth unforced three-dimensional Navier--Stokes
solution with constant pressure.

## Clock, heat-kernel, and sign audit

The handoff explicitly resets the frozen complete clock
`61R^2--65R^2` to `0--4R^2`.  The cutoff equals one on the terminal scaled
interval `(3,4)`, which is the interval used for the positive-cap lower
bound.

The scaled heat-kernel variable is correctly

\[
 X=z+\beta s+\frac12+\frac{\sqrt{2s}}aZ.
\]

Minkowski's inequality gives the allowance `4sqrt(m)/a`.  On the coherent
rectangle the Gaussian tail is bounded by

\[
 \left(\frac95\right)^{2m}\sqrt2e^{-49a^2/800}
 =o\bigl((3/2)^{2m}\bigr),
\]

so the good/bad decomposition and Jensen's inequality produce the stated
uniform lower bound.  This limiting argument is in the analytic proof, not
delegated to finite arithmetic.

The scaled drift is negative.  The cross-section `W_a` is negative on the
selected positive cap, making that contribution favourable.  On the
negative cap, `w<0` for large `L`, and the drift reduces its absolute value;
the negative cap is the only adverse contribution.  The adverse-to-positive
base ratio is exactly `(2/3)/(3/2)=4/9`, so its fourth-multiple power is
absorbed.

The central upper base is certified by

\[
 \frac{26}{25}+\frac18=\frac{233}{200}<\frac76,
\]

and division gives the complete signed-flux lower-bound base `9/7`.

## Normalized-rate and claim-boundary audit

The physical conversion and central proxy give the normalized rate

\[
 \frac{4\log(9/7)}{3969}-\frac2{11907}
 >\frac2{35721}>0,
\]

using `log(1+x)>x/(1+x)` at `x=2/7`.  Also
`q(L)/L^2 -> 2/3969`, so the result is an explicit quadratic-mode-density
obstruction for the complete signed flux against the central-fibre proxy.

The denominator is not the full physical plateau mass.  The nearby plateau
fibre sees only an `exp(O(m/a))` initial static contrast from the selected
cap; the note does not turn this observation into a full spacetime quotient
upper bound.  Therefore it correctly makes no counterexample claim against
R0.76E, E.24, or Version-M.

The constant background has not been embedded in the frozen mean-zero,
inversion-paired Version-M subclass.  Full-plateau sharpness, arbitrary
packets, nonconstant shears, Version-M extraction, suitable-weak transfer,
regularity, and singularity remain open.  **NOT CLAY.**

## Source, certificate, and structural audit

The source report separates established heat-observability and
Turan--Nazarov/Remez context from the local Gaussian proof.  It makes no
novelty, priority, or exhaustive-search claim.

- Main tags: G.1--G.40, continuous and unique.
- Main displays: 40 opens / 40 closes.
- Handoff displays: 16 opens / 16 closes.
- UTF-8, control bytes, CR, trailing whitespace, reference closure, bare
  delimiters, and undefined cutoff-radius symbols: PASS.
- Python assertions: 120/120.
- Ruby assertions: 120/120, independently assigned with nil-default
  fail-closed coverage and compatible with the host Ruby 2.6 runtime.
- Named mutations rejected: 120/120 by each implementation.
- Unknown mutations: rejected fail-closed by both implementations.
- `PYTHONHASHSEED=0,1,42`: byte-stable.
- Python/Ruby exact section and ordered mutation inventory: identical.
- Clean archive rerun of core `17b366e4...`: PASS.
- Exact core inventory: 12/12 files.

Finite certificates bind the frozen source bytes, exact arithmetic,
structure, source ledger, and claim boundary.  They are not the continuum
proof.

## Publication boundary

The handoff requests one bilingual reader page, synchronized PDF, site
indexes, and all twelve frozen artifacts, followed by desktop/mobile render
QA and online byte verification.  It preserves the recap endpoint at
R0.75W and forbids future-version leakage.

Publication must not add a formal figure, simulation, full-plateau lower
bound, arbitrary-packet claim, unconditional Version-M claim, regularity
claim, recap change, or second task.  The handoff is internally consistent
and ready for one-time FIFO transfer to the sole publication task after F.
