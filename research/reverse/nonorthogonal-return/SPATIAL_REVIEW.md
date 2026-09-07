# 共享非正交空间四次映射：非作者审查

2026-09-08，PRIVATE_CORE。结论：**限定 PASS，无待修数学阻断。**

我全文读取下表三份文本后，重新手推 SPATIAL_PROOF 的 NS.2–7。本文不是主稿作者的自审；我此前参与过旧等长门及热树范围的审议，因此不是对研究背景的盲审。本轮未读 Pauli 的 SPATIAL_INDEPENDENT 或其它新独立推导。未执行科学程序、数组、指数数值、参数选择或 Git 操作；下述证据是解析推导，不是新计算证书。

## 1. 定义与第一层投影

本合同固定
\[
P=|p|^2>0,\quad Q=|q|^2>0,\quad c=p\cdot q\ne0,
\quad \Delta=PQ-c^2>0,\quad L_\pm=P+Q\pm2c>0.
\]
因此 \(e_p=q-cp/P\) 与 \(n=p\times q\) 在 \(p^\perp\) 内非零、相互正交，确实给出全部复二维横向极化；\(e_q,n\) 对 \(q^\perp\) 同理。这里没有把非正交基变成新的方程坐标。点积是复双线性点积，只有负种子取复共轭。

令第一层投影前的括号分别为 \(A_+,A_-\)。其平面部分直接展开为
\[
(A_+)_{\rm pl}
=\frac{ad\Delta}{PQ}\bigl[(Q-c)p+(P-c)q\bigr],
\]
\[
(A_-)_{\rm pl}
=\frac{a\bar d\Delta}{PQ}\bigl[-(Q+c)p+(P+c)q\bigr].
\]
记 \(h_+=ad\Delta^2/(PQ)\)、\(h_-=a\bar d\Delta^2/(PQ)\)，可逐项核得
\[
(p\cdot A_+,q\cdot A_+)=(h_+,h_+),\qquad
(p\cdot A_-,q\cdot A_-)=(-h_-,h_-).
\]
于是对 \(r=p+q,s=p-q\)，先投影再乘 \(-i\) 给出
\[
N_+\cdot s
=-i\left[0-\frac{(P-Q)2h_+}{L_+}\right]
=\frac{2iad\Delta^2(P-Q)}{PQ L_+},
\]
\[
N_-\cdot r
=-i\left[0-\frac{(P-Q)(-2h_-)}{L_-}\right]
=-\frac{2ia\bar d\Delta^2(P-Q)}{PQ L_-}.
\]
这支付 NS.3 的相反 \(i\) 符号，未略去任一第一层 Leray 投影。

法向 \(n\) 同时垂直 \(r,s\)，故投影不改变其系数。直接由原始两个括号得到
\[
z_+=-i\Delta(ae/P+bd/Q),\qquad
z_-=-i\Delta(-a\bar e/P+b\bar d/Q),
\]
与 NS.2 一致。特别是 \(N_-\) 既不是自由输入，也一般不是 \(N_+\) 的共轭。

## 2. 第二层投影、四次项和符号

设 \(x=N_+\cdot s\)、\(y=N_-\cdot r\)，并沿用主稿
\(D=\Delta^2(P-Q)/(PQ)\)。两个前代中的 \(p\) 种子均为 \(U\)，因此
\[
xy=\frac{4a^2|d|^2D^2}{L_+L_-}.
\]
这里是 \(a^2\)，不是 \(|a|^2\)；不能对第二层的双线性运算增添共轭。

由 \(N_+\perp r,N_-\perp s\)，有
\[
N_+\cdot p=x/2,\quad N_+\cdot q=-x/2,\qquad
N_-\cdot p=y/2,\quad N_-\cdot q=y/2.
\]
因此 \(T=xN_-+yN_+\) 满足 \(T\cdot p=xy,T\cdot q=0\)。完整第二层投影为
\[
C=-i\left(T-\frac{xy}{P}p\right),\qquad
C\cdot q=\frac{icxy}{P}.
\]
再用 \(e_p\cdot q=\Delta/P\)，得 \(C_e=icxy/\Delta\)，正好是 NS.5。两个有序项在 \(T\) 中各出现一次，不需再乘二。

法向系数可在合并分母前独立写成
\[
C_n=2iaD\Delta\left[
\frac aP\left(\frac{d\bar e}{L_+}+\frac{\bar d e}{L_-}\right)
-\frac{b|d|^2}{Q}\left(\frac1{L_+}-\frac1{L_-}\right)
\right].
\]
由于 \(1/L_+-1/L_-=-4c/(L_+L_-)\)，取
\[
\kappa=\frac{2i\Delta^3(P-Q)}{P^2Q^2L_+L_-}
\]
便得到
\[
C_e=\kappa\,2c(P-Q)a^2|d|^2,
\]
\[
C_n=\kappa\left[
a^2Q(L_-d\bar e+L_+\bar d e)+4cPab|d|^2
\right].
\]
NS.6 的 \(b\) 项及其正号均正确。它来自共享原种子的法向分量，不能删除，也不能把两个 \(d\bar e,\bar d e\) 当成独立的自由参数。

## 3. 零分支与热树适用范围

在本合同 \(c\ne0,\Delta>0\) 内，若 \(P=Q\) 或 \(a=0\) 或 \(d=0\)，上述两分量均为零。反之，若 \(P\ne Q\) 且 \(ad\ne0\)，则 \(C_e\ne0\)：所有几何分母严格正，\(c\)、\(P-Q\)、\(a^2\)、\(|d|^2\) 均非零。\(e_p\) 与 \(n\) 线性独立，法向分量不能抵消这个平面分量。因此 NS.7 的充分性和必要性都成立，没有遗漏复相位退化分支。

这不要求法向分量非零；其额外零条件仍由 NS.6 整个括号决定。本判据也不适用于把 \(c=0\) 或平行极限直接代入“当且仅当”的扩展。主稿把 \(c=0\) 仅用作公式接口核对，是准确的：此时平面项消失，法向式保留正交相关项。

我同时核对了 SOURCE_AND_HEAT_PREFLIGHT 的 NH.2–6 与此处定义的连接。两个不同的第一层热率为 \(P+Q\pm2c\)，对应的积分 \(I_\pm\) 对正时间均严格正，其乘积为
\[
I_+(\tau)I_-(\tau)
=e^{-2(P+Q)\tau}\left(\frac{\sinh(c\tau)}c\right)^2.
\]
第二层接收热率是 \(|2p|^2=4P\)，所以这一个配对的两个有序项确有同一严格正权重 \(J_{p\leftarrow q}(t)\)。在所定义的树内，该对贡献的零判据因此与空间 \(C\) 相同。其它配对在同一接收模可以相消；本文没有证明完整接收和非零。

通过范围仅为单对共享种子所诱导的精确四次空间映射及其已有正热权重连接。它没有认证三对共同模板、原解中的两代真实供给、\(1+3/3+1\)、目标外作用、近似稳定性或无限维余项。\(v_1,w_{22}\) 仍是树项，非原解的独立世代；单对非零不成为 NS 机制或候选。未新增文献适用性或新颖性结论。

## 4. 实读来源绑定

以下三份均全文实读；未重新打开预检所引继承 HTML 或外部论文。本次不把其历史引用视作新核验的外部定理。

| 工作树相对路径 | SHA256 |
| --- | --- |
| `research/reverse/nonorthogonal-return/SPATIAL_CONTRACT.md` | `ba31859d9b2e2654c8cf8e00bf64da3b54070c93e9fa036594a96e3d3f70fb1d` |
| `research/reverse/nonorthogonal-return/SPATIAL_PROOF.md` | `50510f2b1b2bee2ed3739bd9a5a1276f16056e244f5b71192b9a39b8066190a5` |
| `research/reverse/nonorthogonal-return/SOURCE_AND_HEAT_PREFLIGHT.md` | `cd0206ef0164387d41e246485d1f4a3a0815fef42ed45163816d21ac4e6fdbe0` |
