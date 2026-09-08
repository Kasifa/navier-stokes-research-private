# 不变密度的物质导数：联合抵消与剩余耗散成本

2026-09-08。IDC，PRIVATE_CORE；这是 [ID 候选](clay_b_invariant_density_entropy_20260908.md) 的一次有界后续核算，不另计完成小节。结论不是简单的“压力又出现，所以失败”：合并确实消去了粗估中的显式高阶导数，并有一个低幅非局部抵消；但仍未得到任意数据的临界控制。完成本次核算后，停止在没有额外控制的情况下继续改写这条直接不变密度支路。原 NS / PF 指定中心联合好尺度仍 OPEN / NOT CLAY。

## 1. 沿用的对象与常数模式

沿用 ID 的同一无外力光滑周期 NS 轨道、\(0<a<b<T_*\)、固定 \(\kappa>0\)、\(0<\alpha\le1\)。省略 \(\kappa\) 下标：\(q=(|G|^2+\kappa^2)^{1/2}\)、\(\Phi=q-\kappa\)、\(B=G/q\)、\(\Sigma=\operatorname{sym}B\)、\(K=I+\alpha Q(\Sigma\,\cdot)\)、\(K\rho=1\)，\(Q=\Delta^{-1}\operatorname{divdiv}\) 采用 ID 的正 Fourier 符号。令
\[
 D_t=\partial_t+u\cdot\nabla,\quad R_{\rm test}=D_t+\nu\Delta,
 \quad N=G^2+H,\quad H=\nabla^2p,\quad D_tG=\nu\Delta G-N.
 \tag{IDC.1}
\]
这里 \(\operatorname{tr}N=0\)。所有未标区域的空间积分均在整个周期胞；时间积分保留 \([a,b]\)。

定义 \(\mathcal C_uF=[u\cdot\nabla,Q]F\)。由无散性和 \(Q\) 删除常数模式，\(\int\mathcal C_uF=0\)。\(K\) 保持均值，但一般 \(K1\ne1\)；\(K^*1=1\)。不能把这两个性质混为一谈。直接微分 \(K\rho=1\) 得
\[
 \begin{aligned}
 K D_t\rho&=-\alpha Q(\rho D_t\Sigma)-\alpha\mathcal C_u(\rho\Sigma),\\
 K R_{\rm test}\rho
 &=-\alpha Q\left(\rho R_{\rm test}\Sigma
 +2\nu\sum_j\rho_j\Sigma_j\right)-\alpha\mathcal C_u(\rho\Sigma).
 \end{aligned}
 \tag{IDC.2}
\]
两个交换子都是负号；\(D_t\rho\)、\(R_{\rm test}\rho\) 的均值均为零。只因 \(u\) 无散，并不能删掉交换子的非零频率。

## 2. 归一化梯度的完整链式法则

令 \(P_j=\partial_jG\)，定义矩阵映射的导数
\[
 \mathcal J X=D_G\Sigma[X]
 =q^{-1}\{\operatorname{sym}X-\Sigma(B:X)\},
 \qquad
 \mathcal J^*W=q^{-1}\{W-B(\Sigma:W)\}\quad(W=W^T).
 \tag{IDC.3}
\]
对实际兼容梯度的空间变化，二阶链式项为
\[
 \begin{aligned}
 \Xi&=\sum_jD_G^2\Sigma[P_j,P_j]\\
 &=q^{-2}\sum_j\{-2(B:P_j)\operatorname{sym}P_j
 -|P_j|^2\Sigma+3(B:P_j)^2\Sigma\}\\
 &=-2\nabla\log q\cdot\nabla\Sigma-\frac Dq\Sigma,
 \qquad D=\sum_j\frac{|P_j|^2-(B:P_j)^2}{q}.
 \end{aligned}
 \tag{IDC.4}
\]
最后一式用 \(B:P_j=\partial_jq\) 和 \(q\Sigma_j=\operatorname{sym}P_j-\Sigma(B:P_j)\)。因此
\[
 D_t\Sigma=-\mathcal JN+\nu\Delta\Sigma-\nu\Xi,
 \qquad R_{\rm test}\Sigma=-\mathcal JN+2\nu\Delta\Sigma-\nu\Xi.
 \tag{IDC.5}
\]
完整各项迹零；单独拆开的 \(H\) 或 \(G^2\) 部分不一定迹零。

## 3. 有效乘子与代表选择

对状态泛函 \(\mathcal E(G)=\int\rho(G)\Phi(G)\)，令
\[
 \chi=K^{-*}\Phi,\qquad W=Q^*\chi,\qquad s=\Sigma:W,
 \qquad M=\rho\{B-\alpha\mathcal J^*W\}.
 \tag{IDC.6}
\]
对兼容无散变化 \(\delta G=\nabla\delta u\)，\(\delta\rho=-\alpha K^{-1}Q(\rho\mathcal J\delta G)\)。于是
\[
 \delta\mathcal E=\int M:\delta G.
 \tag{IDC.7}
\]
这是对权重变化的完整变分，不能只取 \(\rho B\)。在这个约束空间，\(M\) 可加任意标量场 \(\lambda I\)，也可加一个光滑周期 Hessian，而不改变与兼容无散梯度的全域配对。

必须用完整演化判断抵消：\(H\) 单独不是许可的迹零变化。改成 \(M+\lambda I\) 时，\(\int M:H\) 改变 \(-\int\lambda f\)，\(\int M:G^2\) 改变 \(+\int\lambda f\)，\(f=\operatorname{tr}G^2\)。故对标量代表选择，联合 \(N\) 配对才不变。任意 Hessian 代表还会重新分配输运项，不能固定其余项后单改乘子。下文始终使用 IDC.6 的确定代表。

## 4. 全局联合式与真正消去的项

由 IDC.2 和 IDC.3，对 \(\mathcal E\) 作物质导数后有
\[
 \mathcal E'=\int M:D_tG-\alpha\int\chi\mathcal C_u(\rho\Sigma),
 \quad
 \mathcal E'+\nu\int\nabla M:\nabla G
 =-\int M:N-\alpha\int\chi\mathcal C_u(\rho\Sigma).
 \tag{IDC.8}
\]
这里的 \(\int\nabla M:\nabla G\) 尚无已证正号；IDC.7 也不证明泛函在任意幅度上凸。

另一种保留原 \(D\) 的等价式来自将 IDC.5 代回 ID 的加权熵：
\[
 \begin{aligned}
 \mathcal E'+\nu\int\rho D
 ={}&-\int M:N-\alpha\int\chi\mathcal C_u(\rho\Sigma)+\mathcal V,\\
 \mathcal V={}&\alpha\nu\int\rho W:\Xi
 +2\alpha\nu\int\rho\nabla W:\nabla\Sigma.
 \end{aligned}
 \tag{IDC.9}
\]
关键步骤是把 \(-2\alpha\nu\int W:(\rho\Delta\Sigma+\sum_j\rho_j\Sigma_j)\) 整体分部积分。这样全局黏性块不再显式含 \(G_t\)、\(\Delta G\) 或 \(\nabla\rho\)，不能继续把之前的 \(\|\rho G_t/q\|_2\) 粗界当成该联合式必须付出的成本。但 \(W\) 仍是非局部量，所得式子尚不是基本能量估计。

再用 IDC.4，得到精确重排
\[
 \mathcal E'+\nu\int\rho\left(1+\frac{\alpha s}{q}\right)D
 =-\int M:N-\alpha\int\chi\mathcal C_u(\rho\Sigma)
 +2\alpha\nu\int\rho q\nabla(W/q):\nabla\Sigma,
 \qquad 1+\frac{\alpha s}{q}=2-\frac{\kappa+\chi}{q}.
 \tag{IDC.10}
\]
最后的系数等式来自 \(K^*\chi=\chi+\alpha s=\Phi\)，不赋予它正号。实际有
\[
 D-q|\nabla B|^2=\frac{\kappa^2}{q^3}|\nabla q|^2\ge0,
 \qquad q|\nabla\Sigma|^2\le D,
 \qquad
 \left|2\alpha\nu\int\rho q\nabla(W/q):\nabla\Sigma\right|
 \le\delta\nu\int\rho D+\frac{\alpha^2\nu}{\delta}
 \int\rho q|\nabla(W/q)|^2
 \tag{IDC.11}
\]
对任意 \(\delta>0\) 成立。还缺 \(\int\rho q|\nabla(W/q)|^2\) 的统一控制和黏性整体的强制性；不能先把未知符号系数视为正，再宣称已经吸收。这只是定位这一吸收方案的缺项，不是对其他带符号机制的不可能性证明。

## 5. 指定中心的局部式没有消失

取任意光滑非负周期截止 \(\eta(x,t)\)，定义 \(\mathcal E_\eta=\int\rho\eta\Phi\)、\(\chi_\eta=K^{-*}(\eta\Phi)\)、\(W_\eta=Q^*\chi_\eta\)、\(M_\eta=\rho(\eta B-\alpha\mathcal J^*W_\eta)\)。同样的计算给
\[
 \begin{aligned}
 [\mathcal E_\eta]_a^b+\nu\iint\rho\eta D
 ={}&-\iint M_\eta:N-\alpha\iint\chi_\eta\mathcal C_u(\rho\Sigma)\\
 &+\alpha\nu\iint\rho W_\eta:\Xi
 +2\alpha\nu\iint\rho\nabla W_\eta:\nabla\Sigma\\
 &+\iint\rho\Phi R_{\rm test}\eta
 +2\nu\iint\Phi\nabla\rho\cdot\nabla\eta.
 \end{aligned}
 \tag{IDC.12}
\]
所有积分仍在全周期胞。即使 \(\eta\) 支撑于指定小球，\(\chi_\eta,W_\eta,M_\eta\) 一般也不紧支，非局部尾部不能丢掉。压力以 \(N=G^2+H\) 原样保留，并非删除；因此不再额外添加 ID.17 的压力转换边界项。时间端点和两项显式截止成本都保留。全局 \(L^2\) 密度界依然不提供指定中心的统一正下界。

## 6. 一个真实但仅限低幅的抵消

固定光滑无散 \(v\)，令 \(Z=\nabla v\)、\(G=\varepsilon Z\)、\(u=\varepsilon v\)、\(h=|Z|^2\)、\(S=\operatorname{sym}Z\)。这是对 NS 向量场和泛函的固定时间片展开，不另造实际轨道族或终端例子。\(QS=0\) 来自兼容性。固定 \(\kappa>0\) 下，Taylor 展开及小幅逆算子给
\[
 \begin{aligned}
 \rho&=1+\frac{\alpha\varepsilon^3}{2\kappa^3}Q(hS)+O(\varepsilon^4),\\
 \chi&=\frac{\varepsilon^2h}{2\kappa}+O(\varepsilon^3),\qquad
 M=\frac{\varepsilon Z}{\kappa}
 -\frac{\alpha\varepsilon^2}{2\kappa^2}Q^*h+O(\varepsilon^3),\\
 \mathcal E(\varepsilon Z)&=\frac{\varepsilon^2}{2\kappa}\int h
 -\frac{\varepsilon^4}{8\kappa^3}\int h^2+O(\varepsilon^5).
 \end{aligned}
 \tag{IDC.13}
\]
这里不是一般的 \(\rho-1=O(\varepsilon)\)：线性归一化梯度被 \(Q\) 消去。二次乘子 \(Q^*h\) 是 Hessian，对兼容无散梯度的全域配对为零。所有余项可在固定有限阶光滑范数中解释，常数依赖 \(v,\kappa,\alpha\)；不声称基本能量一致或 \(\kappa\downarrow0\) 一致。

令 \(-\Delta p_0=f_0=\operatorname{tr}Z^2\)、\(H_0=\nabla^2p_0\)、\(N_0=Z^2+H_0\)。直接用 \(\nabla(v\cdot\nabla v)=Z^2+v\cdot\nabla Z\)，有
\[
 QN_0=-Q(v\cdot\nabla Z),\qquad
 \mathcal C_u(\rho\Sigma)=\frac{\varepsilon^2}{\kappa}QN_0+O(\varepsilon^4).
 \tag{IDC.14}
\]
因为 \(Q\nabla(v\cdot\nabla v)=f_0\)、\(QH_0=-f_0\)，无需引入额外动力学假设。于是 IDC.8 中来自二次 Hessian 乘子的 \(+\alpha\varepsilon^4(2\kappa^2)^{-1}\int h QN_0\)，与交换子产生的对应负项精确抵消。黏性配对中该乘子的三次贡献也为零，因为 \(\Delta Z\) 仍是兼容无散梯度。这里只恢复低幅的梯度能量结构；不是任意幅度上的凸性、耗散正号或临界尺度增益。

## 7. 判断与停止条件

本次完成了 ID 留下的物质导数问题，并修正“逐项检查压力”不足以判断联合抵消的认识。新核算减少了粗导数成本，确认了一个低幅抵消；但全局与局部式仍缺联合源控制、黏性强制性、加权余项控制和指定中心密度非退化，未补上 PF 的自动联合好尺度。

因此本轮后停止这条直接不变密度加权改写：不继续对同一组未控量反复换名字、作固定参数小例子或增加审计数量。若将来出现能处理这些缺项的实质估计，才重新开启。下一研究入口回到同一原 NS 的指定中心前终端问题，先从现有问题清单选择一个不同的具体动力学输入；本轮没有选定替代估计，不把方向意向写成已有研究结果。

主任务全文重读 ID 并独立推导上述公式。variable_reference_check 独立推导物质导数、链式项、联合黏性简化及局部式；ma_freeze_review 独立推导约束变分、低幅展开并复核 IDC.14 抵消。两者均是参与式 AI 核算；最终稿读回范围另记检查点。本轮没有外部文献新断言、仿真、DGX、图表或公开产物，不新建 release、不交接发布、不修改既有冻结源。记录不证明新颖性或真人同行评审通过。
