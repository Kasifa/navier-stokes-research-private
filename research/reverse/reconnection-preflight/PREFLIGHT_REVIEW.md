# 重联预审的独立交叉复核

2026-09-07。PRIVATE_CORE。独立审查者：`/root/driver_contract_review`。本审查者不是下列两份来源报告或 Stokes 引理的作者；结论来自实际原文阅读和下述手工推导，不以主代理或作者的 PASS 代替证据。这里的独立性仅指作者分工，不是真人同行评审。

**PASS，范围限定为来源适用性预审、Stokes 条件接口及时间来源分解的条件余项。** 未发现阻断当前被审文本结论的数学错误。没有得到第一阶段新生结构独立供给第二阶段的认证下界；数值来源的这一归因仍未支付，不能写成已经证明失败。本记录不是新奇性排除定理，也不认证一个奇性候选。

## 1. 本审查者实际读了什么

全文读取 `CONTRACT.md`、`THEORY_READING.md`、`NUMERICAL_READING.md`、`STOKES_BASELINE_LEMMA.md`、`SOURCE_ATTRIBUTION_LEMMA.md` 与 `OUTCOME.md`。本审查者也不是后两份文本的作者。合同开头的“当前已读”是启动时的阅读状态；后续两报告与本审查分别记录实际完成范围，不能把启动状态当作最终阅读结论。

理论原文使用本地 arXiv:1606.06176v2 PDF，直接用 Poppler 重新提取并核读 PDF 页 2–3、9–10、13–22、27–28；页 17–19 对可能截断的工具输出另行分批重读。另实际查看来源页图像 18、21，核对 Duhamel 和重标公式。本审查者没有完成 §2、§3 的全部证明复证，没有审计 §5、外引 KAM/拓扑定理或出版版。来源报告作者自己的更广阅读范围不记入本人的阅读量。

数值原文使用本地 arXiv:1212.3829v2 PDF，直接重新提取并核读正文 PDF 页 1–14；实际查看来源页图像 4、8、9、11。未追读第 15 页参考文献，未读 v1 或其他数值论文，未取得运行源码与原始生产数据。

上述来源页图像仅帮助读取原文，不是本项目生成的科学图。以下代数核对均为手工推导；本次没有 PDE 仿真、参数扫描、数值实验或新的科学计算证书。文末哈希仅标识实际输入字节。

## 2. 理论构造的交叉审查

**方程与量词。** 原文页 2–3 的固定正黏性、固定 \(2\pi\) 三维环面、无外力完整 NS 和同一全局光滑轨道均已核对。Theorem 1.1 先给有限时间表和有限目标族，再选一个允许的实值零均值初值；该初值在这一轨道内不再改变。增加阶段数时可以重新选初值，故准确量词是“每份有限计划存在一个初值”，不能换成“存在一个初值实现所有阶段”。本审查不补造奇数终点后未指定的时间。

**预置分量与拓扑新生。** 页 17–18 的初值含全部 \(\delta_jW_j\)。由 \(\operatorname{curl}W_j=N_jW_j\) 及不同频率，\(\Pi_{|m|=N_j}u_0=q\delta_jW_j\ne0\) 是直接 Fourier 结论。它证明后续主导速度分量具有初始线性前身，并不证明完整初始涡场已有后来目标拓扑。Lemma 4.2 与初始小性恰把整体初始场限制在没有可缩目标结构的邻域；奇数时刻的局部可缩结构确为全场的拓扑新生。报告同时保留这两点，准确。

**双向作用、压力与符号。** 页 9 的 \(v\otimes w\) 是对称外积，故
\[
2v\otimes w=v\otimes_{\mathrm{ord}}w+w\otimes_{\mathrm{ord}}v.
\]
页 18 式 (4.4) 的完整 Duhamel 差是 \(-2\mathrm{Lin}-\mathrm{Bil}\)，周期 Leray 投影保留压力；没有少一向项。页 21 的印刷重标展开确与此符号和系数不一致，本审查在原图中核实了这一点。报告按 (4.4) 修正精确恒等式、在范数预算中吸收固定系数 2，处理正确；这不是对整篇定理的否定。

**原证实际控制。** 原文页 13、17–22 的扰动小性、保留至 \(H^{r+1}\) 的界、Lin/Bil 的 \(H^r\) 上界，以及 Step 3 分别压低热非目标项和完整非线性余项，均与报告一致。高频基场的衰减和有限计划相关常数不能变成任意数据、任意次数的统一控制。构造按未来阶段降低主导频率，且拓扑判据在除以目标振幅后使用，不能由拓扑重联推出临界量放大或向无限高频供给。页 27–28 对线性机制的解释支持这一适用性判断，但不能代替第一代供给的定量下界。

## 3. 数值来源的交叉审查

**运行归属与域。** 正文结构运行的 \(4\pi\times32\pi\times8\pi,\nu=.001\)，正文统计运行的 \(4\pi\times32\pi\times4\pi,\nu=.0005\)，与图 5–6 中 \(4\pi\times16\pi\times2\pi,\nu=.0005\) 标签的差别，均在原文/图像中实核。不能未经说明就将它们视为同一完整周期域或自行补入对称子域映射。来源确叙述一份固定结构运行中的连续事件，未叙述事件间重置初值；这与统计图属于另一组参数需要同时说明。不同图的重联接近、结构完成与诊断峰值时间不能拼成统一严格停止时刻。

**归因未付。** 页 8–10、13–14 说明新桥、线程/尾部、残留原涡管共同参与，且次级扭曲可早于首次重联完成。因而“第一代完全结束后，纯新生结构才独立驱动下一代”不是原文已证的因果分解。残留旧管仍是演化真解的一部分，不是外力或被固定不动的初始种子；它的存在也不能反向证明新桥没有供给。没有可计算的全场来源分解及余项，正确裁决是未认证，不能称为该物理机制已失败。

**误差缺项。** 页 6 的 \(128^3\) 用于初始化/重映射之前，不是完整生产网格证书。正文没有补齐两组生产网格、推进与去混叠参数、逐次加密误差及连续尾部后验界。初始 Fourier 滤波不把普通 \(\nu\Delta\) 方程变成超黏性演化。图内运行名不能补出缺失配置。以上缺项限制移植与认证，不证明计算本身错误。

**两个直接代数检查。** 记 \(D=X^2+Y^2+a^2\)，则
\[
\partial_X(\Gamma X/D)-\partial_Y(-\Gamma Y/D)=2\Gamma a^2/D^2.
\]
因此 p.4 式 (5) 的两式按通常二维 curl 的确有因子 2 不匹配；只能要求澄清幅度约定，不能据此推断运行代码。若 \(Z=\int|\omega|^2\)，完整周期 NS 给
\[
Z'=2\int\omega^TS\omega-2\nu\int|\nabla\omega|^2.
\]
所以 p.8 式 (9) 中的生产项不能不加归一化和耗散就读成完整 \(Z'\)。报告的限定正确。页 12 的矩排序仍未证明，页 14 的有限重联/量子或足够长域叙述也没有固定原 NS 解无限迭代的量词。

## 4. Stokes 基线引理的独立推导

令 \(h=e^{\nu t\Delta}u_0\)，\(\operatorname{curl}W_k=N_kW_k\)。对 S.2 第一差取 curl 后除以 \(N_k\)，直接得到
\[
\frac{\operatorname{curl}h}{c_kN_k}-W_k
=\frac1{N_k}\operatorname{curl}\left(\frac h{c_k}-W_k\right).
\]
再对 \(u-h\) 用三角不等式，即得 S.3–S.4，没有漏掉 \(N_k^{-1}\)。在三维固定环面，\(r\ge7,\alpha<1\) 确保 \(r>4+\alpha+3/2\)，所以 \(H^r\hookrightarrow C^{4,\alpha}\) 及所写 curl 算子界成立。S.6 两项相加至多是 S.5 严格阈值的一半，端点仍留有严格余量。

对最终允许初值 \(u_0=q\sum_j\delta_jW_j\)，热演化与 \(c_k=q\delta_ke^{-\nu N_k^2T_k}\) 相除，\(q\) 完全消去，S.7 的全部非目标指数和幅度比正确。\(T_0=0\) 的式子也正确。正的空间常数只重参数化涡量曲线，故结论确为指定拓扑性质，不是幅度下界。

对同一最终初值的真实 NS 解，以 Beltrami 热解 \(w_q\) 为背景，展开完整有序二次项并合并对称记号，得到 S.8 的 \(-2L_q-B_q\)。S.9 是这一精确差的上界。振幅归一化只能重新取 \(qa\) 的 NS 解，不能把旧 NS 轨道乘 \(q\)；被审稿已作此限制。

页 20–22 的原参数选择分别支付有限多个热误差和非线性误差的定性小性。进一步预设有限个拓扑半径下的严格阈值是允许的；单独缩小 \(\delta_1\) 不能完成它，因为背景/目标幅度比会反向增大。稿件所述配合 \(N_0\) 的指数衰减和幂次幅度选择，避免了这一错误。这里没有实际选定新的参数值或获得数值误差界；原文所引拓扑稳定性仍是明确的外部输入。

因此 Stokes 基线的肯定结论通过：该有限构造的热场本身可以进入相同指定拓扑邻域，完整 NS 也可由真实余项控制进入它。两者不必具有全部相同的涡拓扑；\(h\) 一般不是 NS 解；本审查没有删种子的另一 NS 解、纯第一代供给或一般重联必为线性的结论。

## 5. 时间来源分解和条件预算的独立推导

本节直接从被审稿定义推导，不依赖其作者的独立审计标签。固定同一轨道与 \(t_1\)，热半群性质给 \(v=h+g=E(t-t_1)u(t_1)\)，而完整 mild 式给 \(r=\int_{t_1}^tE(t-s)B(u,u)\,ds\)。将 \(u=h+g+r\) 代入有序双线性算子，\(\mathcal G\) 一项、\(\mathcal H\) 三项、\(\mathcal R\) 五项恰好覆盖全部九项。重组
\[
B(r,u)+B(v,r)=B(r,v)+B(r,r)+B(v,r)
\]
没有遗漏 \(B(r,r)\)、任一回流方向或热传播。\(g\) 的前史积分来自原解，不是自由添加状态；但这一积分含全部早期自作用、混合作用与返回作用，不能由时间标签认定为物理上的纯第一代涡管。

向量 Fourier 卷积用 Euclidean 长度、Leray 算子范数不超过 1，确得 \(\|B(f,g)\|_{A_m}\le\|f\|_{A_m}\|g\|_{A_{m+1}}\)。对无散第一因子，\(\widehat f(p)\cdot q=\widehat f(p)\cdot(p+q)\)，故热平滑把导数移至输出频率；\(\sup_{x\ge0}xe^{-\nu\sigma x^2}\le(\nu\sigma)^{-1/2}\) 给式 (8)，没有分量数或体积常数。

由独立给定的真实解 \(A_{m+1}\) 上界 \(M\)，式 (2) 在 \(A_m\) 给 \(\|r(t_1+\sigma)\|\le M^2\sigma\)。在重组式 (6) 中使用热输出导数估计得到
\[
\|\mathcal R(t_1+\tau)\|_{A_m}
\le\frac{(M+K)M^2}{\sqrt\nu}
\int_0^\tau\sigma(\tau-\sigma)^{-1/2}d\sigma
=\frac{4(M+K)M^2}{3\sqrt\nu}\tau^{3/2}.
\]
这里 \(r\) 用 \(A_m\)，\(u,v\) 的同级范数由 \(A_{m+1}\) 输入控制；端点奇性可积。若另付 \(A_{m+2}\) 上界，则先得 \(r\) 的 \(A_{m+1}\) 线性时间界，再用未经平滑的乘积界积分，系数确为 \((M_2+K_2)M_2^2/2\)。稿件没有把这一更高空间正则输入偷偷加入第一预算，也未声称指数最优。

在 \(T_{\rm loc}=\nu/(256A^2)\) 上，双线性积分常数为 \(2\sqrt{T_{\rm loc}/\nu}\)。半径 \(2A\) 球映入范数不超过 \(3A/2\) 的球，差值常数不超过 \(1/2\)，均核对正确。高阶 tame 卷积的两项给 \(c_\ell=2^\ell(2A)/\sqrt\nu\)；其反复半阶 Volterra 卷积的 Gamma 分母正是 \(\Gamma(1+n/2)\)，在同一有限窗口收敛。高一阶一致界与低阶压缩收敛经加权 \(\ell^1\) 插值给任意有限阶连续收敛，继而由方程得时间光滑。没有为每个导数另取趋零窗口。

从已认证的 \(u(t_1)\) 续接时 \(M=2A,K\le A\)，代入得到 \(16A^3\tau^{3/2}/\sqrt\nu\)；这仍是同一原解的局部分析。它不自动认证此前到达 \(t_1\)、所给范数上界或超出充分局部窗口的时间。\(A=0\) 另按唯一零解处理，避免除零。

这一条件上界没有压低 \(\mathcal H\)，没有给 \(\mathcal G\) 非零目标/占优下界，也没有为线性 \(h+g\) 的目标贡献作归因。它只是固定参照与切点后的精确来源账目和全 PDE 余项；不能将各项当作正交代际能量，或把 \(g\) 的热续演称为 NS 解。相关边界全部通过。

## 6. 当前边界

理论材料给出可复用的拓扑接收邻域和完整误差方法；数值材料给出新旧结构共同参与的定性线索。两者均未交付本任务所要求的、压住初始直接通道并证明第一代真实供给下界的完整两步合同。结论止于这一来源和判据筛选，保留以后补证或其他机制的可能性；没有奇性、统一返回、一个固定初值的无限尺度、有限总时间或一般正则性结论。

`OUTCOME.md` 的 NO-CANDIDATE 限定为两份材料未交付本合同的严格接口，且明确区分理论构造的已识别来源路径与数值机制的未付归因，表述通过。两项条件接口的公式与本审查手推匹配，没有新增已证的供给占优。审查指出的唯一需修正文句是最终 \(u_0\) 与中间初值的 \(q\) 归一化记号可能重复；作者已改为“中间初值 \(a\)、最终允许初值 \(u_0=qa\)”及对应真实解，本人实际重读了修后段落。

该结果稿对其他作者/主代理阅读活动的叙述属于各自记录，不是本审查替他们认证的阅读量；本人范围只见 §1。结果稿所指后继 `heat-preload-boundary/CONTRACT.md` 不在本次审查内，本 PASS 不扩展到尚未审核的后继数学。当前为来源审计与条件推论，不要求将常用恒等式、局部压缩或原文直接推论另封为新颖研究结果。

## 7. 实际输入字节绑定

以下 18 条路径相对本工作树。绑定包括六份全文被审稿、两个原 PDF 与文本、两个来源清单，以及本审查者实际查看的六张来源页图像。清单中作者的阅读记录不扩张本审查范围。未绑定未读的新稿；后续审查须另列增补及实际文件哈希。

| 实际输入路径 | SHA-256 |
| --- | --- |
| `research/reverse/reconnection-preflight/CONTRACT.md` | `23eca817fca5500e6dc7e7ec5647272751929fd486c58ed3dd6f30d32a893cf4` |
| `research/reverse/reconnection-preflight/THEORY_READING.md` | `50f67bf49150d254b398a1a60161f0e0ac92736dbdfee2f936e0b330e45cf418` |
| `research/reverse/reconnection-preflight/NUMERICAL_READING.md` | `776cd2ca9be34cb835b32a7e9166d504cc103e835f4a9fb25bfe1eb7b8664b00` |
| `research/reverse/reconnection-preflight/STOKES_BASELINE_LEMMA.md` | `e1c7baedaa8f56d15028cce300006db0edae174302b8044d14d54f6ef1c04cc3` |
| `research/reverse/reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md` | `d22bcca237977647b54ebbe13288c63a24a7c610a52a7c2265f4e3cfe366607a` |
| `research/reverse/reconnection-preflight/OUTCOME.md` | `4028dfb0b4dfdfaa1e5f9d02ebdc1f95d54b87c71e7f48339b0740977067a530` |
| `research/reverse/reconnection-preflight/theory/SOURCE_MANIFEST.json` | `a8c738c03717311770dd576e89e8862ade9365eaafaf94cff85b1b48415a8d94` |
| `research/reverse/reconnection-preflight/theory/enciso-luca-peralta-salas-1606.06176v2.pdf` | `ba89fa2fa06cf1dd058f9ea121364a36c59c4cdc25880e4cc7754c89ed319269` |
| `research/reverse/reconnection-preflight/theory/enciso-luca-peralta-salas-1606.06176v2.txt` | `c1077dfd622a7aca9c4e5b53caa1460c6f37022e175930bc7eb51e440e402390` |
| `research/reverse/reconnection-preflight/numerics/source-hashes.json` | `e64eeb3fa986e30f1b5c405ff80a0776581117966e12dcec34e9e63073b52284` |
| `research/reverse/reconnection-preflight/numerics/kerr-1212.3829v2.pdf` | `38de54eb0de154302fbb12f12b701c8902ba5dc45e62d2f9d3118051aefc5044` |
| `research/reverse/reconnection-preflight/numerics/kerr-1212.3829v2.txt` | `eecb786e9846aaf17a6575f2cd01bffd19f70ab232d63c4541c24e5e530951fd` |
| `research/reverse/reconnection-preflight/theory/source-page-18.png` | `ce33f80c720807cbdb804dcbbb67cbc7ada6b6860b89248fe531afed852d14a1` |
| `research/reverse/reconnection-preflight/theory/source-page-21.png` | `8c8e8da2835bca492ec6f7c0a07c427e3cc6bef174898209f206b4eb6aa43bb8` |
| `research/reverse/reconnection-preflight/numerics/source-page-04.png` | `96667fb1c4b5c45ae35f8dc53c8ecebf6eeca825f167035042b586c902c07310` |
| `research/reverse/reconnection-preflight/numerics/source-page-08.png` | `027bd18bd8bdcdd24e3a9dc9252264f039ed081f65239f6094d8a3fd4eb98b65` |
| `research/reverse/reconnection-preflight/numerics/source-page-09.png` | `702f2955288ccf216576fc202f7b4284216ef13d2b5e3b70524abf9232664f7c` |
| `research/reverse/reconnection-preflight/numerics/source-page-11.png` | `528f0ec0f11424aae1ba588dfb849e8c4b0e024be1cb10c54979e713c798e95f` |
