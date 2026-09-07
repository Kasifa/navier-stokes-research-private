# 热预置边界的独立数学复核

2026-09-07。PRIVATE_CORE。审查者：`/root/driver_contract_review`，不是 `DERIVATION.md` 的作者。作者分工独立性不等于真人同行评审。

**PASS，限定于本合同的条件边界与最终稿 H.1–H.15（含 H.7a–c）。** 未发现尚待修复的内部数学错误。本记录直接核验现有合同、无限和、Hilbert 几何与完整 NS 能量式；不新选初值、不做 PDE 数值计算、参数扫描或冻结。没有因此接受奇性候选、真实第二代供给或同初值 NS 等号可达性。

## 1. 固定初值、无限谱和零时刻

全文读取 `CONTRACT.md` 与 `DERIVATION.md`，并在作者加入 H.7a–c、收紧 H.15 后再次全文读取最终稿。论证确实固定一次初值 \(a\)、黏性、环面和阈值 \(K\)；并未把每个有限截断或每个频率分别选出的初值族当作单一轨道。允许非零均值不会影响结果：零模留在低尾，热场分母依然为正。

光滑初值使 \(\sum_k\lambda_k^m|\widehat a(k)|^2<\infty\) 对所有有限整数 \(m\) 成立。对任意有限 \([0,T]\)，时间导数项的绝对值受同一可和数列控制，故逐项求导、在零时刻取右导数以及其连续性均合法。此处没有先把无限和截断后漏掉尾误差。任意非零 Fourier 系数又给 \(S(t)\ge b_{k_*}e^{-2\nu\lambda_{k_*}T}>0\)，商的导数在整个有限窗口定义良好。

## 2. 高低协方差符号

从 \(S_A/S\) 的商导数直接得到 H.2。展开 \(\mathbb E[\mathbf1_A\lambda]-\mathbb E[\mathbf1_A]\mathbb E[\lambda]\) 后，高–高部分以 \(i,j\) 交换抵消，留下
\[
\sum_{i\in A,j\notin A}\mu_i\mu_j(\lambda_i-\lambda_j).
\]
完整双和绝对值不超过 \(2\sum_k\lambda_k\mu_k\)，所以这一交换不是条件收敛的重排。高尾使用 \(|i|\ge K\)，低尾使用 \(|j|<K\)，每个留下的差严格为正；只有其权重可能为零。初始两侧能量都非零时，对任一有限时刻存在严格正项。高侧或低侧初始为空则比值分别恒为 0 或 1。H.4–H.5 的符号、严格性和时间积分通过。

这里的结论是固定阈值尾的比例，既不是移动频带的振幅，也不是重新挑选频率阈值后所得的单调性。

## 3. 相对全场误差的几何检查

设 \(x=h/\|h\|\)、\(y=u/\|u\|\)、\(\rho=\|u\|/\|h\|\)。由 \(\|x-\rho y\|\le\varepsilon<1\) 得内积 \(c=\langle x,y\rangle>0\)，再由
\[
\|x-\rho y\|^2=(\rho-c)^2+1-c^2
\]
得夹角正弦不超过 \(\varepsilon\)。在 \(x+y,x-y\) 归一化所得正交基中，投影比例差等于 \(2\sqrt{1-c^2}\langle e,Qf\rangle\)。比较 \((e+f)/\sqrt2\) 与 \((e-f)/\sqrt2\) 的投影范数，得 \(2|\langle e,Qf\rangle|\le1\)。因此 H.7 的通用常数 1 正确，变化的全能量分母已经由单位方向与 \(\rho\) 完整处理。

原稿给出的二维等号例也可直接验证：夹角 \(\theta\)、\(u=\cos\theta\,y\) 使相对距离等于 \(\sin\theta=\varepsilon\)，两个投影比例之差为 \(\sin(2\varphi+\theta)\sin\theta=\varepsilon\)。其锐性仅是一般 Hilbert 空间投影问题的锐性，不是同初值 NS 轨道的可达等号；作者已明确区别。

本审查另外直接推导基准比例已知时的角度限制。令
\[
\alpha=\arcsin\sqrt{p_Q(h)},\quad
\beta=\arcsin\sqrt{p_Q(u)},\quad \theta=\arcsin\varepsilon.
\]
对 \(Q\) 与 \(I-Q\) 两部分分别用 Cauchy，不要求分量的内积为正，仍有
\[
\langle x,y\rangle
\le\sqrt{p_Q(h)p_Q(u)}+
\sqrt{(1-p_Q(h))(1-p_Q(u))}
=\cos(\alpha-\beta).
\]
另一方面 \(\langle x,y\rangle\ge\sqrt{1-\varepsilon^2}=\cos\theta\)。因为 \(|\alpha-\beta|\in[0,\pi/2]\)，得到 \(|\alpha-\beta|\le\theta\)。这给出截在 \([0,\pi/2]\) 内的上下角度界，热场尾为空时尤其给 \(p_Q(u)\le\varepsilon^2\)。原来仅用 H.7 得到的 \(\varepsilon\) 上界并无错误；平方界使用了额外已知的基准比例。

最终 H.7a 的两级夹角不等式、H.7b 的上下端点截取和 H.7c 均与以上独立推导逐项一致。\(F_\varepsilon\) 在 \([0,1]\) 上连续非减；截断至 \(\pi/2\) 避免把 \(\sin^2\) 延伸到其非单调区间。\(\varepsilon=0\)、\(p_h=0\) 或 1 的端点也正确。

## 4. 两时刻条件和完整 NS 能量分母

分别使用相对误差界，并将热场的确切下降量 \(D_h\) 相减，H.10 的 \(\varepsilon_1+\varepsilon_2-D_h\) 上界正确。\(t_1=0\) 可用实际同初值等式取 \(\varepsilon_1=0\)。拓扑邻域或除以目标振幅后的 \(H^r\) 小性，必须另行换算才能成为这里相对全场 \(L^2\) 的假设。两时刻假设也不能升级为全时一致假设。

对完整 NS，周期分部积分和 Leray 自伴性给 \(\langle u,B(u,u)\rangle=0\)。因此
\[
E'=-2\nu Z,\qquad E_K'=2\Phi-2\nu Z_K,
\]
及
\[
p'=\frac{2\Phi}{E}-2\nu\left(\frac{Z_K}{E}-p\frac ZE\right).
\]
系数 2、分母的导数及黏性项全部正确。正交 Fourier 尾投影与导数交换，没有把它与光滑环带乘子混为一谈。对当时真实谱再次使用 §2 的绝对收敛双和，括号非负，但完整非线性 \(\Phi\) 不限号。故 H.11–H.13 没有给一般 NS 热单调性，也没有从通量正性推出第一代自产归因。

若两个观测时刻支付相对误差，则 \(u(t_2)\ne0\)；能量不增又给整个窗口 \(E(t)\ge E(t_2)>0\)，所以积分时不存在未经说明的零分母。此判断无需调用未在本稿证明的反向唯一性。

## 5. 既有 FA 输入的定向核对

实际重新读取 `research/clay_b_frequency_activation_20260907.md` 的 FA.1–FA.6、FA.10–FA.17 及 §7 边界。本次按既有接受的 FA.4 结论使用它，没有重新认证其全部 Euclidean 非退化种子证明、旧冻结记录或外部来源。

FA.4 的初始支撑在 \(N\le|k|\le2N\)，光滑乘子 \(\chi(k/N)\) 支撑在 \(2.05N<|k|<2.2N\)，且 \(0\le\chi\le1\)。固定其中一个已存在的充分大 dyadic \(N\) 及其原解，取 \(K=2.05N\)，得到初始正交高尾为零；后来 \(\|\chi(D/N)u\|_2>0\) 则必有 \(\|Q_Ku\|_2>0\)。这里仅使用支撑包含，不要求 \(\chi(D/N)\) 幂等。

FA.16 的缩放最终回到固定 \(2\pi\) 环面、固定原黏性 \(\nu\)；扩大环面的辅助黏性不是最终更换方程。选定单个 \(N\) 后，这是一条固定初值光滑轨道上的有限激活。起末比值为零和正，中值定理给某时刻 \(p'_K>0\)。它支持“完整 NS 可以向上改变此比例”，不支持一个固定初值的无限级联或新的两代供给结论。

## 6. 全时尾紧性与研究边界

H.14 对每个固定 \(K\) 用热单调性，并因 \(t=0\) 包含在上确界中取得等号。随后 \(K\to\infty\) 仅用同一 \(a\) 的初始可和谱能量尾。即使每个阈值另选观测时间，这一全时结论仍有效；它没有使用“对每个阈值更换初值”的量词。

全时 NS 相对误差假设若独立支付，可逐时转用 §3 的几何界。基准热比例上界 \(p_K(a)\to0\)，结合角度公式给尾比例的全时极限上界 \(\varepsilon_0^2\)。这仍是条件性上界；正 \(\varepsilon_0\) 下不能仅由此把右端改为零，更不能从两个已检验时刻获得整个存在区间的误差认证。

未加权 \(L^2\) 比例尾的紧性不提供 \(\sum |k|^{2s}|\widehat u(k)|^2\) 的统一上界。小能量高频部分仍可携带很大的导数加权量。因此热结论或条件性 NS 尾上界都不能排除一般奇性，也不是所有奇性必须经过的预设比例门槛。没有已认证的新 \(\varepsilon_i\)、实际新候选或跨代统一误差。

## 7. 历史审计的实际核对范围

全文读取 `HISTORY_REVIEW.md`，检查它引用的是包含 H.7a–c 及平方尾界的最终稿。该审计将 R0.5 的三线性/临界 Sobolev 比值、线性化算子稳定性谱、位置空间热滤波方差与本稿 Fourier 二次能量概率分开；这些区分与当前命题的数学对象一致。其 FA 迁移结论由本人在 §5 已实读的源稿另外核对。其关于相对两条 NS 真解的稳定性不能直接用于一般热参照的限定，也与完整 \(B(h,h)\) 源项存在相符。

本审查没有重新阅读该历史审计列举的全部 15 个旧科学输入，也没有通读 283 文件语料或重新搜索外部论文；不将该代理的实读范围记成本人的独立原文认证。历史报告的有限检索未命中结论不被当作新颖性证明。

实际用 SHA-256 与字节数重新核对 `history-review-inputs.json` 中 20 个绑定记录及 `history-search-manifest.json` 中 283 个语料记录，全部匹配。20 项包括其 15 个实读输入与 5 个检索证据文件；它们不是 20 个新科学证书，也不意味着本人已阅读所有绑定正文。哈希检查是文件完整性操作，没有重新运行旧数值脚本或数学扫描。

## 8. 最终输入绑定

以下路径相对当前科学工作树，绑定本次实际用于审查的文件。`SOURCE_ATTRIBUTION_LEMMA.md` 的完整推导在本人前一轮已全文独立审过；本轮使用该既有来源接口，并核对其当前字节未变。对 FA 的本轮阅读范围见 §5，其它历史正文不因清单绑定而被扩入本人的证明审查。

| 实际输入路径 | SHA-256 |
| --- | --- |
| `research/reverse/heat-preload-boundary/CONTRACT.md` | `9d78b048092b9b6af2dfa8ba44896bec39a5c9145aa1a28373c96bffb6377784` |
| `research/reverse/heat-preload-boundary/DERIVATION.md` | `333d5708b253a3f86d52324dd7e28e97b941afcf9c7c71c9b041616df0bc6a1a` |
| `research/reverse/heat-preload-boundary/HISTORY_REVIEW.md` | `087d946230029f86677b3a0ac93b746a879d74a981acc3493eb721bd6434ba08` |
| `research/reverse/heat-preload-boundary/history-review-inputs.json` | `9cf13a43fe506518c84fcfa47668f8b685a279d2bd7bf24c4456b58680c23b18` |
| `research/reverse/heat-preload-boundary/history-search-manifest.json` | `817c98edc1bc4a0448d23799efaacf950110d254c463637993cbf3cdefb14508` |
| `research/clay_b_frequency_activation_20260907.md` | `42bbc2ba3abae7aa1eeb25ee0b29f896d7d8ddcafccb0da518dded4851dd897a` |
| `research/reverse/reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md` | `d22bcca237977647b54ebbe13288c63a24a7c610a52a7c2265f4e3cfe366607a` |
