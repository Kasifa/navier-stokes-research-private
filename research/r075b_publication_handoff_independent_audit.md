# R0.75B publication handoff — independent audit

## Frozen object

- Handoff: `research/r075b_publication_handoff.md`
- Audited SHA-256: `78513e06c613cee87eed15626ac73863586021f87d83a48600c2c6519f043a3a`
- Verdict: **PASS**
- Blocking issues: **0**

## Reproducibility and queue audit

- All 10 path/hash rows resolve, and every file SHA-256 equals the value frozen in the handoff.
- Core commit `29ade05d496c93e5eb9db74e3f462e2207d505f0` resolves as a commit.
- The sole active publication-task id is `01a06480-0532-7fd0-bdf0-57571465a2d4`.
- The handoff requires `R0.75A-Step26` to be verified first, then appends `R0.75B-Step27` exactly once in that same task.
- It forbids creating a new publication task and limits this transaction to B; C, D, and later materials may not be read or published.
- Together with the frozen predecessor/successor metadata, the queue is A-Step26 → B-Step27 → C-Step28.
- `cumulative recap required` and `formal scientific figure required` are both `false`.

## Mathematical and claim-boundary audit

- The safe subclock is stated as paid, and the outer endpoint short-window branch is also stated as paid.
- The remaining obstruction is only the outer accumulated-dissipation/full-clock step.
- The exact rates and margins agree with the frozen research objects:
  `-92837/476280000`, `4279/238140000`,
  `27163/476280000`, and threshold `4279/79380000`.
- The adverse full-window coefficient is described as failure of the present method, not as a counterexample.
- The handoff does not promote the unresolved full `K` estimate to a theorem.
- Literature language is restricted to a finite non-hit and makes no novelty or priority claim.
- The handoff explicitly states that it does not solve the Clay problem.

## Byte-level rebound

The sole defect in the preceding frozen version—the U+000C FORM FEED before `rac` in the adverse-rate formula—has been replaced by the intended `\frac`. A fresh whole-file scan finds zero disallowed control characters. The corrected formula now reads
`\frac\rho4-\frac{c_\gamma}{12}=\frac{27163}{476280000}>0`, with no change to its mathematical content or boundary.

## Release conclusion

The corrected and rebound B handoff is internally consistent and release-ready, subject to its stated FIFO predecessor verification.
