# 四叶出生拓扑的历史范围核查

2026-09-08。PRIVATE_CORE。**HISTORY SCOPE ONLY / NO ACCEPTED CANDIDATE / NOT CLAY。**

本记录只核实际科学对象和已付结论，不开始新四频率构造、系数展开、扫描或时间证书。我的此前身份包括 COHERENCE、MIXED_ROOT、SOURCE_BRIDGE 独立稿作者，以及若干后续主稿作者和非作者审查人；这是有历史关联的非盲范围复核，不是新的一路数学证明。

**直接答案：TrueBandSupply 的具体真实供给接口确实使用同一三对初始种子，在加倍接收处的两个出生门共享种子。它没有把四份不同共轭种子各用一次的指定出生对及新接收，认证为一个新的两步机制。与此同时，“四叶”“2+2”“四个初始正频率”都不能单独构成新问题的增量：前两者已完整进入旧树展开，第三者在更早 R0.12–R0.13 的实际初始支持中已经出现。**

## 1. 先区分三个计数

这里必须分别计数：

1. **叶位置：** 四叶树有四个初始因子，允许同一个系数重复出现。
2. **带符号 Fourier 频率：** \(p\) 和 \(-p\) 是不同频率，却受实值条件联系。
3. **独立指定的共轭种子组：** \(\{\pm p\}\) 只给一份复横向系数 \(U_p\)，负模是 \(\overline U_p\)，不是第二个自由种子。

“两独立出生对”若仅指两个二叶子树，是旧 \(2+2\) 根。若进一步指两对不重复使用任何共轭种子组，才是不同的初始叶赋值限制；这仍没有改变无标签的二叉树形。它也不表示统计独立、可分别更换初值或可忽略跨对作用。

## 2. JOINT、MIXED_ROOT 和 TrueBandSupply 实际证明了什么

本轮全文实读 JOINT、MIXED_ROOT、SOURCE_BRIDGE 的合同和主证明，并按冻结 manifest 的科学 claims 核对接纳范围。三个合同的共同初始支持是
\[
 \mathcal A=\{\pm p_1,\pm p_2,\pm p_3\},\qquad
 a=\sum_{i=1}^3
   (U_i e^{ip_i\cdot x}+\overline U_i e^{-ip_i\cdot x}),
 \quad p_i\cdot U_i=0,\ U_i\ne0 .
 \tag{FLH.1}
\]
三个 \(p_i\) 是线性独立整数向量。JOINT/MIXED_ROOT 另有其长度等几何条件；SOURCE_BRIDGE 的局部收敛不要求成对长度不同。均在单位正黏性、无外力、固定 \(2\pi\) 环面中使用完整 Fourier–Leray 算子。

第一层两叶响应 \(v_1\) 支撑包含于
\[
 \mathcal L=\{\sigma p_i+\tau p_j:i<j,\ \sigma,\tau=\pm1\}.
 \tag{FLH.2}
\]
同轴或相反种子的初门严格为零。独立整数坐标还保证每个 FLH.2 频率的出生原种子组唯一；其两个有序作用都保留。

接收集合固定为 \(\mathcal D=\{\pm2p_i\}\)。JOINT §1、MIXED_ROOT §1 的穷尽表明，在 \(+2p_i\) 上，非零可能的 \(2+2\) 根只能是
\[
 (p_i+p_j)+(p_i-p_j)=2p_i,\qquad j\ne i ,
 \tag{FLH.3}
\]
并保留反序。这棵树的四个叶标签是
\[
 \{p_i,p_j,p_i,-p_j\}.
 \tag{FLH.4}
\]
因此两次出生共同使用同一个 \(U_i\)，另一输入分别为 \(U_j,\overline U_j\)。其空间映射对 \(U_i\) 复二次、对 \(U_j,\overline U_j\) 各一次；不是四个自由初始因子的多线性系数。

| 层次 | 已付的具体结论 | 没有由此付出的内容 |
|---|---|---|
| JOINT 的 \(w_{22}\) | 全部 \(\mathcal D\) 接收配对；同一组三种子、精确热权重、共轭及共同模板方向/幅度条件 | 不把各边种子自由化；有限纯树不是原解 |
| MIXED_ROOT 的 \(v_3\) | 在 \(\mathcal D\) 全部 \(2+2,1+3,3+1\) 根；回种子通道实际保留后逐项判零；精确各层 Leray、正黏性积分和树内四次时间余项 | 指定非退化单对的同阶混合作用障碍不是三对总和下界 |
| SOURCE_BRIDGE | 全部叶数、有序根和所有 Fourier 输出的级数收敛为同一固定三对数据的光滑唯一 NS；完整周期压力；真实频带投影和来源项的明确无限维误差 | 没有实际新数据或已求值总向量间隙；不是两步再生成 |

四叶到 \(2p_i\) 的另一可能叶多重集为三个 \(+p_i\) 和一个 \(-p_i\)，它的初门或根门因横向共线而零。余下的非平凡四叶集合就是 FLH.4。三种不同原种子组不能以四叶到达这一加倍目标；这条排除依靠三个 \(p_i\) 的线性独立，不能移作任意扩充支持的频率无碰撞定理。

## 3. “全部四叶已覆盖”的准确范围

旧记号 \(v_n\) 是非线性门数 \(n\)、叶数 \(n+1\)。SOURCE_BRIDGE 的完整递归在 \(n=3\) 已含
\[
 v_3=H(v_1,v_1)+H(v_0,v_2)+H(v_2,v_0),
 \qquad v_2=H(v_0,v_1)+H(v_1,v_0),
 \tag{FLH.5}
\]
其中 \(H\) 是完整有序热 Duhamel 映射。因此所有有序四叶树形都已在算子中，不能把左右换序、根 \(2+2\) 或两个二叶出生称为新的无标签树形。

还须区分“在完整和中保留”与“具体接收的系数、符号或净来源已分析”。从旧 FLH.2 的支持名单直接核对，三对支持的两个非零可能出生边只有如下类型；本表只登记频率相容性，不计算或断言其系数非零：

| 两个出生边 | 根输出的频率类型 | 旧覆盖层次 |
|---|---|---|
| 来自同一无向边 \(\{i,j\}\)，两个根频率不共线 | \(\pm2p_i\) 或 \(\pm2p_j\) | JOINT/MIXED_ROOT 具体配对和系数已穷尽 |
| 来自不同边 \(\{i,j\},\{i,k\}\)，共有指标的叶同号 | \(2\sigma p_i+\tau p_j+\chi p_k\) | 已在完整 \(w_{22}\)、\(v_3\) 和 NS 中保留；不是该包的 \(\mathcal D\) 接收分类 |
| 同上，但共有指标的叶反号 | \(\tau p_j+\chi p_k\in\mathcal L\) | 同样已保留；属于第一频带内的四叶反馈 |
| 两个根频率相同或相反 | 同线根的完整作用为零 | 不能把频率加法的形式输出认作已出生 |

表中 \(\{i,j,k\}=\{1,2,3\}\)，所有符号只用于复核既有支持，无实际频率选择。特别第三行可以有四个不同带符号叶
\(\{\sigma p_i,-\sigma p_i,\tau p_j,\chi p_k\}\)，却仍只含三份共轭种子资料。因此笼统说“三对支持没有四个不同初始频率的四叶树”不正确。

旧 next-mixed 还对首轮固定循环三对数据、依赖全部三组的第三阶混合响应作过具体代数诊断，保留 \(2B(N,N)\)、\(B(a,C)\)、\(B(C,a)\)。本轮全文读取其合同和 PREFLIGHT，只登记其三组支持、四次齐次/第三阶及非独立原解的边界，没有重跑旧计算或采用旧数值为新数据。这进一步说明非加倍的三组混合作用也不是全未接触。

## 4. 真正的“同解供给”与一般可复用工具

TrueBandSupply 中
\[
 g=P_{\mathcal L}u,\qquad
 \mathcal S=\int_0^t e^{(t-s)\Delta}
           P_{\mathcal D}B(g,g)(s)\,ds,\qquad
 W=P_{\mathcal D}w_{22}
 \tag{FLH.6}
\]
其中 \(g,\mathcal S\) 是 FLH.1 同一固定原解的实际投影和来源，\(W\) 是同数据有限树比较项，不能混称为真实投影。\(g(0)=0\)，没有将两份任意前代场预置到初值。

记该固定数据的 \(A=\|a\|_{\mathcal A_0}\)、\(K=\max_i|p_i|\)、\(q=4AKt\)，以下无下标范数均为 \(\mathcal A_0\)。已证窗口是 \(0\le t\le1/(8AK)\)，且
\[
 \|g-v_1\|\le \frac{Aq^3}{1-q^2},\qquad
 \|P_{\mathcal D}u-P_{\mathcal D}v_3\|
 \le\frac{Aq^5}{1-q^2},
 \qquad
 \|\mathcal S-W\|
 \le\frac{Aq^5(5-q^2)}{40(1-q^2)^2}.
 \tag{FLH.7}
\]
这信用全部无限维尾部，不得缩写成仅形式树。但来源非零/占优仍要完整总向量条件。后续 \(W_0\ne0\) 时的真实来源比极限为
\(\|M_0\|/\|W_0\|\)，不准用单条边的比值代替它。

更一般的工具也已存在。SAL 全文给任意光滑初值、任意固定 \(\nu>0\) 的完整 Wiener 局部解和条件时间来源分账，并没有三对支持限制。SOURCE_BRIDGE §1–2 的粗收敛证明只用有限支持半径、初值范数及每阶叶数增长；将这套原理写到另一个有限支持上本身不构成新的机制。另一方面，FLH.7 的具体投影和缺阶预算使用三独立频率的坐标奇偶性及 \(\mathcal L,\mathcal D\) 的不相交/零门，不能给任意四组频率后直接照抄。

四个三维波向量不可能全部实线性独立；增加第四个共轭种子组后，旧三坐标的唯一表示与奇偶论证都需要按实际支持重新核验。这只是旧证明适用域的提醒，不是在本预检中构造或枚举新共振。

“两代”另有一项旧实际结果必须区别：first-cycle 的固定循环三对初值，已有两个初始为空模态的同解严格短时非零及全 Fourier 余项。其第二个目标的领先项是原种子与一个新生二叶分量作用，即三叶 \(1+2\)，不是两份二叶新生量的四叶 \(2+2\)。本轮实读合同及证明§§1–3，不把该真实结果抹除，也不改变它的来源标签。

## 5. 后续星形、三边、最低和完整行没有扩充初始支持

| 后续合同/科学结果 | 仍然固定的对象 | 准确限制 |
|---|---|---|
| net-mixed-cancellation | 同一三对、\(\mathcal D\) 上完整 \(M_0,W_0\) | 一般非全等长几何的代数稀薄性与条件来源比；例外集不是被普遍排除 |
| STAR_TEMPLATE | 三种子的两边活跃星形，同一中心给两个叶 | 条件分支原方向障碍；纯 \(W\) 全正时间与真实 NS 短窗区别保留 |
| three-edge-compatibility | 原三种子全活跃三角，完整复二维极化 | 共享形状标量系统及恰两线性类型障碍；没有第四种子 |
| two-elliptic/最低行 | 同一三角，仅最短线性、两高面积非零、最低两条 \(\beta=0\) | 最低 \(Z\) 和 \(C\) 条件、高投影/面积条件；条件可解不代表整体实例 |
| full-high-row、joint-direction | 上述同一三种子、同一恢复变量 | 完整 \(M_0=0\) 与最低非零 \(C\) 原方向的条件恢复；不是新增接收或已存在候选 |
| short-window-source-amplitude | 原 \(\mathcal L,\mathcal D,g,\mathcal S\) 与同一三对初值 | 已认证短窗内的复制幅度门；不重置 \(g\) 为新的 NS 初值 |

本轮主作者实际读取上述全部合同、net-mixed 与 STAR_TEMPLATE 主证明全文，以及最低/完整高行的对象段；各冻结 manifest 的科学 claims/not_claimed 与这些限制相符。另有只读协作者核对同一批后续合同及必要证明段，没有写文件或提供新推导；我没有把其较多的阅读范围冒称本人全文阅读。

## 6. 更早四组支持不能遗漏

沿旧 HISTORY_SCOPE 明确引用的科学源定位后，实际读取 R0.11 §2、R0.12 §1/§5–7、R0.13 §2–6入口及§8范围段。**R0.12 明写初始四个正频率为**
\[
 P_{n-1},\quad Q_{n-1},\quad b_n,\quad d_n,
 \tag{FLH.8}
\]
加各自共轭负模。它们有旧固定极化及催化幅度限制，并不是后来三对支持的换名。

但该预定接力是先由 \(P_{n-1},Q_{n-1}\) 出生 \(a_n\)，再分别借 \(b_n,d_n\) 到 \(P_n,Q_n\)，最终到 \(a_{n+1}\)。目标领先树有六叶；两个三叶子树共享前面两个泵种子。R0.13 明确研究其第五阶、六次齐次部分以及全部根分裂；其表中的 \((2,2)\) 是左右 **Taylor 阶数**，对应叶数 \(3+3\)，不能认作本题四叶 \(2+2\)。

R0.12 的完整低阶递推当然包括这些初始支持允许的第三阶/四叶项，R0.13 也保留中间叶标签。因此不能说旧库“从未包含四组支持的四叶作用”。这种算子覆盖不等于已证明某个四组各一次的叶赋值系数非零。本轮实际读到的主目标与准确结论，是该固定族的六叶接力系数、外部路径影响及明确未付的 PDE 时间余项；不是一个已认证的“四份不同种子各一次、两个指定二叶出生及其新接收净供给”的同解定理。

这里只核旧正文的支持和结论范围，未复核数值表、执行算法、读取链接的科学数组或复用实际参数。旧正文中同时显示的系数/数值只作历史上下文，不作本次证据。旧 R0.13 的算子符号、归一化与当前约定也没有被静默等同。

## 7. 当前裁决与停止点

- 若下一提议仅是写四叶 \(2+2\)、让两个第一层量作用、增加第四个初始频率或重给一般局部 NS 余项，则这些原则已有覆盖；**仅凭这些描述应判 NO-CANDIDATE，不具有已确认科学增量。**
- 若明确要求四个彼此非相反的共轭种子组各贡献一个叶，并锁定两个实际出生频率、一个具体接收及全部竞争来源，则它不属于旧三对加倍接收的 FLH.3–4 分类。然而本记录没有证明它未在其它旧稿/原文出现，也没有证明它有可用增量、非零输出或可行数据；其无标签树形仍是旧 \(2+2\)。

因此这里只确认一个需要进一步精确定义的**初始叶赋值/接收范围区别**，不批准或启动四频率构造，不称新颖，也不把“范围不同”写成“候选通过”。本树已有四组支持的旧族，是以后任何精确新合同必须面对的直接去重来源，不能略过。

实际全部正负出生、其它配对、\(1+3/3+1\)、回流、共轭相干、黏性以及同解尾部不能因“独立出生对”这个名称而删除。真正后续仍须先由根给出有限、可检查且不重复旧结果的目标；本记录到此停止，没有实际频率、极化、初值、时间或容限选择，更无统一迭代、同一初值无限尺度或有限总时间结论。

## 8. 实际来源与字节

路径相对 /Users/kasifa/Documents/Math/navier-stokes-reverse/。以下哈希均本轮实测；“全文”只指实际显示且已读的本地科学文本，不代表重证全部数学。manifest 仅用于源绑定和科学范围，未读取任务或发布状态、使用 Git 或执行全包脚本；没有把 manifest 中其它用途字段作为状态调查。

| 文件 | 主作者实际范围 | SHA-256 |
|---|---|---|
| nonorthogonal-return/JOINT_CONTRACT.md | 全文 | cc3cd571b87cde40488345d8d8faa6ac774892701f30869ee479c3d82088e23c |
| nonorthogonal-return/JOINT_PROOF.md | 全文 | 057381db9781ad59d8957282f02b9c917d2a3901dcc0ca1ec0b881c1db115808 |
| nonorthogonal-return/freeze.json | 工具返回的科学文件/claims段；未宣称完整重绑定 | b327adfbcec73d0def1b8f42074f270dcbf3e1875e41b911b15513e56310f024 |
| mixed-polarization/MIXED_ROOT_CONTRACT.md | 全文 | 4922918d272558efb8ddc9c05012acbffe9d497c2baf11a63b6027fc24e44bb1 |
| mixed-polarization/MIXED_ROOT_PROOF.md | 全文 | 3e540dccc41dcf99b79b1a72cf5bff0e5d58331c4ad4ecf961ac783fd3bf1832 |
| mixed-polarization/SOURCE_BRIDGE_CONTRACT.md | 全文 | 32e6c8152c8b42592d84b9c5809654b9a7528d96d4231bcfe9f2351ebc01ba37 |
| mixed-polarization/SOURCE_BRIDGE_PROOF.md | 全文 | b6085eb219e5872ec1e5b3e990fdb5c3b6c7a4f7dc75e265f4adb19cd871d4a4 |
| mixed-polarization/freeze.json | 文件绑定和科学claims；另读第150行至末尾的范围字段 | d0724cf912623efae9e9522fe1a0c5b2dd447d62dfaabcbeb14205be1f3f419a |
| net-mixed-cancellation/CONTRACT.md | 全文 | 8ec55579d3288a15e47f2b1af17a2d981ac174fb649dc496fb6d5ac0d9b2e7e8 |
| net-mixed-cancellation/PROOF.md | 全文 | 2f0584ae5776ac3eb02318cc7353a70b0a6e0ab39bb6419b5b9217eff529e327 |
| net-mixed-cancellation/STAR_TEMPLATE_CONTRACT.md | 全文 | b7543164be08ff3b625e45745b7f9aab4b81d74f082f4f71cbb1f220f62e7ad0 |
| net-mixed-cancellation/STAR_TEMPLATE_PROOF.md | 全文 | 214ccd8197923dc5039a452beaa4111b80292cd6ac22f9491b1487e0cd42e46d |
| net-mixed-cancellation/freeze.json | claims/not_claimed | d05cfb0732d0ce915876476942b37f18a98afb091c22252fdcb3b5cedc8999ea |
| three-edge-compatibility/CONTRACT.md | 全文 | 51909466ff2baf93b83d419775b0fbd2f1ceff4dec59c785358401d80ff01143 |
| three-edge-compatibility/freeze.json | claims/not_claimed | 1ba798a30722690bb768e8e08570c316799864059b91662616c70bf28a2bc604 |
| two-elliptic-compatibility/CONTRACT.md | 全文 | ee05b39370f178cac5aebcf3c3046478c848c74b0078ee26edafb3282029ad52 |
| two-elliptic-compatibility/PROOF.md | 第1–47行，TL.1–2及支持/共享定义 | 8961c72504eb7d60f35ee53050c99a2a25203ad539f85a9135ca16706dcc1cba |
| two-elliptic-compatibility/freeze.json | claims/not_claimed | 825273fede22a73aafa17711fc0bbabce96ef2b57e19bece794f9c798a9ea3a8 |
| full-high-row-reduction/CONTRACT.md | 全文 | 8f1dd745dc12409f3e49b7b56073b3fb38fca4a26d23774f0df4ea12292ecc6e |
| full-high-row-reduction/PROOF.md | 第1–29行，FR.1–2及共享输入 | 3d02da817e164bbf8f75bdddfea74a4e0d2b14c12d890952aeeb727866cc3c6b |
| full-high-row-reduction/freeze.json | claims/not_claimed | dadfc5d6c7555a24c0a961531b17086f84227d8e0b47b47ace4c15694d80c8e0 |
| joint-direction-compatibility/CONTRACT.md | 全文 | 5b8dc82300556766260a13c1f9124d7a02989ec14e242cf5aad8b49fc5d16ad3 |
| short-window-source-amplitude/CONTRACT.md | 全文 | d0e42e518d8b5d4c3d13511fe79f6903f46d7c6d31910702f19282e1907e14de |
| reconnection-preflight/SOURCE_ATTRIBUTION_LEMMA.md | 全文，含通用对象与来源量词 | d22bcca237977647b54ebbe13288c63a24a7c610a52a7c2265f4e3cfe366607a |
| first-cycle/CONTRACT.md | 全文 | 6311d166a3bba64faa3f7d1afe042535702014f0e7b2dfffa6952acb7eb68cf8 |
| first-cycle/PROOF.md | 第1–140行，§§1–3 | a87672a035f1c80a0225ce8956fca53ffc2eb07fdd4e83092505b4ac657f6120 |
| next-mixed/CONTRACT.md | 全文 | 11d78f96e54be82a3062b91256cbe1fdd464badb9f180776c70a4705bc7a1d9b |
| next-mixed/PREFLIGHT.md | 全文，仅旧诊断范围，不新认证其计算 | 9e3fcaa0803f44af4bef629a78bf3da1b0ca569b44ee1541872085aeeb7e8858 |
| unequal-axis-return/HISTORY_SCOPE.md | 全文科学历史，用于定位R0.11–13；未打开其旧checkpoint依赖 | 1c209e0dc0e2d5c2f1077e1cb30f3fec4cfd196d9dadb3599a6a9cef97588207 |
| public/notes/r0-11.html | 本地科学正文第229–250行 | ad8ebe34c67939cd371f621cc7fbf5f54cf501c4d2506e587aa1494f4ef52095 |
| public/notes/r0-12.html | 本地科学正文第210–249、337–445行；旧数值显示不作本轮证据 | a8e98babfa76e0379157367155c6161294b276a1c5565b0f48878a4a28c7cb7a |
| public/notes/r0-13.html | 本地科学正文第232–370、447–465行；只用对象、叶标签与范围 | e5ad43432fb040c60aa51a3716bdd1b606c297f47df45e60722ae7e83903675e |

上表前29行文件位于 research/reverse/ 下，后三行位于工作树所列 public/notes/，均为本地历史科学文本读取，不是访问、检查或操作网站。一次联合 manifest 输出被工具截断，已将相应范围表述为实际可见段落，没有将未显示字节冒称全文读。协作者只补查后续对象段，其非主作者阅读不扩大本表。没有外部文献检索或新颖性认证。

该表是此次阅读证据，不是32项数学结果或32份新接纳。只在本独占 HISTORY_SCOPE.md 写入，全文自读后停改；没有科学程序、数组执行、实际选参或扫描，没有 Git、外发、发布或状态操作。
