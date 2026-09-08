# 三项动力学候选：尺度成本仍未改善

2026-09-08。DBS，PRIVATE_CORE。内部候选核算，不是独立成果小节或发布冻结。上一轮 JC 完成了联合源检查，但没有新的无条件临界估计。本轮回到同一原 NS 演化，检查终端局部动能、频带幅度变差及物质流占据成本。前两项与已有记录重合或属于经典估计的细化；第三项没有移除尺度化母柱成本。一般三维 NS / Clay 仍 OPEN / NOT CLAY。

本轮没有选定可接受的新闭合机制。这不是证明所有相关路线不可能，也不是把完成一次核算当作解决了一个新的正则性问题。

## 1. 本轮的原问题没有变小

固定正黏性、无外力、光滑周期原 NS 解，在 \([0,T_*)\) 光滑，\(T_*<\infty\)，记 \(G_{ij}=\partial_j u_i\)。候选终点尚未被证明奇异或正则。保留任意光滑无散初值和同一条解，不以改变初值的短时解族替代其成熟历史。

[PF](clay_b_pressure_free_shape_criterion_20260908.md) 的条件出口仍须在指定中心、同一尺度上同时得到
\[
 \mathsf A(r)+\mathsf E(r)\le M,\qquad
 \mathsf K(r)<\varepsilon_{\rm PF}(M).
 \tag{DBS.1}
\]
其中 \(\mathsf K=r^{-1}\int_{Q_r}|\nabla\Theta(G)|^2\)。DBS.1 按 PF 的单位黏性规范理解；下述恒等式显示一般固定 \(\nu>0\)，不声称 PF 的同一阈值与黏性无关。固定解依赖的有限总耗散、强梯度 L1 终端迹以及尺度趋零，均不能直接代替 DBS.1。直接排除首次奇点也可以绕过 PF；但不能只改写一个尚未支付的临界假设。

## 2. TG 不会消去终端二次能量缺陷

[BM §2](clay_b_euler_rigidity_energy_atom_20260906.md) 已从固定截止局部能量等式得到整个时间极限
\[
 |u(t)|^2dx\rightharpoonup^*\mu_*\quad(t\uparrow T_*).
\]
[TG](clay_b_strong_gradient_terminal_trace_20260908.md) 现在给 \(u(t)\to u_*\) 强 W1,1，特别是强 L1。结合统一 L2 上界，先对有界测试函数使用强 L1，再以 L2 稠密逼近，得到整个时间极限的弱 L2 收敛。对每个非负光滑 \(\phi\)，加权弱下半连续性仅给
\[
 \int\phi|u_*|^2\le\int\phi\,d\mu_*,
 \qquad \mu_*=|u_*|^2dx+\lambda_*,\quad \lambda_*\ge0.
 \tag{DBS.2}
\]
没有反向不等式可令 \(\lambda_*=0\)。线性增长梯度密度的强迹，不是速度平方的强迹。若 \(\mu_*\) 有点原子，该原子完整留在 \(\lambda_*\) 中。

取固定 \(0<s<T_*\)、\(0<r<\pi/4\)，标准 \(\chi_r=1\) 于 \(B_r(x_0)\)、支于 \(B_{2r}(x_0)\)。完整终端恒等式为
\[
 \begin{aligned}
 \frac12\int\chi_r|u_*|^2+\frac12\int\chi_r\,d\lambda_*
 +\nu\int_s^{T_*}\!\!\int\chi_r|G|^2
 ={}&\frac12\int\chi_r|u(s)|^2\\
 &+\frac{\nu}{2}\int_s^{T_*}\!\!\int |u|^2\Delta\chi_r
 +\int_s^{T_*}\!\!\int(\tfrac12|u|^2+p)u\cdot\nabla\chi_r .
 \end{aligned}
 \tag{DBS.3}
\]
各项先在光滑区间成立，再用 BM 的可积性取终端极限。压力的时间常数可以由无散性消去，近压和远压不能删除。除以 \(r\) 后，环层绝对成本为
\[
 C\nu r^{-3}\int_s^{T_*}\!\!\int_{B_{2r}\setminus B_r}|u|^2
 +Cr^{-2}\int_s^{T_*}\!\!\int_{B_{2r}\setminus B_r}
 (|u|^3+|p-c(t)||u|).
 \tag{DBS.4}
\]
这里 \(c(t)\) 选择使所写乘积可积，例如规范零均值压力下取零。初端项仍保留。TG 没有给出这些量的临界衰减率。

在额外正原子假设下，[BO.6、14、16](clay_b_energy_atom_dissipation_20260906.md) 已构造最后阈值窗并证明（该稿 \(\nu=1\)）
\[
 D_r\ge cm\delta_r/r^2,\quad
 \delta_rD_r^3\ge cm^4E^{-3}r^4,\quad
 D_r\ge cm^{5/4}E^{-3/4}r^{1/2}.
 \tag{DBS.5}
\]
其保证的 dyadic 下界可求和；实际尾窗嵌套，不能相加或相减下界来制造不相交的成本。这条候选停止于已有 BO 边界，不新增原子定理。任意奇点必产生原子的箭头也没有证明。

## 3. 频带幅度的线性变差：细化成立，半阶权重仍在

[FA.3](clay_b_frequency_activation_20260907.md) 已给空频带激活的能量级时间尺度；[FCB §1–3](clay_b_frequency_cascade_budget_20260907.md) 已给加权三次、二次正变差。这里仅核算同一解上的线性幅度版本，不将它称为新的动力学机制。

令 \(\bar u\) 为守恒空间均值，\(w=u-\bar u\)。取实偶径向单调 \(\chi\in C_c^\infty(\mathbb R^3)\)，在 \(|\xi|\le1\) 为1、在 \(|\xi|\ge2\) 为0。令 \(\widehat P_0(k)=\chi(k)\mathbf1_{k\ne0}\)，且 \(j\ge1\) 时 \(\widehat P_j(k)=\chi(2^{-j}k)-\chi(2^{1-j}k)\)。这给光滑、有限重叠的周期非零频率恒等分解，不要求幂等。记 \(w_j=P_jw\)、\(\lambda_j=2^j\)；常模态不参与。设
\[
 a_j=\|w_j\|_2,\qquad b_j=\lambda_j a_j.
\]
非零模上 \(\sum b_j^2\le C\|G\|_2^2\)。这里仅用于全周期频带幅度的计算，没有移动 PF 的指定物理中心。常漂移 \(\bar u\cdot\nabla w_j\) 在带能量配对中为零。

写 \(R_j=P_j\mathbb P\operatorname{div}(w\otimes w)\)。直接周期分块估计给
\[
 \sum_{j\ge0}\lambda_j^{-1/2}\|R_j\|_2
 \le C\|G\|_2^2.
 \tag{DBS.6}
\]
完整证明如下。固定充分大的整数 \(L\ge4\)，低高项 \(q\le p-L\) 的输出满足 \(|j-p|\le C_0\)。Bernstein 及频带上完整 Leray 乘子给
\[
 \lambda_j^{-1/2}
 \|P_j\mathbb P\operatorname{div}(w_q\otimes w_p)\|_2
 \le C2^{-(j-q)/2}b_qb_p .
\]
交换两输入顺序亦同。几何核可和，离散 Cauchy–Schwarz/Young 给这部分总和不超过 \(C\sum b_j^2\)。邻近高高项 \(|p-q|\le L\) 允许全部低输出 \(j\le p+C_0\)。用输出核的 \(L^1\to L^2\) 范数 \(C\lambda_j^{5/2}\)，得到
\[
 \lambda_j^{-1/2}
 \|P_j\mathbb P\operatorname{div}(w_p\otimes w_q)\|_2
 \le C2^{-2(p-j)}b_pb_q.
\]
先求所有允许的 j，再求有限邻壳 p、q，仍不超过 \(C\sum b_j^2\)。最低有限频率的常数统一吸收。先对有限分解计算；在每个闭前终端光滑区间取极限，再用非负求和得到 DBS.6。没有把原压力删掉，也没有假设只从相邻低频供能。

真实带能量等式为
\[
 (a_j^2/2)'+\nu\|\nabla w_j\|_2^2
 =-\langle R_j,w_j\rangle.
\]
在 \(a_j>0\) 处有 \((a_j')_+\le\|R_j\|_2\)；非负局部绝对连续函数在其零集上导数几乎处处为零，故无须除以零。对任意固定 \(0<a<T_*\)，得到
\[
 \sum_j\lambda_j^{-1/2}V_+(a_j;[a,T_*))
 \le C\int_a^{T_*}\|G(t)\|_2^2dt.
 \tag{DBS.7}
\]
再用 \(V_-\le V_++a_j(a)\)，
\[
 \sum_j\lambda_j^{-1/2}{\rm TV}(a_j;[a,T_*))
 \le 2C\int_a^{T_*}\|G\|_2^2+C\|w(a)\|_2.
 \tag{DBS.8}
\]
末项由 \(\sum\lambda_j^{-1}<\infty\) 与频带 L2 平方和控制。它是幅度的变差，不是向量解的强空间范数时间 BV。

固定幅度每尺度各上穿一次的保证成本仍是 \(\lambda_j^{-1/2}\)，可以求和；NS 临界振幅 \(a_j\asymp\lambda_j^{-1/2}\) 的对应成本更是 \(\lambda_j^{-1}\)。这只是所得必要预算仍相容，不是实现该级联的 NS 解。不能据此得到不可求和耗散或正则性。该细化保留作内部计算，不新增科学成果编号。

## 4. 物质坐标消去显式对流，但不消去费用

取 \(0<a=b-r^2<b<T_*\)、\(4r<\pi\)，\(I=(a,b)\)。令反向标记的经典物质流满足
\[
 \partial_sX(s;b,y)=u(X(s;b,y),s),\qquad X(b;b,y)=y.
\]
记 \(F=D_yX\)、\(C=F^{-1}F^{-T}\)、\(v=u\circ X\)、\(\widetilde p=p\circ X\)。无散性给 \(\det F=1\)，且 \(\partial_sF=(G\circ X)F\)。所有流和恒等式先止于 \(b<T_*\)，不预设流在奇异终点仍光滑。

空间 Piola 换元给
\[
 \partial_sv-\nu\operatorname{div}_y(C\nabla_yv)
       +F^{-T}\nabla_y\widetilde p=0,\qquad
 \operatorname{div}_y(F^{-1}v)=0.
 \tag{DBS.9}
\]
扩散逐速度分量作用：第 i 分量为 \(\sum_{\alpha,\beta}\partial_{y_\alpha}(C_{\alpha\beta}\partial_{y_\beta}v_i)\)。对任意固定光滑非负周期标签截止 \(\eta\)，积分得
\[
 \begin{aligned}
 \left[\frac12\int\eta|v|^2\right]_a^b
 +\nu\int_a^b\!\!\int\eta|G\circ X|^2
 ={}&-\nu\int_a^b\!\!\int\nabla\eta\cdot C\nabla_y\frac{|v|^2}{2}\\
 &+\int_a^b\!\!\int\widetilde p\,F^{-1}v\cdot\nabla\eta .
 \end{aligned}
 \tag{DBS.10}
\]
因为 \(\nabla_yv=(G\circ X)F\)，正扩散恰为原 \(|G|^2\)。压力分部积分使用 DBS.9 的无散性。没有 \(\partial_s\eta\) 项，但原初端物质包、变形扩散和压力边界功全部仍在。

## 5. 平均占据成本仍带原临界尺度

对终端标签 \(y\in B_r(x_0)\)，沿反向流首次到达 \(\partial B_{2r}(x_0)\) 时停止；没有退出则一直走到 a。记停止时刻为 \(\tau_y\)，以及
\[
 H(y)=\int_{\tau_y}^b|G(X(s;b,y),s)|\,ds.
\]
停止前轨迹均在母球中。退出轨迹的路程至少 r，而 \(b-\tau_y\le r^2\)。Cauchy–Schwarz、体积保持及停止指标不超过一，分别给
\[
 \begin{aligned}
 |\{\text{退出}\}|&\le
       \int_a^b\!\!\int_{B_{2r}}|u|^2,\\
 \int_{B_r}H(y)^2dy&\le r^2
       \int_a^b\!\!\int_{B_{2r}}|G|^2 .
 \end{aligned}
 \tag{DBS.11}
\]
第一式具体由 \(r^2\le r^2\int_{\tau_y}^b|u(X,s)|^2ds\) 对退出标签积分。第二式对所有标签同样应用时间 Cauchy。故对 \(L>0\)，坏标签相对体积满足
\[
 \frac{|\{\text{退出}\}\cup\{H>L\}|}{|B_r|}
 \le C\left[\mathsf A(2r)+\frac{\mathsf E(2r)}{L^2}\right],
 \tag{DBS.12}
\]
其中母柱按 \(B_{2r}\times(b-4r^2,b)\) 定义，并假设其底端为正；I 是它的子窗。若只使用 I 定义母量，同一证明也成立。没有把实际速度均值当成零。

在未退出且 \(H\le L\) 的轨迹上，矩阵 ODE 给
\[
 \|F^{\pm1}(s)\|_{\rm op}\le e^L,\qquad
 e^{-2L}I\le C(s)\le e^{2L}I\quad(a\le s\le b).
 \tag{DBS.13}
\]
这没有在整个标签域给统一椭圆性。放大 L 可以降低梯度坏集的上界，却提高变形系数成本；退出项还含 A。即使已有共同母帽，坏集估计也不能直接给指定标签或指定中心的控制。把 DBS.10 限制在这个一般仅可测的好标签集合，还需要合法光滑截止及其导数成本，不能直接乘指示函数丢掉边界项。

因此普通物质换元和有限占据积分没有自动得到 DBS.1；既没有共同母帽，也没有形状耗散小量。停止的是当前这次闭合尝试，不是对一切物质流方法的否定。

## 6. 本轮判断与来源范围

终端局部动能候选停在 BM/BO 已有边界；频带线性变差属于经典分块乘积的细化，保留可和半阶权重；物质流候选保留尺度化占据与压力边界成本。本轮没有接受新的无条件临界输入，没有选定下一项具体替代机制，不通过换名称或增加完成计数掩盖这个事实。

下一轮应针对一个尚未核算、可能减少上述明确缺项的原 NS 演化机制提出可反驳的目标式，再作实际推导；不能重开本轮三项的相邻条件版本、初端解族或相同文献摘要。探索不要求预先证明目标，但接受为输入必须有完整证明。完整 Clay 目标保持 active。

主任务实际全文读 PF、PFA、TG、TF、BM、BO、两份策略记录；FA 读取前200行，FCB 读取前230行，其中本轮使用的是 §1–3。没有重新认证这些稿件的全部外部依赖。三位协作者参与各自模块核算；实际最终文件审读另由检查点记录，不冒充真人同行评审或新颖性认证。

另作四条普通定向网页查询。检索返回的 2608.04138 与 1705.04420 已在本地原子路线登记，不重新计作新来源。[Núñez 的 2003 年论文出版社预览](https://doi.org/10.1016/S0167-2789(02)00770-4)以给定时刻涡量平方积分及局部解析性控制间歇突发；本轮只读预览，不采用其未读完整证明作为新预算。不宣称全面文献综述或 Deep Research。

本轮仅内部记录，无新独立小节、release、发布移交、公开摘要、累计 recap、仿真、DGX 或科学附图。TG 的既有冻结与一次交接保持不变。
