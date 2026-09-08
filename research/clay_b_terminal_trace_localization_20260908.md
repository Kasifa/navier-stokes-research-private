# 强终端迹的局部化：截止、伴随与源尾速率

2026-09-08。LT，PRIVATE_CORE，INTERNAL CHECK / OPEN / NOT CLAY。本轮完成 TG 后的局部化检查，没有取得新的无条件临界估计，不另计独立完成小节、release 或发布交接。Nash 平滑是旧稿已有工具；这里的新工作是将它用于 TG 的真实梯度源，并明确仍缺的速率。强终端迹 TG 保持原样。

## 1. 同一解与固定截止

固定未归一化的 \(2\pi\) 三维环面、\(\nu>0\)，同一无外力光滑 NS 解在 \([0,T)\) 存在，\(T<\infty\)，任取 \(0<a<T\)。以下局部球取在固定注入半径内，涉及 \(B_{2r}\) 时取 \(2r<\pi\)，母柱位于同一解的时空区域。沿用
\[
 L=\partial_t+u\cdot\nabla-\nu\Delta,\quad
 G=\nabla u,\quad H=\nabla^2p,\quad F=-G^2-H,\quad LG=F,
 \qquad Lq+\nu\mu_G=B_0:F,\quad q=|G|.
 \tag{LT.1}
\]
\(\mu_G\ge0\) 含原零集耗散；不只取经典非零集密度。GD 给
\(\|F(t)\|_1\le(1+C_H)\|G(t)\|_2^2\)，TG 给 \(G(t)\to G_*\) 强 L1、\(u(t)\to u_*\) 强 W1,1。这里不假设 T 正则或可延拓。

取 TG 的整体光滑截断 \(F_R=F\vartheta(|F|^2/R^2)\)，辅助解 \(Lv_R=F_R\)、\(v_R(a)=G(a)\)。记 \(w_R=G-v_R\)、\(e_R=F-F_R\)。凸范数正则化给 \(L|w_R|\le|e_R|\)。对任意非负光滑空间紧支或周期测试 \(\phi\)，闭前终端时段 \(a\le s<t<T\) 上
\[
 \left[\int\phi|w_R|\right]_s^t
 \le\int_s^t\!\!\int\phi|e_R|
 +\int_s^t\!\!\int|w_R|(\phi_t+u\cdot\nabla\phi+\nu\Delta\phi).
 \tag{LT.2}
\]
测试延至 T 且导数有界时，固定 r、R 后可用 TG 和辅助强迹令 \(t\uparrow T\)。原 G 属于时空 L2，辅助解有界，故固定截止下 \(u w_R\) 可积。这里不是原梯度耗散恒等式，不把 \(w_R\) 的范数缺陷换成 \(\mu_G\)。

令 \(I_r=(T-r^2,T)\)，标准截止空间支于 \(B_{2r}(x_0)\)，定义于闭时间窗 \(\overline{I_r}\)，具有标准导数界而不要求两端同时消失。除以 r 后，源、时间截止、输运、扩散的系数依次为
\[
 r^{-1},\qquad Cr^{-3},\qquad Cr^{-2},\qquad C\nu r^{-3}.
 \tag{LT.3}
\]
底部项 \(r^{-1}\int\phi(s)|w_R(s)|\) 仍在；静态空间截止才没有时间导数项。用 \(|w_R|\le|G|+B_R\)、\(B_R=\|G(a)\|_\infty+2R(T-a)\)，以及 PF 的标准 \(\mathsf A,\mathsf E\)，直接 Cauchy 只给
\[
 \begin{aligned}
 r^{-2}\int_{I_r}\!\!\int_{B_{2r}}|u||w_R|
 &\le C\{\sqrt{\mathsf A(2r)\mathsf E(2r)}
                  +B_Rr^2\sqrt{\mathsf A(2r)}\},\\
 r^{-3}\int_{I_r}\!\!\int_{B_{2r}}|w_R|
 &\le C\{\sqrt{\mathsf E(2r)}+B_Rr^2\}.
 \end{aligned}
 \tag{LT.4}
\]
前提是这些母柱位于同一解的区域内。这就是旧 WE 的同尺度成本，不是收缩。

压力也没有因截源变成局部量。按 WE/AH 在母球 \(B_\ell\) 作无散扩张 \(v_\ell\)，令 \(\pi_\ell\) 为扩张压力、\(h_\ell=p-\pi_\ell\) 在内球调和。子尺度 \(r=\theta\ell\)、\(0<\theta\le1/4\) 上
\[
 r^{-1}\int_{I_r}\!\!\int_{B_r}|F|
 \le C\theta^{-1}\mathsf E(\ell)
       +C\theta^2\{\mathcal H(\ell)+\mathsf E(\ell)\},
 \quad \mathcal H(\ell)=\ell^{-1}\int_{Q_\ell}|H|.
 \tag{LT.5}
\]
这是 NE.1–4 的旧绝对值界。只使用时间区间包含，没有额外 \(\theta^2\) 时间因子。由于 \(|e_R|\le|F|\)，它可粗控源尾，却没有产生随 R 的定量衰减。将 \(F\) 的非线性截断拆为分别截断近压和远压并不等价。

## 2. 固定正龄与按尺度重启不同

记 \(\delta_R(a)=\int_a^T\int|e_R|\)、\(L_a=T-a\)。全周期 Kato 可以避开局部通量，但它只给
\[
 r^{-1}\int_{B_r}|G_*|
 \le Cr^2\{\|G(a)\|_\infty+2RL_a\}+\delta_R(a)/r.
 \tag{LT.6}
\]
若仅靠此上界趋零，就必须同时控制 \(R(r)r^2\to0\) 与
\(\delta_{R(r)}(a)=o(r)\)。固定解的 \(\delta_R(a)\to0\) 没有给这个对角关系；不擅自交换两个极限。

改在 \(a_r=T-r^2>0\) 重启，差值初始为零，但上界变成
\[
 r^{-1}\int_{B_r}|G_*|
 \le Cr^2\|G(a_r)\|_\infty+CRr^4+\delta_R(a_r)/r.
 \tag{LT.7}
\]
差值底部消失，不等于辅助初值成本消失。重标度 \(G^{(r)}=r^2G\)、\(F^{(r)}=r^4F\) 下，源阈值为 \(\lambda=r^4R\)。固定 a 的辅助源累计是 \(2\lambda L_a/r^2\)，按尺度重启则为 \(2\lambda\)；后者仍保留 \(r^2\|G(a_r)\|_\infty\)。能量和 Hardy 只给
\(\delta_R(a_r)\le C\int_{I_r}\|G(t)\|_2^2dt=o(1)\)，没有除以 r 后的小量。

## 3. 终端伴随权可以构造，原耗散仍保留

先取光滑 \(0\le\eta_r\le1\)，支于 \(B_r(x_0)\)，质量 \(m_r\asymp r^3\)。在同一真实漂移上解
\[
 h_t+u\cdot\nabla h+\nu\Delta h=0,\qquad h(T)=\eta_r.
 \tag{LT.8}
\]
这不是求一条反向 NS 解。先以 \(b<T\) 为终点求 \(h_b\)。反向 L2 收缩及对固定 \(\eta_r\) 的 Duhamel 估计给
\[
 \|h_b(t)-\eta_r\|_2
 \le\int_t^b\{\|\nabla\eta_r\|_\infty\|u(s)\|_2+
                       \nu\|\Delta\eta_r\|_2\}\,ds.
\]
比较 \(b<c<T\) 时，在 b 用此界估计 \(h_c(b)-\eta_r\)，再反向收缩到 t。因 \(u\in L^1_tL^2_x\)，这些解延为终端数据后在 \(C([a,T];L^2)\) 中 Cauchy。最大值、质量守恒和能量差的极限给
\[
 0\le h\le1,\quad \int h(t)=m_r,\quad
 \nu\int_t^T\|\nabla h\|_2^2
   =\tfrac12\{\|\eta_r\|_2^2-\|h(t)\|_2^2\}.
 \tag{LT.9}
\]
固定闭前终端子区间上，实际光滑漂移的抛物内估计给 \(h_b\to h\) 的空间光滑收敛。梯度能量差和终端 L2 连续性排除上述能量等式的额外端点缺陷。指标终端数据可用 L2 逼近、保持 \(0\le\eta\le1\) 后取得。

将 \(h_b\) 用于原梯度及完整范数方程，再令 \(b\uparrow T\)，得到
\[
 \begin{aligned}
 \int\eta_r G_*&=\int h(a)G(a)+\int_a^T\!\!\int hF,\\
 \int\eta_r|G_*|+\nu\int_a^T\!\!\int h\,d\mu_G
 &=\int h(a)|G(a)|+\int_a^T\!\!\int hB_0:F.
 \end{aligned}
 \tag{LT.10}
\]
极限依据是 TG 的强 L1 迹、\(F\in L^1\)、\(\mu_G\) 总量有限、\(h_b\le1\) 及远离终端的光滑收敛；先截去一小段终端尾，再让尾长度趋零。没有把零集测度当作普通密度。指标终端数据同样可按此顺序通过。

于是原熵而非差值熵满足
\[
 \int\eta_r|G_*|+\nu\int h\,d\mu_G
 \le m_r\{\|G(a)\|_\infty+2RL_a\}
       +\int_a^T\!\!\int h|e_R|.
 \tag{LT.11}
\]
欧拉截止项确实消失，但这里尚无
\(\int h|H|\le C\int h|G|^2\) 的加权压力定理。安全的界是
\(\int h|H|\le \|h(t)\|_\infty C_H\|G(t)\|_2^2\)，右边为全胞积分。

伴随权也没有自动支配指定柱。对在 \(B_r\) 为零、在 \(B_{2r}^c\) 为一的截止，用 \(\|h\|_2\le\sqrt{m_r}\) 得粗逃逸界
\[
 \frac{\int_{B_{2r}^c}h(t)}{m_r}
 \le \min\{1,C(T-t)[U_2r^{-5/2}+\nu r^{-2}]\},
 \quad U_2=\sup_{a<t<T}\|u(t)\|_2.
 \tag{LT.12}
\]
这只是上界，不是逃逸必然发生；也不是中心点态下界。在抛物时长 \(r^2/\nu\) 上它不提供统一小量。旧 physical-adjoint B.8–15 已给更细的移动中心矩预算；其中也保留相应归一化耗散依赖，不能在此默认为已控制。没有 \(h\ge c>0\) 的合法中心柱下界，就不能用 LT.10 直接得到 PF 的无权 \(\mathsf K(r)\)。

## 4. 旧 Nash 工具给出明确的时间源核

记 \(S^u(t,s)\) 为同一漂移的逐分量齐次传播，\(V=(2\pi)^3\)。旧 BP.11 和 physical-adjoint B.14 已展开如下标准估计：
\[
 \|S^u(t,s)\|_{1\to\infty}
 \le C\{V^{-1}+[\nu(t-s)]^{-3/2}\}.
 \tag{LT.13}
\]
简证：Kato 给 L1 收缩，Fourier 分频给
\(y\le CK^3m^2+K^{-2}D\)；高于常数模态平台时
\(D\ge cy^{5/3}m^{-4/3}\)。与 \(y'=-2\nu D\) 合并得到
\(1\to2\) 界 \(C[V^{-1/2}+(\nu(t-s))^{-3/4}]\)。
反向伴随的漂移为时间反转后的 \(-u\)，仍无散；对偶给
\(2\to\infty\)，在中点合成即得 LT.13。这里是线性辅助演化，不把时间反转说成 NS 对称性。常数不含漂移大小或高阶范数，但只给高度，不给位置下界。

令 \(f(s)=\|F(s)\|_1\)、
\[
 K_r(\tau)=\min\{1,C|B_r|[V^{-1}+(\nu\tau)^{-3/2}]\}.
\]
正性、Duhamel 和 LT.13 给每个指定中心
\[
 \int_{B_r(x_0)}|G_*|
 \le K_r(L_a)\|G(a)\|_1+\int_a^T K_r(T-s)f(s)\,ds.
 \tag{LT.14}
\]
先对 \(t<T\) 证明；\(K_r\le1\)、\(f\in L^1\) 和 TG 强迹允许支配收敛到 T。也可用 LT.10 与指标终端权的高度界证明。它替换的是局部质量估计中的未知 Fourier 尾，不是原强 L1 时间连续性的统一模量。

写 \(J_F(h)=\int_{T-h}^Tf(s)\,ds\)，\(h_r=r^2/\nu<L_a\)。分开早期初值、有限体积项、近终端源和远端时间尾，得
\[
 \begin{aligned}
 r^{-1}\int_{B_r}|G_*|
 \le{}&Cr^2[V^{-1}+(\nu L_a)^{-3/2}]\|G(a)\|_1
       +Cr^2V^{-1}J_F(L_a)\\
 &+J_F(h_r)/r
       +Cr^2\nu^{-3/2}\int_{h_r}^{L_a}
                    \tau^{-3/2}f(T-\tau)\,d\tau .
 \end{aligned}
 \tag{LT.15}
\]
一个使此上界趋零的充分条件是
\[
 J_F(h)=o(\sqrt{\nu h})\quad(h\downarrow0).
 \tag{LT.16}
\]
远端加权项用 \(dJ_F(\tau)=f(T-\tau)d\tau\) 分部积分，保留有限上端项，并以
\(\frac32\int_{h_r}^{L_a}\tau^{-5/2}J_F(\tau)d\tau\) 控制即可。
先在 \(0<\tau<\delta\) 用 \(J_F(\tau)\le\epsilon\sqrt{\nu\tau}\)，得到常数倍 \(\epsilon r^2/(\nu h_r)=C\epsilon\)；固定 \(\tau\ge\delta\) 部分为 \(O_\delta(r^2)\)。没有用“可积”代替所需速率。

现有 Hardy 仅给
\(J_F(h)\le(1+C_H)\int_{T-h}^T\|G(t)\|_2^2dt=o(1)\)。
LT.16 是待证的额外源条件，不是本轮得到的事实。本稿只使用它对上述上界的充分性，不声称它与指定中心正则性等价。即使 LT.15 的切片小量成立，本轮也未由它取得 PF 的共同 \(\mathsf A+\mathsf E\) 与小 \(\mathsf K\)。

若直接将条件加强为全胞 enstrophy 尾 \(o(\sqrt h)\)，更不能当作新的正则判据。标准周期 H1 延拓接口与
\(y' \le C\nu^{-3}y^3\)、\(y=\|G\|_2^2\)，在有限最大奇异端点给
\(y(t)\ge c\nu^{3/2}(T-t)^{-1/2}\)，故其尾至少为 \(c'\nu^{3/2}\sqrt h\)。
该微分不等式来自三维 Sobolev、插值及吸收黏性；对趋终端且 \(y\to\infty\) 的子列积分 \(y^{-2}\) 得所述下界。均值由无散输运消去。这里仅解释一个过强替代条件与旧局部理论的关系，不将其转为额外成果；完整联合源 F 的 L1 尾与全胞 enstrophy 尾不等同。

## 5. 本轮结论与下一项

固定截止回到 WE/AH 的同尺度项；同漂移伴随消去截止，但留下加权真实源和中心权重下界；Nash 给明确的时间卷积，却没有控制其临界源尾。这三个结论相容。它们只表明当前绝对值估计链没有闭合，不是对一切局部化、伴随或 NS 稳定机制的不可能性证明。

因此不继续仅优化 R(r)、换平滑正权或加强到已知足以延拓的能量尾。下一项选定的待检对象是同一真实漂移的**带符号矩阵源响应**
\[
 \mathcal D_{a,t}=\int_a^t S^u(t,s)(G^2+\nabla^2p)(s)\,ds,
 \qquad G(t)=S^u(t,a)G(a)-\mathcal D_{a,t}.
 \tag{LT.17}
\]
NE 已给空间 Hardy/零均值结构；先核查该结构在实际漂移传播中保留什么抵消，尤其压力算子与传播的交换子。必须估计完整响应而非重新取 \(|F|\)，保留原初值、时间顺序、非局部压力和临界系数；不能把另一个形式恒等式或经典 Hardy 原子分解计作增益。这个具体测试已选定，其所需新临界估计尚未证明；不复活直接不变密度重写，也不导入任意粗漂移反例为原 NS 反例。

## 6. 实际检查范围

主任务全文读 TG、WE、PF、NE；定向读 AH 1–105、BP 1–215、physical-adjoint 160–230，以及旧 common-adjoint 的来源范围记录。A 全文读 TG，定向读 WE 46–81、199–216及 AH 7–47，独立核对 LT.2–7 对应模块；B 全文读 TG，核对终端伴随构造、完整熵式和逃逸模块；C 全文读 TG，独立展开 Nash、时间核与临界分部积分模块。最终文件审读与哈希另记检查点，不将模块消息冒充最终稿全文审读；全部为参与式 AI 核查，非真人同行评审。

普通一次查询后，主任务打开 [Albritton–Dong，arXiv:2107.12511v1](https://arxiv.org/html/2107.12511v1)，定向阅读导言及公式1.23附近的 Nash 与定位区别。只作经典来源和范围核对，不移植其一般粗漂移反例或未读证明。本轮未用 Deep Research、未认证新颖性；不把该网页转换显示日期误当论文版本日期。Nash 的本地既有证明已通过文件检索去重。

没有仿真、DGX、数值证书、科学图、读者HTML/PDF、翻译、新recap、release或发布交接。只保存这次内部推导和下一项问题，既有 TG 源码与其一次移交记录不变。
