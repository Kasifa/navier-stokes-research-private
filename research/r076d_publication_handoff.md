# R0.76D publication handoff -- frozen FIFO release contract

## Release identity

- release id: `R0.76D-Step55`
- research label: `R0.76D`
- publication task id: `01a06480-0532-7fd0-bdf0-57571465a2d4`
- logical predecessor: `R0.76C-Step54`
- cumulative recap required: `false`
- retained recap terminal release: `R0.75W-Step48`
- formal scientific figure required: `false`
- core research commit:
  `c0cfe20b1970d9abbc32c191a5fad71dfdad1465`

This handoff authorizes only R0.76D.  Do not read or publish later material.
Do not create or reuse a second publishing, recap, reflection,
lessons-learned, usage-notes, or temporary task/system.  The sole publisher
must wait until R0.76C-Step54 has been deployed and verified, then append
R0.76D exactly once in the same FIFO task.  The cumulative recap through W
must remain byte-identical.

## Frozen source ledger

| SHA-256 | source path |
|---|---|
| `cd94e3384f01963cb7b8a14fdb8376c6197c361473447f15500db0acac5e958e` | `research/r076d_quantitative_growing_mode_entropy_window.md` |
| `9b99247ceb34cadc12c7f4f0858be642316ca80d1ff83d05dfd745a9906356d8` | `research/r076d_quantitative_growing_mode_entropy_window_primary_audit.md` |
| `f2358780d382dcace69b7ebef855bf3c8e63d15b581dc86b62b7e3c751fbd310` | `research/r076d_report-source.md` |
| `ffe5c2b9a1a6b0c20b710dc45fcac9543069ea6af38dce34804665012984b374` | `scripts/r076d_quantitative_growing_mode_entropy_window_fixtures.json` |
| `eb5dd9ebaa6a74cbc7f999fdbd55ee54a50588342c3dfba9412ac53c935ba2dd` | `scripts/r076d_quantitative_growing_mode_entropy_window_expected.json` |
| `ed96f55b1326f1e7c1330670c132c523c7861f53edcb046b662159d83e60ce54` | `scripts/r076d_quantitative_growing_mode_entropy_window_certificate.py` |
| `9f12fa2aadc35dfb228e8f0ab60eec420c5c6bdfa306f1b66ca4828cdde4d391` | `scripts/r076d_quantitative_growing_mode_entropy_window_certificate_independent.rb` |
| `b69b5380ffd60ad713c3971311cf6197bc5254a44abbb8e65f3d19990ec5e592` | `scripts/r076d_quantitative_growing_mode_entropy_window_qa.sh` |
| `e57d160e8b3b37ed714e884750f50abbaaaac25a1e3ec3ba395a0193e0b6757d` | `research/r076d_quantitative_growing_mode_entropy_window_certificate.json` |
| `460917d50cd9aeeb4af5898322915d67fa8ec3e1971f2e5945becf858ccd9c94` | `research/r076d_quantitative_growing_mode_entropy_window_certificate_report.md` |
| `0d6e3b7f363fdb9e031a228038ae7af4152d51d101e6050f39c4de7dc21fa69a` | `research/r076d_quantitative_growing_mode_entropy_window_independent_audit.md` |
| `e0313b591dee896aae87930dfd01cfa2c6cd3f1e7a82875b439ba0399402fab6` | `research/r076d_quantitative_growing_mode_entropy_window_qa_report.md` |

Every source byte must match this ledger before rendering.  The core commit
must resolve as a commit, and its changed paths must be exactly these twelve
rows.  Any mismatch is a release blocker.

## Publication synopsis

Fix an integer `q>=1`, integer torus frequencies, nonnegative amplitudes,
real phases, and a real constant speed:

\[
 q\in\mathbb N,\quad q\ge1,\qquad
 n_j\in\mathbb N,\quad A_j\ge0,\quad
 \phi_j\in\mathbb R,\quad B\in\mathbb R.
\]

For the exact real constant-shear family

\[
 F(t,x_2)=\sum_{j=1}^q A_j e^{-n_j^2t}
 \cos(n_jx_2-\phi_j-n_jBt),
 \qquad
 1\le n_1<\cdots<n_q\le2n_1,
\]

R0.76C proved the complete signed collar-flux estimate for each fixed
finite `q`, but left the dependence of its constant on `q` unquantified.
R0.76D makes that loss explicit:

\[
 \boxed{
 |\mathcal T_{\boldsymbol n,R}|
 \le \exp\!\bigl(C_*q\log(q+1)\bigr)
 a^{2/3}R^{-1/3}
 \bigl(M_{\boldsymbol n,R}^{\rm plat}\bigr)^{2/3}.}
\]

The constants are independent of `q`, `R`, the frequencies, amplitudes,
phases, and constant speed `B`, after the frozen profiles and sufficiently
large-`L` gate are fixed.  The exponential term is part of the estimate and
must not be suppressed.

## Growing-mode consequence

With the same normalized flux and plateau mass as R0.76C,

\[
 \mathfrak X_{\boldsymbol n,R}
 \le \exp\!\bigl(C_*q\log(q+1)\bigr)
 a^{2/3}\omega^{1/3}
 \bigl(p_{\boldsymbol n,R}^{\rm plat}\bigr)^{2/3}.
\]

Therefore every integer-valued mode count satisfying

\[
 q(L)\log(q(L)+1)=o(L^2)
\]

retains the exact frozen coefficient rate

\[
 \limsup_{L\to\infty}L^{-2}
 \log\!\left[e^{C_*q(L)\log(q(L)+1)}
 a^{2/3}\omega^{1/3}\right]
 =-\frac2{11907}.
\]

This is a growing-mode window, not a uniform arbitrary-packet theorem.

## Quantitative spatial observation

For an exponential sum with at most `N<=2q` active terms and spatial
frequencies bounded by `2alpha`, Chebyshev on the unit plateau interval and
the measurable-set Turan--Nazarov theorem give

\[
 \|g\|_{L^\infty(J^+)}\le D^{2q}\|g\|_{L^3(I)}.
\]

For `z_0 in J`, set `f(t)=g(z_0+t/2)`.  Erdelyi's point derivative theorem
applies to complex coefficients with maximal rescaled frequency at most
`alpha`:

\[
 |f'(0)|\le\bigl(\alpha+2e(N+1)\bigr)
 \|f\|_{L^\infty([-1,1])}.
\]

Since `g'(z_0)=2f'(0)`, the resulting explicit row is

\[
 \|g\|_{L^\infty(J)}
 +(\alpha+q)^{-1}\|g'\|_{L^\infty(J)}
 \le D^{2q}\|g\|_{L^3(I)}.
\]

Repeated exponents are combined and zero terms deleted first.  No
frequency-gap denominator or temporal/transport imaginary-part loss enters;
the spatial derivative retains the explicit `alpha+q` factor.

## Counted heat tail

For at most `N<=2q` temporal exponents with real parts in `[-4,-1]`, the
centered Turan--Nazarov argument gives

\[
 |Q(\tau)|^3
 \le D^{3N}(1+\tau)^{3(N-1)}e^{-3\tau}
 \int_0^1|Q(r)|^3dr.
\]

After integration in the spatial parameter and raising to the power `2/3`,
put `m=2(N-1)`.  The weighted tail obeys

\[
 \int_1^\infty\tau(1+\tau)^me^{-2\tau}d\tau
 \le\frac{(m+1)!}{4}
 \le e^{CN\log(N+1)}.
\]

For the endpoint, `T>=4` gives the explicit comparison

\[
 T^{2/3}(1+T)^me^{-2T}
 \le\left(\frac54\right)^mT^{m+2/3}e^{-2T},
\]

and the global maximum of the last polynomial-exponential factor has the
same `exp(CN log(N+1))` bound.  Hence

\[
 \int_0^T\tau k(\tau)^{2/3}d\tau
 \le e^{CN\log(N+1)}K_T^{2/3},
 \qquad
 k(T)^{2/3}
 \le e^{CN\log(N+1)}T^{-2/3}K_T^{2/3}.
\]

Every time fibre must be an exponential polynomial satisfying the stated
real-part hypothesis.  Do not publish this as a result for an arbitrary
measurable time-dependent family.

## Complete-real energy and scale ledger

The proof keeps the complete real square and uses

\[
 a^{-2}(\alpha+q)^2
 \le C\left(\lambda+\frac{q^2}{a^2}\right).
\]

For `lambda<=1`, the bounded original clock pays all rows by Holder and the
quantitative endpoint trace.  For `lambda>1`, the cutoff onset and heat clock
give

\[
 \lambda\int_0^4\zeta(s)h(s)^{2/3}ds
 \le e^{Cq\log(q+1)}\lambda^{-1/3}H^{2/3},
\]

while the endpoint powers cancel exactly because `T=4lambda` and
`K_T=lambda H`.  The remaining `q^2/a^2` factor is polynomial in `q` and is
absorbed by the displayed modal-entropy exponential.

The exact physical prefactor and plateau mass are `a^2R^3v/2` and at least
`4pi delta_0a^2R^5H`.  Eliminating `H` yields
`a^(2/3)R^(-1/3)M^(2/3)`; normalization cancels `R` and leaves the frozen
rate `-2/11907`.

## Source and claim boundary

The continuum proof imports two generic approximation-theory results:

1. Nazarov's positive-measure Turan--Nazarov inequality, also restated by
   Friedland--Yomdin; and
2. Erdelyi's point derivative inequality for complex pure-imaginary
   exponential sums.

The spatial placement, counted factorial tail, endpoint comparison,
`lambda` split, complete-real energy payment, physical conversion, and
growing-mode corollary are local deductions.  The bounded source screen is
not evidence of novelty, priority, sharpness, or literature completeness.

R0.75R remains compatible: it rules out a uniform plateau-only conclusion
for arbitrary growing packets, whereas the present constant grows with `q`
and the theorem stays inside the exact constant-shear family.  Arbitrary
packets, nonconstant or vertically dependent shear, projection from a larger
velocity, arbitrary-field E.24, complete Version-M extraction, fixed
deletion, suitable-weak transfer, regularity, and singularity remain open.
When `B\ne0`, the constant background has not been shown to belong to the
frozen mean-zero, inversion-paired Version-M subclass.  **NOT CLAY.**

## Proof and certificate boundary

The independent counterexample-first audit and primary audit both report
PASS with zero mathematical and release blockers.  The audit inserted the
previously hidden `(5/4)^m` endpoint comparison before the core was frozen.

The exact fixture has `q=3`, `N=6`, `m=10`,
`11!/4=9,979,200`, `lambda=4`, `T=16`, gradient coefficient `257/64`,
weighted lambda exponent `-1/3`, endpoint exponent zero, and frozen rate
`-2/11907`.  Python and Ruby each report 123/123 assertions, identical 6/6
exact sections, rejection of all 123 named mutations, fail-closed unknown
mutations, and regeneration stability.  Python is byte-stable under
`PYTHONHASHSEED=0,1,42`.  The main note has D.1--D.41 and 41/41 display
pairs.  The core inventory is exactly twelve files, and a clean archive of
the core commit reran the complete QA with a byte-identical QA report.

These computations bind finite arithmetic, structure, source bytes, and
claim boundaries.  They are not proof of Turan--Nazarov, Erdelyi, or the
analytic flux theorem.

## Recap and figure boundary

R0.75W remains the terminal milestone recap.  R0.76D is an ordinary analytic
note release.  Do not update the cumulative recap.  Preserve its HTML and
PDF byte-for-byte and label the terminal release exactly as
`R0.75W-Step48`.

No simulation, DNS result, formal scientific figure, or decorative plot is
claimed or required for R0.76D.

## Publication and deployment QA

Publish one bilingual R0.76D research page and synchronized downloadable
PDF.  Expose all twelve frozen research, audit, source, certificate, and QA
artifacts.  Update the homepage, latest-research count, navigation, research
and literature reviews, version ledger, global notes index, English
translation, and formal archive through R0.76D while keeping the
latest-recap endpoint at R0.75W.

Run structural, equation, internal-link, asset, recap-preservation, and
forbidden-future-version tests; render desktop and mobile views; verify no
overflow or raw TeX leakage.  Commit and push only R0.76D, wait for GitHub
Pages to succeed, and compare every declared online object byte-for-byte
with the release commit.  A push or green workflow alone is not deployment
proof.

Do not add a figure, simulation, arbitrary-packet claim, unconditional
Version-M claim, regularity claim, recap change, or second task.  The release
is complete only when R0.76D-Step55 is deployed and verified online, after C
and before any later release.
