# 两高总纯供给原方向主稿：非作者逐式审查

2026-09-08，PRIVATE_CORE。审查对象为 PROOF.md 的 HC.1–13 及总行非零、共同幅度和未付范围。结论：在明列同一数据及非零投影域内手核通过，未发现需要修改的问题。完整 NC.9 的单位基换算、接收三次相位因子、两条真实发送权重、方向式的非零倍数及有限降次均准确。

通过范围仅为两条较高总纯供给行属于各自原复种子直线的条件检验。零总行仍可能通过该方向检验；两个总行非零、共同模板幅度及实际几何/原解实现均未由本稿证明。

## 1. 身份、实际阅读及来源字节

本代理不是本稿作者。此前已审查 NC、完整高行、最低纯方向及后续幅度/面积等相关文本，并有前阶段作者经历；这里是对本项新主稿的非作者审查，不称全课题盲审。本次没有读取 higher-pure-direction/INDEPENDENT.md 或其它本项新推导。

本次先全文阅读合同与主稿，再实际重读下列旧源段落。路径相对于 research/reverse/：

| 来源及本次实际范围 | SHA-256 |
| --- | --- |
| higher-pure-direction/CONTRACT.md；全文 | cdda8089bdfedd67d090634ca91fc25e83c33cd0072bd60235c98e5f11d55187 |
| higher-pure-direction/PROOF.md；全文 | b5eedc38fb528bbb48e2ae51012742612a64edb87f88d22223b55d7a2b7ac488 |
| net-mixed-cancellation/INDEPENDENT.md；第 1–120 行，完整 NC.1–10 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |
| full-high-row-reduction/PROOF.md；第 1–115 行，FR.1–10 及紧接虚部开头 | 3d02da817e164bbf8f75bdddfea74a4e0d2b14c12d890952aeeb727866cc3c6b |
| two-elliptic-compatibility/PROOF.md；第 230–315 行，最低纯方向与非零范围；不作本稿新系数输入 | 8961c72504eb7d60f35ee53050c99a2a25203ad539f85a9135ca16706dcc1cba |

主稿已列的 NC、FR 散列与实测一致。使用的是 NC.9 已明确的完整空间映射和 FR 的直接同数据等式，没有重称本次复核了其背后所有树、全部原始 Leray 推导或时间核；内部转引不自动计为本次全文阅读。

## 2. HC.1–3：反向法向与完整纯 C 五系数

在 NC 的非单位基 \(e,f,n=p\times q\) 中，单位基满足
\[
E_{pq}=\sqrt{P/\Delta}\,e,\qquad
E_{qp}=\sqrt{Q/\Delta}\,f,\qquad
N_{pq}=n/\sqrt\Delta,\quad N_{qp}=-n/\sqrt\Delta.
\]
所以
\[
u=a\sqrt{P/\Delta},\quad v=az/\sqrt\Delta,\quad
x=b\sqrt{Q/\Delta},\quad y_{\rm NC}=-b(s+iy)/\sqrt\Delta.
\]
最后一个负号不能省略。直接取 \(x\overline{y_{\rm NC}}\) 得
\[
R_{\rm NC}=-|b|^2\sqrt Q\,s/\Delta,\qquad
I_{\rm NC}=|b|^2\sqrt Q\,y/\Delta.
\]
同一发送复系数只以实际 \(|b|^2\) 出现，其实虚相干保留符号。

把以上表达逐项代入 NC.9，平面系数手核为
\[
4i\,a^2|b|^2\,
\frac{\Delta^{3/2}cd^2}{P^{3/2}Q\Lambda}.
\]
法向三项则为
\[
a^2|b|^2\left\{
\frac{8i\,cd\Delta^{3/2}}{\sqrt P\,Q\Lambda}\,z
-\frac{4i\,d(P+Q)\Delta^{3/2}}{P\sqrt Q\,\Lambda}\,s
+\frac{8cd\Delta^{3/2}}{P\sqrt Q\,\Lambda}\,y
\right\}.
\]
分别除以 \(iL_{pq}a^2|b|^2\)，准确给出 HC.3 的 \(L_{pq},K_{pq},\kappa_{pq},A_{pq}^{C},B_{pq}^{C}\)。特别最后一个实际实项在该归一化下是 \(iB_{pq}^{C}y\)，\(B_{pq}^{C}\) 为稿中带负号的表达，不能把它改成正发送面积项。平面、自接收反馈、发送实相干、发送虚相干全部来自完整 NC.9，没有删减有序项。

原域 \(P,Q>0,\Delta>0,c,d\ne0\) 给
\(\Lambda=(P-Q)^2+4\Delta>0\)，从而 \(L_{pq}>0,\kappa_{pq}\ne0\)。HC.3 与 NC 的 \(\kappa\) 正是同一个系数。HC.4 中除 \(c\) 和 \(\kappa\) 在此合法；这套方向归一化不声称覆盖正交、等长或零平面投影的域外分支。

## 3. HC.4–5：接收 a³ 与双线性方向判据

直接比较五系数可核
\[
\kappa-K=\kappa\frac{P+Q}{2P},\qquad
A^{C}/\kappa=-\sqrt{Q/P}\frac{P+Q}{2c},\qquad
B^{C}/\kappa=-\sqrt{Q/P}.
\]
由于 \([E_{pq},N_{pq}]_p=1\)，行列式展开为
\[
[a(E+zN),C]_p
=iLa^3|b|^2\{(\kappa-K)z+A^{C}s+iB^{C}y\}.
\]
这准确得到 HC.5。接收幂为 \(a^3\)，不是 \(|a|^2a\)；前者来自原纯向量对接收的复二次依赖，再乘行列式中的同一接收系数。发送系数仍为 \(|b|^2\)，没有在此重新配相位。

在复化的二维横向平面上，非零 \(U\) 与 \(C\) 的该双线性行列式为零，恰等价于 \(C\in\mathbb C U\)。可直接按 \(E,N\) 两坐标解线性相关性，不需要除 \(U\cdot U\)。所以复各向同性的 \(U\cdot U=0\) 情形仍被覆盖；\(C=0\) 同样被方向判据包含。

## 4. HC.6–9：同一发送相干和 η 权重

从同一个高种子
\[
t_i=C_i+S_i(s_i+iy_i)
\]
换基，得到接收比 \((C_it_i-1)/(S_it_i)\)。同一发送 \(U_j\) 的实虚比则与 FR.6–7 完全相同：
\[
s_{ji}=(C_j-X_j/M_j)/S_j,\qquad y_{ji}=y_j/M_j.
\]
不是 \(Y_j/M_j\)。这里 \(Y_j=S_jy_j\) 已与换基分母中的 \(S_j\) 抵消，发送实际投影模方仍为 \(|a_j|^2M_j\)。

最低发送投影是 \(z_0\xi_i\)，\(\xi_i\) 为非零实数，所以两条实际权重恰为
\[
\eta_{i0}=L_{i0}h\xi_i^2>0,\qquad
\eta_{ij}=L_{ij}|a_j|^2M_j>0.
\]
对 \(ij\) 边，接收平面投影由 \(a_i\) 变为 \(a_it_i\)，因此行列式带 \(t_i^3\)，发送权重带 \(M_j\)。这分别支付 HC.8 的两个关键因子，不能相互替换或独立选择。

两个接收基之间是同向单位旋转，其行列式为一；两边在同一个法向 \(p_i/\sqrt{P_i}\) 下相加。故 HC.8 检查的是总行，没有要求每条单边各自沿原方向。若改用 NC.3 的 \(W_{0,i}=(C_{i0}+C_{ij})/3\)，共同非零因子 \(1/3\) 不改变这里的方向或零行判据；本稿未将这种方向等价当作共同模板已支付。

FR.3–5 给实际
\[
b_i=\frac{\eta_{ij}\chi_{ij}}{\eta_{i0}\chi_{i0}},
\quad \mu_i=\frac{\kappa_{i0}}{\chi_{i0}}>2,\quad
\rho_i=\frac{\kappa_{ij}}{\chi_{ij}},
\quad b_i=-\frac{\mu_i}{2X_i}.
\]
逐项约分即
\[
\frac{\eta_{ij}\kappa_{ij}}{\eta_{i0}\kappa_{i0}}
=\frac{b_i\rho_i}{\mu_i}=-\frac{\rho_i}{2X_i}.
\]
HC.9 正确。\(X_i\ne0\) 与高边 \(\chi_{ij}\ne0\) 都由实际非实指定投影式支付；没有把 \(\rho_i\) 或权重比预设为正，也没有重新选择行幅度。

## 5. HC.10–13：非零倍数和实际降次

HC.8 乘 \(2X_iS_i\) 并用 \(z_i=(t_i-C_i)/S_i\) 后，最低项成为
\[
2X_i\{\ell_{i0}(t_i-C_i)+S_i a_{i0}^{D}v_{0i}\}.
\]
高边项成为
\[
-\rho_i\{\ell_{ij}t_i^2(C_it_i-1)
+S_it_i^3(a_{ij}^{D}s_{ji}+ib_{ij}^{D}y_{ji})\}.
\]
这与 HC.10 完全一致。其完整乘数为
\[
\mathcal K_i
=\frac{2X_iS_i}{i a_i^3\eta_{i0}\kappa_{i0}}
[U_i,C_{i0}+C_{ij}]_i.
\]
分子和分母的各因子均非零，所以零式可双向恢复。乘数可能为复数或带号，只用于等式；没有用它保留未经证明的不等式符号。

在实际 \(t_i=X_i+iY_i\)、\(M_i=X_i^2+Y_i^2\) 上，
\[
t_i^2=2X_it_i-M_i,\qquad
t_i^3=(4X_i^2-M_i)t_i-2X_iM_i.
\]
这两式直接相乘回代成立，无需除 \(Y_i\)、\(4X_i^2-M_i\) 或任何化简系数。把高边三次项写为
\[
(\theta_i+i\epsilon_i)t_i^3-\ell_{ij}t_i^2
\]
再代入，分别汇集 \(t_i\) 项与常数项，恰得 HC.12 的 \(\mathcal A_i,\mathcal B_i\)，包括常数中的
\(+\rho_i\{2X_iM_i(\theta_i+i\epsilon_i)-\ell_{ij}M_i\}\)。

这些系数依赖同一种子的实际 \(X_i,M_i\) 及另一发送的相干，不是对一个自由变量 \(t\) 给出的独立一次方程。此次降次也没有声称得到关于方向 \(r\) 的固定低次多项式。

展开 \((A_R+iA_I)(X_i+iY_i)+B_R+iB_I\)，HC.13 的实虚两式及所有符号正确。没有除 \(\mathcal A_i,\mathcal B_i,\theta_i\) 等量：\(\mathcal A_i=0\) 时仍准确要求 \(\mathcal B_i=0\)，其它系数消失亦按原式处理。发送面积继续通过实际 \(\epsilon_i=S_i b_{ij}^{D}y_j/M_j\) 保留，未随降次删除。

## 6. 总行零、共同幅度和通过范围

对 \(i=1,2\) 同时检验 HC.10 或 HC.13，在原同数据前提下给出两个总纯行沿各自原复直线的准确四实条件。两条行同时使用同一组种子、实际 \(\eta\) 与发送相干，不按行拼接。

方向成立仍允许某个总行为零。主稿仅在方向式已成立后使用
\[
\gamma_i=\frac{(C_{i0}+C_{ij})\cdot\overline{U_i}}{|U_i|^2}
\]
恢复其比例；分母是严格正的 Hermitian 范数，因而在此时总行非零恰等价于 \(\gamma_i\ne0\)。该公式本身不先证明方向，也没有证明 \(\gamma_i\ne0\)、各行幅度一致或模板相位关系。

最低纯行非零与原方向只能按已明确的前置最低条件引用，不能从单边纯 C 非零推总行非零。即便另行支付完整混合零行及最低纯方向，本稿四式也只补两高纯方向；没有自动补足共同模板或实际原解供给。

当前固定非正交、互异长度、非零投影、实际指定高投影及非零 \(\chi\) 域之外的分支，本稿没有作全域排除。合法整数几何及同一种子是否能共同满足这些方向式仍未证明存在或无解。没有实际参数、方向根、初值、幅度、时间选择，没有新黏性时间核、同解余项、有限两步、跨代一致控制、单初值无限尺度、有限总时间或奇性结论，旧失败不变。

本次工具仅用于文本读取、文本写入及 SHA-256 元数据核验，没有科学程序、数组、数值求值、实际选参、特例、扫描、Git、重置或外发。最终全文自读并复核来源字节后停止修改，自身 SHA-256 另报。PASS WITHIN THE EXPLICIT SAME-DATA DOMAIN；TOTAL PURE-DIRECTION TEST ONLY；NO-CANDIDATE；NOT CLAY。
