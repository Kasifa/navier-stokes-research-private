# 混合极化的相干协方差：独立完整单对推导

2026-09-08，PRIVATE_CORE。状态：**独立稿，待本轮非作者全文审查；没有接受 NS 候选。**

本稿从本轮合同和已接受的单对空间公式自行推导。完整实读来源仅为文末列出的三份文件；未读本轮 `COHERENCE_PROOF.md` 或本轮任何审稿，未使用旧代理的口头结论。全部为手工符号推导；未用 Git、科学程序、计算数组、数值求值、参数扫描或外部来源，未选择实际整数波向量、时间或三对初值。

结论限于合同定义的完整单对四次树：固定接收种子时，输出具有对发送 Hermitian 协方差的线性延拓；两种螺旋强度不能重建确定性混合极化的输出。下文给出两个发送状态和同一个接收状态均非退化的严格对照。

## CI.1 几何、点积和有序项

令未指定实际值的频率符号 \(p,q\) 满足
\[
P=|p|^2>0,\quad Q=|q|^2>0,\quad c=p\cdot q\ne0,
\quad \Delta=PQ-c^2>0,\quad d=P-Q\ne0.
\tag{CI.1}
\]
另记
\[
S=P+Q,\quad k_\pm=p\pm q,\quad
\lambda_\pm=S\pm2c=|k_\pm|^2>0,
\quad \Lambda=\lambda_+\lambda_-=S^2-4c^2>0.
\]
因此频率非平行、非正交且原频率长度不同。定义实向量
\[
e=q-\frac cPp,\qquad f=p-\frac cQq,\qquad n=p\times q.
\]
它们满足
\[
e\perp p,\quad f\perp q,\quad n\perp p,q,
\quad |e|^2=\frac\Delta P,\quad |f|^2=\frac\Delta Q,
\quad |n|^2=\Delta,
\quad e\cdot f=-\frac{c\Delta}{PQ}.
\tag{CI.2}
\]
写任意横向种子为
\[
U=u e+v n,\qquad V=x f+y n,
\qquad u,v,x,y\in\mathbb C.
\tag{CI.3}
\]
Fourier 卷积中的点积是复双线性点积，不能替换为 Hermitian 内积。Hermitian 内积只用于下文的螺旋正交、范数和协方差。实值条件将 \(-q\) 的种子固定为 \(\overline V\)，并未给它一个独立极化。

按已接受来源的单位黏性归一化，Fourier–Leray 非线性为
\[
\mathcal N(\widehat u,\widehat u)(k)
=-iP_k\sum_{a+b=k}(\widehat u(a)\cdot b)\widehat u(b),
\qquad P_k=I-\frac{k\otimes k}{|k|^2}.
\tag{CI.4}
\]
两条第一层边完整保留两个有序项：
\[
N_+=-iP_{k_+}[(U\cdot q)V+(V\cdot p)U],
\]
\[
N_-=-iP_{k_-}[-(U\cdot q)\overline V
 +(\overline V\cdot p)U].
\tag{CI.5}
\]
定义
\[
a=\Delta/P,\quad b=\Delta/Q,\quad \kappa=\Delta/(PQ),
\quad t_+=n\times k_+=Pe-Qf,\quad t_-=n\times k_-=Pe+Qf.
\]
利用
\[
|t_\pm|^2=\Delta\lambda_\pm,\quad t_+\cdot t_-=\Delta d,
\quad P_{k_+}t_-=\frac d{\lambda_+}t_+,
\quad P_{k_-}t_+=\frac d{\lambda_-}t_-,
\]
第一层压力投影给出
\[
A_+=\frac{\kappa d}{\lambda_+}ux,\quad
A_-=\frac{\kappa d}{\lambda_-}u\overline x,
\]
\[
B_+=a u y+b x v,\qquad
B_-=-a u\overline y+b\overline x v,
\]
\[
N_+=-i(A_+t_++B_+n),\qquad
N_-=-i(A_-t_-+B_-n).
\tag{CI.6}
\]
这里所有第一层系数仍由同一个 \(U,V,\overline V\) 决定。

第二层完整有序和为
\[
C_{p\leftarrow q}(U,V)
=-iP_{2p}[(N_+\cdot k_-)N_-+(N_-\cdot k_+)N_+].
\tag{CI.7}
\]
由 \(t_+\cdot k_-=-2\Delta\)、\(t_-\cdot k_+=2\Delta\)，两个点积分别为 \(2i\Delta A_+\) 和 \(-2i\Delta A_-\)。括号内因此恰为
\[
2\Delta[A_+A_-(t_--t_+)+(A_+B_--A_-B_+)n].
\]
再用 \(t_--t_+=2Qf\)、\(P_{2p}f=-(c/Q)e\) 和 \(P_{2p}n=n\)，得
\[
C_{p\leftarrow q}
=4ic\Delta A_+A_-e-2i\Delta(A_+B_--A_-B_+)n.
\tag{CI.8}
\]
两层 Leray 与两个第二层有序项均已实施；没有额外乘一个有序因子二。

为把全部相干性显式保留，令
\[
R=\Re(x\overline y),\qquad I=\Im(x\overline y).
\]
直接合并两个分母有
\[
\frac{x\overline y}{\lambda_+}
 +\frac{\overline x y}{\lambda_-}
=\frac{2SR-4icI}{\Lambda},
\qquad
\frac1{\lambda_+}-\frac1{\lambda_-}=-\frac{4c}{\Lambda}.
\]
代入 CI.8，得到与已接受空间公式一致的完整单对表达式
\[
\boxed{
C_{p\leftarrow q}(U,V)
=\frac{4i\Delta^3d}{P^2Q^2\Lambda}u
\left[cdu|x|^2e+
\{Qu(SR-2icI)+2cP|x|^2v\}n\right].}
\tag{CI.9}
\]
这里 \(u^2\) 来自两个正 \(p\) 输入，不能写成 \(|u|^2\)。发送方向则出现一个 \(V\) 和一个 \(\overline V\)。

## CI.2 在同一个发送横截面中固定螺旋基

令
\[
F=\sqrt{\frac Q\Delta}\,f,\qquad N=\frac n{\sqrt\Delta}.
\]
则 \(F,N\) 为 \(q^\perp\) 内实正交单位向量。取向满足
\[
\frac q{\sqrt Q}\times F=-N,\qquad
\frac q{\sqrt Q}\times N=F.
\]
在本稿固定这一相位规范，定义
\[
\boxed{h_+=\frac{F-iN}{\sqrt2},\qquad
h_-=\frac{F+iN}{\sqrt2}.}
\tag{CI.10}
\]
手核得
\[
i q\times h_\sigma=\sigma\sqrt Q\,h_\sigma,
\qquad h_\sigma^*h_\tau=\delta_{\sigma\tau},
\qquad \sigma,\tau\in\{+1,-1\}.
\tag{CI.11}
\]
因此这确为一对 Hermitian 正交单位螺旋基。

任意发送极化写为
\[
V=z_+h_++z_-h_-,
\qquad
x=\frac{\sqrt Q}{\sqrt{2\Delta}}(z_++z_-),
\qquad
y=\frac{-i}{\sqrt{2\Delta}}(z_+-z_-).
\tag{CI.12}
\]
用同一个相干乘积 \(\omega=z_+\overline{z_-}\) 定义四个实量
\[
T=|z_+|^2+|z_-|^2,\qquad
D=|z_+|^2-|z_-|^2,\qquad
X=2\Re\omega,\qquad Y=2\Im\omega.
\tag{CI.13}
\]
从 CI.12 直接展开：
\[
|x|^2=\frac Q{2\Delta}(T+X),\qquad
|y|^2=\frac1{2\Delta}(T-X),
\]
\[
x\overline y
=\frac{i\sqrt Q}{2\Delta}
 (|z_+|^2-|z_-|^2-\omega+\overline\omega)
=\frac{\sqrt Q}{2\Delta}(Y+iD).
\tag{CI.14}
\]
故 \(R=\sqrt QY/(2\Delta)\)、\(I=\sqrt QD/(2\Delta)\)。尤其不能在固定两种强度之后擅自将 \(R\) 设为零，或将 \(|x|^2\) 固定为 \(QT/(2\Delta)\)。

定义非零几何常数
\[
K=\frac{2i\Delta^2d}{P^2Q\Lambda}.
\]
把 CI.14 代入完整 CI.9，恰得
\[
\boxed{
C_{p\leftarrow q}(U,V)
=K u\left[
cdu(T+X)e+
\{\sqrt Q\,u(SY-2icD)+2cP v(T+X)\}n
\right].}
\tag{CI.15}
\]
相干实部 \(X\) 进入平面通道以及含 \(v\) 的法向部分，相干虚部 \(Y\) 进入含 \(u^2\) 的法向部分。此式是完整有序四次系数的恒等式，未做相位平均。

## CI.3 “对秩一协方差线性”的准确意义

令 \(\rho=VV^*\) 为 \(q^\perp\) 上的 Hermitian 非负秩一算子；零种子时秩为零。其螺旋坐标为
\[
H_{\sigma\tau}=h_\sigma^*\rho h_\tau
=z_\sigma\overline{z_\tau}.
\tag{CI.16}
\]
于是
\[
T=H_{++}+H_{--},\qquad D=H_{++}-H_{--},
\]
\[
X=H_{+-}+H_{-+},\qquad
Y=\frac{H_{+-}-H_{-+}}i.
\tag{CI.17}
\]
这些都是算子条目的线性函数。固定 \(U\) 后，以 CI.17 代入 CI.15，定义 \(\mathcal L_U(\rho)\)。在 Hermitian 算子的实向量空间上，\(\mathcal L_U\) 是实线性映射，而且
\[
\boxed{C_{p\leftarrow q}(U,V)=\mathcal L_U(VV^*).}
\tag{CI.18}
\]
若允许一般复横向算子，以同样条目公式定义即可得到复线性延拓。所谓“线性”指这一个延拓；秩一非负算子集合本身不是向量空间，不能将它的非封闭性略去。

作为不依赖螺旋记号的核对，因 \(f,n\) 为固定实向量，
\[
|x|^2=\frac{Q^2}{\Delta^2}f^*\rho f,\qquad
x\overline y=\frac Q{\Delta^2}f^*\rho n.
\tag{CI.19}
\]
连同其共轭条目，CI.9 也直接给出同一线性性。输出并不需要 \(|y|^2\) 的独立项；这与已接受的纯法向发送零分支一致，并不允许删去 \(x\overline y\)。

对于接收种子，CI.15 只含 \(u^2\) 和 \(uv\)，所以是 \(U\) 的复齐次二次式；它一般不是 \(UU^*\) 的函数。完整相位齐次律为
\[
C_{p\leftarrow q}(\alpha U,\beta V)
=\alpha^2|\beta|^2 C_{p\leftarrow q}(U,V),
\qquad \alpha,\beta\in\mathbb C.
\tag{CI.20}
\]

确定性秩一条件保留
\[
X^2+Y^2=4|z_+|^2|z_-|^2,\qquad
D^2+X^2+Y^2=T^2,\qquad
\|V\|^2=\operatorname{tr}\rho=T.
\tag{CI.21}
\]
两种强度固定了相干乘积的模，未固定其相位。

## CI.4 非相干强度替换会改变完整输出

仅保留两种强度等价于另造算子
\[
\rho_{\rm diag}=|z_+|^2h_+h_+^*
 +|z_-|^2h_-h_-^*.
\]
若两种强度均非零，此算子为秩二，并非实际确定性极化的 \(VV^*\)。其线性输出等于
\[
\mathcal L_U(\rho_{\rm diag})
=|z_+|^2 C_{p\leftarrow q}(U,h_+)
 +|z_-|^2 C_{p\leftarrow q}(U,h_-).
\tag{CI.22}
\]
它确实是非相干强度合成，但与原输入的差精确为
\[
\boxed{
\mathcal L_U(VV^*)-\mathcal L_U(\rho_{\rm diag})
=Ku\left[cduX e+
\{\sqrt Q\,uSY+2cPvX\}n\right].}
\tag{CI.23}
\]
保持 CI.1，并取合法非退化接收种子 \(u\ne0\)，允许任意 \(v\)。若 CI.23 为零，先由独立的平面分量及 \(Kcdu^2\ne0\) 得 \(X=0\)，继而由法向分量及 \(K\sqrt Q\,S u^2\ne0\) 得 \(Y=0\)。反向显然成立。因此
\[
\mathcal L_U(VV^*)=\mathcal L_U(\rho_{\rm diag})
\iff X=Y=0.
\tag{CI.24}
\]
对于确定性真混合 \(z_+z_-\ne0\)，CI.21 排除了 \(X=Y=0\)。在本稿全部非退化几何和接收条件下，任何真混合都不能这样替换为两种纯螺旋输出的非相干强度合成。

更一般地，固定同一对强度时，两个输出相等蕴含 \(\Delta X=\Delta Y=0\)：先看平面差，再看法向差。因此在这组条件下，完整输出能区别固定强度上的不同相干相位。此论断没有把 \(\mathcal L_U\) 宣称为对所有 Hermitian 算子的单射。

## CI.5 两个发送状态均非退化的严格符号对照

令 \(r,s\) 为任意未取数值的严格正实符号，保持同一个
\[
U=u e+v n,\qquad u\ne0,
\]
以及同一个 CI.1 几何与 CI.10 螺旋规范。构造两个代数对照状态
\[
\boxed{V^{(+)}=r h_++i s h_-,\qquad
V^{(-)}=r h_+-i s h_-.}
\tag{CI.25}
\]
两态的两种螺旋强度均为 \((r^2,s^2)\)，范数平方均为 \(T=r^2+s^2\)。同时
\[
D=r^2-s^2,\qquad X^{(+)}=X^{(-)}=0,
\qquad Y^{(+)}=-2rs,\quad Y^{(-)}=2rs.
\tag{CI.26}
\]
它们各自的协方差均为实际秩一 \(V^{(\pm)}V^{(\pm)*}\)，非对角条目分别为 \(\mp i rs\)，并未换成混合算子。

发送平面坐标为
\[
x^{(\pm)}=\frac{\sqrt Q}{\sqrt{2\Delta}}(r\pm i s),
\qquad |x^{(\pm)}|^2=\frac Q{2\Delta}(r^2+s^2)>0.
\tag{CI.27}
\]
因此 \(U\cdot q=\Delta u/P\ne0\)、\(V^{(\pm)}\cdot p=\Delta x^{(\pm)}/Q\ne0\)。结合 \(d\ne0\)，两个发送状态的两条第一层平面系数均非零；两个完整四次输出也各有非零平面分量。对照未借用一个纯法向发送零分支。

由 CI.15，两态的完整平面输出相同，完整法向输出的差为
\[
\boxed{
C_{p\leftarrow q}(U,V^{(+)})
-C_{p\leftarrow q}(U,V^{(-)})
=-4K\sqrt Q\,Srsu^2 n
=-\frac{8i\Delta^2dSrs}{P^2\sqrt Q\,\Lambda}u^2 n
\ne0.}
\tag{CI.28}
\]
非零性只使用 \(\Delta>0\)、\(d\ne0\)、\(P,Q,S,\Lambda>0\)、\(r,s>0\)、\(u\ne0\) 和 \(n\ne0\)。\(v\) 任意且在差式中消去。两种螺旋的非负强度加上范数，因而仍不足以重建完整单对 \(C\)。

CI.28 的差恰为纯法向向量，并不违反已接受的“任何非零本对输出都有非零平面分量”：两个被比较的输出各有同一非零平面分量；其差对应协方差之差，不能自动视为另一秩一发送种子的输出。

## CI.6 热因子、条件与未付范围

本对正时间贡献按已接受来源是共同实权重
\[
J(t)=e^{-4Pt}\int_0^t e^{2(P-Q)\tau}
\frac{\sinh^2(c\tau)}{c^2}\,d\tau
\tag{CI.29}
\]
乘以 \(C\)。对任意符号 \(t>0\)，由于 \(c\ne0\)，积分内函数在 \(\tau>0\) 严格为正，所以 \(J(t)>0\)。它只依赖同一几何和时间，不依赖选择 \(V^{(+)}\) 或 \(V^{(-)}\)。故 CI.28 乘以同一 \(J(t)\) 后仍严格非零。\(t=0\) 则 \(J=0\)，本稿不在那里声称输出有别；没有选择任何实际时间。

本稿的非退化命题要求 CI.1 和 \(u\ne0\)。若 \(u=0\) 或 \(d=0\)，已接受公式使所有发送极化的本对输出为零，不能在那里声称能辨认相干性。若 \(c=0\)，本稿用于从平面通道识别 \(X\) 的论证不适用；若 \(\Delta=0\)，当前横向基失效。单螺旋边界 \(r=0\) 或 \(s=0\) 不满足本对照的真混合条件，CI.28 的差在那里为零。这些分支没有被隐藏。

CI.5 的两态是两个确定性输入的符号代数对照，**不是同一 NS 原解的两代**，也不是已选定的实际三对种子或奇性候选。本稿不构造实际初值，不证明一般共同返回可解，也不把不同边的相干量提升为可以独立指定的变量。

余项为零只表示由公式（CI.5）至（CI.7）定义的这一个有限 \(2+2\) 树空间公式及其共同热权重是精确恒等式。三对共同接收、全部配对及其不同热权重、同一组三对种子的相容性、原解的 \(1+3/3+1\)、其他混合与回流、真实第一代供给、无限维误差与统一迭代均未支付。没有有限 NS 两步机制、固定初值无限尺度、有限总时间、奇性、全局正则性或 Clay 结论。

## CI.7 实际完整来源与独立性绑定

本轮实际全文读取的数学来源如下。路径相对于 `research/reverse/`：

| 文件 | SHA256 |
|---|---|
| mixed-polarization/COHERENCE_CONTRACT.md | ef0172d56243edea9f4014acb57c05c877ab4bd6fe147ab42fe6237073441643 |
| nonorthogonal-return/SPATIAL_INDEPENDENT.md | d8413facd655e775e7e3582b45947be92a3c0f60387b966625475088ff3703f8 |
| nonorthogonal-return/ROOT_SPATIAL_REVIEW.md | 0e300c6b239dde79452e99d17cfb32558dcdf4a075c356e3c885e770a1d71355 |

本稿未追读这些文件内部列举的其他稿件；“来源文件列有某稿哈希”不等于本人已读该稿。没有外部定理依赖或新颖性声明。本轮仅写入本独占文件；哈希只绑定实际文本，不能代替独立数学审查。
