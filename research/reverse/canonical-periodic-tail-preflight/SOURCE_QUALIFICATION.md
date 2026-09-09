# 原截止交换项的端点正则性与完整周期定义

2026-09-09，PRIVATE_CORE。条件使用同一外部原文构造、已经固定的 \(c,\mathcal A\) 和 Cor.10.6 的周期化，不选择新截止或缩放。本稿作者有此前原文读记经历，已知合同披露的根先前手推，未读本题根证明，不称全课题互盲；外部全文／Lean认证仍未完成。
**条件来源资格通过：\(W=\nabla c\times\mathcal A\) 的光滑零延拓具有全空间、全部固定阶混合导数的兼容单侧终端极限；按速度量纲定义的 \(\Pi W\) 在整个固定单位环面光滑至 \(t=1\)。\(\Pi(cu_{\rm loc})\) 在 \(t<1\) 的完整定义与其 curl 的固定支撑也成立。** 本稿不证明新残差为零或外部无力奇性。

## 1. 实际原文范围与字节

全文读本题合同；复读固定抽取文本的 PDF页15中 Theorem3.1、16页§3.5、116–118页及119页 Lemma10.2证明、125页与126页 Cor.10.6证明末段。对应文本732–799、5624–5810、6051–6116行；均为此前读过的页面，不声称重审完整构造。
复用并实际视读原页图：forced-tail-audit/reading-evidence/force-map/pdf-page-118.png 和 reading-evidence/periodic-p125.png；核 (10.3)–(10.5) 的乘积／域以及 Cor.10.6 的速度缩放和时标。没有新渲染或修改第32包。
下表路径相对 research/reverse/，SHA-256 为本轮实际完整文件字节。

| 来源 | SHA-256 |
|---|---|
| canonical-periodic-tail-preflight/CONTRACT.md | 3005cf028be47e53a574ffc27d6862da1543f4522f23cb517dd84720df722634 |
| forced-tail-audit/sources/navier-stokes.pdf | 0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f |
| forced-tail-audit/sources/paper-text.txt | 7c8d1e236e6285de297f4d88d05056f3de5a8bdcc6454ddc81b665cf98ae0c26 |

## 2. 同一原乘积先在局部域定义，再光滑零延拓

以下以 \(y\in\mathbb R^3,s<1\) 记原文空间、时间，\(\tau=1-s\)。原域是 \(\Omega_*=\{\tau>0,\ q<q_*\}\)，\(u_{\rm loc}=\operatorname{curl}\mathcal A+\mathcal B e_\theta\)；Theorem3.1(i) 给实际代表的笛卡尔光滑性，包括轴。
Prop.10.1／页118已经固定 \(c(y,s)=\chi_x(y)\chi_t(s)\)。\(\chi_x\) 在含原点的固定柱形邻域等于1，空间支撑 \(K\) 紧含于原指定柱体；\(\chi_t=0\) 在 \(s\le1-\tau_0\)，\(\chi_t=1\) 在 \(1-\tau_0/2\le s<1\)。原 (10.3) 的选择使 \(c\) 的支撑与所有实际截止导数的支撑在 \(\tau>0\) 时保持 \(q\le q_*/2<q_*\) 的域边界间隙。
定义 \(a=cu_{\rm loc}\) 及 \(W=\nabla_yc\times\mathcal A=\chi_t\nabla\chi_x\times\mathcal A\)，仅在这片原域中相乘；在其外定义为0。固定截止的光滑性、域边界间隙和原场的笛卡尔光滑性给 \(a,W\in C^\infty(\mathbb R^3\times[0,1))\)，空间支撑均在 \(K\)，早期共同为零。这没有给 \(\mathcal A\) 人为定义全域值。
原 (10.4) 的乘积式逐点成为完整零延拓后的 \(u=a+W\)。一般不能令 \(a\) 单独无散；其散度为 \(\nabla c\cdot u_{\rm loc}\)，完整 \(W\) 的散度与之相消。光滑零延拓保证这些身份没有遗漏支撑边界分布。

## 3. \(W\) 的全部单侧端点导数

令 \(D_c=\operatorname{supp}\nabla\chi_x\)。它是 \(K\) 内的固定紧集，且与原点一个固定邻域分离；全部 \(W\) 的混合导数支撑都在 \(D_c\)。晚时 \(\chi_t=1\)，只需在 \(D_c\) 上核 \(\nabla\chi_x\times\mathcal A\)。在原点邻域直接用 \(W=0\)，不作“零乘以终端奇异势”的定义。
**第一类终端点：\(y\in D_c,\ z\ne0\)。** 原坐标给 \(q\ge |z|^{1/D}>0\)，其中 \(D=1/2-h\)。在该点一个紧邻域和足够晚时段，\(q\) 有正下界，上界仍小于 \(q_*\)。Theorem3.1(ii) 直接对实际 \(\mathcal A\) 的所有笛卡尔时空导数给一致界及兼容极限；乘以固定 \(\nabla\chi_x\) 后同样成立。这包括 \(r=0,z\ne0\) 的轴上点，不使用只在 \(X>0\) 才成立的估计。
**第二类终端点：\(y\in D_c,\ z=0\)。** 因 \(D_c\) 避开原点，此时 \(r>0\)。在一个小邻域保留半径正下界；由原 (10.3) \(q\le C_0(\tau+|z|^{1/D})\)，使该邻域足够靠近该点且时间足够晚，就有 \(X=r^2/(2q)>X_{\rm ext}\)。这是分析用邻域，不改变任何原截止或构造参数。Theorem3.1(iii)／(3.5) 在这里给 \(\mathcal A=0\) 的开域身份，故所有 \(\mathcal A\) 导数及 \(W\) 精确为零。
这两类邻域覆盖固定紧集 \(D_c\)，有限子覆盖给出同一终端时间窗中的每个固定阶全空间一致导数界。每个导数都有局部一致极限；在重叠处极限由同一个 \(W\) 唯一确定，有限覆盖遂给全空间一致极限。空间／时间基本定理使这些极限互相兼容。
因此存在唯一由左侧 jets 决定的 \(W(\cdot,1)\)，使 \(W\in C^\infty(\mathbb R^3\times[0,1])\) 按单侧意义成立，支撑仍在 \(D_c\)。对任意固定 \(\alpha,\ell\)，\(\sup_{y,\,0\le s\le1}|\partial_y^\alpha\partial_s^\ell W|<\infty\)：终端窗由上述覆盖支付，其余闭时间段由既有光滑性和固定紧支撑支付。这里不要求给出 \(s>1\) 的新物理延续。
该论证只用 Theorem3.1(i)–(iii)、原域／截止及页119已有的同类终端覆盖；未使用 (5.42)，未把局部方位公式当成轴上统一估计，也未计算 \(W\) 是否非零。

## 4. 固定 \(\Pi\) 的量纲、时间链式因子和端点

保持合同的 \(\nu=1\) 与原 Cor.10.6 已固定的 \(\lambda>1\)。记 \(Q_0=(-1/2,1/2)^3\)，\(\lambda^{-1}K\Subset Q_0\)，\(t_0=1-\lambda^{-2}\)，\(s(t)=\lambda^2(t-t_0)\)。对上面完整零延拓后的速度型对象 \(g=a,W,u\)，定义
\[
 (\Pi g)(x,t)=\lambda\sum_{n\in\mathbb Z^3}g(\lambda(x+n),s(t))\quad(t_0\le t<1),\qquad \Pi g=0\quad(t<t_0).
\]
\(\Pi\) 是这个速度缩放／周期化操作，不是 Leray 投影；不能用原力的 \(\lambda^3\) 因子代替前面的 \(\lambda\)。\(t=1\) 恰映到 \(s=1\)。早期共同零时段支付 \(t_0\) 处的光滑拼接。
各副本的支撑由固定 \(\lambda^{-1}K\Subset Q_0\) 保持正间隙，局部有限且任一点至多一个非零副本。对 \(g=W\)，包括单侧端点，
\[
 \partial_x^\alpha\partial_t^\ell(\Pi W)
 =\lambda^{1+|\alpha|+2\ell}\sum_{n\in\mathbb Z^3}
 (\partial_y^\alpha\partial_s^\ell W)(\lambda(x+n),s(t)).
\]
固定 \(\lambda\)、分离支撑和第3节的全空间极限给 \(\Pi W\in C^\infty(\mathbb T^3\times[0,1])\) 的单侧结论；每个固定阶范数一致有界。端点取值始终来自同一原 \(W\)，没有新取尾部或重置初值。
若只需合同中的 \(H=\mathbb P_T\Pi W-\operatorname{mean}_T\Pi W\)，上述输入也足够：单位周期 Fourier 中 \(k\ne0\) 时投影矩阵为 \(I-kk^T/|k|^2\)，\(k=0\) 为 \(I\)。它在每个 Sobolev 阶有界；对全部时间导数应用，再用任意高阶 Sobolev 嵌入，得 \(H\) 全部固定阶导数的兼容极限和一致界。均值项是单独的光滑常向量减法，没有把力投影零模改成0。

## 5. \(\Pi(cu_{\rm loc})\) 的完整 curl 支撑

\(\Pi(cu_{\rm loc})\) 必须指第2节全域零延拓的 \(a\) 再施加第4节的 \(\Pi\)，不能把未知域上的局部公式直接周期相加。它在每个 \(t<1\) 光滑、实值、周期，支撑于同一紧集 \(K_T=[\lambda^{-1}K]\Subset Q_0\)；本稿不声称 \(a,\Pi a,u\) 在 \(t=1\) 光滑或有界。
局部微分给完整身份 \(\operatorname{curl}_ya=\nabla c\times u_{\rm loc}+c\,\operatorname{curl}_yu_{\rm loc}\)（继以光滑零延拓），以及 \(\operatorname{curl}_x\Pi a=\lambda^2\sum_n(\operatorname{curl}_ya)(\lambda(x+n),s(t))\)。因此 \(\operatorname{supp}\operatorname{curl}\Pi a\subset K_T\)，在固定非空开集 \(\mathbb T^3\setminus K_T\) 上恒零。
完整周期投影的 Fourier 身份 \(k\times(\mathbb P_k\widehat a)=k\times\widehat a\) 与常向量 curl 为零，还给合同规范场 \(V=\mathbb P_T\Pi a-\operatorname{mean}_T\Pi a\) 满足 \(\operatorname{curl}V=\operatorname{curl}\Pi a\)。这只支付开集零涡量的来源资格；并不声称投影后速度仍紧支撑，亦不在本稿作无力尾段的解析性排除。

范围停在同一原乘积的端点正则性、固定周期定义和 curl 支撑；没有原力 jets／\(H,b,B\) 实际矩值、强残差证书或外部无力解认证。科学程序／数组／FFT／Lean／Git／外发均为0；只写此文件，全文自读后停稿。
