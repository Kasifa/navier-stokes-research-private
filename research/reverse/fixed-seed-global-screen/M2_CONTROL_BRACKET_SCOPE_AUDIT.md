# 临界参数夹界的价值审计与一个统一排除界

2026-09-08。PRIVATE_CORE。**已有解析界和已接受的旧节点残差下界，足以排除 m≥9/2 与当前指定控制族的共同预算；尚不能排除当前参照使用这个控制族。** 9/2是排除区域的有理隔板，不是新选的μ₂或ε。

本轮只读P、CC、MB、UE、CB等正文及旧已接受结果的相应范围，作手推代数。没有读取失败M₂运行的科学值或数组，没有新指数/对数数值求值、Fraction程序、参数扫描、科学执行或新证书生产。下面只给一项实际筛选推论；其证明不依赖新CB对数夹界。

## 1. 历史与实际增量

P固定参数化显式函数；旧节点结果给同一原参照的必要残差预算η；CC已证明η<εS<E(m₀)。因此实际已知节点落在MB的正临界点分支，而非仍待判定的三选一：m₀=19/5，存在唯一mcrit>m₀，E(mcrit)=η。旧文各自“尚未判定”的说明保留历史字节，不覆盖CC后来的结论。

MB证明E(m)对参数m严格递减至零；UE补证所有有限m≥m₀的全窗标量最小门都位于T。因而0<ε≤E(m)是**此指定函数对取满包络的两条标量控制式**的准确全窗条件，不是实际NS全局性的充要条件。节点和标量门的交集仍只是η≤ε≤E(m)。

CB给更一般的灵敏度信息。以k=(3/8)(1−e⁻ᵀ)、γ=20991/21119、ℓ=log(E(m₀)/η)>0，有

\[
-k<(\log E)'< -\gamma k,
\qquad \frac{\ell}{k}<m_{\rm crit}-m_0<\frac{\ell}{\gamma k}.
\]

复核其符号：ρ=hy/[2(C+h−hy)]在(0,128/21119)内，所以乘−k后不等号反向；正长度积分和除以正数给上述开夹界。它有助于把将来已有的参数必要下界与控制预算作符号比较；在没有ℓ或实际导数要求的新证据时，不能单凭夹界宣布参照可行/不可行，也没有支付任何空间导数或全窗残差输入。

现有H上下界已足以做更直接的粗筛。H上界2695275/16主要在CC中支付η<E(m₀)，保证正临界点存在；以下统一排除界只需H下界、旧η下界与P.18的代数常数。故CB是本次价值审计的对象，不是下面屏障的必要证明依赖。

## 2. 唯一筛选推论：m≥9/2时共同预算为空

沿用

\[
T=5/2,\quad m_0=19/5,\quad C=49/128,\quad
A(m)=A(m_0)+\tfrac38(m-m_0),
\]
\[
H_0:=H_{m_0}(T),\quad
k:=\tfrac38(1-e^{-T})>\tfrac{11}{32},
\quad H_m(T)=H_0e^{k(m-m_0)}.
\tag{BA.1}
\]

最后的严格界来自P.12的e⁻ᵀ<1/12；H比值是原定义的精确恒等式。UE/MB保证Lₘ(T)>1、f(T)>1，因此

\[
0<g_m(T)=\frac{(1-L_m(T)^{-1})e^{-2T}}{f(T)}<\frac1{144}.
\]

P.18已有不等式的纯代数部分为

\[
\frac{441}{2}\left(\frac{27}{640}\right)^2-C
=\frac{7889}{819200}>\frac1{144},
\tag{BA.2}
\]

其中最后一步是7889×144=1136016>819200。这里复用该有理恒等式和严格比较，不复用P.18针对某个旧ε的失败结论去替代任意m的证明。联合gₘ界，对每个m≥m₀统一有

\[
E(m)H_m(T)
=\sqrt{\frac2{441}(C+g_m(T))}<\frac{27}{640}.
\tag{BA.3}
\]

旧P.14–15、CE及UE给H₀>2269215/16。FULL_NODAL_RESIDUAL_OUTCOME及其已接受终审给的是**完整原参照残差**的下界，故

\[
\eta>2.38018447116\times10^{-7}
>\frac{119}{500000000}.
\tag{BA.4}
\]

后一个分数只是将已接受下界向下放宽，未选新残差预算；不涉及失败M₂运行。

若某m≥m₀存在共同预算η≤ε≤E(m)，BA.1–4给

\[
\eta H_0e^{k(m-m_0)}\le E(m)H_m(T)<\frac{27}{640},
\]
\[
e^{k(m-m_0)}
<\frac{337500000}{270036585}<\frac54.
\tag{BA.5}
\]

这里2269215×119=270036585；最后的严格比较为
4×337500000=1350000000<1350182925=5×270036585。没有计算e的任何新值。

对x>0，由1/(1+x)=1−x+x²−x³/(1+x)积分得到

\[
\log(1+x)<x-\frac{x^2}{2}+\frac{x^3}{3}.
\]

取固定证明隔板x=1/4，log(5/4)<43/192。由BA.1和BA.5，

\[
m-m_0<\frac{32}{11}\frac{43}{192}
=\frac{43}{66}<\frac7{10},
\tag{BA.6}
\]

最后仅用430<462。因此得到本轮唯一的排除推论：

\[
\boxed{\ m\ge\frac92\ \Longrightarrow\quad
\nexists\varepsilon>0:\ \eta\le\varepsilon\le E(m).\ }
\tag{BA.7}
\]

CC、MB给出的mcrit本身满足η=E(mcrit)，所以同一推论亦写成m₀<mcrit<9/2。虽然UE允许ε=E(m)在终点取等，BA.3–6仍为严格不等式；m=9/2这个端点也被排除，不能凭控制式允许等号逃开。本文未计算mcrit的数值或声称此粗上限最优。

## 3. 对当前固定参照有用和无用的范围

有用之处是：提高μ₂来覆盖导数并非无代价。固定μ₁=19/5、μ₃=6及此显式函数族时，所有m≥9/2已被旧节点需求与控制预算共同排除；不必为这些参数再做同一种上解预算试探。这是整片参数区域的解析排除，不是评估E(9/2)后的试点或参数扫描。

当前尚未有这里所需的实际导数必要下界，证明该参照必须使用m≥9/2。既有单段‖D²v‖∞,F≤3833/500是上界，不能反过来声称m至少这么大；而且它本身也不是全窗指数包络。临时M₂运行的任何Q₂、D、判定或派生量均未用于本文。

同样，m<9/2不认证实际参照的导数包络、全窗r₀/r₂或其它后验假设。这里排除的是此指定函数对取满包络并同时覆盖旧节点需求的组合；较小实际系数、其它控制函数、其它后验方法和真实NS解不在排除范围内。当前参考场筛查因此只得到一个已知排除区，未得到整个指定族对该场不可能，也未得到可行证书。

本推论没有修复上游生产成本证据缺口，没有追认失败M₂运行，整体producer_resource_complete、resource_complete、certificate_ready、release_ready继续为false。不新增正式包或发布动作。所有常数比较与对数不等式为正文手推；工具仅用于读取、写稿和SHA。

## 4. 实际来源与阅读范围

P/CC/CE/MB/UE/CB的定义及本文所用证明段已实际读取；对应根审查用于确认既有接受边界。旧完整节点OUTCOME/终审只读取原残差显示、η下界及其适用范围，未读取其数组或重新执行旧核。旧单段导数OUTCOME只用于辨别上界与下界。下表SHA定位实际字节，不代替任何科学复算；CB虽列入阅读绑定，并非BA.1–7的必要依赖。

| 实际输入路径（相对反向树） | SHA-256 |
| --- | --- |
| `research/reverse/fixed-seed-global-screen/PARAMETRIC_COST_LEMMA.md` | `bcbb265b0b9639d2fcae54dddee5415cce0cec62f1874d008dc389d2ae7ea2cf` |
| `research/reverse/fixed-seed-global-screen/CONTROL_FAMILY_NODE_COMPATIBILITY.md` | `4f37255af866f4bdeb8f2be9e11a4be76c70a90c994904c2b9934c537b0dac12` |
| `research/reverse/fixed-seed-global-screen/CONTROL_AND_INCREMENT_ROOT_REVIEW.md` | `7d4b2c9eb29ed11036ffa878d0e90d7c4d946d6ab95a5232c495c1cb05c5cc56` |
| `research/reverse/fixed-seed-global-screen/CONTROL_FAMILY_ENDPOINT_LEMMA.md` | `bfc2a232188fc838078d9f4036c4b7b0fb684d881f72644c9f0996eaef2c691d` |
| `research/reverse/fixed-seed-global-screen/NODAL_VS_CONTROL_INTERFACE.md` | `59d06565ff7cb693b6e5a63eb306b25b2009b4cb19ed5914c7453bb118ad8439` |
| `research/reverse/fixed-seed-global-screen/M2_CONTROL_BUDGET_MONOTONICITY.md` | `750262253c2e90f35ea15713438bf76bf08c752eed2ed94d2370d83d30f0b3ba` |
| `research/reverse/fixed-seed-global-screen/M2_CONTROL_BUDGET_ROOT_REVIEW.md` | `9601cee1282fb4ffd57c42ad75084fd922ed8c819980bebcfbad717639189c6a` |
| `research/reverse/fixed-seed-global-screen/M2_CONTROL_FAMILY_UNIFORM_ENDPOINT_LEMMA.md` | `9170e28436fdf0ee9c47978a66f6df23000cc2bafe2b58c08d75abb989dfcf4c` |
| `research/reverse/fixed-seed-global-screen/M2_CONTROL_FAMILY_UNIFORM_ENDPOINT_ROOT_REVIEW.md` | `41252e116b7f31654e655b75ab987da6d6980e6583110eb5c47d6d11d9d61ccd` |
| `research/reverse/fixed-seed-global-screen/M2_CONTROL_CRITICAL_PARAMETER_BRACKET.md` | `46cdb53fbfd1f033f011b54fa62da5b1217b55db713a4611460c4904e7409484` |
| `research/reverse/fixed-seed-global-screen/FULL_NODAL_RESIDUAL_OUTCOME.md` | `223c963e10ae14c93a231901dfe1554b8c61b63324537ebc250ddb7ae15d32ee` |
| `research/reverse/fixed-seed-global-screen/FULL_NODAL_RESIDUAL_FINAL_REVIEW.md` | `6d191cdb7be53601617754769b55b50be6346e5abfc2ca93083bf0518be7bc69` |
| `research/reverse/fixed-seed-global-screen/ONE_SEGMENT_DERIVATIVE_OUTCOME.md` | `ac2e7737600b1584da1ed47197335e84dedae4dc61659eae667847391acaa81f` |
