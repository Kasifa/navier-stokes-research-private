# 共享非正交前代的四次空间映射：独立展开

2026-09-08，PRIVATE_CORE。状态：**精确相关映射及完整零分支，待非作者审查；未接受候选。**

本轮完整读取 `SPATIAL_CONTRACT.md` 与本人已写的 `INDEPENDENT_PREFLIGHT.md`，没有读取本轮空间主稿或其他空间推导。以下保留同一对原种子及共轭，自行展开两层完整有序 Fourier–Leray 系数。无科学程序、数组、数值参数选择、Git 或外部定理调用。

## SI.1 非单位横向分解

沿用非平行实整数频率 \(p,q\)，满足 \(c=p\cdot q\ne0\)。记
\[
P=|p|^2,\quad Q=|q|^2,\quad S=P+Q,
\quad \Delta=PQ-c^2>0,\quad d=P-Q,
\]
\[
k_\pm=p\pm q,\qquad \lambda_\pm=S\pm2c>0,
\qquad \Lambda=\lambda_+\lambda_-=S^2-4c^2>0.
\]
在同一个欧氏空间中定义
\[
e=q-\frac cPp,\qquad f=p-\frac cQq,\qquad n=p\times q.
\tag{SI.1}
\]
有
\[
|e|^2=\frac\Delta P,\quad |f|^2=\frac\Delta Q,
\quad |n|^2=\Delta,
\quad e\perp n,\quad f\perp n,
\quad e\cdot f=-\frac{c\Delta}{PQ}.
\]
因此任意 \(U\perp p,V\perp q\) 唯一表示为
\[
U=u e+v n,\qquad V=x f+y n,
\qquad u,v,x,y\in\mathbb C.
\tag{SI.2}
\]
这里四个符号是原种子的坐标；不是两个前代的自由坐标。实基不随相位变化，所以
\(\overline V=\overline x f+\overline y n\)，
\(\overline U=\overline u e+\overline v n\)。特别地
\[
U\cdot q=\frac\Delta P u,\qquad
V\cdot p=\frac\Delta Q x.
\tag{SI.3}
\]
这仅为固定欧氏向量的分解，没有改变物理坐标、Laplacian、黏性或周期域。

## SI.2 完整第一层投影

从已核有序式开始：
\[
N_+=-iP_{k_+}[(U\cdot q)V+(V\cdot p)U],
\]
\[
N_-=-iP_{k_-}[-(U\cdot q)\overline V+(\overline V\cdot p)U].
\tag{SI.4}
\]
置
\[
a=\Delta/P,\quad b=\Delta/Q,\quad \kappa=\Delta/(PQ),
\]
\[
t_+=n\times k_+=Pe-Qf,
\qquad t_-=n\times k_-=Pe+Qf.
\tag{SI.5}
\]
频率平面内的第一层原始有序和分别为
\[
ux(af+be)=\kappa ux\,t_-,
\qquad
u\overline x(-af+be)=\kappa u\overline x\,t_+.
\]
同时法向系数分别为
\(a u y+b x v\) 与 \(-a u\overline y+b\overline x v\)。因
\[
|t_\pm|^2=\Delta\lambda_\pm,
\qquad t_+\cdot t_-=\Delta d,
\]
完整第一层 Leray 给
\[
P_{k_+}t_-=\frac d{\lambda_+}t_+,
\qquad P_{k_-}t_+=\frac d{\lambda_-}t_-.
\tag{SI.6}
\]
法向 n 已垂直于两个频率，不被投影改变。定义
\[
A_+=\frac{\kappa d}{\lambda_+}ux,
\quad A_-=\frac{\kappa d}{\lambda_-}u\overline x,
\]
\[
B_+=a u y+b x v,
\qquad B_-=-a u\overline y+b\overline x v.
\]
于是全部前代为
\[
\boxed{N_+=-i(A_+t_++B_+n),\qquad
N_-=-i(A_-t_-+B_-n).}
\tag{SI.7}
\]
同一个 \(u,v,x,y\) 同时决定四个 \(A_\pm,B_\pm\)；其中的共轭不可移到 u 或 v 上。

## SI.3 两个第二层有序项与投影

由定向 \(n=p\times q\) 可得
\[
t_+\cdot k_-=-2\Delta,
\qquad t_-\cdot k_+=2\Delta.
\]
故
\[
N_+\cdot k_-=2i\Delta A_+,
\qquad N_-\cdot k_+=-2i\Delta A_-.
\tag{SI.8}
\]
用原种子点积写，同样为
\[
N_+\cdot k_-=\frac{2id}{\lambda_+}(U\cdot q)(V\cdot p),
\]
\[
N_-\cdot k_+=-\frac{2id}{\lambda_-}(U\cdot q)\overline{(V\cdot p)}.
\tag{SI.9}
\]
这一步已经体现共享输入的限制：即使 \(c\ne0\)，若 \(P=Q\)，两个交叉点积仍恒为零。

合同所求完整四次空间系数为
\[
C_{p\leftarrow q}=-iP_{2p}
[(N_+\cdot k_-)N_-+(N_-\cdot k_+)N_+].
\tag{SI.10}
\]
将两个有序项各代入一次，括号合并为
\[
2\Delta[A_+A_-(t_--t_+)
+(A_+B_--A_-B_+)n].
\]
而
\[
t_--t_+=2Qf,\qquad
P_{2p}f=-\frac cQe,\qquad P_{2p}n=n.
\]
所以
\[
\boxed{C_{p\leftarrow q}
=4ic\Delta A_+A_- e
-2i\Delta(A_+B_--A_-B_+)n.}
\tag{SI.11}
\]
这里第二层压力投影已经完整实施，没有沿接收方向留下未投影项，也没有额外添加一个有序系数2。

## SI.4 平面与法向相关系数

记同一 q 种子的实相关量
\[
R=\Re(x\overline y),\qquad I=\Im(x\overline y).
\]
由
\[
A_+A_-=\frac{\kappa^2d^2}{\Lambda}u^2|x|^2,
\]
以及
\[
\frac{x\overline y}{\lambda_+}
+\frac{\overline x y}{\lambda_-}
=\frac{2SR-4icI}{\Lambda},
\qquad
\frac1{\lambda_+}-\frac1{\lambda_-}=-\frac{4c}{\Lambda},
\]
得到完整分解
\[
C_{p\leftarrow q}=C_e e+C_n n,
\tag{SI.12}
\]
\[
\boxed{C_e=\frac{4ic\Delta^3d^2}{P^2Q^2\Lambda}
u^2|x|^2,}
\tag{SI.13}
\]
\[
\boxed{C_n=\frac{4i\Delta^3d}{P^2Q^2\Lambda}
u\,[Q u(SR-2icI)+2cP|x|^2v].}
\tag{SI.14}
\]
等价的合并式为
\[
\boxed{C_{p\leftarrow q}
=\frac{4i\Delta^3d}{P^2Q^2\Lambda}u
\left[cdu|x|^2e+
\{Qu(SR-2icI)+2cP|x|^2v\}n\right].}
\tag{SI.15}
\]
两条通道不能各自独立调相。尤其应保留 \(u^2\)，不能误写成 \(|u|^2\)；到 \(2p\) 的两次 p 输入均为正频率，而 q 输入分别为正负频率。整体满足符号齐次律
\[
C_{p\leftarrow q}(zU,wV)
=z^2|w|^2 C_{p\leftarrow q}(U,V)
\qquad(z,w\in\mathbb C),
\]
负接收模则取完整复共轭。这些是对相位和实值反馈的代数核对，不是选取新的幅度。

作为平面项的独立对照，前稿 NP.14 给
\[
C_{p\leftarrow q}\cdot q
=\frac{ic}{P}(N_+\cdot k_-)(N_-\cdot k_+)
=\frac{4icd^2}{P\Lambda}(U\cdot q)^2|V\cdot p|^2.
\]
由于 \(e\cdot q=\Delta/P\)，这等价于
\[
C_e=\frac{4icd^2}{\Delta\Lambda}
(U\cdot q)^2|V\cdot p|^2,
\tag{SI.16}
\]
与 SI.13 完全一致。

## SI.5 全部零分支

以下均保持合同的 \(c\ne0\)、\(\Delta>0\)。因 e 与 n 是 \(p^\perp\) 内非零且相互正交的实向量，SI.12 的两分量不会彼此相消。

由 SI.13，平面分量为零当且仅当
\[
d=0\quad\text{或}\quad u=0\quad\text{或}\quad x=0.
\tag{SI.17}
\]
每个分支又使 SI.14 为零：前两个杀掉其整体因子；第三个给 \(R=I=|x|^2=0\)。反之，若三个条件均不成立，SI.13 必非零。因此
\[
\boxed{C_{p\leftarrow q}=0
\iff P=Q\ \text{或}\ U\cdot q=0\ \text{或}\ V\cdot p=0.}
\tag{SI.18}
\]
其中 \(U\cdot q=0\) 配合 \(U\cdot p=0\) 正是 \(U\in\operatorname{span}_{\mathbb C}n\)，V 的分支同理；允许零种子时它们也已包含在这些条件内。

所以非退化分支的每个非零输出都具有非零频率平面分量；**不存在非零而纯法向的本对四次输出**。这不是说法向分量恒为零：它由 SI.14 的相关表达式决定。

为给法向分量的准确零条件，限制到 \(d u x\ne0\)。此时
\[
C_n=0\iff
Qu(SR-2icI)+2cP|x|^2v=0.
\tag{SI.19}
\]
若记 \(\zeta=y/x\)，则 \(R=|x|^2\Re\zeta\)、\(I=-|x|^2\Im\zeta\)，故等价为
\[
\boxed{\frac vu
=-\frac{QS}{2cP}\Re\zeta
-i\frac QP\Im\zeta.}
\tag{SI.20}
\]
同一非退化范围内，两个输出系数的相关比值精确为
\[
\frac{C_n}{C_e}
=\frac{2P}{d}\frac vu
+\frac{Q}{cd}[S\Re\zeta+2ic\Im\zeta].
\tag{SI.21}
\]
这是原种子相对极化的公式，不是自由选择前代的像论证。其 v 项系数非零，说明共享种子并不恒等强制法向通道为零；本稿不据此选择极化或声称其他接收通道能同时满足模板条件。

第一层本身是否为零也可准确保留。由 \(t_\pm,n\) 线性独立，
\[
N_+=0\iff d u x=0\ \text{且}\ Qu y+Px v=0,
\]
\[
N_-=0\iff d u\overline x=0\ \text{且}\ -Qu\overline y+P\overline x v=0.
\tag{SI.22}
\]
在 \(d u x\ne0\) 时两个前代均非零；在 SI.18 的退化分支里，前代可以是非零法向场，但其到 \(2p\) 的完整二次自作用仍为零。因此不能把第一层激活与第四次接收等同。

## SI.6 与旧门及热权重的边界

旧等长第二门的前提是 \(|p+q|=|p-q|\)，等价于 \(c=0\)。当前保持 \(c\ne0\)，但展开显示另一项共享种子限制：若**原频率**等长 \(P=Q\)，第一层的两个平面系数 \(A_\pm\) 恒为零，第二层的完整空间系数也恒为零。两个等长条件不同，不能互相替换。

若形式上取正交接口 \(c=0\)，SI.13 变为零，SI.14 变为
\[
C_n=\frac{4iP Q^2(P-Q)}{P+Q}u^2\Re(x\overline y),
\]
与正交情形仅有法向接收的结构一致；此句仅检验公式接口。SI.18 的必要充分零判据明确限于 \(c\ne0\)，不能直接延伸到正交极限。

本对正时间的树贡献是已接受的严格正实权重
\[
J(t)=e^{-4Pt}\int_0^t e^{2(P-Q)s}\frac{\sinh^2(cs)}{c^2}\,ds
\]
乘以 SI.15；因此对 \(t>0\)，本对的空间零分支不被热权重改变。所有公式的解析余项为零，但它们仍只属于单对、单个 2+2 树。

本稿没有支付三对线性独立频率的全部接收及共同模板条件，没有把本对的可变法向系数升级为新的独立前代自由度。完整原解的 1+3/3+1、种子混合、其他接收、实值回流的全系统作用以及无限维误差仍未付。没有接受候选，也不提供真正两步供给、NS 奇性、单初值无限尺度或统一迭代结论。

## SI.7 实读来源及独立性

| 本轮完整实读文件 | SHA256 |
|---|---|
| SPATIAL_CONTRACT.md | ba31859d9b2e2654c8cf8e00bf64da3b54070c93e9fa036594a96e3d3f70fb1d |
| INDEPENDENT_PREFLIGHT.md | 679ce998bd78f2203232e6404df376eb94a2a19419c6ae3fdb82b25dbf823f65 |

未读本轮主空间推导；未新增外部定理依赖或新颖性声明。实际字节绑定不能代替数学审查，本稿待非作者全文核验。
