# 随机压力冲量：已付二阶矩与未付终端一致可积性

2026-09-08。SPI，私有内部核算；不是独立成果小节或发布冻结。
输入提交：`70e576ef61177596207aa060608477d4e9b09ca2`。
状态：经典随机表示的直接推论／限定终端识别；一般三维 NS 与 Clay 仍 OPEN、NOT CLAY。

压力冲量型全域涨落—耗散关系已有文献及本地 CG 记录，不是新发现。
本次把它放在同一个前向概率空间中，核清三个量：压力冲量有一致二阶矩；
随机补偿误差和黏性冲量有强 L2 终端迹；压力冲量自身的强 L2 迹仍未得到。
最后一项与原速度的强 L2 终端迹等价，不能用前两项替代。

## 1. 同一原解与同一个概率空间

固定 ν>0、无外力、三维周期光滑 NS 解，在 [0,T*) 光滑，T*<∞。
采用一个固定的零均值 Galilean 代表，不限制一般初值均值；压力取周期零均值。
固定 0<a<T*。记胞体积 V，⟨f⟩=V^(−1)∫f，G=∇u，
\[
 e(t)=\langle|u(t)|^2\rangle,\qquad
 \mathcal D(s,t)=\int_s^t\langle|G(r)|^2\rangle\,dr,
 \qquad e(t)+2\nu\mathcal D(s,t)=e(s).
 \tag{SPI.1}
\]
η 为均匀初始标签，独立于三维标准 Brownian 运动 W；使用前向 Itô 方程
\[
 dX_t=u(X_t,t)dt+\sqrt{2\nu}\,dW_t,\qquad X_a=\eta.
 \tag{SPI.2}
\]
在每个闭光滑前缀上求解，唯一性将这些解拼成同一个 [a,T*) 过程。
不预设终端 SDE、光滑逆流或形变矩阵有界。无散性与 Fokker–Planck 唯一性
使每个 X_t 都均匀；其未来 Brownian 增量独立于截至 t 的历史。
概率测度记为 ℙ。以下期望同时平均标签与噪声，不是固定终点 x 的逐点上界。

定义同一过程上的向量随机变量
\[
 I_t=\int_a^t\nabla p(X_r,r)dr,\quad
 Y_t=u(\eta,a)-I_t,\quad U_t=u(X_t,t),\quad Z_t=Y_t-U_t.
 \tag{SPI.3}
\]

## 2. 条件均值与压力冲量的二阶矩

令 m_i(t,x)dx=E[Y_{t,i}1_{X_t∈dx}]。对 Y_{t,i}φ(X_t) 用前向 Itô；
Y 为适应的有限变差过程，其与 φ(X_t) 的交叉变差为零。弱式给
\[
 \partial_t m+\operatorname{div}(um)-\nu\Delta m=-V^{-1}\nabla p,
 \qquad m(a)=V^{-1}u(a).
\]
u/V 满足同一线性方程。在每个闭光滑前缀，线性唯一性因此给
\[
 E[Y_t\mid X_t]=U_t,\qquad E[Z_t\mid X_t]=0.
 \tag{SPI.4}
\]
由原压力正交性，
\[
 \frac d{dt}E|Y_t|^2=-2E[Y_t\cdot\nabla p(X_t,t)]
 =-2\langle u\cdot\nabla p\rangle=0.
\]
于是
\[
 E|Y_t|^2=e(a),\qquad E|I_t|^2\le4e(a),\qquad
 E|Z_t|^2=e(a)-e(t)=2\nu\mathcal D(a,t).
 \tag{SPI.5}
\]
最后一步使用条件期望的正交分解和 SPI.1。也有准确交叉关系
E|I_t|²=2E[u(η,a)·I_t]，不是逐点的压力功消失。
这些是已有全域 FDR 的直接后果，不是较强的原 NS 临界估计。

## 3. 重启给增量，不需要把 Z 称为前向鞅

固定确定时刻 a≤s<t<T*。以均匀的 X_s 为标签、只用未来 Brownian 增量重启，
上述同一证明适用于 Y^{(s)}_t=u(X_s,s)−∫_s^t∇p(X_r,r)dr。
而 Y^{(s)}_t−U_t 恰等于 Z_t−Z_s，所以
\[
 E|Z_t-Z_s|^2=2\nu\mathcal D(s,t).
 \tag{SPI.6}
\]
有限总耗散使 Z_t 在固定概率空间中强 L2-Cauchy 至 T*。
这不是把原压力冲量 I_t 当成鞅，也未扩展到随机停止时刻。

前向 Itô 的实际符号为
\[
 dU_t=(2\nu\Delta u-\nabla p)(X_t,t)dt
       +\sqrt{2\nu}\,G(X_t,t)dW_t.
 \tag{SPI.7}
\]
尤其不能删掉 2νΔu。记 A_{s,t}=ν∫_s^tΔu(X_r,r)dr，
B_{s,t}=√(2ν)∫_s^tG(X_r,r)dW_r，则
\[
 Z_t-Z_s=-2A_{s,t}-B_{s,t},\qquad
 E|B_{s,t}|^2=2\nu\mathcal D(s,t),\qquad
 E|A_{s,t}|^2\le2\nu\mathcal D(s,t).
 \tag{SPI.8}
\]
末式由 4E|A|²≤2E|Z_t−Z_s|²+2E|B|² 得到，不假设两项独立。
因此 A_{a,t} 也有强 L2 终端迹。这是沿随机路径的有符号黏性冲量控制，
不是 ∫||Δu||₂dt 有界，更不是原速度的强 L2 迹。

## 4. 压力冲量只先得到较弱的强迹

周期压力满足 ∇p=−(I−P)(u·∇u)，P 为完整 Leray 投影。
零均值 Sobolev 与 1<3/2<∞ 的投影有界性给
\[
 \|\nabla p(t)\|_{L^{3/2}}\le C\|u(t)\|_6\|G(t)\|_2
 \le C\|G(t)\|_2^2.
\]
常数只依赖固定胞；转换成体积平均时仍记为 C。
均匀单时分布与 Minkowski 给
\[
 \|I_t-I_s\|_{L^{3/2}(\mathbb P)}\le C\mathcal D(s,t),\qquad
 \|U_t-U_s\|_{L^{3/2}(\mathbb P)}
 \le C\mathcal D(s,t)+\sqrt{2\nu\mathcal D(s,t)}.
 \tag{SPI.9}
\]
因此 I_t→I_* 强 L3/2；SPI.5 的一致 L2 上界再给 I_t⇀I_* 弱 L2。
这一步不升级成强 L2。Z_t 的强 L2 迹记作 Z_*。

## 5. 与原速度终端迹的准确对应

这里额外调用已经核对的本地结果：[LP.6](clay_b_leray_paid_budget_20260907.md)
给 ∫_a^{T*}||u||∞dt<∞；[TG.3](clay_b_strong_gradient_terminal_trace_20260908.md)
给 u(t)→u_* 强 L1、u_*∈L2。没有重新认证它们的全部外部依赖。

SPI.2 与上述总速度界、Brownian 连续性给 X_t→X_* 几乎处处；
X_* 仍均匀，因为每个 X_t 均匀。对任意 L2 函数 f，先用连续函数逼近 f，
再用两个均匀分布控制逼近误差，得到 f(X_t)→f(X_*) 强 L2。
特别地，u_*(X_t)→u_*(X_*) 强 L2，而
\[
 E|u(X_t,t)-u_*(X_t)|=V^{-1}\|u(t)-u_*\|_1\to0.
\]
故 U_t 的概率极限是 U_*=u_*(X_*)。由 SPI.3、SPI.6、SPI.9，
U_*=u(η,a)−I_*−Z_*，I_* 的定义一致。

同一均匀分布还给准确范数关系
\[
 \left|\|U_t-U_*\|_{L^2(\mathbb P)}-V^{-1/2}\|u(t)-u_*\|_2\right|
 \le\|u_*(X_t)-u_*(X_*)\|_{L^2(\mathbb P)}\to0.
\]
因 u(η,a)−Z_t 已强 L2 收敛，由此得到
\[
 u(t)\to u_*\text{ 强 }L^2_x
 \quad\Longleftrightarrow\quad I_t\to I_*\text{ 强 }L^2(\mathbb P)
 \quad\Longleftrightarrow\quad
 \{|I_t|^2:t\in[t_0,T_*)\}\text{ 一致可积},
 \quad a<t_0<T_*\text{ 固定}.
 \tag{SPI.10}
\]
最后的 Vitali 等价使用已经得到的概率收敛；远离终端的闭区间本来光滑。
一致 L2 有界只控制 E|I_t|² 的总量，并不控制其大值尾部，不能代替 SPI.10。

还可准确识别总二次缺陷。令 C_t=u(η,a)−Z_t，则 C_t→C_* 强 L2，
I_t⇀I_* 弱 L2，所以 ⟨C_t,I_t⟩ 收敛。展开 U_t=C_t−I_t 后得到
\[
 \lim_{t\uparrow T_*}E|I_t|^2-E|I_*|^2
 =V^{-1}\left(\lim_{t\uparrow T_*}\|u(t)\|_2^2-\|u_*\|_2^2\right)\ge0.
 \tag{SPI.11}
\]
两边极限存在：原能量有左极限，C_t 的强收敛和交叉项收敛给左侧。
这是总量缺陷的识别，不是逐点能量原子的对应或排除。

## 6. 路线判断与实际来源

本次的可用补足是 SPI.6–9：同一概率空间中的补偿误差、黏性冲量强 L2 迹，
以及压力冲量的强 L3/2 迹。没有消去 SPI.10 的二次尾部条件。
即使将来取得速度强 L2 迹，也不等于证明终端光滑；完整 Clay 目标没有改成能量等式。
不得将这里的均匀标签平均条件化成每个空间终点的上界，或直接移植为 PF 的共同好尺度。

不能直接把 SPI.5 的 4e(a) 界用于任意截断后的压力源：其推导用了
E[Y_t|X_t]=u(X_t,t) 与真实 NS 压力正交性。换源后条件均值一般不再是原速度。
下一项若继续，只检查保留这些关系的二次尾部机制；不再以“也是随机表示”
重开 CG 的 Weber 形变、六维迹或既有四次应变预算。

原文：[Drivas–Eyink，arXiv:1606.00729v3](https://arxiv.org/html/1606.00729v3)，
§2 式 (3)–(13) 的时间方向与 FDR、§5 式 (51)–(54) 的 NS 压力冲量及其后限制，
本轮主任务实际定向读取。它们已在 [CG §3](clay_b_clock_stochastic_screen_20260907.md)
登记；不是新文献发现，也不将原文的无黏性极限讨论移植成固定 ν 的终端定理。
本稿的固定概率空间推导写在上面，未依赖一个未核的弱解终端随机表示。

主任务本轮全文读 CG、LP、TG 与 DBS；C 全文读 CG、LP 作去重，确认 FDR 旧覆盖；
B 独立核条件均值、二阶矩及终端对应，A 独立核重启增量、Itô 符号与黏性冲量。
B 为终端对应全文读 TG，并读 LP 第 1–160 行；未重核全部上游依赖。
C 实际全文审读 182 行、8237 字节成稿，限定通过 SPI.1–11；审读版本 SHA256：
`fbab690e7d214adfebb89a0900280ca52bf9f527c6ba5ce35470a6276d152a2d`。
主任务最后仅补本段审读范围记录，没有改变数学推导。
参与式 AI 推导与审读不等于真人同行评审或新颖性认证。
本轮仅两条普通定向查询后回到已登记原文；没有 Deep Research 后台服务、
仿真、随机抽样、DGX、科学图、新读者 PDF、独立 release 或发布操作。

## 7. 同日续核：不换压力源的径向尾矩

本节起完成 §6 留下的具体测试。输入提交为
`4b09c511193a80f9eedaceac73afcb523d32716c`；前六节的阅读、查询和审读记录
仍只描述首轮。沿用原 X、Y、Z、压力与概率空间，不另造截断后的 NS 解。

令 R>0，Π_R 为到闭球 {|y|≤R} 的 Euclidean 投影，
θ_R(y)=(1−R/|y|)_+，并在 y=0 取零。定义
\[
 \Phi_R(y)=(|y|-R)_+^2,\qquad Q_R(t)=E\Phi_R(Y_t),\qquad
 \frac14E[|Y_t|^2 1_{\{|Y_t|>2R\}}]\le Q_R(t)
 \le E[|Y_t|^2 1_{\{|Y_t|>R\}}].
 \tag{SPI.12}
\]
因此 sup_t Q_R(t)→0 正是 Y 的平方一致可积性；因为 u(η,a) 有界，
它也等价于 I 的平方一致可积性。R≥||u(a)||∞ 时 Q_R(a)=0。

Y 在闭光滑前缀是绝对连续的有限变差过程；Φ_R 是 C1，
DΦ_R(y)=2θ_R(y)y。这里的链式法则没有 Itô 二阶修正或局部时项。
定义条件量
α_R=E[θ_R(Y_t)|X_t=x]，κ_R=E[θ_R(Y_t)Z_t|X_t=x]，
b_R=E[Π_R(Y_t)|X_t=x]。SPI.4 给 b_R=u−α_Ru−κ_R，故
\[
 Q_R'(t)=-2\langle\nabla p\cdot(\alpha_Ru+\kappa_R)\rangle
          =2\langle\nabla p\cdot b_R\rangle.
 \tag{SPI.13}
\]
只能消去完整的 ⟨u·∇p⟩，不能分别消去两个截断项。
因 |b_R|≤R，用 SPI.9 的压力预算得到实际可付的时间界
\[
 \operatorname{Var}_{[s,t]}Q_R
 \le2R\int_s^t\langle|\nabla p|\rangle dr
 \le C R\mathcal D(s,t),\qquad a\le s<t<T_*.
 \tag{SPI.14}
\]
这里 Var 表示标量函数的时间总变差，不是随机方差。
每个固定 R 的 Q_R 因而有唯一终端极限；代价增长为 R，不给一致尾部小量。
这项界利用真实压力取消，不要求未拆开的 |Y·∇p| 在整个前终端区间可积。

## 8. 协方差小量存在，但压力配对仍缺指数

设 c(x,t)=E[|Z_t|²|X_t=x]。因为条件均值 E[Z_t|X_t]=0，
条件 Cauchy–Schwarz 给 |κ_R|²≤c α_R(1−α_R)。同时
0≤α_R≤1，⟨α_R⟩≤e(a)/R²。由 SPI.6，Z 在加入终端后是 L2 连续的，
所以整个时间族 |Z_t|² 一致可积。记
z(K)=sup_t E[|Z_t|²1_{|Z_t|²>K}]→0，则对任意 K>0，
\[
 \sup_{a\le t<T_*}\|\kappa_R(t)\|_{L^2_{\rm av}}^2
 \le\sup_t E[|Z_t|^2 1_{\{|Y_t|>R\}}]
 \le z(K)+K e(a)/R^2.
 \tag{SPI.15}
\]
先取 K 大、再取 R 大，得到 κ_R→0 于 L∞_t L2_x。
这是实际小量，不是把协方差当成完全未控。但直接用于本测试的压力界
∇p∈L1_t L3/2_x 需要 L∞_t L3_x 配对；SPI.15 没有支付这个指数。

记 g(t)=⟨|G(t)|²⟩^(1/2)。固定胞的零均值 Sobolev 给
||u||_{6,av}≤Cg，||∇p||_{3/2,av}≤Cg²，以及
\[
 |\langle\nabla p\cdot\alpha_Ru\rangle|
 \le\|\nabla p\|_{3/2,{\rm av}}\|\alpha_R\|_{6,{\rm av}}
       \|u\|_{6,{\rm av}}
 \le C e(a)^{1/6}R^{-1/3}g(t)^3.
 \tag{SPI.16}
\]
这需要本轮未支付的 ∫g³；基本耗散只支付 ∫g²。
SPI.15–16 的分项绝对值估计只定位当前缺口，不证明两个有符号项不可能进一步抵消，
也不把所列范数说成原 NS 所有已知预算的穷尽清单。

## 9. 正源二阶矩传播只控制波动部分

这一交叉检查使用联合分布的弱式，不假定 (X,Y) 在 y 变量有密度或平滑性。
联合输运的 y 方向力是 −∇p(x,t)，显式扩散只在 x。
对 Y_iY_j φ(X) 用 Itô，并用 SPI.4，令
Σ(x,t)=E[Y_t⊗Y_t|X_t=x]，K=Σ−u⊗u，Γ=∂t+u·∇−νΔ，得到
\[
 \Gamma\Sigma=-(u\otimes\nabla p+\nabla p\otimes u),\qquad
 K=E[Z_t\otimes Z_t\mid X_t=x],\qquad
 \Gamma K=2\nu GG^{\mathsf T},\quad K(a)=0.
 \tag{SPI.17}
\]
Γ(u⊗u) 比 ΓΣ 多出 −2νGGᵀ，正源的符号由此固定。
同漂移的正传播算子给 K 的正半定表示。特别地，c=tr K≥0 满足
Γc=2ν|G|²；源在整个有限时间柱属于 L1，且 u∈L2_{t,x}。
直接使用本轮全文读回的 TG §2–4 同漂移引理，得到
\[
 c(t)\to c_*\text{ 强 }L^1_x,\qquad
 s(x,t):=E[|Y_t|^2\mid X_t=x]=|u(x,t)|^2+c(x,t),
 \qquad \Gamma s=-2\operatorname{div}(pu).
 \tag{SPI.18}
\]
s≥0 且 ⟨s⟩=e(a)，但其均值部分 |u|² 的尾仍未控制。
结合 TG 的 u 强 L1 收敛、原速度 L2 上界和 c 的强 L1 迹，
s 的空间一致可积性／强 L1 终端迹等价于 u 的强 L2 终端迹。
这使用上述真实分解，不是一般条件期望的反向一致可积性结论。

不能把 s 的散度源直接当作 TG 已付的 L1 函数源。例如直接使用能量插值得
||u·∇p||_1≤C||u||_2^(1/2)||G||_2^(5/2)，时间幂次仍大于2。
这不排除联合分布存在其他可用耦合结构，只说明二阶正源传播本身尚未补足尾部。

## 10. 阈值极限准确返回未付的终端能量缺陷

令 Y_*=u(η,a)−I_*。SPI.9 给 Y_t→Y_* 强 L1，而 SPI.5 给 E|Y_t|²=e(a)。
函数 Ψ_R(y)=|y|²−Φ_R(y) 是 2R-Lipschitz，所以对每个固定 R，
\[
 Q_R(T_*^-):=\lim_{t\uparrow T_*}Q_R(t)
 =\Delta_Y+E\Phi_R(Y_*),\qquad
 \Delta_Y=e(a)-E|Y_*|^2\ge0.
 \tag{SPI.19}
\]
这个极限也与 SPI.14 一致。由 Y=u(η,a)−I 的固定初端交叉项弱收敛和 SPI.11，
Δ_Y 恰是体积平均的原速度总能量缺陷。

事实上，取任意 ε>0，先固定 R0 使 EΦ_R0(Y_*)<ε，再由 SPI.19
取 b<T* 使所有 b<t<T* 的 Q_R0(t)≤Δ_Y+2ε。
当 R≥R0，Φ_R≤Φ_R0；在剩下的紧前缀 [a,b]，Y 的路径幅值有确定的共同上界
||u(a)||∞+∫_a^b||∇p(r)||∞dr，故足够大 R 时 Q_R 在此前缀恒为零。
另一方面，每个 R 的 sup_t Q_R 不小于其终端极限，因而不小于 Δ_Y。
两侧合并得到
\[
 \lim_{R\to\infty}\sup_{a\le t<T_*}Q_R(t)
 =\Delta_Y
 =V^{-1}\left(\lim_{t\uparrow T_*}\|u(t)\|_2^2-\|u_*\|_2^2\right).
 \tag{SPI.20}
\]
这里没有预设交换两个极限。结论把目标准确还原为缺陷消失，没有证明 Δ_Y=0。

本次具体测试完成：已得固定 R 时间变差和 κ_R 的一致 L2 小量，
但未得能消去 SPI.20 右侧的新压力估计。停止仅用这些预算继续改写径向尾矩、
正二阶矩传播或其等价缺陷条件；有新的实质有符号压力配对估计才重开此入口。
这不是所有随机方法的不可能性结论，也不是正则性、反例或独立原创成果。
完整 Clay 目标不变，TG 仍是最后独立冻结；本补记不建立 release 或新交接。

续核来源与审读：主任务全文读本稿首轮186行及 LP、TG；B 独立推导 SPI.12–16、
SPI.19–20，A 独立推条件矩的弱式与正源符号，C 核条件方差与 TG 接口并做定向去重。
主任务只重开已登记 Drivas–Eyink 原文 §5 的 NS 表示、FDR 及无黏性极限限制；
没有新检索命中或充分查新结论，不把原文的无黏性讨论当固定 ν 终端定理。
C、B 分别实读新增第187–325行，并核对前186行与各自已全文读过的首轮版本相同。
成稿审读版本为325行、15311字节，SHA256：
`f58f48de562cfb92676152db1d17183d87b8edeaa862f7147a35e82c997280a4`。
C 限定通过 SPI.12–20，B 重点通过截断／配对／阈值极限，不重新认证全部上游依赖。
主任务全文读回补记，最后只补本段实际审读记录。参与式 AI 审读不是真人同行评审。
