# 固定配对与主项首阶：非作者审核

2026-09-20，PRIVATE_CORE。**条件性 PASS，无实质需修项。** ROOT_PAIRING 的 SP.1–9、MAIN_FIRST_ORDER 的 MF.1–5，以及以MF.6和完整均值小阶为前提的MF.7–8换写成立。未接纳MF.6、均值余项、实际完整首系数或其非零性；本结论不是单一配对检验已经成功或失败。

本人参与旧热源资格、增长、残差及CIV结构审核，非这两稿作者。已知合同预先披露的根思路，属非盲非作者AI审查；未读本题另两名作者正在形成的算子/波桥稿，不以其状态消息代替证明。只审核原固定φ，不改变合同或选择第二测试。

## 精确周期配对与零阶结构

1. 固定φ是整个 \(\mathbb R^3\) 上光滑、无散、均值零的方位向量，支撑为闭单位球；球面处无限阶平坦。正文“支撑B(1)”按此读即可，所有分部积分在全空间或真实周期胞进行，不需φ属于开球内部的紧支撑类。足够晚缩放后的闭支撑严格处于中心胞内，故其周期延拓合法。
2. SP.1先以真实周期无散测试支付 \(P\phi_\tau=\phi_\tau\)、自伴性及 \(\langle-P\operatorname{div}C,\phi_\tau\rangle=\int C:\nabla_x\phi_\tau\)；完整压力/远场没有被设零。SP.2是周期提升上的全Gaussian身份。换元后张量项因子为 \(\lambda_p\tau^{A+1-2A-1/2}=\lambda_p\tau^{-h}\)，线性项为 \(-\lambda_p^2\int\Delta W_\tau\cdot\phi\)，SP.3符号及速度/时间/体积因子齐全。
3. 光滑周期源资格给 \(M_F<\infty\) 用的是足够高Sobolev阶，不是裸P的 \(L^\infty\) 有界性。SP.4将Δ移到紧支撑φ，完整 \(H_\tau\) 一致有界及逐点极限提供明确积分余项趋零；未求未滤波误差导数。
4. 对 \(F_0=f(r)e_\theta+g(r)e_3\)，无散及轴光滑性给 \(\operatorname{div}(F_0\otimes F_0)=-f^2e_r/r\)，是至多对数增长的径向势梯度。径向Gaussian不生成水平径向速度，平滑后仍为纯旋流/轴向形式。故SP.5的零阶J为零成立；这不支付 \(\tau^{-h}J\) 的极限。
5. SP.6全部非零副本并入 \(D_\tau\)。支撑分离使 \(F_\tau^0D_\tau=0\)，在 \(|Y|<\lambda_p/(2\sqrt\tau)\) 有D=0；在测试支撑上的一次热差至多 \(MT_\tau\)，张量热差至多 \(M^2T_\tau\)，两项热速度乘积差共至多 \(2M^2T_\tau\)。SP.7的3及超代数Gaussian尾正确，未作有限像截断。
6. SP.8的SO(2)平均在全空间零副本操作，不是晶格连续旋转。Gaussian/φ的协变性保证有序Q不变，对每个位置分别平均得两交叉项各自为零；J(w)完整保留。SP.9的BM、MB、MM以及实际波识别资格未被删去，误差绝对上界不被用作实际下界。

## 原主项首阶及候选系数

7. 原(4.3)的径向速度为 \(q^{-1/2}V_0/\sqrt{2X}\)。由 \(\eta/\tau^h=(1-\eta^2)^Dz\)、\(X=(r^2/2)(1-\eta^2)\)，q/τ与X的改变在固定Y处始于 \(O(\tau^{2h})\)；η的一阶系数是z，径向归一化首阶是v。因此MF.1完整保留 \(H_1=\lambda_p(v e_r+za e_\theta+zb e_3)\)，没有漏掉轴向线性项。
8. 原(4.6)–(4.7)在η=0给 \(V_0(X,0)=-\int_0^X U_{{\rm pr},\eta}(s,0)\,ds\)。故 \(v'+v/r=(V_0)_X=-b\)，H1在轴外无散；\(V_0/X,F,U\) 的Cartesian光滑轴因子使此身份跨轴成立，无轴上分布项。H0亦无散。
9. Theorem4.6(i),(v)支付全η有限X控制、U/V0固定外区为零；(4.29)在外区使E、\(XE_X\)、\(E_\eta\)有界（H及其有限次导数只在固定有界非负区间使用）。在 \(|\eta|\le1/2\)，变形剖面的η差商受 \(C|z|\) 控制；在其补集，\(\tau^{-h}\le2|z|\)。晚时原时间截止恒1，空间截止非1区域/零延拓域外与原点有固定距离，给 \(\tau^{-h}\le d_0^{-2h}|Y|^{2h}\)。因而MF.2有真实全域多项式主控，不仅是有界Y上的Taylor。
10. 上述主控对每个固定Gaussian权重及有限p可积，故 \(Z_\tau=(F_{B\tau}-H_0)/\tau^h\to H_1\) 的带权极限成立。Q也可通过绝对收敛积分作用于这些多项式增长场；两有序交叉差趋零，\(\tau^hQ(Z_\tau,Z_\tau)\to0\)，支付MF.3的严格 \(o(\tau^h)\)，未仅由J趋零猜阶数。
11. \(\operatorname{div}(H_0\otimes H_1+H_1\otimes H_0)\) 的方位项是 \(\lambda_p^2[vf'+vf/r+ga]\)：前两项分别来自径向导数与基向量转动，ga来自轴向导数za；不得漏其中任何项。Gaussian保持z并以二维向量热核平滑水平向量，故MF.4–5的完整有序系数与“后乘积减前平滑”的号正确。
12. 原(4.12)/Prop4.2明确将轴向黏性移出并保留径向黏性，领先方位残差为负的 \((\partial_r+2/r)T\)。在η=0，时间项 \(Af+(r/2)f'\)、完整对流N及 \(-\Delta_\theta f\) 均有同一幂；轴向黏性相差 \(\tau^{2h}\)。因此MF.7的负应力号正确。
13. 条件MF.6的方位积分以柱测度r dr分部积分，\(\int T(\partial_r\bar\phi_\theta-\bar\phi_\theta/r)=-\int(\partial_rT+2T/r)\bar\phi_\theta\)，没有额外因子2；T在原固定壳平坦，无边界项。该代数不证明物理波能使用MF.6，也不预删zθ项。
14. 二维向量恒等式 \(S(Y_h\cdot\nabla F)=Y_h\cdot\nabla SF+2\Delta_hSF\) 给半膨胀项的 \(+\Delta_\theta\bar f\)。直接将MF.5及条件波项代入SP.3，得到 \(\lambda_p^3[-\Delta_\theta\bar f+\bar N_{\rm prod}-S(N+D_\theta T)]\)；用MF.7换写恰为MF.8，最后只剩一个负 \(\Delta_\theta\bar f\)。常数、符号及 \(\lambda_p^3\) 一致。

## 实际阅读与绑定

本次全文读下列三稿；原论文只定向读所列抽取文本，未新渲染/视核PDF，未认证原构造全文。旧输入按此前已审字节复用，本次仅复核哈希。

| 文件（以research/reverse为根） | 实际范围 | SHA-256 |
| --- | --- | --- |
| heat-signed-pairing-preflight/CONTRACT.md | 本次全文29行 | 1f1f00d70e878cd1eeeebc9064b5882f516a43258014084062a8cf6a4b975145 |
| heat-signed-pairing-preflight/ROOT_PAIRING.md | 本次全文79行，SP.1–9 | cd4efab711e44b4567a50004eddf585ba8b5f6da4afb973970195a48df5f1d86 |
| heat-signed-pairing-preflight/MAIN_FIRST_ORDER.md | 本次全文81行，MF.1–8 | a3b0747644e1e8de8329b4bd5530f853d16c2ee6b99521ce5a12aed05deed4d7 |
| forced-tail-audit/sources/paper-text.txt | 本次1215–1398、1580–1673行；PDF25–28、32–34页相关文字，重点(4.3)–(4.14)、Theorem4.6/(4.29) | 7c8d1e236e6285de297f4d88d05056f3de5a8bdcc6454ddc81b665cf98ae0c26 |
| heat-vorticity-tail-preflight/MAIN_TERM_AND_IMAGES.md | 此前全文；复用MG.2–4 | bb25839f76bfab719b3bca7afed9a724c624a4a172a1fc55bff684975cc3fc7a |
| heat-vorticity-tail-preflight/WEIGHTED_ERROR_INDEPENDENT.md | 此前已审，近期实读70–112行；复用WE.10–11 | fb7a2f8284f2f1a838306e3a68f9a2ae7cb6cf76a9a63b574d05832eb8f38018 |
| heat-vorticity-tail-preflight/ROOT_INTERFACE.md | 此前全文；复用完整热残差HI.2 | 909ccebe0c56d9cb0845a9eca6be78fb42c082e7671f5a6030529fc1b505d491 |
| civ-applicability-20260920/FIXED_HEAT_STRUCTURAL_TEST.md | 此前全文逐式审；复用CS.2–6 | 85b46bba996909be83074fb7b75f0c3f516c57838504d2d9b7078d42390ee591 |

**尚未支付。** 实际均值的BM/MB/MM为 \(o(\tau^h)\)、完整物理相位到加权波双平均的桥、滤波波速度乘积的小阶、全部zθ/同异标签/curl/尾项及其严格余项，均不在此次PASS内；MF.8尚不能标作实际M的极限，更未获其非零/零性。既有正速度积分I不决定该含导数配对的符号，不由宽上界判失败；同一入口仍按合同推进。只写本稿，全文自读后停止；科学程序/数组/FFT/数值/扫描/Git/外发均0。
