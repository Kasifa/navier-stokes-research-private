# 最低接收行主稿的非作者逐式审查

2026-09-08，PRIVATE_CORE。被审主稿为 `PROOF.md` 的最终字节 `8961c72504eb7d60f35ee53050c99a2a25203ad539f85a9135ca16706dcc1cba`。结论：**TL.1–35 在本合同域内通过；最低完整 Z 行的唯一实部消元，以及在该行成立后完整 C 行沿原种子复方向的充要条件均获手工核验。没有实际三频实例或全部接收行的可解性结论。**

审查者不是本稿作者，且本轮未读本目录的新 `INDEPENDENT.md`。审查者曾撰写上一阶段 `three-edge-compatibility/PROOF.md` 并审查其若干后续结果，故不声称对既有科学背景完全盲。本轮直接从实读 NC.4–10 核对被审式子，没有用上一阶段自己的推导代替本稿的证明。

另须准确披露形成历史：根在主稿形成过程中提出过吸收接收投影平方的规范建议，之后实际读过主稿。本稿 TL.33 和末尾来源段记录了等价式的手工核对，但没有显式写出该建议来源。根已向本审查者确认这段历史，并允许在审查中记录；本审查据此明确标记主稿**并非完全盲于根的规范建议**。这不等于根提供了其余证明，也不将当前数学核验称作人类审稿或第三份盲推导。未据此改动主稿。

## 1. 实际读取与绑定

| 来源 | 本轮实际阅读范围及用途 | SHA-256 |
|---|---|---|
| `two-elliptic-compatibility/CONTRACT.md` | 全文；几何、极化、活跃性、最低行和有限首项范围 | `ee05b39370f178cac5aebcf3c3046478c848c74b0078ee26edafb3282029ad52` |
| `two-elliptic-compatibility/PROOF.md` | 全文；逐式核验 TL.1–35、所有边界和来源陈述 | `8961c72504eb7d60f35ee53050c99a2a25203ad539f85a9135ca16706dcc1cba` |
| `net-mixed-cancellation/INDEPENDENT.md` | 本轮实读第 44–119 行，即 NC.4–10 及完整 Z、C、协方差和缩放；其余部分本轮未重读 | `25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58` |

NC 是先前接受的完整有限单对系数接口；本轮核验其在当前假设下的代入与消元，不冒称重新证明了旧稿全部 Fourier–Leray 展开。本轮没有读取或调用 SOURCE_BRIDGE 来增加时间结论，也没有读取本项独立稿来补证。全部检查为手工符号推理；工具仅用于文本读写及 SHA-256 字节绑定，无科学程序、数值求值、数组、选参、扫描、Git、额度重置或外发。

## 2. TL.1–5：β 零几何与完整系数

将合同中的 \(8c^2=-4P^2+PQ+2Q^2\) 代入，分别得到
\[
(P+Q)^2-4c^2=\tfrac32P(2P+Q),\qquad
(4P+Q)^2-16c^2=3(4P-Q)(2P+Q),
\]
\[
4P^2-PQ+Q^2-4c^2=\tfrac32P(4P-Q),\qquad
PQ-c^2=(4P-Q)(P+2Q)/8.
\]
它们与 TL.3 一致。保留正负号展开还给
\[
\lambda_\pm E_\pm^{\rm freq}
=3(2P+Q)(Q\pm2c).
\]
由于 \(P>Q/4\)，有 \(c^2<Q^2/4\)，两个 \(Q\pm2c\) 均严格为正，约分合法。故 \(h_+=h_-\)、\(\beta=0\)，并得到 TL.4 的 \(\alpha,\chi,\kappa=2\chi\)。当前 \(c\ne0,d<0\) 保证 \(\chi\ne0\)，但没有给两条边相同符号。

完整 C 的三个系数须另算。NC.9 给出的
\[
\chi^C=\frac{2cd^2}{Q\Lambda},\qquad
\alpha^C=\frac{2d(P+Q)}{\Lambda},\qquad
\beta^C=-\frac{4cd}{\Lambda}
\]
确实化为 TL.5，特别是
\(\chi^C=(d/P)\chi\)、\(\beta^C=-(2Q/P)\chi\ne0\)。因此 β 零没有删除 C 的面积项。未发现漏系数或错号。

## 3. TL.6–18：同一极化、法向负号及唯一最低 Z 消元

单位基满足 \(\widetilde N_j=-N_j\)。直接从 TL.8 转回 NC 坐标，除主稿列出的式子外，还有
\[
y_j^{\rm NC}=-\mathcal A_j\eta_j/\sqrt{\Delta_j},\qquad
x_j^{\rm NC}\overline{y_j^{\rm NC}}
=-\frac{|\mathcal A_j|^2\sqrt{Q_j}}{\Delta_j}
(\xi_j-i\tau_j).
\]
所以 NC 的实相干为负的 \(\xi_j\) 倍数，虚相干为正的 \(\tau_j\) 倍数。发送端法向负号和共轭顺序均已保留。由有向单位基直接计算
\(i\widehat q_j\cdot(U_j\times\bar U_j)=2|\mathcal A_j|^2\tau_j\)，与 TL.9 一致。

用接收 NC 坐标
\(u=z_0x_j\sqrt{P/\Delta_j}\)、\(v=z_0y_j/\sqrt{\Delta_j}\)
代入 NC.7–8，可核出公共因子 \(i z_0^2L_j|\mathcal A_j|^2\)。其单位基系数依次为
\[
\chi_jx_j^2,\qquad
\kappa_jx_jy_j-
\sqrt{P/Q_j}\,\alpha_j\xi_jx_j^2
+i\sqrt{P/Q_j}\,\beta_j\tau_jx_j^2.
\]
在 β 零域精确变成 TL.12；发送面积保留在同一向量中，只是未出现在此 Z 式子内。

由 \(E_2=\mathsf C E_1+\mathsf S N_1\) 和
\(N_2=-\mathsf S E_1+\mathsf C N_1\)，得到 TL.14 的两个不同符号。对总 Z 分别点乘 \(E_2,E_1\)，所得两实方程正是 TL.16。由于 \(\mathsf S\ne0\)，它们是完整横向向量零条件的等价检测；除以已非零的 \(\theta_1a^2,\theta_2b^2,\mathsf S\) 后，TL.17–18 的两个解及所有倒数项均正确。

未知 \(\xi_1,\xi_2\) 的系数向量是
\(-\theta_j\gamma_jx_j^2N_j\)。两向量独立且标量非零，故唯一性不是变量计数，亦没有遗漏降秩支。允许 \(\xi_j=0\) 和任一 \(y_j=0\)；它们均不迫使 \(\tau_j=0\)。固定发送实际投影 \(\mathcal A_j\) 后，\(w\) 的符号为 \(\operatorname{sgn}(c_1c_2)\)，与 TL.15 一致。

## 4. TL.19–25：完整 C 的实、虚方向条件

直接代入 NC.9，C 的单位基法向项与 Z 共用 \(\kappa_jx_jy_j\)，其余为
\(-\sqrt{P/Q_j}\alpha_j^C\xi_jx_j^2
+i\sqrt{P/Q_j}\beta_j^C\tau_jx_j^2\)。
结合 \(\alpha_j^C/\alpha_j=s_j\nu_j\) 和
\(\sqrt{P/Q_j}\beta_j^C/\chi_j=-2\sqrt{Q_j/P}\)，恰得 TL.20。乘回外部的 \(i\) 后，面积项成为 TL.21 的正号实向量 \(V_{\rm re}\)，不是负号。

每个 \(\theta_j\sqrt{Q_j/P}\tau_jx_j^2\ne0\)，而 \(N_1,N_2\) 实线性独立，故 \(V_{\rm re}\ne0\)，进而完整最低 C 非零。这个非零性不依赖最低 Z 已经消元；但它本身也不证明 C 沿原方向。

因为 \(R\) 实且非零，除去非零复数 \(z_0^2\) 后，C 属于 \(\mathbb C U_0=\mathbb C R\) 当且仅当两个实向量均属于 \(\mathbb R R\)。双线性行列式因此给 TL.22 的两个条件；这里没有误用 Hermitian 点积。

由 \([R,N_j]=x_j\) 得面积条件中的三次投影 \(x_j^3\)，TL.23 的负号、平方根和 \(w\rho^3\) 均正确。再用实际面积 \(\mathfrak h_j=2|\mathcal A_j|^2\tau_j\) 消去投影模方，得到 TL.24。另一条件由
\([R,E_j]=-y_j\)、\(2-d_j/P=(P+Q_j)/P=s_j\)
直接给 TL.25。面积条件并不自动支付这一实相干方向条件。

## 5. TL.26–29：正性与原权重 w 的三次式

令 \(r_j=Q_j/P\)，则 \(1<r_1<r_2<4\)。手工通分核得主稿关于
\(\mathsf B_2-\mathsf B_1\)、\(\mathsf A(r)-2\)、\(\mathsf B(r)+2\)
的三个恒等式均正确。特别是 \(D_*<0\)、\(\mathsf A_1>2\)、\(\mathsf B_2>-2\)、\(\mathsf B_1<0\)，保证 \(\mathsf L>0\)；\(\mathsf M=\mathsf A_2-D_*>0\)。再由
\[
\mathsf A_2-\mathsf A_1=(r_2-r_1)-D_*>0
\]
和主稿的乘积展开，严格得到
\(0<\mathsf L\mathsf M/(\mathsf A_1\mathsf A_2)<1\)。没有使用实际长度选择。

把 TL.14、17 代入 TL.25，先逐项复核 TL.29，再按 \(\rho\) 合并，四个系数分别为
\[
w\mathsf A_2\mathsf C,\quad
w(-\mathsf B_1+2\mathsf B_2-s_2)=-w\mathsf M,\quad
s_1-2\mathsf B_1+\mathsf B_2=\mathsf L,\quad
-\mathsf A_1\mathsf C.
\]
故 TL.28 的公共因子 \(\theta_1a^3/\mathsf S\) 及三次式均正确。对固定的原发送投影权重比 \(w\)，这是关于实际接收方向比 \(\rho\) 的式子；不能预先把 \(w\rho^2\) 当作与方向变化无关的同一个原权重。

## 6. TL.30–33：零分母、投影正交及吸收平方规范

在 \(\rho\ne0\) 的合同域，\(\Psi=\mathcal D w-\mathcal N\)。主稿对 \(\mathcal D\ne0\)、单零和双零的三类划分穷尽；\(\mathcal D\ne0,\mathcal N=0\) 只给被排除的 \(w=0\)。双零精确要求
\[
\mathsf C\ne0,\quad
\rho=\frac{\mathsf M}{\mathsf A_2\mathsf C},\quad
\mathsf C^2=\frac{\mathsf L\mathsf M}{\mathsf A_1\mathsf A_2}.
\]
该值严格在 \((0,1)\)，所以仅由 \(\mathsf S\ne0\) 不能排除；主稿没有把这点误报为已实现整数几何。此处“任意实际非零 w”只针对这一实方向方程，仍须满足符号、最低 Z、面积比和其余合同条件。

若 \(\mathsf C=0\)，则 \(\Psi=\rho(\mathsf L-w\mathsf M\rho)\)，排除 \(\rho=0\) 后恰得 TL.32。此时 \(\mathcal D=-\mathsf M\rho^2\ne0\)。又因
\(w\rho^3=\mathsf L^3/(w^2\mathsf M^3)>0\)，TL.23 强制面积异号。这里的 \(\mathsf C=0\) 是两个最低横向投影正交；不等于任何原频率对的点积为零，也不等于完整向量 C 为零。

代入 \(\mathfrak r=w\rho^2\) 后，TL.33 与 TL.28 完全等价。固定非零 \(\rho\) 时，\(w\leftrightarrow\mathfrak r\) 可逆且保号；固定原 \(w\) 改变 \(\rho\) 时，\(\mathfrak r\) 则随平方变化。此转换没有新增独立自由度。

为检验从另一方向解这个短式也没有隐藏漏支，若按 \(\mathfrak r\) 固定而解 \(\rho\)，其系数和右端同时为零恰要求
\[
\mathsf C\ne0,\quad
\mathfrak r=-\frac{\mathsf L}{\mathsf A_2\mathsf C},\quad
\mathsf C^2=\frac{\mathsf L\mathsf M}{\mathsf A_1\mathsf A_2}.
\]
此时短式对非零 \(\rho\) 恒成立，但必须同时恢复 \(w=\mathfrak r/\rho^2\) 及其实际符号；这不是原 \(w\) 固定下的任意方向。在该几何等式上，直接因式分解为
\[
\Psi=(\mathsf A_2\mathsf C\rho-\mathsf M)
\left(w\rho^2+\frac{\mathsf L}{\mathsf A_2\mathsf C}\right).
\]
第一因子为零是 TL.31；第二因子为零由 TL.30 的普通分式支覆盖，交点由 TL.31 覆盖。因此主稿原分类没有漏掉改用短式后呈现的分支。两种单独求解的双零描述不能直接混同。

## 7. TL.34–35、分母和通过范围

TL.34 的充要性成立于固定合同几何、同一实接收代表 R、实际非零发送投影及非零面积的坐标描述。TL.35 在 TL.34 成立后，又精确要求一个实方向方程和一个非零面积比；由 \(V_{\rm re}\ne0\) 保证方向输出非零。没有把零向量当作原方向返回。

分母条件逐项有依据：\(P,Q_j,\Delta_j\) 正；\(c_j,d_j\) 非零，故 \(\chi_j,\gamma_j,\theta_j\) 非零；活跃性给 \(a,b\ne0\)，进而 \(\rho,w\ne0\)；三频独立给 \(\mathsf S\ne0\)。允许零的接收法向坐标和发送实比值不作分母。真正变动的消元分母通过 TL.30–32 分支处理。非零面积发送向量的实部与虚部张成其横向实平面，故其与任一非平行实频率的复双线性点积非零；这也没有免除最低实接收的两条活跃性。

同一数据的代表变化 \(R\mapsto\lambda R,z_0\mapsto z_0/\lambda\)，其中 \(\lambda\) 为非零实数，保持 \(\rho,w\) 和所有向量条件。发送非零复缩放保留 \(\eta_j\)，并按 NC.10 的发送模方改变相应权重；不能借此把不同数据的幅度、方向条件拼在一起。

未发现需要修改数学公式的缺陷。唯一证据措辞点是文首记录的根规范建议来源，已在本非作者审查中明确补足披露，未夸大主稿的盲性。通过范围严格止于：**给定合同域内最低完整 Z 行与最低完整 C 原方向行的条件接口，以及最低 C 非零。**

本稿没有证明条件联合可实现于任何独立整数三频，没有证明两条较高接收的完整 M 行、另外两条 C 原方向行、共同幅度、平移或相容正交变换满足，也没有接受任何候选。单行条件充分性不能升级成全部实例充分性。没有本轮同一 NS 的短时方向结论、有限时刻模板、跨代再生成、无限尺度或有限总时间构造；没有奇性或全局正则性结论。EXACT LOWEST-ROW CONDITIONS ONLY；NO-CANDIDATE ACCEPTED；NOT CLAY。

本审查仅写本文件；实际全文回读本审查并复核绑定源字节后，最终 SHA-256 在停改通知中提供。
