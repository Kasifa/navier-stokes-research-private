# 原重联构造的 Stokes 基线：条件推论与归一化核对

2026-09-07。PRIVATE_CORE。由 Enciso–Lucà–Peralta-Salas 原文 Lemma 4.2、§4 Step 3 直接整理的有限条件推论；不是新颖定理或新的初值构造，不作冻结包。本记录不独立证明所引 KAM/拓扑稳定性结果。

**结论为肯定。** 原文分别压小了热演化中的非目标项和完整 NS 的非线性余项。因此，在同一份已经选定的有限计划中，纯 Stokes 热场与 NS 解均可在指定时刻进入同一个目标场的拓扑稳定邻域。这里比较的是各时刻的涡量线场及指定目标性质，不把热场称为 NS 解，不断言两个完整涡场的全部拓扑相同。

## 1. 实读位置与证据输入

本轮重新读取：arXiv v2 第 15 页 Lemma 4.2 的表述、归一化涡量条件及 Sobolev 接口（提取文本行 785–825）；第 20–22 页 Step 3，式 (4.8)–(4.12)、参数选择及最后的精确范数归一化（文本行 1103–1225）。完整 Duhamel 公式和对称张量约定沿用上一轮已经实读并图像核对的第 9、18 页。

| 输入文件（相对 `reconnection-preflight/`） | 本轮核对 SHA-256 |
| --- | --- |
| `CONTRACT.md` | `23eca817fca5500e6dc7e7ec5647272751929fd486c58ed3dd6f30d32a893cf4` |
| `THEORY_READING.md` | `50f67bf49150d254b398a1a60161f0e0ac92736dbdfee2f936e0b330e45cf418` |
| `theory/SOURCE_MANIFEST.json` | `a8c738c03717311770dd576e89e8862ade9365eaafaf94cff85b1b48415a8d94` |
| `theory/enciso-luca-peralta-salas-1606.06176v2.pdf` | `ba89fa2fa06cf1dd058f9ea121364a36c59c4cdc25880e4cc7754c89ed319269` |
| `theory/enciso-luca-peralta-salas-1606.06176v2.txt` | `c1077dfd622a7aca9c4e5b53caa1460c6f37022e175930bc7eb51e440e402390` |

原始来源：[arXiv:1606.06176v2](https://arxiv.org/pdf/1606.06176v2)，出版标识 [doi:10.1016/j.aim.2017.01.025](https://doi.org/10.1016/j.aim.2017.01.025)。本推论绑定作者 v2 的公式，不声称出版版逐字复核。

## 2. 严格条件版

固定原文的 \(2\pi\) 三维环面、\(\nu>0\)、有限时刻 \(T_k\)、整数 \(r\ge7\) 和 \(0<\alpha<1\)。目标场满足
\[
\operatorname{curl}W_k=N_kW_k,\qquad N_k\ge1.
\]
对每个所考虑的 \(k\)，令 \(\theta_k>0\) 为 Lemma 4.2 允许的归一化涡量邻域半径：若一个允许的无散场 \(Z\) 满足
\[
\left\|\frac{\operatorname{curl}Z}{N_k}-W_k\right\|_{C^{3,\alpha}}<\theta_k,
\tag{S.1}
\]
则其涡量线场具有该目标性质。奇数 \(k\) 的性质是包含与指定 \(S_k\) 微分同胚的涡线/涡管；偶数 \(k\) 的 \(W_k=B_{N_k}\) 对应没有可缩涡线/涡管。Lemma 4.2 的两部分可分别使用；若原表述以两个误差之和给出小性，取另一比较场恰为其目标即可。

令
\[
K_{r,\alpha}:=\|\operatorname{curl}\|_{H^r(\mathbb T^3)\to C^{3,\alpha}(\mathbb T^3)}<\infty.
\]
该有限性来自 \(H^r\hookrightarrow C^{4,\alpha}\)。\(K_{r,\alpha}\) 只依赖固定空间和范数约定，不依赖所选频率。拓扑半径 \(\theta_k\) 则必须按实际目标族取值；本记录不假定它对所有有限计划统一。

设 \(h(t)=e^{\nu t\Delta}u_0\)，\(u\) 为同一初值的完整 NS 解。若 \(c_k>0\)，且
\[
\left\|\frac{h(T_k)}{c_k}-W_k\right\|_{H^r}\le\eta_k,
\qquad
\left\|\frac{u(T_k)-h(T_k)}{c_k}\right\|_{H^r}\le\varepsilon_k,
\tag{S.2}
\]
则有严格的接口估计
\[
\left\|\frac{\operatorname{curl}h(T_k)}{c_kN_k}-W_k\right\|_{C^{3,\alpha}}
\le\frac{K_{r,\alpha}}{N_k}\eta_k,
\tag{S.3}
\]
\[
\left\|\frac{\operatorname{curl}u(T_k)}{c_kN_k}-W_k\right\|_{C^{3,\alpha}}
\le\frac{K_{r,\alpha}}{N_k}(\eta_k+\varepsilon_k).
\tag{S.4}
\]
因此
\[
K_{r,\alpha}(\eta_k+\varepsilon_k)<N_k\theta_k
\tag{S.5}
\]
足以让二者同享目标性质；热场自身只需 \(K_{r,\alpha}\eta_k<N_k\theta_k\)。一个留有明确余量的充分选择是
\[
\eta_k\le\frac{N_k\theta_k}{4K_{r,\alpha}},\qquad
\varepsilon_k\le\frac{N_k\theta_k}{4K_{r,\alpha}}.
\tag{S.6}
\]
式 S.3–4 的证明只需对 S.2 取 curl、使用 \(\operatorname{curl}W_k=N_kW_k\) 及三角不等式。正的空间常数 \(c_kN_k\) 只改变涡量积分曲线的参数速度，故不改变所比较的涡线几何及不变环面。这里的 \(\eta_k,\varepsilon_k\) 是**已经除以目标振幅**后的速度误差，不能用未归一化的绝对小误差代替。

## 3. 原构造的热误差是精确可读的

只复述原文已选的中间初值，记
\[
a=\sum_{j=0}^n\delta_jW_j,
\qquad \delta_0=M,\quad W_0=B_{N_0}.
\]
精确范数归一化后，允许初值为
\[
u_0=qa,\qquad q:=\frac{M}{\|a\|_2}>0.
\]
这只是原论文最后一步的记号，不在本记录中另选任何 \(W_j,N_j,\delta_j\)。由于各 \(W_j\) 都是对应 Laplacian 特征场，
\[
h(t)=q\sum_{j=0}^n\delta_je^{-\nu N_j^2t}W_j.
\]
取
\[
c_k=q\delta_ke^{-\nu N_k^2T_k},
\]
便精确得到
\[
\frac{h(T_k)}{c_k}=W_k+H_k,
\qquad
H_k=\sum_{j\ne k}\frac{\delta_j}{\delta_k}
e^{-\nu(N_j^2-N_k^2)T_k}W_j.
\tag{S.7}
\]
原文 (4.11) 恰好控制 \(\|H_k\|_{H^r}\ll1\)。因此纯热场的拓扑邻域条件不是从 NS 总误差中猜出来的，而是已被单独控制的输入。\(q\) 在 S.7 中**完全消去**，故热场的归一化误差和拓扑比较对这一最终精确归一化不变。

在 \(T_0=0\) 时，\(c_0=qM\)，
\[
H_0=M^{-1}\sum_{j=1}^n\delta_jW_j,
\qquad u(0)=h(0)=u_0.
\]
原文 (4.8) 使这一初始整体场落在 \(B_{N_0}\) 的稳定邻域。因此虽然所有后续速度分量都预置于 \(u_0\)，完整初始涡场并没有后来奇数时刻的那些可缩目标结构。热场基线不改变这一区别。

## 4. 完整非线性与精确 q 归一化

对最终初值 \(u_0=qa\) 的真实 NS 解，记
\[
w_q(t)=qMW_0e^{-\nu N_0^2t},\qquad v_q=u-w_q.
\]
\(w_q\) 本身是 Beltrami 热衰减解。沿用作者的对称张量约定
\[
(b\otimes d)_{ij}=\tfrac12(b_id_j+d_ib_j),
\]
定义
\[
L_q(t)=\int_0^t e^{\nu(t-s)\Delta}\mathbb P\operatorname{div}(v_q(s)\otimes w_q(s))\,ds,
\quad
B_q(t)=\int_0^t e^{\nu(t-s)\Delta}\mathbb P\operatorname{div}(v_q(s)\otimes v_q(s))\,ds.
\]
于是完整精确恒等式为
\[
u(t)-h(t)=-2L_q(t)-B_q(t).
\tag{S.8}
\]
若改用通常的有序外积，\(2v_q\otimes w_q\) 必须完整写为 \(v_q\otimes_{\rm ord}w_q+w_q\otimes_{\rm ord}v_q\)。压力由周期 Leray 投影保留；没有删去任何一向混合项、黏性或频率通道。S.8 沿用原式 (4.4) 的符号，未复制第 21 页重标公式中已记录的印刷不一致。

所需的一个直接误差上界是
\[
\varepsilon_k=\frac{2\|L_q(T_k)\|_{H^r}+\|B_q(T_k)\|_{H^r}}{q\delta_ke^{-\nu N_k^2T_k}}.
\tag{S.9}
\]
原文对未归一化中间初值的 Lemma 4.4 和 (4.12) 正是此类条件。对最终 \(q\) 需使用 \(qa\) 对应的真实解及其估计，不能令它等于 \(q\) 倍旧 NS 解。论文最后利用 \(q=1+O(\delta_1)\) 及所保留的严格小性余量重新适用这些估计。就此条件推论而言，也可直接把最终解的 S.9 作为明确假设；本记录没有为未列出的数值参数声称已获得一个数值误差界。

## 5. 原参数选择是否已支付条件

**已支付定性的有限计划条件。** Step 3 分别要求初始热误差 (4.8)、后续热误差 (4.11) 及重标后的非线性误差 (4.12) 足够小，然后调用同一个 Lemma 4.2。这正包含纯热场进入邻域所需的小性，也包含 NS 解相对热场的稳定余量。若需要把原文的 \(\ll1\) 明确为 S.6，可在原文允许的有限参数选择中事先指定这一更小阈值。

这一陈述不是“所有原文语法上允许的参数自动满足 S.6”。它表示：原存在性构造可以为给定有限目标族选择足够严格的余量。取有限个 \(\theta_k\) 的最小值是允许的，不能由此推得统一于 \(n\)、任意拓扑或任意时间表的下界。

也不能孤立地缩小 \(\delta_1\) 就宣称全部条件改善。S.7 中背景项含 \(M/\delta_k\)，可能因此增大。原选择需要协调操作：先分离 \(N_1,\ldots,N_n\) 以处理目标项的热比值，再选足够大的 \(N_0\) 和足够小的幅度常数。按原第 22 页的配方，\(\delta_1\) 对 \(N_0\) 的依赖只有幂次，而背景项有 \(e^{-\nu N_0^2T_k}\)，故在固定 \(T_k>0\) 和有限其余参数下可通过重新留足频率间隔支付该背景余量。归一化线性余项由 \(N_0^{-2}\) 支付，归一化双线性余项由幅度常数支付；最终仍须共同核对 (4.2)、(4.8)–(4.12)。本记录没有实际重新选参。

## 6. 这一基线比较说明什么

原构造的有限拓扑时间表同时通过热场的运动学比较和完整 NS 的误差控制。由此可把“进入某个稳定拓扑邻域”识别为该构造中热衰减本身已经实现的性质，而不是第一代非线性供给已经得到证明的判据。

这不否定 NS 中确有真实重联，也不声称一般 NS 重联都是线性过程。两场可以具有不同的其他涡结构；本记录只比较原文指定的性质。\(h\) 仅作为 Stokes 热场出现，不能因它满足相同的有限拓扑观测条件就称它满足完整 NS。这里没有新增放大、供给下界、统一返回映射或奇性结论，只把原文已明确解释的线性机制落实为可核对的基线条件。
