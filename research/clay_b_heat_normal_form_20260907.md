# 热流三次校正：消项成立，直接大数据 Lyapunov 修补失败

2026-09-07（Asia/Shanghai）。内部解析筛查 HN；不构成新的科学发布冻结。

本节检验一个具体候选：给三维周期 NS 的半阶能量加上三次热流校正，再补一个正的四次能量项，希望得到控制任意大初值且沿解不增的泛函。结论是：第一步的三次消项确实成立；裸校正不下有界；所选正四次补项能够恢复范数控制，却仍不能使泛函沿所有光滑原 NS 解不增。这排除这一个直接闭合方案，不排除其它修正泛函或一般能量法，不证明奇性或正则性。

## 1. 原方程、三次生产与热流逆

取未归一化环面 \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\)，体积 \(V=(2\pi)^3\)，固定 \(\nu>0\)。场均为实、零均值、无散；首先在光滑类计算。记 \(\Lambda=(-\Delta)^{1/2}\)，\(\mathbb P\) 为完整 Leray 投影：

\[
 \partial_tu=\nu\Delta u-\mathcal N(u),\qquad
 \mathcal N(u)=\mathbb P[(u\cdot\nabla)u],
 \quad
 A(u)=\tfrac12\|\Lambda^{1/2}u\|_2^2,\quad
 D(u)=\|\Lambda^{3/2}u\|_2^2.
 \tag{HN.1}
\]

这里 \(A\) 是标量能量，不是文献中的 Stokes 算子。所有三维初值仍是研究目标；没有加入记忆应力、外力或截断非线性。配对采用实 \(L^2\) 内积。由于 \(\Lambda u\) 无散，压力投影可以在此配对中消去：

\[
 \frac{dA}{dt}=-\nu D+C,\qquad
 C(u)=-\langle\Lambda u,\mathcal N(u)\rangle
      =-\int_{\mathbb T^3}\Lambda u\cdot(u\cdot\nabla)u\,dx.
 \tag{HN.2}
\]

零均值周期 Sobolev 嵌入 \(\dot H^{1/2}\hookrightarrow L^3\)，用于 \(u,\Lambda u,\nabla u\)，与三因子 Hölder 给出

\[
 |C(u)|\le c_S\|\Lambda^{1/2}u\|_2
                   \|\Lambda^{3/2}u\|_2^2
          =c_S\sqrt{2A(u)}D(u).
 \tag{HN.3}
\]

这是常规临界小数据吸收结构，本节不将其计为新发现。令 \(H_s=e^{\nu s\Delta}\)，定义依赖当前场的三次泛函

\[
 B(u)=\int_0^\infty C(H_su)\,ds,\qquad
 \int_0^\infty D(H_su)\,ds=\frac{A(u)}{\nu},
 \qquad
 |B(u)|\le \frac{c_B}{\nu}A(u)^{3/2},
 \quad c_B=\sqrt2\,c_S.
 \tag{HN.4}
\]

热流的 \(A(H_su)\) 不增且因零均值趋零，故第二式是热能量等式的积分，第三式来自 HN.3；这也证明绝对收敛。此处积分的是从当前场另行出发的线性热流，不是未知 NS 未来轨道，因此没有预设全局正则性。

在光滑类，\(C\) 和 \(B\) 都是实齐次三次多项式。将三次配对完全对称化，即平均
\(-\langle\Lambda u_1,(u_2\cdot\nabla)u_3\rangle\)
在三个槽位的六个排列，再沿共同热流积分，得到 \(B\) 的对称三线性形式。HN.4 与实极化恒等式给出这一形式在 \(\dot H^{1/2}\) 三槽上的连续界，故 \(B\) 唯一连续延拓到零均值无散 \(\dot H^{1/2}\)。以下求导仍只需光滑场及光滑方向。

半群平移立即决定校正的符号：

\[
 B(H_tu)=\int_t^\infty C(H_su)\,ds,\qquad
 DB(u)[\nu\Delta u]=-C(u).
 \tag{HN.5}
\]

于是沿任意局部光滑的完整 NS 解，

\[
 \frac{d}{dt}(A+B)=-\nu D+Q(u),\qquad
 Q(u):=DB(u)[-\mathcal N(u)],\qquad
 Q(\lambda u)=\lambda^4Q(u).
 \tag{HN.6}
\]

\(Q\) 是光滑类上的实四次泛函。本文只用固定光滑场上 \(Q(u)\) 有限和齐次性；没有证明它的任意大数据符号、可吸收范数界或累计预算。不能从“降为四次余项”推断余项更小。

## 2. Fourier 分母及一个确实非零的三次量

采用 \(u(x)=\sum_k\widehat u_k e^{ik\cdot x}\)，
\(\|u\|_2^2=V\sum_k|\widehat u_k|^2\)。对非零模式 \(k\)，完整有序卷积为

\[
 \widehat{\mathcal N(u)}_k
   =i\mathbb P_k\sum_{a+b=k}(k\cdot\widehat u_a)\widehat u_b,
 \qquad
 \mathbb P_k z=z-\frac{k(k\cdot z)}{|k|^2}.
 \tag{HN.7}
\]

因每项 \(a\cdot\widehat u_a=0\)，用 \(k\) 或 \(b\) 作导数频率一致。对三角多项式可直接逐项积分；对光滑场由快速 Fourier 衰减得到同式：

\[
 B(u)=-V\,\operatorname{Re}
 \sum_{\substack{k\ne0\\a+b=k}}
 \frac{i|k|\,(k\cdot\widehat u_a)
                  (\overline{\widehat u_k}\cdot\widehat u_b)}
      {\nu(|k|^2+|a|^2+|b|^2)}.
 \tag{HN.8}
\]

分母是三个热衰减率之和，不是
\(|k|^2-|a|^2-|b|^2\)。非零贡献的分母严格正；这只是标量能量同调方程，不是对完整向量场作 Poincaré–Dulac 变换，也没有据此宣布一般正规形没有共振。

现在固定一个显式场 \(v\)：

\[
 p=(1,0,0),\quad q=(0,2,0),\quad r=p+q=(1,2,0);
 \qquad
 \widehat v_p=(0,1,0),\quad
 \widehat v_q=(1,0,0),\quad
 \widehat v_r=i(2,-1,0),\quad
 \widehat v_{-k}=\overline{\widehat v_k}.
 \tag{HN.9}
\]

其余系数均零。该场实、光滑、零均值、无散，属于完整三维问题允许的初值；它只依赖前两个坐标且第三分量为零。这个例子用于检验泛函，不是寻找三维爆破。逐项保留 HN.7 的有序卷积和投影，在与非零初始模式配对的三个正频率上得到

\[
 \widehat{\mathcal N(v)}_p=(0,1,0),\qquad
 \widehat{\mathcal N(v)}_q=(-4,0,0),\qquad
 \widehat{\mathcal N(v)}_r=\frac{3i}{5}(2,-1,0).
 \tag{HN.10}
\]

负频率取共轭。其它输出即便非零也没有从方程删除；只是计算当下的 \(C(v)\) 时，那里 \(\widehat v_k=0\)，配对为零。正频率上的实配对
\(\operatorname{Re}(\overline{\widehat v_k}\cdot\widehat{\mathcal N(v)}_k)\)
分别为 \(1,-4,3\)，因此

\[
 \begin{aligned}
 C(v)&=V(-2+16-6\sqrt5)=V(14-6\sqrt5)>0,\\
 A(v)&=V(3+5\sqrt5),\qquad
 D(v)=2V(9+25\sqrt5),\\
 C(H_sv)&=e^{-10\nu s}C(v),\qquad
 B(v)=\frac{C(v)}{10\nu}>0.
 \end{aligned}
 \tag{HN.11}
\]

严格正性只需 \(14^2=196>180=(6\sqrt5)^2\)。每个有效三元项的平方频率和是 \(1+4+5=10\)。附带一致性检查：去掉半阶权重后的非线性能量变化为 \(-2+8-6=0\)，平面涡量能量权重下为 \(-2+32-30=0\)，与通常守恒消去一致。它们不代表半阶能量也守恒。

## 3. 裸三次校正不可能控制所有大初值

因 \(A(-u)=A(u)\)、\(B(-u)=-B(u)\)，HN.11 给出

\[
 (A+B)(-\lambda v)=\lambda^2A(v)-\lambda^3B(v)
       \longrightarrow-\infty
 \quad(\lambda\to+\infty).
 \tag{HN.12}
\]

所以裸 \(A+B\) 在所有光滑零均值无散场上甚至不下有界，更不是控制 \(A\) 的全局正能量。HN.4 只能保证当 \(\sqrt{A}/\nu\) 足够小时与 \(A\) 可比；本文不单凭这一比较声称已经控制 HN.6 的余项。

这里改变的是初值振幅，不是从一条固定初值轨道提取爆破。标准局部光滑存在性允许每个有限振幅作为原 NS 初值；没有假定六个模式在后续时间保持封闭。

## 4. 加正四次项能够保正，却不能获得全局单调性

检验最直接的非负修补，固定 \(K>0\)：

\[
 F_K(u)=A(u)+B(u)+\frac{K}{\nu^2}A(u)^2,\qquad
 F_K(u)\ge A(u)(1-c_Bx+Kx^2),\quad
 x=\frac{\sqrt{A(u)}}{\nu}.
 \tag{HN.13}
\]

当 \(K\ge c_B^2/2\) 时，
\(1-c_Bx+Kx^2\ge1-c_B^2/(4K)\ge1/2\)，于是 \(F_K\ge A/2\)，确实全局控制原来的半阶范数。但是必须沿完整原方程重新求导：

\[
 \frac{dF_K}{dt}
 =-\nu D+Q-\frac{2K}{\nu}AD+\frac{2K}{\nu^2}AC.
 \tag{HN.14}
\]

对初值 \(u(0)=\lambda v\) 的实际局部光滑原 NS 解，初始导数精确为

\[
 \left.\frac{dF_K}{dt}\right|_{t=0}
 =-\nu\lambda^2D(v)
  +\lambda^4\left[Q(v)-\frac{2K}{\nu}A(v)D(v)\right]
  +\lambda^5\frac{2K}{\nu^2}A(v)C(v)>0
 \quad\text{当 }\lambda\text{ 充分大}.
 \tag{HN.15}
\]

固定 \(v,\nu,K\) 后，末项系数严格正，其余系数有限；五次项支配四次项和二次项。这对每个固定 \(K>0\) 都成立，特别包括确保 \(F_K\ge A/2\) 的那些 \(K\)。连续性还给出一个足够短的实际增长区间。无需计算 \(Q(v)\) 的具体数值，更不需要模拟长时解。

因此，这个特定补项不能同时提供“全局范数控制”和“对所有光滑原 NS 解不增”的 Lyapunov 闭合。该结论没有排除包含更高阶相互抵消项、非多项式项、时间依赖项的泛函；也没有排除容许短时增长而利用其它已付量的 Gronwall 方案。本文未得到任何这样的替代闭合。

## 5. 与既有工作的区别及本节的停止边界

本地 R0.70B 第8节是另一问题：对指定环带三次生产寻找平移不变的二次涡量乘子，并在 Euler 非线性下要求零三次余项。它明确不覆盖非二次泛函；不能用该定理直接否定这里对线性热生成元求逆的三次校正。本地 R0.73W 第7节已有热尺度积分后的临界三线性/小数据边界，但没有构造本节的 \(B\) 及 \(F_K\)。有限本地检索未发现同式记录，不代表领域新颖性。

正规形本来就是 NS 的既有研究工具。[Foias–Hoang–Olson–Ziane (2009) 官方摘要](https://ems.press/journals/aihpc/articles/4077872) 将归一化映射的原始定义域写为产生全局正则解的初值集合 \(\mathcal R\)，并讨论扩张序列空间中的系统；本轮只核读其摘要与元数据，没有调用其完整定理或证明。

[Foias–Hoang–Saut, arXiv:1711.07184v1，第1.3–1.4节](https://arxiv.org/html/1711.07184v1) 明确区分长时正则尾部与三维 \(\mathcal R=V\) 的开放问题。其晚时正规形表述不能被当成覆盖任意初值及首次潜在奇点的保证。该预印本官方提交日期为2017-11-20；HTML 显示的另一日期不作为新版本证据。[官方版本记录](https://arxiv.org/abs/1711.07184)

本节没有调用这些文献的正规形构造作为证明依赖，也没有证明四次余项的临界乘子定理。仅凭“零阶符号”断言 Coifman–Meyer 条件成立仍需处理低输出、高输入区域；未审过的估计不加入结论。

本次有限检验到此完成：热同调消项成立，但裸三次能量和所选正四次修补均不能给出所期待的直接大数据单调能量。停止对这一具体形式的重复调参。任意大初值三维正则性、G、R216–R217 及一般终端缺口仍 OPEN / NOT CLAY。没有接受下一条无条件闭合候选，也不将“再加若干高阶项”自动批准为下一阶段。

这是一条内部、可审查的候选排除记录，不新增科学 release、不再次交接此前 FA。实际数学审查、有限复算和版本保留范围见配套 audit/checks；研究任务不检查或执行发布。
