# 两高总纯方向独立稿：序贯非作者审查

2026-09-08，PRIVATE_CORE。审查对象为 INDEPENDENT.md 的 HDI.1–22 及形成、变换和未付范围。结论：逐式手核通过，无待修问题。通过内容包括完整总行方向与非零坐标判据、最低发送单边方向缺陷，以及共同恢复域内四个实际实条件。

本项没有证明真实两边缺陷不能相消，没有证明总行自动非零、三个比例符合共同模板或任何实际几何/原解机制存在。

## 1. 身份、阅读顺序和来源字节

本代理不是独立稿作者，但已先审本目录根主稿并形成 REVIEW.md。本次是随后实际阅读独立稿的序贯非作者审查，不能称互盲。独立作者形成本稿时未读根新稿的历史按其披露保留；不因本次后读比较而改写。审查者另有前阶段作者与审查经历。

本次证明核验直接从实际读取的 NC.9、FR 及独立稿明列恢复式完成，没有把根主稿的结论或本代理先前 REVIEW 的通过状态当作被审稿证明。

本次实际全文读取合同、独立稿和 FR，重读 NC 的指定完整系数段，并首次按需读取 JDI 的下列恢复段落。路径相对于 research/reverse/：

| 来源及本次实际范围 | SHA-256 |
| --- | --- |
| higher-pure-direction/CONTRACT.md；全文 | cdda8089bdfedd67d090634ca91fc25e83c33cd0072bd60235c98e5f11d55187 |
| higher-pure-direction/INDEPENDENT.md；全文 | 66aac8470f43aa84b04509c843551457c29414e7f9851bf507bde70a9d612363 |
| net-mixed-cancellation/INDEPENDENT.md；第 1–140 行，完整 NC.1–12 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |
| full-high-row-reduction/PROOF.md；全文重读 | 3d02da817e164bbf8f75bdddfea74a4e0d2b14c12d890952aeeb727866cc3c6b |
| joint-direction-compatibility/INDEPENDENT.md；第 24–161、306–390 行，固定域及明列共享恢复 | 4ed20002939dbafce9f20955dbcf3a0efde1da8aa2ad1f040ce474b9c5861c26 |

被审稿这四项来源绑定与当前实测一致。JDI 的读取只支持本文所用的明确恢复式和域；没有因此声称本次全文审过 JDI 中间联合论证或证明其允许集合非空。旧源内部转引不自动计为本轮实读，本次未重新推导全部原始有序树或任何黏性时间核。

## 2. HDI.1–7：单位基、发送法向及同一种子

几何的 \(N_{qp}=-N_{pq}\) 给 NC 坐标 \(y=-H/\sqrt\Delta\)。于是
\[
x\overline y=-\frac{\sqrt Q}{\Delta}|D|^2\overline\omega,
\]
其真实部为负 \(\sqrt Q|D|^2\operatorname{Re}\omega/\Delta\)，虚部为正 \(\sqrt Q|D|^2\operatorname{Im}\omega/\Delta\)。HDI.4 两相干号正确，不能因 \(N'\) 是反向法向而同时误反第二个号。

将 \(u=A\sqrt{P/\Delta},v=B/\sqrt\Delta\) 和这些发送量逐项代入 NC.9，得到平面项
\[
\frac{4i\Delta^{3/2}cd^2}{P^{3/2}Q\Lambda}A^2|D|^2
\]
及反馈项
\[
\frac{8i\Delta^{3/2}cd}{\sqrt P\,Q\Lambda}AB|D|^2.
\]
发送实、虚项分别组成
\(-i\theta\sqrt{PQ}A^2|D|^2
(\Sigma\operatorname{Re}\omega+2ic\operatorname{Im}\omega)\)。
因此 HDI.5 的 \(\theta\)、两处 \(d\)、完整反馈与两相干项均正确。此处是接收的复二次依赖，不是接收模方；发送相位只通过同一实际协方差消去。

高种子 \(y_i\ne0\) 保证任一非零实横向方向的复投影非零：归一化投影若为 \(\alpha+\beta s_i+i\beta y_i=0\)，则 \(\beta=0\) 再给 \(\alpha=0\)，矛盾。最低发送的两个投影则是原域明确的非零假设。因此实际应用中定义 \(\omega\) 的分母都有依据。

HDI.6 的 \(\theta,\xi,\psi,\lambda,\Omega\) 直接重组 HDI.5。由于 \(\theta\) 的号只取决于 \(P_i-P_k\)，确有
\(\lambda_{10},\lambda_{20},\lambda_{21}>0\)、\(\lambda_{12}<0\)；不能因发送模方正而把最后一项正化。

同向接收旋转给
\[
t_i=C_i+S_iz_i,\qquad
n_i=-S_i+C_iz_i=(C_it_i-1)/S_i.
\]
这不要求 \(C_i\ne0\)。FR 的实际发送比则是
\[
\omega_{ji}=(C_jt_j-1)/(S_jt_j),\quad
\operatorname{Re}\omega_{ji}=(C_j-X_j/M_j)/S_j,\quad
\operatorname{Im}\omega_{ji}=y_j/M_j,
\]
其投影模方同时为 \(|a_j|^2M_j\)。HDI.7 没有把虚比写成 \(Y_j/M_j\)，也没有为另一行另选相干。

HDI 第 2–4 节的这些恒等式及方向判据不需要先有完整混合零行或指定高投影为零；特别无需先除 \(X_i\)。第 5 节加入 FR/JDI 实际恢复后才使用 \(M_i=-2X_iB_i/\mu_i\) 等较强输入，两个域层次保留准确。

## 3. HDI.8–13：完整总行、a³ 行列式及 q 非零

最低贡献在 \(E_{i0},N_{i0}\) 基中的归一化坐标为
\[
\lambda_{i0}\bigl(\xi_{i0},\ \psi_{i0}z_i-\Omega_{i0}\bigr).
\]
另一贡献先在 \(E_{ij},N_{ij}\) 基写成
\[
\lambda_{ij}\bigl(\xi_{ij}t_i^2,
\psi_{ij}t_in_i-\Omega_{ij}t_i^2\bigr),
\]
再用 \(E_{ij}=C_iE_{i0}+S_iN_{i0}\)、
\(N_{ij}=-S_iE_{i0}+C_iN_{i0}\) 转回。其第一坐标恰为
\[
\lambda_{ij}\{(C_i\xi_{ij}+S_i\Omega_{ij})t_i^2
-S_i\psi_{ij}t_in_i\},
\]
第二坐标也与 HDI.9 一致。两条贡献确实先在同一个接收平面相加。

由第一接收坐标 \(a_i\ne0\)，直接有
\[
[U_i,\mathcal C_i]=ia_i^3(\mathfrak n_i-z_i\mathfrak q_i).
\]
也可在高边自身同向单位基求行列式：该边贡献为
\[
\lambda_{ij}t_i^2\{(\psi_{ij}-\xi_{ij})n_i-\Omega_{ij}t_i\}.
\]
利用 \(\psi_{ik}-\xi_{ik}=c_{ik}\Sigma_{ik}\)，分别核得 HDI.10 的最低项和高边项。这条独立展开没有借根稿代替证明。

复二维横向平面内，非零 \(U_i\) 与总行线性相关恰等价于其双线性行列式为零。因此 HDI.11 成立，且包含零总行。当该方向式已成立时，\(\mathfrak n_i=z_i\mathfrak q_i\)，所以
\[
\mathcal C_i=ia_i\mathfrak q_iU_i,\qquad
W_{0,i}=(ia_i\mathfrak q_i/3)U_i.
\]
故 HDI.12 的总行非零 iff 准确；但它必须和 HDI.11 联用。若不先有方向式，第一坐标为零本身不等于总行零。

这里没有除 \(U_i\cdot U_i=a_i^2(1+z_i^2)\)，复各向同性情形仍成立。接收相位是 \(a_i^3\)，发送仍为真实 Hermitian 模方；不能改成 \(|a_i|^2a_i\)。

## 4. HDI.14：新增单条最低发送方向缺陷

最低发送种子沿实 \(R\)，故其发送比 \(v_{0i}\) 实，最低项的归一化行列式准确为
\[
\lambda_{i0}\Sigma_{i0}
\{c_{i0}s_i-\sqrt{P_iP_0}v_{0i}+ic_{i0}y_i\}.
\]
该复数的虚部为 \(\lambda_{i0}\Sigma_{i0}c_{i0}y_i\ne0\)：\(\lambda_{i0}>0\) 使用真实最低投影非零和 \(P_i>P_0\)，另有 \(c_{i0}\ne0,y_i\ne0,\Sigma_{i0}>0\)。因此单条最低发送贡献必不沿高种子的复方向。

这是本独立稿新增且在本轮直接手核的必要结构；它甚至不需要预先支付完整混合零行。若高总方向成立，另一高发送的方向行列式必须非零，并准确抵消该缺陷。因此“两条单边各自先沿原方向”的做法在此域失败。

但两缺陷相消仍是允许情形；总行也仍可能在相加后为零。本结论没有证明相消不可能或总行非零，没有使用虚部非零去推出错误的全局方向障碍。

## 5. HDI.15–20：共同面积的四个实际实条件

加入明列恢复域后，\(D_i=y_i^2>0\)、\(y_j=k_i y_i\)，其中 \(k_1=k,k_2=1/k\)。这使高边发送虚相干成为同一实际 \(y_i\) 的倍数，不能另设自由变量。

将 \(n_i=(C_it_i-1)/S_i\) 与实际 \(\Omega_{ij}\) 代入 HDI.10，括号准确化为
\[
(\mathsf H_i-i\mathsf V_i y_i)t_i^3-\mathsf L_i t_i^2.
\]
\(\mathsf H_i\) 中的 \(S_i,S_j\) 分母、\(\mathsf L_i=c_{ij}\Sigma_{ij}/S_i\) 及
\(\mathsf V_i=2c_{ij}\sqrt{P_iP_j}k_i/M_j\)
均与 HDI.16 一致。\(\mathsf H_i\) 的发送实比若改写为
\((C_j+\mu_j/(2B_j))/S_j\)，约去 \(X_j\) 的依据只在这里已付的实际投影域中成立。

直接展开
\[
t_i^2=X_i^2-S_i^2D_i+2iX_iS_iy_i,
\]
\[
t_i^3=X_i(X_i^2-3S_i^2D_i)
+iS_iy_i(3X_i^2-S_i^2D_i).
\]
在 \(-i\mathsf V_i y_i t_i^3\) 中，两次 \(i\) 相乘给实部的正项
\[
+\mathsf V_iS_iD_i(3X_i^2-S_i^2D_i);
\]
虚部除以非零 \(y_i\) 后则为负项
\[
-\mathsf V_iX_i(X_i^2-3S_i^2D_i).
\]
其余 \(\mathsf H_i,\mathsf L_i\) 项及最低项逐项相加，正好得到 HDI.19 的两个实残差。因此
\(\mathcal F_i=\mathcal D_i^{\rm R}+iy_i\mathcal D_i^{\rm I}\)，HDI.20 的四实 iff 成立。

这一分离没有除 \(\mathsf H_i,\mathsf L_i,\mathsf V_i\) 或相干括号；允许的系数消失直接由原式处理。总行非零仍另需 \(\mathfrak q_1\mathfrak q_2\ne0\)，不能由四个方向残差为零代替。

## 6. HDI.21–22：恢复、共同翻号、相位和尺度

实际读取的 JDI 段落给出同一 \(r\) 上的 \(R\)、\(w\)、\(X_i\)、正面积、真实有符号 \(k\)、两发送模方及共同正 \(h\)。HDI.21 逐项与这些明确公式一致。其使用是条件性的，不能从形式上的方向根自动宣称面积、共同 \(h\) 或完整混合行已通过。

最低投影为 \(z_0r_i\)、\(r_1=1,r_2=r\)，高发送投影为 \(a_jt_j\)，所以
\[
\lambda_{i0}=\theta_{i0}hr_i^2,\qquad
\lambda_{ij}=\theta_{ij}|a_j|^2M_j
\]
准确成立。负号可能来自 \(\theta_{12}\)，不来自发送模方。两高方向检验使用同一 \(h\) 与同一组发送，不分行重选。

同时翻转 \(y_1,y_2\) 时，\(k_i,X_i,M_i,D_i,\lambda,\mathsf H_i,\mathsf L_i,\mathsf V_i\) 不变，故四个 \(\mathcal D\) 残差不变。\(z_i,t_i,n_i\) 及 \(\Omega_{ij}\) 同步取复共轭，HDI.9 因而给
\(\mathfrak q_i\mapsto\overline{\mathfrak q_i}\)，总行非零状态也不变。这里说的是归一化坐标的共轭，不把保持 \(a_i\) 不变的共同翻号误说成整个复种子的无条件共轭。单独翻一条面积则不保留原 \(k\)。

各种子乘单位相位时，发送投影模方及比值不变；接收方向行列式只乘对应的非零三次相位。因此相位不能修复已经失败的方向门或总行零状态。但比例 \(ia_i\mathfrak q_i/3\) 仍含接收相位，稿件正确保留了共同模板比例的后续检查，没有宣称相位对模板条件也无作用。

共同改变整体正模方尺度 \(\mathcal B\) 时，\(h,|a_1|^2,|a_2|^2\) 同比变化，\(\lambda,\mathcal D_i^{\rm R},\mathcal D_i^{\rm I},\mathfrak q_i\) 因而同乘正尺度；其零状态不变。面积平方 \(D_i=y_i^2\) 和归一化 \(X_i,M_i\) 不随此整体尺度改变，须与名称相近的方向残差 \(\mathcal D_i\) 区分。这一结论不允许重新选择相对发送幅度。

## 7. 除法、零支和最终范围

全部分母来自正长度、\(\Delta,\Lambda\)，已付非零发送投影、\(S_i,S_j,t_i,M_i,y_i,k\)，以及 JDI 明列恢复域。早期直接总方向式不需除 \(X_i\)；进入实际指定投影恢复后其非零性才由 FR 支付。没有除 \(C_i,s_i,1+z_i^2,\alpha,\beta,G_i\) 或可能为零的相干括号。平行、正交、等长、零发送或零面积的合同外分支没有因本稿被全域排除。

本次通过的是 HDI.1–22 所给条件接口及新增单条最低发送方向缺陷。总行零分支明确保留；共同面积翻号、相位与整体尺度不能修复方向失败，但这些不变量也不证明方向条件必失败。合法三频与同一种子是否同时满足四实式及非零条件仍 OPEN。

三个行非零、共同模板幅度、真实空间实例、原解时间窗、NS 两步、有限时间再生成、统一及跨代余项、单初值无限尺度与有限总时间均未由本项支付。无实际候选，旧失败未修复；精确空间首项筛选不排除任意正来源容限。

本次只有手工符号推理、文本读写及 SHA-256 元数据核验，没有科学程序、数组、数值求值、实际选参、特例、枚举、扫描、Git、重置或外发。最终全文自读并复核来源字节后停止修改，自身哈希另报。PASS WITHIN THE STATED SAME-DATA DOMAINS；SEQUENTIAL NON-AUTHOR REVIEW；REALIZATION OPEN；NO-CANDIDATE；NOT CLAY。
