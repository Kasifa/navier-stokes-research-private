# 正对称时空张量：NS 动力学与行列式增益检查

2026-09-08。内部方法检查，记为 PTS。这里只检查常密度 NS 的两个自然四维张量，不提出新的正则性准则，不另立研究小节或发布版本。

结论：完整黏性张量准确保留动量方程，但使它半正定需要额外的压力与应变上确界估计。删去黏性后的张量有一个真实的二次散度抵消，不过任意无散时间族及其 Poisson 压力都满足它。对这两个张量，直接的全域平均行列式不等式已由代数成立，不能当作新的 NS 动力学估计。局部边界机制及其他张量构造并未被排除。

分类：文献方法 `LITERATURE`；下列光滑框架恒等式与代数结论 `PROVED`（本地推导）；新的无条件临界估计、指定中心好尺度与 Clay 问题均 `OPEN / NOT CLAY`。本记录使用 AI 推导、文献核对与独立 AI 复核，不代表真人同行评审或原创性认定。

## 1. 研究对象与文献接口

取固定平坦三维环面 \(\Omega=\mathbb T^3\)，有限时间区间 \(I=(a,b)\Subset(0,T_*)\)，黏性 \(\nu>0\)。先在 \(\overline I\times\Omega\) 上光滑的原方程解中计算：

\[
 \partial_tu+\operatorname{div}_x(u\otimes u)+\nabla p=\nu\Delta u,
 \qquad\operatorname{div}u=0,\qquad\int_\Omega p(t,x)\,dx=0. \tag{PTS.1}
\]

\(T_*\) 可以是候选首次奇异时刻；本记录不预设趋近它时的光滑范数有统一界。空间压力为规范 Poisson 解，\(-\Delta p=\partial_i\partial_j(u_i u_j)\)。记 \(D=(\nabla u+\nabla u^T)/2\)，所以 \(\operatorname{tr}D=0\) 且 \(2\operatorname{div}D=\Delta u\)。时空变量为 \(y=(t,x)\)，\((\operatorname{Div}A)_\alpha=\sum_{\beta=0}^3\partial_{y_\beta}A_{\alpha\beta}\)。公式在固定单位下书写，不把四维各向同性缩放当作 NS 抛物缩放。

Serre 的补偿可积性使用半正定、对称、逐行无散度张量。其周期定理控制 \(\langle(\det A)^{1/(d-1)}\rangle\)；有界凸域版本保留法向迹，允许散度为测度时还计入其总变差。四维对应指数 \(1/3\)。出处为 *Divergence-free positive symmetric tensors and fluid dynamics*，[arXiv v2，定理 2.1、2.2，§4.1、§5](https://arxiv.org/html/1705.00331v2)。[正式发表记录](https://www.numdam.org/item/AIHPC_2018__35_5_1209_0/)为 *Ann. Inst. H. Poincaré C* 35(5), 2018, 1209–1234，DOI 10.1016/j.anihpc.2017.11.002。

文献适用条件不能省略：空间周期不等于时空周期；有限时间 NS 解不能未经端点检查就周期延拓。本文不重新证明最优输运或周期 Monge–Ampère 存在性，也不把光滑标量测试自动推广为任意非光滑凸势。

## 2. 完整黏性张量：正性恰好要求什么

定义

\[
 T_\nu=\begin{pmatrix}1&u^T\\u&u\otimes u+pI_3-2\nu D\end{pmatrix}.
 \tag{PTS.2}
\]

由 PTS.1，\(\operatorname{Div}T_\nu=0\)。第一行为质量约束，其余三行为完整黏性动量方程。对可逆矩阵

\[
 L=\begin{pmatrix}1&0\\u&I_3\end{pmatrix},\qquad
 T_\nu=L\begin{pmatrix}1&0\\0&pI_3-2\nu D\end{pmatrix}L^T,\qquad\det L=1,
 \tag{PTS.3}
\]

得到精确等价

\[
 T_\nu\succeq0\quad\Longleftrightarrow\quad pI_3-2\nu D\succeq0.
 \tag{PTS.4}
\]

若 PTS.4 在整个空间切片成立，则取迹给 \(3p\ge0\)。压力零均值迫使 \(p=0\)，随后半正定矩阵 \(-2\nu D\) 的迹为零，故 \(D=0\)。周期积分分部给 \(\int|\nabla u|^2=2\int|D|^2=0\)，所以速度空间常数。若每个时刻都如此，原 NS 再给其时间常数。这不是奇异性结论，只说明未平移规范压力的原张量，除常数解外不能整体半正定。

可以改用压力规范平移 \(P=p+c(t)\)：

\[
 T_{\nu,c}=T_\nu+\operatorname{diag}(0,c(t)I_3),\qquad
 \operatorname{Div}T_{\nu,c}=0.
 \tag{PTS.5}
\]

没有 \(c'(t)\) 项，因为平移只进入空间应力块。最小逐时平移为

\[
 c_{\min}(t)=\operatorname*{ess\,sup}_{x\in\Omega}
       \{2\nu\lambda_{\max}(D(x,t))-p(x,t)\},\qquad
 T_{\nu,c}\succeq0\ \Longleftrightarrow\ c(t)\ge c_{\min}(t).
 \tag{PTS.6}
\]

\(c_{\min}\ge0\)：\(\lambda_{\max}(D)\ge0\)，而周期零均值压力不可能处处严格正。光滑紧时间区间上此量有限，并可选有界平移；这不提供趋近 \(T_*\) 的统一时间可积性。基本能量控制 \(u\in L^\infty_tL^2_x\)、\(\nabla u\in L^2_{t,x}\)，目前没有从这些输入推出 PTS.6 上确界成本的终端一致估计。这里没有证明该成本沿某个实际 NS 解发散，也没有声称其可积性等价于某个正则性判据。

若改用空间变化的 \(c(t,x)\)，则新增散度为 \((0,\nabla_xc)\)，不再是压力规范变换。即便用允许测度散度的版本，也要先证明该余项具有所需的总变差界。

## 3. 行列式消去了什么，仍保留了什么

令 \(S=P I_3-2\nu D\)。由 PTS.3 及 \(\operatorname{tr}D=0\)，

\[
 \det T_{\nu,c}=\det S
 =P^3-2\nu^2P|D|^2-8\nu^3\det D.
 \tag{PTS.7}
\]

显式的速度项 \(u\otimes u\) 被消去，但 \(D\) 与非局部压力仍依赖速度，不能因此说张量完全没有速度信息。若 \(S\succeq0\)，对三个特征值用算术—几何平均，得到

\[
 0\le (\det T_{\nu,c})^{1/3}\le\tfrac13\operatorname{tr}S=P,
 \qquad \int_\Omega P(t,x)\,dx=|\Omega|c(t).
 \tag{PTS.8}
\]

因此，行列式输出尚不是速度临界范数或形状耗散的下界；若想借它产生好尺度，必须另证相应的定量控制，不能把 PTS.7 的压力依赖当作已得到这种控制。

## 4. 删去黏性后，Hessian 测试确有抵消

在同一个原 NS 解上定义另一个张量，而不是更换原方程：

\[
 T_{0,c}=\begin{pmatrix}1&u^T\\u&u\otimes u+P I_3\end{pmatrix}.
 \tag{PTS.9}
\]

它满足 \(\operatorname{Div}T_{0,c}=(0,\nu\Delta u)\)，一般不逐行无散度。不过

\[
 \operatorname{Div}\operatorname{Div}T_{0,c}
 =2\partial_t\operatorname{div}u+
   \partial_i\partial_j(u_i u_j)+\Delta p=0.
 \tag{PTS.10}
\]

这意味着任意光滑、时间紧支、空间周期标量 \(\psi\) 满足

\[
 \int_{I\times\Omega}T_{0,c}:D^2_{t,x}\psi=0.
 \tag{PTS.11}
\]

也可以从 \(\int\nu\Delta u\cdot\nabla_x\psi=0\) 直接看出黏性余项的抵消。因此，仅以“不是逐行无散度”为由否定所有 Monge–Ampère 型 Hessian 测试，并不正确。

但 PTS.10–11 有更弱的真实假设：取任意光滑无散时间族 \(u(t)\)，逐时定义规范 Poisson 压力，完全不要求其满足 NS，公式仍成立。此时

\[
 \operatorname{Div}T_{0,c}=(0,R),\qquad
 R=\partial_tu+\operatorname{div}(u\otimes u)+\nabla p,
 \qquad\operatorname{div}_xR=0.
 \tag{PTS.12}
\]

标量 Hessian 测试看不到这部分无散的动量残差，因而单独使用 PTS.11 不会区分真实 NS 演化和任意无散时间族。它仍可能是其他估计的一部分；本文不证明所有补偿可积性推广均无用。

与此同时，Schur 补给

\[
 T_{0,c}\succeq0\ \Longleftrightarrow\ P\ge0,
 \qquad (\det T_{0,c})^{1/3}=P,
 \qquad\int_\Omega(\det T_{0,c})^{1/3}=|\Omega|c(t).
 \tag{PTS.13}
\]

这里正性不再要求 \(D=0\)，不能与未平移的完整黏性张量混同。

## 5. 直接全域平均输出已经由代数成立

本节只使用空间周期和有限时间区间，不假设时间周期，也不调用 Serre 定理。记 \(\langle\cdot\rangle\) 为 \(I\times\Omega\) 上归一化平均，\(m=\langle u\rangle\)，\(\bar c=\langle c\rangle\)，以及

\[
 C_u=\langle u\otimes u\rangle-m\otimes m
    =\langle(u-m)\otimes(u-m)\rangle\succeq0.
 \tag{PTS.14}
\]

因为 \(\langle D\rangle=0\)、\(\langle p\rangle=0\)，两种张量均有

\[
 \langle T_{\nu,c}\rangle=\langle T_{0,c}\rangle
 =\begin{pmatrix}1&m^T\\m&\langle u\otimes u\rangle+\bar cI_3\end{pmatrix},
 \quad\det\langle T_{\nu,c}\rangle=\det(C_u+\bar cI_3)\ge\bar c^3.
 \tag{PTS.15}
\]

对于各自满足半正定条件的平移，均有 \(\bar c\ge0\)。结合 PTS.8、13，直接得到

\[
 \langle(\det T_{\nu,c})^{1/3}\rangle
 \le\bar c\le(\det\langle T_{\nu,c}\rangle)^{1/3},
 \qquad
 \langle(\det T_{0,c})^{1/3}\rangle
 =\bar c\le(\det\langle T_{0,c}\rangle)^{1/3}.
 \tag{PTS.16}
\]

这些式子甚至不使用动量方程：任意光滑空间周期无散时间族、任意逐时零均值压力及足够大的平移就适用。换言之，若只要求这两个特定张量的“平均行列式不超过平均张量行列式”，所得事实比 NS 动力学弱，不能单独产生所需增益。这并非一般张量的行列式凹性，也不是新的补偿可积性定理。

## 6. 局部化后不能忽略的项

取光滑截止 \(\eta\ge0\)。在原 NS 解上，完整张量满足

\[
 \operatorname{Div}(\eta T_{\nu,c})=T_{\nu,c}\nabla_{t,x}\eta.
 \tag{PTS.17}
\]

其中包含时间通量，以及空间方向的速度、压力平移和黏性应力；不能只保留其中一个有利项。删去黏性时则为

\[
 \operatorname{Div}(\eta T_{0,c})=T_{0,c}\nabla\eta+\eta(0,\nu\Delta u),
 \qquad
 \operatorname{DivDiv}(\eta T_{0,c})
 =T_{0,c}:D^2\eta+2\nu\Delta u\cdot\nabla_x\eta.
 \tag{PTS.18}
\]

这里使用张量对称性以及 PTS.10。全域无权 Hessian 抵消不意味着 PTS.18 的各项分别为零。若将整个乘积 \(\eta\psi\) 作为测试，乘积法则中的所有交叉项仍须保留。

有界时空域还需要端点与侧边界的法向迹。仅因原解在每个 \(b<T_*\) 上光滑，并不能获得 \(b\uparrow T_*\) 时的统一界；也不能以四维时间周期延拓消除真实端点。本文没有建立局部带权行列式估计的严格尺度增益或可求和误差，故未否定这种进一步研究的可能。

## 7. 本轮决定与下一项研究

这次不继续重复检查 PTS.2、9 的全域行列式输出，也不为压力平移或标量 Hessian 抵消增加相邻版本。它们尚未给出从任意原初值、同一实际前终端 NS 解到指定中心联合好尺度的估计。

若之后重新采用正张量方法，必须提出不同于已核全域平均输出的具体估计，可以包括同一张量的局部带权或边界机制；还须证明它确实控制目标临界量，并估计取得正性、散度余项和局部边界的成本。仅换坐标、换压力规范或删去黏性再用 PTS.11，不满足这个要求。

下一次实质推导回到保留完整动量信息的局部带符号估计。候选式须明确所用实际输入、端点和尺度；应先检验是否比逐时 Poisson 恒等式强，再检验能否导出能量控制与小形状耗散同时成立的指定中心尺度。新的具体估计尚未确定，本记录不把探索计划计作正面结果。

## 8. 阅读、去重与核验边界

主审实际读取了 Serre v2 的定义、定理 2.1/2.2、§4.1 与 §5 的有关完整证明段落，核对正式发表元数据；未重新认证其引用的 Monge–Ampère 存在性定理。2024 年环面扩展仅用于发现检索，未采用其证明。此次不是全面文献综述，不声称穷尽查新。

内部关键词检索未找到先前同名的 Serre/补偿可积性检查；旧笔记中正定亚网格应力讨论不等于本题。相邻的能量—梯度熵、仿射压力、混合吸收和原序列压力源障碍已做过定向比较，不在本记录重写为新成果。

全部 PTS 结论为解析恒等式或基本矩阵推导。没有仿真、DGX 作业、科学图、区间证书或新反例计数。独立复核的实际范围、文件哈希和待办存于配套检查点；这份内部记录不单独创建 release，不重发历史交接，不读取或监督发布执行。
