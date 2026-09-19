# 完整热交换差：三稿联合非作者审核

2026-09-20，PRIVATE_CORE；恢复后完成此前中断的审核。本次仅新增此审查，不改三份被审稿或第34包停止稿。

**结论：算子接口及根稿后续条件推论通过；实际小非线性传递仍为 INPUT_NOT_QUALIFIED。** 独立稿 RTI.1–11 支付根稿 RT.2，可明确取 \(K_0=(1+\sqrt2)(c_1+2c_3)\)。未发现需修正的数学错误；不接受实际残差非零、趋零或无力机制结论。

本人是前项 AXIS_LABEL_SOURCE 的作者及既有热接口/增长范围审查参与者，不是本题 ROOT_INPUT_CHECK 或 INDEPENDENT 的作者。先读根稿、后读独立稿；合同已有根的桥积分思路，根成稿前亦收到独立作者常数/幂次消息。此为非盲非作者 AI 审查，不是人类同行评审或额外一份互盲证明。
三稿保留2026-09-09形成时的条件/待审核措辞；本次2026-09-20实际全文重读及下列逐式检查才关闭算子待证条件，不回写其历史身份。

## 逐式核查

1. RTI.1–4：单位环面、\(\xi_k=2\pi k\)、\(P_0=I\)、有序无共轭张量及 Frobenius 范数一致。Gaussian 一、三阶导数式和周期化 \(L^1\) 缩放成立。RTI.3 积分项符号为 \(-i\xi_i\xi_j\xi_\ell e^{-a|\xi|^2}/|\xi|^2\)，与直接散度合成完整 Leray 投影；零模均为零，不作零除。
2. \(\int_a^\infty b^{-3/2}db=2a^{-1/2}\) 支付全算子积分；全导数张量收缩用 Cauchy–Schwarz，不漏额外维数因子。因此 \(C_L=c_1+2c_3\) 对所有 \(a>0\) 有效，含全部周期像与大热时尾；没有使用错误的裸 \(P:L^\infty\to L^\infty\) 有界性。
3. RTI.5–7：桥积分中令 \(u=y-z,v=y+z\)，\(dy\,dz=2^{-3}du\,dv\)，Gaussian 乘积恰变成 \(g_\rho(u)g_\rho(v)\)。完整周期延拓与正核可积性支付 Fubini，热后乘积等于 \(S_{\rho/2}H_\rho\)，包括零频、反向频率及全部相位；\(\sqrt2\) 正来自半热时，故 RTI.7 常数正确。
4. RTI.8–9/RT.1–2：精确保留 \(Q_\rho(B,E)+Q_\rho(E,B)+Q_\rho(E,E)\) 及三个负号热后乘积。范数中的2来自两个有序交叉，不是张量相等假设。B/E 均可非无散、非零均值；E=0、B=0和常值抵消边界正确。所得是上界，不含非零下界。
5. RTI.10–11/RT.3：固定 \(\rho=\tau/\lambda_p^2\) 给 \(\rho^{-1/2}=\lambda_p\tau^{-1/2}\)，归一化交叉幂为 \(A+1-\tfrac12-2A+\epsilon=\epsilon-h\)，EE幂为 \(2\epsilon-h\)。取 \(\epsilon=h/4\) 得 \(-3h/4,-h/2\)，速度因子/时间因子均未混淆。
6. 保留旧较锐 \(h/2\) 及对数幂只得交叉 \(\tau^{-h/2}(1+|\log\tau|)^P\)、EE的 \((1+|\log\tau|)^{2P}\)。这些不衰减上界不足以证明目标趋零，也不能证明其不趋零；\(\epsilon>h\) 仅是此绝对估计的一种充分小阶条件，非必要条件。
7. RT.4：全周期核给 \(\|\Delta S_\rho E\|_\infty\le c_\Delta\rho^{-1}\|E\|_\infty\)，因此归一化为 \(c_\Delta\lambda_p^2C_E\tau^\epsilon\to0\)。这不调用未滤波 E 的导数。B 对应界仅有界，不付极限或非零性。
8. 源项仅在原 F 具有闭时间光滑周期资格的条件下使用：充分高阶 Sobolev/Fourier 控制使 \(\sup_{[0,1]}\|PF\|_\infty<\infty\)，再用热收缩得 \(\tau^{A+1}\|S_\rho PF\|_\infty\to0\)。这是该外部资格的条件应用，未新增全文原文认证，亦非裸 P 的 \(L^\infty\) 估计。
9. 由旧 HI.2 的 \(\rho'=-1\) 身份，RT.5 完整为 \(G_h=S_\rho PF-\Delta S_\rho B-P\operatorname{div}C_\rho(B)-\Delta S_\rho E-P\operatorname{div}D_\rho\)。黏性负号和全部混合项齐全；没有漏项后再把 B 当作实际无散 NS 轨道。只含 B 的两项不能称其独立 NS 残差。

## 实际读取与来源绑定

以下三份本题稿本次均全文读；旧稿本次仅复读列示段落并核当前字节，不声称重审旧包。路径以 research/reverse 为根。

| 文件 | 本次读取范围 | SHA-256 |
| --- | --- | --- |
| heat-residual-transfer-preflight/CONTRACT.md | 全文 | 17e94e397c9832de1c3e9fe5c49038403cffef564da01dd92e88365dd98c427f |
| heat-residual-transfer-preflight/ROOT_INPUT_CHECK.md | 全文，RT.1–5 | bc0d50ba62c9a3c6f7c45259a7f8b9e33967b758249c3eb4d19c3259d0d352a0 |
| heat-residual-transfer-preflight/INDEPENDENT.md | 全文，RTI.1–11及来源 | d0da8a4c48ff1881121b310244b04f2470dabeadcc00e90f6cb1f7072db4ff4b |
| heat-vorticity-tail-preflight/MAIN_TERM_AND_IMAGES.md | 第17–28行，MG.2 | bb25839f76bfab719b3bca7afed9a724c624a4a172a1fc55bff684975cc3fc7a |
| heat-vorticity-tail-preflight/WEIGHTED_ERROR_INDEPENDENT.md | 第70–112行，WE.8–12 | fb7a2f8284f2f1a838306e3a68f9a2ae7cb6cf76a9a63b574d05832eb8f38018 |
| heat-vorticity-tail-preflight/ROOT_INTERFACE.md | 第21–37行，HI.2–3 | 909ccebe0c56d9cb0845a9eca6be78fb42c082e7671f5a6030529fc1b505d491 |

旧 MG.2/WE.10 的全空间界结合固定速度缩放与支撑不交，给本题整个周期 B/E 界；不能用单点高斯增长结论代替它。旧来源及其外部构造资格仍按原接纳范围使用，本次未读新外部论文或认证其完整证明。

**最终范围。** 已支付完整热算子传递界、同一尺度的线性误差及条件光滑源项；尚缺完整有符号非线性交换差与主阶黏性/通量的共同控制，允许实际消去。没有强残差小量、强稳定、无力尾段或原固定 \(2\pi\) 环面单一 \(a_*\) 的轨道结论；单位环面外部比较场不替换原数据。经典核方法不作新颖性宣称，CIV 适用性筛选未在本审查预付。

本稿完成后全文自读并停止修改；科学程序、数组、FFT、Lean、参数扫描、Git及外发均0。审查自身不自绑定，最终 SHA 随交付报告。
