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
