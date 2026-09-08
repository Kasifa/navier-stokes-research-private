# 全横向极化的 Fourier 支撑不变性：独立证明

2026-09-08。PRIVATE_CORE。**独立稿已完成正文推导，待非作者复核。PROVED SUPPORT INTERFACE / NO-CANDIDATE / NOT CLAY。**

本稿全文读取本目录先锁合同及本工作树 AGENTS.md 后独立形成，没有读取同目录根 PROOF.md、另一份新证明或本项未来审查。合同已披露根先行观察过一对模作用及第三频率补齐思路；这不是结果未知的预注册。本作者曾写旧 SOURCE_BRIDGE_INDEPENDENT.md，并参与此前多阶段非盲审查；本轮的独立性仅指没有互读本轮证明，不声称与整个研究历史隔离。

这里证明一个支撑空间对**所有横向极化和所有其中的实值无散三角多项式**统一封闭的充要条件。通过时再连接到同一个实际 NS 最大经典分支；不通过时构造依赖一对符号频率的有限见证。没有选择实际整数频率、初值、参数或时刻，没有科学程序、数组、数值求值、枚举、扫描、Git、外部消息或发布。

## SI.1 对象与结论

固定 \(\nu>0\)，在 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\) 上使用
\[
 u(x)=\sum_{k\in\mathbb Z^3}\widehat u_k e^{ik\cdot x},\qquad
 \widehat u_{-k}=\overline{\widehat u_k},\qquad
 k\cdot\widehat u_k=0,\qquad \widehat u_0=0.
 \tag{SI.1}
\]
点积在 Fourier 卷积中为复双线性点积，向量长度为 Hermitian 欧氏范数。非零模 Leray 投影为
\[
 \mathbb P_k=I-\frac{k\otimes k}{|k|^2},\qquad
 B(f,g)_k=-i\mathbb P_k
       \sum_{r+s=k}(\widehat f_r\cdot s)\widehat g_s.
 \tag{SI.2}
\]
第一输入无散时，每个零模有序项都有
\(\widehat f_r\cdot(-r)=0\)，故规定 \(B(f,g)_0=0\)。不把零模作为未处理例外，也不把 \(B\) 改为对称双线性算子。

令 \(N=-N\subset\mathbb Z^3\setminus\{0\}\)，并令
\(d=\dim_{\mathbb R}\operatorname{span}_{\mathbb R}N\)，空集的 \(d\) 为零。下列三件事等价：

1. 每个满足 SI.1、支撑在 \(N\) 内的三角多项式 \(a\)，均有
   \(\operatorname{supp}\widehat{B(a,a)}\subset N\)。
2. 对每对 \(p,q\in N\)，若 \(p\times q\ne0\)，则 \(p+q\in N\)。
3. 当 \(d\le1\) 时，对称集合 \(N\) 没有额外限制；当 \(d\ge2\) 时，
   \[
   H:=N\cup\{0\}\quad\hbox{是 }\mathbb Z^3\hbox{ 的加法子群}.
   \tag{SI.3}
   \]

子群不要求是整个 \(\mathbb Z^3\)，也不要求等于其所在实线性空间与 \(\mathbb Z^3\) 的交。分类不是将所有允许支撑补成整个整数格。

上述条件还等价于：每个光滑 \(a\in V_N\) 的同数据、固定 \(\nu\)、无外力 NS 最大经典分支在其整个存在区间内支撑于 \(N\)。这句话不给最大时间统一下界，也不声称 \(d\ge2\) 时解全局存在。动力学等价性在 SI.5–7 中另证。

## SI.2 一对非共线模：完整有序项的必要性

任取满足 \(p\times q\ne0\) 的符号 \(p,q\in N\)，置
\[
 U=q-\frac{p\cdot q}{|p|^2}p,\qquad
 V=p\times q,\qquad
 \gamma=U\cdot q
       =|q|^2-\frac{(p\cdot q)^2}{|p|^2}
       =\frac{|p\times q|^2}{|p|^2}>0 .
 \tag{SI.4}
\]
于是 \(U\cdot p=0\)，\(V\cdot p=V\cdot q=0\)，且 \(U,V\ne0\)。考虑唯一这份实值有限初值
\[
 a(x)=Ue^{ip\cdot x}+Ue^{-ip\cdot x}
      +Ve^{iq\cdot x}+Ve^{-iq\cdot x}.
 \tag{SI.5}
\]
它无散、零均值、光滑且支撑于 \(\{\pm p,\pm q\}\subset N\)。这只是对任意失败频率对的符号见证，没有赋予 \(p,q\) 实际整数值。

令 \(k=p+q\)。非共线性使 \(k\ne0\) 且 \(k\notin\{\pm p,\pm q\}\)。在 SI.2 的整个有序卷积中，能输出 \(k\) 的输入对只有 \((p,q)\) 与 \((q,p)\)。因此
\[
 \begin{aligned}
 B(a,a)_{p+q}
 &=-i\mathbb P_{p+q}
       \bigl[(U\cdot q)V+(V\cdot p)U\bigr]\\
 &=-i\gamma V\ne0.
 \end{aligned}
 \tag{SI.6}
\]
第二个有序项实际为零；第一个完整保留。因为 \(V\perp p+q\)，Leray 投影确实不改变这个非零向量。没有仅检验未投影的对流项。

为核清其它有序项与实值条件，全部非零输出为
\[
 \begin{aligned}
 B(a,a)_{p+q}&=-i\gamma V,&
 B(a,a)_{p-q}&= i\gamma V,\\
 B(a,a)_{-p-q}&= i\gamma V,&
 B(a,a)_{-p+q}&=-i\gamma V .
 \end{aligned}
 \tag{SI.7}
\]
这四个频率互异。自配对、相反模配对和所有以 \(\pm q\) 为第一输入的项都由横向点积为零消失。SI.7 的负模恰为相应正模的共轭。因此若命题 1 成立，SI.6 必迫使 \(p+q\in N\)，得到命题 2。

该见证也覆盖 \(|p|=|q|\)；没有等长的额外退化分支。这里允许三维速度的全部横向方向，即使两个波向量张成的平面只有二维。把速度另限于该平面，或把每个模限于一条极化线，会改变这一量词，不能直接使用本段必要性。

## SI.3 非共线加法条件的充分性

设命题 2 成立。更强地，对任意两个支撑在 \(N\) 内的无散三角多项式 \(f,g\)，SI.2 中每个有序项都满足：

- 若 \(r,s\) 共线，则 \(\widehat f_r\cdot s=0\)，此项为零；
- 若 \(r,s\) 不共线，则 \(r+s\in N\)，输出经 Leray 后仍位于同一个频率。

零模已在 SI.2 处理。故
\[
 \operatorname{supp}\widehat{B(f,g)}\subset N.
 \tag{SI.8}
\]
尤其命题 1 成立。这里不借不同输入对的偶然相消，也没有把无限维解近似成此处的多项式。

若 \(d\le1\)，所有输入对均共线，因而
\[
 B(f,g)=0,\qquad (f\cdot\nabla)g=0
 \tag{SI.9}
\]
对所有这类多项式成立，对光滑同支撑场则由绝对收敛延拓。因此任意对称 \(N\) 都通过检验，包含空集及有限或无限共线集合。没有必要要求 \(p+p\in N\)。

## SI.4 秩至少二时，共线和也被迫补齐

设 \(d\ge2\) 且命题 2 成立。要证 SI.3，只须核查 \(H\) 的加法闭合；零元和取负已经具有。

取 \(p,q\in N\)。不共线情形已有结论。共线且 \(p+q=0\) 时，和属于 \(H\)。剩下只考虑
\[
 p\times q=0,\qquad p+q\ne0.
 \tag{SI.10}
\]
因 \(d\ge2\)，可取 \(r\in N\) 不与 \(p\) 共线。此时也不与 \(q\) 共线，所以命题 2 和对称性给
\[
 p+r\in N,\qquad q-r\in N.
 \tag{SI.11}
\]
这些向量非零，并且
\[
 (p+r)\times(q-r)
 =-p\times r+r\times q
 =-(p+q)\times r\ne0.
 \tag{SI.12}
\]
最后一个非零性由 SI.10 及 \(r\notin\operatorname{span}p\) 保证。再用一次命题 2，
\[
 (p+r)+(q-r)=p+q\in N.
 \tag{SI.13}
\]
这也处理 \(p=q\) 和任意非零共线和，不需要先假设倍频已经允许。于是 \(H\) 是加法子群。反向则直接由子群加法和非共线和不为零得到命题 2，完成三件事的等价证明。

一个限于本接口的推论是：有限的 \(N\) 若包含两个非共线向量，就不能满足全极化统一不变性。若满足，SI.3 将包含一个非零向量的全部整数倍，与有限性矛盾。这个推论仍不是任何特定极化初值的泄漏定理。

## SI.5 固定正黏性的全 Fourier 局部构造

为避免把 Galerkin 支撑直接当成实际解，这里给出适用于一般光滑初值的完整入口。它沿用旧 SB.3、SB.23、SB.26 的 Wiener 估计方法，但不把旧三对有限数据、单位黏性或叶数窗口作为本项假设。

对非负整数 \(m\)，定义
\[
 \|f\|_{\mathcal A_m}
  =\sum_{k\in\mathbb Z^3}(1+|k|)^m|\widehat f_k|,
 \qquad \mathcal A=\mathcal A_0,\qquad
 E_\nu(t)=e^{\nu t\Delta}.
 \tag{SI.14}
\]
实值、无散、零均值条件给出其中的闭实 Banach 子空间。所有光滑周期初值属于每个 \(\mathcal A_m\)。

利用 \(\widehat f_r\cdot s=\widehat f_r\cdot(r+s)\)，
\((1+|r+s|)^m\le(1+|r|)^m(1+|s|)^m\) 及
\[
 |k|e^{-\nu\tau|k|^2}\le(\nu\tau)^{-1/2},
 \qquad \tau>0,
\]
从完整卷积直接得到
\[
 \|E_\nu(\tau)B(f,g)\|_{\mathcal A_m}
 \le(\nu\tau)^{-1/2}\|f\|_{\mathcal A_m}\|g\|_{\mathcal A_m}.
 \tag{SI.15}
\]
因此
\[
 \left\|\int_0^t E_\nu(t-s)B(f(s),g(s))\,ds
 \right\|_{C([0,h],\mathcal A_m)}
 \le b_h\|f\|_{C_t\mathcal A_m}\|g\|_{C_t\mathcal A_m},
 \quad b_h=2\sqrt{h/\nu}.
 \tag{SI.16}
\]
该积分在 \(C_t\mathcal A_m\) 中存在且连续：奇核可积，对有限 Fourier 和直接成立，再用 SI.15 及尾部逼近。这些是无限卷积的估计，不执行频率截断演算。

先在 \(m=0\) 工作。若 \(a=0\)，零解直接成立。否则令 \(A=\|a\|_{\mathcal A}>0\)、\(R=2A\)。存在 \(h>0\) 使
\[
 b_hR^2\le R-A,\qquad 2b_hR<1.
 \tag{SI.17}
\]
这里没有选择实际 \(h\)。映射
\[
 \Phi_a(u)(t)=E_\nu(t)a+
       \int_0^tE_\nu(t-s)B(u(s),u(s))\,ds
 \tag{SI.18}
\]
由 SI.16 将 \(C_t\mathcal A\) 的半径 \(R\) 闭球映到自身，Lipschitz 常数至多 \(2b_hR<1\)。Banach 收缩给同数据的实际全 Fourier mild 解。实值、无散和零均值由 SI.2 及热乘子保持。

两条已有的 \(C_t\mathcal A\) mild 解若起点相同，在充分短的子区间有
\[
 \|u-\widetilde u\|_{C_t\mathcal A}
 \le b_h(M_u+M_{\widetilde u})
       \|u-\widetilde u\|_{C_t\mathcal A},
 \tag{SI.19}
\]
其中 \(M_u,M_{\widetilde u}\) 是该区间上的有限范数。将系数取小于一并作有限分段，得到整个共同有限窗口的唯一性。局部构造可在同一解的实际状态继续，得到唯一最大 mild 分支；这是解的延拓论证，不是重置种子或改换初值。

还须支付光滑性在同一分支上的保持。对 \(m\ge1\)，存在只依赖 \(m\) 的有限 \(c_m>0\)，使
\[
 \begin{aligned}
 \|E_\nu(\tau)B(f,g)\|_{\mathcal A_m}
 \le c_m(\nu\tau)^{-1/2}\bigl(
   \|f\|_{\mathcal A_m}\|g\|_{\mathcal A}
  +\|f\|_{\mathcal A}\|g\|_{\mathcal A_m}\bigr).
 \end{aligned}
 \tag{SI.20}
\]
这是由
\((1+|r+s|)^m\le c_m[(1+|r|)^m+(1+|s|)^m]\)
逐项求和得出。

在任何已经存在的紧窗口上，令
\(M=\sup_t\|u(t)\|_{\mathcal A}<\infty\)。
局部 \(\mathcal A_m\) 构造与 SI.19 的唯一性属于同一 \(u\)。
在其中长度为 \(\ell\) 的一段，SI.20 给
\[
 \sup_{t_0\le t\le t_0+\ell}\|u(t)\|_{\mathcal A_m}
 \le \|u(t_0)\|_{\mathcal A_m}
  +4c_mM\sqrt{\ell/\nu}
     \sup_{t_0\le t\le t_0+\ell}\|u(t)\|_{\mathcal A_m}.
 \tag{SI.21}
\]
取 \(\ell\) 足够小使后系数小于 \(1/2\)，便有有限的高阶范数界。这个 \(\ell\) 只依赖该紧窗口的 \(M,m,\nu\)，不依赖尚待控制的高阶范数。若高阶分支试图在该段内提前结束，界 SI.21 和局部收缩的同一半径构造将其延长，矛盾。有限分段遂将每个 \(\mathcal A_m\) 正则性延到整个给定紧窗口。所用有界范数延拓准则亦可直接从 SI.18 得到：固定一个足够近的左端点后，末端 Duhamel 部分由 SI.16 一致变小，热演化部分连续，先取得末端极限再用局部构造继续。

因此对光滑 \(a\)，上述最大分支在每个紧子区间内连续取值于所有 \(\mathcal A_m\)。完整未平滑卷积还满足
\[
 \|B(f,g)\|_{\mathcal A_m}
 \le\|f\|_{\mathcal A_m}\|g\|_{\mathcal A_{m+1}}.
 \tag{SI.22}
\]
从 SI.18 或逐模积分与绝对收敛得
\[
 u\in C^1_t\mathcal A_m,\qquad
 \partial_tu=\nu\Delta u+B(u,u)
 \tag{SI.23}
\]
对每个 \(m\) 成立，初始端点取右导数。进一步对方程求导，每次只使用有限个更高空间阶和 SI.22，给所有时间导数。故它是同数据的光滑经典 NS 分支。任何延长的光滑经典解都属于局部 \(C_t\mathcal A\) 唯一性类；由 SI.19 与当前分支一致，所以这里的最大分支就是同数据最大经典分支，记作 \([0,T_{\max})\)。没有给出 \(T_{\max}=\infty\)。

压力也在同一分支上完整恢复，零均值规范为
\[
 \widehat\pi_k(t)=
 -\frac1{|k|^2}\sum_{r+s=k}
       (k\cdot\widehat u_r(t))(k\cdot\widehat u_s(t)),
 \quad k\ne0,\qquad \widehat\pi_0=0.
 \tag{SI.24}
\]
上述高阶绝对收敛保证压力光滑。它满足
\(-\Delta\pi=\partial_i\partial_j(u_i u_j)\)，并给
\[
 \partial_tu-\nu\Delta u+(u\cdot\nabla)u+\nabla\pi=0.
 \tag{SI.25}
\]
黏性、周期压力及全部有序作用均未删除。

## SI.6 通过时：同一个最大经典分支保持支撑

假设 SI.1 的三个等价条件成立。定义闭子空间
\[
 \mathcal A(N)=\{f\in\mathcal A:
     \widehat f_k=0\text{ 对所有 }k\notin N\},
 \tag{SI.26}
\]
并仍同时要求实值、无散、零均值。闭性可逐模由
\(|\widehat f_k|\le\|f\|_{\mathcal A}\) 看出。

SI.8 和 SI.15 表明，对于 \(\tau>0\)，
\(E_\nu(\tau)B(f,g)\) 将 \(\mathcal A(N)\times\mathcal A(N)\)
映入 \(\mathcal A(N)\)。这里先对有限 Fourier 和用 SI.8，再由
SI.15 连续延拓，所以并没有对未正则化的 \(\mathcal A\) 卷积强作逐项求导。热半群本身也保持该空间。因此以 \(E_\nu(t)a\) 开始的 SI.18 收缩迭代全在 \(C_t\mathcal A(N)\) 中，极限属于同一闭空间。

SI.19 将这个受支撑限制的构造认作同一个完整 NS 解。对任意 \(T<T_{\max}\)，其 \(C([0,T],\mathcal A)\) 范数有限。可用共同的充分小步长，从已经保持支撑的实际状态开始重复上述局部论证，有限步覆盖 \([0,T]\)。在每个衔接端点支撑由闭性保持。于是
\[
 \operatorname{supp}\widehat u(t)\subset N
 \qquad(0\le t<T_{\max}).
 \tag{SI.27}
\]
这是极限与唯一性后的无限维结论，不是某个 Galerkin 系统的不变性替代品。

若 \(d\le1\)，SI.9 更直接给
\[
 u(t)=E_\nu(t)a,\qquad \pi(t)=0
 \tag{SI.28}
\]
为全局光滑解，唯一性使其就是实际最大分支。空集时为零解。这个线性退化例外不被混入 \(d\ge2\) 的子群分类。

## SI.7 不通过时：同一真实解的初始泄漏及严格余项

若三个等价条件不成立，由 SI.1–4 必有符号
\[
 p,q\in N,\qquad p\times q\ne0,\qquad k=p+q\notin N.
 \tag{SI.29}
\]
采用公式 SI.4–5 的一份固定初值，并保持事先固定的 \(\nu>0\)。第 SI.5 节所构造的真实解在初始端点具有 SI.23 的时间正则性。由于 \(\widehat a_k=0\)，
\[
 c_k:=\left.\frac{d}{dt}\widehat u_k(t)\right|_{t=0+}
   =-\nu|k|^2\widehat a_k+B(a,a)_k
   =-i\gamma V\ne0.
 \tag{SI.30}
\]
黏性项在该模的初始值确实为零，而不是从方程中略去。由 SI.24，SI.5 这份初值的压力在初始时刻也为零：同轴点积为零，异轴乘积含有 \(k\cdot V=0\)。后续压力仍按 SI.24 完整演化，未被假定继续为零。SI.30 也可直接用已含 Leray 的 SI.6 核验，不依赖额外压力假设。

定义实际余项
\[
 r_k(t)=\int_0^t\bigl[\partial_s\widehat u_k(s)-c_k\bigr]\,ds.
 \tag{SI.31}
\]
SI.23 的 \(C^1_t\mathcal A\) 正则性保证积分合法，且
\[
 \widehat u_k(t)=t c_k+r_k(t),\qquad
 \frac{|r_k(t)|}{t}
 \le\sup_{0\le s\le t}|\partial_s\widehat u_k(s)-c_k|
 \longrightarrow0\quad(t\downarrow0).
 \tag{SI.32}
\]
因此存在依赖这份固定 \(a,\nu\) 的
\(\delta\in(0,T_{\max})\)，使
\[
 |\widehat u_k(t)|\ge\frac{|c_k|}{2}\,t>0
 \qquad(0<t<\delta).
 \tag{SI.33}
\]
这只是一阶导数连续性给出的存在性时间窗。没有显式数值 \(\delta\)、统一于所有失败频率对的窗口、数值尾界或计算证书。所有后续 Fourier 作用包含在实际余项 SI.31 中；没有对它们作未经证明的 \(O(t^2)\) 声明。

这个见证否定的是“对所有 \(a\in V_N\) 保持”的统一命题。它不声称每个指定的 \(a\) 都泄漏；个别零非线性场或另外受约束的极化空间仍需另作检验。

## SI.8 文献接口、实际阅读与边界

Miller 的固定版本 [2307.03434v5，Appendix D](https://arxiv.org/pdf/2307.03434v5#page=107) 已给加法子群支撑的充分条件：D.1–3 的空间与卷积，D.6–7 的热半群及 NS mild 支撑保持。本稿承认这一已有接口，不主张外部新颖性。其开头的加法必要性概述不能替代本稿对全极化量词和 \(d\le1\) 例外的证明。原文更窄模型另固定每模极化线；集合不满足加法闭合，不能单凭本稿的全极化见证判定该指定模型中的某份数据泄漏。

本轮通过官方固定版本 PDF 的文字提取，实际定向读取 Appendix D 开头、D.1–3 及 D.6–7 的陈述和证明（PDF 第107–109页）；工具同时返回的 D.4–5 等相邻内容没有作为外部存在定理的接纳输入。本轮未取得 PDF 二进制哈希、未作页面视觉或整篇证明审核。下述旧 PRIMARY_SCOPE.md 的 PDF 哈希
\(\texttt{d6e508d194534d86d0eb0a706b5d511766dfe687209dc59a98839469f6b09cc5}\)
是其作者此前实取字节的继承记录，不冒称为本作者本轮实测。

以下路径相对于本工作树 /Users/kasifa/Documents/Math/navier-stokes-reverse/。SHA-256 是本轮对本地实际文件测得；科学输入范围逐项列明。

| 本地来源 | 本轮实际阅读范围 | SHA-256 |
|---|---|---|
| AGENTS.md | 全文；终核发现根已更新开头后，再次全文读取当前版本；隔离、权限与历史状态，不作为数学证据 | 01de3ccca6826934a15614866bdb5f3bc55dd559d6b4458c59d06ab4432eae15 |
| research/reverse/support-invariance/CONTRACT.md | 全文；本项固定合同 | 6e1762229978d3238772594a7d0b87ee902c6002925a2b4ce1098c3382305b0c |
| research/reverse/mixed-polarization/SOURCE_BRIDGE_INDEPENDENT.md | 第1–248行，SB.1–4 全文及下一节标题；本作者旧稿的 Wiener 估计、经典性、唯一性与压力入口 | 1d3d33fbb8fcc17ac1266f2ee88c88eebe328867f385277a0a684cfa2247630a |
| research/reverse/symmetry-source-preflight/PRIMARY_SCOPE.md | 全文；Miller 原文对象、固定极化限制与既往实际阅读记录 | 5200cfc99a1fd2f4b88528e9a523628a0505e7496b8e65c730b24512558ddda3 |

跨会话记忆仅用于确认反向工作树与角色隔离；其中较旧的暂停记录不覆盖当前实际合同。它未被用作本项科学来源或当前状态认证。

本轮闭合的范围是 SI.1 的全极化充要条件、SI.27 的同数据最大经典分支保持，以及失败时 SI.29–33 的符号有限数据初始泄漏。它没有付出指定极化模型的统一不变性，也没有给出真正净化来源、第二代供给优势、任意跨代误差预算、固定初值无限尺度、有限总时间奇性或 Clay 结论。通过此接口仍未形成新再生成候选。
