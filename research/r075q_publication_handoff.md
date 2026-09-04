# R0.75Q Step 42 frozen publication handoff

## Release identity and queue order

- release id: R0.75Q-Step42
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75P-Step41`
- queue rule: hold until R0.75P is verified, then append exactly once to the
  same FIFO task; never create or reuse any other publishing, recap,
  reflection, lessons-learned, usage-notes, or temporary task/system
- frozen research/certificate commit:
  `1b1d092e96aaca9afe723c40994accbe1aee5031`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75Q. Do not read or publish R0.75R or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `9d7058fd7fbc61136967227507e47b0e866c7a4eeafebae198ab05a23645ed9c` | `research/r075q_spatially_spread_harmonic_collar_payment.md` |
| `92255869e165efdbe72557187dd1fe6e7e4449264dcf8033b285286d50f725be` | `research/r075q_spatially_spread_harmonic_collar_payment_primary_audit.md` |
| `b1fcfece0396b04ae9f59e42ef09957a422c36fa0843730a9fb22919bc24c600` | `research/r075q_report-source.md` |
| `a0954f102de2fbc5ac5fb57fd68ba2ae084cc27743240fac6e3297b81d4410f5` | `scripts/r075q_spatially_spread_harmonic_collar_payment_fixtures.json` |
| `8f3e45bb4a62e2a5bd506fd3cc522610d59115f34411fd85b04c7b72081cb444` | `scripts/r075q_spatially_spread_harmonic_collar_payment_expected.json` |
| `fc53a51af160befea1ffc146256aba31792cd4bd3de36004ff851f3b57d7cc12` | `research/r075q_spatially_spread_harmonic_collar_payment_certificate.json` |
| `b5f8fdd24f7bf4911eadf1fe6fb1aa25ac255dcd0bd7a36dcc239d2e023b591d` | `research/r075q_spatially_spread_harmonic_collar_payment_certificate_report.md` |
| `932d1ef7e14701a08584c926a68951e878a2e3f1a74e03a4a22a8a590faa6c8f` | `research/r075q_spatially_spread_harmonic_collar_payment_independent_audit.md` |
| `356796d82e9857ef94642871509dfcacf2c699c4e683fe00ed2cd946a6fdc6b6` | `research/r075q_spatially_spread_harmonic_collar_payment_qa_report.md` |
| `e9a2758fd7688be5bd5970c28385ef501a1716095c1d673fb81071989e0fe09e` | `scripts/r075q_spatially_spread_harmonic_collar_payment_certificate.py` |
| `4d0a81b580bba7061faefe98777d5ad55330d3b60f6563774e73ec8da9a17bbd` | `scripts/r075q_spatially_spread_harmonic_collar_payment_certificate_independent.rb` |
| `f34eee300896e19372983f027a4a52821872f9f63df2df0fa5236d888f5b9ddc` | `scripts/r075q_spatially_spread_harmonic_collar_payment_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0. Independent audit: **PASS**, blockers 0. Certificate QA: Python
20/20, Ruby 21/21, 180/180 negative mutation families rejected
independently by each implementation, unknown mutations fail closed,
`PYTHONHASHSEED=0,1,42` byte stability, and complete regeneration byte
stability. The root task reran the complete QA suite twice after the
independent audit; both runs passed.

## Result and exact boundary

R0.75P pays a physical collar when a quantified fraction of a packet's
energy is already present in a small entrance disk. R0.75Q proves a
complementary exact benchmark that needs no entrance-concentration
hypothesis. The field is one real constant-shear harmonic,

\[
 F_k(t,x_2)=A e^{-k^2t}\cos(k(x_2-Bt)),
 \qquad A>0,\quad k\in\mathbb N,
\]

independent of `x_1,x_3`. The assumptions are

\[
 k^2T\ge1,\qquad kaR\ge2\pi,\qquad
 k\ge R^{-3/2},\qquad |B|\le C_BR^{-2},
 \qquad a\ge4\delta_0,\qquad (a+\delta)R<\frac\pi2.
\]

For the canonical radial plateau shell, the derivative row obeys

\[
 V_{\xi,3}:=\int_{\mathbb T^3}|\partial_2\xi_{a,R}|\,dx
 \le C_\vartheta a^2R^2.
\]

The constant horizontal row of `F_k^2` cancels exactly against
`partial_2 xi`. The remaining heat-decaying row gives

\[
 |\mathcal T_{k,\eta}^{(3)}|
 \le\frac{A^2|B|V_{\xi,3}}{8k^2}
 \le C_\vartheta A^2|B|a^2R^2k^{-2}.
\]

Every `x_2` interval of length `aR/2` contains enough complete periods of
`|cos|^3`, uniformly in phase. A rectangular subcollar has `x_1` fibre
length at least `4delta_0R`. Together with `k^2T>=1`, this proves

\[
 \boxed{
 M_{k,\rm col}
 \ge c_{\rm box}\delta_0a^2R^3k^{-2}A^3,
 \qquad c_{\rm box}=\frac{2(1-e^{-3})}{9\pi}.}
\]

Eliminating `A` therefore gives the physical-collar payment

\[
 \boxed{
 |\mathcal T_{k,\eta}^{(3)}|
 \le C_\vartheta\delta_0^{-2/3}|B|a^{2/3}k^{-2/3}
 M_{k,\rm col}^{2/3}.}
\]

For
`p_(k,col)=R^(-2)omega M_(k,col)` and
`X_(k,col)=(omega/R)[T_(k,eta)^(3)]_+`, the frozen shear and frequency
bounds leave

\[
 \boxed{
 \mathfrak X_{k,\rm col}
 \le C L^{2/3}R^{-2/3}\omega^{1/3}
 p_{k,\rm col}^{2/3},\qquad
 L^{2/3}R^{-2/3}\omega^{1/3}
 =L^{2/3}e^{-4279L^2/238140000}\longrightarrow0.}
\]

The final Version-M inclusion is a narrower, conditional statement. The
whole time window must lie in the same scale-`2R` exterior measurement
interval, the plateau tube must lie in a row of weight at least `omega`,
and `F_k` must be an actual coordinate component of the same smooth
velocity `v_R` measured by `P_R^M` on that tube. Only under those conditions
does pointwise `|F_k|<=|v_R|` imply

\[
 p_{k,\rm col}\le C P_R^M,
 \qquad
 \boxed{\mathfrak X_{k,\rm col}\le C(P_R^M)^{2/3}.}
\]

This ledger step is not asserted for a Fourier or Littlewood--Paley
projection of a larger component, and it does not assert arbitrary
zero-trajectory realization.

The example genuinely belongs to the low-entrance side of the previous
dichotomy. For any R0.75P entrance cutoff,

\[
 E_0=2\pi^2A^2,
 \qquad
 \frac{E_{\rm in}}{E_0}\le\frac{a^2R^2}{2\pi},
 \qquad
 \frac{a^2R^2}{R^\sigma}\longrightarrow0
 \quad(0\le\sigma<2).
\]

Thus Q closes collar localization for one spatially spread harmonic, but
not for a general low-concentration packet. Two or more horizontal modes,
destructive interference, arbitrary vertical structure, nonconstant shear,
inter-packet and low-difference summation, arbitrary-field E.24,
complete-clock extraction, fixed deletion, suitable-weak transfer,
regularity, and singularity remain **OPEN**.

The primary-source screen includes current mode-by-mode and
streamline-localized passive-scalar estimates, including the 2026
hypocoercive preprint, but none is represented as the spherical-collar
`L^3` theorem proved here. The search is bounded and establishes no
completeness, novelty, or priority claim. **NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75Q research page and synchronized downloadable
PDF, expose every frozen audit/certificate/source artifact, and update the
homepage, latest-research count, navigation, version ledger, and global
index through Q. Do not update the cumulative recap at this non-major
milestone and do not invent a formal figure, simulation, DNS result,
multimode theorem, unconditional Version-M inclusion, arbitrary-field E.24,
or literature-completeness claim.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; desktop/mobile render inspection; GitHub Pages workflow verification;
and online byte-identity checks. Report the site commit, workflow run,
page/PDF/object counts, and deployed-byte verdict. No second task is
authorized. **NOT CLAY.**
