# R0.75R Step 43 frozen publication handoff

## Release identity and queue order

- release id: R0.75R-Step43
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75Q-Step42`
- queue rule: hold until R0.75Q is deployed and verified, then append exactly
  once to the same FIFO task; never create or reuse any other publishing,
  recap, reflection, lessons-learned, usage-notes, or temporary task/system
- frozen research/certificate commit:
  `0b7a57c826823d14bfad66913556e8ed88584325`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75R.  Do not read or publish R0.75S or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `e5eba5b262a8e140eaa149b6d914f355f2f3c636ec1e74cf85515f1c38fd32f3` | `research/r075r_outer_cap_spectral_concentration_obstruction.md` |
| `9b52e3d54fce43c609f70f0b8e71c53def0b4b705144be39a7b62e88d5e07355` | `research/r075r_outer_cap_spectral_concentration_obstruction_primary_audit.md` |
| `767bfc43f9510a2acdf7fbff9d52624ed23ed80e4c3af174c77a47c3824d87ed` | `research/r075r_report-source.md` |
| `226b7411967f2fa6f1960d29a03f32ef40945af47c6545c3f60e4115e507a1d1` | `scripts/r075r_outer_cap_spectral_concentration_obstruction_fixtures.json` |
| `25d46dc6276a42f764dc503100750186213186368aebc9d94be409cd80f3c251` | `scripts/r075r_outer_cap_spectral_concentration_obstruction_expected.json` |
| `9dcd06306bef05f33f88c09e982e97f04b3fd5a3ee9542e2e063c083a535a3ac` | `research/r075r_outer_cap_spectral_concentration_obstruction_certificate.json` |
| `40d17a2b3ddc7c2ee024c0e6288101eded441effa468d22555a1a8cb38c4d65f` | `research/r075r_outer_cap_spectral_concentration_obstruction_certificate_report.md` |
| `aac8e1a9fb01f9ba5b1e41d2ac25c9ee40a97e001a65e7c16a1dc1521dcf89dc` | `research/r075r_outer_cap_spectral_concentration_obstruction_independent_audit.md` |
| `f9fa78b9a4dc918a318a64cff38408e0b3508a83446225532989651718884b19` | `research/r075r_outer_cap_spectral_concentration_obstruction_qa_report.md` |
| `2c712cc35f53063212466a9c26b094d100a39809b8d424cc4062eb5b062d4e86` | `scripts/r075r_outer_cap_spectral_concentration_obstruction_certificate.py` |
| `2da9b4d9cbc53c7e0bb33f834f658b72ec7cfe88bacb215d221612a2dfa4283e` | `scripts/r075r_outer_cap_spectral_concentration_obstruction_certificate_independent.rb` |
| `266b8c2143f02e6f47365859d1343fcc1668601b977521783cadf939f0458aa5` | `scripts/r075r_outer_cap_spectral_concentration_obstruction_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0.  Independent mathematical reread: **PASS**, blockers 0 after one
incorrectly untranslated heat-kernel tail formula was corrected.  Certificate
QA: Python 21/21, Ruby 23/23, 76/76 negative mutation families rejected by
each implementation, unknown mutations fail closed, `PYTHONHASHSEED=0,1,42`
byte stability, and complete regeneration byte stability.

## Result and exact boundary

R0.75Q proves a favorable plateau-shell payment for one spatially spread
harmonic.  R0.75R shows that this particular payment cannot be extended
uniformly to arbitrary high-band multimode packets.

For the canonical radial cutoff, integrating the derivative over the two
coordinates absent from the field gives the exact cross-sectional identity

\[
 D_R(y):=\int_{\mathbb T^2_{x_1,x_3}}\partial_2\xi_{a,R}\,dx_1dx_3
 =-2\pi y\vartheta(|y|/R-a).
\]

Choose a positive outer-cap point `y_0=(a+s_*)R` strictly beyond the
`x_2` projection of the plateau.  For fixed `m>=1`, let `K` be the smallest
multiple of `16m` above `R^(-3/2)` and set

\[
 n=\frac{K}{16m},\qquad q=\frac{3K}{2},\qquad
 G_K(y)=A d_n(y-y_0)^{2m}\cos(q(y-y_0)),qquad T=K^{-2}.
\]

The normalized Dirichlet kernel `d_n` gives the exact real spectral support

\[
 \operatorname {supp}\widehat G_K
 \subset\left\{j:\frac{11K}{8}\le|j|\le\frac{13K}{8}\right\}
 \subset\{j:K\le|j|\le2K\}.
\]

With `B=-bR^(-2)` for a fixed small `b>0`, define

\[
 F_K(t,y)=e^{t\partial_2^2}G_K(y-Bt),qquad
 u_K(t,x)=(0,B,F_K(t,x_2)).
\]

This is an exact global smooth unforced three-dimensional Navier--Stokes
solution with constant pressure.  Over one diffusive time, the drift is at
most `bR`, the packet retains a fixed fraction of its `L^2` mass in the
positive outer cap, and Gaussian leakage to the negative cap is negligible.
The signed flux and plateau mass therefore satisfy

\[
 \boxed{
 \mathcal T_K\ge c_m|B|aRA^2n^{-1}K^{-2},\qquad
 M_{K,{\rm plat}}\le
 C_mA^3a^2R^3K^{-2}(nR)^{-6m}.}
\]

The first inequality is a lower bound: `B<0` and the exact radial identity
make the positive-cap contribution favorable; the only adverse negative-cap
term is absorbed by the separated heat tail.  The second inequality follows
because the plateau sees only the Dirichlet tail at distance comparable to
`R`.

For
`p_(K,plat)=R^(-2)omega M_(K,plat)` and
`X_K=(omega/R)[T_K]_+`, the quotient obeys

\[
 \boxed{
 \frac{\mathfrak X_K}{p_{K,{\rm plat}}^{2/3}}
 \ge c_mbL^{-1/3}R^{-2m-1/6}\omega^{1/3}
 =c_mbL^{-1/3}e^{\kappa_mL^2},}
\]

where

\[
 \kappa_m=\frac{(2m+1/6)\rho}{4}-\frac{c_\gamma}{12}>0.
\]

For the smallest packet power,

\[
 \kappa_1=\frac{304373}{952560000}>0,
 \qquad
 R^{-13/6}\omega^{1/3}=R^{-304373/214326}.
\]

Thus no constant independent of `L` can make

\[
 \mathfrak X_K\le C p_{K,{\rm plat}}^{2/3}
\]

hold for every such high-band packet.  The amplitude cancels exactly.  This
is a geometric and spectral obstruction, not a large-amplitude artifact.

## What the negative result changes

The next positive argument cannot replace a multimode packet by the cubic
mass on the plateau without additional information.  It must instead use a
payment covering the full signed-flux cap, impose a quantitative spreading
or thickness hypothesis, find a signed multimode cancellation, or transfer
outer-cap mass into an already counted Version-M row.

The result does **not** refute the full cutoff-support payment, Version-M, or
E.24.  The full Version-M exterior rows see more than the plateau atom and
may count the constant background.  This exact solution has also not been
embedded in the frozen mean-zero, inversion-paired Version-M subclass.  It is
globally smooth, so it supplies no singularity mechanism.

The bounded source screen uses primary records on torus
Logvinenko--Sereda estimates, thickness-dependent heat observability, and
Davies--Gaffney/Gaussian off-diagonal bounds.  Those results are compatible
with the explicit construction and are not substituted for its local proof.
The search establishes no completeness, novelty, or priority claim.

## Publication and deployment QA

Publish one bilingual R0.75R research page and synchronized downloadable PDF,
expose every frozen audit/certificate/source artifact, and update the
homepage, latest-research count, navigation, version ledger, and global index
through R.  Present it as a rigorous negative result that eliminates a
plateau-only multimode route, not as a failure of all localization or signed
methods.

Do not update the cumulative recap at this non-major milestone and do not
invent a formal figure or simulation.  Run structural, equation,
internal-link, asset, and forbidden-future-version tests; desktop/mobile
render inspection; GitHub Pages workflow verification; and online
byte-identity checks.  Report the site commit, workflow run, page/PDF/object
counts, and deployed-byte verdict.  No second task is authorized.

Full-support payment, Version-M admissibility and aggregation, E.24,
complete-clock extraction, fixed deletion, suitable-weak transfer,
regularity, and singularity remain **OPEN**.  **NOT CLAY.**
