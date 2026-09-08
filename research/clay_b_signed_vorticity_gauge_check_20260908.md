# 有符号涡量指数矩：表示成立，临界估计仍缺

2026-09-08。PRIVATE_CORE，内部解析检查。用户恢复后，从 DBS 保存点继续。这里核算保留方向扩散负项的涡量反应传播，不重复将热核平滑或随机表示本身当成新机制。得到的是标准工具的具体适用边界，不是新的正则性定理、独立成果小节或发布冻结。一般三维 NS / Clay 仍 OPEN / NOT CLAY。

## 1. 对象与正则化

固定三维周期空间 \(\Omega=(\mathbb R/2\pi\mathbb Z)^3\)、正黏性 \(\nu\)，同一无外力光滑 NS 解在 \([0,T_*)\) 存在，\(T_*<\infty\)。保留任意光滑无散初值，固定 \(0<a<T_*\)，所有计算先止于 \(b<T_*\)。记
\[
 G=\nabla u,\quad S=(G+G^\top)/2,\quad
 \omega=\operatorname{curl}u,\quad q=|\omega|,\quad
 L=\partial_t+u\cdot\nabla-\nu\Delta.
 \tag{SVG.1}
\]
在 \(q>0\) 处，\(Lq=(\xi^\top S\xi-\nu|\nabla\xi|^2)q\)，\(\xi=\omega/q\)。这是旧 [VB §2–3](clay_b_vorticity_direction_budget_20260907.md) 的非零集恒等式，不可忽略该稿的零集耗散测度后直接全域使用。

固定 \(\kappa>0\)，令 \(r_\kappa=(q^2+\kappa^2)^{1/2}\)。向量链式法则给
\[
 Lr_\kappa=V_\kappa r_\kappa,\qquad
 V_\kappa=\frac{\omega^\top S\omega}{r_\kappa^2}
 -\nu\sum_j\left\{
 \frac{|\partial_j\omega|^2}{r_\kappa^2}
 -\frac{(\omega\cdot\partial_j\omega)^2}{r_\kappa^4}\right\}.
 \tag{SVG.2}
\]
大括号非负，因此 \((V_\kappa)_+\le|S|\le|G|\)。在非零集，负项是
\[
 -\nu\frac{q^2}{r_\kappa^2}|\nabla\xi|^2
 -\nu\frac{\kappa^2}{r_\kappa^4}|\nabla q|^2.
 \tag{SVG.3}
\]
SVG.2 在零点同样光滑；SVG.3 只用来解释非零集结构。全稿保留固定 \(\kappa\)，不交换 \(\kappa\downarrow0\) 与终端、路径或积分极限。

## 2. 精确指数矩及其两侧比较

记 \(\mathcal U_\kappa(t,s)\) 为 \(Lz=V_\kappa z\) 的正传播，定义 \(H_\kappa(t,x)=\mathcal U_\kappa(t,a)1(x)\)。在闭前终端区间，系数光滑有界。令从 \((t,x)\) 反向标记的周期扩散满足
\[
 dY_\rho=-u(t-\rho,Y_\rho)d\rho+\sqrt{2\nu}\,dB_\rho,
 \quad Y_0=x,\quad0\le\rho\le t-a.
\]
对 \(e^{\int_0^\rho V_\kappa(t-\eta,Y_\eta)d\eta}z(t-\rho,Y_\rho)\) 作 Itô 计算，其漂移为 \(-Lz+V_\kappa z=0\)。有界区间上的鞅期望给
\[
 H_\kappa(t,x)=\mathbb E_{t,x}
 \exp\!\left(\int_0^{t-a}V_\kappa(t-\rho,Y_\rho)d\rho\right),
 \qquad r_\kappa(t)=\mathcal U_\kappa(t,a)r_\kappa(a).
 \tag{SVG.4}
\]
这保留同一真实漂移及有符号势，不是把 NS 时间反转成另一个 NS 解。

现取 \(M=\|\omega(a)\|_\infty>0\)，并固定 \(\kappa=M\)。初端满足 \(M\le r_M(a,x)\le\sqrt2M\)。传播保序给所有 \(a\le t<T_*\)
\[
 M H_M(t,x)\le r_M(t,x)\le\sqrt2M H_M(t,x).
 \tag{SVG.5}
\]
因此，对这个固定正龄、固定解，\(\sup_{a\le t<T_*}\|H_M(t)\|_\infty<\infty\) 与 \(\sup_{a\le t<T_*}\|\omega(t)\|_\infty<\infty\) 等价。保留负方向项的表示合法，但仅写出表示没有给出一致上界，更没有减少待证困难。此处不证明一切利用该表示的方法无效。

若 \(M=0\)，周期无散无旋场 \(u(a)\) 是空间常向量；经典唯一性使此后仍为同一常速度解。任取 \(\kappa>0\) 即有 \(V_\kappa=0,H_\kappa=1\)。此平凡分支不通过除以 M 处理。

## 3. 改写为无反应方程，漂移却不再无散

令 \(R=M H_M/r_M\)。由乘积法则，\(L(r_M R)=R Lr_M+r_M LR-2\nu\nabla r_M\cdot\nabla R\)，故
\[
 [\partial_t+(u-2\nu\nabla\log r_M)\cdot\nabla-\nu\Delta]R=0,
 \qquad 1/\sqrt2\le R\le1.
 \tag{SVG.6}
\]
新漂移的散度是 \(-2\nu\Delta\log r_M\)，一般不为零。因此旧不可压缩漂移的 Nash 常数不能直接用于这一变换。比值的最大值原理只是再次证明 SVG.5，不控制 \(r_M\) 本身。

旧 VB 的 \(L^1\) 模长预算则确实给出有限的空间平均。设 \(g(t)=\|G(t)\|_2\)、\(Q(a)=\|\omega(a)\|_1\)、\(v_\Omega=|\Omega|\)。由 \(|f_\kappa|\le q|S|_{\rm op}\) 及周期无散恒等式，\(\int|f_\kappa|\le g^2/\sqrt3\)，其中 \(f_\kappa=\omega^\top S\omega/r_\kappa\)。令 \(d_\kappa\) 为 VB.3 的非负密度，得到
\[
 \int_a^b\!\!\int r_M|V_M|
 \le Q(a)+\frac2{\sqrt3}\int_a^b g^2,
 \quad
 \int H_M(b)\le\frac{Q(a)+M v_\Omega+\frac1{\sqrt3}\int_a^b g^2}{M}.
 \tag{SVG.7}
\]
第一式使用 \(r_M V_M=f_M-\nu d_M\) 以及 \(\int(r_M-M)\) 的完整恒等式。它也给 \(\int|V_M H_M|<\infty\)。[TG §2–4](clay_b_strong_gradient_terminal_trace_20260908.md) 的同漂移引理因此可直接用于 \(z=H_M,f=V_MH_M\)：\(H_M\) 有强 L1 终端迹，且在整个有限区间一致可积。这是旧引理的非临界推论，不给空间最大值控制。

## 4. 取绝对值后，短时核仍有指数缺口

记 \(P(t,s)\) 为同一无散漂移的无反应标量传播。旧 [LT §4](clay_b_terminal_trace_localization_20260908.md) 的周期 Nash 证明给
\[
 \|P(t,s)\|_{2\to\infty}\le C\{v_\Omega^{-1/2}+[\nu(t-s)]^{-3/4}\}.
\]
于是，对 \(a\le b-h<b<T_*\)，
\[
 \left\|\int_{b-h}^bP(b,s)|G(s)|ds\right\|_\infty
 \le C\int_0^h\{v_\Omega^{-1/2}+(\nu\tau)^{-3/4}\}g(b-\tau)d\tau.
 \tag{SVG.8}
\]
能量只给 \(g\in L^2(a,T_*)\)，不足以用 Hölder 控制右端的对角奇性。具体地，\(g(b-\tau)=\tau^{-\beta}\)、\(1/4\le\beta<1/2\)，是 L2 时间函数，而加权积分发散；这里只检查该时间卷积算子，不声称此函数由原 NS 实现。普通时间 \(L^p,p>4\) 足够控制 SVG.8 的右端；该卷积的端点可用 \(L^{4,1}\) Lorentz 控制，不能单由普通 \(L^4\) 对此右端作一致估计。这不否定另用原 NS 方程得到的正则性准则。

TG 给出的 \(L^\infty_tL^1_x\) 与能量的 \(L^2_tL^2_x\) 插值也不闭合：若 \(1/m=1-\theta/2,p=2/\theta\)，\(0\le\theta\le1\)（\(\theta=0\) 时 \(p=\infty\)），则
\[
 \frac1p+\frac3{2m}=\frac32-\frac\theta4\ge\frac54>1.
 \tag{SVG.9}
\]
这是这一组范数结合无散核估计的缺口，不排除未证明的原方程相关性增益。

还可把 TG 的实际截源残差原样代入。沿用其 \(F=-G^2-\nabla^2p\)、有界辅助场 \(v_R\)、\(e_R=F-F_R\)，有 \(\sup|v_R|\le B_R\) 和 \(\|e_R\|_{L^1_{t,x}}=\delta_R\to0\)。Kato、传播正性和复合性给
\[
 \left\|\int_{b-h}^bP(b,s)|G(s)|ds\right\|_\infty
 \le hB_R+
 \left\|\int_a^b\min\{h,b-\sigma\}\,
 P(b,\sigma)|e_R(\sigma)|d\sigma\right\|_\infty.
 \tag{SVG.10}
\]
证明：\(|G(s)|\le B_R+\int_a^sP(s,\sigma)|e_R(\sigma)|d\sigma\)，再用 Tonelli；给定 \(\sigma\) 的外层 s 区间长度正是 \(\min\{h,b-\sigma\}\)。初端 \(v_R(a)=G(a)\) 已包括在 \(B_R\) 中。

LT 的 \(1\to\infty\) 界给出近对角奇异核部分 \(C\nu^{-3/2}(b-\sigma)^{-1/2}\|e_R(\sigma)\|_1\)，另有有限体积项至多 \(Cv_\Omega^{-1}h\delta_R\)。仅有 \(\delta_R\to0\) 不控制前一个带奇权积分。完整压力仍在同一个 \(e_R\) 内；不能独立截断压力、删去它或任意交换 R、h 与终端极限。

## 5. 零集、局部化及停止边界

旧 VB.11 的精确剪切，在非零涡量条带内方向常值、伸长为零，但模长仍衰减；VB.12 的零集耗散承担全部损失。因此将非零集的 \(V=0\) 当成全域无杀死势并套用无缺陷表示，会给错误答案。固定 M 的 SVG.2 已合法包含零点邻域，不需要作这种替换。

若将 SVG.4 限制到空间球并停在首次触边，表示必须保留侧边界的 \(r_M\) 值和停止前指数因子。全周期的初端比较不能替代未知的侧边界控制。也不能改用反射过程而默认为原解满足零法向导数；那会出现额外边界局部时间项。本轮没有提出已闭合的局部核下界、桥条件指数矩、共同 A/E 或小 K。

## 6. 结论、来源与下次起点

本轮完成固定正则化的有符号表示、两侧比较、变换漂移和实际截源核尾的核算。它说明当前“保留负项后直接估计指数矩”的尝试仍缺一致点态估计；普通绝对值核与 TG 定性迹也未补上这个缺口。停止这几个具体推导的相邻改写，不宣布整个随机方法无效。下一项具体替代机制尚未选定，也没有新的无条件临界输入。应先提出一项尚未核算、能利用原 NS 时空相关性的明确目标式，再检验其相对已列缺口的增益；不能把选择意向、等价表示或旧来源重新算成成果。

主任务实读 VB、TG 全文和 LT §4 完整论证；SVG.2–10 在本轮直接复算。三位 AI 协作者分别参与去重、时间核和零集/正传播核查；最终实际成稿审查另记检查点，不冒称真人同行评审或新颖性认证。

普通定向搜索共三个查询，定位到的随机表示及浓缩比较均有旧记录；[浓缩比较论文摘要](https://arxiv.org/abs/2503.16723)还明确区分全空间与环面，不能据此移植无前因子的全空间结论。本轮不采用其未重读的完整证明，也未启动 Deep Research；检索不是穷尽性综述。

只保存内部记录，无新独立小节、release、发布移交、网页、PDF、翻译、recap、仿真、DGX 或科学附图。TG 仍为最后独立冻结小节，既有一次交接不变。
