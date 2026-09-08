# 高行独立投影稿及共享权重的非作者审查

2026-09-08，PRIVATE_CORE。结论：**HIGHER_ROW_INDEPENDENT.md 的 HI.1–21 通过手工核验。完整实二次投影门、另边平面系数为零与等长支、未消去的另一完整分量，以及原三边两高行的共享权重恒等式均正确。通过范围仍是投影条件及共享数据的必要关系，没有完整高行或联合实例的可解性结论。**

本审查者不是被审独立稿作者，但已审过根的 `HIGHER_ROW_PROJECTION.md` 和随后面积稿，也熟悉已接纳最低接口。因此这是对独立稿实际字节的非作者核验，不是全课题盲审。独立稿关于其形成时未读根主投影稿的陈述不因本次后续阅读而被改写；本审查亦不把这种作者形成历史转移为审查者盲性。本轮未读根的新 `PROJECTED_PAIR_PROOF.md`，没有用它补证。

## 1. 实际来源与绑定

| 来源 | 本轮实际阅读和用途 | SHA-256 |
|---|---|---|
| `two-elliptic-compatibility/HIGHER_ROW_CONTRACT.md` | 全文；一般高行投影、另一分量和原三边范围 | `5ee395fc46c92b9161bafec1fdf9e690456526e9038b7c1efed540ffff56b1ad` |
| `two-elliptic-compatibility/HIGHER_ROW_INDEPENDENT.md` | 全文；逐式 HI.1–21、实频率推广及边界 | `ab7df7bbf6d698c2ee6bb223c06fe478cc34ecc37db1806bc8a774a9c037d9e0` |
| `net-mixed-cancellation/INDEPENDENT.md` | 第 44–119 行，NC.4–10；完整非单位基相干 Z、几何系数及缩放 | `25111397d32eef2751a91b1ad1ab6a446794742874b97bf6b0b73b3964d11a58` |
| `three-edge-compatibility/MAX_RECEIVER_RATIO.md` | 全文；重新手核一般 P>Q 的严格比值 | `ff52531d6e1b5563c99504aba8e6b6e4e5afce77b76e7e286e74d397c3d610c5` |
| `two-elliptic-compatibility/CONTRACT.md` | 全文；原整数三频、同一 U0 线性及 U1、U2 非零面积的对应域 | `ee05b39370f178cac5aebcf3c3046478c848c74b0078ee26edafb3282029ad52` |

旧 NC 和 MAX 是先前接受的接口，本轮实读范围如表，不冒记旧 NC 全部原始 Leray 展开在本轮重审。根主投影稿及面积稿属于此前实际审过的背景，本轮不借它们替代被审证明。工具只用于文本读写和 SHA-256，全部数学核验为手工符号，无科学程序、数值求值、数组、选参、扫描、Git、重置、外发或发布。

## 2. HI.1–5：更宽域、面积规范和完整映射

本稿只要求 P>Q，不要求 P 与另一发送平方长度相异。因此 \(d_r=0\) 是合法边界。三频实线性独立保证两条接收边非平行、\(\Delta_s>0\)，以及两个投影方向的 \(\mathsf S\ne0\)。NC 的分母是非零频率模平方的乘积，故 \(\Lambda_s,\Omega_s>0\)；HI.1 的 \(L_s>0\) 和实系数均合法。实频率的推广在这里仅为有限向量代数；第 6 节应用原环面数据时仍须使用合同的整数频率，不能把任意实向量称为环面 Fourier 实例。

若 \(a=U\cdot E_q=0\)，则 U 在横向复平面中只能沿实方向 \(N_q\)，与非零面积矛盾。旋转实基直接给
\[
U\cdot N_q=a(t-\mathsf C)/\mathsf S,\qquad
U\cdot N_r=a(\mathsf Ct-1)/\mathsf S.
\]
按本稿实际采用的面积规范
\(\mathfrak h_U=(2i)^{-1}p\cdot(\bar U\times U)\)，有
\[
\bar U\times U
=\frac{2i|a|^2\Im t}{\mathsf S}\frac p{\sqrt P},
\]
故 HI.3 的 \(\sqrt P\)、\(\mathsf S\) 及号正确。该规范等于单位频率面积 \(i\widehat p\cdot(U\times\bar U)\) 乘 \(\sqrt P/2>0\)，没有面积符号冲突。因此 t 有限且非实，特别非零。

发送采用 NC 的非单位基 f、n；与发送端正定向单位法向的写法相比，比值包含方向负号，不能逐字照搬单位基中的发送比值。这里
\[
\Re(x_r\bar y_r)=|x_r|^2\xi,\qquad
\Im(x_r\bar y_r)=-|x_r|^2\theta.
\]
又因 \(f_r\times n_r=-(\Delta_r/Q_r)r\)，直接得到
\(\mathfrak h_W=-\Delta_r|x_r|^2\theta\)，与 HI.4 的发送面积号一致。线性 V 的非零 f 投影给 \(x_q\ne0\)，且 \(y_q/x_q=\rho\) 为实；允许 \(\rho=0\)。

从 NC 直接换基，接收系数为
\(u=A_s/\ell_s\)、\(v=B_s/(\sqrt P\ell_s)\)。NC.7 的 e 系数是 \(iL_s\chi_su^2|x_s|^2\)，NC.8 的两个法向项分别是
\(iL_su^2(\alpha_s\Re(x_s\bar y_s)+i\beta_s\Im(x_s\bar y_s))\)
和 \(iL_s\kappa_suv|x_s|^2\)。乘回 e、n 后，公共权重恰为
\(\mu_s=L_s|x_s|^2/\ell_s\)。因此 HI.5 的平面项、\(\kappa_s A_sB_s\)、正的 \(\sqrt P\alpha_q\rho\)，以及另一发送的 \(-i\sqrt P\beta_r\theta\) 均正确。完整发送实、虚相干未被删除；此映射不除 \(\chi_r\)。

## 3. HI.6–8：严格比值和投影等价式

P>Q 使 \(H_q=(P-Q)(4P-Q)+4\Delta_q>0\)，故 \(\chi_q,\kappa_q\) 非零且同号。手工展开 MAX 恒等式并写 \(d=P-Q>0\)，
\[
P\Omega_q-2(2P+Q)H_q
=QK,\quad K=Q^2+7Qd+4d^2+8c_q^2>0,
\]
得到 HI.6 的 \(b=\kappa_q/\chi_q>2\)，不需要 β 零条件。这里 b 是严格边比值，\(\lambda\) 才是两实际通道的权重比；二者不可混用。

HI.7 中 \(\eta,\tau\) 为实，\(k_q\ne0\)，而 \(k_r\) 及 \(\lambda\) 可为零或任一符号。沿 \(E_r\) 点乘完整 HI.5，q 边给
\[
\mathsf C+b(t-\mathsf C)+\eta\mathsf S=bt+\tau,
\]
r 边仅在此投影中因 \(N_r\cdot E_r=0\) 留下 \(\lambda t^2\)。共同除数是非零 \(ik_qa^2\)，接收因子是复平方，不是模方。因此 HI.8 对这个复点积的充要性准确。实际频率 \(r=(c_r/P)p+\ell_r E_r\)，而 Z 总在 \(p^\perp\)，所以改用 r 点乘确实只多正因子 \(\ell_r\)。

## 4. HI.9–12：零平面系数、等长和完整非实根分类

\(\lambda=0\) 当且仅当 \(\chi_r=0\)，此时多项式是 \(bt+\tau\)，b 非零且全部系数实，只可能有实根。这与 t 非实矛盾，所以不能有完整零行。此论证未除 \(\chi_r\)，包括所有合法零系数支。

在当前 \(c_r\ne0\)、\(P,Q_r>0\)、正分母域，
\(\chi_r=0\iff d_rH_r=0\)。因此另一发送等长 \(Q_r=P\) 被覆盖，不等长的 \(H_r=0\) 也被覆盖。等长时另一完整 Z 可能仍有法向相干贡献；这里排除的是总行零的必要投影条件，未误称该边完整向量为零。若 P>Q_r，则 MAX 的正性另保证 \(\chi_r\ne0\)。\(c_r=0\) 明确属于当前域外。

当 \(\lambda\ne0\)，设 t=X+iY、Y 非零，直接取 HI.8 的虚部和实部，依次得
\[
X=-\frac b{2\lambda}\ne0,\qquad
Y^2=\frac{4\lambda\tau-b^2}{4\lambda^2}>0.
\]
这与 HI.10 一致，并给 HI.11 的两个形式根；虚部大小的分母应为 \(2|\lambda|\)，主稿已正确保留。对实际固定 t，HI.10 的全部等式和不等式一起才与这个非实根条件等价；只看负判别式不能替实际 t 过门。

重实根、两个实根、\(\tau=0\)、\(\lambda\tau\le0\)、X=0 等支均按主稿排除。\(\mathsf C,\eta,\rho,\alpha_q\) 未作分母，可以为零；\(\mathsf C=0\) 仍适用同一分类。由于 b 非零，即使降次也没有恒零多项式。另由两实部关系得到
\[
|t|^2=\tau/\lambda>0,
\]
故 HI.12 的两个符号关系正确。发送投影模方为正并不强迫 \(\chi_r/\chi_q\) 为正；主稿没有把负 \(\lambda\) 支删掉。

## 5. HI.13：尚需为零的另一完整分量

旋转关系给 \(E_q\cdot N_r=-\mathsf S\)、\(N_q\cdot N_r=\mathsf C\)。因此 q 边的归一化贡献是
\[
-\mathsf S+\mathsf C
\left[\frac{b(t-\mathsf C)}{\mathsf S}+\eta\right].
\]
r 边平面方向与 \(N_r\) 正交，法向部分按
\(A_r=at\)、\(B_r=a(\mathsf Ct-1)/\mathsf S\) 代入，恰为
\[
\frac{\mu_r}{k_q}
\left[\frac{\kappa_rt(\mathsf Ct-1)}{\mathsf S}
+\sqrt P(\alpha_r\xi-i\beta_r\theta)t^2\right].
\]
这逐项核得 HI.13，尤其发送虚相干的负 i、\(\mathsf S\) 的位置和 \(\mu_r/k_q\) 均正确。该式在 \(\chi_r=0\) 时仍合法。两个正交横向点积一起为零才是完整行零；主稿明确没有求解 HI.13，不把 HI.8–12 的投影分类当作完整行充分性。

## 6. HI.14–19：实际权重、两行共享投影和线性比值

对有向接收 \(i\leftarrow j\)，NC 的
\(U_j\cdot p_i=\Delta_{ij}x_{ij}/P_j\) 给 HI.14 第一式。再直接代入本稿的权重定义：
\[
\mu_{ij}
=\frac{2\Delta_{ij}^{5/2}}{P_i^{3/2}P_j}|x_{ij}|^2
=\frac{2P_j\sqrt{\Delta_{ij}}}{P_i^{3/2}}
|U_j\cdot p_i|^2.
\]
乘 \(\chi_{ij}\) 后与 HI.14 第二式一致。取 j 边与 0 边之比，公共 \(2/P_i^{3/2}\) 消去，精确得到 HI.15；没有遗漏 P_j、P_0 或平方根因子。

因为 U_i 横向，\(U_i\cdot E_{ij}=(U_i\cdot p_j)/\ell_{ij}\)。两个方向相除给
\[
t_i=\sqrt{\Delta_{i0}/\Delta_{ij}}
\frac{U_i\cdot p_j}{U_i\cdot p_0},
\]
即 HI.16。所有分母均由实际活跃性支付，U_i 面积非零仍给 \(t_i\notin\mathbb R\)。

线性发送 U0 的 n 坐标是
\((U_0\cdot(p_i\times p_0))/\Delta_{i0}\)，f 坐标是
\(P_0(U_0\cdot p_i)/\Delta_{i0}\)。相除得 HI.17；若 U0=z0R，非零 z0 精确消去，所以两行的实发送比值确由同一个 R 决定。

在另一行 j 的 HI.16 取模方，得到
\[
|U_j\cdot p_i|^2
=\frac{\Delta_{ij}}{\Delta_{j0}}
|t_j|^2|U_j\cdot p_0|^2.
\]
代回 HI.15，恰好给 HI.18 的 \(\mathcal K_i\) 和 HI.19 的
\(\lambda_i=\mathcal K_i|t_j|^2\)。因 \(\chi_{i0}\ne0\)，定义合法；即使 \(\chi_{ij}=0\)，此恒等式也以两端同为零保持有效。

\(\mathcal K_i\) 是共享数据系数，含当前 U0、Uj 的实际投影模方，并非纯几何常数，也不是两个新增的独立幅度。其符号由 \(\chi_{ij}/\chi_{i0}\) 决定。更改任何种子的模长必须按同一数据同时更新对应 \(\lambda_i,\mathcal K_i\) 和相关投影；比值 \(t_j\) 对该种子的整体非零复缩放不变，但这不释放其它权重。

## 7. HI.20–21：联合必要恒等式及范围

若两个高行都通过投影门，\(\lambda_1,\lambda_2\ne0\)，且
\(|t_i|^2=\tau_i/\lambda_i\)。因此
\[
\lambda_1\lambda_2
=\mathcal K_1|t_2|^2\lambda_2
=\mathcal K_1\tau_2,
\qquad
\lambda_1\lambda_2=\mathcal K_2\tau_1.
\]
HI.20 的交叉指标准确。这里 \(\tau_i\) 是本稿 HI.7 的实多项式常数，不是极化面积或最低行投影比。两个恒等式必须与实际复 t_i、各自实二次式和负判别式、两个 HI.13 一起检验，不能单独当作充分条件。

按原排序，接收更长的 \(\chi_{10},\chi_{20},\chi_{21}\ne0\) 已由 MAX 支付；\(\chi_{12}\) 不能如此处理。因为该边 c 非零、长度不同、分母正且其余因子非零，确有
\(\chi_{12}=0\iff H_{12}=0\)。HI.9 随即排除这一子面上的中间完整零行，得到 HI.21。主稿没有声称最低 β 零几何必然落在该面，也未从其补集推出联合可解。

未发现 HI.1–21 的公式、非零条件或范围存在待修问题。比根主投影稿更宽的等长域已明确且由不除 \(\chi_r\) 的论证处理；新增共享权重关系来自实际 NC 投影转换，没有把各行参数独立化。

通过范围严格止于有限完整相干代数：一条较短线性发送边所给的完整投影二次门、合法退化支和另一完整分量，以及原三边两高行的实际共享权重必要关系。原整数几何、固定三种子是否联合通过、整组三行相消、C 原方向和共同模板幅度仍未解决。没有实际数据、真实 NS 窗口、来源比、跨代余项、再生成、奇性或全局正则性结论；没有修复或追认旧失败证据。FULL HIGHER ROWS OPEN；NO-CANDIDATE；NOT CLAY。

本轮只写本审查文件；实际全文回读并复核源字节后停改，最终 SHA-256 另行提供。
