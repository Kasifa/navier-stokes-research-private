# 径向对数熵：变量系数压力项仍未受控

2026-09-08，北京时间。RL，PRIVATE_CORE，内部有限公式检查，不是新的研究小节或独立冻结包。SG 已完成的估计不重做。以下是同一光滑周期原 NS 的精确计算，不是新的临界先验估计，OPEN / NOT CLAY。

## 一个全域 C2 测试函数

沿用 SG 的 \(q=|S|,\ N=S^2+\Omega^2+H,\ LS=-N\)。定义
\[
 \psi(q)=(e+q)\log(1+q/e)-q,\quad
 k(q)=\psi'(q)=\log(1+q/e),\quad
 g(q)=k(q)/q,\quad g(0)=1/e,\quad\Phi(S)=\psi(|S|).
 \tag{RL.1}
\]
\(\Phi\) 全域 C2、凸，\(D\Phi(S)=Q=g(q)S\)。它的 Hessian 径向特征值为 \(1/(e+q)\)，切向特征值为 g(q)，且 \(1/(e+q)\le g(q)\le1/e\)。在 \(q>0\) 上写 \(B=S/q\)，则
\[
 d_\Phi=\sum_jD^2\Phi(S)[\partial_jS,\partial_jS]
 =\frac{|\nabla q|^2}{e+q}+qk(q)|\nabla B|^2.
 \tag{RL.2}
\]
在 S=0 处使用全域 Hessian，\(d_\Phi=|\nabla S|^2/e\)。这次没有新的零集缺陷测度；不是从不可微的 q 方程删掉旧测度，而是重新选了零点可 C2 微分的函数。

完整积分等式为
\[
 \int\Phi(S(T))+\nu\int_0^T\!\!\int d_\Phi
 =\int\Phi(S(0))-\int_0^T\!\!\int Q:(S^2+\Omega^2+H).
 \tag{RL.3}
\]
它保留无界的 k 系数。有限光滑 T 时各项存在，不代表在候选终点前有统一控制。

## 压力的常系数消项没有消去变量系数

因 \(\operatorname{div}S=\Delta u/2\)，逐时周期分部积分给
\[
 \mathcal P=\int g(q)S:H
 =-\int\nabla p\cdot\left[\frac{g(q)}2\Delta u+
                       g'(q)S\nabla q\right].
 \tag{RL.4}
\]
第二项在零矩阵处按零连续延拓。常数 g 的压力积分确实为零，因为 \(\operatorname{div}\Delta u=0\)；变量 g 不满足这个消项。另一等价积分式是
\[
 \mathcal P=-\int\nabla p\cdot A^\top\nabla(g(q)).
 \tag{RL.5}
\]
其证明为 \(S:H=A:H=\partial_j u_i\,\partial_i\partial_j p\)，沿 i 分部积分，用 \(\partial_i\partial_j u_i=0\)。标量 \(g(q)\) 的弱梯度几乎处处解释，不能因 g 在零矩阵处不具有经典径向梯度而删除其余区域的项。常数部分的消项不等于 RL.5 为零。

正半定 Hessian 的最大特征值为 g，故
\[
 \sum_j|\partial_jQ|^2\le g\,d_\Phi,\qquad
 |\operatorname{div}Q|^2\le3g\,d_\Phi.
\]
Young 不等式给
\[
 |\mathcal P|\le\frac\nu2\int d_\Phi+
                  \frac3{2\nu}\int g(q)|\nabla p|^2.
 \tag{RL.6}
\]
惯性项绝对值由 \(k(q)|A|^2\) 控制。因此
\[
 \boxed{\int\Phi(S(T))+\frac\nu2\int_0^T\!\!\int d_\Phi
 \le\int\Phi(S(0))+
 \int_0^T\!\!\int k(q)|A|^2+
 \frac3{2\nu}\int_0^T\!\!\int g(q)|\nabla p|^2.}
 \tag{RL.7}
\]
右侧最后两项尚未由 SG 或基本能量控制。压力 Hessian 的 L1 界不能直接提供压力梯度平方界；\(g\le1/e\) 也没有补上它。没有对实际 NS 声称这些量一定发散，更没有以未知上界证明本路线不可能。

## 记录边界与下一步

主任务推导 RL.1–4、6–7，C 独立复算系数、零集接口和抛物链式，并给出等价的 RL.5；主任务随后重算其指标和分部积分。模块核验不等于此文件已经由非作者或真人审读。没有仿真、DGX、附图、文献新定理或新的发布请求。

这项有限检查确认：直接扩大测试函数斜率，未能把完整梯度估计变成临界控制。下一步只允许针对 RL.3／5 中实际带符号的惯性—压力组合寻找可证消项，并先核对既有压力／伸长记录；不再尝试靠无界系数乘一个 L1 上界完成估计。若没有额外的原 NS 结构输入，不将 RL.7 当作新成果继续迭代权重。
