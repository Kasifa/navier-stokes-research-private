# 中文第 5–7 节及附录 A–D 语义审校

结论：当前机器翻译快照 **不宜直接发布**。以下提供完整段落替换，覆盖实质误译及明显不通顺；数学表达式、公式编号、交叉引用、文献引文与代码节点均复用英文快照原始 HTML。此处是翻译语义审校，不是重新审定数学证明，也不重复英文公式核对。

## 快照与定位

- 中文：`/tmp/heat-edge-zh.html`；SHA256 `039fdaa1c280bb8239121b5cb1a25fcbe9684cbdc43c1fbf17fa037ad0245c19`。
- 英文：`/tmp/heat-edge-en-normalized.html`；SHA256 `5d0b319f6e0b90d1c2def1ce3913bc0e2227e87294e59a181547812b3064df1b`。
- 冻结源稿：`paper-edge-v2/papers/near-edge-extrapolation-and-parabolic-shear/arxiv/source/sections/` 中 `frame-and-mass.tex`、`upper-bound.tex`、`discussion.tex`、`time-weighted.tex`、`sharpness.tex`、`consequences.tex`、`diagnostic.tex`。
- P54–P116 是整个英文/中文片段中从 1 起算的 `<p>` 序号，即 XPath `(//p)[n]`，不是段落现有 ID。图注单列。对应第 5 节 P54–69，第 6 节 P70–83，第 7 节 P84–89，附录 A P90–96，B P97–106，C P107–113，D P114–116。
- 下面的 HTML 代码块可以整体替换对应 `<p>`；外层定理/证明容器与锚点不移动。代码块中的显示公式及其关联锚点、编号也已完整保留，不应再追加原段落的公式编号。

## 必须纠正的语义

| 段落 | 当前实际错误 | 正确限定或方向 |
|---|---|---|
| P64 | Minkowski 上界译成“限制在……之上”，单调方向表述含混 | 该范数随 λ 增大而减小；Minkowski 给出上界 |
| P74 | `such that` 译成“例如”；固定条件变成示例，截断函数范围条件错接 | 所列均为假设；0≤θ≤1 为全局约束，θ=1 仅在指定区间 |
| P77 | 区间长度“一致有上下界”译成残句 | 上界与严格正的下界均需保留 |
| P81 | 指数的 `real parts` 译成“真实零件” | 复指数实部位于所列区间，且分 λ≤1 与 λ>1 两种情形 |
| P87 | `No priority claim ... beyond ...` 被打乱为“无优先权该声明超出……” | 不提出超出第 3 节显式比较范围的优先权主张 |
| P90 | measure space 译成“度量空间”；末句语法失效 | 测度空间；既不需要实部上界，也不需要虚部有界 |
| P93、P95 | order witness、abstract class 译为“命令证人”“摘要类” | 抽象时间范数类中的阶见证；不转化为空间约束下的最优性 |
| P99 | phases 译成“阶段” | 任意相位允许吸收符号，正振幅不排除相消 |
| P101 | `the carrier is one and ...` 漏掉“等于 1”，将载波误接为后面的切比雪夫不等式 | 端点载波因子等于 1；后一个不等式另述 |
| P110 | `Neither ... nor ...` 的否定丢失，变成“确定实际通量的变化” | 等号或阈值失效都不能据此断言实际通量发生转变 |
| P113 | `more slowly than` 丢失“更慢” | μ 可以比 log A 增长得更慢；不能仅凭指数简写断言商发散 |
| P114–116、图注 | 鞍点、次数增长律、数值求积、极限等被译为“鞍座”“四次定律”“正交”“限制” | 有限网格稳定性诊断不构成全部次数/尺度的误差包络或连续极限证书 |

其他逐段修订同时恢复：完整空间平台与完整速度两种质量的区别；固定参考系；固定振幅与任意振幅缩放的量词；有符号整个时间积分及帽区相消；文学来源应为数学文献；AI 自动审查不等于人类同行评审或形式化证明认证。

## 精确替换：第 5 节

### P54

```html
<p>完整空间平台与完整速度之间的区别至关重要。本节将式 <a href="#eq:parabolic-physical-payment" class="xref" data-ref-target="eq:parabolic-physical-payment">(30)</a> 中的量记为 <span class="math inline">\(M_{F,L}=M_L^{\mathrm{plat}}\)</span>；除非另有说明，沿用定理 <a href="#thm:parabolic-shear" class="xref" data-ref-target="thm:parabolic-shear">4.5</a> 中的精确初始系数、截断函数和次数序列。以下结论讨论该显式构造族的归一化，并非一般的局部能量估计。</p>
```

### P55

```html
<p><strong>命题 5.1（观测参考系的变换）</strong> 对于 <span class="math inline">\(u(t,x)=(0,B,F(t,x_2))\)</span>，定义 <span class="math inline">\(y=x-Bt e_2\)</span> 以及 <span class="math display" data-source-display="display-078" data-source-sha256="4478769d20d85a88f340cf8d993aeb677ff50faf7bfc78505f40e7b06f1e706a">\[\widetilde u(t,y)=u(t,y+Bt e_2)-B
e_2=(0,0,H(t,y_2)).\]</span> 则有 <span class="math inline">\(H_t=H_{y_2y_2}\)</span>。对任意支集位于环面的某个欧氏坐标图内的光滑径向截断函数 <span class="math inline">\(\phi(y)\)</span>，都有 <span class="math display" data-source-display="display-079" data-source-sha256="bd08e5d2caf90aaeb7d2740c47448f79b52681b98ca161f1b64e126557974671">\[\frac12\int_{\mathbb T^3}|\widetilde u|^2
                     \widetilde
u\cdot\nabla\phi\,dy=0.\]</span></p>
```

### P56

```html
<p><em>证明。</em> 由定义可得 <span class="math inline">\(H(t,y_2)=F(t,y_2+Bt)\)</span>，因此 <span class="math inline">\(H_t=F_t+BF_{x_2}=F_{x_2x_2}\)</span>。通量的被积函数为 <span class="math inline">\(H(t,y_2)^3\partial_{y_3}\phi/2\)</span>。由微积分基本定理及 <span class="math inline">\(\phi\)</span> 的支集条件，它对 <span class="math inline">\(y_3\)</span> 的积分为零。利用周期性也可得到相同结论。◻</p>
```

### P57

```html
<p>在 <span class="math inline">\(y\)</span> 坐标中固定的截断函数，对应于原坐标中随时间平移的截断函数。此外，减去常速度后，动能也会改变。因此，此处的零通量与定理 <a href="#thm:parabolic-shear" class="xref" data-ref-target="thm:parabolic-shear">4.5</a> 中的正通量是两种不同的观测量；后者不具有伽利略不变性。它测量的是通过固定窗口的常速度输运。本构造并未引入涡拉伸或能量级联机制。</p>
```

### P58

```html
<p><strong>命题 5.2（指定振幅下的完整速度质量）</strong> 定义正的完整速度质量及时空体积为 <span class="math display" data-source-display="display-080" data-source-sha256="49660e0afbd27f1154f9ad735c6ada6bb30ed4a09043689553f0b7fb73bb2e2e">\[M_{u,L}=\int_0^{4R^2}\int_{\mathcal P_L}
                  (B^2+F(t,x_2)^2)^{3/2}\,dx\,dt,
\qquad V_L=4R^2|\mathcal P_L|.\]</span> 沿满足式 <a href="#eq:edge-degree-regime" class="xref" data-ref-target="eq:edge-degree-regime">(17)</a> 的每一个次数序列，都有 <span class="tex-anchor" id="eq:complete-volume" aria-hidden="true"></span><span class="tex-anchor" id="eq:complete-mass" aria-hidden="true"></span><span class="tex-anchor" id="eq:component-scales" aria-hidden="true"></span><span class="math display" data-source-display="display-081" data-source-sha256="04f56d3a5a1067870bc3dbc30f6d373603a9b6e80c6695ae0c9406fc0196e42a">\[\begin{align}
V_L&amp;=32\pi\delta_0a^2R^5
                   \left(1+\frac{\delta_0^2}{3a^2}\right),
                   \\
M_{u,L}&amp;=(1+o(1))\,32\pi\delta_0\beta^3
                       \frac{a^5}{A^3}R^2,\\
M_{F,L}&amp;=R^5\exp(o(L^2)),\qquad
\mathcal T_L=R^3\exp(o(L^2)).
\end{align}\]</span><span class="equation-numbers">(38) · (39) · (40)</span> 最后一式使用了 <span class="math inline">\(\mathcal T_L\)</span> 最终为正这一事实。特别地，<span class="tex-anchor" id="eq:complete-velocity-rate" aria-hidden="true"></span><span class="math display" data-source-display="display-082" data-source-sha256="4f6ab201e3787f8c2e62ea5d3c9a0a024fafac1d4fedfcf075ab7bfbe5ad5252">\[\begin{equation}

R^{1/3}\frac{\mathcal T_L}{M_{u,L}^{2/3}}
   =R^2\exp(o(L^2))\longrightarrow0,
\qquad
\lim_{L\to\infty}\frac1{L^2}
\log\left(R^{1/3}\frac{\mathcal T_L}{M_{u,L}^{2/3}}\right)
   =-\frac9{20000}.
\end{equation}\]</span><span class="equation-numbers">(41)</span> 所有极限均针对式 <a href="#eq:parabolic-fourier-coefficients" class="xref" data-ref-target="eq:parabolic-fourier-coefficients">(24)</a> 中固定的振幅；这些结论对振幅的任意重新缩放并不一致成立。</p>
```

### P59

```html
<p><em>证明。</em> 将两个球的体积相减，即精确得到式 <a href="#eq:complete-volume" class="xref" data-ref-target="eq:complete-volume">(38)</a>。由于 <span class="math inline">\(a,A\asymp L\)</span> 且 <span class="math inline">\(\mu=o(A)\)</span>，全局控制上界与动态传递估计给出 <span class="math display" data-source-display="display-083" data-source-sha256="a3b2772ecb9ab4e7674f46e7dfcb407a77b44ed755d5f9819c89510e87a0c05e">\[\sup_{[0,4R^2]\times\mathcal
P_L}|F|
\le C Q_{m,A}(4,c_p+4\gamma_L)+o(1)
=\exp(o(L^2)),
\qquad \gamma_L=\beta a/A.\]</span> 事实上，热演化边缘定理表明：对于有界范围内的坐标 <span class="math inline">\(c\)</span>，有 <span class="math inline">\(\log
Q_{m,A}(4,c)=F_4\mu^2+o(\mu^2)+O(\mu)\)</span>，且关于 <span class="math inline">\(c\)</span> 一致成立。另一方面，<span class="math inline">\(|B|=\beta a/(AR)\)</span>，故 <span class="math inline">\(\sup|F|/|B|\to0\)</span>。在整个积分区域上一致有 <span class="math inline">\((B^2+F^2)^{3/2}=|B|^3(1+o(1))\)</span>。乘以精确的时空体积，即得式 <a href="#eq:complete-mass" class="xref" data-ref-target="eq:complete-mass">(39)</a>。</p>
```

### P60

```html
<p>对于余下的两个尺度，先使用式 <a href="#eq:parabolic-S-bounds" class="xref" data-ref-target="eq:parabolic-S-bounds">(35)</a>、<a href="#eq:parabolic-K-upper" class="xref" data-ref-target="eq:parabolic-K-upper">(36)</a>、<a href="#eq:parabolic-K-lower" class="xref" data-ref-target="eq:parabolic-K-lower">(37)</a> 中的正下界和上界，再使用式 <a href="#eq:parabolic-dimensional-identities" class="xref" data-ref-target="eq:parabolic-dimensional-identities">(34)</a>。这些界中的每个 <span class="math inline">\(Q(4,c)\)</span> 的对数都是 <span class="math inline">\(o(L^2)\)</span>；<span class="math inline">\(a,A,\beta\)</span> 以及 <span class="math inline">\(h_\mu=(1+\mu^2)^{-1}\)</span> 所贡献的对数为 <span class="math inline">\(O(\log A)=o(L^2)\)</span>。于是上下两侧均给出式 <a href="#eq:component-scales" class="xref" data-ref-target="eq:component-scales">(40)</a>。这一步使用的是整个有符号时间积分的下界，并非某个帽区贡献的绝对值。</p>
```

### P61

```html
<p>对于该族的每个非零成员，分母 <span class="math inline">\(M_{F,L}\)</span> 都为正：非零有限傅里叶和不可能在一个空间区间上恒为零，而平台在一个区间上具有正的横截面积。时间演化保持其非零傅里叶系数。<span class="math inline">\(\mathcal T_L\)</span> 的正性则仅在序列上最终成立；它来自定理 <a href="#thm:parabolic-shear" class="xref" data-ref-target="thm:parabolic-shear">4.5</a> 中晚时刻帽区的配对，以及对较早时段有符号贡献的吸收。因此，沿每个序列，式 <a href="#eq:complete-velocity-rate" class="xref" data-ref-target="eq:complete-velocity-rate">(41)</a> 中的对数最终有定义。式 <a href="#eq:complete-mass" class="xref" data-ref-target="eq:complete-mass">(39)</a>–<a href="#eq:component-scales" class="xref" data-ref-target="eq:component-scales">(40)</a> 给出的净幂次为 <span class="math inline">\(R^{1/3+3-4/3}=R^2\)</span>。最后，<span class="math inline">\(2L^{-2}\log R=-9/20000\)</span>。◻</p>
```

### P62

```html
<p>关于振幅的限定不能删除。下面的初等结论明确展示了这种依赖关系。</p>
```

### P63

```html
<p><strong>命题 5.3（振幅重新缩放）</strong> 固定一个剪切流、一个时空体积为 <span class="math inline">\(V&gt;0\)</span> 的有限观测区域，以及与上文相同的分子和分母定义。假设 <span class="math inline">\(M_F&gt;0\)</span> 且 <span class="math inline">\(\mathcal T\ge0\)</span>。对 <span class="math inline">\(\lambda&gt;0\)</span>，将其初始剖面替换为 <span class="math inline">\(\lambda F(0,\cdot)\)</span>，并保持 <span class="math inline">\(B\)</span> 不变。所得解在同一时间区间内的剖面始终为 <span class="math inline">\(\lambda F(t,\cdot)\)</span>。令 <span class="math display" data-source-display="display-084" data-source-sha256="2da09c1e4d3d6459dbb565b4bf19a36528768743d03bcead208445b5a9dd017a">\[Z_F=R^{1/3}\frac{\mathcal T}{M_F^{2/3}},\qquad
Z_u(\lambda)=R^{1/3}
  \frac{\lambda^2\mathcal T}
  {\left[\int(B^2+\lambda^2F^2)^{3/2}\right]^{2/3}}.\]</span> 则 <span class="math inline">\(Z_u(\lambda)\)</span> 单调不减，并且 <span class="tex-anchor" id="eq:amplitude-sandwich" aria-hidden="true"></span><span class="math display" data-source-display="display-085" data-source-sha256="e91abb5c44204398ae90e4e00756416199acd4b3a63e6ee679c215a243fe0801">\[\begin{equation}

\frac{Z_F}{1+(B/\lambda)^2(V/M_F)^{2/3}}
\le Z_u(\lambda)\le Z_F,
\qquad \lim_{\lambda\to\infty}Z_u(\lambda)=Z_F.
\end{equation}\]</span><span class="equation-numbers">(42)</span> 对于命题 <a href="#prop:full-velocity-mass" class="xref" data-ref-target="prop:full-velocity-mass">5.2</a> 中的构造族，显式选取 <span class="math inline">\(\lambda_L=R^{-2}\)</span> 可得 <span class="math inline">\(Z_u(\lambda_L)/Z_F\to1\)</span>。因此，当 <span class="math inline">\(\mu/\log A\to\infty\)</span> 时，该重新缩放后的构造族满足 <span class="math inline">\(Z_u(\lambda_L)\to\infty\)</span>。</p>
```

### P64

```html
<p><em>证明。</em> 标量平流–热方程是线性的，其输运通量关于 <span class="math inline">\(F\)</span> 为二次齐次。将完整质量除以 <span class="math inline">\(\lambda^3\)</span> 后，再取三分之二次幂，得到 <span class="math display" data-source-display="display-086" data-source-sha256="8e33af6c87c8e18bc3bc3c43dc4561fe9ac2d6915ef2921e2eb5a4d59f1b7710">\[\left\|F^2+(B/\lambda)^2\right\|_{L^{3/2}}.\]</span> 该量随 <span class="math inline">\(\lambda\)</span> 增大而减小，其下界为 <span class="math inline">\(\|F^2\|_{L^{3/2}}=M_F^{2/3}\)</span>。Minkowski 不等式给出的上界为 <span class="math inline">\(M_F^{2/3}+(B/\lambda)^2V^{2/3}\)</span>。由此得到所述不等式、单调性和极限；其中也包括 <span class="math inline">\(B=0\)</span> 的情形，此时各处均取等号。支配收敛定理也可直接给出该极限：当 <span class="math inline">\(\lambda\ge1\)</span> 时，可用 <span class="math inline">\((F^2+B^2)^{3/2}\)</span> 作为支配函数。对于指定的构造族，<span class="math display" data-source-display="display-087" data-source-sha256="203eacf6ef6ea6d3b33efd8472e54e9f663e89703fe5790bb4f63625bb3d4065">\[(B/\lambda_L)^2(V_L/M_{F,L})^{2/3}
       =R^2\exp(o(L^2))\longrightarrow0.\]</span> 所述发散结论遂由定理 <a href="#thm:parabolic-shear" class="xref" data-ref-target="thm:parabolic-shear">4.5</a> 得到。每个重新缩放后的成员，在整个时间区间上仍使用同一份初始数据。◻</p>
```

### P65

```html
<p>这种重新缩放保留了很大的常漂移，并不能产生一致有界的初始能量。这说明式 <a href="#eq:complete-velocity-rate" class="xref" data-ref-target="eq:complete-velocity-rate">(41)</a> 不能被解读为针对所有振幅归一化方式的不可能性定理。它也不是一般局部能量估计的反例：本文的分量估计保留了已明确写出的几何因子和频率因子，而重新缩放并不会消除这些因子。</p>
```

### P66

```html
<p><strong>命题 5.4（相同初始形状下的有界漂移）</strong> 保持 <span class="math inline">\(a,A,R,m\)</span> 以及式 <a href="#eq:parabolic-fourier-coefficients" class="xref" data-ref-target="eq:parabolic-fourier-coefficients">(24)</a> 中的初始系数不变，将漂移替换为任意满足 <span class="math inline">\(|B_L|\le B_*&lt;\infty\)</span> 的 <span class="math inline">\(B_L\)</span>。将相应的通量和分量质量分别记为 <span class="math inline">\(\mathcal T_L^{(B_L)}\)</span> 和 <span class="math inline">\(M_{F,L}^{(B_L)}\)</span>。存在仅依赖于固定截断函数及 <span class="math inline">\(B_*\)</span> 的常数 <span class="math inline">\(C\)</span>，使得沿每个允许的次数序列，最终都有 <span class="tex-anchor" id="eq:bounded-drift-decay" aria-hidden="true"></span><span class="math display" data-source-display="display-088" data-source-sha256="34ab19eb9cfe1547c9e2c2414075f6427f67404600e7fb7307500eae637610b8">\[\begin{equation}

R^{1/3}\frac{|\mathcal T_L^{(B_L)}|}
{(M_{F,L}^{(B_L)})^{2/3}}
\le C |B_L|R a^{1/3}(1+\mu^2)^{2/3}e^{C\mu}
\longrightarrow0.
\end{equation}\]</span><span class="equation-numbers">(43)</span> 对振幅作任意正倍数缩放，并将分量质量替换为完整速度质量后，同一个上界仍然成立。若 <span class="math inline">\(B_L=0\)</span>，则通量精确为零。</p>
```

### P67

```html
<p><em>证明。</em> 在命题 <a href="#prop:dynamic-confluence" class="xref" data-ref-target="prop:dynamic-confluence">4.3</a> 中，<span class="math inline">\(x\)</span> 坐标上的实平移变为 <span class="math inline">\(B_LRs/A\)</span>。其余算子估计、载波估计及汇合估计均不变；这里的平移小于该命题已经允许的平移。因此，对于有界的 <span class="math inline">\(B_L\)</span>，相同的绝对传递界一致成立。</p>
```

### P68

```html
<p>由精确的通量横截面公式以及 <span class="math inline">\(\int|W_a|\le C\)</span>，对某个固定的 <span class="math inline">\(C_1&gt;0\)</span> 可得 <span class="math display" data-source-display="display-089" data-source-sha256="b42b93d62413d024f00e5a1b510bdc730a77c3bb5f72bed9797e7b109caa63f1">\[|\mathcal T_L^{(B_L)}|
       \le C|B_L|aR^4 Q_{m,A}(4,C_1)^2\]</span> 为得到质量下界，选取边缘坐标位移为 <span class="math inline">\(+|B_L|Rs\)</span> 的一侧外平台条带。理想多项式的奇偶性允许选取任意一侧。在长度为 <span class="math inline">\(h_\mu\)</span> 的末端时间层上，该条带的边缘坐标至少为 <span class="math inline">\(\delta_0\)</span>。由末端导数估计和绝对传递界，得到 <span class="math display" data-source-display="display-090" data-source-sha256="c09cab6107a7e5e25b8842c9700132c6efaadda6989e7ff041535595367c8f27">\[M_{F,L}^{(B_L)}
       \ge caR^5 h_\mu Q_{m,A}(4,\delta_0)^3.\]</span> 此处限制积分区域仅用于证明这个下界；质量的定义仍然包含完整空间平台及整个时间区间。<span class="math inline">\(C_1\)</span> 与 <span class="math inline">\(\delta_0\)</span> 处的热演化边缘比值至多为 <span class="math inline">\(e^{C\mu}\)</span>。结合上述两个界，即得式 <a href="#eq:bounded-drift-decay" class="xref" data-ref-target="eq:bounded-drift-decay">(43)</a>。其对数上界为 <span class="math inline">\(\log R+O(\mu+\log
A)\)</span> 加一个有界项；由于 <span class="math inline">\(\mu=o(A)\)</span> 且 <span class="math inline">\(A\asymp L\)</span>，该上界趋于 <span class="math inline">\(-\infty\)</span>。分量商在振幅重新缩放下不变，而完整质量不小于分量质量。由此得到最后的断言。当 <span class="math inline">\(B_L=0\)</span> 时，精确的横截面通量公式为零。◻</p>
```

### P69

```html
<p>最后这个命题针对的是相同的初始形状和尺度。它既不排除其他具有有界漂移的剖面，也未对一般傅里叶类给出相匹配的动态上界和下界。</p>
```

## 精确替换：第 6 节

### P70

```html
<p>这一辅助应用将已有的空间不等式、时间不等式与剪切流的能量恒等式结合起来，并不单独提出新的外推尺度。</p>
```

### P71

```html
<p><strong>引理 6.1（引自 Zhang 的空间估计）</strong> 设 <span class="math inline">\(g(x)=\sum_{j=1}^N c_j e^{i\xi_jx}\)</span> 的频率为任意实数、系数为复数，并且 <span class="math inline">\(0\le d\le1\)</span>，则 <span class="tex-anchor" id="eq:ub-edge" aria-hidden="true"></span><span class="math display" data-source-display="display-091" data-source-sha256="109435ccc6821d09644eb3277c7595ba22f86c0668ef2230a3c8e0817e02a804">\[\begin{equation}

\max\{|g(1+d)|,|g(-1-d)|\}
\le C_ZN e^{3\sqrt2N\sqrt d}\|g\|_{L^2(-1,1)},
\qquad C_Z=\sqrt{9\cdot8191/2}.
\end{equation}\]</span><span class="equation-numbers">(44)</span> 因而，对 <span class="math inline">\(J=[-e,e]\)</span>、<span class="math inline">\(I=[-e(1+d),e(1+d)]\)</span> 及 <span class="math inline">\(e&gt;0\)</span>，有 <span class="tex-anchor" id="eq:ub-affine-edge" aria-hidden="true"></span><span class="math display" data-source-display="display-092" data-source-sha256="b11cf95d637b291d454fd25ee49348f7aef38b55da4815bad1bb5412e22e411e">\[\begin{equation}

\|g\|_{L^\infty(I)}^2
\le\frac{C_Z^2}{e}N^2e^{6\sqrt2N\sqrt d}\int_J|g|^2.
\end{equation}\]</span><span class="equation-numbers">(45)</span></p>
```

### P72

```html
<p><em>来源与缩放。</em> 右端点的结论来自 Zhang 的近边缘定理 <span class="citation" data-cites="Zhang2026">(<a href="#ref-Zhang2026" role="doc-biblioref">Zhang 2026</a>, Theorem 1.1 and Proposition 4.2,
v1)</span>，其中采用可用的有限区间常数 <span class="math inline">\(8191\)</span>。通过反射可得左端点的结论。这里不要求频率分离；重复频率可以合并，系数允许为零。仿射缩放给出 <span class="math inline">\(J\)</span> 外部的第二个结论。对于内部点 <span class="math inline">\(z\)</span>，分别在 <span class="math inline">\([-e,z]\)</span> 和 <span class="math inline">\([z,e]\)</span> 上应用 <span class="math inline">\(d=0\)</span> 时的端点界，得到 <span class="math inline">\(\ell_\pm|g(z)|^2\le2C_Z^2N^2\int_{J_\pm}|g|^2\)</span>。将这两个估计相加，即得到 <span class="math inline">\(J\)</span> 上的相同界。◻</p>
```

### P73

```html
<p>此处引用的是一项预印本结果，作为注明来源的已有估计使用。本节仅需 <span class="math inline">\(d\le1\)</span> 的范围。推论 <a href="#lem:ub-delay" class="xref" data-ref-target="lem:ub-delay">A.1</a> 提供时间估计，式 <a href="#eq:ub-cutoff-time" class="xref" data-ref-target="eq:ub-cutoff-time">(65)</a> 是其缩放形式。</p>
```

### P74

```html
<p>记 <span class="math inline">\(\mathbb T=\mathbb R/(2\pi\mathbb
Z)\)</span>。固定 <span class="math inline">\(0&lt;\delta_0&lt;\delta\)</span> 及函数 <span class="math inline">\(\vartheta\in
C_c^\infty((-\delta,\delta))\)</span>，要求它满足 <span class="math inline">\(0\le\vartheta\le1\)</span>，并且在 <span class="math inline">\([-\delta_0,\delta_0]\)</span> 上有 <span class="math inline">\(\vartheta=1\)</span>。再固定满足 <span class="math inline">\(0\le\eta\le1\)</span> 和 <span class="math inline">\(\eta(0)=0\)</span> 的函数 <span class="math inline">\(\eta\in C^1([0,4])\)</span>。对满足 <span class="math inline">\(R&gt;0\)</span>、<span class="math inline">\(a\ge\max(1,\delta+2\delta_0)\)</span> 及 <span class="math inline">\((a+\delta)R&lt;\pi/2\)</span> 的参数，定义 <span class="tex-anchor" id="eq:ub-geometry" aria-hidden="true"></span><span class="tex-anchor" id="eq:ub-F" aria-hidden="true"></span><span class="math display" data-source-display="display-093" data-source-sha256="d404a56e711c1373daae1c0e68483383cba60d0743f3a96cf22aa43e25a1de10">\[\begin{align}
\xi_{a,R}(x)&amp;=\vartheta(|x|/R-a),&amp;
\mathcal S^{\rm plat}_{a,R}
&amp;=\{x\in\mathbb T^3:\,||x|/R-a|\le\delta_0\},
\\
F(t,x_2)&amp;=\sum_{j=1}^q A_je^{-n_j^2t}
                   \cos(n_jx_2-\phi_j-n_jBt),

\end{align}\]</span><span class="equation-numbers">(46) · (47)</span> 其中项数 <span class="math inline">\(q\ge1\)</span>，各频率为满足 <span class="math inline">\(1\le n_1&lt;\cdots&lt;n_q\le2n_1\)</span> 的整数，且 <span class="math inline">\(A_j\ge0\)</span>、<span class="math inline">\(\phi_j,B\in\mathbb R\)</span>。截断函数的支集位于环面的一个欧氏坐标图内，并在该坐标图外延拓为零。速度场 <span class="math inline">\(u=(0,B,F)\)</span> 是黏度为 1、压力为零的精确光滑 Navier–Stokes 解：唯一非平凡的演化方程为 <span class="math inline">\(F_t+BF_{x_2}-F_{x_2x_2}=0\)</span>。</p>
```

### P75

```html
<p>定义完整通量与完整平台观测量为 <span class="tex-anchor" id="eq:ub-T" aria-hidden="true"></span><span class="tex-anchor" id="eq:ub-M" aria-hidden="true"></span><span class="math display" data-source-display="display-094" data-source-sha256="85ea2b24a0ba6ad61ed22e8757ab9e389050a546a484fcfb9d4c3dc27a0c19eb">\[\begin{align}
\mathcal T_{\boldsymbol n,R}
&amp;=\frac12\int_0^{4R^2}\!\int_{\mathbb T^3}
       \eta(t/R^2)B\,\partial_2\xi_{a,R}(x)F(t,x_2)^2\,dx\,dt,
\\
M^{\rm plat}_{\boldsymbol n,R}
&amp;=\int_0^{4R^2}\!\int_{\mathcal S^{\rm plat}_{a,R}}
                         |F(t,x_2)|^3\,dx\,dt.

\end{align}\]</span><span class="equation-numbers">(48) · (49)</span> 时间截断函数只出现在通量中；平台观测量采用整个不加时间权重的时间区间。</p>
```

### P76

```html
<p><strong>定理 6.2（完整时间区间上的上界）</strong> 对上述数据，令 <span class="math display" data-source-display="display-095" data-source-sha256="80edaf8df92703c85a656f7a6392b77e83a6e303394f50147d8aa3c86ebeb65f">\[\Delta_a=\frac{\delta+\delta_0}{a-\delta_0},\qquad
\Phi_a=12\sqrt2q\sqrt{\Delta_a}.\]</span> 存在仅依赖于 <span class="math inline">\(\vartheta,\delta_0,\delta\)</span> 及 <span class="math inline">\(\|\eta'\|_\infty\)</span> 的常数 <span class="math inline">\(C\)</span>，使得 <span class="tex-anchor" id="eq:ub-main-refined" aria-hidden="true"></span><span class="math display" data-source-display="display-096" data-source-sha256="3e1f5c925982bed5e714ebb9928bade9a5daa85c55cb6563728005eb77eb9d7b">\[\begin{equation}

|\mathcal T_{\boldsymbol n,R}|
\le C a^{2/3}R^{-1/3}
       \left(q^4+\frac{q^7}{a^2}+q^{13/3}\right)e^{\Phi_a}
       \bigl(M^{\rm plat}_{\boldsymbol n,R}\bigr)^{2/3}.
\end{equation}\]</span><span class="equation-numbers">(50)</span> 特别地，<span class="tex-anchor" id="eq:ub-main" aria-hidden="true"></span><span class="math display" data-source-display="display-097" data-source-sha256="dafb7964506825ec5daa95ce6c5ad254bc24f22574485843f42268b511ddf09e">\[\begin{equation}

|\mathcal T_{\boldsymbol n,R}|
\le C a^{2/3}R^{-1/3}q^7e^{\Phi_a}
       \bigl(M^{\rm plat}_{\boldsymbol n,R}\bigr)^{2/3}.
\end{equation}\]</span><span class="equation-numbers">(51)</span> 该常数与 <span class="math inline">\(q,R\)</span>、所有频率、振幅、相位及 <span class="math inline">\(B\)</span> 无关。</p>
```

### P77

```html
<p><em>证明。</em> 采用缩放变量 <span class="math display" data-source-display="display-098" data-source-sha256="c6b7d28b2478c6246e3d7b42af08142fbf057ae9717129d6c181e504b4311247">\[\begin{gathered}
s=t/R^2,\quad z=x_2/(aR),\quad G(s,z)=F(R^2s,aRz),\\
\kappa_j=n_jaR,\quad \alpha=\kappa_1,\quad
v=BR/a,\quad\lambda=(\alpha/a)^2.
\end{gathered}\]</span> 则 <span class="math inline">\(G_s+vG_z-a^{-2}G_{zz}=0\)</span>，其 <span class="math inline">\(2q\)</span> 个复指数空间频率为 <span class="math inline">\(\pm\kappa_j\)</span>，并满足 <span class="math inline">\(\alpha\le\kappa_j\le2\alpha\)</span>。令 <span class="math display" data-source-display="display-099" data-source-sha256="48dad7604663aab2c920a48045d5f0b850050f2de6b590b49cc960aaf1d8a5dc">\[\begin{gathered}
e_a=1-\delta_0/a,\quad E_a=[-e_a,e_a],\quad
I_a=[-1-\delta/a,1+\delta/a],\\
h(s)=\int_{E_a}|G(s,z)|^3\,dz,\quad H=\int_0^4h(s)\,ds.
\end{gathered}\]</span> 由假设可知 <span class="math inline">\(e_a\ge1/2\)</span>、<span class="math inline">\(\Delta_a\le1\)</span>，且这些区间的长度具有一致的有限上界和严格正的下界。在式 <a href="#eq:ub-affine-edge" class="xref" data-ref-target="eq:ub-affine-edge">(45)</a> 中取 <span class="math inline">\(N=2q\)</span>，再应用 Hölder 不等式，得到 <span class="tex-anchor" id="eq:ub-observation" aria-hidden="true"></span><span class="math display" data-source-display="display-100" data-source-sha256="5f5a75def1789561b4c91b21cdf584ae001aa5129d624ec9ed52f2270de3ee1e">\[\begin{equation}

\|G(s)\|_{L^\infty(I_a)}^2
\le\frac{4C_Z^2}{e_a}q^2e^{\Phi_a}\int_{E_a}|G|^2
\le Cq^2e^{\Phi_a}h(s)^{2/3}.
\end{equation}\]</span><span class="equation-numbers">(52)</span></p>
```

### P78

```html
<p>余下论证将用到以下两个文献中的估计。Erdélyi 的 Markov 不等式 <span class="citation" data-cites="Erdelyi2017">(<a href="#ref-Erdelyi2017" role="doc-biblioref">Erdélyi 2017</a>, Theorem 9.1, arXiv v1)</span> 表明：对于定义在 <span class="math inline">\([0,1]\)</span> 上的 <span class="math inline">\(f(x)=\sum_{r=1}^N
c_re^{i\mu_rx}\)</span>，若各频率满足 <span class="math inline">\(\mu_r\in\mathbb
R\)</span>，则 <span class="tex-anchor" id="eq:ub-markov-input" aria-hidden="true"></span><span class="math display" data-source-display="display-101" data-source-sha256="3b76c3897f5e1680f4172465c65eab80f1a043567a97229808d1aa8f0002d2ce">\[\begin{equation}

\|f'\|_\infty\le C
       \left(N^5+\sum_{r=1}^N\mu_r^2\right)^{1/2}\|f\|_\infty.
\end{equation}\]</span><span class="equation-numbers">(53)</span> 该文给出的更精确因子为 <span class="math inline">\((1+\varepsilon_N)(108N^5+\sum_r\mu_r^2)^{1/2}\)</span>，其中 <span class="math inline">\(1+\varepsilon_N\)</span> 一致有界。Kós 的端点不等式 <span class="citation" data-cites="Kos2008">(<a href="#ref-Kos2008" role="doc-biblioref">Kós 2008</a>)</span> 亦列于 Erdélyi 论文的式 (1.2)，其内容为 <span class="tex-anchor" id="eq:ub-kos-input" aria-hidden="true"></span><span class="math display" data-source-display="display-102" data-source-sha256="ca781feaeefc2ae8fdc79fa70f29e949f3f4fa67ac5efeb64b692bc3d6d040c2">\[\begin{equation}

|f(0)|\le2N\|f\|_{L^2(0,1)},\qquad
f(r)=\sum_{j=1}^N c_je^{\gamma_jr},\quad
\operatorname{Re}\gamma_j\ge0.
\end{equation}\]</span><span class="equation-numbers">(54)</span></p>
```

### P79

```html
<p>在式 <a href="#eq:ub-markov-input" class="xref" data-ref-target="eq:ub-markov-input">(53)</a> 中，将 <span class="math inline">\(I_a\)</span> 仿射映射到 <span class="math inline">\([0,1]\)</span>。该区间长度有上界和严格正的下界，且 <span class="math inline">\(\sum_j(\kappa_j^2+(-\kappa_j)^2)\le8q\alpha^2\)</span>。结合式 <a href="#eq:ub-observation" class="xref" data-ref-target="eq:ub-observation">(52)</a>，得到 <span class="tex-anchor" id="eq:ub-derivative" aria-hidden="true"></span><span class="math display" data-source-display="display-103" data-source-sha256="b78b223633fc06df986c9508c12bbe6746478c28e4168517b1ab40d83da85794">\[\begin{equation}

\|G_z(s)\|_{L^\infty(I_a)}^2
\le C(q^7+q^3\alpha^2)e^{\Phi_a}h(s)^{2/3}.
\end{equation}\]</span><span class="equation-numbers">(55)</span> 固定 <span class="math inline">\(z\)</span> 后，函数 <span class="math inline">\(r\mapsto G(4-r,z)\)</span>（<span class="math inline">\(0\le r\le1\)</span>）至多包含 <span class="math inline">\(2q\)</span> 个指数项，指数为 <span class="math inline">\((\kappa_j/a)^2\pm iv\kappa_j\)</span>。应用式 <a href="#eq:ub-kos-input" class="xref" data-ref-target="eq:ub-kos-input">(54)</a>，取三次幂，再在单位区间上使用 Hölder 不等式，得到 <span class="tex-anchor" id="eq:ub-endpoint" aria-hidden="true"></span><span class="math display" data-source-display="display-104" data-source-sha256="d48e2b3d8ceff0f673ed0a4c9cee579f70f1c8272e4f57d19a62c766e69e58f1">\[\begin{equation}

h(4)\le64q^3\int_3^4h(s)\,ds\le64q^3H,
\qquad h(4)^{2/3}\le16q^2H^{2/3}.
\end{equation}\]</span><span class="equation-numbers">(56)</span></p>
```

### P80

```html
<p>径向几何可以精确计算。在 <span class="math inline">\(y=x_2\)</span> 处，截断函数的横截面积分为 <span class="math inline">\(2\pi\int_{|y|}^\infty
r\vartheta(r/R-a)\,dr\)</span>。对 <span class="math inline">\(y\)</span> 求导得到 <span class="math display" data-source-display="display-105" data-source-sha256="f662506f6cfce8872129ab2a17ef2648172393b51964c1ba0bcd2959ec38a0f6">\[\int_{\mathbb
T^2}\partial_2\xi_{a,R}(x_1,y,x_3)\,dx_1\,dx_3
=-2\pi y\vartheta(|y|/R-a).\]</span> 因此，令 <span class="math display" data-source-display="display-106" data-source-sha256="c6ec24509077c910c4772a720a5dc61be8528294f9f98624ca7db53674d6d6e3">\[W_a(z)=-2\pi az\vartheta(a(|z|-1)),\qquad
\Xi_a(z)=\int_{-\infty}^zW_a(r)\,dr,\]</span> 可将通量精确改写为 <span class="tex-anchor" id="eq:ub-flux-conversion" aria-hidden="true"></span><span class="math display" data-source-display="display-107" data-source-sha256="187046321b45c4cbb6f5326a9b4dd886b5b2d13f78e6811d2ff99618cee59920">\[\begin{equation}

\mathcal T_{\boldsymbol n,R}
=\frac{a^2R^3}{2}\,v\int_0^4\eta(s)
                         \int_{\mathbb R}W_a(z)G(s,z)^2\,dz\,ds.
\end{equation}\]</span><span class="equation-numbers">(57)</span> 函数 <span class="math inline">\(W_a\)</span> 是奇函数，且积分为零。其支集由两个长度均为 <span class="math inline">\(O(a^{-1})\)</span> 的区间组成，在支集上有 <span class="math inline">\(|W_a|\le Ca\)</span>。因而 <span class="tex-anchor" id="eq:ub-kernel-bounds" aria-hidden="true"></span><span class="math display" data-source-display="display-108" data-source-sha256="c1aaf734b28b9935b5ce49898f8db330b04d20f4b6e2c13dc6c303dd65015dfb">\[\begin{equation}

\operatorname{supp}\Xi_a\subset I_a,\qquad
\|\Xi_a\|_1+\|\Xi_a\|_\infty\le C,\qquad
\|\Xi_a''\|_1=\|W_a'\|_1\le Ca.
\end{equation}\]</span><span class="equation-numbers">(58)</span> 这些界可以直接通过在支集上对 <span class="math inline">\(W_a\)</span> 求导得到；该支集与 <span class="math inline">\(z=0\)</span> 保持正距离。</p>
```

### P81

```html
<p>令 <span class="math inline">\(\mathcal E(s)=\int_{\mathbb
R}\Xi_a(z)G(s,z)^2\,dz\)</span>。将方程 <span class="math inline">\((G^2)_s+v(G^2)_z-a^{-2}(G^2)_{zz}=-2a^{-2}|G_z|^2\)</span> 乘以 <span class="math inline">\(\Xi_a\)</span>，再对空间和时间积分，得到 <span class="tex-anchor" id="eq:ub-energy" aria-hidden="true"></span><span class="math display" data-source-display="display-109" data-source-sha256="9d175e37022119ca1ecb7273d575118b286c93a5e060760c4eba3e81bd8eafa0">\[\begin{align}
v\int_0^4\eta\int W_aG^2
&amp;=\eta(4)\mathcal E(4)-\int_0^4\eta'\mathcal E\,ds
\nonumber\\
&amp;\quad-a^{-2}\int_0^4\eta\int\Xi_a''G^2
       +2a^{-2}\int_0^4\eta\int\Xi_a|G_z|^2.

\end{align}\]</span><span class="equation-numbers">(59)</span> 由于 <span class="math inline">\(\eta(0)=0\)</span>，没有初始时刻的边界项。利用式 <a href="#eq:ub-observation" class="xref" data-ref-target="eq:ub-observation">(52)</a>、<a href="#eq:ub-endpoint" class="xref" data-ref-target="eq:ub-endpoint">(56)</a> 和 <a href="#eq:ub-kernel-bounds" class="xref" data-ref-target="eq:ub-kernel-bounds">(58)</a>，右端前三项的绝对值之和至多为 <span class="tex-anchor" id="eq:ub-first-rows" aria-hidden="true"></span><span class="math display" data-source-display="display-110" data-source-sha256="3543e640f2ab90c33b8883a132c073a559e37c1232440266674ddd77748daeb9">\[\begin{equation}

C(q^4+q^2+a^{-1}q^2)e^{\Phi_a}H^{2/3}.
\end{equation}\]</span><span class="equation-numbers">(60)</span> 这里使用了 <span class="math inline">\(\int_0^4h^{2/3}\le4^{1/3}H^{2/3}\)</span>。由式 <a href="#eq:ub-derivative" class="xref" data-ref-target="eq:ub-derivative">(55)</a>，最后一项可估计为 <span class="math display" data-source-display="display-111" data-source-sha256="2b5c6bd8b1b5d1f4b65ac9224fb6760d7930495d423321384da6c59fc72e8568">\[Ce^{\Phi_a}\left[
       \frac{q^7}{a^2}\int_0^4\eta h^{2/3}\,ds
       +q^3\lambda\int_0^4\eta h^{2/3}\,ds\right].\]</span> 方括号内的第一项至多为 <span class="math inline">\(Cq^7a^{-2}H^{2/3}\)</span>。若 <span class="math inline">\(\lambda\le1\)</span>，则 Hölder 不等式将第二项控制在 <span class="math inline">\(Cq^3H^{2/3}\)</span> 以内。若 <span class="math inline">\(\lambda&gt;1\)</span>，则 <span class="math inline">\(G\)</span> 的时间衰减指数的实部位于 <span class="math inline">\([\lambda,4\lambda]\)</span>，并且 <span class="math inline">\(\eta(s)\le\|\eta'\|_\infty s\)</span>。在式 <a href="#eq:ub-cutoff-time" class="xref" data-ref-target="eq:ub-cutoff-time">(65)</a> 中取 <span class="math inline">\(N\le2q\)</span>，可将该项控制在 <span class="math inline">\(Cq^{13/3}\lambda^{-1/3}H^{2/3}\le
Cq^{13/3}H^{2/3}\)</span> 以内。将这些估计与式 <a href="#eq:ub-energy" class="xref" data-ref-target="eq:ub-energy">(59)</a> 结合，得到 <span class="tex-anchor" id="eq:ub-scaled-bound" aria-hidden="true"></span><span class="math display" data-source-display="display-112" data-source-sha256="29896b53c9d8d7b298ec122cf1aa85e224d52fb885d30a99478ec81c89cc2c16">\[\begin{equation}

\left|v\int_0^4\eta\int W_aG^2\right|
\le C\left(q^4+\frac{q^7}{a^2}+q^{13/3}\right)
                  e^{\Phi_a}H^{2/3}.
\end{equation}\]</span><span class="equation-numbers">(61)</span></p>
```

### P82

```html
<p>最后，在 <span class="math inline">\(x_2=aRz\)</span> 处的平台横截面积除以 <span class="math inline">\(R^2\)</span> 后等于 <span class="math display" data-source-display="display-113" data-source-sha256="ba40fd7be86b80fa64daf720d5e0e6ff6586e19fd60a96524520e00e660a04be">\[\pi\left(
[(a+\delta_0)^2-a^2z^2]_+
-[(a-\delta_0)^2-a^2z^2]_+\right).\]</span> 当 <span class="math inline">\(z\in E_a\)</span> 时，该表达式精确等于 <span class="math inline">\(4\pi a\delta_0\)</span>。由于 <span class="math inline">\(dt\,dx_2=aR^3\,ds\,dz\)</span>，得到 <span class="tex-anchor" id="eq:ub-mass-conversion" aria-hidden="true"></span><span class="math display" data-source-display="display-114" data-source-sha256="9cd06d683cf981dc8b73869fc4140f65237f48b03af9088107d4aa7e17ee653c">\[\begin{equation}

M^{\rm plat}_{\boldsymbol n,R}\ge4\pi\delta_0a^2R^5H.
\end{equation}\]</span><span class="equation-numbers">(62)</span> 式 <a href="#eq:ub-flux-conversion" class="xref" data-ref-target="eq:ub-flux-conversion">(57)</a>、<a href="#eq:ub-scaled-bound" class="xref" data-ref-target="eq:ub-scaled-bound">(61)</a> 和 <a href="#eq:ub-mass-conversion" class="xref" data-ref-target="eq:ub-mass-conversion">(62)</a> 共同给出式 <a href="#eq:ub-main-refined" class="xref" data-ref-target="eq:ub-main-refined">(50)</a>。由于 <span class="math inline">\(a,q\ge1\)</span>，有 <span class="math inline">\(q^4+q^7/a^2+q^{13/3}\le3q^7\)</span>，从而得到式 <a href="#eq:ub-main" class="xref" data-ref-target="eq:ub-main">(51)</a>。◻</p>
```

### P83

```html
<p class="remark" data-source-block="remark-29" data-source-sha256="9937ae59ba07fea744fa35d5a2e7d552ca1fd2bb455b65b1e4d0550be3608b1b"><span class="tex-anchor" id="rem:ub-window" aria-hidden="true"></span><strong>注 6.3（间隙收缩的参数区间）</strong> 令 <span class="math inline">\(a=pL\)</span>，其中 <span class="math inline">\(p&gt;0\)</span> 固定；再令 <span class="math inline">\(\omega=\exp(-\gamma L^2)\)</span>，其中 <span class="math inline">\(\gamma&gt;0\)</span> 固定。定义 <span class="math inline">\(P=R^{-2}\omega M^{\rm plat}_{\boldsymbol
n,R}\)</span> 和 <span class="math inline">\(X=(\omega/R)[\mathcal
T_{\boldsymbol n,R}]_+\)</span>。式 <a href="#eq:ub-main" class="xref" data-ref-target="eq:ub-main">(51)</a> 化为 <span class="math display" data-source-display="display-115" data-source-sha256="7986633600d5643be2fb95fe0e971beaa2f49b8916e47256afa9eb4d38451286">\[X\le C
a^{2/3}q^7\omega^{1/3}e^{12\sqrt2q\sqrt{\Delta_a}}P^{2/3}.\]</span> 若 <span class="math inline">\(q=q(L)=o(L^{5/2})\)</span>，则 <span class="math inline">\(\Delta_a=O(L^{-1})\)</span>，并且 <span class="math display" data-source-display="display-116" data-source-sha256="bef7879981f6dfaf0e051e3ca711a07ecd1d1fc9c906049785e1d47e7986c7b1">\[\lim_{L\to\infty}\frac1{L^2}
   \log\left(Ca^{2/3}q(L)^7\omega^{1/3}
                   e^{12\sqrt2q(L)\sqrt{\Delta_a}}\right)
=-\frac\gamma3.\]</span> 这是所证明的上界系数的对数渐近率，并不声称某个具体通量达到该渐近率。对于归一化参数 <span class="math inline">\(\gamma=2/3969\)</span>，该渐近率为 <span class="math inline">\(-2/11907\)</span>。</p>
```

## 精确替换：第 7 节

### P84

```html
<p>定量边缘判据要求外部剖面为正、两侧具有全局包络、内部具有控制界，并且在一个固定的鞍点邻域内具有下界。归一化的第一类和第二类切比雪夫族满足这些假设。所得误差阶足以支持结论，但尚不知是否最优。该判据并未证明任意参数下的 Jacobi 定理，也不覆盖 <span class="math inline">\(\mu/A\)</span> 与零保持正距离的次数范围。</p>
```

### P85

```html
<p>固定初始数据的剪切流下界与二进频带上的一致上界具有不同的量词。该下界并未逐一匹配上界系数中的所有多项式因子或指数因子。对于相同观测量和相同函数类，建立相匹配的动态上界与下界仍是未解决的问题。抽象时间不等式的最优阶 <span class="math inline">\(N^{4/3}\)</span> 并未解决这个带有空间约束的问题。若将有符号通量改为逐点绝对值的积分，也会改变观测量及其相消论证。</p>
```

### P86

```html
<p>原始振幅下的完整速度商、通过大幅度振幅缩放恢复该商的结论，以及有界漂移估计，都针对明确指定的剪切流族。沿主序列，漂移和环面上的能量不必有界。向平面空间的延拓通常具有无限总能量。本文并未建立一致能量类、极限弱解、涡拉伸机制，或适用于任意三维 Navier–Stokes 初始数据的判据。可选归一化中的常数 <span class="math inline">\(-2/11907\)</span> 来自所选外部权重的指数，而不是普适的动力学常数。</p>
```

### P87

```html
<p>特殊函数文献比较核查了具体的第一手来源及其参数范围。它并非穷尽性的优先权检索；可能仍存在更一般的终止超几何结果。本文不提出超出第 <a href="#sec:literature" class="xref" data-ref-target="sec:literature">3</a> 节显式比较范围的优先权主张。</p>
```

### P88

```html
<p>OpenAI Codex 协助了草稿撰写、文献检索、证明组织、精确有限代数核查及验证脚本编写。本文给出了定理证明，并对所引用的不等式列明假设、注明来源。另行开展的自动审查核查了新的定量定理、归一化论证和时间不等式的阶证明；这些审查不属于人类同行评审，也不是形式化证明助手的认证。作者对稿件承担责任。有限计算检验的是恒等式及选定参数，并非对连续极限渐近断言的验证。</p>
```

### P89

```html
<p>辅助文件包含精确有限代数核查，以及图 <a href="#fig:edge-diagnostic" class="xref" data-ref-target="fig:edge-diagnostic">1</a> 的代码、参数、数据和参考 SVG。文件 <code>anc/README.md</code> 列出了运行命令及依赖项。这些可复现材料是对证明的补充；有限核查和数值求积诊断不能认证连续极限。</p>
```

## 精确替换：附录 A

### P90

```html
<p><strong>推论 A.1（由 Erdélyi 结果导出的时间加权衰减）</strong> 设 <span class="math inline">\((E,\nu)\)</span> 为测度空间，<span class="math inline">\(N\ge1\)</span>，且 <span class="math inline">\(\zeta_j\in\mathbb C\)</span> 满足 <span class="math inline">\(\operatorname{Re}\zeta_j\ge1\)</span>。对可测、取有限值的系数，定义 <span class="math display" data-source-display="display-117" data-source-sha256="ca31294948e6f92626e302c30797f0a78218913a5e70591601e9908c12d7b243">\[f(t,z)=\sum_{j=1}^N c_j(z)e^{-\zeta_jt},\quad
k(t)=\int_E|f(t,z)|^3\,d\nu(z),\quad K_T=\int_0^Tk(t)\,dt.\]</span> 若 <span class="math inline">\(T&gt;0\)</span> 且 <span class="math inline">\(K_T&lt;\infty\)</span>，则 <span class="tex-anchor" id="eq:ub-delay" aria-hidden="true"></span><span class="math display" data-source-display="display-118" data-source-sha256="65ad685f332608c1d0d55e34bed5c608f3dca6927f93db50121c130b558ddf7f">\[\begin{equation}

\int_0^Tt\,k(t)^{2/3}\,dt\le C_*N^{4/3}K_T^{2/3},
\qquad C_*=4^{-1/3}36^{4/3}+1.
\end{equation}\]</span><span class="equation-numbers">(63)</span> 无需对实部另设上界，也无需假设虚部有界。</p>
```

### P91

```html
<p><em>证明。</em> 合并重合的指数；由单调性可得采用原始项数 <span class="math inline">\(N\)</span> 的估计。Erdélyi 的无限区间–有限区间定理 <span class="citation" data-cites="Erdelyi2017">(<a href="#ref-Erdelyi2017" role="doc-biblioref">Erdélyi 2017</a>, Theorem 3.1, arXiv v1)</span> 适用于指数实部非正的复指数和。将其应用于 <span class="math inline">\(e^tf(t,z)\)</span>，得到 <span class="math display" data-source-display="display-119" data-source-sha256="180d8cb76fef161cd824d01b6b85b7d734829586dc59fa5c99e1959cd0234b3e">\[J(z):=\int_0^\infty e^t|f(t,z)|^2\,dt
\le8191\int_0^{9N}e^t|f(t,z)|^2\,dt
\le8191e^{9N}I_{9N}(z),\]</span> 其中 <span class="math inline">\(I_b(z)=\int_0^b|f(t,z)|^2\,dt\)</span>。由于系数均取有限值，且衰减率的实部至少为 1，这些积分逐点有限。在长度为 2 的区间上，对 <span class="math inline">\(e^{t/2}f(t,z)\)</span> 应用中点估计 <span class="citation" data-cites="Erdelyi2017">(<a href="#ref-Erdelyi2017" role="doc-biblioref">Erdélyi 2017</a>, Lemma
12.5, arXiv v1)</span>，当 <span class="math inline">\(t\ge1\)</span> 时得到 <span class="math display" data-source-display="display-120" data-source-sha256="b846838a7226d49be5f67b8ccd0ae0621674a0fc785795df153a1406391726e8">\[e^t|f(t,z)|^2\le
N\int_{t-1}^{t+1}e^u|f(u,z)|^2\,du\le NJ(z).\]</span> 因此 <span class="math inline">\(|f(t,z)|^2\le8191Ne^{9N-t}I_{9N}(z)\)</span>。这一中点估计允许任意复指数。</p>
```

### P92

```html
<p>取 <span class="math inline">\(S=36N\)</span>。若 <span class="math inline">\(T\ge S\)</span>，Minkowski 不等式和 Hölder 不等式给出 <span class="math display" data-source-display="display-121" data-source-sha256="9240b5a97830e5eaa53ef6dffafb18907763b067d772d08b04f47266a8ddf2b5">\[\|I_{9N}\|_{L^{3/2}(E)}
\le\int_0^{9N}k(t)^{2/3}\,dt
\le(9N)^{1/3}K_T^{2/3}.\]</span> 因而，<span class="math inline">\([S,T]\)</span> 上的积分至多为 <span class="math display" data-source-display="display-122" data-source-sha256="89e940aadb903cffda1bf54ebef850844c5b88529d628dc3b539fab108ae7bc1">\[8191N(9N)^{1/3}(36N+1)e^{-27N}K_T^{2/3}
\le N^{4/3}K_T^{2/3}.\]</span> 最后一个不等式利用了：在 <span class="math inline">\(N\ge1\)</span> 的范围内，<span class="math inline">\((36N+1)e^{-27N}\)</span> 随项数增大而减小，且 <span class="math inline">\(8191\,9^{1/3}37e^{-27}&lt;1\)</span>。无论是 <span class="math inline">\(T\ge S\)</span> 还是 <span class="math inline">\(T&lt;S\)</span>，初始部分均满足 <span class="math display" data-source-display="display-123" data-source-sha256="cf156b9be8563c0b3b81aa015360128c70bd64f03181c01aed87c7ea72235e36">\[\int_0^{\min(T,S)}t k(t)^{2/3}\,dt
\le\left(\int_0^S t^3\,dt\right)^{1/3}K_T^{2/3}
=4^{-1/3}(36N)^{4/3}K_T^{2/3}.\]</span> 由此证明了结论，也包括 <span class="math inline">\(K_T=0\)</span> 的情形。◻</p>
```

### P93

```html
<p><strong>命题 A.2（阶的显式见证）</strong> 对每个 <span class="math inline">\(N\ge1\)</span>，都存在恰含 <span class="math inline">\(N\)</span> 个非零项的实指数和，全部衰减率均位于 <span class="math inline">\([1,5/4]\)</span>，使得在单点空间上取 <span class="math inline">\(T=N\)</span> 时有 <span class="tex-anchor" id="eq:time-order" aria-hidden="true"></span><span class="math display" data-source-display="display-124" data-source-sha256="d8d83f9770bc4035cce1ca79b7d06e5dfc0ecbd46fa08010990a31b74c7651ba">\[\begin{equation}

\frac{\int_0^N t f_N(t)^2\,dt}
{\left(\int_0^N f_N(t)^3\,dt\right)^{2/3}}
\ge\frac{N^{4/3}}{128}.
\end{equation}\]</span><span class="equation-numbers">(64)</span> 因此，在式 <a href="#eq:ub-delay" class="xref" data-ref-target="eq:ub-delay">(63)</a> 所对应的抽象函数类中，其 <span class="math inline">\(N^{4/3}\)</span> 阶不能替换为 <span class="math inline">\(o(N^{4/3})\)</span>。</p>
```

### P94

```html
<p><em>证明。</em> 令 <span class="math inline">\(\epsilon=N^{-2}\)</span>、<span class="math inline">\(w(t)=(1-e^{-\epsilon t})/\epsilon\)</span>，以及 <span class="math display" data-source-display="display-125" data-source-sha256="429719752eb45d2e83eadbb2fa5b508f30eea79715752924750cf54f98282bc3">\[f_N(t)=e^{-t}\sum_{k=0}^{N-1}\frac{w(t)^k}{k!}
       =\sum_{j=0}^{N-1}b_je^{-(1+j\epsilon)t},\qquad
b_j=\frac{(-1)^j}{j!\epsilon^j}
      \sum_{h=0}^{N-1-j}\frac1{\epsilon^h h!}.\]</span> 系数恒等式由二项式定理得到，且内层求和的各项均为正。因此，每个系数都满足 <span class="math inline">\(b_j\ne0\)</span>；又因为 <span class="math inline">\((N-1)/N^2\le1/4\)</span>，这些互异衰减率均位于 <span class="math inline">\([1,5/4]\)</span>。记 <span class="math inline">\(f_{0,N}(u)=e^{-u}\sum_{k=0}^{N-1}u^k/k!\)</span>。它等于均值为 <span class="math inline">\(u\)</span> 的泊松随机变量小于 <span class="math inline">\(N\)</span> 的概率，也等价于初等的不完全伽马恒等式 <span class="citation" data-cites="DLMF">(<a href="#ref-DLMF" role="doc-biblioref">National Institute of Standards
and Technology n.d., sec. 8.4.11</a>)</span>。当 <span class="math inline">\(0\le t\le N/2\)</span> 时，有 <span class="math display" data-source-display="display-126" data-source-sha256="dee40918c3280f49363ef3a6ee952de01dc5cdc3079f09fc182d1909e83e8e17">\[0\le w(t)\le t,\qquad t-w(t)\le\epsilon
t^2/2\le1/8,
\qquad f_{0,N}(w(t))\ge1-w(t)/N\ge\tfrac12.\]</span> 中间的不等式由积分 <span class="math inline">\(1-e^{-\epsilon u}\le\epsilon u\)</span> 得到；最后一个不等式是概率论中的 Markov 不等式。因此，在该区间上有 <span class="math inline">\(f_N(t)=e^{-(t-w(t))}f_{0,N}(w(t))\ge\tfrac12e^{-1/8}&gt;1/4\)</span>。对所有 <span class="math inline">\(t\ge0\)</span>，都有 <span class="math inline">\(0&lt;f_N(t)\le f_{0,N}(t)\le1\)</span>。于是 <span class="math inline">\(K_N=\int_0^N f_N^3\,dt\)</span> 位于 <span class="math inline">\((0,N]\)</span>，并且 <span class="math display" data-source-display="display-127" data-source-sha256="c922e8d9df6959f0f504b6d098e2ef17565f77262a2a60cb03c6fb918f106083">\[\int_0^N t
f_N^2\,dt\ge\frac1{16}\int_0^{N/2}t\,dt
=\frac{N^2}{128}.\]</span> 两者相除即得式 <a href="#eq:time-order" class="xref" data-ref-target="eq:time-order">(64)</a>。上述论证也包含 <span class="math inline">\(N=1\)</span> 的情形：此时 <span class="math inline">\(b_0=1\)</span>，且 <span class="math inline">\(f_1=e^{-t}\)</span>。如需将三次质量归一化为 1，可将 <span class="math inline">\(f_N\)</span> 替换为 <span class="math inline">\(K_N^{-1/3}f_N\)</span>；该商保持不变。◻</p>
```

### P95

```html
<p>这一初等构造针对抽象的时间范数商。其中彼此接近的实衰减率不必是剪切流整数频率的平方，也没有与之对应的空间约束。因此，它既不证明 <span class="math inline">\(q^7\)</span> 通量系数的最优性，也不确定最优指数常数或动力学转变。上界估计是已有文献结果的直接推论；本文不对这个阶见证提出优先权主张。</p>
```

### P96

```html
<p>为便于后续应用，若 <span class="math inline">\(G(s,z)\)</span> 的时间衰减率的实部至少为 <span class="math inline">\(\lambda&gt;0\)</span>，记 <span class="math inline">\(h(s)=\int_E|G(s,z)|^3\,d\nu\)</span>、<span class="math inline">\(H=\int_0^4h(s)\,ds\)</span>。当 <span class="math inline">\(0\le\eta(s)\le C_\eta s\)</span> 时，通过变量代换 <span class="math inline">\(t=\lambda s\)</span> 得到 <span class="tex-anchor" id="eq:ub-cutoff-time" aria-hidden="true"></span><span class="math display" data-source-display="display-128" data-source-sha256="5d1d61fba8d8a4747ce52e77d9e3020efdfa1dac7261946b62daf29f45816d06">\[\begin{equation}

\lambda\int_0^4\eta(s)h(s)^{2/3}\,ds
\le C_* C_\eta N^{4/3}\lambda^{-1/3}H^{2/3}.
\end{equation}\]</span><span class="equation-numbers">(65)</span></p>
```

## 精确替换：附录 B

### P97

```html
<p>本附录记录所需的空间结论及其来源。近边缘尺度与切比雪夫汇合构造属于已有工作 <span class="citation" data-cites="Zhang2026">(<a href="#ref-Zhang2026" role="doc-biblioref">Zhang 2026</a>, Propositions
7.1 and 8.4)</span>；Erdélyi 的工作中也出现了多项式端点见证 <span class="citation" data-cites="Erdelyi2017">(<a href="#ref-Erdelyi2017" role="doc-biblioref">Erdélyi 2017</a>)</span>。下面的初等改动使构造取实值，并将频率限制在一个二进频带内；它们不是另外的新外推定理。这里的所有范数均采用 <span class="math inline">\([-1,1]\)</span> 上的勒贝格测度。</p>
```

### P98

```html
<p><strong>引理 B.1（系数恒等式）</strong> 对次数为 <span class="math inline">\(n\)</span> 的实系数多项式 <span class="math inline">\(p\)</span> 及 <span class="math inline">\(\eta&gt;0\)</span>，有 <span class="tex-anchor" id="eq:confluent-map" aria-hidden="true"></span><span class="math display" data-source-display="display-129" data-source-sha256="03ce767a5d0c15c5a59ab391467bb9dcc7b5059190ba9502cbc4b65cbc082ae3">\[\begin{equation}

p\left(\frac{e^{i\eta x}-1}{i\eta}\right)
=\sum_{j=0}^n b_j(\eta)e^{ij\eta x},\qquad
b_j(\eta)=\frac{p^{(j)}(i/\eta)}{j!(i\eta)^j}.
\end{equation}\]</span><span class="equation-numbers">(66)</span> 若 <span class="math inline">\(p\)</span> 的所有根均为实数，则对每个 <span class="math inline">\(\eta&gt;0\)</span>，所有 <span class="math inline">\(b_j\)</span> 都非零。固定一个全实根多项式 <span class="math inline">\(p\)</span>、<span class="math inline">\(M&gt;0\)</span> 及实数 <span class="math inline">\(\theta\)</span>；将上述表达式乘以 <span class="math inline">\(e^{i(Mx+\theta)}\)</span> 后取实部的两倍。当 <span class="math inline">\(n\eta\le M\)</span> 时，所得实函数恰有 <span class="math inline">\(n+1\)</span> 个位于 <span class="math inline">\([M,2M]\)</span> 内的正频率；当 <span class="math inline">\(\eta\downarrow0\)</span> 时，它局部一致收敛于 <span class="math inline">\(2p(x)\cos(Mx+\theta)\)</span>。</p>
```

### P99

```html
<p><em>证明。</em> 利用 <span class="math inline">\(w_\eta(x)=i/\eta+e^{i\eta x}/(i\eta)\)</span>，将 <span class="math inline">\(p\)</span> 在 <span class="math inline">\(i/\eta\)</span> 处展开。由 Rolle 定理，每个非常数导数的零点均为实数，因此它在 <span class="math inline">\(i/\eta\)</span> 处不为零。最高阶导数为非零常数。取实值后，正频率为 <span class="math inline">\(M+j\eta\)</span>，对应振幅为 <span class="math inline">\(2|b_j|\)</span>。最后，<span class="math inline">\(|w_\eta(x)-x|\le\eta x^2/2\)</span> 给出紧集上的一致收敛。允许任意相位意味着正振幅并不排除相消：符号可以吸收到相位之中。◻</p>
```

### P100

```html
<p><strong>命题 B.2（实值频带内保留的已知空间阶）</strong> 设 <span class="math inline">\(\mathcal R_q^{\rm
dyad}\)</span> 由实余弦和组成，每个和恰有 <span class="math inline">\(q\ge2\)</span> 个位于同一个二进频带内的正频率，振幅非零，相位任意。对于 <span class="math inline">\(0&lt;d\le1\)</span>，有 <span class="math display" data-source-display="display-130" data-source-sha256="d08c8fed5318a5a0ce47ed982f2564ad1dcc527a77eacbefb03ac31e9a1e2dc8">\[\begin{align*}
\sup_{g\in\mathcal R_q^{\rm dyad}}
\frac{|g(1+d)|}{\|g\|_2}
&amp;\ge\frac{e^{(q-1)\operatorname{arcosh}(1+d)}}{2\sqrt2},\\
\sup_{g\in\mathcal R_q^{\rm dyad}}
\frac{\int_1^{1+d}|g|^2}{\|g\|_r^2}
&amp;\ge\frac d{128}e^{2(q-1)\sqrt{7d/8}},\qquad r=2,3,\\
\sup_{g\in\mathcal R_q^{\rm dyad}}\frac{|g(1)|}{\|g\|_2}
&amp;\ge q/\sqrt2,\qquad
\sup_{g\in\mathcal R_q^{\rm dyad}}\frac{|g(1)|}{\|g\|_3}
\ge2^{-1/3}q^{2/3}.
\end{align*}\]</span> 这些是沿汇合序列得到的上确界结论。</p>
```

### P101

```html
<p><em>证明。</em> 对于外部估计，在引理 <a href="#lem:confluent-real-rooted" class="xref" data-ref-target="lem:confluent-real-rooted">B.1</a> 中取 <span class="math inline">\(p=T_{q-1}\)</span>、<span class="math inline">\(M=1\)</span>、<span class="math inline">\(\theta=-(1+d)\)</span>。极限函数为 <span class="math inline">\(g_0=2T_{q-1}(x)\cos(x-1-d)\)</span>，并满足 <span class="math inline">\(\|g_0\|_2^2\le8\)</span> 和 <span class="math inline">\(\|g_0\|_3^3\le16\)</span>。在 <span class="math inline">\(1+d\)</span> 处，载波因子等于 1，且 <span class="math inline">\(T_{q-1}(1+d)\ge\tfrac12e^{(q-1)\operatorname{arcosh}(1+d)}\)</span>。在区间 <span class="math inline">\([1+7d/8,1+d]\)</span> 上，载波因子的平方至少为 <span class="math inline">\(1/2\)</span>，而 <span class="math inline">\(T_{q-1}\)</span> 单调递增。利用 <span class="math inline">\(0\le x\le1\)</span> 时成立的 <span class="math inline">\(\operatorname{arcosh}(1+x)\ge\sqrt x\)</span>，外部平方积分至少为 <span class="math inline">\((d/16)e^{2(q-1)\sqrt{7d/8}}\)</span>。紧集上的一致收敛将这两个比值传递到汇合序列。</p>
```

### P102

```html
<p>对于端点，取经典的 Legendre 核 <span class="math inline">\(K_{q-1}(x)=\sum_{r=0}^{q-1}(2r+1)P_r(x)/2\)</span>。正交性给出 <span class="math inline">\(K_{q-1}(1)=\|K_{q-1}\|_2^2=q^2/2\)</span>；由 <span class="math inline">\(|P_r|\le1\)</span> 得到 <span class="math inline">\(\|K_{q-1}\|_3^3\le q^4/4\)</span>。该核的所有零点均为位于 <span class="math inline">\((-1,1)\)</span> 内的单根：由于 <span class="math inline">\(\int K_{q-1}r=r(1)\)</span>，它关于正权重 <span class="math inline">\(1-x\)</span> 与所有次数更低的多项式正交。若这类根的数量少于 <span class="math inline">\(q-1\)</span>，将其变号因子相乘即可得到通常的矛盾。取 <span class="math inline">\(M=1\)</span>、<span class="math inline">\(\theta=-1\)</span>，应用系数引理。载波因子在观测端点等于 1，且乘上该因子不会增大任一范数，从而得到最后两个不等式。◻</p>
```

### P103

```html
<p>这里，将 <span class="math inline">\(L^3\)</span> 端点比值平方后所得的下界幂次为 <span class="math inline">\(q^{4/3}\)</span>。这并未证明端点的最优幂次：Erdélyi 的 <span class="math inline">\(L^p\)</span> 估计 <span class="citation" data-cites="Erdelyi2017">(<a href="#ref-Erdelyi2017" role="doc-biblioref">Erdélyi 2017</a>, Theorem 2.10, arXiv v1)</span> 在 <span class="math inline">\(p=3\)</span> 时，对 <span class="math inline">\(2q\)</span> 个复指数分支计数，给出的平方比值上界幂次为 <span class="math inline">\(q^{5/3}\)</span>。</p>
```

### P104

```html
<p><strong>命题 B.3（指定时刻的整数频率实现）</strong> 设 <span class="math inline">\(p\)</span> 是次数为 <span class="math inline">\(q-1\)</span> 的全实根多项式，取 <span class="math inline">\(R,A&gt;0\)</span>、<span class="math inline">\(\eta=AR\)</span>、满足 <span class="math inline">\(n_0\ge q-1\ge1\)</span> 的整数，并固定 <span class="math inline">\(s_*\ge0,B,\theta\)</span>。令 <span class="math inline">\(n_j=n_0+j\)</span>、<span class="math inline">\(a_j=2|b_j(\eta)|e^{n_j^2R^2s_*}\)</span> 及 <span class="math inline">\(\phi_j=-\theta-\arg b_j(\eta)-n_jBR^2s_*\)</span>。则精确剪切流 <span class="math inline">\(F(t,y)=\sum_j
a_je^{-n_j^2t}\cos(n_jy-\phi_j-n_jBt)\)</span> 满足 <span class="math display" data-source-display="display-131" data-source-sha256="154d49d1d06cf308271c568fd0c7b32b69282ed0974679c2add719b13bd2d91c">\[F(R^2s_*,ARx)=2\operatorname{Re}
       \{e^{i\theta+in_0\eta x}p(w_\eta(x))\}.\]</span></p>
```

### P105

```html
<p><em>证明。</em> 代入上述振幅和相位即可。每个傅里叶项满足 <span class="math inline">\(F_t+BF_y=F_{yy}\)</span>，并且 <span class="math inline">\(n_0+q-1\le2n_0\)</span>。◻</p>
```

### P106

```html
<p>最后这个命题中的系数可以依赖于 <span class="math inline">\(s_*\)</span>。因此，它不能替代第 <a href="#sec:parabolic" class="xref" data-ref-target="sec:parabolic">4</a> 节在固定初始数据下对整个时间区间进行的论证。对于所有 <span class="math inline">\(\eta&gt;0\)</span> 均非零这一结论，也不说明系数的大小或数值稳定性。</p>
```

## 精确替换：附录 C

### P107

```html
<p>本附录记录估计对外部指数归一化的依赖，并比较静态尺度与抛物型尺度。</p>
```

### P108

```html
<p><strong>推论 C.1（模态数增长边界处的充分系数）</strong> 保持定理 <a href="#thm:ub-flux" class="xref" data-ref-target="thm:ub-flux">6.2</a> 中的截断函数和常数不变。固定 <span class="math inline">\(p_0,\gamma&gt;0\)</span>，选取 <span class="math inline">\(R(L)&gt;0\)</span>，使该定理的几何假设对所有充分大的 <span class="math inline">\(L\)</span> 成立；令 <span class="math inline">\(a=p_0L\)</span>、<span class="math inline">\(\omega=\exp(-\gamma L^2)\)</span>，并采用归一化量 <span class="math display" data-source-display="display-132" data-source-sha256="ff98c2c23bf8a2ede3e2fc933aee169be773f97cc4acb841cdf6ca37de1d47fd">\[P=R^{-2}\omega M^{\rm
plat}_{\boldsymbol n,R},
\qquad X=(\omega/R)[\mathcal T_{\boldsymbol n,R}]_+.\]</span> 若 <span class="math inline">\(q(L)\ge1\)</span> 取整数值，且 <span class="math inline">\(q(L)/L^{5/2}\to\kappa\in[0,\infty)\)</span>，则不等式 <span class="math inline">\(X\le\mathcal B_LP^{2/3}\)</span> 中的系数 <span class="math display" data-source-display="display-133" data-source-sha256="b2330444947879e94dd71e25315ca00d3e03bdd556d466b1ccf8928ddc96f685">\[\mathcal B_L
=C a^{2/3}q(L)^7\omega^{1/3}
          \exp(12\sqrt2\,q(L)\sqrt{\Delta_a})\]</span> 满足 <span class="tex-anchor" id="eq:critical-rate" aria-hidden="true"></span><span class="math display" data-source-display="display-134" data-source-sha256="799c91eaeaa1e9405852b91ee36372b85049658f0a3640b225090458f074010c">\[\begin{equation}

\lim_{L\to\infty}\frac{\log\mathcal B_L}{L^2}
=-\frac{\gamma}{3}
       +12\sqrt2\,\kappa\sqrt{\frac{\delta+\delta_0}{p_0}}.
\end{equation}\]</span><span class="equation-numbers">(67)</span> 特别地，只要 <span class="tex-anchor" id="eq:critical-kappa" aria-hidden="true"></span><span class="math display" data-source-display="display-135" data-source-sha256="30844a4243ea407b4254718f81c0f414bd5d2ca8303ea1a4ca29d4417a30cce6">\[\begin{equation}

\kappa&lt;
\frac{\gamma}{36\sqrt2}
           \sqrt{\frac{p_0}{\delta+\delta_0}}.
\end{equation}\]</span><span class="equation-numbers">(68)</span>，该系数的对数除以尺度参数的平方后仍具有严格负的渐近率，因此系数衰减。若将式 <a href="#eq:critical-kappa" class="xref" data-ref-target="eq:critical-kappa">(68)</a> 中的极限值替换为相应上极限，并仍要求严格小于右端，则同样得到该衰减结论。</p>
```

### P109

```html
<p><em>证明。</em> 定理 <a href="#thm:ub-flux" class="xref" data-ref-target="thm:ub-flux">6.2</a> 中关于 <span class="math inline">\(R\)</span> 的幂次因子精确相消，给出归一化不等式：<span class="math display" data-source-display="display-136" data-source-sha256="d88c063ab98f50574dd2f3a9bdbe817de0aedfa4e6c254a78ee66e80dda6f6f0">\[\frac{\omega}{R}\,
     a^{2/3}R^{-1/3}(R^2\omega^{-1}P)^{2/3}
=a^{2/3}\omega^{1/3}P^{2/3}.\]</span> 由于 <span class="math inline">\(\Delta_a=(\delta+\delta_0)/(p_0L-\delta_0)\)</span>，有 <span class="math display" data-source-display="display-137" data-source-sha256="8a80b21a5da156feefb8418b16fee979e450a843a786d3be7b12e38dda5c55dd">\[\frac{12\sqrt2\,q(L)\sqrt{\Delta_a}}{L^2}
=12\sqrt2\,\frac{q(L)}{L^{5/2}}
       \sqrt{\frac{\delta+\delta_0}{p_0-\delta_0/L}}.\]</span> 此表达式的极限就是式 <a href="#eq:critical-rate" class="xref" data-ref-target="eq:critical-rate">(67)</a> 中的正项。<span class="math inline">\(C,a^{2/3}\)</span> 及 <span class="math inline">\(q^7\)</span> 的对数除以 <span class="math inline">\(L^2\)</span> 后均趋于零，而权重的贡献为 <span class="math inline">\(-\gamma/3\)</span>。使用上极限作同样计算，即可证明最后的断言。◻</p>
```

### P110

```html
<p>这只是已证明的上界系数衰减的一个充分参数范围。式 <a href="#eq:critical-kappa" class="xref" data-ref-target="eq:critical-kappa">(68)</a> 取等号或不满足其严格不等式，都不能据此断言实际通量发生转变。数值常数来自所引用的外推估计。附录 <a href="#sec:sharpness" class="xref" data-ref-target="sec:sharpness">B</a> 中的空间见证，并未针对这一模态数增长边界提供相匹配的时间积分下界。</p>
```

### P111

```html
<p>选取尺度参数 <span class="math inline">\(p_0=32/63\)</span>、<span class="math inline">\(\gamma=2/3969\)</span> 以及 <span class="math inline">\(R=\exp(-9L^2/40000)\)</span> 时，注 <a href="#rem:ub-window" class="xref" data-ref-target="rem:ub-window">6.3</a> 中的次临界渐近率为 <span class="math inline">\(-2/11907\)</span>。定理 <a href="#thm:parabolic-shear" class="xref" data-ref-target="thm:parabolic-shear">4.5</a> 的精确切比雪夫族在较小的参数范围 <span class="math inline">\(m=o(A^2)\)</span> 内具有相同的归一化渐近率。这两个结论的强度不同：前者给出一致上界的系数，后者则给出显式选定的构造族实际达到的渐近率。</p>
```

### P112

```html
<p>采用幂律参数化，可以清楚区分静态尺度与抛物型尺度。固定 <span class="math inline">\(1/2&lt;\sigma&lt;2\)</span>，令 <span class="math inline">\(m\)</span> 为最接近 <span class="math inline">\(A^\sigma\)</span> 的正偶整数。则 <span class="tex-anchor" id="eq:power-law-regimes" aria-hidden="true"></span><span class="math display" data-source-display="display-138" data-source-sha256="9cc44e35bfd372bab0c054800b2190b47c8bcaf0e13e5df0cdc91cc411367666">\[\begin{equation}

\frac{m}{\sqrt A}\sim A^{\sigma-1/2},\qquad
\mu\sim A^{(2\sigma-1)/3},\qquad
\mu^2\sim A^{(4\sigma-2)/3}.
\end{equation}\]</span><span class="equation-numbers">(69)</span> 第一个尺度描述静态边缘增益的对数；第二个尺度描述完整时间区间商中依赖边缘的指数因子，同时保留其代数前因子；第三个尺度描述在归一化比较中相消的共同热演化振幅。在此参数范围内，<span class="math inline">\(\mu=o(A)\)</span>；特别地，当 <span class="math inline">\(A\)</span> 与 <span class="math inline">\(L\)</span> 同阶时，有 <span class="math inline">\(\mu=o(L^2)\)</span>。</p>
```

### P113

```html
<p>通量商中的多项式因子不能丢弃。例如，<span class="math inline">\(m/\sqrt A\to\infty\)</span> 允许 <span class="math inline">\(\mu\)</span> 比 <span class="math inline">\(\log A\)</span> 增长得更慢。此时，仅将表达式写作 <span class="math inline">\(\exp(\Theta(\mu))\)</span>，并不足以推出未加权商发散。本文使用的是定理 <a href="#thm:parabolic-shear" class="xref" data-ref-target="thm:parabolic-shear">4.5</a> 中的双侧不等式，而不是这一简写。</p>
```

## 精确替换：附录 D

### P114

```html
<p>图 <a href="#fig:edge-diagnostic" class="xref" data-ref-target="fig:edge-diagnostic">1</a> 展示了定理 <a href="#thm:heat-edge" class="xref" data-ref-target="thm:heat-edge">4.1</a> 的证明中所用正外部积分的三个常数。记 <span class="math display" data-source-display="display-139" data-source-sha256="307aaae433fcee3183ace5a272b2aa01eae239b33f4cd48cd880d56722229723">\[I_{m,A}(s,c)=\frac1{\sqrt{4\pi s}}\int_0^\infty
\cosh\!\left(m\operatorname{arcosh}(1+y/A)\right)
             e^{-(y-c)^2/(4s)}\,dy .\]</span> 在 <span class="math inline">\(s=4\)</span> 时，归一化鞍点位置、对数振幅及单位坐标位移下的对数倾斜，分别趋于 <span class="math inline">\(2^{5/3}\)</span>、<span class="math inline">\(3\,2^{-2/3}\)</span> 和 <span class="math inline">\(2^{-4/3}\)</span>。该计算以对数形式求值这个正积分，并未通过大傅里叶系数相减来获得小残差。</p>
```

### P115

```html
<p>计算采用确定性的 IEEE-754 binary64 数值求积，精细计算使用 40 001 个网格点，对照计算使用 20 001 个网格点；积分区间按照对数相位下降 48 的标准截断。辅助目录 <code>anc/heat-edge/</code> 包含绘图源码、参数及全部 16 行数据；运行 <code>plot.py --check</code> 可复现数值比较报告。两种分辨率及尾部截断的比较用于衡量这次有限计算的稳定性，并未给出适用于所有次数和尺度的误差包络。极限断言和 Navier–Stokes 结论的依据是解析证明。</p>
```

### P116

```html
<p>该图仅展示定性极限，并不展示定量界或第二类切比雪夫扩展。<code>anc/checks/</code> 中另含精确代数核查；二者均不构成连续极限证书。</p>
```

### 图 1 完整图注

```html
<figcaption><span class="math inline">\(s=4\)</span> 时的有限热演化边缘诊断。四种次数增长律均令 <span class="math inline">\(m\)</span> 为最接近 <span class="math inline">\(A^\sigma\)</span> 的正偶整数，取 <span class="math inline">\(\sigma=0.75,1,1.25,1.5\)</span> 及 <span class="math inline">\(A=256,1024,4096,16384\)</span>。子图 (a)–(c) 依次展示鞍点位置除以 <span class="math inline">\(\mu\)</span>、<span class="math inline">\(\log
I_{m,A}(4,0)/\mu^2\)</span> 和 <span class="math inline">\([\log
I_{m,A}(4,1)-\log I_{m,A}(4,0)]/\mu\)</span>。水平虚线对应三个解析极限。所有量均为无量纲量，子图 (b)–(c) 使用自然对数。各子图的纵轴显示范围分别放大。在这一有限网格上，<span class="math inline">\(\sigma=0.75\)</span> 的对数倾斜序列略微远离其极限；不能根据这些绘制值断言收敛。图例中的字母 <span class="math inline">\(p\)</span> 在这里表示 <span class="math inline">\(\sigma\)</span>，不表示压力或尺度参数 <span class="math inline">\(p_0\)</span>。</figcaption>
```

## 标题与收尾核验

- 第 5–7 节及附录 A–C 现有章节标题没有需要阻断发布的语义差异。
- 建议将 `h1#sec:diagnostic` 的文字替换为 **D 热演化边缘计算的有限诊断**；保留现有 ID、编号及属性。
- 63 个完整段落替换及 1 个完整图注已全部给出。各段的数学、公式锚点、公式编号、交叉引用、文献引文、代码节点均逐段进行原 HTML 节点多重集检查，零缺失、零新增、零内容修改。段落自身属性也全部保留，包括注 6.3 的 source-block 信息和锚点。中文语序所需的节点移动有意保留。
- 段落替换节点计数：`math` 392，`tex-anchor` 33，`equation-numbers` 28，`xref` 57，`citation` 9，`code` 4；图注另外保留 12 个数学节点。
- 当前快照审校完成后，英文和中文输入文件 SHA256 仍与本报告开头一致。本文仅写入本报告，未修改转换器、源稿或网站。最终发布包装、浏览器排版及整体替换后的全文章节契约属于后续验收，不在此快照报告中冒报通过。

### 对照源文件 SHA256

- `frame-and-mass.tex`：`a430ec1536cf92b9f50759bb847b005dd3c3bd569d2db50bcbf2bde07e3c35bb`
- `upper-bound.tex`：`ac53834ed60887625e8874a17c023c0aa62ae3695722efb1d6e789da870bfa01`
- `discussion.tex`：`0a4c9619c6ea711c7267743ecbe70e8a15ed3ea887372c2f96e6bda35b7f0f51`
- `time-weighted.tex`：`8b59ed97145ac07a710b87dbc6c964f9b974009ea97d6e5d4d6d43bf11bcb7ae`
- `sharpness.tex`：`567e8c763982e5351a47b8c7b41068abfce3b27f738426ef8abd9af530c1a279`
- `consequences.tex`：`ff434448c7fc3a7c93aa3850d8f1a8d381d409e4ede08825e105df7943777618`
- `diagnostic.tex`：`73c40bfbe180c874870325bd39709b9a6e9876c6bec72910c6a640fec4a34ed9`
