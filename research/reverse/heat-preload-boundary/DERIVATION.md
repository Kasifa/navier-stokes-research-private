# 固定初值的热尾比例、相对误差与完整 NS 通量

2026-09-07。PRIVATE_CORE。自包含的有界解析推导与已有结论接口，不主张新颖性，不选择新初值候选，不作模拟或有限截断证书。

结论：同一个非零光滑初值即使含无限 Fourier 模式，其纯热场的固定高频尾能量比例仍不增。两时刻真实 NS 相对该热场的全场 \(L^2\) 误差若分别不超过 \(\varepsilon_1,\varepsilon_2<1\)，其尾比例增量至多为两误差之和，扣除已知的热场比例下降量。单时刻的通用误差常数可以严格取 1，且在一般正交投影问题中不可改小。完整 NS 自身没有这个热单调性。

保留热场接收带本身的能量比例还能得到更细的角距离界：若热场该带全空，相对误差 \(\varepsilon\) 只允许真实场该带比例至多 \(\varepsilon^2\)。相应的全时高频尾上界也由粗界 \(\varepsilon_0\) 收紧为 \(\varepsilon_0^2\)，仍不构成奇性排除。

## 1. 对象、无限和及零时刻

固定 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\)、\(\nu>0\)、一个非零光滑实值无散初值 \(a\)，及一次固定的 \(K>0\)。允许 \(a\) 有无限 Fourier 支撑；本推导不额外要求零均值。设
\[
h(t)=e^{\nu t\Delta}a,\qquad Q_K=\mathbf1_{\{|k|\ge K\}}(D),\qquad
p_K(f)=\frac{\|Q_Kf\|_2^2}{\|f\|_2^2}\quad(f\ne0).
\]
\(Q_K\) 是正交投影，不是环形光滑乘子。记
\[
b_k=|\widehat a(k)|^2,\quad \lambda_k=|k|^2,
\quad A=\{k:|k|\ge K\},\quad A^c=\{k:|k|<K\},
\]
\[
S(t)=\sum_k b_ke^{-2\nu\lambda_kt},\qquad
S_A(t)=\sum_{k\in A}b_ke^{-2\nu\lambda_kt}.
\tag{H.1}
\]
Parseval 的体积因子在比值中消去，故 \(p_K(h(t))=S_A(t)/S(t)\)。

光滑性给出对任意整数 \(m\ge0\)，
\[
\sum_k(1+\lambda_k)^m b_k<\infty.
\]
所以 H.1 及其第 \(m\) 阶时间导数的绝对值分别受 \(\sum_k(2\nu\lambda_k)^m b_k\) 控制。对每个有限 \([0,T]\)，可由支配收敛逐项求导，各阶右导数连续到 \(t=0\)。这处理的是实际无限和，不是先假定有限模态。

选任一 \(b_{k_*}>0\)。在 \([0,T]\) 上有
\[
S(t)\ge b_{k_*}e^{-2\nu\lambda_{k_*}T}>0.
\]
因此上述商及其导数在有限时间都定义良好，热场不会在有限时刻成为零场。

## 2. 热尾比例的精确协方差公式

令 \(\mu_k(t)=b_ke^{-2\nu\lambda_kt}/S(t)\)。它是在同一固定谱上的概率分布，且 \(\sum_k\lambda_k\mu_k(t)<\infty\)。直接求导得
\[
\frac d{dt}p_K(h(t))
=-2\nu\left[\sum_{k\in A}\lambda_k\mu_k
-\left(\sum_{k\in A}\mu_k\right)\left(\sum_k\lambda_k\mu_k\right)\right].
\tag{H.2}
\]
括号可以严格写成
\[
C_h(t):=\sum_{i\in A}\sum_{j\in A^c}
\mu_i(t)\mu_j(t)(\lambda_i-\lambda_j)\ge0.
\tag{H.3}
\]
为说明重排合法，完整双和的绝对值受
\[
\sum_{i,j}\mu_i\mu_j(\lambda_i+\lambda_j)
=2\sum_k\lambda_k\mu_k<\infty
\]
控制；高–高部分可交换求和并因反对称性抵消。余下 H.3 的每项非负，因为高尾内 \(\lambda_i\ge K^2\)，低尾内 \(\lambda_j<K^2\)。也可直接对这部分使用 Tonelli 定理。

所以
\[
\boxed{\frac d{dt}p_K(h(t))=-2\nu C_h(t)\le0.}
\tag{H.4}
\]
若初始高尾和低尾都具有正能量，则某个 H.3 项在每个有限 \(t\) 都严格为正，比例严格下降。若初始高尾为空或低尾为空，则比例分别恒为 0 或 1。零模属于低尾，这不造成例外。

对任意有限 \(0\le t_1<t_2\)，定义可解析表示的热下降量
\[
D_h(t_1,t_2):=p_K(h(t_1))-p_K(h(t_2))
=2\nu\int_{t_1}^{t_2}C_h(t)\,dt\ge0.
\tag{H.5}
\]
这没有给未计算的无限谱总和一个数值证书。所有时间、所有谱项始终使用同一个 \(a\) 和同一个阈值 \(K\)。改换阈值、移动频带或逐时重新归一化某一叶，不是 H.4 的结论。

## 3. 正交投影比例的 sharp 相对误差界

下面在实 Hilbert 空间证明一个独立几何事实，可直接用于实值速度的 \(L^2\)。设 \(Q\) 为正交投影，\(h\ne0\)，且
\[
\|u-h\|\le\varepsilon\|h\|,\qquad 0\le\varepsilon<1.
\tag{H.6}
\]
则 \(u\ne0\)，并有
\[
\boxed{\left|\frac{\|Qu\|^2}{\|u\|^2}
-\frac{\|Qh\|^2}{\|h\|^2}\right|\le\varepsilon.}
\tag{H.7}
\]

**第一步：夹角受控。** 写 \(x=h/\|h\|\)、\(y=u/\|u\|\)、\(\rho=\|u\|/\|h\|\)。由 H.6，
\[
\langle x,\rho y\rangle\ge1-\varepsilon>0.
\]
故 \(c:=\langle x,y\rangle>0\)。又有
\[
\varepsilon^2\ge\|x-\rho y\|^2
=(\rho-c)^2+1-c^2\ge1-c^2.
\tag{H.8}
\]
记 \(s=\sqrt{1-c^2}\)，则 \(s\le\varepsilon\)。

**第二步：投影比例差不超过夹角的正弦。** 若 \(c=1\)，两比例相等。否则定义正交单位向量
\[
e=\frac{x+y}{\sqrt{2+2c}},\qquad
f=\frac{y-x}{\sqrt{2-2c}}.
\]
写 \(x=\alpha e-\beta f\)、\(y=\alpha e+\beta f\)，其中
\(\alpha=\sqrt{(1+c)/2}\)、\(\beta=\sqrt{(1-c)/2}\)。于是
\[
\langle y,Qy\rangle-\langle x,Qx\rangle
=4\alpha\beta\langle e,Qf\rangle
=2s\langle e,Qf\rangle.
\]
单位向量 \((e+f)/\sqrt2\)、\((e-f)/\sqrt2\) 的投影范数平方都在 \([0,1]\)，两者之差为 \(2\langle e,Qf\rangle\)。因此
\[
2|\langle e,Qf\rangle|\le1,
\]
与 H.8 合并即得 H.7。证明同时控制了变化的全场能量分母，没有把它冻结为热场分母。

**保留接收带比例的精细角距离界。** 令
\[
p_h=\|Qx\|^2,\quad p_u=\|Qy\|^2,\quad
\alpha_x=\arcsin\sqrt{p_h},\quad
\alpha_y=\arcsin\sqrt{p_u}.
\]
这两个角均在 \([0,\pi/2]\)。在 \(Q\) 与 \(I-Q\) 的正交分解中分别使用 Cauchy–Schwarz，有
\[
\begin{aligned}
c=\langle x,y\rangle
&=\langle Qx,Qy\rangle+\langle(I-Q)x,(I-Q)y\rangle\\
&\le\sqrt{p_hp_u}+\sqrt{(1-p_h)(1-p_u)}\\
&=\cos(\alpha_y-\alpha_x).
\end{aligned}
\]
因为 \(c>0\)，实际夹角 \(\vartheta=\arccos c\) 属于 \([0,\pi/2)\)。H.8 给 \(\sin\vartheta\le\varepsilon\)，而上式及 \(|\alpha_y-\alpha_x|\le\pi/2\) 给
\[
\boxed{\left|\arcsin\sqrt{p_u}-\arcsin\sqrt{p_h}\right|
\le\vartheta\le\arcsin\varepsilon.}
\tag{H.7a}
\]
因此，若记连续非减函数
\[
F_\varepsilon(p):=
\sin^2\!\left(\min\!\left\{\frac\pi2,
\arcsin\sqrt p+\arcsin\varepsilon\right\}\right),
\quad 0\le p\le1,
\]
就有
\[
\sin^2\!\left(\max\!\left\{0,
\arcsin\sqrt{p_h}-\arcsin\varepsilon\right\}\right)
\le p_u\le F_\varepsilon(p_h).
\tag{H.7b}
\]
特别地，\(F_\varepsilon(0)=\varepsilon^2\)，故
\[
Qh=0\quad\Longrightarrow\quad p_Q(u)\le\varepsilon^2.
\tag{H.7c}
\]
这保留了接收带原有能量信息；H.7 的统一常数 1 仍然正确，两种表述不能混同为同初值 NS 类中的最优性主张。

**常数不能普遍改小。** 对任意 \(0<\varepsilon<1\)，在 \(\mathbb R^2\) 上取投影 \(Q(z_1,z_2)=(0,z_2)\)，令
\[
\theta=\arcsin\varepsilon,\quad \varphi=\frac\pi4-\frac\theta2,
\quad h=(\cos\varphi,\sin\varphi),
\]
\[
y=(\cos(\varphi+\theta),\sin(\varphi+\theta)),\qquad u=\cos\theta\,y.
\]
直接手算得到
\[
\|u-h\|=\varepsilon\|h\|=\varepsilon,
\qquad p_Q(u)-p_Q(h)
=\sin(2\varphi+\theta)\sin\theta=\varepsilon.
\]
这个等号例只证明一般 Hilbert 正交投影误差常数的最优性，不称它来自同一个 NS 解，也不提出新的速度候选。若投影在所限空间上恒为 0 或恒等映射，比例当然无误差。

## 4. 同一真实 NS 解的两时刻条件上界

设同一允许初值 \(a\) 的光滑 NS 解 \(u\) 在两个观测时刻满足实际支付的误差条件
\[
\|u(t_i)-h(t_i)\|_2\le\varepsilon_i\|h(t_i)\|_2,
\quad 0\le\varepsilon_i<1,\quad i=1,2.
\tag{H.9}
\]
逐个使用 H.7，再用 H.5，可得
\[
\boxed{p_K(u(t_2))-p_K(u(t_1))
\le\varepsilon_1+\varepsilon_2-D_h(t_1,t_2)
\le\varepsilon_1+\varepsilon_2.}
\tag{H.10}
\]
还可与比例范围给出的上界 1 取最小值。若已证明
\(D_h>\varepsilon_1+\varepsilon_2\)，则两时刻的真实 NS 比例也必须严格下降。反之，一个增量 \(\gamma>0\) 至少要求
\[
\varepsilon_1+\varepsilon_2\ge\gamma+D_h
\]
才能与 H.9 同时成立。\(t_1=0\) 时，因为 \(u(0)=h(0)=a\)，可取 \(\varepsilon_1=0\)。

这些都是条件结论。目标场重标后的 \(H^r\) 小误差、拓扑稳定邻域或一个未量化的“近似热演化”，均不能自动支付 H.9 的相对**全场** \(L^2\) 误差。常数 1 的 sharp 性也只属于 H.7，未声称 H.10 在同初值 NS 轨道类内达到等号。

## 5. 完整 NS 的比例方程

采用与既有来源分解一致的有序双线性符号
\[
B(f,g)=-\mathbb P[(f\cdot\nabla)g],\qquad
u_t=\nu\Delta u+B(u,u).
\]
\(\mathbb P\) 为完整周期 Leray 投影。记
\[
E=\|u\|_2^2,\quad E_K=\|Q_Ku\|_2^2,\quad
Z=\|\nabla u\|_2^2,\quad Z_K=\|\nabla Q_Ku\|_2^2,
\]
\[
\Phi=\langle Q_Ku,Q_KB(u,u)\rangle_{L^2},\qquad p=E_K/E.
\]
在 \(E>0\) 的光滑时段，周期分部积分、无散性及投影自伴性给
\[
\langle u,B(u,u)\rangle=0,\qquad
E'=-2\nu Z,\qquad E_K'=2\Phi-2\nu Z_K.
\]
故
\[
\boxed{p'=\frac{2\Phi}{E}
-2\nu\left[\frac{Z_K}{E}-p\frac ZE\right].}
\tag{H.11}
\]
傅里叶投影有界且与空间导数交换，光滑性足以支持这里的全频运算。若使用 H.9 的两个观测时刻，\(E(t_2)>0\)，而 NS 能量不增，故整个 \([t_1,t_2]\) 都有 \(E(t)\ge E(t_2)>0\)。

对任意当时速度 \(u\)，同 H.3 的高–低双和证明
\[
C_u:=\frac{Z_K}{E}-p\frac ZE\ge0.
\tag{H.12}
\]
因此固定高频尾的黏性协方差项始终非正，但 \(\Phi\) 没有固定符号。只要某实际时刻 \(\Phi>\nu E C_u\)，就有 \(p'>0\)。在整个窗口上精确地
\[
p(t_2)-p(t_1)=2\int_{t_1}^{t_2}\frac{\Phi(t)}{E(t)}\,dt
-2\nu\int_{t_1}^{t_2}C_u(t)\,dt.
\tag{H.13}
\]
正增量需要非线性补偿黏性协方差，但本公式未把 \(\Phi\) 标为纯第一代供给。

“真实 NS 可出现比例上升”也与本树既有 FA 结果直接相容，无需在本轮构造新初值。FA.4 的初始支撑在 \(N\le|k|\le2N\)，其光滑目标乘子支撑在 \(2.05N<|k|<2.2N\)，且后来目标能量严格为正。固定其中一个已存在的 \(N\) 及其同一条解，取一次固定阈值 \(K=2.05N\)，则正交尾比例从 0 变为正，因而光滑性和中值定理保证某时刻 \(p'_K>0\)。这里是对既有有限激活的引用；没有把不同 \(N\) 的初值族拼成一条无限轨道，也没有混同 FA 光滑乘子与本投影：只用了前者的支撑包含在后者尾内。

## 6. 供给与量词边界

H.4 排除的是同一固定热初值通过纯热衰减提高固定阈值高尾的相对能量；它允许热场总能量和各项均衰减，并允许预置的低频项后来占主导。无限初始支撑已在 H.1–3 中处理，不留下“任意有限谱都成立、但无限谱未核”的缺口。

还可以把这一点写成对全部热演化时间一致的谱尾结论。因为 \(a\in L^2\) 且 \(a\ne0\)，
\[
\sup_{t\ge0}p_K(h(t))=p_K(a)
=\frac{\sum_{|k|\ge K}|\widehat a(k)|^2}{\sum_k|\widehat a(k)|^2}
\longrightarrow0\quad(K\to\infty).
\tag{H.14}
\]
等号使用了允许 \(t=0\)，极限由初始绝对可和的谱能量尾给出。换言之，对每个固定 \(\rho>0\)，存在依赖该同一 \(a,\rho\) 的 \(K_\rho\)，使所有 \(K\ge K_\rho\) 和所有 \(t\ge0\) 都有 \(p_K(h(t))<\rho\)。即使可以为每个 \(K\) 分别挑观测时刻，纯热预置仍不能通过任意高频处固定正能量占比的合同。这是一致谱尾紧性，不要求初值只有有限模式。

若同一 NS 解在其实际光滑存在时间集合 \(I=[0,T_*)\)（\(T_*\) 可有限或无限）上另已证明
\[
\|u(t)-h(t)\|_2\le\varepsilon_0\|h(t)\|_2
\quad\text{对全部 }t\in I,\qquad 0\le\varepsilon_0<1,
\]
H.7 给出的粗界 \(p_K(a)+\varepsilon_0\) 可以用 H.7b 收紧。由 \(F_{\varepsilon_0}\) 非减及 H.14，
\[
\sup_{t\in I}p_K(u(t))\le F_{\varepsilon_0}(p_K(a)),
\qquad
\limsup_{K\to\infty}\sup_{t\in I}p_K(u(t))\le\varepsilon_0^2.
\tag{H.15}
\]
最后一步使用 \(F_{\varepsilon_0}\) 在 0 处连续且 \(F_{\varepsilon_0}(0)=\varepsilon_0^2\)。这是此前 \(\varepsilon_0\) 上界的收窄，不是更换误差假设。当 \(\varepsilon_0>0\) 时，本推导没有把右端继续降为 0，也没有证明 \(\varepsilon_0^2\) 在同初值 NS 全时轨道类内最优。不能把两个时刻的误差假设升级为此全时假设。即使热场满足 H.14，或某 NS 场族的未加权尾能量趋零，这也没有给高导数的频率加权谱和统一上界。因此 H.14–15 不排除携带趋零 \(L^2\) 能量却有高导数增长的集中，更不能据此排除奇性。

H.10 只在相对全场误差已付时转移成 NS 的条件约束。H.11–13 的 \(\Phi\) 是完整当前速度的二次作用，含初始热种子、全部历史及其混合反馈；不能从其正性推得截止某时刻历史的自作用占优。实际归因仍须使用 `reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md` 的固定热参照与有序来源分解，并支付其中的场范数、直接种子项和余项预算。

本推导不声称一般 NS 的高尾比例单调，也不声称所有奇性必须满足某个预设的两时刻比例增量。这里没有通过筛选的新机制、经数值认证的 \(\varepsilon_i\)、跨代统一性或有限总时间结论。

## 7. 输入绑定与证据性质

本文件的无限和推导、Hilbert 界及其等号例均为独立解析/手算证明，没有数值计算或扫描。

| 文件（相对工作树根目录） | 实读定位 | SHA-256 |
| --- | --- | --- |
| `research/reverse/heat-preload-boundary/CONTRACT.md` | 全文 | `9d78b048092b9b6af2dfa8ba44896bec39a5c9145aa1a28373c96bffb6377784` |
| `research/reverse/reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md` | 全文，特别是有序来源分解及其适用边界 | `d22bcca237977647b54ebbe13288c63a24a7c610a52a7c2265f4e3cfe366607a` |
| `research/clay_b_frequency_activation_20260907.md` | 本轮复读 FA.2–4、FA.15；FA.7–14 已于前轮实读 | `42bbc2ba3abae7aa1eeb25ee0b29f896d7d8ddcafccb0da518dded4851dd897a` |
