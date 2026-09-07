# 指定控制函数族终点门的独立审查

2026-09-08。PRIVATE_CORE。**PASS：CE.1–CE.2、终点唯一最小性及所述条件后验接口成立。** 本审查者未编写 CONTROL_FAMILY_ENDPOINT_LEMMA.md，也未参与其中的新分段论证；全文读取原稿、PARAMETRIC_COST_LEMMA.md、NODAL_VS_CONTROL_INTERFACE.md 后独立推导。旧 HYBRID_DERIVATION.md 为本审查者的既有工作；它与另一代理的 HYBRID_INDEPENDENT_REVIEW.md 只作为已接受的比较/延拓接口使用，不冒称本次重新独立证明旧接口。

本轮未发现数学阻断或需要修改原稿的错误。以下接受仅限固定 \(A=2067/160,d=15/128,T=5/2\) 的同一显式控制族，以及指定取满包络。没有选择新的预算数值、计算新指数值、取轨道样本或运行 PDE/控制 ODE。

## 1. 正性、原点与精确标量条件

P.12 给
\[
b(T)=Ae^{-T}-d>A/13-d=7293/8320>0.
\]
因 \(b'(t)=-Ae^{-t}<0\)，全窗 \(b>0\)。所以 \(L'=bL>0\)、\(L(0)=1\)、\(f(0)=1\)、\(f'=e^{-2t}>0\)，进而 \(H=Lf>0\) 且严格递增。对 \(t>0\)，\(L>1,g>0\)；在原点 \(g(0)=0\)，\(K(0)=2C/441=1/576\)，K 连续正。不能在原点使用 \(g'/g\)，稿中也没有这样做。

对 \(\beta=\varepsilon H,\alpha=\beta/64\)，直接微分
\[
\beta'=b\beta+\varepsilon L e^{-2t}.
\]
第一条取满包络的控制式乘64后的余量为
\[
[(A-\mu_1)e^{-t}+1-d]\beta+\varepsilon(L-1)e^{-2t}\ge0.
\]
这里 \(A\ge\mu_1,1-d>0,L\ge1\)，故对每个 \(\varepsilon>0\) 均成立。

第二式中 \(\sqrt{\alpha\beta}=\beta/8\)，三个导数系数合并为 \(Ae^{-t}\beta\)。因此
\[
\frac{\beta'-F_{\rm env}}{\beta}
=\frac12-d-\frac{441}{2}\varepsilon^2H^2
 +\frac{(1-L^{-1})e^{-2t}}{f}
=C+g-\frac{441}{2}\varepsilon^2H^2.
\]
除以正的 \(\beta,H^2\) 合法，得到 NC.2 的“当且仅当”
\(\varepsilon^2\le K(t)\)。这是直接保留三次项后的等价式，不需要先假设 \(\beta\le1/24\)。由于这些函数连续，逐时控制与几乎处处控制之间也没有孤立端点反例。

## 2. 后段的严格下降

对 \(t>0\)，由 b 递减，
\[
\log L(t)=\int_0^t b(s)\,ds\ge tb(t)>0.
\]
又 \(L(t)-1>\log L(t)\)，所以
\[
\frac{b(t)}{L(t)-1}<\frac{b(t)}{\log L(t)}\le\frac1t.
\]
独立对 g 作对数微分得到
\[
\frac{g'}g=\frac{b}{L-1}-2-\frac{f'}f
<\frac1t-2-\frac{f'}f.
\]
在 \(t\ge1/2\) 时 \(1/t-2\le0\)，而 \(f'/f>0\)。因此该段 \(g'<0\)。因 \(C+g>0\)、H 严格增加，
\[
\frac{K'}K=\frac{g'}{C+g}-2\frac{H'}H<0.
\]
这证明 K 在 \([1/2,T]\) 严格递减，包含左端 \(1/2\)；没有假定原点附近亦递减。

## 3. 早段与终点严格分离

对 \(0\le t\le1/2\)，
\[
A(1-e^{-t})-dt\le At\le A/2=2067/320<7.
\]
P.11 的 \(e<3\) 与 \(f<3/2\) 给
\[
H(t)<3^8/2=H_E.
\]
结合 \(g\ge0,C>0\)，即使 \(t=0\) 也有严格界
\[
K(t)>\frac{2C}{441H_E^2}.
\]
严格性来自 H 的严格上界，不依赖 \(g(0)>0\)。

从原 P.14–P.15 独立重接
\[
H(T)>94770\frac{431}{288}
=\frac{2269215}{16}=H_->6561=2H_E.
\]
又 \(L(T)>1\)、\(e^{-2T}<1/144\)、\(f(T)>431/288\)，故
\[
0<g(T)<\frac{1/144}{431/288}=\frac2{431}<C.
\]
于是
\[
K(T)<\frac{4C}{441H_-^2}
<\frac{C}{441H_E^2}
<\frac{2C}{441H_E^2}<K(t)
\quad(0\le t\le1/2).
\]
这里 \(H_->2H_E\) 足以支付平方分母中的因子4，链条没有漏掉系数。结合后段严格递减，T 是闭窗唯一最小点。分段位置 \(1/2\) 是解析论证中的固定界点，不是科学采样。

## 4. 必要充分门及终点条件

由正性、连续性和上面的最小值定位，指定函数为取满 P.1 包络提供全窗两条控制式，当且仅当
\[
0<\varepsilon\le\sqrt{K(T)}
=\frac1{H(T)}\sqrt{\frac2{441}(C+g(T))}.
\]
上端包含等号是正确的：后验比较允许控制微分不等式取等；正 \(\beta\) 在紧闭窗有严格正下界。这个“仅当”不能扩大到较小实际系数或其它控制函数。

不经旧 \(1/24\) 吸收，直接从该门得
\[
\beta(T)^2\le\frac2{441}(C+g(T))
<\frac{4C}{441}=\frac1{288}<\frac1{256}.
\]
故 \(\beta(T)<1/16\)，全窗也有有限正控制。Y.25 及其已审比较/延拓并未把 \(\beta<1/24\) 作为一般假设；旧数值只是原充分吸收方式的限制。直接支付 Y.25 后，可用原延拓论证到达 T。

若同一参照的实际全窗输入确实被该 P.1 包络覆盖，并满足原正则性、初始值、周期、零均值等假设，以及完整终点 \(A_{-1}(v(T))\le X_*\le1/2\)，则
\[
A_{-1}(u(T))\le X_*+6\beta(T)
<\frac12+\frac6{16}=\frac78<1.
\]
原严格小数据门遂给同一原初值的全局光滑性。没有把未知原解系数当作控制输入，也没有把控制函数的正起值当作修改物理初值。即使 \(\varepsilon=\varepsilon_N\)，上述终点余量仍严格。

因为 \(g(T)>0\) 且 \(2C/441=1/576\)，有
\[
\varepsilon_N>\frac1{24H(T)}=\varepsilon_S.
\]
这是符号关系，没有指定第三个预算。现有粗 H 区间和节点必要预算的相对位置仍不足以比较准确 \(\eta\) 与 \(\varepsilon_N\)；本审查没有补算该比较，也没有把必要预算与宽阈值包围的重叠当作可行性。

## 5. 实际小整数检查及来源

除解析手推外，本轮以标准库 Fraction 实际核了以下9个固定有理关系，结果均为 True：

| 固定关系 | 结果 |
| --- | --- |
| \(2067/320<7\) | True |
| \(A/13-d=7293/8320>0\) | True |
| \(94770(431/288)=2269215/16\) | True |
| \(2269215>104976\)，即 \(H_->2H_E\) | True |
| \(256<21119\)，即 \(2/431<49/128\) | True |
| \(2(49/128)/441=1/576\) | True |
| \(4(49/128)/441=1/288\) | True |
| \(1/288<1/256\) | True |
| \(1/2+6/16=7/8<1\) | True |

这些是正文整数/分数恒等式的检查，没有调用指数函数、产生节点、运行参数试探或任何科学内核。本次未重新读取节点结果或旧二进制。NODAL_VS_CONTROL_INTERFACE.md 关于“尚未定位最小值”的文字保持其历史完成范围；本次新稿是其后续解析加强，不要求改写旧记录。

全文实读三份主要文本；HYBRID_DERIVATION.md 的 §§5–8 与 HYBRID_INDEPENDENT_REVIEW.md 的比较/延拓及时间 C1 段用于核对条件终点接口。该引理及本审查不声称新颖性，不另行冻结或发布，也不认证实际全窗导数、残差或原 NS 结论。下表仅绑定实际读取的五份源文件，路径相对反向科学工作树。

| 实际来源 | SHA-256 |
| --- | --- |
| research/reverse/fixed-seed-global-screen/CONTROL_FAMILY_ENDPOINT_LEMMA.md | bfc2a232188fc838078d9f4036c4b7b0fb684d881f72644c9f0996eaef2c691d |
| research/reverse/fixed-seed-global-screen/PARAMETRIC_COST_LEMMA.md | bcbb265b0b9639d2fcae54dddee5415cce0cec62f1874d008dc389d2ae7ea2cf |
| research/reverse/fixed-seed-global-screen/NODAL_VS_CONTROL_INTERFACE.md | 59d06565ff7cb693b6e5a63eb306b25b2009b4cb19ed5914c7453bb118ad8439 |
| research/reverse/fixed-seed-global-screen/HYBRID_DERIVATION.md | 2b1be8ad9612b10a019c4cdb43c74b7ae5f76e739d0ee572ba4decb1d3013fbc |
| research/reverse/fixed-seed-global-screen/HYBRID_INDEPENDENT_REVIEW.md | 2cbc394084e8a4991b8e18b6aeb90b04263aca2021d23f2ffe205e8ba22939ac |
