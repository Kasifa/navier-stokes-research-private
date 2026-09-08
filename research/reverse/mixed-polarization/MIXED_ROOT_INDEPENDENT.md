# 完整四叶接收的种子混合根：独立穷尽与短窗界

2026-09-08，PRIVATE_CORE。状态：**独立推导，待非作者全文审查；没有接受 NS 候选。**

本项完整实读新合同与 `JOINT_INDEPENDENT.md`，并沿用本代理已经完整实读且本项再次核对字节的 `COHERENCE_INDEPENDENT.md`、`SPATIAL_INDEPENDENT.md` 与 `ROOT_SPATIAL_REVIEW.md`。未读本轮根的 `MIXED_ROOT_PROOF.md` 或本轮其他推导。实际来源及 SHA256 在文末。

全部论证为手工符号推导。未用 Git、科学程序、计算数组、数值求值、频率或时间扫描、外部文献或额度重置；本项仅写入本独占稿。

结论为合同指定的有限四叶响应：\(1+3/3+1\) 根具有与 \(w_{22}\) 相同的三次时间阶，首项是否相消由完整空间系数决定。下文在合同准许的非退化频率平面符号极化中给出完整系数、严格正黏性核、明确几何短窗和树内误差界，证明这一类输入不能仅靠缩短时间将混合根变为相对 \(w_{22}\) 的小余项。

## MI.1 定义与双有序记号

固定合同中的无外力、单位黏性三维 \(2\pi\) 环面，以及同一组三个线性独立整数频率 \(p_i\)，其 \(P_i=|p_i|^2\) 两两不同。种子 \(U_i\perp p_i\) 为复向量，负模严格取共轭。没有给这些频率或种子指定实际值。

Fourier 双线性作用约定为
\[
B(X_r,Y_s)_{r+s}=-iP_{r+s}(X\cdot s)Y,
\qquad P_k=I-\frac{k\otimes k}{|k|^2}.
\tag{MI.1}
\]
其中点积为复双线性点积。为逐层保留两个有序项，记
\[
\mathfrak B(X,Y;r,s)
=-iP_{r+s}[(X\cdot s)Y+(Y\cdot r)X].
\tag{MI.2}
\]
这已包含两个有序作用，不再额外乘二。所有实际输出都经过其频率的 Leray 投影。

按合同定义
\[
v_0=e^{t\Delta}a,
\quad v_1=\int_0^t e^{(t-s)\Delta}B(v_0,v_0)(s)\,ds,
\]
\[
v_2=\int_0^t e^{(t-s)\Delta}
[B(v_0,v_1)+B(v_1,v_0)](s)\,ds,
\]
\[
v_3=\int_0^t e^{(t-s)\Delta}
[B(v_1,v_1)+B(v_0,v_2)+B(v_2,v_0)](s)\,ds.
\tag{MI.3}
\]
这里下标计非线性门数：\(v_2\) 为三叶项，\(v_3\) 为四叶项。以下均是这些给定有限积分的恒等式，不将它们自动认作真实 NS 解的已控 Taylor 展开。

## MI.2 三叶支撑及加倍接收根穷尽

第一层同轴配对逐项为零：对 \(\sigma p_i,\tau p_i\)，两种种子都横向于 \(p_i\)，故两个卷积点积均为零，包括相反频率的零模。由线性独立性，第一层潜在支撑恰为
\[
\mathcal L=\{\sigma p_i+\tau p_j:
i<j,\ \sigma,\tau=\pm1\},
\tag{MI.4}
\]
共十二个不同非零频率，实际系数允许为零。

\(v_2\) 由一个种子与一个 \(\mathcal L\) 模式相加。若种子重复该模式中的一个标签，同号得到 \(2\sigma p_i+\tau p_j\)，反号得到 \(\tau p_j\)；若三个标签不同，得到 \(\sigma p_1+\tau p_2+\upsilon p_3\)。因此三叶潜在支撑包含于以下互不相交的三类：
\[
\{\pm p_i\},\qquad
\{2\sigma p_i+\tau p_j:i\ne j,\ \sigma,\tau=\pm1\},
\]
\[
\{\sigma p_1+\tau p_2+\upsilon p_3:
\sigma,\tau,\upsilon=\pm1\}.
\tag{MI.5}
\]
三类分别有六、二十四、八个潜在频率。这里保留了回到种子的三叶场和目标外模式，没有从演化中删除它们。

固定正接收 \(2p_i\)。\(2+2\) 根由已接受的整系数辨认给出全部配对
\[
(p_i+p_j,p_i-p_j),\quad(p_i-p_j,p_i+p_j),
\qquad j\ne i.
\tag{MI.6}
\]
对 \(1+3/3+1\) 根，枚举唯一的种子频率 \(r\)：

1. 若 \(r=p_i\)，三叶频率必须为 \(p_i\)。该场一般不能从支撑省略，但根的两个有序点积都严格为零：若 \(Z=(v_2)_{p_i}\)，则 \(U_i\cdot p_i=Z\cdot p_i=0\)，故 \(\mathfrak B(U_i,Z;p_i,p_i)=0\)。
2. 若 \(r=-p_i\)，三叶频率必须为 \(3p_i\)。它不在 MI.5 内；直接追溯也只有三个 \(+p_i\) 叶，而其第一层 \(2p_i\) 自作用为零，因此 \((v_2)_{3p_i}=0\)。此外，即便仅形式上保留一个横向于 \(3p_i\) 的向量 \(Z\)，\((-p_i,3p_i)\) 的两个根点积仍因共线横向性分别为零。
3. 若 \(r=-\sigma p_j\)、\(j\ne i\)，三叶频率必须为 \(2p_i+\sigma p_j\)。其叶多重集由线性独立性唯一固定为 \((p_i,p_i,\sigma p_j)\)。三叶根只有种子 \(p_i\) 与第一层 \(p_i+\sigma p_j\) 的两个有序作用；另一个可能拆分 \((\sigma p_j,2p_i)\) 的第一层系数严格为零。

这穷尽了六个种子选择。MI.5 中三个不同标签的三叶模式不能与一个种子相加为 \(2p_i\)：其余两个标签无法同时消去。所有目标外三叶频率仍保留在 \(v_2\) 中，只是依据线性独立性不供给当前接收。

因此非零混合根只可能是
\[
(-\sigma p_j,2p_i+\sigma p_j),\quad
(2p_i+\sigma p_j,-\sigma p_j),
\qquad j\ne i,\ \sigma=\pm1.
\tag{MI.7}
\]
第一层、中间层及最终根的两个有序项都将在下面保留。负接收 \(-2p_i\) 由完整共轭给出，没有独立负模参数。

## MI.3 同一单对的三层完整空间映射

固定一条有序边，简写
\[
p=p_i,\quad q=p_j,\quad U=U_i,\quad V=U_j,
\]
\[
P=|p|^2,\quad Q=|q|^2,\quad c=p\cdot q,
\quad \Delta=PQ-c^2>0,\quad d=P-Q\ne0,\quad S=P+Q,
\]
\[
k_\sigma=p+\sigma q,\quad \lambda_\sigma=|k_\sigma|^2=S+2\sigma c,
\]
\[
\ell_\sigma=2p+\sigma q,\quad E_\sigma=|\ell_\sigma|^2=4P+Q+4\sigma c,
\quad \Lambda=\lambda_+\lambda_->0.
\tag{MI.8}
\]
非平行性保证所有 \(\lambda_\sigma,E_\sigma>0\)。本节允许 \(c=0\)，没有除以 \(c\)。非正交及 \(P>Q\) 只在后面的解析检验中加入。

沿用已接受的实横向分解
\[
e=q-\frac cPp,\qquad f=p-\frac cQq,\qquad n=p\times q,
\qquad U=u e+v n,\qquad V=x f+y n.
\tag{MI.9}
\]
定义
\[
V_+=V,\quad V_-=\overline V,
\qquad x_+=x,\quad x_-=\overline x,
\qquad y_+=y,\quad y_-=\overline y,
\]
\[
a=\Delta/P,\quad b=\Delta/Q,\quad\kappa=\Delta/(PQ),
\quad t_\sigma=n\times k_\sigma=Pe-\sigma Qf,
\quad r_\sigma=n\times\ell_\sigma=2Pe-\sigma Qf.
\]
这里 \(x_{-\sigma}=\overline{x_\sigma}\) 等共轭关系不可自由化。

第一层完整空间系数是
\[
N_\sigma=\mathfrak B(U,V_\sigma;p,\sigma q)
=-i(A_\sigma t_\sigma+B_\sigma n),
\tag{MI.10}
\]
\[
A_\sigma=\frac{\kappa d}{\lambda_\sigma}u x_\sigma,
\qquad B_\sigma=\sigma a u y_\sigma+b x_\sigma v.
\]
中间三叶空间系数定义为
\[
M_\sigma=\mathfrak B(U,N_\sigma;p,k_\sigma).
\tag{MI.11}
\]
手核 \(U\cdot k_\sigma=\sigma a u\)、\(t_\sigma\cdot p=-\sigma\Delta\)，故 \(N_\sigma\cdot p=i\sigma\Delta A_\sigma\)。由此
\[
M_\sigma=P_{\ell_\sigma}
[aQ u A_\sigma f+\sigma(\Delta A_\sigma v-a uB_\sigma)n].
\tag{MI.12}
\]
投影并未省略。因为
\[
|r_\sigma|^2=\Delta E_\sigma,\qquad
f\cdot r_\sigma=-\frac\Delta Q(2c+\sigma Q),
\]
\[
P_{\ell_\sigma}f=-\frac{2c+\sigma Q}{Q E_\sigma}r_\sigma,
\qquad P_{\ell_\sigma}n=n,
\]
得到完整三叶展开
\[
\boxed{M_\sigma=\alpha_\sigma r_\sigma+\beta_\sigma n,}
\tag{MI.13}
\]
\[
\alpha_\sigma=-\frac{a(2c+\sigma Q)}{E_\sigma}u A_\sigma,
\qquad
\beta_\sigma=\sigma(\Delta A_\sigma v-a uB_\sigma).
\tag{MI.14}
\]
为便于复核，展开后等价为
\[
\alpha_\sigma=-\frac{\Delta^2d(2c+\sigma Q)}{P^2Q\lambda_\sigma E_\sigma}
u^2x_\sigma,
\]
\[
\beta_\sigma=-\frac{\Delta^2}{P^2}u^2y_\sigma
-\frac{2\sigma\Delta^2(Q+\sigma c)}{PQ\lambda_\sigma}u x_\sigma v.
\tag{MI.15}
\]
\(M_\sigma\) 已包含前两层的 \(-i\) 因子；下面 MI.16 的最终根再按定义包含第三层的 \(-i\)。

最终混合根定义为
\[
D_\sigma=\mathfrak B(V_{-\sigma},M_\sigma;-\sigma q,\ell_\sigma).
\tag{MI.16}
\]
所需点积为
\[
V_{-\sigma}\cdot\ell_\sigma=2b x_{-\sigma},\qquad
M_\sigma\cdot(-\sigma q)=-2\sigma\Delta\alpha_\sigma.
\]
投影前的平面部分是
\[
2\alpha_\sigma x_{-\sigma}(b r_\sigma-\sigma\Delta f)
=4b\alpha_\sigma x_{-\sigma}t_\sigma.
\]
再用 \(P_{2p}f=-(c/Q)e\)、\(P_{2p}t_\sigma=(P+\sigma c)e\)，得
\[
\boxed{D_\sigma=D_{\sigma,e}e+D_{\sigma,n}n,}
\tag{MI.17}
\]
\[
D_{\sigma,e}=-4ib(P+\sigma c)\alpha_\sigma x_{-\sigma},
\]
\[
D_{\sigma,n}=-2i[b x_{-\sigma}\beta_\sigma
-\sigma\Delta\alpha_\sigma y_{-\sigma}].
\tag{MI.18}
\]
这是三层完整 Leray 映射，两个最终有序项分别导致 MI.18 中的两项。展开为原种子坐标后：
\[
\boxed{
D_{\sigma,e}=\frac{4i\Delta^3d(P+\sigma c)(2c+\sigma Q)}
{P^2Q^2\lambda_\sigma E_\sigma}u^2|x|^2,}
\tag{MI.19}
\]
\[
\boxed{
\begin{aligned}
D_{\sigma,n}={}&\frac{2i\Delta^3}{P^2Q}u^2
\left[x_{-\sigma}y_\sigma
-\frac{\sigma d(2c+\sigma Q)}{\lambda_\sigma E_\sigma}
x_\sigma y_{-\sigma}\right]\\
&+\frac{4i\sigma\Delta^3(Q+\sigma c)}{PQ^2\lambda_\sigma}
u v|x|^2.
\end{aligned}}
\tag{MI.20}
\]
这些式子同时保留 \(x\overline y\)、\(\overline x y\)、\(|x|^2\)，没有将确定性相干性换成强度平均。固定 \(U\) 时，每个 \(D_\sigma\) 均对 \(VV^*\) 具有线性延拓；对接收 \(U\) 则仍含 \(u^2,uv\)，满足
\[
D_\sigma(\zeta U,\eta V)=\zeta^2|\eta|^2D_\sigma(U,V).
\tag{MI.21}
\]
三对问题中，每条边上的这些坐标仍来自同一个 \(U_i\)，不能逐边单独指定。

## MI.4 精确正黏性核与回到种子的三叶场

第一层热因子是
\[
F_\sigma(t)=\int_0^t
e^{-\lambda_\sigma(t-r)-Sr}\,dr>0\qquad(t>0).
\tag{MI.22}
\]
为避免任何人工共振分母，以下直接使用精确指数积分。定义
\[
H_\sigma(t)=\int_0^t e^{-E_\sigma(t-s)}e^{-Ps}F_\sigma(s)\,ds,
\]
\[
K_\sigma(t)=\int_0^t e^{-4P(t-s)}e^{-Qs}H_\sigma(s)\,ds.
\tag{MI.23}
\]
于是
\[
(v_2)_{2p+\sigma q}(t)=H_\sigma(t)M_\sigma,
\qquad
\mathcal M_{p\leftarrow q}(t)=K_+(t)D_++K_-(t)D_-.
\tag{MI.24}
\]
第一条在三种线性独立原种子的合同下没有其他频率来源。全部 \(F_\sigma,H_\sigma,K_\sigma\) 在正时间严格为正，但 \(K_+\) 与 \(K_-\) 一般不同，不能在精确式中改为同一个权重。

时间顺序单纯形表达式为
\[
\boxed{
K_\sigma(t)=\int_{0\le r\le\tau\le s\le t}
e^{-\mathcal A_\sigma(t;s,\tau,r)}\,dr\,d\tau\,ds,}
\tag{MI.25}
\]
其中热作用量定义为
\[
\begin{aligned}
\mathcal A_\sigma(t;s,\tau,r)
={}&4P(t-s)+Qs+E_\sigma(s-\tau)+P\tau\\
&+\lambda_\sigma(\tau-r)+Sr.
\end{aligned}
\tag{MI.26}
\]
等价且明确非负的按时间区间写法为
\[
\mathcal A_\sigma
=4P(t-s)+(E_\sigma+Q)(s-\tau)
+(\lambda_\sigma+S)(\tau-r)+2Sr.
\tag{MI.27}
\]
也可完全收集指数为
\[
K_\sigma(t)=e^{-4Pt}\int_0^t
e^{(-2Q-4\sigma c)s}\int_0^s
e^{(2P+2\sigma c)\tau}\int_0^\tau
e^{2\sigma cr}\,dr\,d\tau\,ds.
\tag{MI.28}
\]
三式精确等价，未对指数作无界 Taylor 替换。

为具体保留 MI.2 中最终根被杀掉的种子返回场，对每个 \(j\ne i\)、\(\sigma=\pm1\) 定义
\[
R_{ij,\sigma}
=\mathfrak B(V_{-\sigma},N_\sigma;-\sigma q,k_\sigma),
\]
\[
L_{ij,\sigma}(t)=\int_0^t e^{-P(t-s)}e^{-Qs}F_\sigma(s)\,ds.
\tag{MI.29}
\]
则完整种子返回为
\[
\boxed{(v_2)_{p_i}(t)=\sum_{j\ne i}\sum_{\sigma=\pm1}
L_{ij,\sigma}(t)R_{ij,\sigma}.}
\tag{MI.30}
\]
这个场没有被假定为零。它由 \(P_{p_i}\) 保证横向，故 MI.2 的共线根逐项为零，无须也不能把该场从 \(v_2\) 支撑删除。MI.29 同样含两个有序项和完整压力投影。

## MI.5 完整 \(v_3\) 加倍接收式

为与已接受单对接口直接比较，写
\[
C_{p\leftarrow q}=\frac{4i\Delta^3d}{P^2Q^2\Lambda}u
\left[cdu|x|^2e+
\{Qu(SR-2icI)+2cP|x|^2v\}n\right],
\]
\[
R=\Re(x\overline y),\qquad I=\Im(x\overline y).
\tag{MI.31}
\]
该式包括 \(c=0\) 的精确连续接口。它是两个第一层模式 \(k_+,k_-\) 的完整有序根。

其精确热核为
\[
J(t)=\int_0^t e^{-4P(t-s)}F_+(s)F_-(s)\,ds>0.
\tag{MI.32}
\]
与已接受来源相同，若令 \(\psi_c(s)=\sinh(cs)/c\)、\(\psi_0(s)=s\)，则
\[
J(t)=e^{-4Pt}\int_0^t e^{2(P-Q)s}\psi_c(s)^2\,ds.
\tag{MI.33}
\]
按边恢复标签后，MI.2 的完整根穷尽给出
\[
\boxed{
(v_3)_{2p_i}(t)
=\sum_{j\ne i}\left[J_{ij}(t)C_{ij}
+K_{ij,+}(t)D_{ij,+}+K_{ij,-}(t)D_{ij,-}\right].}
\tag{MI.34}
\]
式中 \(C_{ij},D_{ij,\sigma}\) 均使用同一组实际符号种子的坐标；每个边有自己的热权重。负接收为右边的完整共轭。来自其他 \(j\) 的输出仍须在同一个 \(p_i^\perp\) 内相加，不能逐边取模替代真实向量和。

MI.34 的积分表达余项为零。它没有删除 \(v_3\) 的目标外输出，也没有将仅针对接收模式的恒等式称为全轨道再生成。

## MI.6 正积分给出的显式三次首项和四次误差界

定义严格正、只依赖几何的常数
\[
\mu_\sigma=\max\{4P,E_\sigma+Q,\lambda_\sigma+S,2S\}.
\tag{MI.35}
\]
由 MI.27，\(0\le\mathcal A_\sigma\le\mu_\sigma t\)。MI.25 单纯形的体积恰为 \(t^3/6\)，所以对每个符号 \(t>0\) 都有
\[
\boxed{
e^{-\mu_\sigma t}\frac{t^3}{6}
\le K_\sigma(t)\le\frac{t^3}{6},\qquad
\left|K_\sigma(t)-\frac{t^3}{6}\right|
\le\frac{\mu_\sigma t^4}{6}.}
\tag{MI.36}
\]
最后一项使用 \(0\le1-e^{-a}\le a\)，没有未估计的余项。

同样，将 MI.32 展开为 \(0\le r,r'\le s\le t\) 上的积分，其作用量为
\[
A_{22}=4P(t-s)+\lambda_+(s-r)+Sr
+\lambda_-(s-r')+Sr'.
\]
该表达非负，且
\[
A_{22}=4P(t-s)+2Ss-2cr+2cr'
\le4P(t-s)+(2S+2|c|)s\le\mu_{22}t,
\]
\[
\mu_{22}=\max\{4P,2S+2|c|\}>0.
\tag{MI.37}
\]
积分域体积是 \(\int_0^t s^2\,ds=t^3/3\)，故
\[
\boxed{
e^{-\mu_{22}t}\frac{t^3}{3}\le J(t)\le\frac{t^3}{3},\qquad
\left|J(t)-\frac{t^3}{3}\right|
\le\frac{\mu_{22}t^4}{3}.}
\tag{MI.38}
\]
特别地，当 \(0<t\le1/(2\mu_{22})\) 时，\(J(t)\ge t^3/6\)。

因此对任意同一单对极化，使用 Hermitian 欧氏范数，有树内明确界
\[
\left\|\mathcal M_{p\leftarrow q}(t)
-\frac{t^3}{6}(D_++D_-)\right\|
\le\frac{t^4}{6}
(\mu_+\|D_+\|+\mu_-\|D_-\|),
\tag{MI.39}
\]
\[
\left\|J(t)C-\frac{t^3}{3}C\right\|
\le\frac{\mu_{22}t^4}{3}\|C\|.
\tag{MI.40}
\]
若将 MI.34 的整行三次首项记为
\[
T_i=\frac13\sum_{j\ne i}C_{ij}
+\frac16\sum_{j\ne i}\sum_{\sigma=\pm1}D_{ij,\sigma},
\]
则完整接收的有限树界是
\[
\boxed{
\|(v_3)_{2p_i}(t)-t^3T_i\|
\le t^4\sum_{j\ne i}\left[
\frac{\mu_{22,ij}}3\|C_{ij}\|
+\frac16\sum_{\sigma=\pm1}\mu_{ij,\sigma}\|D_{ij,\sigma}\|
\right].}
\tag{MI.41}
\]
此式容许真实相消；它没有假设 \(T_i\)、单边 \(C\) 或 \(D_++D_-\) 非零。下面给出合同允许的严格非零检验。

## MI.7 非退化频率平面检验的精确系数

现在进一步保持符号条件
\[
P>Q>0,\quad \Delta>0,\quad c\ne0,
\qquad U=u e,\quad V=x f,\quad u x\ne0.
\tag{MI.42}
\]
这是合同准许的未取数值频率平面极化检验；\(u,x\) 为任意非零复符号，没有另选物理初值。接收和发送均非退化：\(U\cdot q=\Delta u/P\ne0\)、\(V\cdot p=\Delta x/Q\ne0\)。

令非零公共向量及实几何因子为
\[
\Phi=\frac{4i\Delta^3d}{P^2Q^2}u^2|x|^2e,
\qquad \gamma=\frac{cd}{\Lambda}\ne0,
\]
\[
\eta_\sigma=\frac{(P+\sigma c)(2c+\sigma Q)}
{\lambda_\sigma E_\sigma}.
\tag{MI.43}
\]
由于 \(v=y=0\)，MI.31、MI.19–20 精确化为
\[
\boxed{C=\gamma\Phi,\qquad D_\sigma=\eta_\sigma\Phi.}
\tag{MI.44}
\]
这里两个 \(D_\sigma\) 可以有不同符号，其中一个还可能严格为零；以下不将任何单项的正性作为假设。

设
\[
\Omega=E_+E_-=(4P+Q)^2-16c^2>0,
\]
\[
H=4P^2-PQ+Q^2-4c^2
=d(4P-Q)+4\Delta>0.
\tag{MI.45}
\]
\(H>0\) 使用本检验的 \(d=P-Q>0\)。对两个分母作完整通分得
\[
\begin{aligned}
\eta:=\eta_++\eta_-
={}&\frac{(P+c)(Q+2c)(S-2c)(4P+Q-4c)}{\Lambda\Omega}\\
&-\frac{(P-c)(Q-2c)(S+2c)(4P+Q+4c)}{\Lambda\Omega}\\
={}&\boxed{\frac{2c(2P+Q)H}{\Lambda\Omega}}\ne0.
\end{aligned}
\tag{MI.46}
\]
尤其 \(\eta\) 与 \(\gamma\) 同号，并且
\[
\boxed{R_*:=\frac{\eta}{2\gamma}
=\frac{(2P+Q)H}{d\Omega}>0.}
\tag{MI.47}
\]
这已经精确识别了两个混合根三次首项之和的非零性；尚未把不同正时间核 \(K_+,K_-\) 当成相同。正时间结论由下一节的明确余项保证。

## MI.8 明确几何短窗及相对下界

令
\[
\mu=\max\{\mu_+,\mu_-\},\qquad
B=|\eta_+|+|\eta_-|>0,
\]
\[
\boxed{t_*=\min\left\{\frac1{2\mu_{22}},
\frac{|\eta|}{2\mu B}\right\}>0.}
\tag{MI.48}
\]
这是由符号几何决定的明确短窗，并未选择实际时间。定义实标量
\[
m(t)=\eta_+K_+(t)+\eta_-K_-(t),
\quad
W(t)=J(t)C=\gamma J(t)\Phi,
\quad
\mathcal M(t)=m(t)\Phi.
\tag{MI.49}
\]
MI.36 给出精确误差
\[
\boxed{\left|m(t)-\frac{\eta t^3}{6}\right|
\le\frac{\mu B t^4}{6}.}
\tag{MI.50}
\]
故对所有 \(0<t\le t_*\)，\(m(t)\) 与 \(\eta\) 同号，而且
\[
\frac{|\eta|t^3}{12}\le |m(t)|\le\frac{|\eta|t^3}{4},
\qquad \frac{t^3}{6}\le J(t)\le\frac{t^3}{3}.
\tag{MI.51}
\]
两向量沿同一非零复向量 \(\Phi\)，且 \(W(t)\ne0\)。由 \(\eta/\gamma>0\)，存在正实数
\[
R(t)=\frac{m(t)}{\gamma J(t)}>0,
\qquad \mathcal M(t)=R(t)W(t),
\]
满足
\[
\boxed{\frac{R_*}{2}\le
\frac{\|\mathcal M(t)\|}{\|W(t)\|}=R(t)
\le3R_*\qquad(0<t\le t_*).}
\tag{MI.52}
\]
因此缩短时间不能把这一个非退化单对的混合根视为相对 \(w_{22}\) 的趋零小余项。该下界只依赖几何；非零符号极化幅度在比值中约去。

还可给出严格收敛率，避免以未估 \(O(t^4)\) 支持任何正时间结论。由 MI.38、MI.50 写
\[
J(t)=\frac{t^3}{3}(1+\delta(t)),
\quad |\delta(t)|\le\mu_{22}t,
\qquad
m(t)=\frac{t^3}{6}(\eta+\varepsilon(t)),
\quad |\varepsilon(t)|\le\mu Bt.
\]
对 \(0<t<1/\mu_{22}\)，有
\[
\boxed{|R(t)-R_*|
\le\frac{(\mu B+|\eta|\mu_{22})t}
{2|\gamma|(1-\mu_{22}t)}.}
\tag{MI.53}
\]
这证明 \(R(t)\to R_*>0\)，同时给出显式误差和可用窗口。

## MI.9 接受范围与未付部分

本稿给出的是三种线性独立原频率下 \(v_3\) 的全部加倍接收根。种子返回三叶场在 MI.30 中完整保留，其最终根严格为零；未列入 MI.7 的其他三叶模式依据频率独立性不供给当前接收，其场本身没有删除。MI.10–20 保留每一层的共轭、双有序项、Leray 投影和相关原种子。

MI.52–53 的否定范围仅为 MI.42 的符号非退化频率平面输入：它们不能凭“小时间”把这一对的 \(1+3/3+1\) 项降为相对 \(w_{22}\) 的趋零误差。一般极化可以有 \(D_++D_-=0\) 或 \(C=0\) 等分支，整行不同边还可能相消；本稿没有分类它们，没有将一个单对检验推广成一般三对混合极化无候选。

所有精确积分的余项为零；MI.36–41、MI.50–53 的截断误差仅属于指定有限树。没有认证无限维 NS 余项、解对参数的解析性、真实前代供给、有限两步再生成、统一迭代、同一固定初值的无限尺度、有限总时间、奇性或全局正则性。不同树同阶的障碍不等于完整两步机制失败或成功，也没有 Clay 结论。

## MI.10 实际来源绑定

路径相对于 `research/reverse/`。新合同与共同稿在本项全文读取；其余三份已在本代理连续推导上下文全文读取，本项核对字节未变，未将它们内部列出的其他文件冒记为实读。

| 文件 | SHA256 |
|---|---|
| mixed-polarization/MIXED_ROOT_CONTRACT.md | 4922918d272558efb8ddc9c05012acbffe9d497c2baf11a63b6027fc24e44bb1 |
| nonorthogonal-return/JOINT_INDEPENDENT.md | 30fe0231fad9def413e0d468d88cbe8a4c8b537d54e3df89b962cd996f0df215 |
| mixed-polarization/COHERENCE_INDEPENDENT.md | 886c5ff2822942b3ee5fd791ea2eb24477220c7a61213b9030b80861f834cb32 |
| nonorthogonal-return/SPATIAL_INDEPENDENT.md | d8413facd655e775e7e3582b45947be92a3c0f60387b966625475088ff3703f8 |
| nonorthogonal-return/ROOT_SPATIAL_REVIEW.md | 0e300c6b239dde79452e99d17cfb32558dcdf4a075c356e3c885e770a1d71355 |

没有新增外部定理适用性或新颖性声明。哈希固定实际文本，不替代本轮非作者数学审查。
