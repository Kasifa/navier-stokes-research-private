# R0.75V publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.75V-Step47`
- research label: `R0.75V`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75U-Step46`
- cumulative recap required: `true`
- recap terminal release: `R0.75V-Step47`
- formal scientific figure required: `false`
- core research commit:
  `fc676ef2c0bf501e14c6a0e1f84558e470de6eb8`

This handoff authorizes only R0.75V and its milestone recap.  Do not read or
publish R0.75W or later material.  Do not create or reuse a second publishing,
recap, reflection, lessons-learned, usage-notes, or temporary task/system.
The sole publisher must wait until R0.75U-Step46 has been deployed and
verified, then append V and update the cumulative recap exactly once in the
same FIFO task.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `6917ff77099b6271b005ca90335df589434a38b0a57001893dcae8b02fd34824` | `research/r075v_complete_two_harmonic_flux_payment.md` |
| `cf23652951c5e1721270577c9a32bc476142b439aefa8ee5f62112cfd8bf5cbd` | `research/r075v_complete_two_harmonic_flux_payment_primary_audit.md` |
| `a099949ad6968468389b412e1d250c5e1a788ac046b949d4d69fbcf1501e9811` | `research/r075v_report-source.md` |
| `d2a16f6e718931aebca696d4934fa497be6bceef8c4e301a9851d04d11e622bc` | `scripts/r075v_complete_two_harmonic_flux_payment_fixtures.json` |
| `ebe2cd2b8aad095730eca4b59e5b79e630a28a0f0215fd2cec0024a4593386c6` | `scripts/r075v_complete_two_harmonic_flux_payment_expected.json` |
| `c224095be7795a0236575ecc69143e525f652fcfc45236f51751ac25ee68b0d2` | `scripts/r075v_complete_two_harmonic_flux_payment_certificate.py` |
| `d12e36c8aa30cf39a8184a401e929d42a843aa5a0bdeb4f374543cfd3c88dc92` | `scripts/r075v_complete_two_harmonic_flux_payment_certificate_independent.rb` |
| `9683be163d5a933f77ae092544341f2b7d91993cd6f50137483edeb9b42eeeb1` | `scripts/r075v_complete_two_harmonic_flux_payment_qa.sh` |
| `daa3649b42363368d9db1139a9168d46a7ec44df591e696ea36011288f5a1da5` | `research/r075v_complete_two_harmonic_flux_payment_certificate.json` |
| `9618e0a14bfc36a184381e448e17a59238ad8a02d10c22a8fb7be3546e723c7a` | `research/r075v_complete_two_harmonic_flux_payment_certificate_report.md` |
| `0c8ab0c24a201b53cc9bfd9eaa0c38848e5978ca47ce915493601cf4199aa9da` | `research/r075v_complete_two_harmonic_flux_payment_independent_audit.md` |
| `d5c877711b59c6a29b11f821710bc7d04ec34a5a7d48d782695abfba566c1a30` | `research/r075v_complete_two_harmonic_flux_payment_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

R0.75T proves that the local cubic mass of one high-carrier dyadic pair is
coercive in a sharp scalar beat defect.  R0.75U proves that this defect pays
the low difference-frequency row of the exact signed flux.  R0.75V preserves
the joint cancellation among the two self frequencies and the sum frequency,
then pays that remaining block.  The two estimates combine into a complete
signed-flux theorem for the exact pair.

For

\[
 \begin{aligned}
 F(t,x_2)&=A_t\cos(kx_2-\phi_t)+C_t\cos(mx_2-\psi_t),\\
 A_t&=Ae^{-k^2t},\quad C_t=Ce^{-m^2t},\\
 \phi_t&=\phi+kBt,\quad\psi_t=\psi+mBt,
 \end{aligned}
\]

with `A,C>=0`, `1<=m<k<=2m`, and `maR>=C_0`, the full exact signed collar
flux satisfies

\[
 \boxed{
 |\mathcal T_{k,m,R}|
 \le Ca^{2/3}R^{-1/3}
 \bigl(M_{k,m,R}^{\rm plat}\bigr)^{2/3}.}
\]

With

\[
 p_{k,m,R}^{\rm plat}=R^{-2}\omega M_{k,m,R}^{\rm plat},
 \qquad
 \mathfrak X_{k,m,R}=\frac\omega R[\mathcal T_{k,m,R}]_+,
\]

the scale-free normalized theorem is

\[
 \boxed{
 \mathfrak X_{k,m,R}
 \le Ca^{2/3}\omega^{1/3}
 \bigl(p_{k,m,R}^{\rm plat}\bigr)^{2/3}.}
\]

Every power of `R` cancels, and the exact logarithmic `L^2` rate remains

\[
 \lim_{L\to\infty}\frac1{L^2}
 \log(a^{2/3}\omega^{1/3})=-\frac2{11907}<0.
\]

The new V input is the joint payment of

\[
 \begin{aligned}
 \mathcal E_{k,m,R}
 &=\frac B4\int\eta_R
 [A_t^2J_{2k,R}\sin(2\phi_t)
  +C_t^2J_{2m,R}\sin(2\psi_t)]dt\\
 &\quad+\frac B2\int\eta_RA_tC_tJ_{k+m,R}
 \sin(\phi_t+\psi_t)dt.
 \end{aligned}
\]

The proof never bounds these three rows separately.  Separate absolute
values would lose the quadratic cancellation when the amplitudes agree, the
relative phase is `pi`, and `(k-m)aR` is small.

## Proof and certificate boundary

The analytic proof has six exact pieces:

1. the quotient `K_R(r)=J_(r,R)/r` has a smooth even extension and a
   two-jet retaining both arbitrary high-frequency decay and the first two
   powers of `(k-m)aR`;
2. a quadratic identity pairs the central multiplier with the squared beat
   defect, the odd multiplier difference with one defect factor, and the
   even difference with two;
3. the three physical time phases are integrated separately before the
   common phase is factored, eliminating the shear speed without generating
   a spurious relative-phase derivative;
4. the heat quadratic form contains the exact extra term
   `(k-m)^2K_R(k+m)A_tC_t`, which completes rather than destroys the
   cancellation;
5. a right-endpoint complete-clock trace uses the exact forward heat rates,
   affine phase distance, and the one-zero backward amplitude ratio;
6. Holder, the radial decay, and the frozen T collar coercivity yield
   `a^(2/3)R^(-1/3)M^(2/3)`.

The main and primary audits report PASS with zero blockers.  A final
independent differential audit reports PASS with zero blockers.  The frozen
finite suite reports Python 17/17, Ruby 18/18, rejection of all 84 named
mutation families by both implementations, fail-closed rejection of unknown
mutations, byte stability under `PYTHONHASHSEED=0,1,42`, and regeneration
stability.  Finite checks bind exact algebra and source bytes; they are not
represented as numerical proof of the continuum multiplier-jet or endpoint
lemmas.

The bounded primary-source report gives neighboring context from exact
shearing-wave solutions, shear mixing, torus observability, and the official
Clay statement.  No external theorem is imported into the proof, and no
completeness, novelty, or priority claim is made.

## Claim boundary

R0.75V closes the full signed collar flux only for one exact diffusive
two-harmonic dyadic pair with `maR>=C_0`.  The proof requires the exact
constant forward heat rates `k^2,m^2` and the right endpoint of the complete
clock.  It does not cover arbitrary time-dependent damping or forward
growth.

The exact field `u=(0,B,F(t,x_2))` is smooth and unforced, but its nonzero
constant background has not been shown to belong to the frozen mean-zero,
inversion-paired Version-M subclass.  The Version-M consequence is therefore
conditional on the same realized-subclass and ledger-alignment hypotheses as
R0.75S--U and applies only when `F` is an actual component of that velocity.

Low-carrier pairs, three or more harmonics, arbitrary packets, inter-packet
aggregation, nonconstant or vertically dependent shear, projection from a
larger velocity, arbitrary-field E.24, complete Version-M extraction, fixed
deletion, suitable-weak transfer, regularity, and singularity remain open.
**NOT CLAY.**

## Milestone recap boundary

This release is a milestone because it closes the exact high-carrier
two-harmonic branch opened at R0.75T.  Update the cumulative recap through
exactly `R0.75V-Step47`.  It must distinguish:

- T: spatial collar coercivity and the sharp two-wave beat defect;
- U: complete-clock payment of the difference-frequency component;
- V: joint payment of the two self rows and sum row, hence the complete exact
  pair theorem;
- the unchanged open boundary beginning with low carriers and three or more
  modes.

Do not imply that the recap covers W or later work.  Later ordinary releases
must preserve this recap byte-for-byte until the next genuine milestone.

## Publication and deployment QA

Publish one bilingual R0.75V research page, a synchronized downloadable PDF,
and the milestone recap through V.  Expose all twelve frozen source, audit,
certificate, and QA artifacts.  Update the homepage, latest-research count,
latest-recap endpoint, research review, literature review, navigation,
version ledger, global notes index, English translation, and formal archive
through V.

Run structural, equation, internal-link, asset, recap-range, and
forbidden-future-version tests; render desktop and mobile views; verify there
is no overflow or raw TeX leakage.  Commit and push only V and its recap,
wait for the GitHub Pages workflow to succeed, and compare every declared
online object byte-for-byte with the release commit.  A successful push or
workflow alone is not deployment proof.

Do not add a scientific figure, simulation, DNS change, arbitrary-packet
claim, regularity claim, or second task.  The release is complete only when
R0.75V-Step47 and its recap are deployed and verified online, after U and
before W.
