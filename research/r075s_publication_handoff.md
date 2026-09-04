# R0.75S Step 44 frozen publication handoff

## Release identity and queue order

- release id: R0.75S-Step44
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75R-Step43`
- queue rule: hold until R0.75R is deployed and verified, then append exactly
  once to the same FIFO task; never create or reuse any other publishing,
  recap, reflection, lessons-learned, usage-notes, or temporary task/system
- frozen research/certificate commit:
  `0afac1ea57d26466883d89b39b19965dcaaa1e58`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75S.  Do not read or publish R0.75T or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `d2736eaa43443048bd620567c4acd72024dc4c662320a8aa58af31ccc6047ccd` | `research/r075s_full_frequency_single_harmonic_clock_payment.md` |
| `38e2bc95b5785b97df5d85474f3ed6105458a117249710b2c052cebbd769b5eb` | `research/r075s_full_frequency_single_harmonic_clock_payment_primary_audit.md` |
| `ab9771e732204f28d3493ae9db73e7aa62aa980cc15b69dfefb39f226520b2a7` | `research/r075s_report-source.md` |
| `82874592703552c1639c69066ddbf1ab531c135cd92eeae775c20be66cd8260f` | `scripts/r075s_full_frequency_single_harmonic_clock_payment_fixtures.json` |
| `e806089d4649b73649edeed5c0204b81a42dbef79c758283b128ec49a57abd8b` | `scripts/r075s_full_frequency_single_harmonic_clock_payment_expected.json` |
| `da70756ebf873bd9ac9d36cc676e059621cf63069ec8a8c8efc9d2ebe5473b6a` | `research/r075s_full_frequency_single_harmonic_clock_payment_certificate.json` |
| `6580726e22fa1b4af3ab3cfabdb3731b65674cb83479d7524124b456ab132987` | `research/r075s_full_frequency_single_harmonic_clock_payment_certificate_report.md` |
| `2ff691c30692d4742b10d5f28bda4b05f95691ecfd083941e638aef491911462` | `research/r075s_full_frequency_single_harmonic_clock_payment_independent_audit.md` |
| `af318d1aacaa615cbf428631e0da61860668c5ee10c22e418e46df1c7e2e3378` | `research/r075s_full_frequency_single_harmonic_clock_payment_qa_report.md` |
| `3a64a105f8cb01e20d2ec66ac4946beaf66dc726c05c0e9b72c2097fd0947243` | `scripts/r075s_full_frequency_single_harmonic_clock_payment_certificate.py` |
| `93cdcd359c7491a2bd8e48a8f092cad798efac050fd3e806e56f9a3cddbe696e` | `scripts/r075s_full_frequency_single_harmonic_clock_payment_certificate_independent.rb` |
| `b7d8629ea27dd7330784a43965387a8cdea03dc1b1468569260195a1cbcbcaaa` | `scripts/r075s_full_frequency_single_harmonic_clock_payment_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0.  Independent mathematical reread and final difference audit:
**PASS**, blockers 0.  Certificate QA: Python 21/21, Ruby 23/23, 76/76
negative mutation families rejected by each implementation, unknown
mutations fail closed, `PYTHONHASHSEED=0,1,42` byte stability, and complete
regeneration byte stability.

## Result and exact boundary

R0.75Q pays the physical radial-collar flux of one real harmonic only above
three frequency thresholds.  R0.75S removes all of them on the complete
frozen time window

\[
 T_R=t_2-s_R=4R^2.
\]

For every amplitude `A>0`, integer `k>=1`, phase `phi`, and constant shear
`B`, set

\[
 F_k(t,x_2)=Ae^{-k^2t}\cos\bigl(k(x_2-Bt)-\phi\bigr).
\]

Let `eta` be the frozen nondecreasing time cutoff, let `xi_(a,R)` be the
canonical radial cutoff, and let `S_(a,R)^plat` be its plateau shell.  Define

\[
 \begin{aligned}
 \mathcal T_{k,R}
 &:=\frac12\int_0^{T_R}\!\int_{\mathbb T^3}
 \eta B\partial_2\xi_{a,R}|F_k|^2,\\
 M_{k,R}^{\rm plat}
 &:=\int_0^{T_R}\!\int_{\mathcal S_{a,R}^{\rm plat}}|F_k|^3.
 \end{aligned}
\]

The theorem is

\[
 \boxed{
 |\mathcal T_{k,R}|
 \le Ca^{2/3}R^{-1/3}
 \bigl(M_{k,R}^{\rm plat}\bigr)^{2/3}}
\]

uniformly in all four harmonic parameters.  No lower or upper bound on `B`
is needed.

The proof first integrates the radial derivative over the two absent
coordinates:

\[
 D_R(y)=-2\pi y\vartheta(|y|/R-a).
\]

Oddness deletes the constant and cosine rows of `F_k^2`.  The exact flux is
therefore a single sine coefficient times a scalar time phase.  With
`q=kR` and `epsilon=kaR`, that radial coefficient satisfies all three bounds

\[
 |S_{k,R}|\le C_NaR^2
 \min\{\varepsilon,1,q^{-N}\}.
\]

For `epsilon<=2pi`, the harmonic may be almost zero on the shell at one
time.  The local cubic mass then measures the distance to the nearest cosine
node.  A one-dimensional moving-phase lemma proves that either the shear is
too small to create flux or the phase crosses enough plateau mass during the
clock.  For `epsilon>=2pi`, the plateau mass is phase-uniform; bounded-
variation integration by parts gives the time factor `C/k`, and radial
Fourier decay pays the remaining high frequencies.  The two branches overlap
and cover every integer `k>=1`.

After

\[
 p_{k,R}^{\rm plat}=R^{-2}\omega M_{k,R}^{\rm plat},
 \qquad
 \mathfrak X_{k,R}=\frac\omega R[\mathcal T_{k,R}]_+,
\]

the estimate becomes

\[
 \boxed{
 \mathfrak X_{k,R}
 \le Ca^{2/3}\omega^{1/3}
 \bigl(p_{k,R}^{\rm plat}\bigr)^{2/3}.}
\]

Its exact logarithmic `L^2` rate is `-c_gamma/12=-2/11907`; all powers of
`R` cancel.  If the whole time window and plateau tube are aligned with one
existing scale-`2R` exterior row and `F_k` is an actual component of the same
velocity measured there, then `p_(k,R)^plat<=C P_R^M` and this one-harmonic
subclass satisfies the desired `C(P_R^M)^(2/3)` payment.

The field also embeds into the exact global smooth unforced shear

\[
 u_k=(0,B,F_k(t,x_2)),
\]

with constant pressure.  Its nonzero constant background has not been shown
to belong to the frozen mean-zero, inversion-paired Version-M subclass.

## What the positive result changes

The missing low and intermediate frequencies of Q are no longer an
obstruction for a single real harmonic on the complete clock.  The remaining
barrier is structural: the cubic mass of a sum of harmonics is not the sum of
their individual masses, while the signed flux contains every pairwise
difference frequency.  Any next positive step must control this interference
or introduce a payment that survives it.

The result does **not** extend to a Fourier projection of a larger velocity,
two or more harmonics, a nonconstant `x_3` shear, or arbitrary vertical
structure.  It does not contradict the R0.75R concentrated-packet obstruction
because R uses an arbitrary multimode packet rather than one spatially spread
harmonic.

The bounded source screen uses primary records on variable-shear enhanced
dissipation, torus Logvinenko--Sereda estimates, heat observability, and the
official Clay problem.  None is substituted for the local proof, and the
search establishes no completeness, novelty, or priority claim.

## Publication and deployment QA

Publish one bilingual R0.75S research page and synchronized downloadable PDF,
expose every frozen audit/certificate/source artifact, and update the
homepage, latest-research count, navigation, version ledger, and global index
through S.  Present it as a rigorous full-frequency theorem for one exact
subfamily, not as an arbitrary-field estimate.

Do not update the cumulative recap at this non-major milestone and do not
invent a formal figure or simulation.  Run structural, equation,
internal-link, asset, and forbidden-future-version tests; desktop/mobile
render inspection; GitHub Pages workflow verification; and online
byte-identity checks.  Report the site commit, workflow run, page/PDF/object
counts, and deployed-byte verdict.  No second task is authorized.

Multimode interference, packet aggregation, nonconstant shear, arbitrary
vertical structure, Version-M admissibility and aggregation, E.24, complete
clock extraction for the full class, fixed deletion, suitable-weak transfer,
regularity, and singularity remain **OPEN**.  **NOT CLAY.**
