# 负应变方向、局部锥估计与未闭合的时间控制

2026-09-08，北京时间。SC，PRIVATE_CORE。范围内解析证明与条件推论；一般三维 Navier–Stokes 正则性仍为 OPEN / NOT CLAY。不宣称新颖性或人类同行评审。

这一步不再要求完整应变接近一个固定矩阵。一个固定平面上的行列式积分恒等式，允许两个正特征值及其平面内特征方向变化。它给出局部 L2 应变估计，并把条件性正则性问题归结为几何条件失效区域上的一个时间范数。实际方程中的负特征线耗散仍不足以控制这个范数。

## 1. 对象与约定

空间为未归一化的固定 \(\mathbb T^3_{2\pi}\)，\(\nu>0\)。记
\[
 A_{ij}=\partial_j u_i,\quad S=\operatorname{sym}\nabla u,
 \quad\Omega=(A-A^\top)/2,\quad\omega=\operatorname{curl}u,
 \quad H=\nabla^2p,\quad L=\partial_t+u\cdot\nabla-\nu\Delta.
 \tag{SC.1}
\]
矩阵范数不带下标时为 Frobenius 范数；\(\|\cdot\|_{op}\) 是算子范数。空间 L2 范数除另注外取整胞。静态引理适用于所列 H1 速度；动力学只在同一光滑无外力 NS 解的相应开集推导。第 4 节另明确适当弱解的量词。

本稿使用已经核对的 SE.5、SE.11–13，并比较 SE.18 的局部化。SE 指同日的 `clay_b_strain_spectral_entropy_20260908.md`。不把 SE 的跨正负谱耗散误认为完整应变梯度耗散。

## 2. 一个允许正谱块变化的锥引理

固定单位向量 e 和 \(0<\delta\le1/2\)。在 \(e^\perp\oplus\mathbb Re\) 上定义
\[
 K_{e,\delta}=\left\{T=\begin{pmatrix}C&0\\0&-a\end{pmatrix}:
 a\ge0,\ C=C^\top,\ \operatorname{tr}C=a,\ C\ge\delta a I_2\right\}.
 \tag{SC.2}
\]
这是闭凸锥。它只固定负特征线，不固定正平面内的完整矩阵 C。对非零 T，其正特征值为 \(ta,(1-t)a\)，\(\delta\le t\le1/2\)。SE.16 给它与实无散应变波锥的非零相对间隙。不过当 \(\delta<1/2\) 时，\(K-K\) 包含正平面内的 \(\operatorname{diag}(h,-h,0)\) 波锥元；不能将逐点锥约束直接施加给 Fourier 系数。

我改用积分恒等式。取固定正交基 \(e_1,e_2,e\)，记 \(D_i=e_i\cdot\nabla\)、\(u_i=u\cdot e_i\)，并令 \(C_S\) 为 S 在 \(e^\perp\) 上的二维压缩。任意周期 H1 速度均满足
\[
 \boxed{\int\det C_S=-\frac14\int(\omega\cdot e)^2\le0.}
 \tag{SC.3}
\]
证明：固定方向的周期分部积分给
\(\int D_1u_1D_2u_2=\int D_1u_2D_2u_1\)。因此
\[
 \int\left[D_1u_1D_2u_2-\frac{(D_1u_2+D_2u_1)^2}{4}\right]
 =-\frac14\int(D_1u_2-D_2u_1)^2.
\]
先对光滑场计算，再用 H1 稠密逼近。e 不必为有理方向；没有旋转周期胞。SC.3 本身不要求无散。

**锥 L2 引理（PROVED IN STATED SCOPE）。** 设 \(S=T+R=\operatorname{sym}\nabla u\)，\(u\in H^1\) 周期，T、R 为实对称 L2 场，\(T(x)\in K_{e,\delta}\) 几乎处处。令 \(R_h\) 为 R 的二维压缩，设
\[
 \kappa=\delta(1-\delta),\quad\beta=\sqrt{1-2\kappa},\qquad
 C_\delta=\frac{1+\beta}{2\kappa}=\frac1{1-\beta}.
\]
则
\[
 \boxed{\|a\|_2\le C_\delta\|R_h\|_2\le C_\delta\|R\|_2.}
 \tag{SC.4}
\]
证明：\(\det C\ge\kappa a^2\)、\(|\operatorname{cof}C|=|C|\le\beta a\)，且实对称二维矩阵满足 \(|\det R_h|\le|R_h|^2/2\)。展开
\(\det(C+R_h)=\det C+\operatorname{cof}C:R_h+\det R_h\)，结合 SC.3 与 Cauchy–Schwarz，得到
\[
 \kappa X^2\le\beta XY+\frac12Y^2,
 \qquad X=\|a\|_2,\quad Y=\|R_h\|_2.
\]
若 Y=0 则 X=0；否则解二次不等式，用 \(\beta^2+2\kappa=1\) 即得 SC.4。a 无需零均值。这里不声称常数最优。

## 3. 近似负特征方向与完整局部误差

以下 u 无散，故 S 迹零。取局部坐标球 \(B_{2r}(x_0)\)，\(2r<\pi\)，选 \(0\le\eta\le1\) 支撑其中，在 \(B_{3r/2}\) 上为 1，\(|\nabla\eta|\le C/r\)。取空间常向量 c。SE.18 给辅助无散场及完整误差
\[
 v=P_{df}[\eta(u-c)],\qquad\operatorname{sym}\nabla v=\eta S+E_\eta,
\]
\[
 E_\eta=\operatorname{sym}((u-c)\otimes\nabla\eta)
 -\nabla^2\Delta^{-1}((u-c)\cdot\nabla\eta),\quad
 \|E_\eta\|_2\le Cr^{-1}\|u-c\|_{L^2(\operatorname{supp}\nabla\eta)}.
 \tag{SC.5}
\]
逆 Laplacian 的源均值为零。第二项非局部，使用整胞 L2 范数；v 不是另一个 NS 解。

对 SC.4 还能省去这项非局部修正：该引理只要求辅助场是周期 H1 速度，并不要求它无散。因此可直接取
\[
 \widetilde v=\eta(u-c),\qquad
 \operatorname{sym}\nabla\widetilde v=\eta S+\widetilde E_\eta,
 \qquad\widetilde E_\eta=\operatorname{sym}((u-c)\otimes\nabla\eta).
 \tag{SC.5a}
\]
这里 \(\widetilde E_\eta\) 支撑在截断环域，具有 SC.5 的同一 L2 上界；它可以有非零迹，SC.4 允许 R 如此。以下先用 SC.5 写出估计，逐处将 v、\(E_\eta\) 换成带波浪号的量也成立。不是将 Leray 误差擅自丢掉，而是使用一个不需要 Leray 投影的兼容场。普通边界误差并未消失。

将 S 的特征值排序为 \(\lambda_1\le\lambda_2\le\lambda_3\)，令 \(a=-\lambda_1\ge0\)。固定 e，定义 G 为 \(S=0\) 的点与满足
\[
 a>0,\qquad\lambda_2\ge\delta a,\qquad
 \|P_f-P_e\|_{op}\le\varepsilon,\quad P_f=f\otimes f,\quad P_e=e\otimes e
 \tag{SC.6}
\]
的点之并，其中 f 是唯一负特征线的局部单位代表。G 定义在整个 \(B_{2r}\)，\(G^c=B_{2r}\setminus G\)。S=0 处不选 f，相关矩阵一律取零。补集包含非正中间谱、接近零中间谱和角度条件失效的全部区域。本稿的 \(\delta\) 与 a 比较，不是 SE 末节与 \(|S|\) 比较的同名参数。

G 内选择一个可测旋转 U 将 f 所在直线送至 e 所在直线。取局部符号 \(f\cdot e\ge0\) 的最短旋转即可。因为
\(\|U-I\|_{op}\le\sqrt2\|P_f-P_e\|_{op}\) 且 \(|S|\le\sqrt2a\)，所以
\[
 USU^\top\in K_{e,\delta},\qquad |S-USU^\top|\le4a\varepsilon.
\]
在整胞作纯代数分解
\[
 T=\eta\mathbf1_G USU^\top,\quad
 R=\eta\mathbf1_G(S-USU^\top)+\eta\mathbf1_{G^c}S+E_\eta.
\]
不对 U 或 \(\mathbf1_G\) 求导。SC.4 应用于 \(\operatorname{sym}\nabla v=T+R\)，给
\[
 X\le C_\delta(4\varepsilon X+\|\eta S\mathbf1_{G^c}\|_2+\|E_\eta\|_2),
 \qquad X=\|\eta a\mathbf1_G\|_2.
\]
因此当 \(\varepsilon\le(8C_\delta)^{-1}\) 时，
\[
 \boxed{\|\eta a\mathbf1_G\|_2\le
 2C_\delta\left[\|\eta S\mathbf1_{G^c}\|_2+
 Cr^{-1}\|u-c\|_{L^2(\operatorname{supp}\nabla\eta)}\right].}
 \tag{SC.7}
\]
正谱块不必接近比例 1:1；也不要求 G 连通。代价是完整保留 G 的补集和截断误差。

## 4. 一个实际的条件性速度控制出口

取 c=0，利用 \(|S|\le\sqrt2a\) 于 G 以及 SC.7，得到
\[
 \|S\|_{L^2(B_{3r/2})}\le C_\delta\left[
 F(t)+r^{-1}\|u(t)\|_2\right],\qquad
 F(t)=\|S(t)\mathbf1_{G(t)^c}\|_{L^2(B_{2r})}.
 \tag{SC.8}
\]
此后 \(C_\delta\) 表示仅依赖 \(\delta\) 及固定截断形状的有限常数，不再指 SC.4 的精确值。

这里不需要外引高可积性定理或 L1 Korn 不等式。取 \(\chi\in C_c^\infty(B_{3r/2})\)，在 \(B_r\) 上为 1，\(|\nabla\chi|\le C/r\)。对周期 \(w=\chi u\) 直接分部积分得到
\[
 \int|\operatorname{sym}\nabla w|^2
 =\frac12\int|\nabla w|^2+\frac12\int|\operatorname{div}w|^2.
 \tag{SC.9}
\]
将 w 在坐标球外延零，使用三维 \(\|w\|_6\le C\|\nabla w\|_2\)，于是
\[
 \boxed{\|u(t)\|_{L^6(B_r)}\le C_\delta\left[F(t)+r^{-1}\|u(t)\|_2\right].}
 \tag{SC.10}
\]
对能量弱解，上述步骤在具有 H1 空间切片的几乎处处时刻成立；对光滑解则逐时成立。e 可以选为可测的 \(e(t)\)，常数与其变化无关；这里从未对 e 求时间导数。

**条件推论（CONDITIONAL / STANDARD REGULARITY INTERFACE）。** 设 u 是周期适当弱解，满足能量界；\(0<t_0<T_*<T_{end}\) 为其定义时间区间中的时刻。固定 \(B_{2r}(x_0)\)、\(0<\delta\le1/2\) 和上述 \(\varepsilon\)。若存在可测 \(e(t)\)，使相应补集满足
\[
 \boxed{F\in L^4(t_0,T_*),}
 \tag{SC.11}
\]
则 SC.10 和 \(\sup_t\|u(t)\|_2\le\sqrt{2E(0)}\) 给
\(u\in L^4(t_0,T_*;L^6(B_r))\)。标准局部 Serrin 正则性因此排除 \((x_0,T_*)\) 的奇点。特别地，若整个 \(B_{2r}\) 几乎处处满足 SC.6（零应变也计入 G），则 F=0，已足够；参考方向不必在时间上固定。

本轮核对的明确文献接口是 [Neustupa, Theorem 1](https://arxiv.org/html/1310.3112v1)：它允许只在后向抛物外壳上检查速度的 Serrin 范数。取时间指数 4、空间指数 6，满足 \(2/4+3/6=1\)；取其几何参数 \(0<b<4\nu\lambda_S(B_1)\) 并缩小 \(\rho\)，使整个所用后向邻域包含于 \(B_r\times(t_0,T_*)\)。SC.10–11 的整个后向柱范数控制该外壳范数，故满足该定理的条件。不重证或声称全文审查它的局部正则性证明。

这一推论针对已有适当弱解的内部时点。用于一个光滑解的候选首次终点时，另需采用与同一初值及此前光滑段一致的适当弱延拓；存在性和弱强唯一性是标准外部接口，不由空间锥引理证明。这里没有默认终点已经光滑。

SC.11 是未得到的一项附加条件，不是从基本能量推出的结论。基本能量只给 \(F\in L^2_t\)，而不是 L4。若在整个周期胞假设精确的 SC.2 单侧锥（每时刻允许不同轴），则 \(\int e\cdot Se=-\int a=0\) 只容许 S=0；局部球上的条件并无这一全局退化。

## 5. 原方程究竟控制了负特征线的什么

以下回到原光滑解的开集 \(\lambda_1=-a<0<\lambda_2\le\lambda_3\)。负特征线简单；只需局部光滑单位代表 f，不假设可全局定向。令
\[
 P=f\otimes f,\quad\Pi=I-P,\quad
 J=\Pi\left[(S+aI)|_{f^\perp}\right]^{-1}\Pi.
\]
正谱重复不妨碍 J 和 P 光滑。SE.11 的耗散在此为
\[
 d_\pm=4\sum_k\partial_kf\cdot(S+aI)\partial_kf
 =4\sum_{k,j=2,3}(a+\lambda_j)|(\partial_kf)_j|^2,
\]
\[
 \boxed{2a|\nabla P|^2\le d_\pm\le4a|\nabla P|^2.}
 \tag{SC.12}
\]
证明：微分 \((S+aI)f=0\)，得
\((\partial_kS)_{j1}=-(a+\lambda_j)(\partial_kf)_j\)；代入 SE.11。再用 \(a\le a+\lambda_j\le2a\) 与 \(|\nabla P|^2=2|\nabla f|^2\)。SE.13 因而确实控制该开集上的 \(\int a|\nabla P|^2\,dxdt\)。

幅度的完整方程为
\[
 \boxed{La=a^2-\frac14|\omega\times f|^2+f\cdot Hf-\frac\nu2d_\pm.}
 \tag{SC.13}
\]
方向的完整方程为
\[
 \boxed{Lf=\nu|\nabla f|^2f+
 J\Pi\left[Hf+\frac14(\omega\cdot f)\omega+
 2\nu\sum_k(\partial_kS+(\partial_ka)I)\partial_kf\right].}
 \tag{SC.14}
\]
推导不把压力或黏性交叉项删去：由 \(LS=-S^2-\Omega^2-H\) 和
\(\Omega^2=(\omega\otimes\omega-|\omega|^2I)/4\)，对 \((S+aI)f=0\) 施加 L，得到
\[
 0=(LS+(La)I)f+(S+aI)Lf
 -2\nu\sum_k(\partial_kS+(\partial_ka)I)\partial_kf.
\]
取 f 分量并用 \(f\cdot Lf=\nu|\nabla f|^2\) 得 SC.13；取垂直分量并应用 J 得 SC.14。对 \(P=f\otimes f\) 再使用乘积法则：
\[
 LP=(Lf)\otimes f+f\otimes(Lf)-2\nu\sum_k\partial_kf\otimes\partial_kf.
 \tag{SC.15}
\]
局部换号 \(f\mapsto-f\) 时，SC.14 两边同变号，SC.12–13、SC.15 不变。没有将这些光滑公式延拓到负谱不简单或符号改变的集合；SE 原有的零谱测度仍保留。

因为 \(\|J\|_{op}\le a^{-1}\) 和 \(|\nabla a|\le|\nabla S|\)，有
\[
 a|LP|\le C\left[|H|+|\omega|^2+
 \nu|\nabla S||\nabla P|+\nu a|\nabla P|^2\right].
 \tag{SC.16}
\]
压力、涡量平方及最后一项已有时间 L1 控制；混合项尚无。Young 不等式会另外要求控制
\(\nu\int |\nabla S|^2/a\)，其中包含 SE 耗散没有估计的幅度导数和同号块变化。SC.16 因而没有提供完整的加权方向时间变差界。第 4 节出口本身不要求控制 \(e'(t)\)，这个事实也不能消除空间角度补集的估计问题。

## 6. 空间方向耗散与角度补集之间的有限连接

能直接证明的连接如下。固定时刻，在完整球 D=\(B_{2r}\) 上假设 \(\lambda_2>0\)、\(P\in H^1(D)\) 且
\(M\le a\le KM\)，其中 M>0、K≥1。取 \(\bar P=\fint_D P\)，并选其最大特征值的单位特征向量 e。由于 \(\bar P\ge0\)、\(\operatorname{tr}\bar P=1\)，
\[
 \int_D\|P-P_e\|_{op}^2
 =|D|(1-\lambda_{max}(\bar P))
 \le |D|(1-\operatorname{tr}\bar P^2)
 =\int_D|P-\bar P|^2
 \le Cr^2\int_D|\nabla P|^2.
\]
对 \(B_\varepsilon=\{\|P-P_e\|_{op}>\varepsilon\}\)，Chebyshev 不等式遂给
\[
 \boxed{\int_{B_\varepsilon}a^2\le
 CK^2Mr^2\varepsilon^{-2}\int_D a|\nabla P|^2.}
 \tag{SC.17}
\]
这是完整球上的幅度带条件，不得直接套到破碎的高应变集合：跨孔洞与分量之间的方向差没有受到这个 Poincaré 常数控制。它只处理角度失效，不自动控制 \(0<\lambda_2<\delta a\) 或 \(\lambda_2\le0\) 的部分。

即使额外有这样的整球幅度带，SE 的耗散在时间上只有 L1，SC.17 的右端也没有给出 SC.11 所需的 F 的 L4 时间控制。把 \(r\) 选成 \(M^{-1/2}\) 不能自动改变时间指数，也不能删除随时间变动的域和边界项。这里尚无排除高应变集中的无条件估计。

## 7. 文献边界、结论和下一项

我实际核对了 [Arroyo-Rabasa 等的原稿](https://arxiv.org/html/2106.03077v2) 的 Theorem 1.1、Corollary 1.2、Proposition 2.4 及相关证明。它要求极向量一致靠近一个与波锥不交的线性子空间；Remark 1.7 不允许将此替换为任意避开波锥的凸锥。它不直接提供任意 \(\delta\) 下 SC.2 的全范围高可积性。SC.3–10 的证明不依赖这项外部定理，而是使用二维行列式、完整截断和 L2 Korn 恒等式。这个区别不等于新颖性结论。

本节已证明固定负方向宽锥的 L2 控制、允许坏集的局部化、速度 L6 出口和原方程负特征线的完整局部动力学。局部锥估计可以避免 Leray 非局部修正，但没有消除普通截断误差。SC.11 是条件正则性，不是无条件先验估计。SE 的谱耗散仍不足以控制几何补集的 L4 时间范数；接近波锥的区域和局部边界仍在问题中。

下一项不重复窄锥文献移植、固定矩阵 Fourier 引理或另一种投影。先检查 SC.13–17 与应变相容性能否给出适合时间积分的局部插值或自改善估计：允许真实幅度分层，必须保留层边界、零谱与角度补集，并说明是否改善了基本能量的时间指数。困难引理可以继续探索，但不得将目标 SC.11 本身当作已知输入而宣称解决任意初值问题。

本稿没有仿真、DGX 运行、计算证书或科学附图。证明和审查为 AI 辅助研究，非真人同行评审。实际文件审查状态、冻结与后续交接另记；本稿本身不授权公开全文或网站操作。
