# 保留输运相消的 L²/H² 后验控制

2026-09-07。PRIVATE_CORE。独立推导者：`/root/driver_contract_review`，不是 `HYBRID_CONTROL_CONTRACT.md` 或 `ANALYTIC_PREFLIGHT.md` 的作者。本文直接推导合同中的常数、比较与延拓，不把根代理给出的候选式当作证明。

**解析合同通过。** 下述不等式及其终点接口成立，但尚无具体近似场、已认证控制函数或终点通过记录。因此尚未证明既定六模初值的原 NS 解全局光滑，也没有获得奇性证据。所有运算为解析/手算，不运行 PDE、控制 ODE 或格点数值扫描，不声称常数最优。

## 1. 固定对象和完整误差方程

物理对象仍是合同固定的
\[
a=2(\cos x_3,\cos x_1,\cos x_2),\qquad
\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3,\qquad \nu=1.
\]
为核清常数，推导暂写一般固定 \(\nu>0\)，最终用于同一 \(\nu=1\)；这不更换初值或方程。统一用归一化体积
\[
\|f\|_2^2=(2\pi)^{-3}\int_{\mathbb T^3}|f|^2
=\sum_k|f_k|^2.
\]
\(D^j f\) 包括所有有序导数指标和所有向量分量，使用全 Frobenius 长度。因此
\[
\|D^j f\|_2^2=\sum_k|k|^{2j}|f_k|^2.
\tag{Y.1}
\]

设以后给定的近似场 \(v\) 在整个预定 \([0,T]\) 上光滑、实值、无散、零均值，且周期。设
\[
B(f,g)=-\mathbb P[(f\cdot\nabla)g],\qquad
R=v_t-\nu\Delta v-B(v,v).
\]
以同一初值 \(a\) 的真实局部光滑 NS 解为 \(u\)，令 \(w=u-v\)。在真实解现有的光滑时段上精确有
\[
w_t-\nu\Delta w
=B(v,w)+B(w,v)+B(w,w)-R.
\tag{Y.2}
\]
两个有序混合项没有合成 \(2B(v,w)\)。\(R\) 也无散、零均值；误差保持实值、无散和零均值。空间微分与周期 Leray 交换。与 \(D^j w\) 配对时可用投影自伴性消去 \(\mathbb P\)，因为该测试场仍无散；这是完整方程中的精确配对，不是删除压力模型。

记
\[
x=\|w\|_2,\quad y=\|Dw\|_2,\quad
z=\|D^2w\|_2,\quad H=\|D^3w\|_2.
\]
后验输入应是独立已知、非负、连续且有限的函数，满足
\[
M_j(t)\ge\|D^jv(t)\|_{\infty,F}\ (j=1,2,3),
\qquad r_0(t)\ge\|R(t)\|_2,\quad
r_2(t)\ge\|D^2R(t)\|_2.
\tag{Y.3}
\]
以下使用上界也成立；不存在需要先知道真实解导数才能填写的系数。

## 2. 自包含 Fourier 常数

对零均值场，使用齐次绝对 Fourier 范数
\[
A_s(f)=\sum_{k\ne0}|k|^s|f_k|.
\]
最大坐标范数壳 \(\max_j|k_j|=n\) 恰有
\((2n+1)^3-(2n-1)^3=24n^2+2\) 个点，且其中 \(|k|\ge n\)。由递减函数积分比较，
\[
\sum_{n\ge1}n^{-2}<1+\frac14+\int_2^\infty t^{-2}dt=\frac74,
\quad
\sum_{n\ge1}n^{-4}<\frac43,
\quad
\sum_{n\ge1}n^{-6}<\frac65.
\]
所以
\[
\sum_{k\ne0}|k|^{-4}
\le24\sum n^{-2}+2\sum n^{-4}
<\frac{134}{3}<49,
\]
\[
\sum_{k\ne0}|k|^{-6}
\le24\sum n^{-4}+2\sum n^{-6}
<\frac{172}{5}<36.
\tag{Y.4}
\]
这里没有计算有限格点后猜测尾部。由完整无限和的 Cauchy–Schwarz 及 Y.1，
\[
A_1(w)\le7H,\qquad A_{-1}(w)\le6z,
\qquad A_0(w)\le7z.
\tag{Y.5}
\]
逐 Fourier 项的梯度张量长度为 \(|k||w_k|\)，故
\[
\|Dw\|_{\infty,F}\le A_1(w)\le7H.
\tag{Y.6}
\]
再由 \(\sum |k|^2|w_k|^2\) 的 Cauchy–Schwarz 得
\[
y^2\le xz,\qquad y\le\sqrt{xz}.
\tag{Y.7}
\]
上述常数与未归一化体积的 \(L^2\) 混用会发生变化；本文始终采用 Y.1。

## 3. L² 误差：完整无散输运相消

在 Y.2 中，\(\langle w,(v\cdot\nabla)w\rangle\) 和 \(\langle w,(w\cdot\nabla)w\rangle\) 均为零。余下混合项不消去，而有
\[
|\langle w,(w\cdot\nabla)v\rangle|\le M_1x^2.
\]
因此
\[
\frac12(x^2)'+\nu y^2\le M_1x^2+r_0x.
\tag{Y.8}
\]
在 \(x>0\) 处除以 \(x\)，丢掉非负耗散，得到
\[
x'\le M_1x+r_0.
\tag{Y.9}
\]

## 4. H² 误差：逐指标核对全部系数

写 \(w_{ij}=\partial_i\partial_jw\)，所有 \(i,j\) 均从 1 到 3 有序求和。对任意无散输运场 \(b\)，最高项
\[
\sum_{i,j}\langle w_{ij},(b\cdot\nabla)w_{ij}\rangle=0.
\]
取 \(b=v\) 或 \(w\) 均可。其余项必须保留。

对 \((v\cdot\nabla)w\)，乘积展开的三类余项是
\[
(\partial_iv\cdot\nabla)\partial_jw,
\quad(\partial_jv\cdot\nabla)\partial_iw,
\quad(\partial_{ij}v\cdot\nabla)w.
\]
前两类各不超过 \(M_1z^2\)，后一类不超过 \(M_2yz\)，合计
\[
2M_1z^2+M_2yz.
\tag{Y.10}
\]
例如第一类在每点是 \(Dv\) 与两份 \(D^2w\) 的完全缩并；算子范数不超过 Frobenius 范数，故上界为 \(|Dv|_F|D^2w|_F^2\)。这已对全部指标求和，不再附加分量个数。

对 \((w\cdot\nabla)v\)，四类项是
\[
(w\cdot\nabla)\partial_{ij}v,
\quad(\partial_iw\cdot\nabla)\partial_jv,
\quad(\partial_jw\cdot\nabla)\partial_iv,
\quad(\partial_{ij}w\cdot\nabla)v.
\]
分别与 \(w_{ij}\) 配对，并在所有指标上用 Frobenius Cauchy，得到
\[
M_3xz+2M_2yz+M_1z^2.
\tag{Y.11}
\]
其中 \(D^2v,Dw,D^2w\) 的缩并由其三个 Frobenius 长度的乘积控制；归一化空间积分后只需 \(y,z\) 的 Cauchy。

自作用 \((w\cdot\nabla)w\) 的最高输运项消去后，剩余与 Y.10 同型的两项以及 \((\partial_{ij}w\cdot\nabla)w\)。每项均不超过 \(\|Dw\|_{\infty,F}z^2\)，故合计
\[
3\|Dw\|_{\infty,F}z^2\le3A_1(w)z^2\le21Hz^2.
\tag{Y.12}
\]
残差配对不超过 \(r_2z\)，黏性给精确 \(\nu H^2\)。合并 Y.10–Y.12 后，
\[
\frac12(z^2)'+\nu H^2
\le3M_1z^2+3M_2yz+M_3xz+21Hz^2+r_2z.
\]
Young 不等式在此保留一半耗散：
\[
21Hz^2\le\frac\nu2H^2+\frac{441}{2\nu}z^4.
\]
于是完整平方范数预算为
\[
\boxed{\frac12(z^2)'+\frac\nu2H^2
\le3M_1z^2+3M_2\sqrt{xz}\,z+M_3xz
+\frac{441}{2\nu}z^4+r_2z.}
\tag{Y.13}
\]
在 \(z>0\) 处除以 \(z\)，再丢掉非负耗散，恰得合同候选
\[
\boxed{z'\le3M_1z+3M_2\sqrt{xz}+M_3x
+\frac{441}{2\nu}z^3+r_2.}
\tag{Y.14}
\]
常数 \(441/(2\nu)\) 属于保留半份耗散后的充分上界，不声称是最优系数。

## 5. 零范数、积分形式及正上解比较

在任意紧光滑真解时段，\(w\) 与 \(D^2w\) 作为 \(L^2\) 值函数可微，其范数局部 Lipschitz。若 \(x(t)=0\)，则 \(w(t)=0\)，Y.2 给 \(w_t(t)=-R(t)\)，因此
\[
D^+x(t)=\|R(t)\|_2\le r_0(t).
\]
若 \(z(t)=0\)，由零均值及 Fourier 表示同样得到 \(w(t)=0\)，从而
\[
D^+z(t)=\|D^2R(t)\|_2\le r_2(t).
\]
所以 Y.9、Y.14 在零范数处仍有正确上右 Dini 解释；不以除零得到它们。它们也几乎处处成立，并可在任意子区间积分。Y.8、Y.13 本身不除以范数，在零点仍成立。

令独立给定的控制函数 \(\alpha,\beta\) 在整个预定 \([0,T]\) 上绝对连续，且
\[
\alpha\ge0,\qquad \beta>0,
\quad\alpha(0)\ge\|a-v(0)\|_2,
\quad\beta(0)\ge\|D^2(a-v(0))\|_2.
\tag{Y.15}
\]
要求几乎处处
\[
\alpha'\ge M_1\alpha+r_0,
\]
\[
\beta'\ge3M_1\beta+3M_2\sqrt{\alpha\beta}
+M_3\alpha+\frac{441}{2\nu}\beta^3+r_2,
\qquad\max_{[0,T]}\beta<\infty.
\tag{Y.16}
\]
第一个线性比较先给 \(x\le\alpha\)。随后将 Y.14 的 \(x\) 换成 \(\alpha\)，所得右端为
\[
F(t,z)=3M_1z+3M_2\sqrt{\alpha z}+M_3\alpha
+\frac{441}{2\nu}z^3+r_2.
\]
正的连续 \(\beta\) 在闭窗上有最小值 \(\delta>0\)。在首次可能向上越过 \(\beta\) 的邻域，\(z\ge\delta\)；\(F\) 对 \(z\) 的 Lipschitz 常数可由 \(\delta\)、\(\sup\alpha\)、\(\sup\beta+1\) 与已知 \(M_j\) 控制。对 \((z-\beta)_+\) 用该局部 Lipschitz 界及 Gronwall 即排除越界。因此
\[
\boxed{x(t)\le\alpha(t),\qquad z(t)\le\beta(t)}
\tag{Y.17}
\]
在原解仍光滑的部分窗口上成立，初始等号亦允许。

这里没有假设 \(F\) 在 \(z=0\) 局部 Lipschitz：\(\sqrt z\) 项通常不满足它。严格正的 \(\beta\) 正是使上述比较合法的充分条件。不能直接以零上解套用有唯一性保证的标量比较。若原始误差为零，可以未来选取严格正的上解起值，但本文没有替它填写未经认证的数值。

## 6. 控制窗口确实延拓同一真实解

以上比较不是假定原解先存在至 \(T\)。设其最大光滑时间 \(T_{\max}\le T\)。在 \([0,T_{\max})\) 上已有 Y.17。由 Y.13，取其右端的已知上界
\[
J(t)=3M_1\beta^2+3M_2\sqrt{\alpha\beta}\,\beta
+M_3\alpha\beta+\frac{441}{2\nu}\beta^4+r_2\beta.
\]
它在 \([0,T]\) 可积，且对 \(S<T_{\max}\)，
\[
\int_0^S H^2dt
\le\frac{z(0)^2+2\int_0^TJ(t)dt}{\nu}.
\tag{Y.18}
\]
又由 Y.5 及归一化体积，\(A_1(v)\le7\|D^3v\|_2\le7M_3\)，所以
\[
\int_0^{T_{\max}}A_1(u)dt
\le7\int_0^TM_3dt
+7\sqrt T\left(\frac{z(0)^2+2\int_0^TJdt}{\nu}\right)^{1/2}<\infty.
\tag{Y.19}
\]
这不是把未知真解导数当作控制 ODE 的输入；它是由已认证候选输入与控制函数推出的结果。

必要的光滑延拓理由也可直接核对。对 \(\Lambda^m=(1-\Delta)^{m/2}\)，均值定理给
\[
|\langle p+q\rangle^m-\langle q\rangle^m|\,|q|
\le C_m[\langle p\rangle^m|q|+|p|\langle q\rangle^m],\quad m\ge1.
\]
Fourier \(\ell^1*\ell^2\) 估计以及最高输运相消因此给完整 NS 的
\[
\tfrac12(\|u\|_{H^m}^2)'+\nu\|\nabla u\|_{H^m}^2
\le C_m A_1(u)\|u\|_{H^m}^2.
\tag{Y.20}
\]
Y.19 与 Gronwall 在假设有限终点前控制所有有限阶 \(H^m\)。

为明确延拓的统一寿命，也有更直接的低阶界
\[
A_0(u)\le A_0(v)+A_0(w)\le7(M_2+\beta).
\tag{Y.21}
\]
完整 Wiener mild 映射的双线性积分范数不超过 \(2\sqrt{\tau/\nu}\|f\|_{C A_0}\|g\|_{C A_0}\)，因为无散性将导数放到输出频率，\(|k|e^{-\nu s|k|^2}\le(\nu s)^{-1/2}\)。从任意光滑起点 \(b\) 的半径 \(2A_0(b)\) 球出发，\(\tau\le\nu/(256A_0(b)^2)\) 给映球界 \(3A_0(b)/2\) 和差值常数 \(1/2\)。高阶 tame 权重与同一个可积半阶 Volterra 核使任意光滑起点在这一同窗保持光滑，不需要为每阶另缩寿命；其反复卷积级数分母为 \(\Gamma(1+n/2)\)，在有限窗上收敛。

具体地，齐次高阶权重满足 \(|p+q|^\ell\le2^{\ell-1}(|p|^\ell+|q|^\ell)\)。Picard 项的统一 \(A_0\le2A_0(b)\) 界给高阶迭代范数
\[
Z_{j+1}(t)\le A_\ell(b)+c_\ell\int_0^t(t-s)^{-1/2}Z_j(s)ds,
\quad c_\ell=2^\ell(2A_0(b))/\sqrt\nu.
\]
其上界为 \(A_\ell(b)\sum_{n\ge0}(c_\ell\sqrt\pi)^nt^{n/2}/\Gamma(1+n/2)\)。高一阶一致界与 \(A_0\) 压缩收敛经加权 \(\ell^1\) 插值得到任意有限阶连续收敛，方程再给时间光滑性。

Y.21 给从逼近 \(T_{\max}\) 的任一时刻启动上述局部构造的统一正寿命；唯一性将其与原解重叠识别，得到超过 \(T_{\max}\) 的延拓，矛盾。零起点由唯一零解单独处理。因此 Y.15–Y.16 一旦实际支付，确实保证同一原解光滑到达 \(T\)，而非只在“假如已存在到 \(T\)”时估计误差。

## 7. 终点严格小数据门的核对与连接

已全文读取 `ANALYTIC_PREFLIGHT.md`；本节独立核验其中用于终点连接的 G.1–G.8 及光滑延拓，不把本文视作对其余纯热失败部分的全新认证。

对零均值无散真解记 \(X=A_{-1}(u),F=A_0(u),Y=A_1(u)\)。输出频率形式和 Leray 收缩给
\[
A_{-1}(B(u,u))\le F^2,\qquad F^2\le XY.
\]
对每个复向量 Fourier 系数的模长，零系数处用右 Dini 导数，先积分有限和再以单调收敛取全部模式，得到
\[
X(t)+\nu\int_s^tY\le X(s)+\int_s^tF^2,
\qquad X'+(\nu-X)Y\le0.
\tag{Y.22}
\]
紧光滑段上右端可积、\(X\) 绝对连续，故积分/几乎处处/Dini 形式与该原稿一致。若真实终点值 \(X(T)=R_*<\nu\)，连续性与首次接触给以后 \(X\le R_*\)，于是
\[
\int_T^S A_1(u)dt\le\frac{R_*}{\nu-R_*}
\]
对所有仍光滑的 \(S\) 成立。用 Y.20 及上节统一寿命理由排除有限最大光滑终点。这是从已有光滑起点通过严格门后的全局延拓；不处理任意粗糙 \(A_{-1}\) 初值，也不使用等号门。

Y.5、Y.17 及三角不等式给真实终点
\[
A_{-1}(u(T))\le A_{-1}(v(T))+6\beta(T).
\]
因此在 Y.3、Y.15–Y.16 已实际支付之后，若再实际验证
\[
\boxed{A_{-1}(v(T))+6\beta(T)<\nu,}
\tag{Y.23}
\]
便可认证同一初值 \(a\) 的原 NS 解全局光滑。这里还需要独立上界覆盖 \(v(T)\) 的完整 \(A_{-1}\) 尾；有限截断目标值不能代替它。

## 8. 保留固定环面谱隙的强化预算

因为 \(w\) 零均值，最小非零频率长度为 1，Y.1 直接给
\[
y^2\ge x^2,\qquad H^2\ge z^2.
\]
在 Y.8、Y.13 中保留这部分黏性，而不全部丢掉，得到更强且同样严格的式子
\[
\boxed{D^+x\le(M_1-\nu)x+r_0,}
\]
\[
\boxed{D^+z\le(3M_1-\nu/2)z+3M_2\sqrt{xz}
+M_3x+\frac{441}{2\nu}z^3+r_2.}
\tag{Y.24}
\]
正范数处如前除法，零范数处沿用 §5 的直接 Dini 计算，故没有端点例外。

后续若使用谱隙版，可用 Y.15 的同样初值和正性要求，将控制上解条件改为
\[
\alpha'\ge(M_1-\nu)\alpha+r_0,
\]
\[
\beta'\ge(3M_1-\nu/2)\beta+3M_2\sqrt{\alpha\beta}
+M_3\alpha+\frac{441}{2\nu}\beta^3+r_2.
\tag{Y.25}
\]
这里对 \(x\) 的依赖仍非减；对 \(z\) 的线性系数可以为负，但比较只需要在正 \(\beta\) 附近局部 Lipschitz，不要求右端关于 \(z\) 非减。因此先做线性 \(x\) 比较，再按 §5 对 \((z-\beta)_+\) 作局部 Gronwall，仍得 Y.17。

Y.13 的完整平方预算不因使用更强控制上解而改变，所以 Y.18–Y.23 的延拓与终点门均继续适用。Y.16 的较松合同也仍正确；实际后续成本预检可以使用 Y.25，以保留固定环面的黏性谱隙。此项无需更改常数、近似场、初值或黏性，也没有运行轨道计算。

## 9. 已证与未付项目

合同中的两个候选微分预算、常数 7/6/441、零范数处理、正上解比较、光滑延拓和终点门均已解析核验通过。适用条件是一个给定完整近似场，以及覆盖其连续残差、空间导数、初始误差与终点 Fourier 尾的独立证据。

本项没有生成 \(v\)、没有解控制 ODE、没有给出具体可行 \(T\)、\(\alpha\)、\(\beta\)，也没有证明 Y.23 可达。纯热参照在另一绝对残差合同中失败，既不能作为本合同成功的证据，也不能判定既定原解不全局。本文只提供后续计算若要实施必须支付的精确解析合同；它不自动授权扩大扫描、改初值、删种子或追加时间展开。

## 10. 实际输入绑定

以下路径相对本科学工作树。数学证明为手工解析推导；SHA-256 只绑定实际已读输入，不是数值科学证书。本次未读取 Morosi–Pizzocchero 原 PDF，也不引用其常数或算例作本证明输入。

| 实际输入路径 | SHA-256 |
| --- | --- |
| `research/reverse/fixed-seed-global-screen/HYBRID_CONTROL_CONTRACT.md` | `e1c5ac5a07926de0f6e862ba8d0096b8007d73b22b3d6f5c890071c781a9212d` |
| `research/reverse/fixed-seed-global-screen/CONTRACT.md` | `5ed4bdb7c458a720f48ee9e3ec3206153280df8101e23b3852bb13097c334f9e` |
| `research/reverse/fixed-seed-global-screen/ANALYTIC_PREFLIGHT.md` | `52793f58abf5eada0b2002b4abbf9a50dc08d52012d706b4753203c9dabde6cd` |
