# Fixed Kronecker tensor-block contract

2026-09-08. PRIVATE_CORE. IMPLEMENTATION_PREPARED_NOT_EXECUTED.

This is the single cost block specified in section 6 of
CONTINUOUS_RESIDUAL_COST_PREFLIGHT.md and accepted by its root review. It
computes only the full complex convolution of components 1 and 2 of the
96-bit dyadic center at the existing node n=1280, t=5/8. There is no FFT,
integration, mode selection, other node, parameter search, full nonlinear
operator, or NS residual calculation. This center does not replace the
original exact reference.

## 1. Fixed inputs and exact decoding

The original signed spectrum is G=[-8,8]^3 minus zero, 4912 modes, in the
lexicographic order of modes.npy. Authenticate the pinned manifest, that
mode file, and the one block containing n1280. Authenticate every array of
that block, including its time/index descriptors, but use only the value
row indexed 1280 for mathematics. Slopes and other rows are not decoded.

Q=2^52 and L=lcm{|k|^2:k in G}. Set D=2 Q L. Before any addition, promote
each stored int64 to a Python arbitrary-precision integer. If S and T are
respectively the componentwise real sum and imaginary difference at k,-k,
the Gaussian integer numerator is

    A_k = (L/|k|^2) [ |k|^2 (S+iT) - k (k dot (S+iT)) ].

Thus c_k=A_k/D is exactly the original conjugate average followed by the
full Leray projection. Check all 4912 exact divergence and conjugacy
identities. Never use int64 addition for these mathematical operations.

Set Qp=2^96. For each of the 29472 real/imaginary scalar components, divide
Qp A by positive D with Euclidean quotient q and remainder 0<=r<D. Choose
C=q when 2r<D, C=q+1 when 2r>D, and the even member of {q,q+1} when 2r=D.
This is nearest integer, ties to even, including negative inputs. Check
2|Qp A-D C|<=D, and evenness at a tie. This rounding is odd under negation,
so the center c_tilde=C/Qp is conjugate symmetric; check it on all modes.
Do not require or assume that the rounded center remains divergence free.

Save all six scalar components per mode as signed 14-byte little-endian
integers, in the original mode order, with component-major [real,imag]
order: c96-centers.i112le.bin. Strict |C|<2^109 makes this width sufficient.
Hash the file and actually decode it after writing to compare all entries.

Compute exact rational quantities

    M = sum |A_scalar| / D,
    delta = sum |Qp A_scalar-D C_scalar| / (D Qp),
    E_j = 28^(j+1) (2 M delta + delta^2), j=0,2.

Check the a priori bounds M<2^28, delta<2^-82, E_0<2^-47 and E_2<2^-37.
These E_j are only the previously proved input-perturbation allowances
for the future conservative full operator. This block does not compute
that operator and does not claim that E_j bounds its actual residual.

## 2. Fixed packing and exactly three large products

The spatial radix is 33; the coefficient radix is B=2^240. For each input
mode p, e(p)=(p1+8)+33(p2+8)+1089(p3+8), between 0 and 17968. There are
17969 input digits, each 30 bytes. Construct each signed packed integer
from separate nonnegative/negative fixed-width byte arrays and subtract
the two int.from_bytes values. Each component has |C|<2^109; its real-plus-
imaginary sum has magnitude <2^110. No coefficient overlaps its next
digit in this construction.

Let U,V be packed real/imaginary component 1 and X,Y those of component 2.
Perform precisely the three general products

    P0=U X, P1=V Y, P2=(U+V)(X+Y).

The input pairs are fixed independently of their observed values; this
does not replace them with an optimized square benchmark. Record every
input's signed full-width byte SHA, sign and actual bit length, each
product's elapsed wall time, and the product's full-width output SHA.
No claim about scaling the measured time to 18 products or a full window
is permitted.

Output coordinates k in [-16,16]^3 have index

    j(k)=(k1+16)+33(k2+16)+1089(k3+16).

There are J=35937 output digits. Addition of shifted input coordinates
stays in [0,32] in every coordinate, so spatial radix 33 has no carries
or aliasing. Integer polynomial multiplication therefore includes every
ordered p+q=k pair, with its original sign and complex phase.

Each output contains at most 4912 terms. Every raw real-product coefficient
has magnitude <4912*2^220<2^233; after the two/three signed combinations,
each final real/imaginary coefficient has magnitude <2^235<B/2. These are
input-based bounds, not conclusions inferred from balanced decoding.
The packed input width is 4,312,560 bits and the fixed output width is
8,624,880 bits. The geometric sum of digits bounded strictly by B/2 is
strictly less than B^J/2 in absolute value, so signed fixed-width output
conversion is valid for all three products.

## 3. Linear-time signed decoding, including a carry to B

Convert a product z exactly once with

    z.to_bytes(30*J, 'little', signed=True).

The unsigned digits r_j of this two's-complement string satisfy

    z = sum r_j B^j - s B^J,  s=1 if z<0, else 0.

Start carry c_0=0. At each digit set t=r_j+c_j. If t>=B/2, return
w_j=t-B and c_(j+1)=1; otherwise return w_j=t and c_(j+1)=0. The case
t=B is valid: its output is w_j=0 and its next carry is 1. Do not reject
this endpoint or reduce it modulo B and forget its carry.

At each step r_j=w_j+B c_(j+1)-c_j. Summing this identity telescopes:

    z = sum w_j B^j + (c_J-s) B^J.

The a priori strict half-base bound makes the balanced coefficient unique
at every step; induction identifies each w_j with the true convolution
coefficient. The terminal quotient c_J-s must be zero. Check that identity
and the stronger raw coefficient bound |w_j|<2^233 for each product.
This uses one whole-integer byte conversion and a linear scan of J fixed
30-byte pieces; it never repeatedly shifts the whole large integer.

Save product-0.signed-le.bin through product-2.signed-le.bin as the raw
full-width signed integer representations. These bytes are not claimed
to be the independent balanced coefficient encoding. Read each file back
after writing, verify bytes and hash, then decode from the bytes read.

Form all final coefficients R_j=P0_j-P1_j and I_j=P2_j-P0_j-P1_j using
the decoded coefficient arrays. Save all 35937 complex outputs in index
j(k) order as signed 30-byte real then signed 30-byte imaginary values:
tensor12-complex.i240le.bin. Its coefficient denominator is Qp^2=2^192.
After writing, re-read and decode every real and imaginary value. Check
their strict 2^235 bound and conjugacy at indices j and J-1-j.

The physical zero frequency is j=17968. Independently compute the full
4912-term Gaussian integer sum sum_p C_p^1 C_(-p)^2, without using a
packed convolution or half-spectrum reduction. Compare both components
with that output and check the zero imaginary part. This selected direct
check supplements the general packing proof; it does not replace it.

## 4. Evidence, execution gate, and fixed budget

Only audit_kronecker_block.py and this contract are prepared now. Default,
--describe and --check-only only parse code, inspect configuration and
check proof-source hashes. They do not load node data or perform any
scientific kernel. --run is reserved for the root's explicit one-time
instruction after its full source review.

The sole output directory is kronecker-block-trial-01. Reject any existing
contents or attempt to overwrite/retry. Use an exclusive claim and atomic
run.json progress records. Bind actual script, contract, preflight, root
review and C1 SHA; the preflight and root review have fixed expected SHAs.
At execution, record the actual reverse-worktree git HEAD using a read-only
git command in that worktree, and retain byte hashes as the operative
individual source/data bindings. Record the actual command, Python/NumPy,
platform/CPU/thread environment and single-process arbitrary-precision
arithmetic. NumPy is used only for original archive decoding/authentication.

The budget is one execution, 60 seconds wall time, 256 MiB observed peak
RSS, and 8 MiB output. Reserve 128 KiB for metadata/failure records. Check
before and after each large operation and save progress after each
product. The alarm/checks reject observed overruns; this is not a claim
that the OS prevents temporary overallocation or immediately interrupts
a C-level multiplication. Small decoded/rounding arithmetic has an
8192-bit guard; packed arithmetic has the proved fixed input/output widths.

The four binary output groups occupy 5,803,158 bytes: 412,608 center bytes,
3*1,078,110 raw product bytes, and 2,156,220 tensor bytes. Actual writes,
temporary copies, JSON and final resources are still checked against the
budget. Keep existing files and failure details on a stop. COMPLETE is
possible only after actual archive readback, source/input stability and
post-final-write resource checks. Root may retain stdout/stderr separately;
the script emits only bounded progress and a final record pointer.

A completed run means only ONE_FIXED_COMPLEX_TENSOR_BLOCK_VERIFIED. It
does not evaluate other tensor components, output-frequency contraction,
Leray pressure, the original linear terms, any full residual, a continuous
error bound, an NS trajectory, or a global/singularity theorem. A failed
resource gate is COST_NOT_PAID for this fixed implementation and contract.

## 5. Fixed byte bindings

| Input relative to this directory | SHA-256 |
| --- | --- |
| CONTINUOUS_RESIDUAL_COST_PREFLIGHT.md | 0c7ea4b3d33d152f298058a909e446505150d1004529f1a4518c2e1fedc7f796 |
| CONTINUOUS_RESIDUAL_COST_ROOT_REVIEW.md | 4865cf0639e20bc6d8d6c2546e8382c08b59366814168ff2f0b309bc8ef4e5da |
| node-trial-01/manifest.json | 5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a75c6f81622c1cd |
| node-trial-01/modes.npy | f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896 |
| node-trial-01/block-01280-01343.npz | abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e |

The actual output source map additionally records this contract, the
implementation, and C1_RESIDUAL_CONTRACT.md. No prior runtime is claimed.
