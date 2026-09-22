# 固定母球中的谐和压力高角尾

2026-09-22。PRIVATE_CORE / PROVED IN STATED SCOPE / OPEN / NOT CLAY。

跨模环带估计保存后，本节改用椭圆调和结构处理 SA.7 中的一部分压力。结论是：固定母球的谐和压力，高角模在同心小球内有一致指数尾界；已有压力可积性和动能界足以使这部分的归一化截止通量趋零。局部二次源压力、低模动态和非线性输运没有由此得到控制。这是经典调和展开在当前接口的应用，不主张新颖性。

## 1. 同一实际压力的合法分解

固定轴经过指定中心0，固定足够小 \(b>0\) 和终点前区间 \((-T,0)\)。取同一周期无力解的局部提升，在 \(B_{2b}\times(-T,0)\) 上有适当弱解资格、\(p\in L^{3/2}\) 和能量类；推导能量时仍限终点前光滑区间。固定正黏性不变，任何缩尺度过程都不更换原解或初值。

取固定径向 \(\eta\in C_c^\infty(B_{2b})\)，在 \(B_b\) 上为一。将其乘的速度张量零延拓到全空间，定义

\[
p_{\rm loc}=\sum_{i,j}\mathcal R_i\mathcal R_j(\eta u_i u_j),
\qquad H=p-p_{\rm loc}.
\tag{HP.1}
\]

\(\mathcal R_i\) 是全空间 Riesz 算子。由原无力方程的 \(-\Delta p=\partial_i\partial_j(u_i u_j)\)，在 \(B_b\) 内有 \(\Delta H=0\)。这不是把局部角平均当作环面全局对称，也不是删除周期远场；实际原压力与此全空间局部源解的差完整留在 \(H\) 中。

能量插值给局部 \(u\in L^{10/3}\)，故在有限母柱上 \(u\in L^3\)。经典 \(L^{3/2}\) Calderón–Zygmund 界给

\[
\|p_{\rm loc}\|_{L^{3/2}(\mathbb R^3\times(-T,0))}
\le C\|u\|_{L^3(B_{2b}\times(-T,0))}^2,
\quad H\in L^{3/2}(B_b\times(-T,0)).
\tag{HP.2}
\]

不要求这个压力范数在任意解族间共同有界；当前是同一实际解、固定母球的有限范数。可积压力规范按适当解假设选择，空间常数的改变不会影响下文的非零高角模。

## 2. 谐和函数的统一高角尾

令 \(Q_N\) 是标量角投影 \(|m|\ge N\)，\(N\ge2\)。对几乎每个时间，\(H\) 在整个 \(B_b\) 内调和；仅在穿孔球调和不够。取 \(\rho=b/2\)，以所选轴为角轴，单位球面正交归一的球谐展开为

\[
H(r\omega)=\sum_{l=0}^\infty\sum_{m=-l}^{l}
c_{lm}(r/\rho)^lY_{lm}(\omega),
\qquad \sum_{l,m}|c_{lm}|^2=\|H(\rho\,\cdot)\|_{L^2(S^2)}^2.
\tag{HP.3}
\]

母球内部的光滑性保证此内球面展开及局部一致收敛。高角模必有 \(l\ge|m|\ge N\)。Cauchy–Schwarz 与加法公式 \(\sum_{m=-l}^l|Y_{lm}|^2=(2l+1)/(4\pi)\) 给

\[
|Q_NH(r\omega)|\le\|H(\rho\,\cdot)\|_2
\left[\sum_{l\ge N}\frac{2l+1}{4\pi}(r/\rho)^{2l}\right]^{1/2}.
\tag{HP.4}
\]

对 \(q=r/\rho\le1/4\)，尾和精确为

\[
\sum_{l\ge N}(2l+1)q^{2l}
=q^{2N}\left[\frac{2N+1}{1-q^2}+\frac{2q^2}{(1-q^2)^2}\right]
\le C(N+1)q^{2N}.
\tag{HP.5}
\]

调和内点 \(L^{3/2}\) 估计给
\(\|H(\rho\,\cdot)\|_{L^2(S^2)}\le Cb^{-2}\|H\|_{L^{3/2}(B_b)}\)。因此对 \(0<R\le b/8\)，

\[
\|Q_NH\|_{L^\infty(B_R)}
\le Cb^{-2}\sqrt{N+1}(2R/b)^N\|H\|_{L^{3/2}(B_b)}
\le Cb^{-2}(4R/b)^N\|H\|_{L^{3/2}(B_b)}.
\tag{HP.6}
\]

常数独立于 \(N,R\)。第二步用 \(\sqrt{N+1}\le2^N\)。没有假设尖锐角投影在 \(L^\infty\) 上一致有界；一致性来自球面 \(L^2\) 正交展开。

## 3. 实际截止压力通量的尺度归一界

固定光滑径向截止族 \(\chi_R\)，支于 \(B_R\)，\(\|\nabla\chi_R^2\|_\infty\le C_\chi/R\)。令 \(I_R=(-R^2,0)\subset(-T,0)\)，高角向量部分 \(z=P_Hu=P_Hw\)。每个同心球上的协变投影在 \(L^2\) 中收缩，故若

\[
M_0=\operatorname*{ess\,sup}_{-T<t<0}\|u(t)\|_{L^2(B_{2b})}<\infty,
\]

就有 \(\|z(t)\|_{L^2(B_R)}\le M_0\)。这里 \(M_0\) 是范数，不是范数平方，也不是 PF 的共同尺度常数。

径向 \(\nabla\chi_R^2\) 与 \(z\) 点乘保持相应标量高模，所以
\(\int H z\cdot\nabla\chi_R^2=\int Q_NH z\cdot\nabla\chi_R^2\)。逐时空间估计为

\[
\left|\int Q_NH z\cdot\nabla\chi_R^2\right|
\le Cb^{-2}M_0 R^{1/2}(4R/b)^N
\|H(t)\|_{L^{3/2}(B_b)}.
\tag{HP.7}
\]

空间因子来自 \(R^{-1}|B_R|^{1/2}=C R^{1/2}\)。时间 Hölder 给 \(|I_R|^{1/3}=R^{2/3}\)，从而

\[
\boxed{
R^{-1}\int_{I_R}\left|\int Q_NH z\cdot\nabla\chi_R^2\right|dt
\le Cb^{-2}M_0R^{1/6}(4R/b)^N
\|H\|_{L^{3/2}(B_b\times I_R)}.}
\tag{HP.8}
\]

右端以固定母柱范数控制，随 \(R\to0\) 趋零；即使 \(N=2\) 也如此。每个窗口可选择不同整数 \(N(R)\ge2\)，此通量估计不需要对投影作时间微分，也不承担换模后的能量演化结论。同一指定中心和固定轴没有移动。

## 4. 不能从本式删除的压力与其它项

SA.7 中仍有

\[
\int Q_Np_{\rm loc}\,z\cdot\nabla\chi_R^2,
\tag{HP.9}
\]

以及原输运、扩散、时间截止和跨模项。HP.8 只控制固定母球内的调和差。\(p_{\rm loc}\) 包括全部 \(v\otimes v,v\otimes w,w\otimes v,w\otimes w\) 源；其中能被具体投影消去的项须按协变资格证明，不能把它预先化为纯 \(w^2\)。

有限母柱上的 \(p_{\rm loc}\in L^{3/2}\) 与 \(z\in L^3\) 只保证有限尺度配对合法，不给带 \(R^{-2}\) 截止归一化因子的统一小量。这里未证明 HP.9 的符号抵消或临界控制。

固定 \(b\) 是结论的一部分。若另令母球 \(b\asymp R\) 并每窗重新分解，\(b^{-2}\)、\(H_R\) 的范数以及角尾比例都随之改变，不能沿用固定母球的趋零结论。

## 5. 已有方法与研究意义

球内任意调和函数的齐次调和展开是经典事实；[Armitage 1991 的出版方公开 Extract](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/polynomial-expansions-of-positive-harmonic-functions-in-the-unit-ball/4C31201A97EECE83A5F9C29E3B3BDBC0) 明述这一一般展开。该文后续尖锐界针对正调和函数，不应用于这里的有符号压力；本节没有全文审查或调用那些尖锐定理。HP.4–8 的常数、尾和及通量指数在本节直接推导。

旧 R0.69J 处理 Hessian 的低阶四极与Taylor余项，GPH处理压力历史的固定物理远场，PF使用调和压力时间原函数。它们没有被此次高角尾估计替代；低阶压力和不同尺度的近场仍存在。固定远场可剥离本来就是已知类型的信息，不能把它包装成新的临界控制。

本阶段把一个压力子项从当前未控项中单独辨认出来，没有解决完整局部压力、原解低模增长、轴附近控制或 PF 好尺度。按持续授权，审查保存后转向仍有实际信息缺口的下一问题，不以本节保存作为研究停止条件。
