# 联合方向独立稿的序贯非作者审查

2026-09-08，PRIVATE_CORE。**PASS：JDI.1–24、最大不变核论证、全部秩与维数分支，以及同一严格域的反向恢复均成立，无须数学修订。** 实特征值与共同代数实根准确对应；最终仍须原严格域，不能用非零核代替合法方向。

本人不是本稿作者，但已先完成本项 PROOF.md 的非作者审查；此次随后首次全文读取 INDEPENDENT.md，属于序贯非作者审查，不能称为互盲审查或另一路独立形成。本人也有前阶段最低主稿、LAI/ASI、剩余虚部独立稿作者及相关审查历史。下文直接核本稿自身的常数项优先列规范、算子及恢复公式，不把先审主稿的结论当作本稿证明，也不借未来整包状态补证。

全部矩阵、算子、秩与实根论证均为手工符号；工具仅读写文本与 SHA 元数据。未执行科学矩阵程序、数值数组、求根、实际选参、枚举、扫描、Git 或外发。

## 1. 实际阅读与字节

路径相对于 research/reverse/。

| 来源与实际范围 | SHA-256 |
|---|---|
| joint-direction-compatibility/CONTRACT.md，本轮再次全文读取 | 5b8dc82300556766260a13c1f9124d7a02989ec14e242cf5aad8b49fc5d16ad3 |
| joint-direction-compatibility/INDEPENDENT.md，本轮首次全文读取，逐式核 JDI.1–24 | 4ed20002939dbafce9f20955dbcf3a0efde1da8aa2ad1f040ce474b9c5861c26 |
| remaining-real-compatibility/INDEPENDENT.md，本轮首次全文读取，核 RRI 的真实相干、两个实部乘数、余式和严格必要界 | df69ea23d67efa7b970010327833480435867cad305b665e077930e7ae71725f |
| area-square-compatibility/INDEPENDENT.md，本人此前全文自读；紧前审查实读第 40–181、216–250、278–386 行，本轮再读第 302–386 行 | 489fd488a5dbc8dcdc1336904a16d8dcbe3817077ec74137ead1706f545d4acc |
| remaining-imaginary-compatibility/PROOF.md，紧前主稿审查首次全文读取，本轮再读第 59–111 行 | 638ef8812fad8bf3337ecf1c6bd73a4fb73e34843eaa94a2b6a1cb8daff3fdef |
| full-high-row-reduction/PROOF.md，紧前审查实读第 1–132 行，本轮再读第 112–129 行 | 3d02da817e164bbf8f75bdddfea74a4e0d2b14c12d890952aeeb727866cc3c6b |

以上字节均已实测，被审独立稿与作者停改值一致。作为序贯历史，本项主稿曾以
5e3a9708fb07f396a161dc333312d8a310dfb36d5d3d685eb8c2089b80931e62
完成先前审查；它不替代本轮针对独立稿的逐式论证。内部转引不计为另行实读。

## 2. JDI.1–11 的实际系数与余式

JDI.1 的最低实代表确有 \(R\cdot E_{01}=1\)、\(R\cdot E_{02}=r\)。JDI.2 的同一 \(w\)、最低唯一 \(s_i\)、四个仿射系数和 JDI.4 的两个实际 \(Q_i\) 与所读 ASI、RRI 一致。所有几何系数都在求 \(r\) 前固定；没有把高边发送相干或强度变成独立参数。

JDI.3 展开 \(P\) 的四个系数正确。在当前合法最低双 beta 零域，ASI 明列的 \(\alpha_{i0}>0\)、非零 \(\chi_{i0},S_i,S,C\) 给 \(b_{11}b_{21}\ne0\)，故 \(p_3p_0\ne0\)。稿中用 \(x>1\) 表达正性，仍处于来源的同一合法几何域，不据此扩展到其它长度分支。

JDI.5 的面积式与 JDI.6 的严格域组合后，才推出两个正平方和 \(Q_1Q_2\ne0\)。独立稿没有仅凭严格域就提前使用完整高投影的 iff。

JDI.7 与 RI 的两个完整虚部分子逐项相同。JDI.8 与本轮实读 RRI.11 相同；特别是第二行的 \(-2\mu_2rQ_2\) 和第一行的 \(-2\mu_1Q_1\) 不对称，没有误补一个 \(G\)。其发送系数来自
\[
\frac{X_j}{M_j}=-\frac{\mu_j}{2B_j},\qquad
G_i=\mathfrak a_i+\frac{\mathfrak d_i\mu_j}{2B_j}.
\]
\(\mathfrak a_i,\mathfrak d_i,\alpha_{ij},G_i,\ell_i\) 及最高次系数都没有被当作分母。

JDI.9 的递推由
\(r^3+\sigma r^2+\tau r+\upsilon\equiv0\pmod P\)
逐阶成立；每个 \(V_n\) 至多二次。两条实部行采用
\[
f_{i+2}=p_3\mathcal L_i-\lambda_{i3}P
\]
而非未缩放余式，这一点在 JDI.10 中已明确。因为 \(p_3\ne0\)，在 \(P=0\) 上其零集不变，\(\lambda_{i3}=0\) 也不例外。因此 JDI.11 的双向等价及全部降次、恒零支均成立。

## 3. JDI.12–13 的列规范与直接秩分支

本稿列顺序是常数、一次、二次，即
\[
v(r)=(1,r,r^2)^T,\qquad \mathsf A v(r)=0.
\]
这与先审主稿的列顺序不同，不能照搬核坐标；独立稿使用
\(z=(z_0,z_1,z_2)\)、\(z_0\ne0\) 是正确的。

秩三无非零核，故无候选。秩二的核直线包含 \(v(r)\) 当且仅当
\[
z_0\ne0,\qquad z_0z_2=z_1^2,\qquad r=z_1/z_0.
\]
JDI.13 恰为 \(z_0^3P(z_1/z_0)=0\)，所以连同同一个严格域便保真；\(z_0=0\) 不能增入无穷方向。秩一时任一非零行多项式张成五行，故只检验它与 \(P\) 的共同实根，常数、一次、二次及重根都保留。秩零时仍须非零三次 \(P\) 与严格域，不能宣布全部方向通过。

两条实部余式的非零固定缩放可以带号，但不改变核或秩。一般可逆常数行变换也不改变共同零集；没有用依赖未知 \(r\)、可能为零的缩放来改变行规范。

## 4. JDI.14–18 的 companion 算子与最大不变核

记
\[
\mathsf T=
\begin{pmatrix}
0&1&0\\
0&0&1\\
-\upsilon&-\tau&-\sigma
\end{pmatrix}.
\]
逐行作用于 \(v(r)\) 给
\((r,r^2,-\upsilon-\tau r-\sigma r^2)^T\)，所以
\(\mathsf T v(r)=rv(r)\) 恰等价于 \(P(r)=0\)。

反向，若非零实向量 \(z\) 满足 \(\mathsf Tz=rz\)，前两行给
\(z_1=rz_0,z_2=rz_1\)。若 \(z_0=0\)，三坐标全部为零，矛盾；故
\(z=z_0v(r)\)，最后一行再给 \(P(r)=0\)。
因此本算子的实特征向量天然满足所需抛物线坐标关系，无额外有限或无穷方向混入。它不是实际发送比 \(T=kM_1/M_2\) 的替代参数。

令
\[
S(\mathsf T)=\mathsf T^3+\sigma\mathsf T^2+\tau\mathsf T+\upsilon I.
\]
独立稿对 \(S(\mathsf T)=0\) 的直接证明成立：以
\(e^T=(1,0,0)\)，末行给 \(e^TS(\mathsf T)=0\)；又因
\(S(\mathsf T)\) 与 \(\mathsf T\) 交换，
\[
(e^T\mathsf T)S(\mathsf T)
=(e^TS(\mathsf T))\mathsf T=0,\qquad
(e^T\mathsf T^2)S(\mathsf T)=0.
\]
三行 \(e^T,e^T\mathsf T,e^T\mathsf T^2\) 正是坐标行基，故整算子为零。这不依赖对角化或特征根互异。

现在
\[
\mathcal N=\ker_{\mathbb R}
\begin{pmatrix}
\mathsf A\\ \mathsf A\mathsf T\\ \mathsf A\mathsf T^2
\end{pmatrix}
\]
对 \(\mathsf T\) 不变：若 \(z\in\mathcal N\)，前三个零式已给
\(\mathsf A\mathsf Tz=\mathsf A\mathsf T^2z=0\)，且
\[
\mathsf A\mathsf T^3z
=-\sigma\mathsf A\mathsf T^2z-\tau\mathsf A\mathsf Tz
-\upsilon\mathsf Az=0.
\]
故 \(\mathsf Tz\in\mathcal N\)。

反过来，任何包含于 \(\ker\mathsf A\) 的不变子空间，其每个向量及前两次像都被 \(\mathsf A\) 湮灭，因而包含于 \(\mathcal N\)。这确实证明“最大不变子空间”，不是只构造某个充分或必要的较小核。叠加到二次已经够用的理由正是三阶多项式恒等式；没有漏掉更高次条件。

JDI.18 的两个方向也完整：

- 同一实根满足 \(P(r)=0,\mathsf Av(r)=0\) 时，
  \(\mathsf T^jv(r)=r^jv(r)\)，故 \(v(r)\in\mathcal N\)，给限制算子的实特征值。
- 限制算子的实特征值有非零实特征向量 \(z\in\mathcal N\)；实齐次线性系统在该实特征值处有非零实核，故不必以复特征向量补充假设。由前面的反向论证，\(z=z_0v(r)\)、\(P(r)=0\)，再由 \(\mathcal N\subset\ker\mathsf A\) 得 \(\mathsf Av(r)=0\)。

所以共同代数实根与
\(\operatorname{spec}_{\mathbb R}(\mathsf T|_{\mathcal N})\)
准确相等。广义特征向量没有额外贡献；不可对角化、重复根、零行和相关行都不破坏该证明。

## 5. 不变核维数的全部分支

\(m=3-\operatorname{rank}\mathsf O\) 是秩零化度等式，且 \(\mathcal N\) 实不变，限制算子有确定的实表示。

- \(m=0\)：无特征值，候选为空。
- \(m=1\)：限制算子为一个实标量，产生唯一不同实代数候选，仍须严格域。
- \(m=2\)：其特征多项式为
  \(x^2-(\operatorname{tr}T_N)x+\det T_N\)。判别式负、零、正分别给零个、一个、两个不同实特征值；重根时无需可对角化。非零不变核可以没有实特征值。
- \(m=3\)：\(\mathcal N=\mathbb R^3\) 强制 \(\mathsf A=0\)。直接展开 companion 的特征多项式得到
  \(x^3+\sigma x^2+\tau x+\upsilon=P(x)/p_3\)，故取 \(P\) 的全部不同实根。

改变 \(\mathcal N\) 的实基只作限制算子的相似变换，不改变实谱；对五行作可逆常数变换，也同时对 \(\mathsf O\) 的三个块作相应可逆行变换，不改变 \(\mathcal N\)。
所有候选均为非零三次 \(P\) 的根，故至多三个不同实方向。没有因此得到有限个实际初值，也没有证明某个秩或 \(m\) 能由实际几何实现。

## 6. JDI.19–24 的严格恢复与四个乘数

JDI.19 最后与同一个 \(\mathscr D(r)\) 相交，保留
\[
rF_1F_2\ne0,\quad w/\omega>0,\quad
E_1>0,\quad g_2Q_2rF_1<0.
\]
面积式的实际正乘数
\[
P_2\mu_1\mu_2S_1^2S_2^2r^4F_1^2
\]
乘 \(D_2-k^2D_1\) 正好给 \(\mathcal A\)，验证 JDI.20。由此两个平方均正、\(X_iB_i<0\)、\(Q_1Q_2\ne0\)，所有后续分母才合法。

按 JDI.21 只保留一个共同符号
\(y_1=\varepsilon\sqrt{D_1},y_2=ky_1\)。实际 \(k\) 的号没有被平方门删除，两个共同符号又保持实部、模方与相对比不变。

JDI.22 的 \(h\) 与 ASI.23 一致。其号等于
\(-\operatorname{sgn}(g_2X_2)\)，而
\[
g_2X_2<0\iff g_2Q_2rF_1<0
\]
只乘正的 \((rF_1)^2\)。故面积正性没有被误用为共同幅度正性。实际发送比 \(w/\omega\)、原相位和同一整体尺度依此恢复；同一 \(K_1B_2=K_2B_1\) 给两个实际投影权重，而不是分别选择两条最低幅度。

JDI.23 的虚部乘数与 RI.7 完全一致，保留真实
\(T=kM_1/M_2\)。实部乘数可直接从 RRI.9–12 核得：
\[
\mathcal L_1=-\frac{4F_1^2Q_1}{\mu_1}\mathcal R_1,\qquad
\mathcal L_2=-\frac{4F_2^2Q_2}{\mu_2r}\mathcal R_2.
\]
两行的 \(r\) 位置、负号和常数四都正确；它们在已恢复域非零，不需当作正因子。
于是两个指定高复点积加四个实残差零，正由实读 FR.12 恢复完整两高行。连同同一最低接口，确达当前分支完整 \(M_0=0\) 及最低 \(C\) 非零原方向。

反向同一规范、原严格域和来源明列接口中的原数据满足该目标时，必给这同一个 \(r\) 的全部六个原多项式等式，因而经 JDI.11、18 落入 \(\mathscr C\)。故 JDI.24 的条件 iff 成立，其范围仍是本文明确的固定分支，不能扩展为所有初值的分类。

## 7. 必要号界、未覆盖支与结论

末节最长虚部推出实际 \(T>0\)，继而 \(k>0\)、\(GF_1F_2<0\)，并与面积正性共同给所列 \(Q_i\) 严格区间。RRI 的
\[
B_iG_i=\mu_iX_i/B_i+1+\mu_i\rho_i/2,\qquad
-2/\mu_i<X_i/B_i<0
\]
又直接给稿中的严格 \(B_iG_i\) 必要界。二者都没有被当作替代完整等式的充分条件。
\(G_2=0\) 被最长侧的正下界排除；\(G_1=0\)、\(\alpha_{ij}=0\) 或相关系数为零则仍由原式判断，未因除法遗漏。

形式零方向、\(F_1F_2=0\)、非正面积、错误发送号、\(h\le0\) 均未从特征值或清分母步骤增入。最低零投影、无穷方向、\(C_0=0\) 和其它 \(\chi=0\) 分支未覆盖，不能称已被排除。

本次接纳至于完整 \(M_0=0\) 加最低 \(C\) 非零原方向的同方向条件接口。其它两个 \(C\) 方向、共同模板、实际整数几何和种子存在或全域障碍仍未付。没有实际选参或实例，没有 NS 两步、有限时间再生成、统一余项、固定初值无限尺度、有限总时间或奇性结论。精确首项零的条件判据也不排除任意正来源容限；旧失败不变。

审查结论 PASS；SEQUENTIAL NONAUTHOR REVIEW；EXACT REAL SPECTRAL CORRESPONDENCE WITH STRICT RECOVERY；REALIZATION OPEN；NO-CANDIDATE；NOT CLAY。
