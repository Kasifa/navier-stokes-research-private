# Miller 模型与对称性：有界原文范围记录

2026-09-08。PRIVATE_CORE。SOURCE PREFLIGHT / NO MODEL-TO-NS IMPORT / NO-CANDIDATE。

**结论：2307.03434研究固定三维环面上的 Fourier-restricted 模型，其爆破不是普通正黏性 NS 爆破。** 几何对称性、约束频谱和控制方程必须分别保留。对角平面镜像的一般周期性问题，原文附录已作明确限定；不能只据引言的形式记号把它当成标准环面整个函数空间的自变换。

## 1. 继承去重与实际阅读

先在本工作树 research/ 下以精确编号 2307.03434、2404.01505 和 Evan Miller 搜索，再补精确标题及 Fourier-restricted 词。所检文本中两个编号及相关题名未命中；作者命中来自其它正则性论文。这是有限定向检索结果，不证明全库或全部历史从未读过。

为确认作者同名命中实际对象，定向读
research/clay_b_dynamic_strategy_primary_reading_20260906.md 第31–55行（§2及下一节入口）：它记录1710.05569的中间应变特征值准则，不能当成本次两篇的阅读证据。实测该本地文件 SHA-256：
2b8f0ae5f98bea63516261d78a1982060aef98757d827bc41363f4408e8e83c1。
其余作者命中仅读检索上下文，没有冒称全文重审。

官方当前版本由各 arXiv 摘要页实际确认；再读固定版本 PDF。元数据哈希由官方 PDF 字节实测，没有保存或分发 PDF。

| 来源 | 当前版本及 PDF SHA-256 | 本次实际使用原段 |
|---|---|---|
| [2307.03434](https://arxiv.org/abs/2307.03434)，[固定 v5 PDF](https://arxiv.org/pdf/2307.03434v5) | arXiv修订2025-08-28；PDF题头2025-09-01，113页。d6e508d194534d86d0eb0a706b5d511766dfe687209dc59a98839469f6b09cc5 | PDF第2–6页方程、§1.1约束与定义；第7–10页§1.2有关模型及对称保持的陈述；第20–21页Definition 3.1及傅里叶规范；第41–44页§5相关投影/对称性段；第103–104页C.3入口、Definition C.21、Remark C.22、Lemma C.23、Theorem C.24陈述；第107页Appendix D开头 |
| [2404.01505](https://arxiv.org/abs/2404.01505)，[固定 v3 PDF](https://arxiv.org/pdf/2404.01505v3) | arXiv修订2024-12-08；PDF题头2024-12-10，44页。18a0e322a43ca4ef7aacb62a4f63a24c7a46c8294eec7618be66dc2059e01533 | 官方摘要；PDF第1–2页对象区别、第4页Theorem 1.4与第5页Remark 1.5、第6页Theorem 1.7；第9–10页Definitions 1.15–1.26；第39页Theorem 4.13及第43页Corollary 4.21、Remarks 4.22–4.23的对称群陈述 |

页码均指上述 PDF。读取是定向正文提取，不是全篇视觉或证明认证。工具定位时另返回的相邻内容不计为已审结果。本轮不重演2307.03434的§7爆破证明、模式相互作用附录或2404.01505援引的 Elgindi 构造。

## 2. 方程与空间：两处限制均不能删除

2307.03434的 (1.8)–(1.9) 是
\[
 \partial_tu+P_{\mathcal M}((u\cdot\nabla)u)=0,\qquad
 \partial_tu+\nu(-\Delta)^\alpha u+
 P_{\mathcal M}((u\cdot\nabla)u)=0.
\]
普通 Euler/NS 的 Helmholtz 投影 \(P_{\rm df}\) 在这里被更窄的 \(P_{\mathcal M}\) 替代。Definition 1.1不仅要求频谱位于指定壳集合 \(\mathcal M\subset\mathbb Z^3\)，还把每个系数限制到预定实向量 \(v^k\) 的复线性张成方向；\(v^k\) 是 \(\sigma=(1,1,1)\) 在 \(k^\perp\) 上投影的归一化。它不是整个无散空间。Definition 3.1使用固定周期域、整数频率和指数 \(e^{2\pi i k\cdot x}\)，不是随时间改变的环面。

§1.2的黏性爆破陈述保留 \(0<\alpha<\log3/(6\log2)\) 以及其初值/Lyapunov条件。这个范围不含普通拉普拉斯耗散的 \(\alpha=1\)；即便更改耗散，\(P_{\mathcal M}\) 与 \(P_{\rm df}\) 的差别仍在。保有若干能量、涡量恒等式不使两个方程相同。[PDF第3–10页](https://arxiv.org/pdf/2307.03434v5#page=3)

## 3. 对称定义与动力学保持的准确层次

Definition 1.4和Remark 1.6的速度约束分别是
\[
 u(Px)=Pu(x),\qquad u(-x)=-u(x),\qquad
 u(x)=M_\sigma u(M_\sigma x),\quad
 M_\sigma=I-\frac23\sigma\otimes\sigma.
\]
第一个对所有坐标置换 P 成立；最后一个是以 \(\sigma\) 为法向的平面反射，并非涡量按相同符号变换的声明。

- **受限模型内：** Theorems 1.11–1.12陈述这些对称在各自最大存在区间保持。§5所读段给置换与奇性的保持论证；C.24把镜像与 hj-parity 对应，但明确限于已在 \(\dot H^s_{\mathcal M}\) 内且奇、置换对称的场。这不是一般场的 hj 系数描述。镜像的动力学闭合仅按主定理陈述登记，没有重审§6全部模式系统。
- **完整方程的几何对称：** Remark 1.14说这组几何对称也由完整 Euler/NS 保持。实际定向读到的 Proposition 5.8具体给完整 Euler 的置换对称保持（其强解范围 \(s>5/2\)）；Remark 5.14另指出完整方程的奇性保持。对角镜像必须同时读下一段的周期资格，不能把这句话解释成任何正交矩阵都作用在固定标准环面上。
- **约束空间不同：** Appendix D开头明确指出，一般 \(\dot H^s_{\mathcal M}\) 数据在完整 Euler/(低耗散)NS 下不继续留在该空间。几何对称保持不等于受限壳及固定极化保持，因而不能将模型轨迹认作完整方程轨迹。[PDF第42–44页及第107页](https://arxiv.org/pdf/2307.03434v5#page=42)

Remark C.22是必须保留的原文限定：将周期场提升到 \(\mathbb R^3\) 后可以写 \(M_\sigma u(M_\sigma x)\)，但它一般不再具有三个标准坐标周期。原文 (C.134)–(C.135) 给
\[
 k\longmapsto M_\sigma k
 =k-\frac23(\sigma\cdot k)\sigma,
\]
并将变换后仍周期的条件写成：每个支撑频率均满足
\((\sigma\cdot k)/3\in\mathbb Z\)，指出该条件对其模型空间成立。这并未声称镜像约束不存在；它说明变换作为标准环面函数必须先满足资格。本稿只记录这一原文接口，不代替根另作的 lattice 核验或新证明。[PDF第103–104页](https://arxiv.org/pdf/2307.03434v5#page=103)

## 4. 与2404.01505的有限比较

第二篇的对象是完整 Euler。其 Definitions 1.15–1.26在 \(\mathbb R^3\) 上定义正交作用、镜像和群 \(\mathcal G_\sigma\)、\(\mathcal G\)；Theorems 1.7/4.13的旋转共轭也是全空间场的陈述。Corollary 4.21用完整 Euler 的正交协变性和唯一性保持该离散对称。没有由此给出任意旋转在固定标准环面上的自同构。[PDF第9–10、39、43页](https://arxiv.org/pdf/2404.01505v3#page=9)

其摘要及 Theorem 1.4涉及的爆破是 \(C^{1,\alpha}\) 全空间 Euler；Remark 1.5明确其来源是将既有 Elgindi 型轴对称、无周向速度解改变坐标。该来源、正则度和零黏性都不能替换成本任务允许的光滑周期、固定正黏性 NS。这里只核原文对象和群陈述，没有接纳该爆破证明或外引。

本次预检没有选实际新初值、频率、幅度或时刻，没有科学程序、数组、数值求值、扫描、Git、外发或发布。它只形成两个现有原文的准确范围记录，不构成新的普通 NS 动力学输入或候选。
