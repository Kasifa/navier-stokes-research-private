# 固定接收场一次内部供给的输入几何预筛

2026-09-09，PRIVATE_CORE。**固定集合结论：Λ 内任意三个非零频率的最大两两绝对余弦至少为 1/2；这个下界能由秩三的频率组达到。因此，同一 D 上实际 h 的热延续加一次完整内部二次供给，不能同时向满足严格近正交条件的三个频率对提供非零来源。** 这是 QUESTION 所指定对象的手工支持与几何推论，不是实际幅度计算、一般再生排除或奇性结果。

作者 coherence_independent_resumed 曾写六载波结构预筛、A/B 源码与记录、接收二和支持桥、差型独立分析和主核。根在本问之前披露了等长、等互点积及 1/2 可能可达的手算预见；本文独立重推新增 Gram 细节与下述完整范围，不称全课题盲推导。未读取根在本目录的其它推导。本文独立建档，不加入仍在收尾的差型证书包，也不据该包并行状态作数学接纳。

## RG.1 同一真实来源与旧支持桥

在 QUESTION 固定的 ν=1、无外力标准 2π 三维环面上，令 u 为原六载波初值 a_* 的同一完整 NS 经典解。在任何实际存在的闭经典区间 [s,t] 上令
\[
h(r)=P_Du(r),\qquad
D=\{\pm k_0,\pm k_1,\pm k_2\},
\]
\[
k_0=(3,4,6),\quad k_1=(6,3,4),\quad k_2=(4,6,3).
\tag{RG.1}
\]
下述来源保持问题原定义：
\[
C_s(t)=e^{(t-s)\Delta}h(s)
+\int_s^t e^{(t-r)\Delta}B(h(r),h(r))\,dr.
\tag{RG.2}
\]
C_s 是同一原解中指定来源的和，不另解一个有限维或闭合 NS 系统。完整 u 不被假设有限支撑；h 之所以支撑在 D，仅因为它是固定投影。下文 \(\|f\|_{A0}=\sum_k|\widehat f(k)|_2\)，复向量使用 Hermitian 欧氏范数，每个频率对的正、负模各计一次，不重复计对。

已有支持桥 RS.3–4 对全部 D 有序二和给：零频和 ±2k_i 的自作用逐项为零，其余只可能在和型与差型。这里再次核所需理由，保留完整
\[
\widehat{B(f,g)}(m)
=-i\mathbb P_m\sum_{a+b=m}(\widehat f(a)\cdot b)\widehat g(b),
\quad
\mathbb P_m=I-\frac{m\otimes m}{|m|^2}\quad(m\ne0).
\tag{RG.3}
\]
三个 k_i 独立，所以 2k_i 只有有序输入 (k_i,k_i)，其中 \(\widehat h(k_i)\cdot k_i=0\)；负倍频同理。零频的每个输入 (a,−a) 也各由横向性为零，不在零向量上定义或除以 Leray 分母。非同频交叉作用仍含两个不同有序项，本文不将它们未经核验地乘二。

为写 Gram 方便，取
\[
\sigma_i=k_{i+1}+k_{i+2},\qquad
q_i=k_i-k_{i+1}\quad(i\bmod3),
\]
\[
\Lambda=\{\pm k_i,\pm\sigma_i,\pm q_i:i=0,1,2\}.
\tag{RG.4}
\]
热半群不改变 Fourier 支撑；完整 Leray 只作用同一个输出频率。因此在任意上述 [s,t] 上，包含端点，
\[
\boxed{\operatorname{supp}\widehat{C_s(t)}\subset\Lambda.}
\tag{RG.5}
\]
实际相位相消或某个系数为零只能缩小这个集合，不能产生集合外频率。

RS.6、RS.11 还已给差型最少初始叶数 2、和型最少初始叶数 7；那些是初始支持叶词结果，不是本次实际内部供给的非零证据。本稿不重算这些系数，也不把叶词下界当作未知系数的零判。

## RG.2 精确九线 Gram

直接由固定坐标手核
\[
|k_i|^2=3^2+4^2+6^2=61,\qquad
k_i\cdot k_j=3\cdot6+4\cdot3+6\cdot4=54\quad(i\ne j).
\tag{RG.6}
\]
因此对任意实系数 x_i、y_i，有完整身份
\[
\left(\sum_i x_i k_i\right)\cdot\left(\sum_i y_i k_i\right)
=7\sum_i x_i y_i+54\left(\sum_i x_i\right)\left(\sum_i y_i\right).
\tag{RG.7}
\]
右侧在 x=y≠0 时严格为正，亦重新证明三个 k_i 独立。以下九个代表全非零、无相互共线；其整体正负给 Λ 的 18 个不同频率：

| 类型 | 三个代表（依下标 0,1,2） | 平方长度 |
|---|---|---|
| 原接收 | (3,4,6)，(6,3,4)，(4,6,3) | 61 |
| 和型 σ | (10,9,7)，(7,10,9)，(9,7,10) | 230 |
| 差型 q | (−3,1,2)，(2,−3,1)，(1,2,−3) | 14 |

无重复或额外共线可在独立 k 基下直接检查：三类系数分别为 e_i、\(\mathbf1-e_i\)、\(e_i-e_{i+1}\)，不同列除整体负号外不成比例。原接收、正和型的坐标和分别为 13、26；差型的坐标和为 0。

令 I 为 3×3 单位矩阵，J 为 3×3 全一矩阵，并令
\[
H=\begin{pmatrix}1&0&-1\\-1&1&0\\0&-1&1\end{pmatrix}.
\]
按照列序 \((k_0,k_1,k_2;\sigma_0,\sigma_1,\sigma_2;q_0,q_1,q_2)\)，完整 9×9 Gram 为
\[
\boxed{
\begin{pmatrix}
7I+54J&115J-7I&7H\\
115J-7I&7I+223J&-7H\\
7H^{\mathsf T}&-7H^{\mathsf T}&21I-7J
\end{pmatrix}.}
\tag{RG.8}
\]
这是手推的数学矩阵，未执行矩阵程序或数值数组。为使每个块可复核，RG.7 分别给
\[
\begin{aligned}
k_i\cdot\sigma_i&=2\cdot54=108,&
k_i\cdot\sigma_j&=61+54=115\quad(i\ne j),\\
\sigma_i\cdot\sigma_j&=61+3\cdot54=223\quad(i\ne j),&
|\sigma_i|^2&=2(61+54)=230,\\
|q_i|^2&=2(61-54)=14,&
q_i\cdot q_j&=-(61-54)=-7\quad(i\ne j),\\
k_i\cdot q_j&=7(\delta_{ij}-\delta_{i,j+1}),&
\sigma_i\cdot q_j&=-k_i\cdot q_j.
\end{aligned}
\tag{RG.9}
\]
最后一个身份因 \((k_0+k_1+k_2)\cdot q_j=0\) 成立。任意有符号代表的 Gram 项只需乘对应两个符号；绝对余弦不变。

## RG.3 阈值 1/2 的必要性与几何尖锐性

以频率的无向直线为单位，将九条线分为
\[
\mathcal A=\{\mathbb R k_i,\mathbb R\sigma_i\},
\qquad
\mathcal Q=\{\mathbb R q_i\}.
\]
不同线之间的全部绝对余弦由 RG.8 给出：

| 两线类型 | 绝对余弦 | 与 1/2 比较 |
|---|---|---|
| k_i,k_j，i≠j | 54/61 | 严格大于 |
| σ_i,σ_j，i≠j | 223/230 | 严格大于 |
| k_i,σ_j | 108/√(61·230) 或 115/√(61·230) | 两者严格大于 |
| q_i,q_j，i≠j | 1/2 | 相等 |
| k_i,q_j | 0 或 7/√(61·14) | 严格小于 |
| σ_i,q_j | 0 或 7/√(230·14) | 严格小于 |

混合原/和型中较小者仍大于 1/2，因为 \(4\cdot108^2>61\cdot230\)。两个非零跨类值的平方分别为 7/122、7/460，均小于 1/4。各分母严格正，平方比较不改变结论。

任取 Λ 内三个非零频率。若有两个频率重复、互为相反数或共线，该对绝对余弦为 1。否则得到三条不同线：若至少两条属于 \(\mathcal A\)，该对严格大于 1/2；若至多一条属于 \(\mathcal A\)，则至少两条属于 \(\mathcal Q\)，该对恰为 1/2。因此
\[
\boxed{
\max_{i\ne j}\frac{|m_i\cdot m_j|}{|m_i||m_j|}\ge\frac12
\quad(m_1,m_2,m_3\in\Lambda).
}
\tag{RG.10}
\]
整个有符号集合均已覆盖，不通过选择符号避开这个绝对值门。

下界可在本固定集合中达到。三个差型 q₀、q₁、q₂ 彼此的绝对余弦均为 1/2，但其和为零，只有秩二。另一个达到方式为固定集合的成员
\[
(k_0,q_0,q_1).
\tag{RG.11}
\]
q₀、q₁ 不共线，张成坐标和为零的平面；k₀ 的坐标和为 13，故 RG.11 为秩三。其两条跨类绝对余弦分别为 \(7/\sqrt{61\cdot14}\) 与 0，而差型之间为 1/2，所以最大值仍恰为 1/2。

更准确地，三条不同无向线满足最大值≤1/2，当且仅当至少两条是差型且至多一条属于 \(\mathcal A\)。其中三差型给秩二，一条 \(\mathcal A\) 加两条差型给秩三。这个分类只依据 RG.8，且只属于 Λ。

所以 1/2 是本集合的准确几何阈值：要求严格小于 1/2 时没有三线；改成≤1/2 时有秩三几何组；若把严格阈值提高到任何大于 1/2 的数，也有几何组。所有达到者仅是原集合中的整数频率资格，没有新增载波、初值、参数或时间选择，更没有认证这些位置的 C_s 系数同时非零。

## RG.4 对逐对来源门的实际后果

任意目标三频率 \(m_1,m_2,m_3\in\mathbb Z^3\setminus\{0\}\) 若满足 QUESTION 的严格条件
\[
\max_{i\ne j}\frac{|m_i\cdot m_j|}{|m_i||m_j|}<\frac12,
\tag{RG.12}
\]
则由 RG.10 至少有一个 \(m_j\notin\Lambda\)。Λ 对整体负号闭合，故对该频率对 \(E_j=\{\pm m_j\}\)，在每个实际存在的 [s,t] 上有
\[
P_{E_j}C_s(t)=0.
\tag{RG.13}
\]
令真正其它来源为 \(R_s(t)=u(t)-C_s(t)\)。于是该对 \(P_{E_j}R_s(t)=P_{E_j}u(t)\)。若实际目标非零，则其它来源非零而指定来源为零；不定义零分母比值，但等价的乘式门
\[
\|P_{E_j}R_s(t)\|_{A0}
\le\tfrac14\|P_{E_j}C_s(t)\|_{A0},
\qquad \|P_{E_j}u(t)\|_{A0}>0
\tag{RG.14}
\]
不可能成立。若实际目标也为零，则 RG.14 的非零目标要求已经失败。故三个目标对不能同时通过逐对门；本结论不需要估计 h 的增益、幅度或相位。

完整其它来源没有被省略。令 \(z(r)=u(r)-h(r)\)，实际 NS 的 Duhamel 恒等式准确给
\[
\begin{aligned}
R_s(t)
&=e^{(t-s)\Delta}[u(s)-h(s)]\\
&\quad+\int_s^t e^{(t-r)\Delta}
\bigl[B(h,z)+B(z,h)+B(z,z)\bigr](r)\,dr.
\end{aligned}
\tag{RG.15}
\]
两个交叉项有序且不同，z 包含全部其它真实频率、旧目标和回流。保留 ν=1 的完整热传播与 Leray；没有把 u(s) 重置或清空，也没有由 C_s 支撑有限推定完整 u 支撑有限。

原模板的三条轴向低频线绝对余弦均为零，因而满足 RG.12。共同正交旋转及非零共同缩放保留这些绝对余弦；相位平移不改变频率。当变换后的频率仍是当前环面上的非零整数频率时，RG.13–14 对这些目标也适用。这里没有声称任意实旋转、缩放都保持整数格或原 NS 问题。

s=t 时 RG.2 的积分为零、C_s(s)=h(s)，支持结论继续成立；若 h(s)=0 或整个来源为零，也不对零来源作比值。结论只要求所讨论 [s,t] 确实位于原经典分支，不宣称经典解存在到任意给定晚时间。

## RG.5 历史去重与准确停止点

本次全文复读的接收二和支持桥 RS.3–4 已完整覆盖 RG.5 的输出上集；它还覆盖最短叶数和倍频零门。这些不是本次新增发现。六载波原证明 CT.1–2 和结构预筛 CS.1–2 已给实际初值、循环轴种子、D、秩三及完整原解边界；本文不重开循环完成或四叶来源证明。

本次实际核过的上述文本没有给 Λ 的九线 Gram、严格近正交门和尖锐 1/2 分类。旧 return-interface 合同研究 FA 的两中心极化/下一输入资格，并明确有限包宽与中心极限不能互换；其对象不是当前离散 Λ。本稿不抹除它已提出的返回问题，也不将本集合结论套在 FA 的全部带宽上。

定向文字去重有两层，均未读取任务/发布状态：

1. 在 cyclic-six-carrier、cyclic-six-carrier-preflight、cyclic-receiver-supply-preflight、four-leaf-preflight、strategy-20260908、support-invariance 的 Markdown 中检索“近正交、near-orthogonal/near orthogonal、等互点积、Gram 与 61 的相邻文字、223/230、54/61”，没有命中。
2. 在 net-mixed-cancellation 的 CONTRACT/INDEPENDENT/STAR_TEMPLATE_CONTRACT，three-edge-compatibility 的 CONTRACT/INDEPENDENT，two-elliptic-compatibility 与 full-high-row-reduction 的 CONTRACT，return-interface 的 CONTRACT/INDEPENDENT_INTERFACE，以及 four-leaf-preflight/HISTORY_SCOPE 中检索“近正交、near-orthogonal/near orthogonal、223/230、54/61、cos 邻近 1/2、Gram”，没有命中。

这些搜索只登记实际定位范围，不等于逐份全文重读，更不证明全树或外部文献没有数学等价论证。本文将新增内容定位为**旧支持上集上的一个可单独审查的几何推论**，不宣称 C₃、Gram 方法或近正交思想的新颖性，不包装为独立的一般 NS no-go 定理。

当前已闭合的有限结论是 RG.5、RG.8–10 和逐对门障碍 RG.13–15。下列问题不由本稿支付：只要求总带来源占优、允许不同输入几何、允许真实外部协助、继续多次内部生成、实际允许输出的系数非零、输入极化/相位/幅度返回，以及跨尺度统一误差或无限迭代。总带门尤其不能由某一对零来源直接排除，因为当前几何没有给该对实际余来源占总带的任何固定正下界。

## RG.6 实际来源与停改

| 来源（相对 research/reverse/） | 本次实际阅读 | SHA-256 |
|---|---|---|
| receiver-input-geometry/QUESTION.md | 初稿全文及补明 A0/Hermitian/正负计数后的最终全文；对象、阈值不变，根预见已披露 | 5c5f92f0a134147f21ea88bdc6b567560820fcbe67cdfe3880ee0369c49a6e44 |
| cyclic-receiver-supply-preflight/PREFLIGHT.md | 全文复读；原作者，取 RS.1–6、11–13 的固定支持和准确边界 | 841cc7e26a4d8b8c3e8f930e2a2da47824fdcba43cee1fd37e40864a32cf5b58 |
| cyclic-six-carrier/PROOF.md | 全文复读；取 CT.1–2 固定对象，不以形成时 pending 标头重置后续状态 | afd6b0009d7b357dd9ed6c9feaeb8dbb15535a5499dbd8be7911883e3c4f2725 |
| cyclic-six-carrier-preflight/PREFLIGHT.md | 全文复读；取完整算子、循环、轴种子与 D；历史原文读记仅作该稿记录 | 39cabe5efa8e32f7475bd9974bc91bfa38a0db16cfb7b3c4c87cd91977a8437f |
| return-interface/CONTRACT.md | 全文复读；仅比较旧返回问题的对象，不重读 FA/R0 原文全证 | e647b416ef4c310b0b6501d8b49e01adfe1c866f8bd9e9dd937b87f24c3aaa3a |
| four-leaf-preflight/GENERAL_SOURCE_BRIDGE.md | 第 1–90 行，GS.1–7；取完整 Fourier–Leray/热定义和支持边界，不重新证明经典存在 | 59354781b8d04087cf1d5383824dbe741d24b3c0fae8798caa6c50cae24a3ebe |

只写本文件。未读新根稿、未知系数或新程序输出；未运行、导入、编译科学程序或数组，未求根、选参、选择新初值/频率/时间、扫描八叶或执行 Git/外发。本文的固定整数 Gram 身份全部手推。全文自读后另报最终 SHA 并停改，后续非作者审查与接纳由根另行安排；NOT CLAY。
