# 伴随梯度与应变：已支付的局部预算和形状耗散的边界

2026-09-08。AG，PRIVATE_CORE，INTERNAL CHECK / OPEN / NOT CLAY。接 SP.18，本轮修正了一个过粗的成本判断：有界标量伴随的梯度估计不必使用四次时间范数，已有 LP 被动标量预算即可适用。下面补全局部截止、检验原耗散单独支付的猜想，并核对完整源响应的接口。这是内部检查，不另计独立研究小节或 release；不声称新颖性、真人同行评审或 NS 正则性突破。

## 1. 同一实际漂移与完整局部式

固定未归一化 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\)、\(\nu>0\)，同一个无外力光滑 NS 解存在于 \([0,T)\)，压力取零空间均值。仅在 \(0<a<b<T\) 上先行计算。采用
\[
 G_{ij}=\partial_j u_i,\quad H=\nabla^2p,\quad N=G^2+H,\quad
 L_-=\partial_s+u\cdot\nabla-\nu\Delta,\quad L_-G=-N.
 \tag{AG.1}
\]
给定光滑实标量终端 \(\eta\)，令 \(h(s)=S(b,s)^*\eta\)，即
\[
 L_+h=0,\quad h(b)=\eta,\quad L_+=\partial_s+u\cdot\nabla+\nu\Delta.
\]
这里 S 是 SP 的真实逐分量传播，不换参考漂移。记
\(M=\|\eta\|_\infty\)、\(g=\nabla h\)、\(J=\nabla^2h\)、\(e=|g|^2\)、
\(I=g^TGg=g^T(\operatorname{sym}G)g\)。最大值原理给 \(|h|\le M\)，而
\[
 L_+e=-2I+2\nu|J|^2,\qquad
 \left[\int\phi e\right]_a^b
 =\iint e(\phi_s+u\cdot\nabla\phi-\nu\Delta\phi)
       -2\iint\phi I+2\nu\iint\phi|J|^2 .
 \tag{AG.2}
\]
空间积分均在周期胞，双积分在 \([a,b]\)。对非负光滑 \(\phi\)，两个时间切片都保留。反时 \(\tau=b-s\)、漂移 \(-\widetilde u\) 下，等价地有
\[
 [\int\widetilde\phi\,\widetilde e]_{\tau_0}^{\tau_1}
 +2\nu\iint\widetilde\phi|\widetilde J|^2
 =2\iint\widetilde\phi\,\widetilde I+
 \iint\widetilde e(\widetilde\phi_\tau-\widetilde u\cdot\nabla\widetilde\phi
                         +\nu\Delta\widetilde\phi).
 \tag{AG.3}
\]
因此物理时间 AG.2 的扩散截止是负号，不能与反时版本混用。对一般半径 r、时间长度 \(O(r^2)\) 的截止，除以 r 后，时间、输运和扩散截止成本分别有 \(r^{-3},r^{-2},\nu r^{-3}\) 因子；它们没有凭局部化消失。

## 2. 四次成本不是必需的：这是旧 LP 的适配

关键是正确方向的无散兼容性 \(\partial_iG_{ij}=0\)，不是假设 G 对称。周期分部积分给
\[
 \int I=-\int h\,G:J,\qquad
 2\left|\int I\right|\le
 \nu\|J\|_2^2+\frac{M^2}{\nu}\|G\|_2^2.
\]
代入 AG.2，得到
\[
 \boxed{\quad
 \|\nabla h(a)\|_2^2+\nu\int_a^b\|\nabla^2h\|_2^2
 \le\|\nabla\eta\|_2^2+
       \frac{M^2}{\nu}\int_a^b\|G\|_2^2 .
 \quad}
 \tag{AG.4}
\]
有界函数的周期分部积分还给
\[
 \|\nabla h(s)\|_4^2\le C M\|\nabla^2h(s)\|_2,\qquad
 \iint|\nabla h|^4\le CM^2\iint|\nabla^2h|^2 .
 \tag{AG.5}
\]
例如先将 \(\int|\nabla h|^4\) 中一个导数移至
\(|\nabla h|^2\nabla h\)，再用 Cauchy--Schwarz 即得；不要求 h 均值为零。

这正是 [LP.8–9](clay_b_leray_paid_budget_20260907.md) 的有界被动标量估计，应用于反时无散漂移 \(-u(b-\tau)\)。原始位移导数 K-bound 及同类有界函数插值可见 [Constantin，§7](https://arxiv.org/html/math/0005116)。这里不将文献的位移、虚拟速度或可逆 Jacobian 结论一并移植。

所以 SP.18 的四次成本只是那条 Hölder--Gronwall 估计的缺陷，不是实际标量伴随必需的输入。AG.4 不需要原梯度形状耗散；也不能移用于带额外零阶伸长、没有同样最大值控制的 CG Weber 向量。它仍保留终端梯度预算，没有得到 \(\nabla h\) 的临界 \(L^5_{s,x}\) 或最大值界。

## 3. 静态局部截止可以由本地 A/E 支付

固定中心 \(x_0\)、\(2r<\pi\)、\(b-a\le r^2\)。取静态
\(0\le\chi\le1\)，于 \(B_r(x_0)\) 为1，支于 \(B_{3r/2}(x_0)\)，
\(|\nabla\chi|\le C/r,\ |D^2\chi|\le C/r^2\)，令 \(\phi=\chi^4\)。
对任意非负 \(\phi\)，兼容性准确给
\[
 I_\phi:=\int\phi I
 =-\int\phi h\,G:J-\int h(\partial_i\phi)G_{ij}h_j.
 \tag{AG.6}
\]
原输运截止 \(T_\phi=\int(u\cdot\nabla\phi)e\) 不能略去；把一个 h 导数转移后，
\[
 T_\phi=-\int h(u\cdot\nabla\phi)\Delta h
 -\int h\{G^T\nabla\phi+(D^2\phi)u\}\cdot g.
 \tag{AG.7}
\]
由于 \(|\nabla\phi|\le C\chi^3/r,\ |D^2\phi|\le C\chi^2/r^2\)，三个乘积分别按
\((\chi^2J)(\chi u/r)\)、\((\chi^2G)(\chi g/r)\)、
\((\chi u/r)(\chi g/r)\) 配权。故对任意固定小 \(\delta>0\)，
\[
 \begin{aligned}
 2|I_\phi|&\le\delta\nu\int\chi^4|J|^2+
       \frac{C_\delta M^2}{\nu}\int\chi^4|G|^2+
       C_\delta\nu r^{-2}\int\chi^2e,\\
 |T_\phi|&\le\delta\nu\int\chi^4|J|^2+
       \frac{C_\delta M^2}{\nu}\int(\chi^4|G|^2+r^{-2}\chi^2|u|^2)
       +C_\delta\nu r^{-2}\int\chi^2e .
 \end{aligned}
 \tag{AG.8}
\]
AG.2 中的 \(\nu\Delta\phi\) 项有同样的 \(C\nu r^{-2}\int\chi^2e\) 上界。吸收小 \(\delta\) 后，写 \(E_\phi(s)=\int\phi|g(s)|^2\)，有
\[
 E_\phi(a)+\nu\iint\chi^4|J|^2
 \le E_\phi(b)+\frac{CM^2}{\nu}
      \iint_{B_{2r}}(|G|^2+r^{-2}|u|^2)
       +C\nu r^{-2}\iint_{\operatorname{supp}\chi}e .
 \tag{AG.9}
\]
这里没有用全胞耗散替代母球输入。

再取静态 \(\theta=1\) 于 \(\operatorname{supp}\chi\)，支于 \(B_{2r}\)，有相同导数尺度。由 \(L_+h^2=2\nu e\)，保留终端并丢去非负底部标量项，得到
\[
 \nu\iint_{\operatorname{supp}\chi} e
 \le CM^2\left[r^3(1+\nu)+r^{-1}\iint_{B_{2r}}|u|\right].
 \tag{AG.10}
\]
定义本时窗、同一母球的实际预算
\[
 \mathsf A_m=(2r)^{-1}\sup_{a\le s\le b}\int_{B_{2r}}|u(s)|^2,
 \qquad
 \mathsf E_m=(2r)^{-1}\iint_{B_{2r}}|G|^2 .
\]
它们不改成跟踪另一漂移的球，也不隐去均值。时间长度与空间 Cauchy 给
\(\iint|u|^2\le2r^3\mathsf A_m\)、
\(r^{-1}\iint|u|\le Cr^3\sqrt{\mathsf A_m}\)。因此
\[
 \boxed{\quad
 r^{-1}E_\phi(a)+\nu r^{-1}\iint\chi^4|J|^2
 \le r^{-1}E_\phi(b)+CM^2
 \left[\nu^{-1}(\mathsf A_m+\mathsf E_m)+1+\nu+\sqrt{\mathsf A_m}\right].
 \quad}
 \tag{AG.11}
\]
C 只依固定截止几何。母柱必须在同一解的光滑时段内；若另加非零时间截止，须回到 AG.2 支付其导数，不能继续直接引用静态简式。

对幅值有界且 \(\|\nabla\eta_r\|_2^2\le Cr\) 的标准终端截函数，AG.11 给局部有限预算；没有证明指定中心的 \(\mathsf A_m+\mathsf E_m\) 沿临界尺度有界或小，更没有给共同好尺度和小 K。全局能量有限不能自动支付除以 r 的这些量。

## 4. 与原梯度联合测试时，压力仍在

记 \(P=g\otimes g\)。它是伴随导数的张量，不是压力或 Leray 投影。由 AG.1–2，
\[
 L_+P=-G^TP-PG+2\nu J^2.
\]
与 \(L_-G=-N\) 对偶，在同一个闭前终端时窗上有
\[
 \begin{aligned}
 [\int\phi\,G:P]_a^b
 ={}&\iint (G:P)(\phi_s+u\cdot\nabla\phi+\nu\Delta\phi)
       +2\nu\iint\partial_k\phi\,G:\partial_kP\\
 &+\iint\phi\{-N:P-G:(G^TP+PG)+2\nu G:J^2\}.
 \end{aligned}
 \tag{AG.12}
\]
内部两个 Laplacian 在正反扩散对偶下相消；其截止交叉项留在第一行。全胞 \(\phi=1\) 时，
\[
 \frac d{ds}\int g^TGg
 =-\int g^T(2G^2+GG^T+H)g+2\nu\int G:J^2.
 \tag{AG.13}
\]
其中 \(-|G^Tg|^2\) 虽有利，却不是整个式子的独立耗散。[PGR.5](clay_b_piola_gradient_remainder_20260907.md) 给
\(\partial_i(2G^2+H)_{ij}=0\)，只能将其配对转成
\(-\int h(2G^2+H):J\)，不能令它为零。
未加权 \(H\in L^1\) 不直接控制 \(H:(g\otimes g)\)；也没有证明这些较高乘积的全部终端极限。AG.4、AG.11 不需要继续展开 AG.13。

原梯度范数的耗散测度则沿用先前的完整定义：
\[
 q=|G|,\quad
 L_-q=-\mathbf1_{\{q>0\}}(G/q):N-\nu\mu_G,\qquad
 \mu_G=\mathbf1_{\{q>0\}}q\,|\nabla(G/q)|^2\,dx\,ds+\zeta_G,
 \quad \zeta_G\ge0 .
 \tag{AG.14}
\]
在本稿光滑父解上，以范数正则化识别零集测度。不可把它换成参考耗散，也不能令 \(\mu_G=|J|^2\,dx\,ds\)：J 是另一标量问题的 Hessian。

## 5. 纯形状耗散支付的强猜想不成立

本段只否定下列过强的量词：对所有实际光滑 NS 及其 \(\|h\|_\infty\le1\) 伴随，在任意内部时间窗 I 上，存在只依 \(\delta,\nu\) 和固定周期的 \(C_\delta\)，使
\[
 \iint_I g^T(\operatorname{sym}G)g
 \le\delta\nu\iint_I|J|^2+C_\delta\int_{\mathbb T^3\times I}d\mu_G.
 \tag{AG.15}
\]
它没有统一初始能量上限、时间端点、窗口长度下界或其他补偿项。不是 AG.4、AG.11 所陈述的界。

取整数 \(n\to\infty\)，固定终端 \(b=1\)，令
\[
 u_n(s)=a_n(s)\sin y\,e_1,\quad
 a_n(s)=n^4e^{\nu(1-s)},\quad p_n=0,\qquad
 \eta_n(x,y)=\tfrac12[1+\sin(nx+n\sin y)].
 \tag{AG.16}
\]
这是全程光滑的真实无外力周期 NS：非线性输运为零，\(G_n^2=H_n=0\)。令 \(h_n\) 是同一漂移的真实后向伴随，\(h_n(1)=\eta_n\)，故 \(0\le h_n\le1\)。

先在终端精确积分。写 \(\psi=nx+n\sin y\)，则
\(\eta_x=(n/2)\cos\psi,\ \eta_y=(n/2)\cos y\cos\psi\)；
二阶导数为
\(\eta_{xx}=-(n^2/2)\sin\psi\)、
\(\eta_{xy}=-(n^2/2)\cos y\sin\psi\)、
\(\eta_{yy}=-(n^2/2)\cos^2y\sin\psi-(n/2)\sin y\cos\psi\)。
保留 Hessian 两个混合分量，得到
\[
 \int\nabla\eta_n^T(\operatorname{sym}G_n(1))\nabla\eta_n
       =\tfrac{\pi^3}{2}n^6,\qquad
 \|\nabla^2\eta_n\|_2^2
       =\tfrac{19\pi^3}{8}n^4+\tfrac{\pi^3}{2}n^2 .
 \tag{AG.17}
\]
零集耗散不能删除。\(q_n=a_n|\cos y|\)，由一维分布恒等式
\((|\cos y|)''=-|\cos y|+2\delta_{\pi/2}+2\delta_{3\pi/2}\)，准确得到
\[
 d\mu_{G_n}
 =2a_n(s)(\delta_{y=\pi/2}+\delta_{y=3\pi/2})\,dx\,dz\,ds,
 \qquad
 \mu_{G_n}(s)(\mathbb T^3)=16\pi^2 a_n(s).
 \tag{AG.18}
\]
其经典方向耗散在零集外为零，但完整测度不为零。

还需把终端计算推进到真实内部时间，而不能只给终端测试。令
\(F_n(\tau)=h_n(1-\tau)\)，则
\[
 \partial_\tau F_n-a_n(1-\tau)\sin y\,\partial_xF_n-\nu\Delta F_n=0.
\]
逐阶微分、最大值原理和有限阶 Gronwall 给
\(\|F_n(\tau)\|_{C^m}\le C_m n^m
 \exp(C_m\int_0^\tau a_n(1-\sigma)\,d\sigma)\)。
在 \(0\le\tau\le2n^{-8}\) 上，指数一致有界，所以
\(\|\partial_\tau F_n\|_{C^2}\le C_\nu n^7\)、
\(\|F_n(\tau)-\eta_n\|_{C^2}\le C_\nu n^{-1}\)。
这里仅用每个明确光滑漂移的短时稳定性，不要求整族有统一 Lipschitz 界。因此在正龄内部窗口
\[
 I_n=[1-2n^{-8},1-n^{-8}]\subset(1/2,1)
\]
上，充分大 n 满足
\[
 \int g_n^T(\operatorname{sym}G_n)g_n\ge c n^6,\qquad
 \|J_n\|_2^2\le C_\nu n^4,\qquad
 \mu_{G_n}(s)(\mathbb T^3)\le C_\nu n^4.
 \tag{AG.19}
\]
积分后 AG.15 左端至少为 \(c n^{-2}\)，右端至多为
\(C_\nu(\delta\nu+C_\delta)n^{-4}\)，矛盾。

这不否定含 \(\int|G|^2\)、端点梯度、固定能量上限或其他相关补偿的估计。整族 \(\|G_n\|_2^2\) 量级为 \(n^8\)，终端梯度平方量级为 \(n^2\)，窗口随 n 缩短；不能扩大成固定长度窗口或统一初始能量的反例。全部解光滑，既不是奇性构造，也不是原形状方法整体不可能的证明。

## 6. 完整源响应支付到哪里

AG.4 可先通过中间时刻把终端测试放宽到 L2。令 \(\Delta=b-a>0\)、
\(\mathcal E_{a,b}=\int_a^b\|G\|_2^2\)、\(V=(2\pi)^3\)。
标量 L2 能量允许选
\(\sigma\in[a+\Delta/2,a+3\Delta/4]\)，使
\(\|\nabla h(\sigma)\|_2^2\le C(\nu\Delta)^{-1}\|\eta\|_2^2\)。
旧 physical-adjoint / LT 的周期 Nash \(2\to\infty\) 界则给
\(\|h(\sigma)\|_\infty^2\le C[V^{-1}+(\nu\Delta)^{-3/2}]\|\eta\|_2^2\)。
在 \([a,\sigma]\) 上应用 AG.4，得到
\[
 \|\nabla S(b,a)^*\eta\|_2\le B_\Delta\|\eta\|_2,\qquad
 B_\Delta^2=C\left[
  (\nu\Delta)^{-1}+
  \nu^{-1}\{V^{-1}+(\nu\Delta)^{-3/2}\}\mathcal E_{a,b}\right].
 \tag{AG.20}
\]
先对光滑 \(\eta\) 证明，再由 L2 稠密性取得此算子界。它保留真实漂移，只使用已付的梯度平方累计量；不是漂移梯度的最大值界。

完整有符号响应为
\(\mathcal D_{a,b}=\int_a^b S(b,s)N(s)\,ds=S(b,a)G(a)-G(b)\)。
逐分量两次空间分部积分给
\[
 \begin{aligned}
 \langle(\mathcal D_{a,b})_{ij},\eta\rangle
  &=-\int u_i(a)\partial_jh(a)+\int u_i(b)\partial_j\eta,\\
 |\langle(\mathcal D_{a,b})_{ij},\eta\rangle|
  &\le\|u_i(a)\|_2 B_\Delta\|\eta\|_2+
                        \|u_i(b)\|_2\|\nabla\eta\|_2 .
 \end{aligned}
 \tag{AG.21}
\]
这给固定正时间间隔的 \(H^{-1}\) 上界。它不证明 D 的强 \(H^{-1}\) 终端迹，也不证明速度的强 L2 终端迹。对半径 r 的截函数，
\(\|\nabla\eta_r\|_2=O(r^{1/2})\)，只用全局速度 L2 支付第二项、再除以 r 仍有 \(r^{-1/2}\) 成本；不能据此宣布临界源响应小。

直接把源的导数转到 h 上同样保留缺口。由无散性，
\[
 \iint N_{ij}h
 =-\iint u_i(\partial_j u_k)\partial_k h+\iint p\,\partial_i\partial_jh .
 \tag{AG.22}
\]
也可将压力只转移一次。基本能量和周期压力表示给
\(u\in L^{10/3}_{s,x}\)、\(uG,\nabla p\in L^{5/4}_{s,x}\)、
\(p\in L^{5/3}_{s,x}\)，而 AG.4–5 给 \(\nabla h\in L^4\)、\(J\in L^2\)。
分项 Hölder 的倒数和分别为
\[
 \frac45+\frac14=\frac{21}{20}>1,\qquad
 \frac35+\frac12=\frac{11}{10}>1 .
 \tag{AG.23}
\]
这些范数单独不能支付所需一致乘积界；不是宣称实际乘积必不积分。原 \(hN\) 在旧 Hardy / TG 的 \(N\in L^1\) 和有界 h 下本就可积。真正缺少的是联合结构给出的额外临界尺度收益，不是再证明一次普通 L1 可积性。

## 7. 结论、下一测试与核验范围

本轮关闭了“有界标量伴随只能支付四次成本”的判断，也排除了 AG.15 那个无能量和端点补偿的纯耗散猜想。AG.11 是原有 LP 机制的本地化，不另计新机制。压力、端点、原零集测度和指定中心尺度均没有被消去；一般三维正则性和 Clay 问题保持 OPEN。

下一测试限于 AG.22 的完整有符号源配对：保留同一真实伴随，检查源的散度—旋度及压力组合能否在联合估计中改善 AG.23 的分项界，并给出除以 r 后的实际响应控制。先对照 SP、IDC、LP 的既有交换子及投影计算，避免仅把经典 Hardy--BMO 界、分部积分或新命名的条件范数重复计为进展。不能先假设临界 \(\nabla h\in L^5\)、源在更强空间或共同好尺度，再说问题已解决；新的无条件临界估计尚未接受。若只有等价重写，就停止该具体测试，不创建相邻审计 release。

主任务全文核 SP、VR、AH、PGR、WE，定向核 LP 至§5及旧 physical-adjoint 的能量/Nash段；本轮的经典来源只定向阅读 Constantin §7 所列导数预算和插值段，没有全面查新或整篇证明认证。A 核完整局部式、静态 \(\chi^4\) 截止闭合和原梯度联合对偶；B 核真实剪切—真实伴随窗口及完整零集测度；C 核 LP 去重、源指数与 \(H^{-1}\) 接口。最终文件的实际读回范围与哈希另记检查点；这些都是参与式 AI 核验。

仅保存内部主稿、检查点和研究恢复索引。无仿真、DGX、数值证书、科学附图、HTML/PDF、翻译、新 recap、release 或交接。TG 仍是最后独立完成小节，其冻结和一次交接保持不变。本任务不查询发布或反向执行。
