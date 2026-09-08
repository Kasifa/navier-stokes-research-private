# 解析性—稀疏性文献核查：先检验假设能否由无散场满足

2026-09-08。私有来源记录；不是独立研究小节或对外评议稿。
输入提交：`78b9fcea6ee7d44b25e39ebcc0d832deda77a840`。
状态：原文核查／初等兼容性计算；普通三维 NS 与 Clay 目标仍为 OPEN、NOT CLAY。

本次没有取得普通耗散指数 β=1 的新正则性估计。新增的有效信息是：
所核两份手稿按字面要求一整阶 Taylor 系数全正，与无散恒等式不相容；
其中一份的桥接证明另有一个标量指数比较不成立。
这些结论限定到下面的具体版本，不判断作者原意，不否定整个解析性—稀疏性方法。

## 1. 有限阶兼容性：不需要 NS 演化

设 u 在 x* 附近光滑且 div u=0，记
\[
c^i_\alpha=\frac{\partial^\alpha u^i(x_*)}{\alpha!}.
\]
对任意多指标 η，对 div u 求 η 阶导数并除以 η!，得到
\[
\sum_{i=1}^3(\eta_i+1)c^i_{\eta+e_i}=0. \tag{C1}
\]
这是有限阶导数恒等式；即使不用收敛的 Taylor 展开也成立。
若固定 k≥1 的所有分量、所有 |α|=k 系数均有同一个正下界 b，
取 |η|=k−1，则左侧至少为 (k+2)b>0，矛盾。
仅仅把假设改成系数的绝对值下界，并不能沿用这一矛盾；
也不能未经说明把原文的有符号系数改成模长。

## 2. 在两份已核手稿中的直接应用

### Farhat–Grujić，2312.14320v2

原文 §1 的 A1 对全部相关系数给出 c=δρ^(−k)、δ≥M^(−k)>0。
PDF 第 2 页与 HTML 一致，没有绝对值。取 k=1，便有
\[
0=\operatorname{div}u(x_*,t)
=\sum_i c^i_{e_i,1}(t)\ge\frac{3}{M\rho(t)}>0. \tag{C2}
\]
因此此版本 A1 的字面要求不能由光滑不可压速度满足，甚至在单个时刻也不能。
这是条件集合为空，不是构造了一个违反 Theorem 1.1 结论的解。
[版本与原文](https://arxiv.org/html/2312.14320v2)。

### Phiri，2512.03378v1

Theorem 3.2(i) 对同类系数给出带时间权的严格正下界；
PDF 第 9 页保留有符号 δ，证明也明确使用所有分量与多指标。
取 k=2 可避开 k=1 的对数问题。由 C1，
\[
0=\partial_1\operatorname{div}u(x_*,t)
=2c^1_{(2,0,0),2}(t)+c^2_{(1,1,0),2}(t)
+c^3_{(1,0,1),2}(t)>0. \tag{C3}
\]
在假设覆盖的近终端时段内，t<T*、ρ(t)>0，每一项的下界均严格为正。
同样只得到字面假设不可实现，不是 NS 反例。
[定理及证明](https://arxiv.org/html/2512.03378v1)。

## 3. 独立的标量核算：所写桥接比较方向相反

Phiri 的 Theorem 3.2 证明、PDF 第 10 页，在相同正因子下，
将 τ^(−E) 控制为 τ^(−F)，其中 0<τ=T*−t<1，
\[
E_{j,k}=\gamma\frac{j}{(j+1)\log j}
+\gamma\frac{k}{(k+1)\log k},\qquad
F_k=\frac{2\gamma}{\log k},\qquad \gamma>0. \tag{C4}
\]
直接取整数 j=m、k=m²，m≥2。此时 log k≤j≤k，且
\[
E_{m,m^2}-F_{m^2}
=\frac{\gamma}{\log m}
\frac{m^3-m^2-2}{2(m^2+1)(m+1)}>0. \tag{C5}
\]
于是 τ^(−E)>τ^(−F)，与该行不等式方向相反。
对任意固定 m，二者之比随 τ↓0 发散，不能用不依赖时间的乘法常数修复。
这是对展示出的标量比较的反例，不是声称这些数值来自一个满足全部前提的 NS 解；
也未检验原文后续额外截断条件 (9) 的所有组合。
即使以后将系数条件正式修成模长条件，这一行仍需新的有效论证。
[对应证明段落](https://arxiv.org/html/2512.03378v1)。

## 4. 对本路线的实际影响

两篇主定理均在全空间、β>1 且有额外聚焦／导数结构的条件下陈述。
不能把它们直接用于我们任意周期初值的 β=1 方程。
Phiri 证明中使用 1<μ<β 的参数空间，在 β=1 时也为空。
先前 [GS §7](../clay_b_geometric_sparseness_screen_20260907.md)
已经记录高阶指数差与普通 NS 的缺项；本次不将此重新算作发现。

另外两个调用接口尚未在已读模块中得到说明：

- Farhat–Grujić §4 将范数解释成局部球范数，随后调用 §3 的全空间 Corollary 3.2。
  需要外区导数／逃逸时刻控制，或保留截止、压力和非局部扩散成本的局部化版本。
- Phiri 的 Theorem 2.7 将匹配的稀疏时间与尺度存在性列为条件；
  Theorem 3.2 的证明却以该定理引出其存在。该调用还需要独立的输入。

这些是限定阅读范围内的接口检查，不是对全部上游理论的正确性判决。
C2、C3 已足够阻止本次将所写结构当作非空原 NS 分支；无需靠追加错误清单增强结论。
将来若探索类似几何假设，先检查有限阶无散兼容性并给出非空对象；
通过该检查仍不证明它能由 NS 演化产生，更不证明正则性。

## 5. 来源、版本与实际阅读范围

| 来源 | 锁定版本与实际核对 | 私有原件 |
|---|---|---|
| Aseel Farhat、Zoran Grujić，*On persistence of spatial analyticity in the hyper-dissipative Navier-Stokes models* | [arXiv 版本记录](https://arxiv.org/abs/2312.14320)：v2，2025-02-21。主任务读 §1、相关 §2–3 陈述与证明模块、完整 §4；视觉核 PDF 第 2 页。A 独立读 HTML §1、§3–4 及相关准则接口。 | [官方 PDF](https://arxiv.org/pdf/2312.14320v2)；[本地副本](sources/farhat-grujic-2312.14320v2.pdf) |
| Moses Patson Phiri，*On Bridging Analyticity and Sparseness in Hyperdissipative Navier-Stokes Systems* | [arXiv 版本记录](https://arxiv.org/abs/2512.03378)：v1，2025-12-03。主任务读 §1 范围、Theorems 2.7/2.9、Corollary 3.1 陈述及相关证明、Theorem 3.2 与相关证明；视觉核 PDF 第 9、10 页。B 独立完整读 HTML §1–3，并核 PDF 封面及第 9–12 页相关文本。 | [官方 PDF](https://arxiv.org/pdf/2512.03378v1)；[本地副本](sources/phiri-2512.03378v1.pdf) |

原件 SHA-256：

- Farhat–Grujić：`c14f1775a404a2682622e9c122505fc8b99e333c1201ccc33aefb7a7b968705c`。
- Phiri：`dfd61603e5026ccaba664b6329a745dfa95c0b71ad26d65b88304b4db0b4c748`。

Farhat–Grujić 的期刊 DOI 本次直接读取失败，未核期刊版，不推断它与 v2 相同。
Phiri 的 HTML 页内日期为 2026-08-24；这不是 arXiv 新版本记录。
本次没有认证两篇全文全部依赖，也没有真人同行评审或作者确认。
成稿后 A 复核 C1–C2 与 Farhat–Grujić 的适用范围，B 复核 C3–C5、
Phiri 的参数与条件存在性接口；未发现影响这些限定结论的问题。
依 B 的建议，已将 C3 的时间表述收紧到原假设覆盖的近终端时段。

## 6. 检索边界与停点

采用 Deep Research 的有界原文核查流程及 PDF 视觉核对。
计划更新接口不可用，阶段记录保存在本任务；未启动独立后台研究服务。
私有研究分工不允许此处生成网页或新的读者 PDF，故只保留本来源记录与官方原件。

本地先去重 [GS](../clay_b_geometric_sparseness_screen_20260907.md)、
[最近动态输入核查](../clay_b_dynamic_input_refresh_20260908/report-source.md)
及[选题入口](../forward_route_selection_20260908.md)。
Grujić–Xu 2025 的关键导数链接口已有原文记录，不再整篇重读。
另核到 [2024 论文变更记录](https://link.springer.com/article/10.1007/s00021-024-00888-x)
的 2026-02-15 更新只涉及作者单位，未将其当作新数学版本。

外部发现阶段使用六组查询，随后只回到原作者手稿和出版记录：

1. `Navier Stokes derivative hierarchy sparseness analyticity Grujic Xu regularity scaling gap`
2. `Navier Stokes regularity sparseness high order derivatives 2025 2026`
3. `"On Bridging Analyticity and Sparseness" Navier Stokes arxiv`
4. `"Navier-Stokes" "Grujić" "Xu" "2026" derivative`
5. `"On Persistence of Spatial Analyticity" "Farhat" "arxiv"`
6. `"10.1512/iumj.2026.75.60638"`

停点是这两份已核版本不提供本路线所缺的无条件输入，不是认定该方法无前景。
未穷尽文献，未作新颖性认证，未联系作者；不继续扩展检索来代替动力学研究。
下一具体无条件机制仍待选定。GRE/GPH/GRC 的开放出口不变，TG 仍是最后独立冻结。
本记录不生成 release，不重复交接，不发起仿真或 DGX 任务，不执行发布。
