# 空间变参考：原耗散并不会随相对误差一起消失

2026-09-08。VR，PRIVATE_CORE，内部核算；不是一个另计的完成研究小节。它执行 MA 下一步中的有界检查，随后停止这条直接归一化参考吸收支路。一般三维 NS 仍 OPEN / NOT CLAY。

## 1. 原耗散与完整乘积公式

在光滑 NS 柱上令 \(L=\partial_t+u\cdot\nabla-\nu\Delta\)、\(G=\nabla u\)、\(q=|G|\)、\(N=G^2+\nabla^2p\)，故 \(LG=-N\)。在 q>0 处 \(B=G/q\)，\(B_0\) 是将其在零处设为0的有界场。沿用 GD 的原范数正则化极限
\[
 Lq+\nu\mu_G=-B_0:N,\qquad
 \mu_G=\mathbf1_{\{q>0\}}q|\nabla B|^2\,dxdt+\zeta_G.
 \tag{VR.1}
\]
黏性因子不含在 \(\mu_G\) 内。对任意 \(W\in C_t^1C_x^2\)、\(|W|\le1\)，令 \(e=q-W:G\ge0\)，则
\[
 Le+\nu\mu_G=-(B_0-W):N-(LW):G+2\nu\nabla W:\nabla G.
 \tag{VR.2}
\]
这是对 \(\sqrt{q^2+\kappa^2}-W:G\) 作乘积法则再取极限的结果。\(W:G\) 光滑，不删除原零集缺陷，也不对跨零的 \(B_0\) 作经典微分。对非负紧支光滑 \(\phi\)，其局部式保留
\[
 [\int e\phi]_{a}^{b}+\nu\int\phi\,d\mu_G
 =\int e(\phi_t+u\cdot\nabla\phi+\nu\Delta\phi)
 +\int\phi\{-(B_0-W):N-(LW):G+2\nu\nabla W:\nabla G\}.
 \tag{VR.3}
\]

## 2. 归一化参考的导数

在光滑矩阵场 \(C\) 的 \(m=|C|>0\) 区域，设 \(W=C/m\)、\(R=G-C\)、\(\alpha=W:R\)、\(\Pi_WZ=Z-(W:Z)W\)。记 \(LC=-K\)，直接微分给
\[
 LW=-\Pi_WK/m+2\nu\nabla\log m\cdot\nabla W+\nu|\nabla W|^2W.
 \tag{VR.4}
\]
因此 VR.2 右边等于 \(S_{\rm ref}+D_{\rm ref}\)，其中
\[
 S_{\rm ref}=-[B_0-W-\Pi_WR/m]:K-(B_0-W):(N-K),
 \tag{VR.5}
\]
\[
 D_{\rm ref}=\nu(m-\alpha)|\nabla W|^2+2\nu\nabla W:\nabla R
 -2\nu\sum_j(\partial_j\log m)(\partial_jW:R).
 \tag{VR.6}
\]
若 \(C=\nabla v\) 来自另一实际 NS 解，则 \(LC=-N_C+(u-v)\cdot\nabla C\)，\(N_C=C^2+\nabla^2p_C\)。源项另含不可省略的
\(-\Pi_WR:((u-v)\cdot\nabla C)/m\)。其余两项为
\(-[B_0-W-\Pi_WR/m]:N_C\) 和
\(-(B_0-W):(CR+RC+R^2+\nabla^2(p-p_C))\)。只有空间仿射参考才直接退回 AH 已有公式。

取完全匹配的 \(C=G\)，仅在 \(q>0\) 的光滑区域核对：\(e=0\)、\(R=0\)、\(S_{\rm ref}=0\)，但是
\[
 D_{\rm ref}=\nu q|\nabla B|^2.
 \tag{VR.7}
\]
新增导数项抵消全部原方向耗散。因此不能把它当成随相对误差消失的小余项。这里不把该非零区域核算扩张成关于所有参考方法的不可能性定理。

## 3. 改成相对方向耗散后的径向项

在 \(q,m>0\) 上，\(e=q|B-W|^2/2\)。配方给
\[
 Le+\nu q|\nabla(B-W)|^2
 =S_{\rm ref}+\nu e|\nabla W|^2
 +2\nu(B:\nabla W)\cdot(\nabla q-q\nabla\log m).
 \tag{VR.8}
\]
跨 G 零集的分布版本须保留原 \(\nu\zeta_G\)；用 \(\nabla q-q\nabla\log m\) 解释乘积，而不假设 \(\nabla\log q\) 可积。相对方向耗散不是原 \(\mu_G\)。例如径向项的一个 Young 上界需要额外积分
\[
 \int\phi\,\frac{|\nabla q-q\nabla\log m|^2}{q},
 \tag{VR.9}
\]
因为其绝对值至多为该密度乘 \(\epsilon\nu\)，再加 \((2\nu/\epsilon)e|\nabla W|^2\)。GD 只有带 \(d(G)^2/q^2\) 因子的径向控制，不提供 VR.9。它仍是 AH 已定位的缺口。若 C 有零点，应先用 \(C/\sqrt{|C|^2+\delta^2}\)，另算导数和极限，不能设置零点值后略去这些项。

所有上述参考导数与输运差在 NS 缩放下都是四阶密度，\(r^{-1}\int_{Q_r}\) 后仍临界。没有得到新的尺度小因子、可求和余项或同解参考构造。主任务与 variable_reference_check 分别复算，并全文读回 AH、MA；这是参与式 AI 核算，不是新定理的充分查新或真人审稿。保留本记录，停止无新增控制的同类改写。
