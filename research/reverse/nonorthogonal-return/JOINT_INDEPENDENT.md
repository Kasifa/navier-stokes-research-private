# 三对共享种子的共同接收：独立穷尽式与行相位障碍

2026-09-08，PRIVATE_CORE。状态：**得到穷尽接收式、Gram 相容变换、与时间无关的必要行相位门，以及条件性完整接收接口；没有接受候选。** 本稿待非作者实读审查。

本轮完整读取 `JOINT_CONTRACT.md`、本人 `SPATIAL_INDEPENDENT.md` 和 `INDEPENDENT_PREFLIGHT.md`，未读本轮主共同稿。以下共同支撑、变换和正幅度相容性自行推导。无科学程序、数组、指数数值、参数选择、Git 或外部定理调用。

## JI.1 第一层支撑与精确系数

固定线性独立整数波向量 \(p_1,p_2,p_3\)，\(P_i=|p_i|^2\) 两两不同，至少一对 \(c_{ij}=p_i\cdot p_j\ne0\)。每个 \(U_i\in p_i^\perp\setminus\{0\}\)，负模为其共轭。按 \(U_i^+=U_i\)、\(U_i^-=\overline U_i\)，第一层的完整系数为
\[
N_{ij}^{\sigma\tau}=-iP_{\sigma p_i+\tau p_j}
[\tau(U_i^\sigma\cdot p_j)U_j^\tau
+\sigma(U_j^\tau\cdot p_i)U_i^\sigma],
\quad i<j,\quad \sigma,\tau\in\{\pm1\}.
\tag{JI.1}
\]
两种有序作用已各计一次。同轴配对逐项为零，包括相反频率。由于三个频率线性独立，集合
\[
\mathcal L=\{\sigma p_i+\tau p_j:i<j,\ \sigma,\tau=\pm1\}
\]
恰有12个互异非零频率；实际系数可以为零。第一层支撑包含于此集合，没有其他模式。

对 \(k=\sigma p_i+\tau p_j\)，记
\[
F_{ij}^{\sigma\tau}(t)
=\int_0^t e^{-|k|^2(t-s)-(P_i+P_j)s}\,ds.
\]
于是
\[
(v_1)_k(t)=F_{ij}^{\sigma\tau}(t)N_{ij}^{\sigma\tau},
\quad
F_{ij}^{\sigma\tau}(t)=e^{-(P_i+P_j)t}
\frac{1-e^{-2\sigma\tau c_{ij}t}}{2\sigma\tau c_{ij}},
\tag{JI.2}
\]
最后一式在 \(c_{ij}=0\) 处取精确连续值 \(t e^{-(P_i+P_j)t}\)。每个热因子在正时间严格为正，且负输出取完整共轭。

## JI.2 加倍接收配对穷尽

把 \(p_i\) 当作实空间的一组基，仅用于唯一辨认频率系数。每个 \(\mathcal L\) 元素在此基下有两个非零坐标，各为 \(\pm1\)。若两个第一层频率相加为 \(2p_i\)，它们的第 i 坐标都必须为 +1。剩下的两个坐标必须在同一标签 j 上取相反符号。因此全部配对恰为
\[
(p_i+p_j,p_i-p_j),\quad(p_i-p_j,p_i+p_j),
\qquad j\ne i.
\tag{JI.3}
\]
每个正接收模有两条边、每边两个有序项，共四个有序配对。线性独立性排除了跨两种不同 j 的额外碰撞；非正交性不改变这个整系数论证。

沿用同一 \(U_i,U_j\) 的完整单对空间式
\[
C_{ij}=-iP_{2p_i}
[(N_{ij}^{+,+}\cdot(p_i-p_j))N_{ij}^{+,-}
+(N_{ij}^{+,-}\cdot(p_i+p_j))N_{ij}^{+,+}],
\tag{JI.4}
\]
此处用有序标签 i,j 解释 \(N^{+,+},N^{+,-}\)，即始终把 i 作为正接收种子；若原记录取 \(i<j\)，相应交换标签与符号即可。等价且不依赖记号选择的定义就是 JI.3 两项的完整系数。

记
\[
J_{ij}(t)=e^{-4P_it}\int_0^t e^{2(P_i-P_j)s}
\psi_{c_{ij}}(s)^2\,ds,
\quad
\psi_c(s)=\begin{cases}\sinh(cs)/c,&c\ne0,\\s,&c=0.\end{cases}
\tag{JI.5}
\]
全部加倍接收精确为
\[
\boxed{W_i(t):=(w_{22})_{2p_i}(t)
=\sum_{j\ne i}J_{ij}(t)C_{ij}(U_i,U_j).}
\tag{JI.6}
\]
所有 \(J_{ij}(t)>0\)，但不假设各边或各行权重相同。负接收为 \(\overline{W_i(t)}\)。两个向量通道在同一 \(p_i^\perp\) 中相加，可以发生真实相消；不能先取绝对值再比较模板。

## JI.3 目标外通道并未删除

两第一层模式若属于同一无序边，则除 JI.3 类接收外，只有零和或自配对：前者由横向点积逐项为零，后者 \(B(N_k,N_k)_{2k}=0\)。若来自两条不同边，它们在三标签中必共享一个标签 i。

共享标签同号时，输出为
\[
2\sigma p_i+\tau p_j+\upsilon p_k,
\qquad \{i,j,k\}=\{1,2,3\}.
\tag{JI.7}
\]
有24个互异的潜在频率，每个由两条指定第一层边的两个有序项供给。共享标签反号时，输出为
\[
\tau p_j+\upsilon p_k\in\mathcal L.
\tag{JI.8}
\]
每个这样的频率有两种共享符号 \(\sigma=\pm1\)，每种有两个有序项，共四个配对。

为明确这些不是从演化中删除的通道，写
\[
\mathcal B_K(X,Y;r,s)
=-iP_K[(X\cdot s)Y+(Y\cdot r)X],\qquad K=r+s.
\]
JI.7 的实际系数为
\[
\int_0^t e^{-|K|^2(t-s)}
F_{ij}^{\sigma\tau}(s)F_{ik}^{\sigma\upsilon}(s)
\mathcal B_K(N_{ij}^{\sigma\tau},N_{ik}^{\sigma\upsilon};
\sigma p_i+\tau p_j,\sigma p_i+\upsilon p_k)\,ds.
\tag{JI.9}
\]
JI.8 的实际系数为同式把第二条边的共享符号改成 \(-\sigma\)，并对 \(\sigma=\pm1\) 求和。每个 N 仍由同一组三个原种子决定。

因此完整 \(w_{22}\) 的支撑包含于6个目标频率、12个 JI.8 频率及24个 JI.7 频率。配对数也闭合：12个自配对及12个相反配对为零；24个有序配对供给目标，48个供给 JI.8，48个供给 JI.7，总数为 \(12^2=144\)。这只是有限支撑和完整系数的穷尽；不声称每个允许通道在所有极化下非零，也不以未检验的空间相消把它们设为零。

## JI.4 跨边共享坐标及退化条件

每个有序对 i,j 定义
\[
e_{ij}=p_j-\frac{c_{ij}}{P_i}p_i,
\quad n_{ij}=p_i\times p_j,
\quad \Delta_{ij}=P_iP_j-c_{ij}^2>0.
\]
同一 \(U_i\) 必同时满足
\[
U_i=u_{ij}e_{ij}+v_{ij}n_{ij}
=u_{ik}e_{ik}+v_{ik}n_{ik},
\tag{JI.10}
\]
\[
u_{ij}=\frac{P_i(U_i\cdot p_j)}{\Delta_{ij}},
\qquad v_{ij}=\frac{U_i\cdot n_{ij}}{\Delta_{ij}}.
\]
例如令 \(T_{ijk}=\det(p_i,p_j,p_k)\ne0\)，则
\[
U_i\cdot p_k
=u_{ij}\left(c_{jk}-\frac{c_{ij}c_{ik}}{P_i}\right)
+v_{ij}T_{ijk}.
\tag{JI.11}
\]
所以一行两条边上的四个坐标仅来自一个复二维向量，不是四个独立复未知量。

在单对公式中取 \(U_i=u e_{ij}+v n_{ij}\)、
\(U_j=x e_{ji}+y n_{ij}\) 时，准确对应
\((u,v,x,y)=(u_{ij},v_{ij},u_{ji},-v_{ji})\)；最后负号来自 \(n_{ji}=-n_{ij}\)，不能遗漏。

为使 JI.6 可直接复核，置 \(d_{ij}=P_i-P_j\)、
\(\Lambda_{ij}=(P_i+P_j)^2-4c_{ij}^2>0\)、
\(R=\Re(x\overline y)\)、\(I=\Im(x\overline y)\)，完整展开为
\[
C_{ij}=\frac{4i\Delta_{ij}^3d_{ij}}{P_i^2P_j^2\Lambda_{ij}}u
\left[c_{ij}d_{ij}u|x|^2e_{ij}
+\{P_j u[(P_i+P_j)R-2ic_{ij}I]
+2c_{ij}P_i|x|^2v\}n_{ij}\right].
\tag{JI.11a}
\]
此式在 \(c_{ij}=0\) 处也精确成立，未除以 \(c_{ij}\)。各边代入的是 JI.10–11 约束下的同一组三个种子。

长度不同已使 \(P_i-P_j\ne0\)。若 \(c_{ij}\ne0\)，已核单对零判据为
\[
C_{ij}=0\iff U_i\cdot p_j=0\ \text{或}\ U_j\cdot p_i=0.
\tag{JI.12}
\]
若 \(c_{ij}=0\)，则必须用完整连续接口
\[
C_{ij}=\frac{4iP_iP_j^2(P_i-P_j)}{P_i+P_j}
u^2\Re(x\overline y)\,n_{ij}.
\tag{JI.13}
\]
此时零分支为 \(u=0\) 或 \(\Re(x\overline y)=0\)，不能照搬 JI.12。无论哪种边，若一个接收行的两边均为零，或完整相加后为零，就不可能匹配非零种子及 \(\rho>0\)。单边非零仍不保证整行非零。

## JI.5 Gram 相容的 O 与一个共同平移

记列矩阵 \(M=[p_1\ p_2\ p_3]\)，Gram 矩阵 \(G=M^TM\)。长度互异使允许 O 必满足 \(Op_i=\varepsilon_i p_i\)，没有标签置换。若 \(E=\operatorname{diag}(\varepsilon_i)\)，唯一可能的实线性映射为 \(O=MEM^{-1}\)。它正交当且仅当
\[
EGE=G
\iff (\varepsilon_i\varepsilon_j-1)c_{ij}=0\quad\text{对全部 }i,j.
\tag{JI.14}
\]
把非零 \(c_{ij}\) 连成无向图，符号必须在每个连通分量上相同，反之这些符号确实给正交 O。至少一条边的合同下，图连通时只有 \(O=\pm I\)；恰一条边及一个孤立点时有4个允许 O。不能独立给三行选择反射。

展开比较模板，正接收模恰为
\[
\boxed{\bigl[\rho Oa(2O^T(x-x_0))\bigr]_{2p_i}
=\rho\eta_i O U_i^{(\varepsilon_i)},
\qquad \eta_i=e^{-2ip_i\cdot x_0}.}
\tag{JI.15}
\]
一个共同平移确实允许任意三个单位相位：给任意实辐角 \(\theta_i\)，解实线性系统 \(2M^Tx_0=-\theta\)，再将 \(x_0\) 取模 \(2\pi\) 即可。由于 M 为整数矩阵，取模不改变三个指数；因 M 可逆，解存在。负接收自动为真正共轭。

若 O 不保持整个整数格，上式仍是有限种子模板的合法周期比较，因为 \(Op_i=\pm p_i\)。它不是据此获得的完整环面 NS 对称，不能作为未经证明的全场迭代操作。

## JI.6 分离正幅度后的精确方向条件

对同一个种子写
\[
U_i=\sqrt{a_i}e^{i\theta_i}V_i,
\qquad a_i>0,\quad \|V_i\|_{\mathbb C^3}=1,\quad V_i\perp p_i.
\]
这是原未知量的重新表示，没有为每条边另设初值。单对完整映射满足
\[
C_{ij}(zU_i,wU_j)=z^2|w|^2C_{ij}(U_i,U_j),
\]
包括正交边的连续接口。因此置
\[
K_{ij}(t)=J_{ij}(t)C_{ij}(V_i,V_j),\quad
B_i(a,t)=\sum_{j\ne i}a_jK_{ij}(t),\quad
T_i=O V_i^{(\varepsilon_i)},
\tag{JI.16}
\]
便有
\[
W_i=e^{2i\theta_i}a_i B_i.
\]
\(T_i\in p_i^\perp\) 且 Hermitian 范数为1。返回要求 \(B_i\) 落在复直线 \(\mathbb CT_i\) 上，不能只匹配某个分量或范数。

在复化横向平面使用非退化交替形式
\[
\Omega_i(X,Y)=p_i\cdot(X\times Y).
\]
对任意非零 \(T_i\in p_i^\perp\)，\(\Omega_i(T_i,Z)=0\) 当且仅当 \(Z\in\mathbb CT_i\)。这也适用于双线性自点积为零的复向量，因为这里用的是二维非退化交替形式，不是除以 \(T_i\cdot T_i\)。

定义仅由几何、共同形状和允许 O 决定的方向缺陷
\[
\delta_{ij}=\Omega_i(T_i,C_{ij}(V_i,V_j))\in\mathbb C.
\tag{JI.17}
\]
若 \(\{i,j,k\}=\{1,2,3\}\)，共同方向条件精确为
\[
a_jJ_{ij}(t)\delta_{ij}+a_kJ_{ik}(t)\delta_{ik}=0.
\tag{JI.18}
\]

## JI.7 与时间无关的严格行相位障碍

JI.18 的两个系数 \(a_jJ_{ij}\)、\(a_kJ_{ik}\) 都严格为正。故每个接收行必须满足且仅能满足以下方向分支之一：

1. \(\delta_{ij}=\delta_{ik}=0\)，两个边输出已各自落在目标复直线上；
2. 两个缺陷均非零，且
\[
\boxed{\Im(\delta_{ij}\overline{\delta_{ik}})=0,
\qquad \Re(\delta_{ij}\overline{\delta_{ik}})<0.}
\tag{JI.19}
\]

证明很直接但保留了正幅度限制：若两个缺陷非零，除以正系数及其中一个缺陷，JI.18 等价于它们的比值为严格负实数；恰一项为零时不可能相消。反之，两个非零缺陷处于严格相反射线时，一行方向方程确实给出唯一正幅度比。这不等于三行比值相容或共同返回成功。

因此，对于一组三个固定极化形状和一个 Gram 相容 O，只要任意一行出现恰一个零缺陷、非共线复相位，或非零同向实射线，就对**全部正时间、全部正幅度、全部种子整体相位和全部共同平移**排除该 O 下的返回。若对每个有限的允许 O 都有这样的坏行，则这组三个形状在本树合同下全部被排除。

这是一项可作精确实符号判定的必要条件，并非只重写共同方程：它消去了全部热权重、幅度、时间和整体相位。在检查通过之前，调节这些量不能修复方向缺陷；通过也不表示存在候选。

改变形状代表元 \(V_i\mapsto e^{i\phi_i}V_i\) 时，
\[
\delta_{ij}\mapsto e^{i(2+\varepsilon_i)\phi_i}\delta_{ij},
\]
同一行两项获得相同相位，发送端 j 的整体相位完全消失。故 JI.19 不依赖任意代表元相位的选择。这一步仍严格共享原种子，不是把 N 的两极化自由化。

## JI.8 三行正幅度的热循环门

若三行均处于 JI.19 的非零分支，对循环标签
\((i,j,k)=(1,2,3),(2,3,1),(3,1,2)\) 定义
\[
r_i=-\delta_{ik}/\delta_{ij}>0.
\]
JI.18 逐行要求
\[
\frac{a_2}{a_3}=r_1\frac{J_{13}}{J_{12}},\quad
\frac{a_3}{a_1}=r_2\frac{J_{21}}{J_{23}},\quad
\frac{a_1}{a_2}=r_3\frac{J_{32}}{J_{31}}.
\]
相乘得到一个共同时间的严格必要门
\[
\boxed{r_1r_2r_3
\frac{J_{13}(t)J_{21}(t)J_{32}(t)}
{J_{12}(t)J_{23}(t)J_{31}(t)}=1.}
\tag{JI.20}
\]
反之，在此非零方向分支，若给定同一个 t 满足 JI.20，则三条正幅度比确实相容且确定 \((a_1,a_2,a_3)\) 到一个共同正倍数。这个反向陈述只解决方向，不保证行输出非零或共同模长。

若某行两缺陷都为零，不对该行除法，也不套用 JI.20；它的方向自动满足，仍须保留其他行以及下节模长条件。这里没有用 \(J_{ij}>0\) 把循环热比当成1，没有选择时间或搜索它的根。

## JI.9 条件性完整接收接口与共同幅度

对固定符号几何、三个形状、允许 O、同一个 \(t>0\) 和三个 \(a_i>0\)，令 JI.16 的 \(B_i\) 满足全部方向条件。用 Hermitian 内积记
\[
b_i=T_i^*B_i,
\qquad B_i=b_iT_i.
\]
方向条件下此表达精确；使用 Hermitian 内积提取比例不改变原 B 算子的双线性点积。全部接收返回进一步当且仅当
\[
\boxed{a_1|b_1|^2=a_2|b_2|^2=a_3|b_3|^2>0.}
\tag{JI.21}
\]
必要性来自 \(\sqrt{a_i}|b_i|=\rho\)。充分性也只针对接收投影：若共同值为 \(\rho^2>0\)，可取
\[
\eta_i=\frac{\sqrt{a_i}b_i}{\rho}
e^{i(2-\varepsilon_i)\theta_i},
\]
三个 \(\eta_i\) 都单位模，JI.5 的共同平移满射给出一个 \(x_0\)，使 JI.15 同时成立。负模由共轭成立。

若任一 \(B_i=0\)，则即使两个缺陷均为零也不能通过 JI.21。若整体替换 \(a_i\mapsto s a_i\)，则 \(B_i\mapsto sB_i\)，三份量 \(a_i|b_i|^2\) 都乘 \(s^3\)；因此整体放大不能修复三行模长比例不等，只会在已相等时令 \(\rho\mapsto s^{3/2}\rho\)。这保留了单个共同 \(\rho\)，没有偷偷放开每行幅度。

## JI.10 本轮推进与停止边界

本轮新增了 JI.3 的接收配对穷尽、目标外完整通道、JI.14–15 的真实变换合同，以及 JI.19 的无时间行相位障碍。JI.20 与 JI.21 进一步保留跨行正幅度及共同模长的准确接口。尚未选择或证明某组三维整数几何、共同形状和时间通过这些门；因此没有接受候选，也没有对整个非正交族作通用排除。

这些式子属于指定有限 \(w_{22}\) 树，解析余项为零。比较的是其接收投影，目标外通道仍然存在于完整树；本稿不把这种投影约定说成删除了目标外反馈的真实 NS 演化。1+3/3+1、种子直接混合、真实前代偏差、回流和无限维误差仍未支付。即使条件性接收接口可解，也不是完整原解的有限两步供给，更不是单初值无限尺度、统一迭代、有限总时间或奇性证明。

## JI.11 实读来源

| 本轮完整实读文件 | SHA256 |
|---|---|
| JOINT_CONTRACT.md | cc3cd571b87cde40488345d8d8faa6ac774892701f30869ee479c3d82088e23c |
| SPATIAL_INDEPENDENT.md | d8413facd655e775e7e3582b45947be92a3c0f60387b966625475088ff3703f8 |
| INDEPENDENT_PREFLIGHT.md | 679ce998bd78f2203232e6404df376eb94a2a19419c6ae3fdb82b25dbf823f65 |

未读本轮主共同稿，没有新增外部文献或新颖性声明。来源哈希不能代替非作者审查。
