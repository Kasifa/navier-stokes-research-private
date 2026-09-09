# 规范周期补全：非作者逐式比较审查

2026-09-09，PRIVATE_CORE。**PASS：合同五项的条件证明链成立，未发现实质缺口。** 接受范围是这个固定规范补全的运动学性质、完整残差及弱界，以及 **CONDITIONAL_NO_CANDIDATE_FOR_A_FULL_UNFORCED_TAIL**；不是外部构造全文认证或一般无力奇性排除。

本人 Hume（coherence_review_resumed）未写受审两稿；曾写第32包另一条解析性推导并审核根解析稿，另参与本目录前身的 face、压力 jet 和低阶输入审查。本轮已知合同披露的先验提示，全文比较 root 与 Gauss 稿，属于非盲 AI 非作者审核，不称第三份盲证明。未读取尚在形成的 SOURCE_QUALIFICATION。

1. **同一对象与零模通过（CV.1、CTI.1–3）。** Cor10.6 的同一 \(\lambda>1\)、\(s=\lambda^2(t-t_0)\) 与 \(t_0=1-\lambda^{-2}\) 保持终时1；速度、压力、力的缩放分别为 \(\lambda,\lambda^2,\lambda^3\)，黏性不变。原数据早期为0使 \(t_0\) 拼接光滑。正支撑间隙支付原周期副本求和及原非线性分离，但不支付投影后交叉项分离。原 \(U\) 无散且在胞界邻域为0，胞内 \(\int\operatorname{div}(x_iU)=\int U_i=0\) 合法；未把 \(x_i\) 当周期函数。因此 \(m(Z)=-m(C)\) 严格给 \(V=U-H\)。完整物理 \(P_0=I\) 与显式速度均值归零没有混用，实值／共轭和无散均保持。
2. **W 的端点资格通过，仍为声明内的来源应用。** 根稿第2节对固定 \(\operatorname{supp}\nabla\chi_x\) 的覆盖完整：\(z\ne0\) 时 \(q\ge |z|^{1/D}>0\)，在保留上界 \(q<q_*/2\) 的紧邻域用 Theorem3.1(ii) 的 Cartesian 导数；\(z=0\) 时过渡区必有 \(r>0\)，由(10.3)令 \(X>X_{\rm ext}\)，实际 \(A\equiv0\) 给所有 W 导数恒零。有限覆盖、更高时间导数的 Cauchy 界及原零延拓间隙支付全单侧光滑性。第119页确有这两区与 \(A=0\) 的原文依据；没有调用(5.42)到轴上。固定缩放后用足够高 Sobolev 阶数控制全频加权和，再经有界 P 与均值项，给 H 每个固定阶范数有界；未假定 H 非零。
3. **运动学与能量通过（根第3节、CTI.4）。** 有界 H 使 \(\|V\|_\infty\ge\|U\|_\infty-\|H\|_\infty\) 保留原 limsup 无界。根稿从真实受迫 U 的完整能量等式、\(U(0)=0\) 及正则化平方根得到 \(\|U(t)\|_2\le\int_0^1\|F\|_2\)，故 V 的 L² 界成立；Gauss 将同一能量界列为来源条件，结论相容。其额外耗散句明确另需原 U 的积分耗散。两稿都没有给予 V 无力能量等式或新解存在性。
4. **完整压力与残差通过（CV.2、CTI.5–8）。** 零均值 \(q_V\) 的 Fourier 负号来自 \(-\Delta q_V=\partial_i\partial_j(V_iV_j)\)；\(\nabla q_V=-(I-P)\operatorname{div}(V\otimes V)\)。受迫原压力满足 \(-\Delta p_U=\partial_i\partial_j(U_iU_j)-\operatorname{div}F\)，所以 CTI.8 的 \(G_T*\operatorname{div}F\) 为正号，其余压力差由两负交叉和正 H 自作用构成，模时间常数正确。代入 \(V=U-H\) 得 \(-H_t+\nu\Delta H\)、两个负有序交叉及正自作用，未漏任何频率或压力项；\(t<1\) 时力均值0由原方程积分取得，而非改力零模。
5. **归一化弱界通过（CV.3、CTI.9–10）。** 全频 \(H^{-1}\) 权重 \((1+|\xi|^2)^{-1/2}\)、向量 Euclidean 与张量 Frobenius 范数给 \(\|P\operatorname{div}M\|_{-1}\le\|M\|_2\)、\(\|\Delta H\|_{-1}\le\|\nabla H\|_2\)，乘子常数均1。两个张量积各贡献 \(\|U\|_2\|H\|_\infty\)，自作用贡献 \(\|H\|_2\|H\|_\infty\)，准确得到系数2。单位胞归一化没有隐藏体积因子；这是有限上界，不是小残差、正下界或光滑延拓证书。
6. **开零涡量与整尾反证通过（CV.4、CTI.11及两稿末节）。** 逐模 curl 消去梯度和显式均值，故 \(\operatorname{curl}V=\operatorname{curl}Z\)；没有声称 curl 与速度缩放不带额外因子交换。Z 的固定严格内支撑保留非空开零涡量区，不强迫 V 在该区为0。若同一 V 在完整终端尾段 \(G_V=0\)，每个内部紧窗的光滑性先给 \(C A^0\) 与完整 Duhamel式，再从严格较早的同数据起点得到 V 的空间解析性。之后才对 curl V 用解析恒等原理，最后由全域无散、curl 为0和显式零均值逐模得 \(V=0\)，与临终无界矛盾。没有将涡量当另一个 NS 速度，也没有逆时间推理、统一临终解析半径或忽略常速度。

重新核已审解析来源的常数和识别：\(C_0=e^{1/(4\nu)}\)、\(C_1=e^{1/(2\nu)}/\sqrt{e\nu}\) 来自完整热乘子；\(X_d=C A^0\) 内加权上确界范数的完备性及可积 \((t-s)^{-1/2}\) 核支付压缩。条件 \(8C_1R\sqrt d\le1\) 同时支付球内映射和未加权同数据差的唯一性。受审两稿只复用这部分，不搬用旧速度开空区假设。零涡量加零均值的周期 Hodge 步骤是本题另付的一步。

**边界保持。** 只排除固定 \(t_*<1\) 后全域、全时段恒零的残差；不推出每个时刻 \(G_V\ne0\)，也不提供实际 H、涡量尾部或力下界。允许 H=0，不存在除零分支遗漏；较早的零运动短窗不与后续受迫增长冲突。不排除其他有涡量外尾的补全，也未支付改变轨道稳定性、原 \(a_*\) 的无限尺度或新的无力原解。外部来源的存在性仍为条件，不能用这次审查反向认证其166页或形式化证明。

本轮实际全文读 CONTRACT 32行、PROOF 83行、INDEPENDENT 127行及第32包 ROOT_ANALYTIC_PROOF 52行；原文新复读抽取文本第119、125页与第126页 Cor10.6 收尾（相邻 Appendix A 不作本题依赖），视核既有119、125页图。沿用紧前任务已实读第15、117–118页的 Theorem3.1／局部化段；不冒称本轮重审整篇。原文固定版本：[官方 PDF](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)。Gauss 的来源条件没有被其自述自动验收；本审核按上述原段核根给出的 W 资格链，其余外部构造仍条件化。

| 实际来源（相对 research/reverse/） | 最终 SHA-256 |
|---|---|
| canonical-periodic-tail-preflight/CONTRACT.md | 3005cf028be47e53a574ffc27d6862da1543f4522f23cb517dd84720df722634 |
| canonical-periodic-tail-preflight/PROOF.md | 545fee812f2b7ef96c51029e9234b9869815c4a8312236e5726b54a482042453 |
| canonical-periodic-tail-preflight/INDEPENDENT.md | 559a1aeac55066f001beaa25995ce71cc0ed5d2f1922189fa1d0284541ca5375 |
| forced-tail-audit/ROOT_ANALYTIC_PROOF.md | dccd2cfd8d9cbe61597074d2391fc59d3d983de685bf1f2bfbc19b72120e5abf |
| forced-tail-audit/sources/navier-stokes.pdf | 0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f |
| forced-tail-audit/sources/paper-text.txt | 7c8d1e236e6285de297f4d88d05056f3de5a8bdcc6454ddc81b665cf98ae0c26 |

仅写此审核文件；科学执行／数组／新参数／FFT／Lean／Git／外发均0。未修改受审稿、未读取形成中的来源审核、未启动其他研究。全文自读并核最终来源字节后停止修改。
