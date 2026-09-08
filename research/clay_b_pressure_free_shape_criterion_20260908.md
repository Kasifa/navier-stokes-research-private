# 小形状耗散判据：不再要求统一的压力上界

2026-09-08。PF，PRIVATE_CORE。局部条件证明；一般三维 NS 仍 OPEN / NOT CLAY。没有充分查新，不宣称原创性或真人同行评审。

这一节删除 SC 判据中的独立共同压力上界。保留的条件是：一个尺度上的局部动能与梯度耗散有界，而且形状耗散足够小。证明不要求原速度序列时间强紧，而对其局部修正部分取强极限，再逐时间切片使用 SC 的秩一／仿射分类。

这不是任意初值的正则性证明。共同能量上界和足够小的形状耗散尺度，仍须由同一实际 NS 演化产生。VR 的变参考检查没有给出这一步；本节也不把它换成另一个已证明的结论。

## 1. 对象与命题

单位黏性、无外力，\(Q_r=B_r(0)\times(-r^2,0)\)。设 \((u,p)\) 是 \(\overline{Q_1}\) 的某个时空邻域上的局部适当弱解：分布 NS、无散度、局部能量类、\(p\in L^{3/2}_{\rm loc}\) 及局部能量不等式。沿用
\[
 \mathsf A(r)=r^{-1}\operatorname*{ess\,sup}_{-r^2<t<0}\int_{B_r}|u|^2,
 \qquad \mathsf E(r)=r^{-1}\int_{Q_r}|\nabla u|^2.
 \tag{PF.1}
\]
令 \(G_{ij}=\partial_j u_i\)、\(d(G)\) 为完整梯度到所有实秩至多一矩阵的 Frobenius 距离，
\[
 \Theta(G)=d(G)G/|G|^{3/2}\ (G\ne0),\quad\Theta(0)=0,
 \qquad \mathsf K(r)=r^{-1}\int_{Q_r}|\nabla_x\Theta(\nabla u)|^2.
 \tag{PF.2}
\]
弱导数在整个球上理解。WE 给每个这样的解在闭柱邻域内的 \(\Theta\in L^2_tH^1_x\)；其存在可使用该解稍大母柱上的有限压力范数，不要求这些范数在不同解间一致。零阶界 \(|\Theta(G)|^4\le|G|^2\) 则只用 E。

**命题 PF-A（本地证明，PROVED IN STATED SCOPE / CONDITIONAL）。** 对每个有限 \(M>0\)，存在 \(\varepsilon_{\rm PF}(M)>0\)，使
\[
 \mathsf A(1)+\mathsf E(1)\le M,
 \qquad \mathsf K(1)<\varepsilon_{\rm PF}(M)
 \quad\Longrightarrow\quad (0,0)\text{ 正则}.
 \tag{PF.3}
\]
正则指速度在某个后向内柱本质有界。阈值不依赖任何共同的 \(\mathsf D(1)\)，但没有有效数值或正则半径模量。没有删除每个原解的适当性，也没有把一般分布压力解自动纳入该命题。

## 2. 在有时间紧性的部分上取极限

所用文献接口是 [Hyunju Kwon，arXiv:2104.03160v3](https://arxiv.org/html/2104.03160v3)：Lemma 2.5 的局部 Leray 分解及 Theorem 1.4 的速度小量正则性。前者给 \(u=v+h\)，h 调和且无散，v 满足带 h 和无散力 f 的适当方程；q 由速度平方控制，h、f 的空间光滑界由局部动能控制。后者在速度 \(L^3\) 足够小时给局部有界性，不要求压力小量。这些是文献结论，不是本节新证明；下面只使用其固定内外球版本。

反设 PF.3 不成立。存在一个固定 M 和中心均非正则的适当解序列 \((u_n,p_n)\)，满足 A+E 上界及 \(\mathsf K_n(1)\to0\)。用同一个固定空间截止，在 \(B_{1/2}\times(-1,0)\) 上作上述分解，记修正压力为 \(q_n\)，与原压力及梯度模区分。具体 \(v_n=-\operatorname{curl}\Delta^{-1}(\varphi\operatorname{curl}u_n)\)，\(h_n=u_n-v_n\)，\(\varphi\in C_c^\infty(B_1)\) 在 \(\overline{B_{1/2}}\) 的邻域为一。原方程变为
\[
 \partial_tv_n-\Delta v_n+(v_n\cdot\nabla)v_n
 +(v_n\cdot\nabla)h_n+(h_n\cdot\nabla)v_n+\nabla q_n=f_n,
 \quad\operatorname{div}v_n=\operatorname{div}h_n=\operatorname{div}f_n=0.
 \tag{PF.4}
\]
这里 \(h_n\) 不必是梯度；它不是 Wolf 的 Stokes 压力投影。所有截止项和 \(h_n\otimes h_n\) 的贡献保留在文献定义的 \(q_n,f_n\) 中。尤其不能把 f 设为零。

由能量插值与分解的界，在固定内域上一致有
\[
 \|v_n\|_{L^\infty_tL^2_x}+\|\nabla v_n\|_2+\|v_n\|_{10/3}
 +\|q_n\|_{5/3}\le C(M),\qquad
 \|h_n\|_{L^\infty_tW^{k,\infty}_x}+\|f_n\|_\infty\le C_k(M).
 \tag{PF.5}
\]
所需 k 任意固定；至少取2用于空间紧性。q 界来自 \(u_n\in L^{10/3}\)，不是原压力界。PF.4 使 \(\partial_tv_n\) 在固定内球的一致 \(L^{5/3}_tW^{-1,5/3}_x\) 界成立：梯度项 L2、二次项 L5/3，其余项有界系数乘能量函数，均足够。

令 \(R=3/8\)、\(J=(-1/2,0)\)。Aubin–Lions 及 L10/3 插值给共同子列
\[
 v_n\to v\text{ 强 }L^2\text{、强 }L^3(B_R\times J),\quad
 \nabla v_n\rightharpoonup\nabla v\text{ 弱 }L^2,\quad q_n\rightharpoonup q\text{ 弱 }L^{5/3}.
 \tag{PF.6}
\]
同时将 \(h_n\)、所需空间导数及 \(f_n\) 在 L∞ 作弱* 子列，极限记为 \(h,\nabla h,f\)。h 及其空间导数保留调和性、无散度和相应界；f 保留一致界及无散度，不宣称 f 调和。把 PF.4 写为散度形式，强 v 与弱* h 足以传两个交叉项，得到同形式的修正极限方程。不认定 \(v+h\) 仍是原 NS 解，也不认定 f 仍等于弱极限速度的原显式非线性函数。

适当能量不等式也保留：\(q_nv_n\) 用弱 L5/3 与强 L5/2；\(|v_n|^2h_n\)、\(v_n\otimes v_n:\nabla h_n\)、\(f_nv_n\) 用强 L1 与弱* L∞；纯速度三次项用强 L3；耗散用下半连续性。不存在一个被删除的 \(h_n\otimes h_n\) 振荡项，它原已被计入独立的 q、f。没有声称 \(u_n\) 强时间紧，或 \(h_n\to h\) 强时间收敛。

## 3. 逐片分类不需要可测地选择调和参考

令 \(m_n(t)=(\Theta(\nabla u_n))_{B_R}(t)\)。Sobolev–Poincare 给
\[
 \Theta(\nabla u_n)-m_n\to0\quad\text{于 }L^2(J;L^6(B_R)).
 \tag{PF.7}
\]
取同一子列，使 PF.6 的强 L2 和 PF.7 在几乎每个时间切片成立。Fatou 另外给 \(\liminf_n\|\nabla u_n(t)\|_2^2<\infty\) 几乎处处。将所有 n 的切片动能界、h 导数界的零测例外也去掉。

固定这样的 t，先沿 Fatou 的有限下极限取梯度 L2 有界的子列，再由 h_n 的空间 C2 界取子列，使
\[
 h_n(t)\to H_t\text{ 于 }C^1(\overline{B_R}),\qquad
 u_n(t)\to U_t:=v(t)+H_t\text{ 强 }L^2(B_R).
 \tag{PF.8}
\]
\(H_t\) 调和、无散，\(\|H_t\|_{C^1}\le C(M)\)；并且 \(\int|U_t|^2\le M\)。梯度子列弱极限为 \(\nabla U_t\)。这个子列允许依赖 t，不断言 \(H_t=h(t)\)。

SC §3 的空间论证现在适用于 \(U_t\)，而不是 v 或时间弱极限 u。具体取 \(m_n(t)\to C\)。若 C=0，\(d_n^2=|\Theta_n|^2|\nabla u_n|\) 给 \(d_n\to0\) 于 L2；二阶子式的散度形式传极限，得到 \(\operatorname{rank}\nabla U_t\le1\)。若 C≠0，用 \(B_n=\Theta_n/|\Theta_n|\)、\(|\nabla u_n|=|\Theta_n|^2/d(B_n)^2\)；若极限方向的 d 为零，将违背切片 L2 界。故反演连续，\(\nabla U_t\) 是常矩阵。这保留了空间仿射分支，没有假设梯度强收敛。

于是几乎每个 t，有 \(\operatorname{tr}((\nabla U_t)^2)=\beta_t\) 空间恒定。在秩一分支，迹零给 \(\beta_t=0\)；在仿射分支，球上的恒等式
\[
 \int_{B_R}|Lx+c|^2=|B_R||c|^2+|B_R|R^2|L|^2/5
 \tag{PF.9}
\]
给 \(|\beta_t|\le5M/(|B_R|R^2)\)。这个界不使用 Fatou 所选切片梯度界的大小。

写 \(V=\nabla v(t)\)、\(Z_t=\nabla H_t\)。从 \(\operatorname{tr}(V+Z_t)^2=\beta_t\)，得到
\[
 |\operatorname{tr}(V^2)|
 \le |\beta_t|+2|V||Z_t|+|Z_t|^2
 \le C(M)(1+|V|).
 \tag{PF.10}
\]
左边以及最后的右边都是 v 的可测函数，常数独立于切片选择。对几乎每个 t，其违反集合的空间测度为零；Fubini 因而给 PF.10 时空几乎处处成立。无需可测地选择 \(H_t\)、\(\beta_t\) 或分支标签。特别地，
\[
 \operatorname{tr}((\nabla v)^2)\in L^2(B_R\times J).
 \tag{PF.11}
\]
这不是 \(\nabla v\in L^4\)，也没有证明原速度时间弱极限的梯度仍秩一／仿射。

## 4. 修正压力的源属于 L2

对极限 PF.4 取散度，使用 \(\operatorname{div}f=0\)，得到
\[
 -\Delta q=b:=\operatorname{tr}((\nabla v)^2)
              +2\operatorname{tr}(\nabla v\nabla h)\in L^2(B_R\times J).
 \tag{PF.12}
\]
H1 速度的二次散度恒等式可由空间强 H1 光滑化验证；交叉项只需 h 的有界空间导数。PF.11 是这里新增的控制，不是一般能量解自动具有的 L2 压力源界。

固定 \(\chi\in C_c^\infty(B_R)\)，在 \(B_{1/3}\) 为一，令 \(q_0=(-\Delta)^{-1}(\chi b)\)。局部 Newton 势与 Calderon–Zygmund 界给 \(q_0\in L^2(J;H^2(B_R))\)，尤其 \(\nabla q_0\in L^2\)。这是局部 q_0 界，不声称非零均值源的全空间 Newton 势本身属于 L2。于是 \(q_h=q-q_0\) 在 \(B_{1/3}\times J\) 调和，且属于 L5/3。

取 \(I=(-1/4,0)\)，令
\[
 k(x,t)=\int_{-1/4}^t\nabla q_h(x,s)\,ds,\qquad w=v+k.
 \tag{PF.13}
\]
调和内估计与时间 Holder 给 k 及全部空间导数在 \(B_{1/4}\times I\) 有界，\(\operatorname{div}k=\Delta k=0\)。不要求 q_h 时间 L∞，不对 h 作时间微分。精确方程为
\[
 w_t-\Delta w+w\cdot\nabla w=\mathcal F,\qquad\operatorname{div}w=0,
 \tag{PF.14}
\]
\[
 \mathcal F=f-\nabla q_0+k\cdot\nabla w+v\cdot\nabla k
                  -v\cdot\nabla h-h\cdot\nabla v\in L^2.
 \tag{PF.15}
\]
每项均有明确来源和控制；没有把修正速度说成无外力 NS 解。

## 5. 提高极限可积性，再向原解传回速度小量

PF.14 是 RS §4 已写明的小幂截断所需的压力消除方程：w 属于能量类、无散，力属于 L2。在 \(Q_{1/4}\) 内开始，以固定幂 e=1/2 保留截止对流项、正扩散项和顶端切片；非线性去光滑化仍用 \( (1+e)/(10/3)+1/2=19/20<1\)。力项用 L2 Cauchy。三个固定内柱 \(Q_{5/24},Q_{1/6},Q_{1/8}\) 给
\[
 10/3\longrightarrow15/4\longrightarrow9/2\longrightarrow21/4.
 \tag{PF.16}
\]
三个弱端点为 35/9、55/12、65/12，所取强指数均严格小于端点。对任意顶时 \(\tau<0\) 先去正则化，再以同一父柱范数取 \(\tau\uparrow0\)；没有要求极限在未来延拓。k 有界，所以
\[
 v\in L^{21/4}(Q_{1/8}),\qquad C_v(r):=r^{-2}\int_{Q_r}|v|^3\le K_v r^{1/7}\to0.
 \tag{PF.17}
\]

最后无需传回原压力。对每个先固定的 \(0<r<1/8\)，由强 L3 的 v_n 及 h_n 的一致有界性，
\[
 \limsup_n r^{-2}\int_{Q_r}|u_n|^3
 \le4C_v(r)+C(M)r^3\longrightarrow0\quad(r\downarrow0).
 \tag{PF.18}
\]
顺序是先固定 r，再令 n 充分大；没有把 h_n 的时间振荡设为零。Kwon Theorem 1.4 取时间与空间指数均为3，满足 \(2/3+3/3<2\)。具体把 Q_r 缩放到文献的 Q_2，令 \(\widetilde u(y,s)=(r/2)u_n((r/2)y,(r/2)^2s)\)，则
\[
 \|\widetilde u\|_{L^3(Q_2)}^3=4r^{-2}\int_{Q_r}|u_n|^3.
 \tag{PF.19}
\]
选择固定 r 使 PF.18 的右边足够小，再取 n，使 PF.19 低于该文献阈值的三次方，原 u_n 的中心正则。文献的有界常数允许依赖各自有限的切片动能，不要求所有 n 的原压力有界。这与反设矛盾，PF-A 得证。

## 6. 改进的确切范围

在原先 SC／WE 的判据中，统一的 \(\mathsf A+\mathsf E+\mathsf D\) 上界，现在可换为 \(\mathsf A+\mathsf E\)。小形状耗散、适当解、闭柱邻域及单位黏性等条件仍保持。对光滑前终端解，SC.9 的 \(\mathsf K(1)\le(2+1/\sqrt2)^2\int_{Q_1}\Gamma\) 也直接给同样不依赖共同压力上界的充分条件；不改写一般弱解的经典 Gamma 定义。

仍开放的是：对任意原初值、任意候选有限首次奇时和指定中心，从同一实际 NS 方程产生一个合法尺度，使 A+E 有有限上界 M 且 \(\mathsf K<\varepsilon_{\rm PF}(M)\)。不能以 M 随尺度变化而阈值未知的事实宣称已经满足。有限总耗散与每个坏尺度的线性 r 成本仍相容；PF 没有给严格跨尺度收缩、不可求和成本或全局延拓。

下一项应回到这个联合好尺度问题，而不继续以删除另一条假设作为默认产出。先在光滑前终端的同一真实解上固定 \(\mu_G\) 熵恒等式与局部能量恒等式，比较同心两尺度、完整压力和输运余项；适当弱解版本的局部能量须保留不等式或缺陷测度。只有一个可证明的严格尺度增益或独立不可求和成本才可推进一般正则性；若仍只有同尺度 \(C(M)\) 界，就应记录缺口并重新选择具体动力学输入，不重命名权重。

## 7. 阅读和审查范围

本地依赖为 SC 全文的切片分类、RS 全文的子式及小幂截断、WE 全文的弱导数存在；历史稿不回改。主任务实际读取 Kwon v3 的导言相关定义、§2 完整分解证明、§3 正则性证明及§4 Theorem 1.4 证明；未声称审查该文所有参考文献或§5–6。原文含个别指标与公式排字问题，本文只使用标明的接口和自己的 PF.6–19 推导。Wolf 原文用于区分两种投影，不是本证明额外依赖。

两位 AI 协作者参与检查修正紧性、逐片选择与力项；具体文件版本和审读范围由配套审计绑定，不冒充完全非作者或真人审稿。本轮没有 Deep Research 全面综述、充分新颖性检索、仿真、DGX、数值证书或科学附图。内部 VR 核算随包保留，不作为另一项完成成果计数；不制作网页、读者 PDF、公开摘要或阶段 recap。冻结后仅一次交固定发布任务作 PRIVATE_ARCHIVE。
