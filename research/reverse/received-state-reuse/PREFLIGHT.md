# 真实接收场的复状态、投影演化与能量账

2026-09-09，PRIVATE_CORE。**可复用状态接口；当前没有已付资格的新系数计算候选（NO-CANDIDATE）。** 同一原解的 h=P_Du 属于一个由两复维横向代表描述的状态类；完整内部二次项在 D 上无直接回灌。实际 h 的能量可以与全部外场交换，不能由这一投影零推出实际 h 恒衰减、外部全属初始种子或一般再生失败。

作者 coherence_independent_resumed 曾写六载波结构预筛、A/B 和差型主核、接收支持桥、两项几何/整格预筛。根在本问开始前披露了 C₃ 对称与 D 二和支持预见，没有向本人给出下述能量消项公式；本稿在该非全盲背景下独立手核。差型包已完成冻结，本稿不将它重新标为 pending，也不混入其成果范围。没有读取根在本目录的新推导。

## RU.1 原解与全部允许复横向状态

固定 CT.1–2 的同一个 a_*、ν=1、无外力标准 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\)，不重置原解。记
\[
R(x_1,x_2,x_3)=(x_3,x_1,x_2),\quad
\kappa=(3,4,6),\quad k_j=R^j\kappa,\quad D=\{\pm k_j\}.
\]
原初值满足 \(a_*(Rx)=Ra_*(x)\)。旧 CS.3 已逐项核验
\[
\mathbb P_{Rk}=R\mathbb P_kR^{-1},\qquad
B(\mathcal T_Rf,\mathcal T_Rg)=\mathcal T_RB(f,g),
\quad e^{t\Delta}\mathcal T_R=\mathcal T_Re^{t\Delta}.
\]
由完整原解的同数据经典唯一性，在每个实际存在的经典区间，
\[
u(Rx,t)=Ru(x,t),\quad
\widehat u(-k,t)=\overline{\widehat u(k,t)},\quad
k\cdot\widehat u(k,t)=0.
\tag{RU.1}
\]
这只联系完整频率的循环轨道，不把十二模初始空间视为不变空间。零均值由原方程保持。

令 \(H(t)=\widehat u(\kappa,t)\)。上述三条结构约束在 D 上的完整状态表示为
\[
\widehat h(k_j,t)=R^jH(t),\qquad
\widehat h(-k_j,t)=R^j\overline{H(t)},\qquad
3H_1+4H_2+6H_3=0.
\tag{RU.2}
\]
因此可以精确参数化为
\[
H=\left(\xi,\eta,-\frac{3\xi+4\eta}{6}\right),\qquad
\xi,\eta\in\mathbb C.
\tag{RU.3}
\]
这些是形式状态坐标，不是另选的实际幅度。任意这样的 H 都定义一个满足上述对称、实值和无散条件的 D 支撑场；反过来每个满足这些条件的 D 场都由它唯一确定。**这不是说固定 a_* 的真实轨道遍历这个两复维空间，或其中任意状态已由该原解达到。**

写 H=X+iY，X,Y 为实横向向量，则
\[
h(x)=2\sum_{j=0}^2R^j\bigl[X\cos(k_j\cdot x)-Y\sin(k_j\cdot x)\bigr].
\tag{RU.4}
\]
完整范数保留相干：
\[
|H|^2=|\xi|^2+|\eta|^2+\frac{|3\xi+4\eta|^2}{36}.
\]
不能将只在首时间项中成立的 H 为纯虚或沿一个固定极化向量，延伸为实际 H(t) 的全时约束。原初值余弦相位本身也不提供完整 NS 的中心奇性。本文不先验删去 X，不把两个复坐标缩成两种强度。

## RU.2 完整投影演化，非闭合 ODE

记 z=u−h。D 的三个生成元独立，而两个带符号基向量的和不可能是一个带符号基向量，故
\[
D\cap(D+D)=\varnothing,\qquad P_DB(h,h)=0.
\tag{RU.5}
\]
旧 RS.3–4 还给 \(B(h,h)\) 的非零输出仅可能在三对和型及三对差型。RU.5 并不说完整 \(B(h,h)=0\)。

完整投影方程因此是
\[
\partial_t h=-61h+
P_D\bigl[B(h,z)+B(z,h)+B(z,z)\bigr].
\tag{RU.6}
\]
这里 \(|k_j|^2=61\)，固定 ν=1 的黏性没有被删去。两个交叉作用有序且不同。令右侧非黏性代表为 Ξ，则
\[
\dot H=-61H+\Xi,
\tag{RU.7}
\]
\[
\Xi=-i\mathbb P_\kappa
\sum_{a+b=\kappa}
\left[(h_a\cdot b)z_b+(z_a\cdot b)h_b+(z_a\cdot b)z_b\right].
\tag{RU.8}
\]
点积在卷积中为复双线性，负频系数按 RU.2 和 z 的实值条件处理；最后一项是全部外场的完整卷积，不能用原种子或一个有限尾近似替代。经典性使所需 Fourier 和绝对收敛。Ξ 与 κ 横向，且其余 D 模仍按同一个 R 和共轭恢复。

在任意实际存在的 [s,t] 上，准确热延续为
\[
H(t)=e^{-61(t-s)}H(s)+\int_s^t e^{-61(t-r)}\Xi(r)\,dr.
\tag{RU.9}
\]
Ξ 不是已知的 H 函数。RU.7 是完整原解的投影恒等式，不是已经构造出的有限维闭合系统。若人为只保留直接纯 D 项，它只留下热衰减；这不能用于替换真实 Ξ 或判断真实 H(t) 的增长号。

压力保持原完整周期压力：
\[
p_k=-\frac1{|k|^2}\sum_{a+b=k}(k\cdot u_a)(k\cdot u_b),\quad k\ne0,
\qquad p_0=0.
\tag{RU.10}
\]
它包含所有 h/z 交叉及外场项。RU.8 中 Leray 已精确包含这个压力作用，不是另设压力为零。后面的能量配对中压力为零，另由周期分部积分与无散性证明。

## RU.3 直接混合所需外场及尚未封闭的部分

定义固定集合
\[
E=\{\pm(k_j+k_{j+1}),\ \pm(k_j-k_{j+1}):j=0,1,2\},
\qquad b=P_Eu=P_Ez.
\tag{RU.11}
\]
E 是旧 RS.4 的十二个有符号可能输出，不与 D 相交。对输出 m∈D 与 h 输入 a∈D，另一输入必须是 m−a。若 m=a，则该外模是零模，当前 z 的均值为零；若 m=−a，则另一模为 2m，两种有序点积都因横向与共线而为零；其余情况恰在 E。故精确有
\[
P_D\bigl[B(h,z)+B(z,h)\bigr]
=P_D\bigl[B(h,b)+B(b,h)\bigr].
\tag{RU.12}
\]
零均值条件在此必要地被使用，不能将这个结论无条件搬到带恒定输运速度的状态类。

E 有两个正负循环轨道。若取 \(\sigma=k_0+k_1\)、\(q=k_0-k_1\)，则 b 同样由两个完整复代表
\(b_\sigma\in\sigma^\perp\otimes\mathbb C\)、
\(b_q\in q^\perp\otimes\mathbb C\) 及共轭/循环描述；每个代表均有两复维。该完整外场状态不能只记录两种能量或一个首项极化。

即使保留 b，仍有
\[
\Psi=P_DB(z,z).
\tag{RU.13}
\]
若写 \(z=b+c\)，其中 c 包含 D∪E 之外的全部实际模，RU.13 含
\(P_D[B(b,b)+B(b,c)+B(c,b)+B(c,c)]\)。本文没有将其中任何未证为零的项删除。不同外模之和可落在 D，故 RU.12 只缩小直接混合的输入范围，不把完整外场二次来源变成有限 E 系统。

## RU.4 完整实能量账

为明确周期胞测度，以下用归一化内积
\[
\langle f,g\rangle_2=(2\pi)^{-3}\int_{\mathbb T^3}f\cdot g\,dx
=\operatorname{Re}\sum_k f_k\cdot\overline{g_k}.
\]
场 f,g 为实际实值场，复 Fourier 向量的长度取 Hermitian 欧氏范数。若改用未归一化积分，以下能量和所有通量、耗散同时乘 \((2\pi)^3\)，不混用两套数。

由 RU.2 的六模且不重复计对，
\[
\|h\|_2^2=6|H|^2,\quad
\|h\|_{A0}=6|H|,\quad
\mathcal E_h:=\tfrac12\|h\|_2^2=3|H|^2,
\quad \|\nabla h\|_2^2=61\|h\|_2^2.
\tag{RU.14}
\]
每一个正负频率对的能量为 \(|H|^2\)。这不是仅从总带非零推定某一对；它使用了同一真实 C₃ 状态。

对周期实值无散 f,g,v，完整 Leray 的自伴随性及分部积分给
\[
\langle f,B(g,v)\rangle_2
=-\langle v,B(g,f)\rangle_2.
\tag{RU.15}
\]
具体地，左侧是 \(-\int f\cdot(g\cdot\nabla)v\)，分部积分变为 \(+\int v\cdot(g\cdot\nabla)f\)，即右侧；积分均采用上面的归一化。压力项亦由 \(\int f\cdot\nabla p=0\) 消去，不能因此在实际状态方程中删去压力。

RU.15 仅在以下能量配对中支付相消：
\[
\langle h,B(z,h)\rangle_2=0.
\tag{RU.16}
\]
这不是 \(P_DB(z,h)=0\) 的向量身份，故 RU.6–8 仍保留它。另两个能量项定义为
\[
\begin{aligned}
\mathcal J_1&=\langle h,B(h,z)\rangle_2
=-\langle z,B(h,h)\rangle_2
=-\langle b,B(h,h)\rangle_2,\\
\mathcal J_2&=\langle h,B(z,z)\rangle_2
=-\langle z,B(z,h)\rangle_2,\qquad
\mathcal J=\mathcal J_1+\mathcal J_2.
\end{aligned}
\tag{RU.17}
\]
其中 b 的替换使用 \(\operatorname{supp}B(h,h)\subset E\)，没有假定 b 来源于哪一批叶。\(\mathcal J_1,\mathcal J_2\) 均为有符号真实量，未得正号或负号控制。

从完整 RU.6 得
\[
\boxed{\frac d{dt}\mathcal E_h+122\mathcal E_h
=\mathcal J=6\operatorname{Re}(\overline H\cdot\Xi).}
\tag{RU.18}
\]
令 \(\mathcal E_z=\frac12\|z\|_2^2\)。z 的方程保留全部四项
\(P_{D^c}[B(h,h)+B(h,z)+B(z,h)+B(z,z)]\)。其能量中的
\(\langle z,B(h,z)\rangle_2\) 与 \(\langle z,B(z,z)\rangle_2\)
分别由 RU.15 为零，另外两项正是 RU.17 的反号，故
\[
\boxed{\frac d{dt}\mathcal E_z+\|\nabla z\|_2^2=-\mathcal J.}
\tag{RU.19}
\]
h 与 z 的 Fourier 支撑不交，梯度也正交，所以两式相加恢复完整 NS 能量恒等式，不丢失外场耗散。

对任意实际存在的 [s,t]，准确积分账为
\[
\begin{aligned}
\mathcal E_h(t)-\mathcal E_h(s)+\int_s^t122\mathcal E_h(r)\,dr
&=\int_s^t\mathcal J(r)\,dr,\\
\mathcal E_z(t)-\mathcal E_z(s)+\int_s^t\|\nabla z(r)\|_2^2\,dr
&=-\int_s^t\mathcal J(r)\,dr.
\end{aligned}
\tag{RU.20}
\]
因此瞬时接收能量增长要求 \(\mathcal J>122\mathcal E_h\)；保持要求等号。这些是判据恒等式，不是已获有利传递。z 可储存此前生成的能量并回流，RU.19 不把这种可能性判为“全部由原始种子直接供给”。若 H=0，则能量式仍成立，不除以 H、能量或未知通量，也不因某一时刻能量导数为零排除随后出生。

旧来源结果已经给同一原解从 h(0)=0 到既定短窗内三对非零的有限出生；本文保留它。该事实与 RU.20 一致，且不等于任意时刻能量导数均为正，更不支付收到状态可重复使用。

## RU.5 要纳入的生成外场与目前的缺项

为区别实际 b 与仅由 h 内部生成的指定来源，在任意 [s,t] 定义
\[
b_s^{\rm int}(t)=\int_s^t e^{(t-r)\Delta}P_EB(h(r),h(r))\,dr.
\tag{RU.21}
\]
完整原解准确满足
\[
\begin{aligned}
b(t)&=e^{(t-s)\Delta}b(s)+b_s^{\rm int}(t)\\
&\quad+\int_s^t e^{(t-r)\Delta}P_E
\bigl[B(h,z)+B(z,h)+B(z,z)\bigr](r)\,dr.
\end{aligned}
\tag{RU.22}
\]
完整有序三项都保留。E 不交原初始 F，因而 b(0)=0；但“后来生成”不等于“由 h 单独生成”。实际 b 可以包含原始种子的直接激活、其它生成模作用以及此前 h 作用后的回流。不能把 b 替换为 \(b_s^{\rm int}\)，也不能清空 b(s)。

一个真正的再使用合同至少需要同时记录或控制：

- H 的两个完整复横向坐标及其相位/相干，不先限于首项线；
- 实际 b 的和型、差型两个复横向轨道，以及 RU.22 中其内部来源与其余来源的真实差；
- \(\Psi=P_DB(z,z)\) 的完整复强迫和相应外场残差，不仅是 b 的能量；
- 同一个经典时间段中足以控制 RU.17–20 有符号交换、耗散和下一输入状态的误差。

H、b 与 Ψ 足以写出当前时刻 H 的精确导数，但不能由此宣布它们组成闭合有限维动力系统。b 的方程还有完整交叉与外场项，Ψ 的后续演化也未付。要把它们当作可重复输入，必须对实际生成的联合状态给出可验证的持续资格；把“所需通量具有有利符号”直接列为假设不能支付这一点。

即使以后支付了返回同一 D 的反馈，它仍停留在同一频率集合与同一长度 \(\sqrt{61}\)，没有频率增大；这种返回本身不能当作跨尺度再生。跨尺度的下一输入还需另有对象与资格，本文没有提供。

**本次选择：NO-CANDIDATE，限于现在没有足够证据启动新的系数计算。** 可审议的下一输入对象是同一解的联合复状态 \((h,b)\) 连同 RU.13、RU.22 的真实残差控制；目前尚没有已核的联合状态返回域、来源分离或有利能量传递，不能仅凭形式接口选一棵新树、提高到某个高叶阶或再延长旧短窗。这个停止点是缺失输入，不是对所有外部协助或再生方式的普遍排除。

## RU.6 复用范围、实读与停稿

RU.1 的对称来自旧 C₃ 原材料，RU.5 来自旧二和支持桥，完整方程/压力/唯一性来自 GS 的原解入口。能量消项是对这些完整输入作周期分部积分得到的具体账目。因此本文把它们整理为可复用状态接口，不另计新的通用对称、能量或支持定理。

本次对以下科学稿定向搜索“能量/energy、交叉、回流、复横向状态、投影演化”，并进一步搜索 B(z,h)、B(h,z) 的明确字符串：support-invariance/INDEPENDENT，cyclic-six-carrier/PROOF，cyclic-six-carrier-preflight/PREFLIGHT，cyclic-receiver-supply-preflight/PREFLIGHT，return-interface/INDEPENDENT_INTERFACE，GENERAL_SOURCE_BRIDGE，以及本人刚停定的 receiver-input-geometry/PREFLIGHT、receiver-lattice-return/PREFLIGHT。已有返回接口与前项几何稿早已要求保留全部交叉/回流，未将这些要求当作本次发现。检索不是对未读全篇的接纳，未命中也不证明外部文献或全树没有等价公式。

| 来源（相对 research/reverse/） | 本次实际阅读 | SHA-256 |
|---|---|---|
| received-state-reuse/QUESTION.md | 全文；根对称/支持提示及禁止预设有利传递的范围 | 88e5af500d2d07928695653e12db9ac456bdc9d9489587561aad70ed9821f067 |
| cyclic-six-carrier/PROOF.md | 全文复读，CT.1–2 原数据及 CT.3–5 有限来源边界；不以形成时 pending 标头重置已完成接纳 | afd6b0009d7b357dd9ed6c9feaeb8dbb15535a5499dbd8be7911883e3c4f2725 |
| cyclic-six-carrier-preflight/PREFLIGHT.md | 第 1–125 行，CS.1–9 完整对称/固定 D；本作者此前全文读 | 39cabe5efa8e32f7475bd9974bc91bfa38a0db16cfb7b3c4c87cd91977a8437f |
| cyclic-receiver-supply-preflight/PREFLIGHT.md | 第 1–85 行，RS.1–6 固定频率、完整二和与零支；本作者此前全文读 | 841cc7e26a4d8b8c3e8f930e2a2da47824fdcba43cee1fd37e40864a32cf5b58 |
| four-leaf-preflight/GENERAL_SOURCE_BRIDGE.md | 第 1–195 行，GS.1–16 与下一段开头，完整算子、原解、压力、唯一性；不新增存在时间 | 59354781b8d04087cf1d5383824dbe741d24b3c0fae8798caa6c50cae24a3ebe |

其它命中仅作上述关键词定位；本人旧稿的形成身份不被写成此次外部原文全文阅读。只写本文件，未读新根稿或未知系数，未选择新初值、幅度、根或时间；没有科学程序运行、导入、编译、参数扫描、树求值、矩阵执行、Git 或外发。全文自读后另报最终 SHA 并停改，非作者审查另行安排。NOT CLAY。
