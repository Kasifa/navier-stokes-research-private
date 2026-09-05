# R0.76L publication handoff -- frozen research release

## Release identity

- release id: `R0.76L-Step63`
- logical predecessor: `R0.76K-Step62`
- publication task: `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- research repository: `/Users/kasifa/Documents/Math/navier-stokes-r074m`
- branch: `codex/r074r-cubic-packing`
- initial scientific source commit: `6fe15fac7db9c3befbb3bab021787dfd6e76639e`
- corrected scientific source commit: `b234b63c24c7b19efc703367e23b092385066a1c`
- certificate commit: `2f3e0f466cc38fd2b61f2c79773352d95b2464e1`
- scientific figure required: `true`, one figure package
- simulation required: `false`
- cumulative recap required: `false`
- retained recap coverage: `R0.76I-Step60`, as specified by the preceding research handoff

The corrected source commit supersedes the initial commit for reading and
hash verification. Its only correction makes the description of the
finite p=0.75 tilt sequence agree with the data and caption: it moves
slightly away from the analytic limit on the displayed grid.

This is one research freeze package, submitted once to the fixed publication
task. The publisher owns its FIFO entry after R0.76K-Step62, reader HTML/PDF,
bilingual text, site navigation, release assets, GitHub Pages, retries, and
online verification. The research task resumes mathematics after this
handoff. This document makes no claim about publication status.

## Frozen file inventory

The following 24 scientific assets must match the certificate commit tree,
except for the figure manifest, which is sealed by the final handoff commit.
The handoff and this inventory's audit are also sealed by that final commit;
they do not hash themselves. The five upstream R0.76K dependencies remain
explicitly bound in the fixture and both certificates.

| SHA-256 | path |
|---|---|
| `13492867aa83ead472d8db8d55c9a5d8c65a2418b1de397e0cffdd845b8a5c7a` | `research/r076l_parabolic_edge_smoothing_complete_clock.md` |
| `cdd0fd35a67e863cc767d889e2d1abc7332ee0c74939834423f2d4c66f62ae9b` | `research/r076l_parabolic_edge_smoothing_complete_clock_certificate.json` |
| `1b96a8e293f2fe43ea1c539e148525052e88c59aa2039788831ba96cb62cb6c9` | `research/r076l_parabolic_edge_smoothing_complete_clock_certificate_report.md` |
| `3c06bfb4ffe45c2b0dac17018e915841582f3ba06def65f15fa3a97b449c159d` | `research/r076l_parabolic_edge_smoothing_complete_clock_independent_audit.md` |
| `5fe138cb857ea9e4c34d8fbb404932be45ed809bd96337248839cd9bd67cd8cb` | `research/r076l_parabolic_edge_smoothing_complete_clock_primary_audit.md` |
| `e607cf82699da1cdd541514535a970ed25507fbf0a70a43b2f31fc8e66a6ebff` | `research/r076l_parabolic_edge_smoothing_complete_clock_qa_report.md` |
| `dfa2f5087cb2729350886ad304fe04958c6b55e1610bf771d4a197c6846f5f80` | `research/r076l_report-source.md` |
| `b0410c57bd31c8a9a955d1d88bd2eec634572addb7a0eeb40f5badb38964cb0d` | `scripts/r076l_parabolic_edge_smoothing_complete_clock_certificate.py` |
| `2bd698e00b62fdd85d2f601df22aa2e0199bf2c26de49fc3ff9bbcac3ca94904` | `scripts/r076l_parabolic_edge_smoothing_complete_clock_certificate_independent.rb` |
| `48dc286d198512034aaee9ce65ef696fe367942c9ea9a6e840ac0e7c31c2f8ed` | `scripts/r076l_parabolic_edge_smoothing_complete_clock_expected.json` |
| `cf442a934bd713ef046f1aa5b6f41ea5a1cfe118e6cef91a30d20a26d16bd1a9` | `scripts/r076l_parabolic_edge_smoothing_complete_clock_fixtures.json` |
| `b434be9cc181882d9dda5a5015a946f9417b173ca3082341bd52fb989a9d6ae9` | `scripts/r076l_parabolic_edge_smoothing_complete_clock_qa.sh` |
| `102e7d96396173cc56cacf0e1552241d617c3d9b94495f1404b74e07c3829316` | `figures/r076l-parabolic-edge/fig-r076l-parabolic-edge/caption.md` |
| `ec613babd5ff988c732bbd9881962e93dc6e5ef2821832eb22a069b843fece28` | `figures/r076l-parabolic-edge/fig-r076l-parabolic-edge/config.json` |
| `bbc7139237a9120d91284c0ddb80c0c73aa93708bb4a8f778f38e1d24d18c96d` | `figures/r076l-parabolic-edge/fig-r076l-parabolic-edge/data.csv` |
| `6de47c8df62ae35fc85e5b1ca2010038dd505d2e15b39caaa1f765b30cf4e7ea` | `figures/r076l-parabolic-edge/fig-r076l-parabolic-edge/figure.pdf` |
| `a5bff2596a6bf9ab0becc41cba0a985744c3b31878c6b11281ca2f4cf891fc75` | `figures/r076l-parabolic-edge/fig-r076l-parabolic-edge/figure.png` |
| `5e9061d5b76b03c60d58cac98320513dc442b7a595604ee9c59697b2e4190662` | `figures/r076l-parabolic-edge/fig-r076l-parabolic-edge/figure.svg` |
| `c6c6e5e6ab980eddf254ec2462b73bc99cc351c05069adb6fb0aefd52719f29f` | `figures/r076l-parabolic-edge/fig-r076l-parabolic-edge/manifest.json` |
| `079a32963e6f9bf72771b647683e83d6264e3c1c365ae0004ac58f29b48ba8a2` | `figures/r076l-parabolic-edge/fig-r076l-parabolic-edge/plot.py` |
| `84569637a2602f6832bbbb2cf2b3fe3fcf9698af2aff088904f3f661ed00430d` | `figures/r076l-parabolic-edge/fig-r076l-parabolic-edge/progress.ndjson` |
| `4c55f693c1ca644edc778d93f2ee232d8ae55a03b44b0c2d0dd20820260dfb2c` | `figures/r076l-parabolic-edge/fig-r076l-parabolic-edge/qa-report.md` |
| `2981e7c156aa9b9807a6c7b92c16d9a99ee48aac4deeb362116eb3849b3fa99d` | `figures/r076l-parabolic-edge/fig-r076l-parabolic-edge/render.cjs` |
| `14f817a9bf9a28dc4f17541f94a26442bee8de83aa2571a6cf92e69cafd517c6` | `figures/r076l-parabolic-edge/fig-r076l-parabolic-edge/resources.csv` |


## Mathematical synopsis

R0.76L continues the exact real dyadic Chebyshev construction from R0.76K.
Let A=a-delta_0, let m be even, and assume

\[
 \sqrt A\ll m=o(A^2),\qquad
 q=m+1,\qquad \mu=(m^2/A)^{1/3}.
\]

For one explicit start-prepaid unforced Navier--Stokes shear with positive
integer frequencies m,...,2m and fixed negative scaled drift -beta/A,
the complete signed collar flux is eventually positive. With the exact
physical flux and full-plateau mass in L.6--L.8, L.11 gives

\[
 c\frac{\beta a^{2/3}}{A(1+\mu^2)}
 e^{[2^{-1/3}\Delta_c-o(1)]\mu}
 \le R^{1/3}\frac{\mathcal T_L}{(M_L^{\rm plat})^{2/3}}
 \le C\frac{\beta a^{4/3}}A(1+\mu^2)^{2/3}e^{C\mu}.
\]

The positive cap gap Delta_c is fixed by L.9--L.10. The exponential edge
factor over the complete clock has scale mu; the earlier static edge
factor has scale mu^(3/2). Polynomial prefactors remain part of the
two-sided statement and must not be omitted from a claim about the full
quotient.

The frozen normalized quantities satisfy

\[
 \lim_{L\to\infty} L^{-2}
 \log\frac{\mathfrak X_L}{(p_L^{\rm plat})^{2/3}}
 =-\frac2{11907}.
\]

This rules out this explicit family in the stated degree window as a
counterexample to the frozen normalized estimate. It is a family-specific
result, not a bound for arbitrary packets.

## Claim and literature boundary

- **LITERATURE-ESTABLISHED:** heat-flow polynomial identities, Gaussian
  convolution, and the classical Chebyshev/Gegenbauer facts listed in
  the source report. Cite its primary sources and preserve its prior-art
  qualifications.
- **PROVED LOCALLY:** the double-scale asymptotic, exact-shear transfer,
  complete-clock sign and full-plateau estimates in L.17--L.66 for the
  explicitly stated family and degree window.
- **FINITE COMPUTATION:** exact rational and cubic-field ledger checks,
  independently implemented Python/Ruby checks, and the 16-row binary64
  diagnostic with archived data, code, and logs.
- **OPEN:** the bulk-exterior saddle and transfer at m comparable with
  A^4, arbitrary packets, the m comparable with A^2 transition, Version-M,
  and all regularity or singularity claims.
- **NOT CLAY:** no Millennium Problem solution, novelty, or priority is claimed.

The formal high-degree prediction L.70--L.72 is not a theorem of this release.
At m=kappa A^4 it predicts a squared cap-to-plateau exponent
Delta_c sqrt(kappa/2) A^2 and the candidate threshold

\[
 \kappa>\frac{2}{1536^2\Delta_c^2}.
\]

The next stage requires new proofs of the bulk saddle, growing-degree
transfer, signed pairing, and full-plateau payment. Do not promote the
formal threshold or a finite diagnostic into an established result.

## Verification and figure transfer

The Python certificate passes 64/64 assertions. The independent Ruby
implementation passes 279/279. Their complete exact objects agree with
the frozen expected JSON. The QA includes 25 observed-ledger corruptions,
26 parsed-input corruptions, 11 arithmetic sensitivity cases, the exact
R-rate cancellation check, and 21 isolated single-byte binding corruptions.
The controls use ordinary validation logic; they do not force failure
flags. Repeated outputs are byte-stable.

The analytic primary audit is separate from these finite certificates.
Certificate PASS does not itself prove continuum asymptotics, a Duhamel
estimate, or the complete-clock theorem.

Figure R0.76L-1 contains three dimensionless panels and 16 data rows.
The package includes vector SVG/PDF, a 600 dpi PNG (4205 x 1701 pixels),
a 178 mm x 72 mm layout, data, parameters, generation/rendering code,
caption, progress/resource logs, checksums, environment, and visual QA.
Its finite p=0.75 tilt sequence moves slightly away from its limit on the
displayed range. Preserve that qualification and the finite-difference
meaning of the third panel.

Run the existing figure validator on the archived package. Link public
figure copies to these same scientific assets. Preserve the established
plain individual-researcher prose and concise retro site style. The
publisher prepares both language versions and the synchronized reader PDF.
This section does not request a cumulative recap.

## Ownership and release handling

Only the fixed publication task receives this package. Use the existing
FIFO and do not create another task for this section or any retry.
Unrelated user changes to AGENTS.md are excluded from the research commit
and release inventory. No site file, deployment, publication queue state,
or online verification was changed by the research freeze operation.
