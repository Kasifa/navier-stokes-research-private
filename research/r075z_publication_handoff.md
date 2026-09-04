# R0.75Z publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.75Z-Step51`
- research label: `R0.75Z`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75Y-Step50`
- cumulative recap required: `false`
- retained recap terminal release: `R0.75W-Step48`
- formal scientific figure required: `false`
- core research commit:
  `85e633132cbcde89ec78bfef465f3c0393c27994`

This handoff authorizes only R0.75Z.  Do not read or publish later material.
Do not create or reuse a second publishing, recap, reflection,
lessons-learned, usage-notes, or temporary task/system.  The sole publisher
must wait until R0.75Y-Step50 has been deployed and verified, then append Z
exactly once in the same FIFO task.  The cumulative recap through W must
remain byte-identical.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `30d2811e8747aa2b40b4787e6f169af19d1381b66fc84610327da221168f3d97` | `research/r075z_unresolved_cluster_carrier_current_gate.md` |
| `895d09e0b403c0a6bcf216624527dd6c2bf76f15d7ce5f6b6b0a31b6f64a1eb0` | `research/r075z_unresolved_cluster_carrier_current_gate_primary_audit.md` |
| `9b071b3e020210922834435ea7e5806620479d400eb044f48f34e7b02c259d4c` | `research/r075z_report-source.md` |
| `9bd703f41f4b4823a4b6fe38136bf2a5bef126cf15edb3b54036cf1b80e4f4b0` | `scripts/r075z_unresolved_cluster_carrier_current_gate_fixtures.json` |
| `6043f94b70b6068a58d7716877a5319edc9edfc90b47bfee23ea7baee0ad58d4` | `scripts/r075z_unresolved_cluster_carrier_current_gate_expected.json` |
| `dce8afaee87120d042a046d220aeca5f345cb38d42e306d70f89a8fb211252a1` | `scripts/r075z_unresolved_cluster_carrier_current_gate_certificate.py` |
| `d4d1cc3445694b6eaac4857d812f9272e9a8214efce11e212d0d03f049d86578` | `scripts/r075z_unresolved_cluster_carrier_current_gate_certificate_independent.rb` |
| `6c5f50401ee0e77253f7b6df8b9e5802fac70e756b497457201d602645e5a1da` | `scripts/r075z_unresolved_cluster_carrier_current_gate_qa.sh` |
| `116b2f4a6bf343f602c3c624b1eac550449162aa43d7e4038e886ba2bbf7b839` | `research/r075z_unresolved_cluster_carrier_current_gate_certificate.json` |
| `861d4585b9969bc10d779552ccd0318e71a92700aa7c0c017e8d2e8fbfbd9163` | `research/r075z_unresolved_cluster_carrier_current_gate_certificate_report.md` |
| `9bffb2446e7d2fd5d85628f15079265e0e94252a61c430c59642a016dda6574c` | `research/r075z_unresolved_cluster_carrier_current_gate_independent_audit.md` |
| `0e9e4286ac132a88f47675869ceb55c5c491ceb6c9a16bd6d6511b3bf9ba1f12` | `research/r075z_unresolved_cluster_carrier_current_gate_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

Fix `q` and an ordered dyadic family

\[
 1\le n_1<\cdots<n_q\le2n_1,
 \qquad \ell=aR.
\]

Choosing the R0.75X threshold `C_0=8q` gives an exhaustive split:

1. `n_1 ell<8q`: paid by R0.75X;
2. `n_1 ell>=8q` and every adjacent scaled gap is at least `8q`: paid by
   R0.75Y, including equality;
3. `n_1 ell>=8q` and at least one adjacent scaled gap is below `8q`: the
   unresolved Z-sector.

Cut the Z-sector family at every adjacent gap greater than or equal to
`8q/ell`.  Each maximal non-singleton cluster `C={r,...,s}` has carrier
`N=n_r` and offsets `d_j=n_j-N` with

\[
 0=d_r<\cdots<d_s,
 \qquad d_s\ell<8q(s-r),
 \qquad d_s\le N.
\]

For the cluster analytic signal,

\[
 H_C=e^{-N^2t}e^{iN(y-Bt)}Z_C,
 \qquad
 Z_C=\sum_{j=r}^s A_je^{-(2Nd_j+d_j^2)t}
 e^{i(d_j(y-Bt)-\phi_j)},
\]

the exact envelope equation is

\[
 \boxed{
 \partial_tZ_C+B\partial_yZ_C-\partial_y^2Z_C
 -2iN\partial_yZ_C=0.}
\]

Thus the demodulated cluster is spatially low-band for fixed `q`, but it is
not another member of the real low-carrier equation used in R0.75X.

## Exact square, current, and obstruction

The cluster square splits exactly as

\[
 F_C^2=\frac12e^{-2N^2t}|Z_C|^2
 +\frac12e^{-2N^2t}\operatorname {Re}
 \left(e^{2iN(y-Bt)}Z_C^2\right).
\]

This induces a density block and a carrier block in the cluster collar
flux.  It does not include the cross-cluster products of the full field.

With `Q=|Z_C|^2` and
`J=Im(conj(Z_C) partial_y Z_C)`, the local identity is

\[
 \boxed{
 \partial_tQ+B\partial_yQ-\partial_y^2Q
 =-2|\partial_yZ_C|^2-4NJ.}
\]

The current has a favorable sign only after full-period integration:

\[
 \int_{-\pi}^{\pi}J\,dy
 =2\pi\sum_{j=r}^s d_jA_j^2e^{-2(2Nd_j+d_j^2)t}\ge0.
\]

It has no pointwise sign.  The exact envelope `Z=2-e^{iy}` gives at `y=0`

\[
 Z=1,\qquad Z_y=-i,\qquad J=-1,
 \qquad |Z_y|^2+2NJ=1-2N.
\]

Therefore no carrier-independent constant can absorb `2N|J|` pointwise
into `|Z|^2+|Z_y|^2`.  This closes only the naive proof strategy that takes
the new current in absolute value and recursively applies R0.75X.  It is not
a counterexample to a signed, nonlocal, joint-block, or final cluster-flux
estimate.

## Proof and certificate boundary

The analytic proof has five exact parts:

1. using R0.75X with `C_0=8q` and the exact signed minimum gap to prove the
   exhaustive X/Y/Z partition;
2. cutting at equality or larger gaps and telescoping strict internal gaps
   to obtain the unique maximal clusters and their width bound;
3. differentiating every envelope mode to retain the imaginary drift
   `-2iN partial_y` and the unbounded real rates `2Nd_j+d_j^2`;
4. expanding the complex square and the local density identity without
   discarding the carrier current;
5. using offset orthogonality for the global sign and `Z=2-e^{iy}` for the
   narrow pointwise non-absorption result.

The continuum proof and primary audit report PASS with zero mathematical
and release blockers.  The finite suite reports Python 15/15, Ruby 15/15,
rejection of all 72 named mutation families by both implementations,
fail-closed unknown mutations, byte stability under
`PYTHONHASHSEED=0,1,42`, regeneration stability, and 31/31 equation tags
and displays.  Its exact `q=2`, `ell=1` fixtures cover `(15,16)` in X,
`(16,32)` at the Y equality separator, and `(16,17)` in a nontrivial Z
cluster.  Finite checks bind arithmetic, conventions, signs, structure, and
source bytes; they are not represented as proof of the continuum identities.

The bounded source report records Nazarov, Kovrijkine, Egidi--Veselic,
Friedland--Yomdin, and Jaming--Saba as local-observation context.  No
external theorem is imported into the exact identities, and no completeness,
novelty, or priority claim is made.

## Claim boundary

R0.75Z does not prove the full clustered-sector collar-flux estimate.  It
does not prove that cluster estimates add, that full-field plateau mass
controls each cluster, or that cross-cluster products are paid.  It does not
cover growing `q`, arbitrary packets, nonconstant or vertically dependent
shear, projection from a larger velocity, arbitrary-field E.24, complete
Version-M extraction, fixed deletion, suitable-weak transfer, regularity, or
singularity.  **NOT CLAY.**

The exact field embeds in the same smooth unforced shear test class as
R0.75Y, subject to the same constant-background and Version-M boundary.
Any Version-M consequence remains conditional on the same measurement row,
weight, realized subclass, actual component, and ledger alignment.

## Recap and figure boundary

R0.75W remains the terminal milestone recap.  Z is a route-reduction and
method-obstruction note, not a full cluster-payment theorem or a phase
closure.  Do not update the cumulative recap.  Preserve the W recap HTML
and PDF byte-for-byte and label its terminal release exactly as
`R0.75W-Step48`.

The result is analytic.  Do not create a formal scientific figure,
simulation, DNS result, or decorative plot for Z.

## Publication and deployment QA

Publish one bilingual R0.75Z research page and synchronized downloadable
PDF.  Expose all twelve frozen source, audit, certificate, and QA artifacts.
Update the homepage, latest-research count, navigation, research and
literature reviews, version ledger, global notes index, English translation,
and formal archive through Z while keeping the latest-recap endpoint at W.

Run structural, equation, internal-link, asset, recap-preservation, and
forbidden-future-version tests; render desktop and mobile views; verify
there is no overflow or raw TeX leakage.  Commit and push only Z, wait for
the GitHub Pages workflow to succeed, and compare every declared online
object byte-for-byte with the release commit.  A successful push or workflow
alone is not deployment proof.

Do not add a figure, simulation, full-cluster-payment claim, regularity
claim, recap change, or second task.  The release is complete only when
R0.75Z-Step51 is deployed and verified online, after Y and before any later
release.
