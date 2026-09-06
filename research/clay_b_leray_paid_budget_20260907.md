# Clay B：Leray 投影与已支付的随机均值预算

2026-09-07。内部研究记录，不是新研究小节或发布冻结。
状态：本轮投影预检已完成推导，独立审读另见配套记录；G、R.216--217、一般三维正则性 OPEN；NOT CLAY。

## 1. 这一步改变了什么

完整投影没有产生新的正则性机制：它精确返回 NS 方程。
但“协方差梯度源没有任何能量级控制”也不准确。
我补全平均位移和被动均值的导数预算，得到原始协方差源的
\(L^{4/3}_{t,x}\) 界，以及独立乘积投影的能量类和 \(L^4_{t,x}\) 界。
这些是下文的直接先验推导，不声称新颖性；它们没有完成指定中心合同 G。

另一项实质修正是：不能从漂移光滑，推断扩散标签均值的 Jacobian
始终可逆。这里所有已支付预算都不使用该逆矩阵。

本轮目标原本是找到足以进入 G、且比原有临界应变假设更弱的真实输入。
结果没有达到这个目标。因此停止“仅靠完整投影消去就闭合”的支线，
不把已知重写包装为新 release，也不重复交接上一小节。

## 2. 固定父解与投影恒等式

取固定正黏性 \(\nu\)，固定三维环面上的无外力、光滑、零均值 NS 父解
\(u\)，仅在 \(0\le t\le T<T_*\) 上推导。
常均值的 Galilean 归一化沿用合同 G；最终问题不限制初值均值。
常数可以依赖固定环面。所有向量/矩阵范数采用欧氏/Frobenius 范数。

令 \(\Gamma=\partial_t+u\cdot\nabla-\nu\Delta\)，
\(G_{ij}=\partial_j u_i\)，\(P\) 为保留零 Fourier 模态的周期 Leray 投影。
矩阵 G 与问题合同 G 不同。沿用 CG.1--7 的同噪声构造，记
\(\bar A=\mathbb E A^\omega=x+\ell\)，\(M=\nabla\bar A\)，
\(N=\mathbb E[u_0(A^\omega)]\)，\(F=H_1(t,x,x)\)，
\(c=C_1(t,x,x)\)，\(m=M^TN\)。于是

\[
 \Gamma\ell=-u,\quad \Gamma M=-MG,\quad \Gamma N=0,\quad
 \Gamma F+G^TF=0,\quad F=m+c,\quad PF=u.
 \tag{LP.1}
\]

初值为 \(\ell=0,M=I,N=F=u_0,c=0\)。
随机表示只在已存在的光滑区间使用，不移植任意弱解或奇点终端版本。
[Constantin--Iyer，v4，第 3--4 节](https://arxiv.org/html/math/0511067v4)
是表示的原始来源；当前协方差记号来自本地 CG 记录。

设 \(\mathcal L_u f=u\cdot\nabla f+G^Tf\)。
若 \(f=Pf+\nabla q\)，逐分量乘积法则给

\[
 \mathcal L_u\nabla q=\nabla(u\cdot\nabla q),\qquad
 P\mathcal L_u f=P\mathcal L_u(Pf),\qquad
 (\partial_t-\nu\Delta)u+P(u\cdot\nabla u)=0.
 \tag{LP.2}
\]

最后一步用 \(G^Tu=\nabla(|u|^2/2)\)。
这里消去的是输运与应变的完整组合，不是分别令投影与它们交换。
这个恒等式也是磁化变量的已知结构；
[Pooley，v3，第 2.1 节及式 (8)](https://arxiv.org/html/1601.04968v3#S2)
已经说明其与 NS 的关系。

定义 \(\mathcal T_i=\sum_{k,a}\partial_kM_{ai}\partial_kN_a\)。
\(\Gamma\) 的乘积法则带有负的二阶交叉项，所以

\[
\begin{aligned}
 (\Gamma+G^T)m&=-2\nu\mathcal T,&
 (\Gamma+G^T)c&=+2\nu\mathcal T,\\
 (\partial_t-\nu\Delta)v+P\mathcal L_uv&=-2\nu P\mathcal T,& v&=Pm,\\
 (\partial_t-\nu\Delta)r+P\mathcal L_ur&=+2\nu P\mathcal T,& r&=Pc,\quad u=v+r.
\end{aligned}
\tag{LP.3}
\]

相加只给 (LP.2)。相反源项不意味着各自的应变功非正。

局部化也不能略去投影/压力。对任意光滑时空截止 \(\chi\)，直接乘原方程得

\[
\begin{split}
 (\partial_t+u\cdot\nabla-\nu\Delta)(\chi u)+\nabla(\chi p)
 &=(\partial_t\chi+u\cdot\nabla\chi-\nu\Delta\chi)u\\
 &\quad-2\nu\sum_k(\partial_k\chi)\partial_ku+p\nabla\chi,\qquad
 \nabla\cdot(\chi u)=u\cdot\nabla\chi .
\end{split}
\tag{LP.4}
\]

再投影仍须保留右侧及 \([P,\chi]\)；梯度消去没有支付局部压力功。
本轮没有把 (LP.4) 接成 G 的移动球预算。

## 3. 速度的非临界时间可积界

以下把使用的先验界直接重推，以区别“光滑区间内有限”与
“上界只依赖固定初值、黏性和有限时间”。
设 \(E=\|u_0\|_2^2\)，\(Y=\|\nabla u\|_2^2\)，\(Z=\|\Delta u\|_2^2\)。
若 \(E=0\)，解为零；下文假定 \(E>0,T>0\)。
基本能量给 \(D=\int_0^T Y\le E/(2\nu)\)。
对原 NS 测试 \(-\Delta u\)，用周期 Sobolev、插值和 Young 得
\(Y'+\nu Z\le C\nu^{-3}Y^3\)。
具体非线性界为
\(C\|\nabla u\|_2^{3/2}\|\Delta u\|_2^{3/2}
 \le(\nu/2)Z+C\nu^{-3}Y^3\)。

对任意常数 \(b>0\)，除以 \((b+Y)^2\) 后时间积分：

\[
 I_b:=\int_0^T\frac{Z}{(b+Y)^2}
 \le \frac1{\nu b}+\frac{CE}{\nu^5}.
 \tag{LP.5}
\]

导数项是 \((-1/(b+Y))'\)，端点贡献上界 \(1/b\)；
这一运算不假设 \(Y\) 一致有界。
零均值 Sobolev 给
\(\|u\|_\infty\le CY^{1/4}Z^{1/4}\)。
依次用时间 Hölder 指数 \(4,4/3\) 和 \(3,3/2\)，得到

\[
 L:=\int_0^T\|u\|_\infty
 \le C I_b^{1/4}D^{1/4}(bT+D)^{1/2}
 \le C\left(\frac E{\nu^2}+\sqrt{\nu T}\right)=:L_* .
 \tag{LP.6}
\]

末步可取 \(b=E/(\nu T)\)，再用加权 Young：
交叉项为 \(E^{1/2}T^{1/4}\nu^{-3/4}\)，
等于 \((E/\nu^2)^{1/2}(\sqrt{\nu T})^{1/2}\)。
这是非临界 \(L^1_tL^\infty_x\)，不是 Serrin 的 \(L^2_tL^\infty_x\)。
推导的既有来源是
[Constantin，arXiv v1，第 7 节与 Appendix A](https://arxiv.org/html/math/0005116#S10)；
本节没有提出一个新的 NS 正则性准则。

## 4. 两个均值的完整导数预算

由 \(\Gamma\ell=-u,\ell(0)=0\) 的向量模长比较原理，
\(\|\ell\|_{L^\infty_{t,x}}\le L\le L_*\)；
由 \(\Gamma N=0\)，记 \(U=\|u_0\|_\infty\)，有
\(\|N\|_{L^\infty_{t,x}}\le U\) 及
\(\|N(t)\|_2^2+2\nu\int_0^t\|\nabla N\|_2^2=E\)。

所需的周期插值可直接积分分部证明：
对光滑向量 \(f\)，将 \(\int|\nabla f|^4\) 中一个导数移到
\(|\nabla f|^2\nabla f\) 上，用 Cauchy--Schwarz，得到
\(\|\nabla f\|_4^2\le C\|f\|_\infty\|D^2f\|_2\)。
无须假设 f 零均值；周期 Fourier 恒等式给
\(\|D^2f\|_2=\|\Delta f\|_2\)。

测试位移方程以 \(-\Delta\ell\)：
输运项积分分部后为
\(-\int\partial_i u_j\,\partial_j\ell_a\,\partial_i\ell_a\)。
其绝对值不超过 \(CL_*Y^{1/2}\|D^2\ell\|_2\)；
外源项不超过 \(E^{1/2}\|D^2\ell\|_2\)。Young 后得

\[
 \|\nabla\ell(t)\|_2^2+\nu\int_0^t\|D^2\ell\|_2^2
 \le C\left(\frac{Et}{\nu}+\frac{L_*^2 E}{\nu^2}\right)
 \le B_\ell .
 \tag{LP.7}
\]

这里 \(B_\ell=C(ET/\nu+L_*^2E/\nu^2)\)。
它与 Constantin 的位移 K-bound 一致；不能把时间积分二阶界
写成每个时刻的二阶界，更不给 \(M^{-1}\) 或 \(\nabla\ell\) 的最大值界。

对 N 作完全相同的测试，没有外源项。
保留初始梯度 \(A_0=\|\nabla u_0\|_2^2\)，得到

\[
 \|\nabla N(t)\|_2^2+\nu\int_0^t\|D^2N\|_2^2
 \le A_0+\frac{CU^2}{\nu}\int_0^tY
 \le A_0+\frac{CU^2E}{\nu^2}=:B_N .
 \tag{LP.8}
\]

因此不能只使用 N 的最低阶能量界后就宣布源只在 \(L^1\)。
应用刚才的有界函数插值，再对时间积分：

\[
 \|\nabla\ell\|_{L^4_{t,x}}^4\le\frac{CL_*^2 B_\ell}{\nu},
 \qquad
 \|\nabla N\|_{L^4_{t,x}}^4\le\frac{CU^2 B_N}{\nu}.
 \tag{LP.9}
\]

这些界一致于 \(T\) 逼近一个有限候选 \(T_*\)，右侧取有限 \(T_*\) 的上界即可；
这不是声称 u、随机形变或原始 F 已有光滑终端迹。

## 5. 源与投影乘积究竟支付到了哪里

逐点 \(|\mathcal T|\le |D^2\ell||\nabla N|\)；
时空 Hölder 指数 \(2,4\) 给

\[
 \|\mathcal T\|_{L^{4/3}_{t,x}}
 \le (B_\ell/\nu)^{1/2}(CU^2B_N/\nu)^{1/4}.
 \tag{LP.10}
\]

较弱的 \(L^1_{t,x}\) 也可由两项 \(L^2\) 相乘得到。
但是 P 不能在 \(L^1_x\) 强端点直接作为有界算子使用。
本轮采用 \(4/3>1\)，合法得到相同类型的 \(P\mathcal T\) 界。

因为 \(m=N+(\nabla\ell)^TN\)，
\(\|m(t)\|_2\le E^{1/2}+U B_\ell^{1/2}\)。
空间微分给三个完整项
\(\nabla N,\ (D^2\ell)^TN,\ (\nabla\ell)^T\nabla N\)，
最后一项由两项时空 \(L^4\) 控制。故

\[
 m,\ v=Pm\in L^\infty_tL^2_x\cap L^2_tH^1_x\cap L^4_{t,x},
 \qquad
 r=Pc=u-v\in L^\infty_tL^2_x\cap L^2_tH^1_x .
 \tag{LP.11}
\]

其中 m 的 \(L^4\) 用 \(\|N\|_\infty\) 和 (LP.9)，
P 在 \(L^4_x\) 有界；不能据此声称 \(r\) 也在 \(L^4\)。
亦不能把投影后的 c 的界变成原始 c 的界；P 看不见其梯度分量。
(LP.11) 的 r 界使用原解能量，不是对未知非线性系统的独立闭合证明。

这些范数没有达到所需缩放。
在局部 NS 缩放 \(u_\lambda=\lambda u(\lambda x,\lambda^2t)\) 下，
\(\ell_\lambda=\lambda^{-1}\ell(\lambda x,\lambda^2t)\)，
\(N_\lambda=\lambda N(\lambda x,\lambda^2t)\)，所以

\[
 \mathcal T_\lambda=\lambda^3\mathcal T(\lambda x,\lambda^2t),
 \qquad
 \|\mathcal T_\lambda\|_{4/3}=\lambda^{-3/4}\|\mathcal T\|_{4/3}.
 \tag{LP.12}
\]

范数比较取对应缩放区域，不把局部缩放误称固定周期胞的自同构。
力的各向同性时空临界指数为 \(5/3\)，不是 \(4/3\)。
在抛物柱体 \(Q_R\) 上，相应归一化量是
\(R^{-3/4}\|\mathcal T\|_{L^{4/3}(Q_R)}\)，
其 \(4/3\) 次方为 \(R^{-1}\int_{Q_R}|\mathcal T|^{4/3}\)。

有限总积分不给这个归一化量在每个指定中心趋零。
仅就范数蕴含而言，
\(f(x,t)=(|x|^2+|t|)^{-3/2}\) 在 \(B_1\times(-1,0)\) 属于 \(L^{4/3}\)，
而小柱体上的上述归一化量保持正的常数：
代换 \(x=Ry,t=R^2s\)，积分正好乘 R。
这只是函数空间例子，不是 NS 解、实际协方差源或同一父解的反例。
因此本轮只记录“尚无 G 桥梁”，不证明所有结构改进均不可能。

## 6. 两个不可借用的捷径

第一，设某区间 M 确实可逆，定义 \(\tilde v=M^{-T}F\)。
由 (LP.1) 的乘积公式直接得到

\[
 \tilde v=N+M^{-T}c,\qquad
 \Gamma\tilde v
 =2\nu M^{-T}\sum_k(\partial_kM)^T\partial_k\tilde v .
 \tag{LP.13}
\]

它是虚速度，不是被动 N；黏性耦合项不能删掉。
[Constantin 的作者修订稿，2000-09-26](https://web.math.princeton.edu/~const/xlnsF.pdf)
包含这一 Eulerian--Lagrangian 结构。M 是平均标签导数，
不是每条随机逆流的导数；逐路径可逆不保证平均矩阵可逆。

[Montgomery-Smith--Pokorný，v2，Theorem 1.1](https://arxiv.org/html/math/0106113)
给出光滑、紧支撑、无散的三维给定漂移，使扩散标签后来无光滑逆。
它否定“光滑漂移自动支付全时逆矩阵”，不构成无外力周期 NS 反例。
本轮不使用其非严格概率讨论来推导正则性。

第二，真实磁化方程中 \(G^TF\) 的模长功没有确定符号。
把它换成 \((\nabla F)^TF=\nabla(|F|^2/2)\)，才得到不同的有最大值原理的模型。
真实 NS 写成这个模型时，右端必须恢复

\[
 (\partial_t+u\cdot\nabla-\nu\Delta)F
       +\tfrac12\nabla|F|^2
 =(\nabla(F-u))^TF .
 \tag{LP.14}
\]

这个额外力没有由上述低阶预算支付其最大值。
[Pooley，第 3 节 Lemma 8 与第 4 节式 (22)--(23)](https://arxiv.org/html/1601.04968v3#S4)
明确区分了模型与原方程。
弱解反向表示也不能自动导入：其一般能量级反向陈述只对无散测试成立，
而完整反向定理另有临界 Sobolev 假设；本轮不采用该外部定理的未读证明。

## 7. 路线决定与记录边界

(LP.7)--(LP.11) 是更完整的已付范数清单，不是更大的正则解类。
没有排除真实 NS 奇点，没有证明能量原子必在奇点生成，
也没有降低 G、R.216--217 或一般三维全局问题的未证输入。

接下来先作有界策略复评，不预先认可下一条正面证明路线。
候选必须明确命中 G 的指定中心好尺度或直接排除首次奇点，
指出所用真实 NS 动力学结构、已付输入和不同于现有重写的增量。
本地已有涡量方向扩散、应变几何和固定历史路线，不能把它们当成未查的新方向。
若候选只换投影、重启时间、相关系数或临界范数记号，停止而不续写相邻版本。
只有证据表明存在值得继续的不同机制，才开展下一项推导。

本轮按 Deep Research 流程完成了有界原著检索、反证来源核查及记录；
文献台账注明版本与实际阅读范围，独立审读不冒充外部同行评审。
没有数值仿真、DGX、科学附图、读者 HTML/PDF 或累计 recap。
内部预检不创建发布冻结。最近已交接小节的记录不变；
未来真正完成的研究冻结只向固定发布任务交接一次。
