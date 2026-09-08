# 两边星形在线性极化子域的中心方向约化

2026-09-08，PRIVATE_CORE。状态：**闭合了中心方向与叶间不活跃的精确几何条件；其在合同整数频率域内的实现性仍 OPEN，待非作者审查。**

本稿沿同目录合同和本人已接受的独立稿，只考察三条频率对均非正交、三个长度平方互异、两条中心—叶边活跃而叶—叶边不活跃的星形。额外明示假设：每个原种子均为非零复标量乘一个非零实横向向量。本稿不声称一般星形必满足这一假设，也未读取另一代理的极化分析、根主稿或根审查。这里所有极化分解都属于同一个中心种子；没有为两条边分别选择中心极化。

全部推导为手工符号；工具仅用于读写文本和 SHA-256。不运行科学程序、数组、数值求值、参数扫描、Git、额度重置或外发；没有选取实际频率、极化或时间。本人已接受的 INDEPENDENT.md 保持字节不变。

## SC.1 完整作用与当前子域

沿用完整双有序 Fourier–Leray 作用
\[
\mathfrak B(X,Y;r,s)
=-iP_{r+s}[(X\cdot s)Y+(Y\cdot r)X],
\qquad P_k=I-\frac{k\otimes k}{|k|^2}.
\tag{SC.1}
\]
点积为复双线性点积。对接收 \(p\)、发送 \(q\)，\(V_+=V,V_-=\bar V\)，定义
\[
N_\sigma=\mathfrak B(U,V_\sigma;p,\sigma q),\quad
T_\sigma=\mathfrak B(U,N_\sigma;p,p+\sigma q),
\]
\[
G_\sigma=\mathfrak B(V_{-\sigma},T_\sigma;-\sigma q,2p+\sigma q),
\quad Z=G_++G_-,
\quad C=\mathfrak B(N_+,N_-;p+q,p-q).
\tag{SC.2}
\]
下文约化的是完整 \(Z\)，未删除根、投影或共轭。对原种子的缩放保留
\[
Z(zU,wV)=z^2|w|^2Z(U,V),\qquad
C(zU,wV)=z^2|w|^2C(U,V).
\tag{SC.3}
\]

记中心频率为 \(p\)，两叶为 \(q_1,q_2\)。三者线性独立且为合同规定的整数向量；当前始终要求三对内积非零、三个长度平方互异。令
\[
P=|p|^2,\quad Q_j=|q_j|^2,\quad c_j=p\cdot q_j,\quad
\Delta_j=PQ_j-c_j^2>0,\quad d_j=P-Q_j.
\]
实际原种子写成
\[
U_0^{\rm act}=z_0U,\qquad U_j^{\rm act}=z_jV_j,
\qquad z_0,z_1,z_2\in\mathbb C\setminus\{0\},
\tag{SC.4}
\]
其中 \(U,V_1,V_2\) 是实横向向量。本稿只在这一显式线性极化子域作结论。

每条中心—叶边使用
\[
e_j=q_j-\frac{c_j}{P}p,\quad
f_j=p-\frac{c_j}{Q_j}q_j,\quad n_j=p\times q_j,
\]
\[
U=u_je_j+v_jn_j,\qquad
V_j=x_jf_j+y_jn_j,\qquad u_jx_j\ne0.
\tag{SC.5}
\]
这里 \(u_j,v_j,x_j,y_j\) 均为实数，且两组 \(u_j,v_j\) 分解同一个 \(U\)。

叶—叶边不活跃，故叶行 \(M_0=0\) 就要求各叶接收中心的完整 \(Z_{j0}=0\)。独立稿 NC.16 的充要条件给出
\[
4c_j^2=P^2-PQ_j+4Q_j^2,\qquad
Q_j<P<4Q_j,\qquad
\Delta_j=\frac{(P-Q_j)(4Q_j-P)}4,
\tag{SC.6}
\]
\[
\frac{y_j}{x_j}=\alpha_j\frac{v_j}{u_j},
\qquad
\alpha_j=\frac{3P-2Q_j}{2c_j}.
\tag{SC.7}
\]
交换接收与发送时，法向由 \(p\times q_j\) 变为其负向，接收和发送的法向坐标都变号；代入实比值后恰得 SC.7。因此这里没有遗漏交换方向的符号。SC.6 强制中心严格最长。

## SC.2 完整中心系数及 \(b_j>2\)

暂省去下标 \(j\)，以下所有符号均属于同一条中心—叶边。定义
\[
\lambda_\pm=P+Q\pm2c,\quad E_\pm=4P+Q\pm4c,\quad
\Lambda=\lambda_+\lambda_-,\quad\Omega=E_+E_-,
\]
\[
h_\pm=\frac{Q\pm2c}{\lambda_\pm E_\pm},\qquad
\rho=2-d(h_++h_-),\qquad
\kappa=\frac{4cdP}{Q\Lambda},
\]
\[
H=4P^2-PQ+Q^2-4c^2,\qquad
\chi=\frac{4cd(2P+Q)H}{Q\Lambda\Omega},\qquad
L=\frac{2\Delta^3}{P^2Q}>0.
\tag{SC.8}
\]
所有分母严格为正；\(d>0\)。将 SC.7 代入完整 NC.7–8（实代表中 \(\Im(x\bar y)=0\)）给出
\[
\boxed{Z_{0j}(U,V_j)=
iL_ju_j^2x_j^2
\left[\chi_je_j+
(\alpha_j\rho_j+\kappa_j)\frac{v_j}{u_j}n_j\right].}
\tag{SC.9}
\]
定义完整方向系数
\[
\boxed{b_j=\frac{\alpha_j\rho_j+\kappa_j}{\chi_j}.}
\tag{SC.10}
\]
SC.6 化简各几何因子为
\[
\Lambda=3Qd,\qquad
\Omega=3(4P^2+4PQ-5Q^2),\qquad
H=3d(P+Q)>0,
\]
\[
\chi=\frac{4cd(2P+Q)(P+Q)}
{3Q^2(4P^2+4PQ-5Q^2)}.
\tag{SC.11}
\]
特别地 \(\chi\) 的符号恰为 \(c\)。

先可不展开多项式证明 \(\rho>0\)。令 \(s_\sigma=Q+2\sigma c\)，则
\(\lambda_\sigma=P+s_\sigma\)、\(E_\sigma=4P-Q+2s_\sigma\)。
若 \(s_\sigma\le0\)，则 \(dh_\sigma\le0\)；若 \(s_\sigma>0\)，则
\[
\lambda_\sigma E_\sigma-ds_\sigma
=P(4P-Q)+5Ps_\sigma+2s_\sigma^2>0.
\]
两种情况均给 \(1-dh_\sigma>0\)，从而 \(\rho>0\)。\(\alpha,\kappa,\chi\) 同为 \(c\) 的符号，因此 \(b>0\)。

这里还可闭合更强的界。直接通分 SC.10，设 \(r=P/Q\in(1,4)\)、\(s=r-1\in(0,3)\)，得到
\[
\boxed{
b-2=
\frac{8r^4+20r^3+47r^2-84r+36}
{(r^2-r+4)(r-1)(2r+1)(r+1)}
=
\frac{27+102s+155s^2+52s^3+8s^4}
{(s^2+s+4)s(2s+3)(s+2)}>0.}
\tag{SC.12}
\]
供手核的中间通分式如下。记
\[
\mathcal L=4P^2+4PQ-5Q^2,\qquad
\mathcal B=2P^3-3P^2Q+6PQ^2+Q^3.
\]
则
\[
h_++h_-=-\frac{2\mathcal B}{\Lambda\mathcal L},\qquad
\rho=2+\frac{2\mathcal B}{3Q\mathcal L},
\]
\[
b=
\frac{4P^5+6P^4Q+30P^3Q^2+57P^2Q^3-98PQ^4+28Q^5}
{(P^2-PQ+4Q^2)(P-Q)(2P+Q)(P+Q)}.
\tag{SC.13}
\]
分子减去分母的两倍，即为
\(Q(8P^4+20P^3Q+47P^2Q^2-84PQ^3+36Q^4)\)。
再除以相应 \(Q\) 次幂并平移 \(r=1+s\)，得到 SC.12。这里没有借助数值求值或软件展开。

在中心平面 \(p^\perp\) 上定义实对称算子
\[
T_j=\Pi_{e_j}+b_j\Pi_{n_j},
\qquad
\Pi_e X=\frac{X\cdot e}{|e|^2}e.
\tag{SC.14}
\]
两条投影互补，故 \(T_j\) 正定，两个特征值是 \(1,b_j>2\)。SC.3、9 化为
\[
\boxed{
\frac{Z_{0j}^{\rm act}}{iz_0^2}
=|z_j|^2L_jx_j^2\chi_ju_j\,T_jU.}
\tag{SC.15}
\]
每条中心向量均非零。共同的 \(iz_0^2\) 相位不改变两项是否严格相反；发送相位只留下正因子 \(|z_j|^2\)，不能改变射线。

## SC.3 同一中心极化的方向二次式

令 \(\ell_j=|e_j|=\sqrt{\Delta_j/P}\)。选取由实际频率给出的定向正交基
\[
E=\frac{e_1}{\ell_1},\qquad
N=\frac{n_1}{\sqrt P\,\ell_1}.
\]
这里是符号坐标选择，不是选择频率或原数据。记
\[
\mathsf C=\frac{e_1\cdot e_2}{\ell_1\ell_2},\qquad
\mathsf S=\frac{(p/\sqrt P)\cdot(e_1\times e_2)}{\ell_1\ell_2}.
\tag{SC.16}
\]
\(\mathsf C^2+\mathsf S^2=1\)，线性独立性保证 \(\mathsf S\ne0\)，所以
\[
e_2=\ell_2(\mathsf CE+\mathsf SN),\qquad
n_2=\sqrt P\,\ell_2(-\mathsf SE+\mathsf CN).
\]
第一条边活跃允许且只允许写
\[
U=a(E+\omega N),\qquad a\in\mathbb R\setminus\{0\},
\]
\[
u_1=\frac a{\ell_1},\quad \frac{v_1}{u_1}=\frac{\omega}{\sqrt P},\qquad
u_2=\frac{a(\mathsf C+\mathsf S\omega)}{\ell_2},\quad
\frac{v_2}{u_2}=
\frac{-\mathsf S+\mathsf C\omega}{\sqrt P(\mathsf C+\mathsf S\omega)}.
\tag{SC.17}
\]
第二条边活跃要求 \(\mathsf C+\mathsf S\omega\ne0\)。

定义
\[
A_\theta=\mathsf C^2+b_2\mathsf S^2,\quad
B_\theta=(1-b_2)\mathsf C\mathsf S,\quad
D_\theta=\mathsf S^2+b_2\mathsf C^2.
\]
则
\[
T_1U=a(E+b_1\omega N),\qquad
T_2U=a[(A_\theta+B_\theta\omega)E+
(B_\theta+D_\theta\omega)N].
\]
中心方向行列式因此完全等价于一个实二次式：
\[
\boxed{
\det_{p^\perp}(T_1U,T_2U)=a^2F(\omega),\qquad
F(\omega)=B_\theta+(D_\theta-b_1A_\theta)\omega
-b_1B_\theta\omega^2.}
\tag{SC.18}
\]

由于 \(T_1,T_2\) 正定，它们作用于同一非零 \(U\) 后如果共线，比例必为严格正实数：分别与 \(U\) 点乘即可。因此 SC.15 的两个完整中心向量处于严格负实射线的充要条件是
\[
\boxed{
F(\omega)=0,\qquad
c_1c_2(\mathsf C+\mathsf S\omega)<0.}
\tag{SC.19}
\]
第二式也自动保留第二条边的活跃性。这里“严格负实射线”指存在 \(\eta>0\) 使
\(Z_{01}^{\rm act}=-\eta Z_{02}^{\rm act}\)；正幅度随后才用于把 \(\eta\) 支付为一，SC.19 没有暗中完成这一选择。

## SC.4 一个无需求斜率的几何障碍

SC.19 进一步迫使
\[
\boxed{c_1c_2\mathsf C<0.}
\tag{SC.20}
\]
证明如下。写 \(E_j=e_j/\ell_j\)，假定
\(T_1U=\lambda T_2U\)，由正定性 \(\lambda>0\)。
活跃性 \(U\cdot E_1\ne0\) 给
\[
\lambda
=\frac{U\cdot T_1U}{U\cdot T_2U}
<b_1.
\]
这里分子严格小于 \(b_1|U|^2\)，分母至少 \(|U|^2\)。
令 \(a_j=U\cdot E_j\ne0\)，将算子恒等式与 \(E_2\) 点乘得
\[
(b_1-\lambda)a_2=(b_1-1)\mathsf C a_1.
\tag{SC.21}
\]
因左右实系数 \(b_1-\lambda,b_1-1\) 严格为正，
\(\mathsf C\ne0\) 且 \(\operatorname{sgn}(a_1a_2)=\operatorname{sgn}\mathsf C\)。
而 SC.15 的负射线恰要求 \(c_1c_2a_1a_2<0\)，得到 SC.20。

故 \(c_1c_2\mathsf C\ge0\) 的全部当前几何均不能实现中心相消。对原频率内积，这写成
\[
c_1c_2\left(q_1\cdot q_2-\frac{c_1c_2}{P}\right)<0.
\]
SC.6 还给 \(c_j^2/\Delta_j\ge3\)，而 \(|\mathsf C|<1\)，所以必要地
\[
\boxed{\frac23<
\frac{P(q_1\cdot q_2)}{c_1c_2}<1.}
\tag{SC.22}
\]
确切地，
\[
\frac{P(q_1\cdot q_2)}{c_1c_2}
=1+\frac{\sqrt{\Delta_1\Delta_2}}{c_1c_2}\mathsf C;
\]
SC.20 使第二项为负，其绝对值严格小于 \(1/3\)。
SC.20、22 只是必要条件，不能用作几何已实现或行列式已为零的证据。

## SC.5 叶间不活跃与纯几何消元

在当前实代表和非零复缩放下，叶—叶边不活跃的完整条件是
\[
(V_1\cdot q_2)(V_2\cdot q_1)=0.
\tag{SC.23}
\]
至少一项为零即可；不能额外假设两项同时为零。保持 SC.7、17 后，定义
\[
\mathcal I_1(\omega)=
\alpha_1Q_1\mathsf S\omega-c_1\mathsf C
+c_2\frac{\ell_1}{\ell_2},
\]
\[
\mathcal I_2(\omega)=
\left(c_1\frac{\ell_2}{\ell_1}-c_2\mathsf C\right)
(\mathsf C+\mathsf S\omega)
+\alpha_2Q_2\mathsf S(\mathsf S-\mathsf C\omega).
\tag{SC.24}
\]
则 SC.23 等价于
\[
\boxed{\mathcal I_1(\omega)\mathcal I_2(\omega)=0.}
\tag{SC.25}
\]
两者都是实一次式（允许 \(\mathcal I_2\) 的一次系数退化）。
其直接核查依据是
\[
f_1\cdot q_2=\frac{\ell_1^2c_2-c_1\ell_1\ell_2\mathsf C}{Q_1},
\quad n_1\cdot q_2=\sqrt P\,\ell_1\ell_2\mathsf S,
\]
\[
f_2\cdot q_1=\frac{\ell_2^2c_1-c_2\ell_1\ell_2\mathsf C}{Q_2},
\quad n_2\cdot q_1=-\sqrt P\,\ell_1\ell_2\mathsf S.
\]
代入 SC.7、17 后，分别有
\[
V_1\cdot q_2=\frac{x_1\ell_1\ell_2}{Q_1}\mathcal I_1(\omega),
\]
\[
V_2\cdot q_1=
\frac{x_2\ell_1\ell_2}{Q_2(\mathsf C+\mathsf S\omega)}
\mathcal I_2(\omega).
\tag{SC.26}
\]
分母在活跃域严格非零，故等价性保留全部允许分支。

特别地，在 \(\mathcal I_1=0\) 分支，设
\[
\mathcal D_1=\alpha_1Q_1\mathsf S\ne0,\qquad
\mathcal N_1=c_1\mathsf C-c_2\frac{\ell_1}{\ell_2}.
\]
叶间不活跃已经固定唯一斜率
\(\omega=\mathcal N_1/\mathcal D_1\)。将其代入 SC.19，得到只含频率几何的精确检验：
\[
\boxed{
B_\theta\mathcal D_1^2
+(D_\theta-b_1A_\theta)\mathcal N_1\mathcal D_1
-b_1B_\theta\mathcal N_1^2=0,}
\tag{SC.27}
\]
\[
\boxed{
c_1c_2(\mathsf C\mathcal D_1+\mathsf S\mathcal N_1)
\mathcal D_1<0.}
\tag{SC.28}
\]
SC.28 是原严格符号条件乘以正数 \(\mathcal D_1^2\) 后的形式，未假设 \(\mathcal D_1>0\)。

另一分支可直接保留 \(\mathcal I_2=0\)、SC.19，避免错误除以可能为零的一次系数；也可交换两个叶的标签后使用 SC.27–28。在交换坐标中
\[
\mathsf C'=\mathsf C,\quad\mathsf S'=-\mathsf S,\qquad
\omega'=\frac{-\mathsf S+\mathsf C\omega}{\mathsf C+\mathsf S\omega},
\]
所有活跃前提保证该坐标合法，故这种交换不丢失退化分支。

## SC.6 已闭合范围与准确剩余问题

在 SC.1–7 明示的实代表子域中，保持同一中心 \(U\) 后，
\[
\boxed{
F(\omega)=0,\quad
c_1c_2(\mathsf C+\mathsf S\omega)<0,\quad
\mathcal I_1(\omega)\mathcal I_2(\omega)=0}
\tag{SC.29}
\]
是“两个叶行完整混合首项为零、叶间边不活跃、两条中心非零混合向量严格反向”的精确约化。对于已给定且满足 SC.6 的几何，两叶的实极化比由 SC.7 固定，而中心同一个实方向由 SC.17 表示；SC.29 没有赋予两条边独立的中心种子。SC.27–28 是其中一个分支的纯几何版本，另一分支通过换标覆盖。

若这样的几何与方向能实现，SC.15 的其余发送因子均为正，可用一个正的叶幅度比例使中心两项大小相等。这是条件下的幅度相容性，不是本稿选取了数据。此时两叶各自只有一条活跃边，NC.16 的完整 \(C_{j0}\ne0\) 保证相应叶接收 \(W_{0,j}\ne0\)；叶间无第二项可与之相消。因此在这个条件性星形内，可以从完整叶行而非中心单边推得总 \(W_0\ne0\)。

尚未证明 SC.6、合同的独立整数频率要求、两分支中的 SC.27–28 或等价 SC.29 可以同时实现，也未证明其无解。当前准确剩余域就是这个显式几何系统；一般活跃三边的复极化系统亦保持 OPEN。SC.20–22 排除了若干几何，只是闭合障碍，不能把未排除的几何改称候选初值。

以上只处理短时首项的 \(M_0=0,W_0\ne0\) 相容性。即使该条件系统以后实现，也只可通过原已接受桥接说明所定义真实来源项的首项关系；不表示正时间所有混合项为零、返回原模板、可迭代再生成、无限尺度控制、有限总时间或 Navier–Stokes 奇性。当前没有实际三对数据或时间。

## 实际来源与字节绑定

当前独立工作实际使用并核对了下列本地来源；未读取本项根主稿、根审查或另一代理星形极化文本。

| 来源 | 实读范围与用途 | SHA-256 |
|---|---|---|
| net-mixed-cancellation/CONTRACT.md | 全文；同一三对、完整总和和首项边界 | 8ec55579d3288a15e47f2b1af17a2d981ac174fb649dc496fb6d5ac0d9b2e7e8 |
| net-mixed-cancellation/INDEPENDENT.md | 本人已全文推导、自核的最终稿；NC.1–19 的完整根及零判据，NC.5 节星形范围与幅度门 | 25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58 |
| mixed-polarization/MIXED_ROOT_INDEPENDENT.md | 本人此前全文推导、自核的接受来源；完整四叶根定义与来源边界，当前未重开前稿证明 | cad93f863ad371723d4510f20588a0f7abcee3e4f8e2984010f88ebcb2fc2dbf |

本稿 SC.6–29 的星形几何、\(b_j>2\)、中心行列式与不活跃消元是这次独立手工推导。本文自身 SHA-256 在最终写入与全文自核之后由工具生成并随交付提供，避免自指哈希。
