# 真实来源的全短窗幅度界与复制必要条件

2026-09-08，PRIVATE_CORE。独立有界手工证明，待非作者审查及根比较。

**合同与形成历史。** 开始时先全文读取本目录合同，随后实际重读历史更正后的最终 CONTRACT.md。更正如实记录根曾用旧界作先行手工价值预检，合同在正式完整论证和任何实证选参前锁定；本稿未接收预检的具体公式或常数，也未读本目录 PROOF.md 或另一新推导。以下独立性仅指本项的新推导，不是全课题盲推导。

**结果。** 仅用已接纳 SOURCE_BRIDGE 的第一层与真实尾部界，在整个指定短窗得到真实来源 S 的严格整体 Wiener 上界。继而分别给出 S 的模板近似、以及另有真实其他来源容限时 P_Du 的模板近似所要求的复制幅度界；两种假设不混用。所有数据、时间、平移及 ε、η 都保持符号，未选实际值。

本文不重新证明旧源的经典存在、唯一性或无限维收敛，不把它们称为新增定理。本人此前有该桥接问题的审查及后续独立推导历史；本次只读取下表范围，按实际公式手核。无科学程序、数组、数值求值、参数扫描、实际初值或频率选取、Git、重置或外发。

## 1. 实际来源与直接输入

路径相对于 research/reverse/。本次实际全文读取两份来源并实测最终字节；内部转引不计为本轮实读。

| 来源 | SHA-256 |
|---|---|
| short-window-source-amplitude/CONTRACT.md，先全文读取，历史更正后再次全文读取 | d0e42e518d8b5d4c3d13511fe79f6903f46d7c6d31910702f19282e1907e14de |
| mixed-polarization/SOURCE_BRIDGE_INDEPENDENT.md，全文，以下称 SBI | 1d3d33fbb8fcc17ac1266f2ee88c88eebe328867f385277a0a684cfa2247630a |

定位旧界时工具还返回旧 SOURCE_BRIDGE_PROOF.md 的匹配行与哈希；本稿数学只使用上表 SBI 的明列等式，不从旧主稿另取常数或论证。

固定 SBI 的同一三对独立整数频率、非零横向种子及真实实值初值
\[
a(x)=\sum_{i=1}^3
\{U_ie^{ip_i\cdot x}+\overline{U_i}e^{-ip_i\cdot x}\},
\quad A=\|a\|_{\mathcal A_0}=2\sum_i|U_i|>0,\quad
K=\max_i|p_i|>0.
\tag{SWI.1}
\]
向量长度为 Hermitian 欧氏范数，卷积点积仍为复双线性。单位正黏性、无外力、三维 2π 环面保持不变。旧源已给出该同一 a 的唯一光滑 NS 原解 u，时间域为
\[
0\le t\le T_{\rm sb}=\frac1{8AK},\quad
q(t)=4AKt,\quad 0\le q(t)\le\frac12.
\tag{SWI.2}
\]
本文在 t>0 得严格幅度结论，不重新选择时间起点。

沿用旧集合
\[
D=\{\pm2p_i\},\qquad
\mathcal L=\{\sigma p_i+\tau p_j:i<j,\ \sigma,\tau=\pm1\}.
\]
第一层 v1 与真实 g=P_Lu 满足 SBI.12、34：
\[
\|v_1(s)\|_{\mathcal A_0}\le A q(s)/4,\quad
\|g(s)-v_1(s)\|_{\mathcal A_0}
\le\frac{Aq(s)^3}{1-q(s)^2}.
\tag{SWI.3}
\]
后者来自完整无穷叶数尾部，并非把 g 设为 v1。全部这些场无散，真实来源定义为
\[
S(t)=\int_0^t e^{(t-s)\Delta}P_D B(g(s),g(s))\,ds,
\]
\[
W(t)=\int_0^t e^{(t-s)\Delta}P_D B(v_1(s),v_1(s))\,ds.
\tag{SWI.4}
\]
S 是同一原解的来源分量，不是另一条自由 NS 解。

## 2. 完整输出导数界与全短窗上界

SBI.37 的完整输出频率界可以直接核清：对无散第一输入 f，在 r+s=k 的每项有 f_r·s=f_r·k。由于 k∈D 时 |k|≤2K，Leray 投影范数至多一，
\[
\|P_DB(f,z)\|_{\mathcal A_0}
\le2K\|f\|_{\mathcal A_0}\|z\|_{\mathcal A_0}.
\tag{SWI.5}
\]
这里对完整有序卷积求和，无额外乘二，也没有删去输入的其它频率。热半群为收缩。

由 SWI.3，在每个 s≤t 有
\[
\|g(s)\|_{\mathcal A_0}
\le A\left\{\frac{q(s)}4+
\frac{q(s)^3}{1-q(s)^2}\right\}.
\]
因此以 q=q(t)>0 和符号积分变量 z=4AKs 写
\[
\begin{split}
\frac{\|S(t)\|_{\mathcal A_0}}A
&\le\frac12\int_0^q
\left\{\frac z4+\frac{z^3}{1-z^2}\right\}^{\!2}\,dz\\
&=\frac12\int_0^q
\left\{\frac{z^2}{16}
+\frac{z^4}{2(1-z^2)}
+\frac{z^6}{(1-z^2)^2}\right\}\,dz.
\end{split}
\tag{SWI.6}
\]
因子 1/2 来自 2KA² ds/A=dz/2；它不是两项有序作用被合并后的定义。

对 0<z<q，有 1−z²>1−q²>0。第二、三项在该开区间严格小于将分母替换为终点分母后的对应正项。因此对每个 t>0，严格得到
\[
\boxed{\|S(t)\|_{\mathcal A_0}<A\Phi(q),}
\]
\[
\boxed{\Phi(q)=\frac{q^3}{96}
+\frac{q^5}{20(1-q^2)}
+\frac{q^7}{14(1-q^2)^2},\qquad 0<q\le\frac12.}
\tag{SWI.7}
\]
严格性来自一个正长度积分区间上的严格比较，不是假设实际 S 非零，也不要求任何模式实现范数上界。

另可用旧 SBI.39 交叉核对非严格版本：
\[
\|W(t)\|_{\mathcal A_0}
\le 2K\int_0^t(Aq(s)/4)^2\,ds
=Aq^3/96,
\]
\[
\|S-W\|_{\mathcal A_0}
\le A\left\{\frac{q^5}{20(1-q^2)}
+\frac{q^7}{14(1-q^2)^2}\right\}.
\tag{SWI.8}
\]
这正是 SWI.7 的三项。SWI.6 则另支付其严格号，未新增原解存在性结论。

Φ 的每一项在 0<q≤1/2 上严格递增：正幂分子增加，正分母减少。因此在合同给定无量纲端点手核
\[
\Phi(1/2)=\frac1{768}+\frac1{480}+\frac1{1008}
=\frac{105+168+80}{80640}
=\frac{353}{80640}=:\kappa_*<1.
\]
于是全窗统一有
\[
\boxed{\|S(t)\|_{\mathcal A_0}<\kappa_* A
\quad\text{对全部 }0<t\le T_{\rm sb}.}
\tag{SWI.9}
\]
q=1/2 只是合同已经规定的归一化窗端；没有在这里选择实际 A、K 或 t。该有理常数是上述界的便利上界，不声称为所有实际数据的最优常数。

## 3. 真实倍频平移模板及 S 的近似

对任意但固定、不选择的实平移 φ，记
\[
T_\phi(x)=a(2x+\phi)
=\sum_i\{U_ie^{ip_i\cdot\phi}e^{2ip_i\cdot x}
+\overline{U_i}e^{-ip_i\cdot\phi}e^{-2ip_i\cdot x}\}.
\]
负频率仍为正频率的共轭，故这是真实实值模板。倍频映射对 Fourier 频率单射，平移只乘单位模复数，因此
\[
\boxed{\|T_\phi\|_{\mathcal A_0}=A,\qquad
\|\lambda T_\phi\|_{\mathcal A_0}=\lambda A
\quad(\lambda\ge0).}
\tag{SWI.10}
\]
没有独立选择各模式相位，也没有因空间倍频引入虚假的 Wiener 范数倍数。

为使“相对模板误差”无歧义，先采用相对于被复制模板 λTφ 的归一化，即
\[
\boxed{\|S(t)-\lambda T_\phi\|_{\mathcal A_0}
\le\varepsilon\lambda A,\qquad
\lambda\ge0,\quad0\le\varepsilon<1.}
\tag{SWI.11}
\]
三角不等式与 SWI.7 给
\[
(1-\varepsilon)\lambda A
\le\|S(t)\|_{\mathcal A_0}<A\Phi(q).
\]
故必要条件为
\[
\boxed{\lambda<
\frac{\Phi(q)}{1-\varepsilon}
\le\frac{\kappa_*}{1-\varepsilon}.}
\tag{SWI.12}
\]
特别地，在全部短窗上，如果
\[
\boxed{\kappa_*\le1-\varepsilon}
\tag{SWI.13}
\]
则 SWI.11 不能以 λ≥1 成立。边界等号也被排除，因为 SWI.7 是严格界。更细的同一时刻必要排除域为 Φ(q)≤1−ε。

本证明没有除 λ 或 \(\|S\|\)。λ=0 时 SWI.11 要求 S=0；反过来 S=0 时，ε<1 强制 λ=0。因此零来源分支完整保留，不把它误称为非零复制。

## 4. 加入真实其他来源容限后的 P_Du 近似

这是与 SWI.11 不同的一组条件。假设在同一时刻、同一原解上确有
\[
\boxed{\|P_Du(t)-S(t)\|_{\mathcal A_0}
\le\eta\|S(t)\|_{\mathcal A_0},\qquad \eta\ge0.}
\tag{SWI.14}
\]
本文不证明任何实际数据满足此容限。它涉及全部真实其他来源，不能由旧 \(\|S-W\|\) 尾部直接替代；S−W 与 P_Du−S 是不同误差。

再单独要求
\[
\boxed{\|P_Du(t)-\lambda T_\phi\|_{\mathcal A_0}
\le\varepsilon\lambda A,\qquad 0\le\varepsilon<1.}
\tag{SWI.15}
\]
由 SWI.14 有 \(\|P_Du\|\le(1+\eta)\|S\|\)，所以
\[
(1-\varepsilon)\lambda A
\le\|P_Du(t)\|_{\mathcal A_0}
<(1+\eta)A\Phi(q).
\]
必要条件精确为
\[
\boxed{\lambda<
\frac{(1+\eta)\Phi(q)}{1-\varepsilon}
\le\frac{(1+\eta)\kappa_*}{1-\varepsilon}.}
\tag{SWI.16}
\]
因此全短窗的明确无 λ≥1 子域为
\[
\boxed{(1+\eta)\kappa_*\le1-\varepsilon,}
\quad\text{即}\quad
\boxed{353(1+\eta)\le80640(1-\varepsilon).}
\tag{SWI.17}
\]
同一时刻可用 \((1+\eta)\Phi(q)\le1-\varepsilon\) 得到更细排除域。没有选择 ε 或 η 的实际值；ε 接近一或 η 较大时，若不满足这些条件，本稿不能据此排除 λ≥1。

若 S=0，则 SWI.14 强制 P_Du=0，随后 SWI.15 与 ε<1 强制 λ=0。一般情形也未除 S 的范数。SWI.16 是条件必要界，不是说一旦该数值界允许 λ，实际模板近似或来源容限就一定成立。

## 5. 若误差改按原初值范数 A 归一化

另一种可能的约定是固定 \(\|S-\lambda T_\phi\|\le\varepsilon A\)，而非 SWI.11 的 ελA。两种假设不同，不能沿用同一个 λ 公式。按这个约定，同样的严格范数界给
\[
\boxed{\|S-\lambda T_\phi\|\le\varepsilon A
\ \Longrightarrow\ \lambda<\varepsilon+\Phi(q)
\le\varepsilon+\kappa_*.}
\tag{SWI.18}
\]
若同时有 SWI.14，但模板近似改为 \(\|P_Du-\lambda T_\phi\|\le\varepsilon A\)，则
\[
\boxed{\lambda<\varepsilon+(1+\eta)\Phi(q)
\le\varepsilon+(1+\eta)\kappa_*.}
\tag{SWI.19}
\]
这里及本节范数仍全部是 \(\mathcal A_0\)。恰好在判断 λ≥1 是否被排除时，全窗容限子域仍分别为 SWI.13、17；但具体 λ 必要上界和 λ=0 的近似含义不同。本稿因此明确列出两种归一化，不将它们等同。

## 6. 范围、自核与未付内容

新增证明只包括：用旧第一层、真实无穷尾部及完整输出导数界得到 S 的整体幅度函数 Φ、全短窗严格有理上界，以及三角不等式给出的复制幅度必要门。该结论不要求实际单代几何或方向已经通过，也不判断其可解性。没有重算、追认或修复旧失败证据。

全短窗指同一个 a、A、K 和同一个原解 u 的 \(0<t\le1/(8AK)\)。g=P_Lu 不是重置后的 NS 初值；S 本身也不是独立无外力解。不能对下一代换 a、重新起钟或重复这个上界而宣称同一初值无限尺度。旧来源容限中的交叉作用没有被删除，也没有被视为互相正交的能量。

本稿不覆盖其它时间窗、背景、模板、频带、延迟供给、跨代无限维余项或一般正来源容限；不证明持续级联、再生成或一般 NS 奇性不可能。当前必要界之外是否存在实际模板近似仍 OPEN。无实际频率、初值、平移、幅度、时间、方向、ε 或 η 选择；无新候选、图档或计算证书。

最终停改前全文自读、逐式手核并复核两份实际来源字节，再报告 SHA。EXACT CONDITIONAL SHORT-WINDOW AMPLITUDE BOUND；TRUE SOURCE RETAINED；NO-CANDIDATE；NOT CLAY。
