# R0.75P Step 41 frozen publication handoff

## Release identity and queue order

- release id: R0.75P-Step41
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75O-Step40`
- queue rule: hold until R0.75O is verified, then append exactly once to the
  same FIFO task; never create or reuse any other publishing, recap,
  reflection, lessons-learned, usage-notes, or temporary task/system
- frozen research/certificate commit:
  `272b4d29a419becd5188721dfdfc88d2a4194082`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75P. Do not read or publish R0.75Q or later
work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `8df38e54514d82102cd3e568e89ec1db93913da3ceac52f1371d77fd79c1b7a6` | `research/r075p_buffered_collar_entrance_concentration.md` |
| `e065759a1df3c118f71dd47ac9b5ded9df40536217f557b3c1155e8bf64d3390` | `research/r075p_buffered_collar_entrance_concentration_primary_audit.md` |
| `fcde6bed847b0628aff7de90a49e8150e4a279fca8e46d7053943fdadf0478ca` | `research/r075p_report-source.md` |
| `9d9bf2a00fbdf58eb85a01a3f7fe931f289a5bc1166430dac1f704e4406ec6d7` | `scripts/r075p_buffered_collar_entrance_concentration_fixtures.json` |
| `cc472fb797c98d61e004c09fb84ba4a29029d72665f60507628c166134b39d31` | `scripts/r075p_buffered_collar_entrance_concentration_expected.json` |
| `acbb41a489120b00a32f75999909f0cabce4f96ac5e8650c3ebfd2e0a35dc0a8` | `research/r075p_buffered_collar_entrance_concentration_certificate.json` |
| `1c9bc9553d1facdab0b385a59480c378dfd516412c38eb3a20e76049745560ac` | `research/r075p_buffered_collar_entrance_concentration_certificate_report.md` |
| `60b042b5830167508f096fe7d990f7d2b5fca99da312f0e6116b8c39c0c7923d` | `research/r075p_buffered_collar_entrance_concentration_independent_audit.md` |
| `81e6ff0eefc1fd4d65b1cd7fc8c950b0e284f7b9c54c4542b1e79c9c6dec1dd7` | `research/r075p_buffered_collar_entrance_concentration_qa_report.md` |
| `5c13e8bb480e4565a4b7be6f6d86a0a963cea5ce9d53495f5e0cf3c7983b1c6c` | `scripts/r075p_buffered_collar_entrance_concentration_certificate.py` |
| `5fb32514dc125462239adc31bc5da58460946d8caaed0d3a1c76d6620b8bfd2c` | `scripts/r075p_buffered_collar_entrance_concentration_certificate_independent.rb` |
| `8c4fbeb7667bdb4f937e66cd73d663fa8cd85538412e538259b9a0128f9a27fb` | `scripts/r075p_buffered_collar_entrance_concentration_qa.sh` |

Primary analytic audit: **PASS**, mathematical blockers 0 and release
blockers 0. Certificate QA: Python 21/21, Ruby 22/22, 132/132 negative
mutation families rejected independently by each implementation, unknown
mutations fail closed, `PYTHONHASHSEED=0,1,42` byte stability, and complete
regeneration byte stability. The root task reran the complete QA suite twice
after the independent audit; both runs passed.

## Result and exact boundary

For one real constant-shear packet with horizontal band and total-frequency
cap

\[
 K\le |n|\le2K,
 \qquad n^2+j^2\le4K^2,
 \qquad K\ge R^{-3/2},
 \qquad |B|\le C_BR^{-2},
\]

assume the canonical radial plateau contains a transported entrance cutoff
whose initial energy satisfies

\[
 E_{\rm in}\ge\mu E_0,
 \qquad 0<\mu\le1.
\]

The moving local-energy identity retains at least half of that energy for
`tau=c_0 mu K^(-2)`. The exact radial fibre length and Holder's inequality
then give

\[
 \boxed{
 M_{K,\rm col}
 \ge c_*a^{-1}\mu^{5/2}K^{-2}E_0^{3/2},
 \qquad
 c_*=\frac{\sqrt2\,\delta_0c_0}{\sqrt\pi}.}
\]

Combining this local cubic lower bound with the R0.75O energy row and the
R0.75N Wiener row yields

\[
 \boxed{
 \mathfrak X_{K,\rm col}
 \le C|B|a^{5/3}\mu^{-5/3}
 R^{1/3}\omega^{1/3}K^{-2/3}
 p_{K,\rm col}^{2/3}.}
\]

At the frozen shear and frequency scales, the coefficient has exponential
rate

\[
 \frac{\rho}{6}-\frac{c_\gamma}{12}
 +\frac{5\sigma\rho}{12}
\]

when `mu>=c_mu R^sigma`. It is strictly negative exactly when

\[
 \boxed{
 0\le\sigma<\sigma_*
 :=\frac15\left(\frac{c_\gamma}{\rho}-2\right)
 =\frac{8558}{178605}.}
\]

The endpoint is excluded because the exponential rate vanishes there while
the retained factor `L^(5/3)` grows.

The final Version-M inclusion is narrower than the packet estimate. It
requires the packet to be an actual coordinate component of the same smooth
velocity measured by `P_R^M`, with the short tube aligned inside the
nonnegative exterior row. Under that additional realized-subclass
hypothesis,

\[
 p_{K,\rm col}\le C P_R^M,
 \qquad
 \boxed{
 \mathfrak X_{K,\rm col}\le C(P_R^M)^{2/3}.}
\]

This pointwise ledger inclusion is not valid for a Littlewood--Paley or
Fourier projection of a larger component. P.3--P.30 do not use the
realization hypothesis, and no arbitrary constant-shear packet is claimed
to realize the frozen inversion-paired zero-trajectory family.

The low-entrance-concentration branch remains open. A torus-scale spatially
spread packet can have entrance fraction of order `L^2R^2`, much smaller
than the sufficient threshold, without being a counterexample to the
signed estimate. The next analytic requirement is a spatially localized
signed heat-kernel or near/far estimate that preserves cancellation.

Nonconstant shear, inter-packet summation, low horizontal differences,
removal of the total upper-frequency cap, arbitrary-field E.24,
complete-clock extraction, fixed deletion, suitable-weak transfer,
regularity, and singularity remain **OPEN**. The bounded primary-source
screen does not establish completeness, novelty, or priority. **NOT CLAY.**

## Publication and deployment QA

Publish one bilingual R0.75P research page and synchronized downloadable
PDF, expose every frozen audit/certificate/source artifact, and update the
homepage, latest-research count, navigation, version ledger, and global
index through P. Do not update the cumulative recap at this non-major
milestone and do not invent a formal figure, simulation, DNS result,
unconditional entrance theorem, arbitrary packet-projection payment, or
literature-completeness claim.

Run structural, equation, internal-link, asset, and forbidden-future-version
tests; desktop/mobile render inspection; GitHub Pages workflow verification;
and online byte-identity checks. Report the site commit, workflow run,
page/PDF/object counts, and deployed-byte verdict. No second task is
authorized. **NOT CLAY.**
