# R0.75W publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.75W-Step48`
- research label: `R0.75W`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75V-Step47`
- cumulative recap required: `true`
- recap terminal release: `R0.75W-Step48`
- formal scientific figure required: `false`
- core research commit:
  `e8e48a510db0c0ed86626c238e4c81c281bcc998`

This handoff authorizes only R0.75W and its milestone recap.  Do not read or
publish R0.75X or later material.  Do not create or reuse a second publishing,
recap, reflection, lessons-learned, usage-notes, or temporary task/system.
The sole publisher must wait until R0.75V-Step47 and its milestone recap have
been deployed and verified, then append W and update the cumulative recap
exactly once in the same FIFO task.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `571b8152e3e5f81becec4dd691488fb5889fac23e94ca7c99bd546399dc320d4` | `research/r075w_full_frequency_two_harmonic_flux_payment.md` |
| `78255a0d84020d1d1c9dc6509ed1cc8eb9a9fdaced21d93e4f586383e4fc9ea0` | `research/r075w_full_frequency_two_harmonic_flux_payment_primary_audit.md` |
| `461ab29f02072eb039c9b57c497a87d04ff95255af68d561c68f4d3224726d7a` | `research/r075w_report-source.md` |
| `2b59973a6901b0a70068a2952e1324fd1780f853508c250821daaab659aa8b1f` | `scripts/r075w_full_frequency_two_harmonic_flux_payment_fixtures.json` |
| `44afc8aebea8e15a4d54adf28fd48f8da28dd61c74e6f87a9ded21667d61867f` | `scripts/r075w_full_frequency_two_harmonic_flux_payment_expected.json` |
| `7d517b429fa0d08f5f2fc61597eb926b12d72fe5543444ea9e4a49094d89a29f` | `scripts/r075w_full_frequency_two_harmonic_flux_payment_certificate.py` |
| `3ecd32cb10eb29f84220fd0110556071bc9637ef06457577291931173bc1e9c4` | `scripts/r075w_full_frequency_two_harmonic_flux_payment_certificate_independent.rb` |
| `3090e129431c03f43fd7aa518d9abe0f6ce74af3e97f50b2c19c65497d1d711a` | `scripts/r075w_full_frequency_two_harmonic_flux_payment_qa.sh` |
| `cd18eca477eb0938703446c6ab9939b4bccaf1f3465e450dfa35cdee758b76c8` | `research/r075w_full_frequency_two_harmonic_flux_payment_certificate.json` |
| `5b5fc6efb2de3e5817c7299cf2b71b3df15eca8caf393e8ccbc85a4796d08284` | `research/r075w_full_frequency_two_harmonic_flux_payment_certificate_report.md` |
| `0e7462c2912bb4be6c63198692014d753d9f57bced48e65543c53e25193315aa` | `research/r075w_full_frequency_two_harmonic_flux_payment_independent_audit.md` |
| `2a6f0b9171b2e1511519510d732c6c4c032fd877e4aa44be480bdc54d799793b` | `research/r075w_full_frequency_two_harmonic_flux_payment_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

R0.75V proves the full signed collar-flux estimate for one exact diffusive
two-harmonic dyadic shear under the high-carrier condition `maR>=C_0`.
R0.75W proves the complementary low-carrier sector without extending the
false pointwise defect used in the high-carrier argument.  The two sectors
combine into a full-frequency theorem for the exact pair

\[
 \begin{aligned}
 F(t,x_2)&=Ae^{-k^2t}\cos(kx_2-\phi-kBt)\\
 &\quad+Ce^{-m^2t}\cos(mx_2-\psi-mBt),
 \end{aligned}
\]

where `A,C>=0`, `1<=m<k<=2m`, and `B` is any real constant.  For every
carrier frequency,

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

the normalized theorem is

\[
 \boxed{
 \mathfrak X_{k,m,R}
 \le Ca^{2/3}\omega^{1/3}
 \bigl(p_{k,m,R}^{\rm plat}\bigr)^{2/3},
 \qquad
 \lim_{L\to\infty}\frac1{L^2}\log(a^{2/3}\omega^{1/3})
 =-\frac2{11907}.}
\]

The exact third-order centre node
`A sin(2my)-2A sin(my)=-A(my)^3+O(A(my)^5)` demonstrates why the old
high-carrier pointwise defect cannot simply be extended to low carriers.
It is not a counterexample to the full signed-flux theorem.

## Proof and certificate boundary

The complementary low-carrier proof has seven exact pieces:

1. scale `t=R^2s`, `x_2=aRz`, `alpha=kaR`, `beta=maR`, and `v=BR/a`, so
   `0<beta<alpha<=2C_0` and
   `G_s+vG_z-a^(-2)G_zz=0`;
2. use the confluent fourth-order spatial equation
   `(partial_z^2+alpha^2)(partial_z^2+beta^2)g=0` and compactness of its
   state matrices to control `g` and `g'` from one local `L^3` observation,
   uniformly through repeated roots and the cubic-polynomial limit;
3. apply the Turan--Nazarov inequality to the at-most-four-term temporal
   exponential polynomial at fixed `z`, giving a right-endpoint trace
   independent of imaginary frequency and frequency gaps;
4. scale the exact radial derivative into the odd kernel
   `W_a(z)=-2*pi*a*z*vartheta(a(|z|-1))` and its compact primitive `Xi_a`;
5. use the exact local energy identity
   `v int W_a G^2=E'-a^(-2)int Xi_a''G^2
   +2a^(-2)int Xi_a|G_z|^2` without dividing by `v`, either frequency,
   an amplitude, or `alpha-beta`;
6. keep the endpoint, cutoff, heat, and localized-dissipation rows together
   to obtain `|v int zeta int W_aG^2|<=CH^(2/3)`;
7. combine the exact flux scaling with the plateau mass lower bound
   `M_plat>=4*pi*delta_0*a^2*R^5*H`, then join the low sector to V.

The main, primary, and independent mathematical audits report PASS with zero
blockers.  The frozen finite suite reports Python 18/18, Ruby 19/19,
rejection of all 89 named mutation families by both implementations,
fail-closed rejection of unknown mutations, byte stability under
`PYTHONHASHSEED=0,1,42`, regeneration stability, 33/33 tagged equations,
34/34 displays, seven frozen bindings, and an exact polynomial fixture for
the local energy identity.  These finite checks bind exact algebra,
structure, and source bytes; they are not represented as numerical proof of
the continuum compactness or Turan--Nazarov lemmas.

The bounded primary-source report records Nazarov's original theorem, a
primary accessible restatement, and the official Clay statement.  It makes
no completeness, novelty, or priority claim.

## Claim boundary

R0.75W closes the carrier-frequency gap only for one exact diffusive dyadic
two-harmonic shear.  It does not cover three or more harmonics, arbitrary
packets, inter-packet aggregation, nonconstant or vertically dependent shear,
or projection from a larger velocity.

The exact pair embeds in the smooth unforced shear `u=(0,B,F(t,x_2))`, but
the nonzero constant background has not been shown to belong to the frozen
mean-zero, inversion-paired Version-M subclass.  The displayed Version-M
consequence therefore remains conditional on realized-subclass and
ledger-alignment hypotheses and on `F` being an actual velocity component.

Arbitrary-field E.24, complete Version-M extraction, fixed deletion,
suitable-weak transfer, regularity, and singularity remain open.  No
numerical experiment, novelty claim, priority claim, or global-regularity
claim is made.  **NOT CLAY.**

## Milestone recap boundary

This release is a milestone because it removes the low-carrier restriction
that remained after V and closes the full-frequency exact two-harmonic
branch.  Update the cumulative recap through exactly `R0.75W-Step48`.  It
must distinguish:

- T: high-carrier spatial collar coercivity and the sharp beat defect;
- U: complete-clock payment of the high-carrier difference-frequency row;
- V: joint payment of the remaining high-carrier self and sum rows;
- W: a different low-carrier local-energy route, followed by the exhaustive
  high/low carrier union;
- the unchanged open boundary beginning with three harmonics, arbitrary
  packets, and the transfer to the full Version-M problem.

Do not imply that the recap covers X or later work.  Later ordinary releases
must preserve this recap byte-for-byte until the next genuine milestone.

## Publication and deployment QA

Publish one bilingual R0.75W research page, a synchronized downloadable PDF,
and the milestone recap through W.  Expose all twelve frozen source, audit,
certificate, and QA artifacts.  Update the homepage, latest-research count,
latest-recap endpoint, research review, literature review, navigation,
version ledger, global notes index, English translation, and formal archive
through W.

Run structural, equation, internal-link, asset, recap-range, and
forbidden-future-version tests; render desktop and mobile views; verify there
is no overflow or raw TeX leakage.  Commit and push only W and its recap,
wait for the GitHub Pages workflow to succeed, and compare every declared
online object byte-for-byte with the release commit.  A successful push or
workflow alone is not deployment proof.

Do not add a scientific figure, simulation, DNS change, arbitrary-packet
claim, regularity claim, or second task.  The release is complete only when
R0.75W-Step48 and its recap are deployed and verified online, after V and
before X.
