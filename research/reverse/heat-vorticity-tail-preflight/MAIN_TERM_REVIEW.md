# 主项向量卷积与全部周期像：非作者审核

2026-09-09，PRIVATE_CORE。**PASS（主项及周期像的条件接口）**；下列两处定义域／组合条件意见已由作者修正并实际重读关闭。第1步完整加权余项仍未在本审核中支付，不能把此 PASS 记成实际热补全增长、无力性或奇性已证。

本人 Hume（coherence_review_resumed）不是 MAIN_TERM_AND_IMAGES 作者，曾审核前两轮规范补全、热接口和来源范围，已知本合同的先验提示；属于非盲 AI 非作者逐式审核。未读第1步任何新形成稿或刚停止的 AXIS_LABEL_SOURCE，不用其未知结论补证本稿。

1. **MG.1 同尺度周期核通过。** 同一 \(\lambda_p\)、\(\tau=\lambda_p^2(1-t)\) 与原 \(t_0\) 保持不变。展开完整单位周期热核、对紧支撑原场换元时，热核的 \(\lambda_p^3\) 和体积元的 \(\lambda_p^{-3}\) 相消，只剩原速度的 \(\lambda_p\)；像平移为 \(\lambda_p n\)，无遗漏量纲。固定时刻紧支撑／光滑与 Gaussian 像和使积分、求和绝对收敛。受审初版将式写为“任意 \(t<1\)”会调用 \(t<t_0\) 的负原时间；现准确限于 \(t_0\le t<1\)，早期直接由原周期定义 \(U=0\) 处理，没有新延拓物理轨道。
2. **MG.2 的全空间主控通过。** Theorem4.6(i) 的闭有限剖面矩形确包括轴及 \(\eta=\pm1\)：\(E=\sqrt{2X}F\)，且 \(V_0/\sqrt{2X}=\sqrt{X/2}(V_0/X)\) 在轴取零极限。外区 \(U_{\rm pr}=V_0=0\)，(4.29) 的正积分给 \(0<H(Z)\le1\)，故 \(E\le c_\infty X^{-A}\)；与有限矩形界拼接得同一有限 \(M_0\)。由 \(q\ge\tau\)、\(A=1/2+h\) 得两切向分量的归一化因子至多1，径向因子至多 \(\tau^h\)。Euclidean 范数由三分量绝对值和控制，无隐藏维数常数；已有 cutoff 乘积的零延拓给整个原空间的统一主控，不借(5.42)外推到轴。
3. **MG.3–5 支配收敛通过。** 固定 \(Y\) 后 \(|\eta|\le\tau^h|Y_3|\to0\)，从 \(\tau=q(1-\eta^2)\) 得 \(q/\tau\to1\)、\(X\to|Y_h|^2/2\)；同一固定 cutoff 最终等于1。径向分量由统一 \(\tau^h M_0\) 趋零，其余两分量按闭剖面连续性收敛，轴可用 Cartesian 代表或零测集处理。换元 \(y=\sqrt\tau Y\) 后核与体积元准确抵消 \(\tau^{\pm3/2}\)，完整 Gaussian 乘 \(M_0\) 可积，覆盖轴、无穷远及 cutoff 外零延拓。故这是全向量支配收敛，不是仅在一条剖面路径作形式极限。
4. **MG.6–7 的完整方向与严格正性通过。** \(e_\theta\cdot e_2=\cos\theta\)，轴向分量对 \(e_2\) 为0；径向分量已由上述极限支付。积分 \(Y_3\) 给 \((4\pi)^{-1}\)，平面 Jacobian 为 \(r\,dr\,d\theta\)，偏心核的角参数恰 \(b=rR/2\)。另一半圆平移 \(\pi\) 给稿中两指数之差；当 \(b>0\) 时在该半圆内部严格正。原 \(R=\sqrt{2X_{\rm in}}>0\) 与 \(E(r^2/2,0)>0\) 使 \(I>0\)；Gaussian 主控又给有限性。没有把正标量当作向量正性，也没有求 I 数值或另选增长点。
5. **MG.8 的全部像通过。** 固定支撑间隙及晚时 \(|x_\tau|_\infty\le d/2\) 给每个 \(\|n\|_\infty=m\ge1\) 的距离至少 \(\lambda_p m/2\)。该层像数为 \((2m+1)^3-(2m-1)^3=24m^2+2\)。置 \(a=\lambda_p^2/16\)，\(m^2\ge1,\tau\le1\) 给 \(am^2/\tau\ge a/(2\tau)+am^2/2\)，准确产生 \(e^{-a/(2\tau)}C_p\)；\(C_p\) 为收敛的完整无限 Gaussian 和，没有有限像遗漏或计数实验。
6. **原能量及像余项通过。** 在对应同一时刻，分离支撑给 \(\|U\|_2^2=\lambda_p^{-1}\|u\|_{L^2(\mathbb R^3)}^2\)，故 \(\|u\|_{L^1(K)}\le|K|^{1/2}\lambda_p^{1/2}E_F\)。主项的 L¹ 界为 \(|K|\|c\|_\infty M_0\tau^{-A}\)，误差用两者之和。乘 MG.8、\(\tau^A\) 与速度因子 \(\lambda_p\) 后，任意留下的固定幂均被 \(e^{-a/(2\tau)}\) 控制，三者全部非零像都是 \(o(1)\)。这里实际 u 的像界由完整 L² 能量支付，不再要求未知点态增长上界；零格像实际误差仍未因此受控。
7. **条件组合分支已修正通过。** 初版把“归一化误差趋0”与“严格小于 I 的界”笼统接到精确极限及半值下界，前提不够。最终§5已区分：趋0才给 \(\tau^A V_h\cdot e_2\to\lambda_p I\) 和晚时 \((\lambda_p I/2)\tau^{-A}\)；仅有误差范数 \(\limsup\le b<I\) 时，只得归一化分量 \(\liminf\ge\lambda_p(I-b)>0\)，须按实际余量另定下界。两种条件均未被本稿宣称已付，也不声称是所有增长证明的必要条件。

本轮全文读 GAUSSIAN_GROWTH_CONTRACT 16行、主稿初版及两次修订后的最终80行；最终 SHA 见下表。定向实读原抽取文本329–401、1201–1294、1593–1656行（§3.1、坐标／(4.3)–(4.5)、Theorem4.6(i),(v)含相邻段），另复读6051–6117行 Cor10.6 与既有 canonical PROOF 第38–49行能量步骤。实际视核既有第33页图，无新渲染。没有重审 Theorem4.6 全构造、完整原文或形成中的加权误差证明。

| 实际来源（相对 research/reverse/） | 最终 SHA-256 |
|---|---|
| heat-vorticity-tail-preflight/GAUSSIAN_GROWTH_CONTRACT.md | 475770a0b7bfc8927bf282aaf9aebfa567a49575b53287e2a217ff4ed699737d |
| heat-vorticity-tail-preflight/MAIN_TERM_AND_IMAGES.md | 9a85d8647a8a330da2b0d2a64b7810dba0d25ebe6c5ba0aa068d2ff7412c228f |
| canonical-periodic-tail-preflight/PROOF.md | 545fee812f2b7ef96c51029e9234b9869815c4a8312236e5726b54a482042453 |
| forced-tail-audit/sources/navier-stokes.pdf | 0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f |
| forced-tail-audit/sources/paper-text.txt | 7c8d1e236e6285de297f4d88d05056f3de5a8bdcc6454ddc81b665cf98ae0c26 |
| localization-tail-preflight/reading-evidence/independent/pdf-page-033.png | f54f3937ea11ca9fd87c2c576e22515eb9c354328f1b5e360fe2b9cbd64ae5fd |

停止范围：只审核同一主项与完整周期像；剩余的是本充分证明路线的零像实际加权误差，不把它改称所有可能增长论证的唯一必要输入。原外部构造仍条件化，原 \(2\pi,a_*\)、\(\rho\)、\(\lambda_p\)、cutoff、剖面和初值未改。未接受实际增长、强稳定、无力残差或统一迭代。只写此文件；科学执行／数组／FFT／Lean／新图／Git／外部发送均0。全文自读、核最终受审字节后停止修改。
