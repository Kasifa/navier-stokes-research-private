# FA 返回接口笔记的独立复核

2026-09-07。PRIVATE_CORE。审查者不是 CONTRACT、ROOT_INTERFACE_NOTES 或 INDEPENDENT_INTERFACE 的作者。实读这三份全文、clay_b_frequency_activation_20260907.md 全文，并定向读取 R0.10 §2、§7 和 R0.11 §3、§6–7 的本地原始正文。

裁决：**LIMITED PASS — 四中心代数、有限宽误差、来源适用性和中心返回失败的限定结论通过；关于无限维余项的措辞和 ROOT 比例估计的分母步骤均已实读修订并关闭。** 当前无待修审查项。本报告不是新定理、完整第二代机制或冻结包。没有重跑旧证书、扫描参数或调用外部新定理。

## 1. 四中心、符号和两个有序区域

记 a=3/2，p=ae₁，q=ae₂，A=e₂，B=e₃，κ₀=σp+τq，其中 σ、τ∈{±1}。本节 τ 是符号，不是时间。FA 的非线性源采用正号

\[
 \Gamma_F=\chi(D)P_L\operatorname{div}(F\otimes F),
\]

实际 NS mild 方程对该源取负号。对输出 κ=κ₀+β，第一有序区域取 ξ=σp+α、η=τq+β−α；第二有序区域经过交换 ξ、η，可使用相同的标量权重。两项相加的完整核是

\[
 K(\xi,\eta)=P_{\xi+\eta}
 \big[(\eta\cdot P_\xi A)P_\eta B
       +(\xi\cdot P_\eta B)P_\xi A\big].
\]

由于各输入投影无散，这也等于直接由 div(F⊗F) 得到的核；没有以未投影极化代替有限宽中的实际 PξA、PηB。中心处

\[
 K(\sigma p,\tau q)
 =P_{\kappa_0}[(\tau a)e_3+0]=\tau a e_3.
\]

这证明 INDEPENDENT_INTERFACE 的 I.1 与 ROOT 第9行系数正确：两个有序区域已经包含在括号的两个加数中，第二个中心加数为零，不再乘以2。四个中心 p+q、p−q、−p+q、−p−q 的主项依次为 +iae₃、−iae₃、+iae₃、−iae₃，均再乘 Iψ/(2π)³。相反中心互为共轭，实值条件相容。实际解领先输出的整体负号也已在 I.5 保留。

## 2. 有限宽 I.2 与乘子支持

FA.8 只要求固定 ψ 光滑、紧支撑、非零、实、非负、偶；没有径向条件。上节两个有序区域的变量交换不要求 ψ 径向，甚至不要求偶性。非负性用于

\[
 J_\delta(\beta)=\int\psi_\delta(\alpha)
                 \psi_\delta(\beta-\alpha)\,d\alpha\ge0
\]

以及把核误差的绝对值压到 CδJδ；偶性在 β=0 时给 Jδ(0)=∫ψδ²=Iψ>0，并保证 FA 种子实值。原稿在有限宽误差里没有偷偷添加径向假设，**PASS**。

所有输入和的中心只有0、±2p、±2q以及四个 κ₀，其扰动半径至多2δ。设 χ=1 的开环包含半径3/√2的球面；它给出一个严格正的径向距离余量 rχ。取固定 δ 足够小，使2δ<rχ，四个目标小球不交，同时

\[
 2\delta<2.05,\qquad 3-2\delta>2.2.
\]

则各目标小球上 χ=1，0及±2p、±2q附近被 χ 排除。这里并未数值指定 rχ 或 δ，符合 FA“固定一个充分小δ”的量词。由远离零频，K 对两个频率在这四组紧邻域一致 Lipschitz，故

\[
 |K(\xi,\eta)-\tau a e_3|\le C\delta.
\]

和非负权重积分后，恰得 I.2 的逐点 Fourier 误差。支持条件也说明没有遗漏其它和频到目标叶的贡献。不能反过来说正时间的整个 Q_Nu 或全部真实新生场也只支持这四个小球；这一支持结论针对初始源 Γ_F。

固定δ时，输入/输出投影仍有偏离，ψ仅偶不足以迫使所有横向偏差在中心精确相消。因此 I.1 仍是主项加O(δ)，不是精确中心极化恒等式。原稿对此已有正确限制。

## 3. ROOT 的法向外 L² 比例：非零分母补核

ROOT 第21行的O(δ)比例不能仅靠误差上界；还需要总输出的非零主项下界。这个下界可由 I.2 直接建立，无需数值积分或新δ扫描。

令 P⊥=I−e₃⊗e₃，常数 C 取四个目标误差界的最大值。四叶不交，因此其中心主项的 Fourier L² 范数是

\[
 \|\widehat L_\delta\|_2
 =\frac{2a}{(2\pi)^3}\|J_\delta\|_2,
 \qquad
 \|\widehat\Gamma_F-\widehat L_\delta\|_2
 \le\frac{2C\delta}{(2\pi)^3}\|J_\delta\|_2.
\]

Jδ 连续且 Jδ(0)=Iψ>0，所以∥Jδ∥₂>0。对上述足够小δ再要求 Cδ<a，有

\[
 \|\widehat\Gamma_F\|_2
 \ge\frac{2(a-C\delta)}{(2\pi)^3}\|J_\delta\|_2>0,
\]

\[
 \frac{\|P_\perp\Gamma_F\|_{L^2(\mathbb R^3)}}
      {\|\Gamma_F\|_{L^2(\mathbb R^3)}}
 \le\frac{C\delta}{a-C\delta}
 \le\frac{2C}{a}\delta\quad(C\delta\le a/2).
\]

Parseval 的共同因子在比例中抵消。这支付了最初审查时 ROOT 省略的分母步骤；该步骤现在已写入 ROOT 第21行，并经本审查实读核对。它支持的是**Euclidean 初始源**法向外比例结论，没有给一个数值δ阈值，也没有把固定未数值化δ的所有可能返回状态排除。

这个下界不是δ一致的正大小界：由定义 Jδ(β)=(ψ*ψ)(β/δ)，有∥Jδ∥₂=δ^(3/2)∥ψ*ψ∥₂。比例成立与绝对输出的δ尺度是两件事。将它用于周期 G_N 或正时间实际输出还须纳入 FA.11、FA.14 的误差，不能在 ROOT 第21行把三种对象混写为同一个“完整输出”。

## 4. 等长门的来源与中心返回判定

独立使用 p=(c,s,0)、q=(c,−s,0)，c,s>0，写 U=u(−s,c,0)+xe₃，V=v(s,c,0)+ye₃。直接相加得到

\[
 (q\cdot U)V+(p\cdot V)U
 =(-4cs^2uv,0,2cs(vx-uy)).
\]

P_(p+q) 去掉第一分量，故 I.3 的符号、常数2cs以及落在span(p×q)中的结论正确。这正是 R0.11 §3 引理1的原命题；R0.10 §7 命题4是其较早的具体中心计算。笔记没有把一般引理归为本轮新结果。

R0.11 §6 命题3还要求 C_(p,−q)(U,conj V)=0。FA 中 A、B为实，实际该核为−iae₃≠0。因此此命题的差频零假设不满足，不能拿其“两个反向输入线都不能保持”作为 FA 的定理结论。R0.11 §7的缺陷常数也属于不同网络。两份笔记已正确分开这些来源，**PASS**。

r₊=p+q 与 r₋=p−q 等长且正交，故仅频率中心的形状相容；四中心主极化都在span(e₃)，而FA输入 A、B线性独立。共同正交变换、非零幅度/相位及置换不能增加极化张成空间的维数，中心模型不返回同一个FA输入模板。一般旋转、放大只在此比较几何，不自动是固定环面的晶格变换或固定黏性的动力学对称。

只保留中心模型时，每一个有序项都有 e₃·ℓ=0，纯第一代自对流逐项为零，包含差频及零频。有限δ时频率和极化均偏离，不能把中心 I.3/I.4直接施于各个不等长微观频率对，更不能宣称 B(G_N,G_N) 恒零。现有笔记保留了这些边界。没有据此证明所有有限宽返回、所有极化模板或一般奇性都不可能。

## 5. 实际 FA.14、光滑乘子与量词

原文 FA.11 明确处理周期影像乘积，得到未归一化扩大环面 L² 中

\[
 \|G_N-d_N^2\mathcal S_N\Gamma_F\|_2\to0,
 \qquad\|G_N\|_2\to\gamma>0
\]

（固定种子后令N增大）。它没有声称每个中心系数完全相等。原文 FA.12–14 给完整原解的统一H⁵窗，以及

\[
 \|\mathcal Q_NU_N(s)+sG_N\|_2\le C_0s^2.
\]

I.5 对符号、范数、正黏性 ε_N=νN^(−1/2)、热项和N一致性的转述准确。这是已经支付的一次激活的全频率真实解余项，不是有限中心截断或单独第一 Picard 近似。

若比较法向外比例，写 \(R_N(s)=\mathcal Q_NU_N(s)+sG_N\)，则在C₀s<∥G_N∥₂时，直接有

\[
 \frac{\|P_\perp\mathcal Q_NU_N(s)\|_2}
      {\|\mathcal Q_NU_N(s)\|_2}
 \le\frac{\|P_\perp G_N\|_2+C_0s}
           {\|G_N\|_2-C_0s}.
\]

因此不能完全忽略 FA.14 对向量状态接近性的已有信息；它确能传递这种L²意义的结构界。缺的是认证所需返回模板、按供给来源分拆、接收时间和下一阶段演化的完整合同。目标乘子支撑在固定尺度的紧频带，也可把其L²误差转成固定阶目标带Sobolev误差；这仍不同于下一门的全部状态合同。ROOT 修订后的第23行已写入上述正时间比例及目标带Sobolev提升，并明确保留FA已有状态信息与完整无限维余项；实读核对通过。

χ是光滑乘子且未假设幂等，故一般Q²≠Q；它不是一组代际正交投影中的成员。即使代数上写u=Qu+(I−Q)u，也不能把相应能量视为无交叉项的代际能量，或把所有高尾改称前一代。第一代自作用与种子混合项、其它新生场必须在同一解的完整Duhamel式中另行核算。

固定δ后，FA的常数对N一致，不等于已经证明δ→0、下一代返回或无限迭代一致。FA.16 回到固定环面/黏性后，初值和时间窗均随N改变。其原始量词是每个充分大dyadic N存在各自光滑初值的一次激活；不存在把这些解族拼成一个固定初值无限轨道的许可。

## 6. 具体修正与通过范围

1. **CLOSED — 余项措辞已修正：** 重新实读 INDEPENDENT_INTERFACE.md 全文，核对第164行已改为“跨代及无限迭代的统一误差控制”，并明确“FA.14 已证的一次激活完整无限维余项保持有效”。I.1–I.5的数学内容保持，最初指出的范围歧义已消除。本审查未修改该文件。
2. **CLOSED — 分母及状态信息已落实：** 重新实读 ROOT_INTERFACE_NOTES.md 全文。第21行已包含Jδ(0)>0、四叶不交、Cδ<3/2、总Fourier L²下界、比例Cδ/(3/2−Cδ)以及绝对主量δ^(3/2)尺度；第23行已包含正时间比例的正分母条件、FA.14的向量L²信息和固定阶目标带Sobolev提升。代数及适用对象与本报告第3、5节一致，没有增加数值δ、错误的δ一致性或完整返回结论。
3. **结论限定通过：** 现有来源尚未给出完整返回合同；中心主项不能返回FA的两独立输入极化，有限宽完整机制保持未裁决。这个来源接口审计可以结束，不等同于新的NS排除定理或需要冻结的新成果。

上述修正已关闭；所列手算和来源命题适用性未发现待修代数错误。限定PASS仍只覆盖本接口审计，有限宽完整机制和返回合同保持未裁决。本报告不审计FA全部独立证书，不依赖新增外部论文，不作新颖性或Clay声明。

## 7. 实际输入 SHA-256

下方绑定本次审查实际读取的原始文件字节。两份修订笔记在全文重读并核验上述具体修正后更新绑定；其余四项与初审字节一致，已再次核对。仅生成文件哈希，没有新增科学数值计算；若来源再次修改，此报告对新字节不自动通过。

```json
{
  "schema": "return-interface-review-inputs-v1",
  "timestamp_utc": "2026-09-07T14:35:41.366928+00:00",
  "worktree": "/Users/kasifa/Documents/Math/navier-stokes-reverse",
  "inputs": [
    {
      "path": "research/reverse/return-interface/CONTRACT.md",
      "bytes": 2040,
      "sha256": "e647b416ef4c310b0b6501d8b49e01adfe1c866f8bd9e9dd937b87f24c3aaa3a"
    },
    {
      "path": "research/reverse/return-interface/ROOT_INTERFACE_NOTES.md",
      "bytes": 4103,
      "sha256": "03deb65a173e254832e298dfe31c3fc8e8c82fe38d996e9bab33dfaaece7bab7"
    },
    {
      "path": "research/reverse/return-interface/INDEPENDENT_INTERFACE.md",
      "bytes": 11402,
      "sha256": "610b9da62651deb5caed543bb8d2f9d721f98062f2719c3f82bc2d3220d5c787"
    },
    {
      "path": "research/clay_b_frequency_activation_20260907.md",
      "bytes": 12364,
      "sha256": "42bbc2ba3abae7aa1eeb25ee0b29f896d7d8ddcafccb0da518dded4851dd897a"
    },
    {
      "path": "public/notes/r0-10.html",
      "bytes": 31861,
      "sha256": "d7566fd57a4b8198a866ff3d317ef15bcd1b6671054c964f8875b00635145a0a"
    },
    {
      "path": "public/notes/r0-11.html",
      "bytes": 29207,
      "sha256": "ad8ebe34c67939cd371f621cc7fbf5f54cf501c4d2506e587aa1494f4ef52095"
    }
  ],
  "external_sources_newly_read": [],
  "scientific_numerical_computation": false,
  "root_notes_latest_time_symbol_and_nonidempotence_read": true,
  "correction_reread": {
    "status": "CLOSED_LIMITED_PASS",
    "full_files_reread": [
      "research/reverse/return-interface/INDEPENDENT_INTERFACE.md",
      "research/reverse/return-interface/ROOT_INTERFACE_NOTES.md"
    ],
    "previous_bindings": [
      {
        "path": "research/reverse/return-interface/ROOT_INTERFACE_NOTES.md",
        "bytes": 3587,
        "sha256": "f00e7ca6daf23c72694581393cdf775004c6f70db1e4de3491595cf3c56e08be"
      },
      {
        "path": "research/reverse/return-interface/INDEPENDENT_INTERFACE.md",
        "bytes": 11318,
        "sha256": "105b8f41583771500dd6743b53668c5f7db069bb1ba594a2137bb89ed6217634"
      }
    ],
    "unchanged_other_inputs_verified": 4,
    "remaining_review_fixes": []
  }
}
```
