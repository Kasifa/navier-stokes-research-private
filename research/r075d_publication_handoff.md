# R0.75D Step 29 frozen publication handoff

## Release identity and queue order

- release id: R0.75D-Step29
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75C-Step28`
- queue rule: hold until R0.75C is verified, then append exactly once to the
  same FIFO task; never create or reuse any other publishing, recap,
  reflection, “lessons learned”, or temporary task/system
- frozen research/certificate commit:
  `1e010e638569f14f74fea6c1db89e08c1f63d622`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75D. Do not read or publish R0.75E or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `54bcd703aff9a55f8fff522ded2bf1c5b629ee2497bd4f2255a6224e4bb747f6` | `research/r075d_passive_gradient_route_screen.md` |
| `f06e29971ea3f0b05c7a1c39983a2ae21aa241a8e46f02e2450632e07c5eaef7` | `research/r075d_passive_gradient_route_screen_primary_audit.md` |
| `5c415c3e280fea1569a42d64d99400fe4dfaf440d2808d637ca57cfc1d386c1f` | `research/r075d_report-source.md` |
| `9222dfa3c7051fbe7d5d78405f6ad8071e54b4eed736cd2afae97f96f617c639` | `research/r075d_passive_gradient_route_screen_certificate.json` |
| `24dfb6fa2ce6e1bce280a34a4f16c0d7aa84e75e08fb2408d7c4edae78f506a1` | `research/r075d_passive_gradient_route_screen_certificate_report.md` |
| `1b1c5e6ba1826b291d7fc649ac0db0cf1e5ae91ce3e8800d36c3ffce5f395439` | `research/r075d_passive_gradient_route_screen_independent_audit.md` |
| `f9c97884fa29ab7151f675ca45eb48e1449ce8fd0cd7fee8997df882528cf940` | `research/r075d_passive_gradient_route_screen_qa_report.md` |
| `5a79cafe4c7794367b23447cdfc09ba0ee49536e756074aa28aa219173fb0823` | `scripts/r075d_passive_gradient_route_screen_certificate.py` |
| `1a8066cfc4fe90266ff38163a60e752988699b21871482308bb307455be3b090` | `scripts/r075d_passive_gradient_route_screen_certificate_independent.rb` |
| `2c3b9e359b41f27733b29e301b105c56e73b2435e8d1c7f40a6615cdcef19557` | `scripts/r075d_passive_gradient_route_screen_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0. Certificate QA: Python 20/20, Ruby 23/23, 41/41 negative
mutations rejected independently by each implementation, unknown mutations
fail closed, and `PYTHONHASHSEED=0,1,42` byte stability. The certificate is
finite exact arithmetic/structure evidence only. The primary-source ledger
is release-bound but not certified as a complete literature search.

## Result and exact boundary

For the remaining passive outer-collar row,

\[
 D_{k,R}^{{\rm out},F}
 :=\frac{\omega}{R}\int_{I_{2R}}\!\int
 \eta_R\xi_k^R|\nabla_{23}F|^2,
\]

the localized energy calculation gives the unconditional fallback

\[
 \boxed{
 D_{k,R}^{{\rm out},F}
 \le C L^{2/3}\omega^{1/3}(P_R^M)^{2/3}+C P_R^M.}
\]

Consequently the target (D_{k,R}^{{\rm out},F}\lesssim(P_R^M)^{2/3})
is proved whenever (P_R^M\le1). A low full-spatial-frequency piece is
also paid conditionally below

\[
 K_{\rm low}=cR^{-1}L^{-1/3}\omega^{-1/6},
 \qquad
 L^{-2}\log K_{\rm low}
 =\frac{147163}{476280000}+o(1),
\]

provided a localized Rayleigh bound and separate cubic comparability hold.
Horizontal modal damping alone is insufficient to infer that Rayleigh
bound because the horizontal zero mode can have arbitrarily large vertical
frequency.

The unconditional fallback does not close the frozen common-shear branch:

\[
 p_b\asymp L^2\omega R^{-3},
 \qquad
 \lim_{L\to\infty}L^{-2}\log p_b
 =\frac{27163}{158760000}>0.
\]

Thus (P_R^M\to\infty) there, and the linear term cannot be absorbed by
the small-payment implication. The mixed flux has the desired quadratic
scale under the still-unproved gate

\[
 \boxed{p_b p_F^2\le C(P_R^M)^2.}
\]

The exact conclusion is therefore:

- the small-payment passive outer-dissipation regime is **PROVED**;
- the general (P^{2/3}+P) Caccioppoli fallback is **PROVED**;
- low full-spatial frequency is paid only under the stated conditional
  localization/comparability hypotheses;
- the interaction gate, signed transport improvement, high-frequency local
  capture, intermediate band, commutators, periodic leakage, and complete
  clock remain **OPEN**;
- no exact counterexample is constructed;
- no regularity, singularity, novelty, or priority conclusion is authorized.

Do not present the failure to absorb the linear term as failure of the
target estimate itself. It is a precise limitation of absolute
Hölder/Young treatment on the large-payment branch. **NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75D research page and synchronized downloadable
PDF, expose all frozen audit/certificate/source artifacts, and update the
homepage, latest-research count, navigation, version ledger, and global
index through D. Do not update the cumulative recap at this non-major
milestone and do not invent a formal figure, simulation, DNS result, or
literature-completeness claim.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; desktop/mobile render inspection; GitHub Pages workflow verification;
and online byte-identity checks. Report the site commit, workflow run,
page/PDF/object counts, and deployed-byte verdict. No second task is
authorized. **NOT CLAY.**
