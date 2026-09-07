# 螺旋度结构：全局消去与局部生成

2026-09-07。PRIVATE_CORE。LITERATURE / PROVED LOCAL CHECK / OPEN / NOT CLAY。

本节没有得到新的无条件正则性估计。已有的总螺旋度恒等式只固定两个临界累计量之差；下面的完整 NS 局部解进一步说明，初始处处零螺旋度也不一定保持。原著核验还发现 Tao 平均化论文 Remark 4.3 的字面公式有局部代数不一致。我给出一个满足所需双消去和奇偶性质的修正式，但没有重新认证整篇平均化爆破证明，也不把这个修正称为新颖性成果。

## 1. 已知的全局恒等式没有提供新的上界

在零均值环面上记 \(D=\sqrt{-\Delta}\)、\(u_\pm\) 为正负 curl 谱投影。已有 `clay_b_helical_sector_dynamics_20260907.md` 的 HS.3–4 给出
\[
C_\pm(t)=\tfrac12\|D^{1/2}u_\pm(t)\|_2^2
 +\nu\int_0^t\|D^{3/2}u_\pm(s)\|_2^2\,ds,
\qquad C_+(t)-C_-(t)=\tfrac12 H(0),
\tag{HL.1}
\]
其中 \(H(t)=\int u\cdot\operatorname{curl}u\)。两个非负累计量的共同导数没有已知符号，固定差不控制和。若额外控制 \(C_++C_-\)，HS.4 已给出光滑延拓；这里没有证明这个额外控制。也不能把黏性 NS 的 \(H(t)\) 一般地当成守恒量。

## 2. 局部恒等式

固定 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\)、任意固定 \(\nu>0\)，外力为零。以下只针对完整 NS 的局部光滑解，压力取零均值。令 \(\omega=\nabla\times u\)、\(h=u\cdot\omega\)，则
\[
\partial_t h+\nabla\cdot\left(uh+(p-|u|^2/2)\omega\right)
=\nu\Delta h-2\nu\sum_{i,j}\partial_i u_j\partial_i\omega_j.
\tag{HL.2}
\]
证明：写 \(u_t=u\times\omega-\nabla(p+|u|^2/2)+\nu\Delta u\) 和
\(\omega_t=\nabla\times(u\times\omega)+\nu\Delta\omega\)。用
\(u\cdot\nabla\times v=v\cdot\nabla\times u-\nabla\cdot(u\times v)\)、
\(u\times(u\times\omega)=uh-|u|^2\omega\) 及乘积 Laplacian 公式，得到 HL.2。

压力通量未消失，黏性右端也不是正定耗散。积分给
\(H'=-2\nu\int\omega\cdot\nabla\times\omega\)，并非一般的 \(H'=0\)。本节未建立弱解的局部螺旋度公式或对 \(|h|\) 的重整化估计。

## 3. 处处零初始螺旋度可以产生局部非零螺旋度

取一次固定初值
\[
a(x,y,z)=(\cos z\sin y,\ \cos z\sin x,\ 0).
\tag{HL.3}
\]
它实、光滑、无散、零均值，且
\[
\Delta a=-2a,\qquad
\omega_a=(\sin z\sin x,-\sin z\sin y,
             \cos z(\cos x-\cos y)),\qquad a\cdot\omega_a\equiv0.
\tag{HL.4}
\]
直接计算
\[
(a\cdot\nabla)a=(\cos^2z\sin x\cos y,\ \cos^2z\sin y\cos x,\ 0),
\quad -\Delta p_0=2\cos^2z\cos x\cos y,
\]
所以完整原方程的初始压力是
\[
p_0=(1/2+\cos(2z)/6)\cos x\cos y.
\tag{HL.5}
\]
取 \(x_*=(0,\pi/2,\pi/2)\)。在那里
\[
a=0,\quad \omega_a=(0,-1,0),\quad \nabla p_0=(0,-1/3,0),
\quad u_t(0,x_*)=-\nabla p_0(x_*)=(0,1/3,0).
\]
对流和黏性项在该点确为零，没有把它们从方程中删去。由于 \(a(x_*)=0\)，
\[
\partial_t h(0,x_*)=u_t(0,x_*)\cdot\omega_a(x_*)=-1/3,
\qquad h(t,x_*)=-t/3+O(t^2).
\tag{HL.6}
\]
对每个固定 \(\nu>0\)，充分小正时间上 \(h(t,x_*)<0\)。时间范围与余项常数可以依赖 \(\nu\)；这里没有黏性一致或终端奇点结论。

### 完整局部解的依据

HL.6 是同一个完整原解的 Taylor 展开，不是 Galerkin 轨道。这里可以直接使用标准周期光滑局部适定性。为明确与已有工具的衔接，也可用已接受固定提交 `90c44d1703486e3983d12b87ed54f22c8c677982` 的 `research/reverse/first-cycle/PROOF.md` 第3节的通用 Wiener 论证，而不是其特定初值或143余项常数。

简述必要参数：取 \(\|f\|_{\mathcal A}=\sum_k|f_k|\)。HL.3 有8个系数、每个长度为 \(1/4\)，故 \(\|a\|_{\mathcal A}=2\)。保留 \(\nu\) 的完整热 Duhamel 映射满足
\[
\|\mathcal H_\nu(f,g)\|_{C_t\mathcal A}
\le2\sqrt{T/\nu}\|f\|_{C_t\mathcal A}\|g\|_{C_t\mathcal A}.
\tag{HL.7}
\]
这是 \(\sup_{r\ge0}re^{-\nu\tau r^2}\le(\nu\tau)^{-1/2}\) 与无散卷积的结果。取 \(T\le\nu/1024\)，在半径4的球上映射入自身，差映射的 Lipschitz 常数至多 \(16\sqrt{T/\nu}\le1/2\)。所以存在唯一完整 mild 解。对每个加权 \(\mathcal A_m\)，tame 乘积界把高阶 Picard 范数控制为线性 Volterra 递推，核为常数乘 \((t-s)^{-1/2}\)；其迭代积分级数 \(\sum_{r\ge0}K_m^rt^{r/2}/\Gamma(1+r/2)\) 收敛。高一阶尾界与零阶收敛给 \(C_t\mathcal A_m\) 收敛，方程随后给各阶单侧时间导数。由此得到 HL.6 所需端点光滑性。没有把某个零阶误差常数提升为高阶常数。

### 同时保持零总螺旋度

令 \(R=\operatorname{diag}(1,1,-1)\)。HL.3 满足 \(a(Rx)=Ra(x)\)。完整 NS 对正交变换协变，\(R u(t,Rx)\) 与 \(u(t,x)\) 有相同初值，因此唯一性给出
\[
u(t,Rx)=Ru(t,x),\qquad
\omega(t,Rx)=\det(R)R\omega(t,x)=-R\omega(t,x).
\]
于是 \(h(t,Rx)=-h(t,x)\)，其全域积分 \(H(t)=0\) 在光滑存在区间内保持，而 HL.6 的局部产生仍成立。这里的总量为零来自这个特定反射对称性，不能推广为“所有 \(H(0)=0\) 初值都保持零总量”。

HL.3–6 只否定点态零螺旋度的普遍不变性。它不同于已有 HS.5–8 的纯正 curl **谱扇区**泄漏。没有证明这个初值爆破，也没有否定特殊零螺旋度类的全局光滑性。

## 4. Tao Remark 4.3 的原文范围

来源：[Tao, arXiv:1402.0290v3](https://arxiv.org/html/1402.0290v3)，2015-04-01。Remark 4.3 已明确讨论在平均化模型中同时加入能量与螺旋度非线性消去。本项目此前的平均化文献记录未覆盖这一段，因此不能把“再加总螺旋度恒等式”当成未被该文考虑的新输入。

本轮读 Definition 3.1、Theorems 3.2–3.3 的陈述及 Remark 4.3 全段；其 arXiv v3 PDF 的印刷第34–35页另经完整渲染查看。本轮没有逐字核验正式 JAMS PDF，也没有完成期刊勘误登记审计；AMS 搜索索引只确认正式版含 Remark 4.3 开头。下面审查一个 elementary 项的字面式及修正，不声称重证 Theorems 3.2–3.3 的长证明、其全部外部依赖或原 NS 爆破。

## 5. 字面六项式的两个问题

这里改用 \(\mathbb R^3\) 上的实 \(L^2\) 配对，**不是**把平均化模型移植到环面。固定 \(0<\epsilon_0<1/2\) 和一个尺度，令 \(a,b,c\) 为实、奇、无散 Schwartz 场，Fourier 支持均位于 Definition 3.1 允许的窄环带 \(\{\xi:1-2\epsilon_0\le|\xi|\le1+2\epsilon_0\}\)。记
\[
J=\operatorname{curl},\quad K=J^{-1}=(-\Delta)^{-1}J,
\quad (\alpha,\beta,\gamma)=(\langle u,a\rangle,\langle u,b\rangle,\langle u,c\rangle),
\quad (\ell,m,n)=(\langle u,Ja\rangle,\langle u,Jb\rangle,\langle u,Jc\rangle),
\quad k=\langle u,Kb\rangle.
\]
在无散场上 \(J^2=-\Delta\)，且 \(J,K\) 自伴。arXiv v3 PDF 与 arXiv 实验 HTML 都把逆算子写成 \(\Delta^{-1}J\)；按该文的标准 Laplacian/Leray 约定，这个算子实际上是 \(-K\)，不是 \(K\)。

即使先修正这个符号，原六项式在对角输入上仍为
\[
F_{\rm print}=\alpha\beta c-\alpha\gamma b
 -\alpha n Kb+kn a-k\ell c+\gamma\ell Kb.
\tag{HL.8}
\]
直接配对得到
\[
\langle F_{\rm print},u\rangle=0,\qquad
\langle F_{\rm print},Ju\rangle=\gamma(\beta\ell-\alpha m).
\tag{HL.9}
\]
最后一式一般非零，外层双线性对称化在 \(u=v\) 时不会修复它。若完全照原文使用 \(K_{\rm print}=\Delta^{-1}J=-K\)，重新记 \(k=\langle u,K_{\rm print}b\rangle\)，curl 配对则为 \(2\alpha\beta n-\alpha\gamma m-\gamma\beta\ell\)，也不恒零。

残差不是只在形式独立变量上出现：在同一环带选三个互不相交、关于原点对称的 Fourier 支撑对，分别构造非零的实奇无散 \(a,b,c\)。例如在各自的一对小球上，令 \(\widehat a(\xi)=i\phi_a(\xi)P_\xi v_a\)，其中 \(\phi_a\) 为实奇光滑紧支撑函数、\(v_a\) 为不与该球中心平行的实向量；另两项同理。共轭对称性、无散性与 Schwartz 性都成立。取 \(u=b+c+Ja\)，则
\[
\alpha=0,\quad \beta=\|b\|_2^2>0,\quad \gamma=\|c\|_2^2>0,
\quad \ell=\|Ja\|_2^2>0,\quad m=n=0.
\]
这同时使真逆读法的 HL.9 为正、字面负逆读法的残差为负。奇偶正交和互不相交的 Fourier 支撑保证所有所用零项。这证明的是原 Remark 中该 elementary 公式声称的普遍消去不成立，不是整篇定理为假。

## 6. 一个局部可行的修正式

仍用真正的 \(K=J^{-1}\)，记 \(q=\langle u,Ka\rangle\)。保留 HL.8 的前两项，把后四项改为
\[
F_{\rm corr}=\alpha\beta c-\alpha\gamma b
 -\beta n Ka+qn b-qm c+\gamma m Ka.
\tag{HL.10}
\]
其 \(u\) 配对分成三对相消项；其 \(Ju\) 配对为
\[
\alpha\beta n-\alpha\gamma m-\beta n\alpha+qnm-qmn+\gamma m\alpha=0.
\tag{HL.11}
\]
更直接地，令 \(T(x,y,z)\) 是三行分别为
\((\langle x,b\rangle,\langle x,Ka\rangle,\langle x,c\rangle)\)、
\((\langle y,b\rangle,\langle y,Ka\rangle,\langle y,c\rangle)\)、
\((\langle z,b\rangle,\langle z,Ka\rangle,\langle z,c\rangle)\)
的行列式，则 \(\langle F_{\rm corr}(u),w\rangle=T(u,Ju,w)\)。取 \(w=u\) 或 \(w=Ju\) 立即得到两个消去。

这个二次映射由极化给对称双线性算子。若 \(u\) 为奇场，\(Ja,Jb,Jc,Ka\) 均为偶场，所以 \(q=m=n=0\)；修正后与原两项 \(\alpha\beta c-\alpha\gamma b\) 相同，且输出为奇场。

再令 \(\lambda=1+\epsilon_0\)、\(f_n(x)=\lambda^{3n/2}f(\lambda^n x)\)。有
\[
Jf_n=\lambda^n(Jf)_n,\qquad Kf_n=\lambda^{-n}(Kf)_n.
\tag{HL.12}
\]
HL.10 的每个修正项都含一个 \(J\) 与一个 \(K\)，额外缩放因子相消。\(Jf,Kf\) 仍为同一允许窄环带的无散 Schwartz 场，因而保留外部 \(\lambda^{5n/2}\) 权重后，所得尺度和仍是 Definition 3.1 的 local-cascade 型有限线性组合。具体地，对 \(u,v\in H^{10}_{\rm df}(\mathbb R^3)\)，每个高频配对 \(|\langle u,f_n\rangle|\le C_f\lambda^{-10n}\|u\|_{H^{10}}\)（\(n\ge0\)），低频则至多 \(\|u\|_2\|f\|_2\)。归一化后的每个输出项的 \(L^2\) 范数，分别受可求和的 \(\lambda^{(5/2-20)n}\)（\(n\ge0\)）与 \(\lambda^{5n/2}\)（\(n<0\)）控制。因此输出尺度和在 \(L^2\) 绝对收敛；取 \(u=v\)，与 \(u\) 或 \(Ju\in L^2\) 配对均可逐尺度求和。双消去不只成立于有限截断。常数可依赖固定 \(\epsilon_0\) 与基函数；此处不声称这些常数随 \(\epsilon_0\downarrow0\) 一致，也不单凭本段调用 Theorem 3.2 的平均表示结论。

热半群也保持奇场，所以“在奇轨道上保留原动力学”并不要求删去黏性。本段只核验修正式的双消去、奇偶、缩放和算子类别；若要重新证明修正模型具有整个爆破结论，仍须明确调用并核对原构造与表示定理的所有接口。本项目本轮没有做这个完整认证。不能从局部可修正推断原 NS 的一般正则性或奇性，也不能据局部字面错误否定原著主定理。

## 7. 本节改变和没有改变的判断

本节补充了原著中螺旋度增强的阅读范围，并留下一个可直接复核的原 NS 局部算例及平均算子的局部修正式。全局临界差恒等式和其占优条件早已在 HS、R0.72I 记录，不重新计为机制。定向本地去重没有找到 HL.3–6 的同一算例；这不构成穷尽查新，也不证明发表价值。

当前不能接受“全局双消去”或“初始处处零螺旋度保持”作为一般正则性的新增闭合步骤。HL.2 的压力与带符号黏性项尚未给出独立可控的正量。这里只排除这些具体论证，没有排除所有利用局部螺旋几何、方向或拓扑的未来论证。

下一项只有在找到具体的原方程时空结构、独立可控量和覆盖任意候选奇点的推导接口后才进入技术计算；不再重复总量恒等式、初始符号或谱偏离参数的换名。一般周期三维光滑延拓、规定中心好尺度合同 G 以及完整 Clay 目标仍 OPEN / NOT CLAY；本轮没有选定新的无条件候选。

本节为解析与定向原著核验，没有 PDE 仿真、DGX 工作、科学图或新的读者 PDF。AI 辅助推导及独立代理审查不等于真人同行评审或形式证明助手认证。完整资料只作私有冻结，不请求公开概要，也不生成阶段回顾。
