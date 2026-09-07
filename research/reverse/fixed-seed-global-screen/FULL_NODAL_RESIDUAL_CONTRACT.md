# 固定 n1280 的完整节点残差双边合同

2026-09-08。PRIVATE_CORE。解析合同，尚未实现或执行新的科学核。对象仍是原固定六模初值、ν=1、T³₂π问题中已保存的唯一 Hermite 参照在 n1280、t*=1280/2048=5/8 的值及物理时间斜率；参照不是原 NS 解。本合同只生成这个节点的 r₀、r₂ 双边界，不增加节点、时间段或全时间窗结论。

本轮独立核对了下列完整残差的符号、Leray 分母、二阶导数权重、零模及对称张量计数；未重算节点、中心、卷积或残差。已有单张量的主/独立全输出比较记录已实读，最终验收仍由根代理当前收束的独立审查负责。

## 1. 原参照、范数和复用输入

固定 G=[-8,8]³\{0}，含4912个双符号模式；完整输出集合 H=[-16,16]³，含35937个模式。所有频率均是物理整数 k，不是打包后的平移索引。

令 Q=2⁵²，L*=lcm{|k|²:k∈G}，D=2 Q L*。从原 n1280 的 value_q52 和 slope_q52 分别按 C¹ 合同作任意精度整数提升、共轭平均、完整 P_k 投影，得到

\[
c_k=A_k/D,\qquad d_k=J_k/D,\qquad k\in G.
\tag{NR.1}
\]

A、J为Gaussian整数三向量；G外均置零，包括零模。L*是共同分母的最小公倍数，下面的线性项 L_k 是向量，二者不混用。两份原场均须精确无散、共轭对称、均值零。已有单张量只重建了值；本合同还必须从原斜率档案重建 J，不能从中心或非线性输出猜斜率。

中心分母固定 QP=2⁹⁶。C_k是对 QP A_k/D 各实虚标量最近整数、平局取偶所得，\(\widetilde c=C/QP\)。本合同复用已有完整29472标量中心和完整 \(T^{12}\) 档案，不重新选中心或精度。已有两条路径对全部中心、全部71874输出标量及舍入见证的精确比较，见第7节绑定。

采用归一化空间L²：\(\|f\|_2^2=(2\pi)^{-3}\int|f|^2=\sum_k|f_k|^2\)。\(D^2f\) 包含全部有序二阶空间导数和三个向量分量，因此其 Fourier 权重是 \(|k|^4\)，不是 \(|k|^2\)，也不是非齐次H²权重。定义

\[
R=d-\Delta c-B(c,c),\qquad r_j=\|D^jR\|_2,\quad j=0,2.
\tag{NR.2}
\]

这里的 R 是唯一参照在 t* 的完整方程残差，不是实际NS解的残差或误差。

## 2. 六个张量与完整保守非线性

对每个 k∈H 定义整数复卷积

\[
T^{j\ell}_k=\sum_{p,q\in G,\ p+q=k}C_p^j C_q^\ell.
\tag{NR.3}
\]

复用已认证的 \(T^{12}\)。另五项 \(T^{11},T^{13},T^{22},T^{23},T^{33}\) 必须各自保留全部35937个复输出、完整有序供给及相位。它们没有继承 \(T^{12}\) 的计算PASS。算术实现和独立审核另行锁定，本合同不重写已有Kronecker引理或预估其成本。

交换哑变量 p,q 并用标量乘法交换性，得到 \(T^{j\ell}=T^{\ell j}\)。因此只保存六项足够，但重建对称3×3张量后，下面每个 j 项恰出现一次；非对角项不得额外乘2。输出零频的张量一般不为零，仍须保留。

中心一般不无散。本合同始终使用

\[
\mathcal C_{\rm cons}(f,g)_k
=-iP_k\sum_{j=1}^3 k_j(f^j*g)_k.
\tag{NR.4}
\]

只有对原精确无散 c，才可用 \(\mathcal C_{\rm cons}(c,c)=B(c,c)\)：逐输入有 \(c_p\cdot q=c_p\cdot k\)。不得把非无散中心的NR.4误称为它的 \(-P(f\cdot\nabla)f\)。这一步完整保留周期压力投影。

## 3. 每个非零输出的唯一整数分子

对 k∈H\{0}，令 s=|k|²，定义

\[
L_k=J_k+sA_k,\qquad
F_k^\ell=\sum_{j=1}^3 k_jT_k^{j\ell},\qquad
N_k=sF_k-k(k\cdot F_k).
\tag{NR.5}
\]

G外的L_k严格为零；F、N依然使用完整H上的非线性输出，不能再次截回G。由于 \(P_kF_k=N_k/s\)，保留原精确线性项的中心残差为

\[
\widehat R_k=\frac{L_k}{D}
-\mathcal C_{\rm cons}(\widetilde c,\widetilde c)_k
=\frac{L_k}{D}+\frac{iN_k}{sQP^2}
=\frac{V_k}{DsQP^2},
\quad V_k=sQP^2L_k+iDN_k.
\tag{NR.6}
\]

所以根提出的加号 \(+iDN_k\) 正确。为避免复实现中的符号混淆，应逐分量保留

\[
\Re V=sQP^2\Re L-D\Im N,\qquad
\Im V=sQP^2\Im L+D\Re N.
\tag{NR.7}
\]

先把同一输出的原斜率、黏性及完整非线性有符号合并成V，再取平方；不得先对这些项取范数或绝对值。定义非负整数

\[
S_k=|V_k|^2=\sum_{\ell=1}^3[(\Re V_k^\ell)^2+(\Im V_k^\ell)^2].
\tag{NR.8}
\]

原c、d共轭，中心和张量亦共轭。k换为−k时，F与N取负共轭，故iN及V取共轭；这是完整符号链的检查。另有 \(k\cdot N=0\)、\(k\cdot L=0\)、\(k\cdot V=0\)。完整输出应核这三条恒等式及共轭，不把它们单独当作全部算术正确性的证明。

零模不使用含s的公式：c₀=d₀=0，NR.4的输出因子k=0，故 \(\widehat R_0=R_0=0\)。张量零模可以非零，却经完整输出收缩严格消去；不得对s=0作除法，也不能人为给零模加入压力项。

## 4. 全谱平方范数和不引入输出LCM的包围

记共同正整数 \(H_0=D^2QP^4=(DQP^2)^2\)。归一化Parseval给

\[
\boxed{\|D^2\widehat R\|_2^2
=\frac{A_2}{H_0},\quad A_2=\sum_{k\in H\setminus\{0\}}S_k,}
\tag{NR.9}
\]

因为每个输出的二阶导数平方权重是s²，恰好约去NR.6分母的s²。这个求和是完整35936个非零双符号输出，不使用半谱或额外因子2。

零阶范数精确为

\[
\|\widehat R\|_2^2
=\frac1{H_0}\sum_{k\ne0}\frac{S_k}{s^2}.
\tag{NR.10}
\]

逐模式作整数Euclidean除法

\[
S_k=s^2 a_k+\rho_k,\quad0\le\rho_k<s^2,
\quad A_0^-=\sum a_k,\quad
A_0^+=A_0^-+\#\{k:\rho_k\ne0\}.
\tag{NR.11}
\]

则

\[
\boxed{\frac{A_0^-}{H_0}\le\|\widehat R\|_2^2
\le\frac{A_0^+}{H_0},\qquad
0\le\frac{A_0^+-A_0^-}{H_0}\le\frac{35936}{H_0}.}
\tag{NR.12}
\]

这里整数取整只扩大零阶平方范数的最终包围；V、S及二阶平方范数仍精确，没有舍入每模速度/残差，也没有改变中心。无需形成所有输出s²的巨大LCM。保存完整S_k或足以独立逐模重算它们的完整V及张量/节点绑定，并保存全部a_k、ρ_k或与完整S逐模复算连接的总和证据，不能只给未经来源连接的三个总数。

根号端点可作有理认证而不使用浮点：对任意固定P=2^b和非负整数A，取

\[
\ell=\operatorname{isqrt}\left(\left\lfloor P^2A/H_0\right\rfloor\right),\qquad
u=\ell+\mathbf1_{\ell^2H_0\ne P^2A}.
\tag{NR.13}
\]

由 \(\ell^2H_0\le P^2A<(\ell+1)^2H_0\) 得
\(\ell/P\le\sqrt{A/H_0}\le u/P\)。实现前须一次固定b及整数保护/停止规则，本解析合同不通过试算选择精度。用A₀⁻的下端与A₀⁺的上端给 \(\underline h_0,\overline h_0\)，用A₂的两个端点给 \(\underline h_2,\overline h_2\)。这也可先以精确根式表达；未执行根号或输出数值靶标。

## 5. 从中心双边界连接原精确节点

复用已通过另一条原节点重建及舍入见证连接的

\[
M=\sum_{k,\ell}(|\Re c_k^\ell|+|\Im c_k^\ell|),\qquad
\delta=\sum_{k,\ell}(|\Re(c-\widetilde c)_k^\ell|
+|\Im(c-\widetilde c)_k^\ell|),
\]
\[
E_j=28^{j+1}(2M\delta+\delta^2),\quad j=0,2.
\tag{NR.14}
\]

这个连接的完整有理值已存于 kronecker-independent-agreement.json；后续实现必须核相同c、C、QP、模式顺序、M、δ来源，不可仅因为误差很小就跳过绑定。CR预审已证明NR.14：完整H的|k|<28，Leray收缩，以及保守双线性算子差的三项展开，给
\(\|D^j[R-\widehat R]\|_2\le E_j\)。本合同不改变该误差合同。

三角及反三角不等式因此给原精确参照节点的双边门

\[
\boxed{\max(0,\underline h_j-E_j)\le r_j
\le\overline h_j+E_j,\qquad j=0,2.}
\tag{NR.15}
\]

误差在范数层面加减，不能从A₂或S_k直接减E₂，也不能把E₂当平方范数误差。原斜率d、黏性以及原c均保持精确，只有非线性中心与原c的差由E_j支付。

旧 \(\varepsilon=2\times10^{-7}\) 包络在这个节点要求

\[
r_2(t_*)\le\varepsilon e^{-5/4},\qquad
r_0(t_*)\le(\varepsilon/64)e^{-5/4}.
\tag{NR.16}
\]

它是否被完整节点否定仍是待测问题。未来若NR.15的严格下界已大于相应阈值，并用有理外包认证指数比较，则该包络被这个节点拒绝；若上界不超过阈值，仅证明这个节点满足相应门；区间跨越阈值则保持未定。没有完整节点新结果前，不用旧浮点6.819e−8作本合同的结果或拒绝证据。

即便两个节点门都通过，也没有任何邻域、连续时间或全窗余项上界。拒绝的对象是指定参照加指定误差包络，不是实际原NS解、其它后验方法或所有奇性路线。

## 6. 实现前的必要证据和停止边界

此文件只锁定数学对象与可审公式。后续须另审源码、实际一次计算预算、根号精度、输出档案与失败保留规则；现在不启动科学核，也不依据单张量耗时预测全部残差成本。

实际完整节点证据至少要连接：原三份档案和n1280值/斜率；完整A、J或可独立重建的绑定；已存C与T¹²；新五份完整对称张量；全部物理输出k、F、N、V、S；零模、共轭和投影恒等式；A₂、A₀⁻、A₀⁺及有理根号端点；相同M、δ、E_j；最终NR.15的完整r₀/r₂双边区间。所有phase、线性/非线性相消都应能从所存精确整数回查。

有限独立审查须核NR.6的符号、s权重和六张量接口，不能因前项T¹²通过就替剩余张量或完整残差预填PASS。源码/输入发生变化、缺一个张量、遗漏G外输出、原斜率未绑定、零模处理不明、或未完成资源门时，只记录未认证，不给完整节点结论。该合同没有新的NS构造、连续控制、全局正则性或奇性证明。

## 7. 复用来源与本轮已读证据

本轮实读连续残差预审及根审（前一有界任务已全文读，不重复推导打包）、KRONECKER_COMPLETE_OUTCOME.md、KRONECKER_PRIMARY_RESULT_REVIEW.md、kronecker-independent-agreement.json。下面五项单块数据/记录的SHA本轮再次以文件字节实际核对；没有解码其中的科学数组或重算原节点。

| 复用来源（相对此目录） | SHA-256 |
| --- | --- |
| C1_RESIDUAL_CONTRACT.md | a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251 |
| CONTINUOUS_RESIDUAL_COST_PREFLIGHT.md | 0c7ea4b3d33d152f298058a909e446505150d1004529f1a4518c2e1fedc7f796 |
| CONTINUOUS_RESIDUAL_COST_ROOT_REVIEW.md | 4865cf0639e20bc6d8d6c2546e8382c08b59366814168ff2f0b309bc8ef4e5da |
| node-trial-01/manifest.json | 5ac2abdfb7a14a38904f2ef1c58d81cf90bea776ce5426a56a75c6f81622c1cd |
| node-trial-01/modes.npy | f184c97c52e561ac53b8936ee51e68690517ad65c79e8050c93a891ac8856896 |
| node-trial-01/block-01280-01343.npz | abf3b33282ff0b08e995c6aa1f80e7d79dbd64a55137574b77d51356b236297e |
| kronecker-block-trial-02/c96-centers.i112le.bin | c16d26dcbea14b63614d192da27a8b268fa49e689a02fb15499601cc1b611c9e |
| kronecker-block-trial-02/tensor12-complex.i240le.bin | 795ce995481d41b1fd4c6810101b62d37b187a268eaba992e97ef6f3f79ca0e6 |
| kronecker-block-trial-02/run.json | 375921aff0ceae1294b7d79947d9dfeaf817ad65ce9edc6c02b9b152ac922d70 |
| kronecker-direct-independent-trial-01/run.json | e4d54cf0690702f54029b4c36412d9d922e14a632090e5a4ac88f2e8b8e293e7 |
| kronecker-independent-agreement.json | 5510285fed346165e428bac4dfcb572548283322937a712be6465829481b5779 |

单块完整比较状态及输入见证来自已存精确比较记录，不把本轮只读SHA核对称为再次独立科学计算。前项最终审查的稳定版本须由后续执行入口绑定；当前不猜测或预填其最终哈希。
