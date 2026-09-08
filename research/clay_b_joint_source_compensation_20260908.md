# 完整源的联合补偿：分数预算成立，临界时间缺口仍在

2026-09-08。JC，PRIVATE_CORE，INTERNAL CHECK / OPEN / NOT CLAY。本轮执行 AG.22 的具体测试。压力与惯性源整体处理后，能得到一个由基本能量支付的周期负阶 Besov 预算；但它与实际伴随的已付范数仍不能配成临界估计。投影转移、符号抵消和原子配对的边界也已核清。因此停止仅凭这些既有输入继续改写同一源配对，不另计独立小节或 release。

## 1. 投影后的测试并不满足齐次伴随

沿用 AG 的同一无外力光滑周期 NS，固定 \(\nu>0\)、\(0<a<b<T_*\)，压力逐时零均值。令
\[
 G_{ij}=\partial_j u_i,\quad H=\nabla^2p,\quad
 f=\operatorname{tr}(G^2),\quad
 N=G^2-Q^*f,\qquad Q^*=\nabla^2\Delta^{-1}.
\]
\(Q^*\) 的非零符号是 \(m(k)=k\otimes k/|k|^2\)，零模为0。
记 \(L_+=\partial_s+u\cdot\nabla+\nu\Delta\)，
取光滑实标量终端测试 \(\eta\)，令 \(h(s)=S(b,s)^*\eta\)、\(L_+h=0\)、\(M=\|\eta\|_\infty\)，仍使用同一实际漂移。空间积分均在未归一化的 \(2\pi\) 周期胞。

令 \(\mathbb P\) 为保留常数的 Leray 投影，固定分量 i,j，并设
\[
 v=e_i\partial_jh,\quad
 \theta=\Delta^{-1}\partial_{ij}h,\quad w=\mathbb Pv=v-\nabla\theta.
\]
则
\[
 L_+v=-e_i(\partial_ju_k)\partial_kh,\qquad
 L_+w=\mathbb PL_+v+[u\cdot\nabla,\mathbb P]v.
 \tag{JC.1}
\]
同一无散 u 与交换子配对，完整得到
\[
 \int u\cdot[u\cdot\nabla,\mathbb P]v
 =-\int u\otimes u:\nabla^2\theta
 =\int p\,\partial_{ij}h .
 \tag{JC.2}
\]
第一步用 \(\mathbb Pu=u\)、\(v-w=\nabla\theta\) 和周期分部积分；第二步用 \(-\Delta p=\partial_k\partial_\ell(u_ku_\ell)\) 及 \(\Delta\theta=\partial_{ij}h\)。所以
\[
 \iint_a^b N_{ij}h=\iint_a^b u\cdot L_+w
 =\left[\int u\cdot w\right]_a^b
 =\left[\int u_i\partial_jh\right]_a^b .
 \tag{JC.3}
\]
最后一步还用了原 NS 对偶以及 \(\operatorname{div}w=0\)。压力只是移入交换子，两个时间切片都在。这严格返回 AG.21，没有产生新的能量级端点控制。

## 2. 完整符号的角因子不是额外时间收益

对两个无散 Fourier 输入 \(v e^{i\xi\cdot x}\)、\(w e^{i\zeta\cdot x}\)，
\(\xi\cdot v=\zeta\cdot w=0\)。令 \(k=\xi+\zeta\)、
\(c=\zeta\cdot v=k\cdot v\)、\(d=\xi\cdot w=k\cdot w\)。
采用不含 \(1/2\) 的交叉项，完整源符号为
\[
 \mathcal N=-d\,v\otimes\zeta-c\,w\otimes\xi+2cd\,m(k).
 \tag{JC.4}
\]
当 k=0 时，c=d=0，源零模本身消失。令
\(R=\xi\times\zeta,\ W=v\times w,\ \beta=R\cdot W=-cd\)，
余子式的极化给
\[
 \mathcal N=-R\otimes W+\beta(I-2m(k)),\qquad
 |\mathcal N|_F^2=|R|^2|W|^2+|\beta|^2=|\mathcal A|_F^2 ,
 \tag{JC.5}
\]
其中 \(\mathcal A=-d\,v\otimes\zeta-c\,w\otimes\xi\) 是 \(G^2\) 交叉项。R 垂直 k；展开平方即得。复振幅以 Hermitian 范数解释，同样成立。

高高输入频率约为 K、输出 \(\kappa=|k|\ll K\) 时，
\(R=\xi\times k\)，所以有一个 \(K\kappa\) 因子，而压力项本身只有 \(O(\kappa^2|v||w|)\)。该一阶量级可以饱和：取
\(\xi=Ke_1,\ \zeta=-Ke_1+Le_2,\ v=e_2+e_3,\ w=(L/K)e_1+e_2\)，其中 \(L\ll K\)，则
\[
 \mathcal N=KL\,e_3\otimes e_1+
 L^2(-e_1\otimes e_1+e_2\otimes e_2-e_3\otimes e_2),
\]
压力交叉项为非零的 \(2L^2e_2\otimes e_2\)。因此一般三维没有第二个统一输出低频因子。低高 \(L\ll K\) 时，一般仍为 \(LK|v||w|\)；例如
\(\xi=Le_1,\zeta=Ke_2,v=e_2,w=e_1\) 给
\(|\mathcal N|=\sqrt2 LK\)，且压力非零。
这些仅检验符号阶数，不是新 NS 轨道或奇性反例。

这与旧 CD/PGR 的余子式结构相同。PGR.6 和 Plancherel 还直接给
\[
 \|G^2+H\|_2^2=\|G^2\|_2^2,\qquad
 \int G^2:H=-\tfrac12\|f\|_2^2,\quad \|H\|_2^2=\|f\|_2^2.
 \tag{JC.6}
\]
等式保留未知的二次源 L2 成本，不是其上界。它不排除实际传播中的时间抵消；频率角也没有自动成为所需时间加权小量。

## 3. 一个由能量支付的联合分数预算

这部分直接证明周期版本，不把全空间定理自动移植。取固定平滑非零频率分解 \(P_j\)，\(j\ge0\)，最低块包含 \(|k|\simeq1\)，非零频率上 \(\sum_jP_j=I\)。所有块支于固定比例环带并有统一 L1 卷积核界；用稍加宽块处理有限重叠。记 \(\Lambda=(-\Delta)^{1/2}\)，删除零模，并定义半范数
\[
 \|F\|_{\dot B^{-\alpha}_{1,1}}
 =\sum_{j\ge0}2^{-\alpha j}\|P_jF\|_1 .
\]
这里不是忽略一个未知均值：\(\int G^2=0\)，故 \(\int N=0\)。
对 \(0<\alpha<1\)，有
\[
 \boxed{\quad
 \|N(s)\|_{\dot B^{-\alpha}_{1,1}}
 \le C_\alpha\|\Lambda^{1-\alpha/2}u(s)\|_2^2
 \le C_\alpha U^\alpha g(s)^{2-\alpha},
 \quad}
 \tag{JC.7}
\]
其中 \(U=\sup_{a\le s\le b}\|u(s)-\bar u\|_2\)，
\(g(s)=\|\nabla u(s)\|_2\)。只在这个范数中减常均值；实际伴随及指定中心没有换漂移。常数依固定周期及分解，不依赖高阶解范数。

证明分为两类交互。写 \(u_j=P_ju\)、
\(a_j=2^{(1-\alpha/2)j}\|u_j\|_2\)。

低高或高低的输入 \(\ell<j-C\) 只有输出 \(k=j+O(1)\)。空间 Cauchy 和块核界给
\[
 2^{-\alpha k}\|P_k(G_\ell G_j)\|_1
 \le C\,2^{-\alpha(j-\ell)/2}a_\ell a_j.
 \tag{JC.8}
\]
几何核可和，离散卷积与 Cauchy 将总和控制为
\(C_\alpha\sum_j a_j^2\)。

高高必须包括 \(|j-\ell|\le C\) 的全部邻壳及其低输出。
对有序双线性项使用真实兼容性
\[
 \mathcal B(v,w)_{ab}
 =\partial_c v_a\,\partial_b w_c
 =\partial_c(v_a\partial_b w_c)\quad(\operatorname{div}w=0).
\]
因此 \(k\le j+C\) 时，
\[
 2^{-\alpha k}\|P_k\mathcal B(u_j,u_\ell)\|_1
 \le C\,2^{(1-\alpha)(k-j)}a_j a_\ell .
 \tag{JC.9}
\]
\(1-\alpha>0\) 允许向低频求和，再对有限邻壳求和即得同一界。这包含相反频率与共轭交互，不假设高高输出仍在高频。每个有序项的均值也是零。

压力在加宽输出环带上的 \(Q^*\) 有统一 L1 核界，所以
\(\sum_k2^{-\alpha k}\|P_kH\|_1\) 由刚才 \(G^2\) 的半范数控制。这是逐壳结论，不是一般 Riesz 变换的 L1 有界性。最后用 Fourier 插值得 JC.7。两项几何和给
\(C_\alpha\le C[\alpha^{-1}+(1-\alpha)^{-1}]\) 的可用上界，不声称最优，也不能把端点常数取作一致。

由能量 \(g\in L^2_s\)，因此
\[
 N\in L^{p_\alpha}((a,b);\dot B^{-\alpha}_{1,1}),\qquad
 p_\alpha=\frac2{2-\alpha},\qquad
 \|N\|_{L^{p_\alpha}_s\dot B^{-\alpha}_{1,1}}
 \le C_\alpha U^\alpha
       \left(\int_a^b g^2\right)^{(2-\alpha)/2}.
 \tag{JC.10}
\]
这是完整源的有效预算，既非单项压力假设，也不是任意 L1 源都有的结论。

但机制是经典的分数散度—旋度补偿。主任务定向读了 [Li–Zhang，Theorem 1.3及其证明](https://arxiv.org/html/2106.11852v1)：该文对全空间无散／无旋乘积给负阶 Hardy 估计，其高高块同样借一个输出导数求和。本节为当前周期源写出上述直接证明，不认领这类空间增益的新颖性，不采用该文未读的其他结论。

## 4. 配到实际伴随时仍缺时间指数

令 \(J=\nabla^2h\)。对非零块，最大值原理和 Bernstein 给
\[
 \|P_jh\|_\infty\le C\min\{M,2^{-j/2}\|J\|_2\}.
\]
取上确界并平衡两项，对 \(0<\alpha\le1/2\)，
\[
 [h]_{\dot B^\alpha_{\infty,\infty}}
 :=\sup_{j\ge0}2^{\alpha j}\|P_jh\|_\infty
 \le C M^{1-2\alpha}\|J\|_2^{2\alpha}.
 \tag{JC.11}
\]
必须使用非零块半范数；常数 h 会否定不含均值项的完整非齐次版本。N 均值为零使其常数测试精确消失。有限重叠的频率配对给
\[
 |\int N_{ij}h|
 \le C_\alpha U^\alpha g^{2-\alpha}
                   M^{1-2\alpha}\|J\|_2^{2\alpha}.
 \tag{JC.12}
\]
AG.4 给 J 的时间 L2，所以 JC.11 只支付
\([h]_{\dot B^\alpha_{\infty,\infty}}\in L^{1/\alpha}_s\)；
而 JC.10 的对偶时间指数是 \(2/\alpha\)。当前分项时间 Hölder 的倒数和为
\[
 \frac{2-\alpha}{2}+\alpha=1+\frac{\alpha}{2}>1.
 \tag{JC.13}
\]
所以更细的联合源范数仍未闭合这条配对链。令 \(\alpha\downarrow0\) 不能凭形式取限产生小量：常数不一致，且回到既有的有界 h 与 L1 源配对。它不证明实际乘积不积分，也不否定存在利用二者时间相关性的更强估计。

## 5. 不需 Lipschitz 时钟的原子版本也有同一个缺项

采用 SP.13 的明确前提：固定分量 i,j，先选定实际源的可测、绝对可和零均值分解
\(N_{ij}(s)=\sum_m\lambda_m(s)a_m(s)\)，小原子支于半径 \(\ell_m<\pi\) 的球，
\(\|a_m\|_1\le1\)。零均值给
\(|\widehat a(k)|\le C\min(1,\ell|k|)\)，在 \(|k|=\ell^{-1}\) 分频可得
\(\|a\|_{\dot H^{-2}}^2\le C\ell\)。结合球上 \(W^{1,4}\) Morrey，
\[
 |\langle a,h\rangle|
 \le\min\{M,C\ell^{1/2}\|J\|_2,
                 C\ell^{1/4}\|\nabla h\|_4\}.
\]
若分解只含这些小原子，记
\(A_\beta(s)=\sum_m|\lambda_m(s)|\ell_m(s)^\beta\)，则
\[
 |\langle(\mathcal D_{a,b})_{ij},\eta\rangle|
 \le C\min\{\|A_{1/2}\|_{L^2_s}\|J\|_{L^2_{s,x}},
             \|A_{1/4}\|_{L^{4/3}_s}\|\nabla h\|_{L^4_{s,x}}\}.
 \tag{JC.14}
\]
这里 \(\mathcal D_{a,b}=\int_a^bS(b,s)N(s)\,ds\)。大原子须另加普通幅值成本。AG 支付的是伴随因子，不是这两个长度矩的时间范数；Hardy 的 \(A_0\in L^1_s\) 控制不能替代它们。也没有构造满足所需新成本的最优分解。

局部讨论另取 \(4r<\pi\)、\(I_r=(b-r^2,b)\subset(0,T_*)\)，令 \(a=b-r^2\)。
采用标准光滑终端截函数 \(0\le\eta_r\le1\)，支于指定 \(B_r(x_0)\)，
\(\|\nabla\eta_r\|_2^2\le Cr\)，令 \(h_r(s)=S(b,s)^*\eta_r\)。
使用同一解上的缓冲母球 \(B_{4r}\)，并显式假设
\[
 \mathsf A_{4r}=(4r)^{-1}\sup_{s\in I_r}\int_{B_{4r}}|u(s)|^2,\qquad
 \mathsf E_{4r}=(4r)^{-1}\iint_{B_{4r}\times I_r}|G|^2,\qquad
 \mathsf A_{4r}+\mathsf E_{4r}\le C_0.
\]
这不是已证明的自动母柱上界。指定中心也不能因终端支集小而自动保留。
对所选支撑球位于 \(B_r(x_0)\) 内的原子，安全的本地 Hessian 因子是
\[
 \ell^{1/2}\bigl[
 \|\nabla^2h_r\|_{L^2(B_{2r})}+r^{-1}\|\nabla h_r\|_{L^2(B_{2r})}\bigr].
\]
这可对局部减均值后的 \(h_r\) 作截断延拓得到；第二项支付仿射部分，不能删除。
在上述完整假设下，AG.11（用半径2r）与标量 Caccioppoli 给方括号内量的时间 L2 为 \(O(r^{1/2})\)；保留截止项的局部插值相应给内球梯度时空 L4 为 \(O(r^{1/4})\)，常数可依 \(\nu,C_0\) 和固定截函数形状。要使这个指定截函数的响应配对除以 r 后趋零，还需例如
\[
 \|A_{1/2,\mathrm{in}}\|_{L^2(I_r)}=o(r^{1/2}),
 \quad\text{或}\quad
 \|A_{1/4,\mathrm{in}}\|_{L^{4/3}(I_r)}=o(r^{3/4}),
 \tag{JC.15}
\]
并保留球外原子的成本。旧 LT 的高度界可以支付外部项的上界，但没有在此证明它除以 r 后小。

原 \(\mu_G\) 包含零集测度，且通过带端点的原熵式控制特定的有符号归一化梯度—N 配对；它不等于上述源原子的长度分布。WE 的 \(\Theta\) 预算也没有在这里给出 JC.15 的比较不等式。没有删除它们，也没有证明这种比较永远不可能。

## 6. 一个拟议刚性入口在预检时被排除

为避免继续停留在同一源代数，我另做了一项有界预检：能否对所有光滑紧支无散
\(v:\mathbb R^3\to\mathbb R^3\) 有
\(\|v\|_6^2\le C\|\operatorname{cof}\nabla v\|_1\)？
这不是已经接受的定理。下面的长管构造直接否定它，因而不进入 NS 演化研究。

取固定 \(\psi\in C_c^\infty(\mathbb R^2_{y,z})\)，\(\psi_y\not\equiv0\)，
令 \(\chi_L(x)=1\) 于 \([0,L]\)，支于 \([-1,L+1]\)，两个端层宽度固定且
\(C^2\) 范数独立于 \(L\ge2\)。例如可由同一个光滑阶跃函数在两端相乘构造。设
\[
 v_L=\operatorname{curl}(0,0,\chi_L\psi)
       =(\chi_L\psi_y,-\chi_L'\psi,0).
\]
管身只有第一行梯度非零，故余子式为零；两个固定体积端层内梯度统一有界。于是
\[
 \|\operatorname{cof}\nabla v_L\|_1\le C,\qquad
 \|v_L\|_6^2\ge\left(L\int_{\mathbb R^2}|\psi_y|^6\right)^{1/3}.
 \tag{JC.16}
\]
这已经否定普适常数。并且 \(w_L(x)=v_L(Lx)\) 可平移支于同一个固定球，
两个范数同乘 \(L^{-1}\)，所以比值仍发散；同时
\[
 \|\nabla w_L\|_2^2=O(1),\qquad
 \|w_L\|_2^2=O(L^{-2}),\qquad
 \|w_L\|_6^2\asymp L^{-2/3},\quad
 \|\operatorname{cof}\nabla w_L\|_1\lesssim L^{-1}.
 \tag{JC.17}
\]
固定支撑和共同 H1 上限不能修复这个线性余子式界。两侧都趋零，故它不否定任何只断言零极限的紧性分类，也不否定含别的范数或不同幂次的估计。这是一个静态候选的否定，不是 NS 轨道或奇性结果，不另计研究小节。

## 7. 本轮决定与记录范围

JC.7–10 是本轮完成的范围内先验估计；它没有提高源—实际伴随配对的临界控制。投影对偶、余子式符号和原子方法都没有补上时间集中及同中心尺度的问题。因此停止把这些既有输入的相邻重写继续作为当前推进路线；不再以新记号、新条件范数或静态符号例子增加独立成果数。

下一入口仍服从 PF 的同一原解、固定正龄、指定中心问题。必须先选出能够处理时间集中或生成共同好尺度的具体动力学输入，再推导；目前尚未接受这样的新估计。第6节的线性余子式候选已经排除，不继续给它优化常数或做轨道仿真，也不把另一个未检验的不等式自动接替为已选方案。

主任务实读 AG 的源接口、IDC/MPS/CD 全文、旧压力文献记录及 R0.69N 前175行；定向读 Li–Zhang 的主张与上述分数 div-curl 证明，不认证整篇或全部上游引理。A 独立核完整符号及 CD/PGR 去重；B 独立核 Leray 对偶和周期分数求和；C 独立核原子、局部仿射成本与原耗散接口，并提出第6节长管反检，主任务独立复算其梯度、支集和缩放。最终文件审读与哈希另记检查点，全部为参与式 AI 核验。

仅保存内部记录和研究恢复指针；无仿真、DGX、图表、HTML/PDF、翻译、recap、新 release 或发布交接。TG 仍是最后独立完成小节，其冻结及一次交接不变；本任务未查询发布或反向执行。一般三维 NS / Clay 仍 OPEN / NOT CLAY。
