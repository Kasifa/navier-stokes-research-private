# R0.75B Step 27 frozen publication handoff

## Release identity and queue order

- release id: R0.75B-Step27
- publication owner: the single active long-lived Codex task `发布任务`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.75A-Step26`
- queue rule: hold until R0.75A is verified, then append exactly once to the
  same FIFO task; do not use the archived same-name task or create any new
  publishing, recap, reflection, or “lessons learned” task/system
- frozen research/certificate commit:
  `29ade05d496c93e5eb9db74e3f462e2207d505f0`
- cumulative recap required: **false**
- formal scientific figure required: **false**

This handoff authorizes only R0.75B.  Do not read or publish R0.75C,
R0.75D, or later work.

## Frozen ledger

| SHA-256 | repository path |
|---|---|
| `430feb9efc151e2b968dd1b7f785a19dc0e38416270ff8ed0275cfc6429b1a5a` | `research/r075b_bulk_clock_outer_padding_gate.md` |
| `8f4c2b6c28c63acce86a191ec3bc32602ce9e64e3df80eef8534f2e15a255209` | `research/r075b_bulk_clock_outer_padding_gate_primary_audit.md` |
| `6cef708d967fc0e7f47bc87d14496a1d2ff67aa6101a49ebe0f29c4f2d7a023a` | `research/r075b_literature_collision_note.md` |
| `04ba3c9971defcf87971fc1d7722ca925074445826c437da9baa5438b9b4d0c0` | `research/r075b_bulk_clock_outer_padding_gate_certificate.json` |
| `ae5f533e57e4588b1d973a1abb34fbde3f9547f01577be8f8121b840d3e44ae2` | `research/r075b_bulk_clock_outer_padding_gate_certificate_report.md` |
| `9d18cc14a72030e6e98d17f9f51ef26515ceecebd80b020ef0c86d1d74715c7f` | `research/r075b_bulk_clock_outer_padding_gate_independent_audit.md` |
| `14e6d7159d32b3b11c58651e3e89513f46d69f0ebc40c4ec8a76e4cae2db6a45` | `research/r075b_bulk_clock_outer_padding_gate_qa_report.md` |
| `35cd3e2608fe143a4c092e48e16563b237fe39622bd06b5712f6b5eae18b9a08` | `scripts/r075b_bulk_clock_outer_padding_gate_certificate.py` |
| `0004da4bc794a6dbc844529db6c0e572e5ad05d9ee9948aaf82ef95ae6f72146` | `scripts/r075b_bulk_clock_outer_padding_gate_certificate_independent.rb` |
| `8ab21a4b11c4d56e88e7e405acbc9cf6d748a276d304336b10d3cd32f5226794` | `scripts/r075b_bulk_clock_outer_padding_gate_qa.sh` |

Primary analytic audit: **PASS**, blockers 0.  Certificate QA: Python 8/8,
Ruby 9/9, 20/20 and 21/21 negative mutations rejected, 47 unique tags and
resolved references, and `PYTHONHASHSEED=0,1,42` byte stability.  The
certificate proves only exact arithmetic, source binding, and structural
sentinels.

The literature object is a bounded primary-source collision screen.  It
confirms that local-energy/Caccioppoli estimates are established methods and
finds no direct statement of this frozen weighted ledger in the screened
sources.  This is not a novelty or priority determination.

## Result and exact boundary

For every smooth periodic inversion-paired exact common-shear field

\[
 u=(F,b,0),\qquad
 (\partial_t+b\partial_2-\Delta_{23})F=0,
 \qquad \partial_tb-\partial_3^2b=0,
\]

put \(k=k_2-1\), \(\omega=\Gamma^{1/4}\), and split the frozen shell
cutoff into a safe part and the outer transition collar.  The safe completed
subclock satisfies

\[
 \boxed{
 K_{k,R}^{\rm safe}(t_2)
 \le CLR^{-1}\omega^{5/6}(P_R^M)^{2/3},}
\]

with favorable exact rate

\[
 \frac\rho4-\frac{5c_\gamma}{24}
 =-\frac{92837}{476280000}<0.
\]

The entire endpoint row is also paid.  The outer-collar endpoint dichotomy
gives

\[
 (P_R^M)^{2/3}
 \ge cH_{k,R}^{\rm out}(t_2)
 R^{2/3}\omega^{-1/3}L^{-2/3},
\]

with gain

\[
 \frac{c_\gamma}{12}-\frac\rho6
 =\frac{4279}{238140000}>0.
\]

Only the outer-collar **accumulated dissipation** remains.  The coarse
full-window estimate has the adverse coefficient

\[
 D_{k,R}^{\rm out}
 \le CL^{2/3}R^{-1}\omega^{1/3}(P_R^M)^{2/3},
 \qquad
 \frac\rho4-\frac{c_\gamma}{12}
 =\frac{27163}{476280000}>0.
\]

This positive sign is failure of that upper estimate, not a counterexample.
On \(R^3\) blocks the exact effective packing reduction is

\[
 D_{k,R}^{\rm out}
 \le CL^{2/3}R^{-2/3}\omega^{1/3}
 N_{\rm eff}^{1/3}(P_R^M)^{2/3},
\]

and the sufficient threshold is

\[
 \limsup_{L\to\infty}\frac{\log N_{\rm eff}}{L^2}
 <\frac{4279}{79380000}.
\]

The release verdict must remain:

- safe complete subclock: **PAID**;
- inner padding: **PAID**;
- full endpoint row: **PAID**;
- outer-collar accumulated dissipation: **OPEN**;
- full \(K\), fixed deletion, suitable-weak extension and regularity:
  **OPEN / NOT CLAY**.

## Publication and deployment QA

Publish one bilingual R0.75B research page and synchronized downloadable PDF,
expose the frozen audit/certificate/literature artifacts, and update homepage,
latest-research count, navigation, literature page, version ledger, and global
index through B.  Do not update the cumulative recap at this non-major
milestone and do not invent a formal figure or simulation.

Run structural, equation, internal-link, and asset tests; desktop/mobile
render inspection; GitHub Pages workflow verification; and online byte
identity checks.  Report the site commit, workflow run, page/PDF/object
counts, and deployed-byte verdict.  No second task is authorized.
**NOT CLAY.**
