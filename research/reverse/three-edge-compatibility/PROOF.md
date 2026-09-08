# 三边共同极化的横向标量与未消去分量

2026-09-08，PRIVATE_CORE。状态：本轮主推导完成，待未读本稿的独立推导及非作者审查。没有接受候选。

**本轮得到完整相干混合系数与同一接收种子的双线性行列式、每个种子在两条邻边上的精确换基关系，以及三个共享复形状下的完整两标量行方程。行列式单独消去了沿原种子的分量；该遗漏在下文显式恢复。尚未由这些方程推出一般全活跃三边的存在性或排除，也未证明它们在逻辑上强于已接受的完整向量门。**

这不是把旧负实射线和幅度环重新命名为新结果。本轮的具体产物是 TC.6、TC.12、TC.18–22：完整系数的共享坐标约化、遗漏项及其精确恢复。全程没有读本目录其他新稿，没有选择实际新频率、极化、幅度或时间；工具只用于文本读写与文件元数据，没有科学程序、数组、数值求值、扫描、Git、额度重置或外发。

## 1. 合同和本轮实际全文来源

固定同一组三个线性独立整数频率 \(p_1,p_2,p_3\)，记
\[
P_i=|p_i|^2>0,\qquad c_{ij}=p_i\cdot p_j\ne0,
\qquad P_i\ne P_j\quad(i\ne j).
\]
同一非零复种子 \(U_i\perp p_i\) 参与它的两条边，负模严格为共轭。全部三条边双向活跃，即所有 \(U_i\cdot p_j\ne0\;(i\ne j)\)。点积与叉积默认复双线性延拓；只在明确的模方、共轭和实虚部处使用 Hermitian 量。

本轮实际全文读取下列三个文件；只沿用其中已接受接口，并对本次所需公式重新手核。路径相对于 `research/reverse/`。

| 实读来源与使用范围 | SHA-256 |
|---|---|
| three-edge-compatibility/CONTRACT.md，全文合同 | 51909466ff2baf93b83d419775b0fbd2f1ceff4dec59c785358401d80ff01143 |
| mixed-polarization/MIXED_ROOT_INDEPENDENT.md，全文；重点 MI.17–21、MI.31、MI.34 的完整有序根和复缩放 | cad93f863ad371723d4510f20588a0f7abcee3e4f8e2984010f88ebcb2fc2dbf |
| net-mixed-cancellation/INDEPENDENT.md，全文；重点 NC.4–10 的完整相干和、NC.25–31 的既有门及其未付条件 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |

这三份的内部来源表不冒记为本轮实读。旧稿中的“待审”是其冻结时文本状态；本轮按合同给定的已接受接口使用，不将字节绑定当作新的非作者审查。没有新增外部定理或文献新颖性声明。

## 2. 完整单对和的接收种子行列式

固定有序边 \(i\leftarrow j\)，暂写 \(p,q,U,V\)，以及
\[
P=|p|^2,\ Q=|q|^2,\ c=p\cdot q,\ d=P-Q,
\quad\Delta=PQ-c^2>0,
\]
\[
\lambda_\pm=P+Q\pm2c,\quad E_\pm=4P+Q\pm4c,
\quad\Lambda=\lambda_+\lambda_->0,\quad\Omega=E_+E_->0.
\tag{TC.1}
\]
使用完整实基
\[
e=q-\frac cPp,\quad f=p-\frac cQq,\quad n=p\times q,
\qquad U=u e+v n,\quad V=x f+y n.
\]
活跃性保证 \(u x\ne0\)。记
\[
w_{ij}=v/u,\qquad w_{ji}=-y/x.
\tag{TC.2}
\]
负号来自反向边的法向 \(n_{ji}=-n\)，不是新选发送极化。

沿用已接受相干几何系数
\[
h_+=\frac{Q+2c}{\lambda_+E_+},\qquad
h_- =\frac{Q-2c}{\lambda_-E_-},
\]
\[
\alpha=2-d(h_++h_-),\quad
\beta=-d(h_+-h_-),\quad
\kappa=\frac{4cdP}{Q\Lambda},
\quad H=4P^2-PQ+Q^2-4c^2.
\]
再定义实几何量
\[
L=\frac{2\Delta^3}{P^2Q}>0,\qquad
\mathsf a=\frac{4cd(2P+Q)H}{Q\Lambda\Omega},
\]
并定义保留完整相干性的复标量
\[
\mathsf b=\kappa w_{ij}-\alpha\Re w_{ji}
+i\beta\Im w_{ji},
\qquad
\mathsf F_{ij}=(\kappa-\mathsf a)w_{ij}
-\alpha\Re w_{ji}+i\beta\Im w_{ji}.
\tag{TC.3}
\]
\(\mathsf a\) 允许为零，没有除以单向例外 \(H\)。NC.7–8 的完整 \(Z=G_++G_-\) 精确写成
\[
\boxed{Z_{ij}=iL u^2|x|^2
\bigl(\mathsf a e+\mathsf b n\bigr),
\qquad \mathsf b=\mathsf a w_{ij}+\mathsf F_{ij}.}
\tag{TC.4}
\]
核对相干号：若 \(z=y/x=-w_{ji}\)，则
\(x\overline y=|x|^2\overline z\)，所以
\(\alpha\Re(x\overline y)+i\beta\Im(x\overline y)
=|x|^2(\alpha\Re z-i\beta\Im z)\)。这正给 TC.3；没有去掉虚协方差。

令固有复双线性交替形式为
\[
\omega_p(X,Y)=p\cdot(X\times Y).
\]
因为 \(\omega_p(e,n)=\Delta\)，直接取坐标行列式得到
\[
\omega_p(U,Z)=\Delta(uZ_n-vZ_e),
\]
\[
\boxed{\omega_{p_i}(U_i,Z_{ij})
=iL_{ij}\Delta_{ij}u_{ij}^{\,3}|x_{ij}|^2\mathsf F_{ij}.}
\tag{TC.5}
\]
因此总混合零行必要地满足
\[
\boxed{\sum_{j\ne i}L_{ij}\Delta_{ij}
u_{ij}^{\,3}|x_{ij}|^2\mathsf F_{ij}=0.}
\tag{TC.6}
\]
这里的复三次因子仍在和内，不能先逐边除掉后相加。尤其不能以 \(|u_{ij}|^3\) 替换它来制造正权重。

## 3. 换基、复缩放和双线性自零边界

形式 \(\omega_p\) 由同一真实频率固定，不依赖横向坐标。若两个实基满足
\[
(e',n')=(e,n)T,\qquad
T=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in GL_2(\mathbb R),
\]
则在相关首坐标非零的图中
\[
u'=\frac{u(d-bw)}{\det T},\qquad
w'=\frac{aw-c}{d-bw},\qquad
\Im w'=\frac{\det T}{|d-bw|^2}\Im w.
\tag{TC.7}
\]
同时 \(\omega_p(e',n')=(\det T)\omega_p(e,n)\)，所以坐标行列式与基面积的乘积保持不变。TC.4 的具体几何系数属于频率定义的标准基，不能只改 \(w\) 而保留全部旧系数，误称这是换基后的同一公式。若某一般换基图的首坐标为零，固有 TC.5 之前的 \(\omega_p(U,Z)\) 仍有定义；本合同的标准邻边图因活跃性始终有效。

完整三层映射满足
\[
Z_{ij}(\zeta U_i,\eta U_j)=\zeta^2|\eta|^2Z_{ij}(U_i,U_j),
\]
\[
\boxed{\omega_{p_i}(\zeta U_i,
Z_{ij}(\zeta U_i,\eta U_j))
=\zeta^3|\eta|^2\omega_{p_i}(U_i,Z_{ij}).}
\tag{TC.8}
\]
因此整体接收相位不能逐邻边独立调节，发送整体相位完全约去，发送完整形状的相干实虚部却没有约去。

\(\omega_p\) 在复二维横向平面非退化；对非零 \(U\)，
\[
\omega_p(U,X)=0\iff X\in\mathbb C U.
\tag{TC.9}
\]
不需除以 \(U\cdot U\)。后者对非零复种子也可能为零，故用双线性自点积恢复平行系数会漏掉合法边界；下面改用已经保证非零的 \(U_i\cdot p_j\)。

## 4. 三个共享复形状的明确坐标

以下 \((i,j,k)\) 一律循环取 \((1,2,3),(2,3,1),(3,1,2)\)。记
\[
\tau=p_1\cdot(p_2\times p_3)\ne0,
\qquad g_i=P_i c_{jk}-c_{ij}c_{ik},
\qquad n_{ij}=p_i\times p_j,
\]
\[
A_i=U_i\cdot p_j\ne0,\qquad
t_i=\frac{U_i\cdot p_k}{U_i\cdot p_j}\ne0.
\]
则横向条件和两个点积唯一恢复同一原种子：
\[
\boxed{U_i=\frac{A_i}{\tau}
\bigl(n_{ki}+t_i n_{ij}\bigr).}
\tag{TC.10}
\]
这是原数据的坐标表示，没有为不同边指定新种子。反过来，在固定合同几何下，非零 \(A_i,t_i\) 给出非零横向且全部交叉点积非零的种子；这是符号参数化，未选择其中任何实际数据。

同一 \(U_i\) 的两个邻边比值严格为
\[
\boxed{
w_{ij}=\frac{\Delta_{ij}t_i-g_i}{P_i\tau},
\qquad
w_{ik}=\frac{g_i-\Delta_{ik}/t_i}{P_i\tau}.}
\tag{TC.11}
\]
例如 \(n_{ki}\cdot n_{ij}=-g_i\)，直接代入 TC.10 即得第一式，第二式用 \(n_{ik}=-n_{ki}\)。等价地，
\[
\boxed{
w_{ik}=\frac{g_iw_{ij}-\tau}{P_i\tau w_{ij}+g_i},
\qquad
\Delta_{ij}\Delta_{ik}=g_i^2+P_i\tau^2.}
\tag{TC.12}
\]
分母为 \(\Delta_{ij}t_i\ne0\)。后一 Gram 恒等式同时核实邻边换基：
\[
e_{ik}=\frac{g_i e_{ij}+\tau n_{ij}}{\Delta_{ij}},
\qquad
n_{ik}=\frac{-P_i\tau e_{ij}+g_i n_{ij}}{\Delta_{ij}}.
\tag{TC.13}
\]
该换基行列式为 \(\Delta_{ik}/\Delta_{ij}>0\)，没有人为反转接收横向定向。

共同种子的椭圆极化量也有坐标无关检验：
\[
\mathfrak h_i=\frac1{2i}
p_i\cdot(\overline U_i\times U_i)\in\mathbb R,
\]
\[
\boxed{
\mathfrak h_i=\Delta_{ij}|u_{ij}|^2\Im w_{ij}
=\frac{P_i|A_i|^2}{\tau}\Im t_i,
\quad
\Im w_{ik}=\frac{\Delta_{ik}}{\Delta_{ij}|t_i|^2}\Im w_{ij}.}
\tag{TC.14}
\]
所以同一种子在两个标准邻边图中的虚部必须同号或同为零。\(\mathfrak h_i=0\iff t_i\in\mathbb R\iff U_i\) 是一个非零复标量乘实向量。这里没有假定三个 \(\mathfrak h_i\) 为零，也没有把它们分别当作逐边可选参数。

## 5. 完整三行的两标量恢复

TC.3 的 \(\mathsf a_{i\ell},\mathsf b_{i\ell},\mathsf F_{i\ell}\) 均使用 TC.11 所强制的共同坐标。定义正实权重
\[
b_{ij}=\frac{P_j|A_j|^2|t_j|^2}{\Delta_{ij}}>0,
\qquad
b_{ik}=\frac{P_k|A_k|^2}{\Delta_{ik}}>0.
\tag{TC.15}
\]
下标的循环约定不能省略：在发送 \(j\) 的自身坐标中，\(U_j\cdot p_i=t_jA_j\)；在发送 \(k\) 的自身坐标中，\(U_k\cdot p_i=A_k\)。

令 \(X_i=Z_{ij}+Z_{ik}=6M_{0,i}\)。将 TC.4 中 \(u=P(U\cdot q)/\Delta\)、\(x=Q(V\cdot p)/\Delta\) 完整代入，得
\[
\boxed{X_i=2iA_i^2\left[
b_{ij}(\mathsf a_{ij}e_{ij}+\mathsf b_{ij}n_{ij})
+b_{ik}t_i^2(\mathsf a_{ik}e_{ik}+\mathsf b_{ik}n_{ik})
\right].}
\tag{TC.16}
\]
不同邻边的复相位差 \(t_i^2\) 保持在真实行和之内。

定义两个明确复标量
\[
\boxed{\mathfrak s_i=b_{ij}\mathsf F_{ij}
+b_{ik}t_i^3\mathsf F_{ik},}
\]
\[
\boxed{\mathfrak l_i=b_{ij}\mathsf a_{ij}\Delta_{ij}
+b_{ik}t_i^2\bigl(\mathsf a_{ik}g_i-P_i\tau\mathsf b_{ik}\bigr).}
\tag{TC.17}
\]
TC.5 和 TC.16 分别给
\[
\boxed{
\omega_{p_i}(U_i,X_i)=2iP_iA_i^3\mathfrak s_i,
\qquad
X_i\cdot p_j=\frac{2iA_i^2}{P_i}\mathfrak l_i.}
\tag{TC.18}
\]
第二式使用 \(e_{ik}\cdot p_j=g_i/P_i\) 和
\(n_{ik}\cdot p_j=-\tau\)，后一个负号对恢复式是必需的。

对任意 \(X\in p_i^\perp\)，由 \(U_i\cdot p_j=A_i\) 及
\(\omega_{p_i}(U_i,n_{ij})=P_iA_i\)，有准确恒等式
\[
X=\frac{X\cdot p_j}{A_i}U_i
+\frac{\omega_{p_i}(U_i,X)}{P_iA_i}n_{ij}.
\tag{TC.19}
\]
于是完整相干行得到
\[
\boxed{X_i=\frac{2iA_i}{P_i}\mathfrak l_iU_i
+2iA_i^2\mathfrak s_i n_{ij}.}
\tag{TC.20}
\]
因为 \(U_i\) 与 \(n_{ij}\) 复线性独立，本合同域内有完整等价：
\[
\boxed{M_0=0\iff
\mathfrak s_i=\mathfrak l_i=0\quad(i=1,2,3).}
\tag{TC.21}
\]
负接收是共轭，未增加自由参数。这是同一组三个复形状 \(t_i\)、三个正幅度 \(|A_i|^2\) 下的精确两标量系统；整体相位 \(A_i/|A_i|\) 不影响其零条件。

遗漏项还可用 \(\mathsf F_{ik}\) 显示得更直接。TC.11 与
\(\mathsf b_{ik}=\mathsf a_{ik}w_{ik}+\mathsf F_{ik}\) 给
\[
\boxed{\mathfrak l_i=
b_{ij}\mathsf a_{ij}\Delta_{ij}
+b_{ik}\bigl(\mathsf a_{ik}\Delta_{ik}t_i
-P_i\tau t_i^2\mathsf F_{ik}\bigr).}
\tag{TC.22}
\]
只检查 \(\mathfrak s_i=0\) 时，TC.20 剩下的是
\(X_i=(2iA_i/P_i)\mathfrak l_iU_i\)，而不是自动零。TC.22 的第一项和与 \(t_i\) 成正比的项没有被行列式删去条件控制，仍须实付。

作为遗漏确实出现在完整单对映射中的核验，在符号域 \(P>Q,c\ne0,ux\ne0\) 的频率平面输入 \(w_{ij}=w_{ji}=0\) 下，\(\mathsf F_{ij}=0\) 而 \(H=(P-Q)(4P-Q)+4\Delta>0\)，故 \(\mathsf a\ne0\) 且 \(Z\in\mathbb C U\setminus\{0\}\)。这只核验单对映射的核内输出；没有把两个邻边都独立设成平面输入，也不构成满足三行 \(\mathfrak s_i=0\) 而未满足 TC.21 的共同三对反例。本稿未证明这样的三行反例存在。

## 6. 尚不能闭合的虚部项

写 \(\mathsf F_{ij}=f_{ij}+ig_{ij}\)，其中
\[
f_{ij}=(\kappa_{ij}-\mathsf a_{ij})\Re w_{ij}
-\alpha_{ij}\Re w_{ji},
\]
\[
g_{ij}=(\kappa_{ij}-\mathsf a_{ij})\Im w_{ij}
+\beta_{ij}\Im w_{ji}.
\tag{TC.23}
\]
TC.14 允许将这里的虚部写成同一顶点的 \(\mathfrak h_i\)，但不能把整个行列式零式改成具有正权重的线性椭圆极化方程。若
\(t_i^3=r_i+is_i\)，TC.17 的实虚部准确为
\[
b_{ij}f_{ij}+b_{ik}(r_if_{ik}-s_ig_{ik})=0,
\]
\[
\boxed{b_{ij}g_{ij}+b_{ik}(r_ig_{ik}+s_if_{ik})=0.}
\tag{TC.24}
\]
其中
\[
r_i=\Re t_i\bigl((\Re t_i)^2-3(\Im t_i)^2\bigr),
\quad
s_i=\Im t_i\bigl(3(\Re t_i)^2-(\Im t_i)^2\bigr).
\]
即使 \(\Im t_i\) 的符号固定，\(s_i\) 仍不具有由此强制的固定符号，\(r_i\) 也不是正权重。\(s_if_{ik}\) 混入接收的复相位和发送的实相干形状，不能因各个 \(b\) 正而去掉。再加上 TC.22 中未消失的平行分量，当前推导未形成可用于三行联合排除的正性闭合。

这准确指出了尝试从行列式直接强迫全部线性极化时尚缺的项，**不证明以后不可能利用 TC.21 的全部方程消去它们**。也没有以“项无固定号”、未知量计数或未找到参数来宣称三边存在或不可解。

## 7. 已完成范围

本轮新推导提供了完整有序相干系数的固有行列式 TC.5–6、共享极化的 Möbius 约束及椭圆极化量 TC.10–14、和保留遗漏平行分量的精确三行系统 TC.17–22。它们没有丢弃确定性虚相干，没有自由化邻边极化，允许 \(H_{ij}=0\)、\(\mathsf F_{ij}=0\)、\(\mathfrak h_i=0\) 和 \(U_i\cdot U_i=0\) 等本合同内边界。

TC.21 与原完整 \(M_0=0\) 等价，故本稿没有宣称它逻辑上强于已接受的负射线和共同幅度环门。本轮价值限于将共享形状与标量遗漏写明，便于下一次有界解析检验；没有把旧门再报告为新的排除。

一般全活跃三边的 \(M_0=0,W_0\ne0\) 仍 OPEN：即使 TC.21 可解，还必须在同一数据上核验 \(W_{0,i}=\sum_{j\ne i}C_{ij}/3\) 不全为零。本文没有求解或接受该条件。正交、等长、失活或线性相关几何不在本合同中，不用当前分母公式延伸宣称它们的分类。

所有等式是有限空间首项的精确代数式，代数余项为零；本文未建立新的正时间结论，未调用或新增 SOURCE_BRIDGE 的真实全 Fourier 余项。\(M_0=0\) 不是正时间完整混合项恒零，更不是模板返回、两步再生成或原解闭合。统一迭代、同一初值无限尺度、无限维跨代余项、有限总时间、奇性及全局正则性均未支付。SHARED-SHAPE SCALAR REDUCTION；OPEN；NO-CANDIDATE；NOT CLAY。
