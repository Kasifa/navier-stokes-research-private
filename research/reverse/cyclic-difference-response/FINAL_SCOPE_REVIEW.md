# 差型真实供给包的最终非作者范围审查

2026-09-09，PRIVATE_CORE。结论：**PASS — 同一固定数据、原绝对短窗内的逐对及总带来源障碍已闭合。** 本次实际读取主、核验两端保存结果的指定类别、最终解释与执行记录，结合此前已逐式审过的 DR/RL 及旧完整 NS 桥，解除这些解析稿对差型非零下界和原 DR.8 窗算术认证的条件。未发现须修的实质问题。

本审查不声称已核尚待根生成的最终 acceptance.json、冻结清单或提交对象；已有 conditional-acceptance.json 是早期条件检查点，身份另见第 7 节。本文不是第三次科学重算，也不把核验作者的结果说明当作其自身的非作者审查。

## 1. 身份与实际阅读

本人不是本项 DR、DI、RL、主源码、核验源码或两份原结果的作者。此前是本项合同、DR、两份最终源码及 RL 的非作者审查者，也参与旧六载波应用、源桥和范围审查；因此这是有前序接触的最终复核，不能称全课题盲审或另一独立证明。

本最终阶段首次全文读 DI 的 INDEPENDENT.md 和其 INDEPENDENT_REVIEW.md，发生在本人完成 DR 与源码专审之后；没有用这个后读经历改写作者形成时的独立历史。实际全文读最终 OUTCOME、EXPERIMENTS、两个 manifest、ROOT_COMPARISON、SOURCES、ALGEBRA、两份 execution、VERIFY_RESULT、PRIMARY_ROOT_READ、VERIFY_ROOT_READ、VERIFY_DESIGN、历史 conditional-acceptance 以及根随后补交的 root-source-binding-check；又全文重读最终 ANALYSIS、RESTART_LEMMA 及自己的 RESTART_REVIEW。其余已专审文本沿本连续任务的实际全文阅读和当前相同 SHA 使用，见第 9 节。

两份最终源码曾分别连续全文静审：主源 723 行、35480 字节，核验源 1415 行、75887 字节，均在唯一执行之前完成，审查结果已另行停稿。本阶段没有执行、导入、编译或探针，也没有重新实现或调用其中科学函数。前输出核心 verify_core_pre_output.py.txt 本人只核哈希/字节，未全文阅读；它的形成史来自实际全文读的设计、适配说明和作者披露，不冒称本人的完整代码认证。

本阶段对原 JSON 的人工阅读是定向的，不能写成两份巨整数输出的逐行全文手算：

- 两端全部顶层状态、完整来源输入表、环境、限额、资源采样和实际执行回执；核验结果的完整 coverage，以及首坐标、零前缀、原根标识、深度和区间。
- 核验端全部六个形式向量、18 个稀疏二次分量、物理相位和目标频率；原首非零多项式的全部系数、最终闭包围、完整原坐标下界、δ、d。
- 核验端常数 gcd 的零判摘要及端点计数证书、五次保存路径的父区间/中点/左右计数/保留子区间/深度；两端完整原 DR.8 窗对象，包括旧 Abar/bbar/T*、Q0/C0、四候选、全部最小下标及四份 left/right/slack。
- 用已存 JSON 对象的相等比较，核主与核验端的完整下界、d、δ、τ、保存路径、保存 Horner 对象及原窗对象相同。这里只比较原记录，不重新求值或生成包围。

未在本最终阶段逐条人工展开主端全部 144 候选、每份长商余/Euclid/Bézout、所有长 Sturm 系数或每步 Horner 的四乘积；它们由先前全文静审的核验逻辑和本次已实际完成的唯一精确核验覆盖。VERIFY_RESULT 的作者披露其本人已全文读核验原输出 4417 行，这不能转记为本人的全文阅读。本次首次投影两个误写的可选顶层键所得 null，仅表示不存在该键；随后实际列键并读取科学计数和资源的正确字段，没有把 null 当零计数、没有修改原结果。

## 2. 唯一执行、来源与覆盖

实际当前原文件和回执核同：

| 阶段 | 停定源码 SHA 前缀 | 原输出 SHA 前缀 / 字节 | 回执与实际状态 |
| --- | --- | --- | --- |
| 主端 | 842679b23991 | 2ecedeb13a1b / 269258 | primary-execution：chunk 3f6e15，exit 0；科学计数 1、completed、DIFFERENCE-WINDOW-CERTIFIED。 |
| 不同组织核验端 | 87fd73e0b5a7 | e2d266940b4e / 188785 | verifier-execution：chunk e8d1ee，exit 0；科学计数 1、completed、DIFFERENCE-CERTIFICATE-VERIFIED。 |

主端来源提交记录为 668b18916d33b2832fc46b68e00184ce37c62738，核验端为 76cfd7a0d35e229a51f4aa2385add468cb637fae。实际命令、argv、源码 SHA 与回执相合。提交对象、运行前输出不存在及根的 28 项 Git 对象检查是根的执行来源记录，本人未运行 Git，不能说是自己亲查提交。当前文件字节则已由本人独立核哈希；核验原结果完整 input_bindings 的 13 个对象，当前 SHA 和字节数逐件全部相同。主端九项输入亦落在这些已核相同的对象中。

核验原结果支付的具体覆盖为：12 初始模、144 有序候选、12 命中有序贡献、六向量的 18 完整分量与 18 份 Q 商余身份；1 个坐标零判、1 份 gcd 证书、6 个普通 Euclid 步骤、2 条 Sturm 链；重放 5 次原保存二分、6 个闭 Horner 记录及 42 步；4 个原窗口候选及 4 份原预算。核验端新增二分为 0，旧 A/B/C 执行为 0。这个实际成功分支没有被写成未知分支已经全部发生。

核验保留全部两个有序作用和全部 Leray 分量，以稀疏二元多项式及双叉积组织同一卷积；保留正负模共轭、物理 +i 相位、原 v=-s、w=r 的未缩放代入。Q 只作为原全局首一平方自由多项式，不被假定为指定根的最小多项式。普通 gcd、除法/Bézout、保存 Sturm 负余式的正缩放、删零变号及半开区间计数均在已审核验范围内。当前第一个坐标即非零，零前缀为 [false]；没有跳过一个未决的早期坐标，也没有宣称另外 17 分量已各自进行根上零分类。

设计与适配保留了不同组织核心先形成、随后读取主输出并适配的次序。Hume 既是核验作者，又有方法稿、DI 审查、旧 GS/C 角色；VERIFY_RESULT 是其执行后结果解读，非盲、非本包最终审查。源码专审、一次实际核验及本范围审查承担不同职责，不重复计为三份独立数学证明。

## 3. 完整六行、同一实嵌入和原下界

物理代表仍为 q=(-3,1,2)，完整系数为

\[
\widehat{B(a_*,a_*)}(q)=iG,\qquad
G=\frac47(3v_*+2w_*)(v_*+3w_*)(-1,19,-11).
\]

另两正模为 Rq、R²q 及相应旋转向量，负模为共轭。形式展开与 DR、DI 的两个完整有序投影一致；一般单对公式及等长法向像是旧方法接口，本包不另计为一般新定理。旧四叶加倍接收在等长支的消失不能用来删这个二叶法向项。

同一旧指定根从 (-75/32,-125/64] 沿原保存的五步路径细化到

\[
I_5=(-2075/1024,-4125/2048].
\]

旧深度 7、新增开始与完成各 5、合计深度 12；核验只重放原路径，没有重选根、继续搜索或改变原归一化。首坐标与 Q 的首一 gcd 为 1；该 gcd 的局部根数为 0，保留的 Q 区间仍含指定唯一根。首个成功原闭 Horner 包围严格为负，其靠零端给

\[
\delta=
\frac{3880728698927672352860026215467141443157}
{248032677071760087808993803632640000}>0,
\qquad d=2\delta\le c:=2|G|_2.
\]

δ 是单坐标的绝对值下界，d 是逐正负频率对首范数的共同下界，不是整个向量范数的求值或近似。完整旋转与共轭核验使三对都可使用同一 d。所有数值来自原记录；本审查没有对指定根作新的科学求值。

原窗口严格保留

\[
Q_0=315\bar A^2+2\bar A\bar b^2,\qquad
C_0=\frac{32}{7}\bar A^2\bar b^6,\qquad
\tau=\min\{T_*,1,d/(2Q_0),d/(8C_0)\}.
\]

实际原记录的全部最小下标为 [3]，末项预算余量为 0，其余三份严格为正。本次读了 τ 的完整原有理数和全部四候选/预算，且与主端完整原对象相同；不另抄一个替代值，不使用 DI 的另一条件窗口。原 Abar、bbar、T* 未随区间细化优化。于是此前 DR/RL 尚待支付的 d>0、d≤c、同一原 τ 的四项预算，现在已由实际不同组织证书闭合。

## 4. 从有限算术接到同一完整 NS

旧 AP/GS 给固定标准 2π 环面、ν=1、无外力、同一 a_* 的完整经典解 u 和周期压力。普通全阶响应、全部 Am 及所需时间导数的同窗收敛和唯一性沿已审原接口；这里没有把新有限系数当作完整 NS 解或重新启动另一份解。

两个有序差型项使用同一正热因子

\[
J(t)=\frac{e^{-14t}-e^{-76t}}{62}>0\quad(t>0),\qquad
0\le t-J(t)\le45t^2\quad(t\ge0).
\]

热率身份由完整频率核验支持，指数积分及不等式由已审 DR/DI 的解析证明支付，程序并未模拟热流。DR.5 的 315Abar² 来自 45 倍完整双线性绝对界；2Abar bbar² 来自原全阶 n≥2 普通尾。对三个差型正负对各自有

\[
\|P_{E_j}u(t)-tF_j\|_{A0}\le Q_0t^2,\qquad
\|P_{E_j}u(t)\|_{A0}\ge ct-Q_0t^2\ge dt/2>0
\quad(0<t\le\tau).
\]

原接收带 D 上的前三个完整时间响应为零，故实际 h=P_Du 满足

\[
\|h(r)\|_{A0}\le2\bar A\bar b^3r^3
\quad(0\le r\le T_*).
\]

这是包含原解全部反馈的真实幅度，不是 W0 或某个截断场。它只利用固定投影支撑和完整普通尾；D 外的真实频率没有被删除。完整有序 B、复双线性系数、Hermitian 系数范数、正负模共轭和 Leray 压力作用在接桥时均保留。

DI 后读比较没有引入另一套参数：DI 的逐对首范数 Ω 正是此处 c；若使用 DI 的正下界符号，应与本处 d 对应，而非与单坐标 δ 混同。DI 利用固定输出长度得到 C7=(16/7)Abar²bbar⁶，主稿 C0=2C7；DI.15 的四项窗与 DR.8 不同。本包实际算术只支付原 DR.8，没有计算或比较两个实际窗，不能借 DI 较小的某个常数自动改称更大窗口。

## 5. 原绝对窗内所有记账起点

VERIFY_RESULT 只解释程序所用的原 s=0 对象；以下全部起点量词来自另行预锁、已审的 RL 解析引理，不虚构核验程序曾求正起点的原解。

对同一实际 u、h=P_Du，E 仅取三个 E_j 之一或其不交并 E_-。任意 0≤s<t≤τ 定义

\[
S_{s,E}(t)=\int_s^t e^{(t-r)\Delta}P_EB(h(r),h(r))\,dr.
\]

因 D 的频率长度为 √61<8，完整双线性界给

\[
\|B(h(r),h(r))\|_{A0}
\le8\|h(r)\|_{A0}^2
\le32\bar A^2\bar b^6r^6.
\]

热半群和投影收缩，所以直接积相消之前的绝对上界得

\[
\|S_{s,E}(t)\|_{A0}
\le C_0(t^7-s^7)\le C_0t^7.
\]

没有使用一般不成立的从零积分范数单调性，也没有将 r³ 换成 (r-s)³。由 t≤τ≤1、t⁶≤t 和 C0τ≤d/8，对每个差型对分别有

\[
\|S_{s,E_j}(t)\|_{A0}
\le C_0t^7\le dt/8
\le\tfrac14\|P_{E_j}u(t)\|_{A0}.
\]

三个正负对不交，A0 是各频率系数 Hermitian 范数的和；实际供给和实际目标均按这些投影可加。逐对先付再相加，得到总 E_- 的同一 1/4 界和严格非零目标。未以总带下界倒推某个单对。

令 z=u-h，完整任意 s 起点 Duhamel 给准确余来源

\[
\begin{aligned}
R_{s,E}(t)&=P_Eu(t)-S_{s,E}(t)\\
&=e^{(t-s)\Delta}P_Eu(s)\\
&\quad+\int_s^t e^{(t-r)\Delta}P_E
\bigl[B(h,z)+B(z,h)+B(z,z)\bigr](r)\,dr.
\end{aligned}
\]

s 处目标热延续和两个不同有序交叉项全部保留；z 包含 D 外的完整原场、反馈与回流。三角不等式遂给

\[
\|R_{s,E}(t)\|_{A0}
\ge\tfrac34\|P_Eu(t)\|_{A0}
\ge3\|S_{s,E}(t)\|_{A0}.
\]

若 S 非零，实际其它来源/该真实供给至少为 3，不能满足原至多 1/4 的来源占优门。若 S=0，则 R=P_Eu(t)≠0，不定义零分母比值。它没有从供给上界制造供给非零。s=0、t=τ 均包含；连续延伸至 s=t>0 时供给为零而目标非零，原点 s=t=0 不作非零或比值断言。

继承的 h 绝对上界本身有效至 T*，但本比例证明仅支付 t≤τ。RL 末尾有关“不提供任意 s>τ”的范围句应按这个区别理解，不能误读为 h 在 τ 后至 T* 没有任何已知上界。没有把绝对时间平移成 t-s 后重用小量，没有支付 τ 以后任意重启、收到状态返回原输入类、和型、不同接收集合、模板恢复、跨轮统一误差或一般再生排除。

## 6. 资源与实验记录的接纳口径

两个原输出、两份实际回执、EXPERIMENTS 和 manifest 的来源及保存值相合：

| 首份完整序列化后的原采样 | 主端 | 核验端 |
| --- | --- | --- |
| wall_seconds_since_entry | 0.053049874999999996 | 0.053112625 |
| user_CPU_seconds | 0.047045 | 0.057579 |
| system_CPU_seconds | 0.013486999999999999 | 0.014643999999999999 |
| RSS_SELF_bytes 高水位 | 20840448 | 23396352 |
| 实际最终输出字节 | 269258 | 188785 |

完整三次资源采样均已实际读，不只读上表末次值。解释器是 Python 3.9.6、Darwin arm64，原记录中的实际可执行路径为 /Library/Developer/CommandLineTools/usr/bin/python3；命令经 /usr/bin/python3 调用不构成不同科学执行。科学 worker/线程各 1，主动启动外部进程 0，第三方库为空；18 个可见逻辑 CPU 不是 18 个 worker。科学使用整数/Fraction，浮点仅为资源元数据。

每端的 60 秒入口计时、256 MiB SELF 目标、严格小于 1 MiB 输出门在保存采样范围内通过。计时从入口导入 time 后开始，包含输入读取、科学、来源复核和首次完整序列化；不包含 time 导入以前、添加最终资源字段、最终序列化和写盘。CPU 是进程累计量，不是该 wall 区间的单独计时。核验首份完整序列化为 188473 字节，加入资源字段后的原文件 188785 字节，不是互相冲突的输出大小。

SELF 高水位不是 OS 硬内存上限或整个进程树/完整生命周期证书；工具回执的 wall_time 也不是科学成本。现有证据没有显示合同采样预算违规，不补估未记成本。执行记录支持本项主与核验各一次、无科学失败重跑；本文没有对机器上所有潜在历史命令作全局审计。文字补丁上下文失败、元数据错键和读取截断等已披露，不伪装为科学运行，也不以本项成功修复旧失败或旧资源缺口。本人未作 Git 格式检查，不报告“所有格式检查通过”。

## 7. 历史状态、字节与最终接纳的分界

ANALYSIS、DI、RL、自己的专审和主执行回执在形成时保留的“条件/pending 独立证书”均有真实阶段含义。实际独立核验现已完成，最终范围可据后来证据解除有关条件，但不能倒改旧原输出或把旧静审写成当时已见结果。

conditional-acceptance.json 明确是主科学前的八项条件检查点，科学计数在该检查点为 0，其 bound_file_scope 将条目绑定到记录的前期 Git 对象。它所列 ROOT_COMPARISON 的历史 SHA 为 2715ee51ad70665fc68c7eead1a7aa256a364acceb9c972f675c5da900bb60c2；后来根比较追加实际运行段，当前 SHA 已另列于下表。根随后补交的 root-source-binding-check.json 已由本人全文读，记录 22 条两端输入与各自运行前 Git 对象匹配、八条历史条件接纳与 668b1891 对象匹配，亦明确历史比较无须等于当前稿。这是根的纯元数据核对证据，本人没有运行 Git 验旧对象；不能将不同阶段的比较字节混为一件，也不能把历史表或该元数据记录称作尚未生成的最终包接纳。

当前 ROOT_COMPARISON/SOURCES 中先前的 pending 段与后续实际两次执行段保持形成次序，非当前执行命令。VERIFY_DESIGN 的未适配核心说明由后续 VERIFY_ADAPTATION 交代，未被当作现最终源码仍不能执行。两端 raw 中的 mathematical_acceptance pending 与 experiment-manifest 中等待单独最终审查的字段仍保留，本文不修改它们；根之后应以单独最终记录承接本审查，而不是覆盖旧运行身份。

本次不读取或并入 receiver-input-geometry 或其它后续科学。figures-manifest 的空图档状态与本项精确文本计算一致；没有新图、读者 PDF、英文翻译或公开内容授权。原三方向有限两层结果不重计为本项新机制，本项也不修复旧失败证书。结论保留 **NO-CANDIDATE-FOR-A-REGENERATING-MECHANISM / OPEN / NOT CLAY**。

## 8. 本次闭合和不闭合的事项

本次闭合的是：原固定 a_* 与同一实嵌入的六差型完整二叶系数非零；共同有理 d 及预锁原 DR.8 窗已由不同组织实际证书支付；经已审无限维 NS 桥与 RL，对每一对及总带、原绝对窗所有 0≤s<t≤τ，真实 h 自供给至多为实际目标的四分之一，其余来源至少为它三倍，零供给支和端点完整保留。

它不是新初值、真实七/八叶求值、新的放大或模板返回，也不是任意时间再供给、一般状态恢复失败或奇性定理。最终接纳文件、冻结清单及 Git 对象由根在本文停稿后另做；本文不提前声称这些程序性工作已完成。

## 9. 实际当前来源 SHA 与阅读范围

本节是本人的实际阅读/当前字节清单，不是尚未形成的 freeze 清单。前 33 件路径相对本目录；“此前全文”仅指本连续任务已经实际全文读过对应停定字节，本次复核 SHA，不冒称又一次全文显示。“本次全文”包括本最终阶段实际全文阅读。两份原 JSON 的定向范围以第 1 节为准。

| 来源 | SHA-256 | 本人阅读范围 |
| --- | --- | --- |
| CONTRACT.md | a1b50ab4293c9d6132a874ed574b7843d0deae672a8928f73d1b9dcc7c09fed6 | 此前最终全文及合同专审；当前哈希。 |
| CONTRACT_REVIEW.md | 791c80270135a1a08e6aea43840cdde8dd5faa0ddc71c6c767d8f3efcc892a73 | 本人此前全文自读停稿；不是新独立来源。 |
| ANALYSIS.md | fdf1a250da8a8f02e3343000f206e9f4f45fe159fb7b7352171d4e08b0fe3367 | 此前逐式审最终稿，本次又全文。 |
| ANALYSIS_REVIEW.md | 02288305451808829feace3ac1f97480ee7cf1f918e011cbbe5a2c9f1cc7080c | 本人此前全文自读停稿；历史条件范围。 |
| METHOD_PREFLIGHT.md | f2c7d90186f083601cab5bc5411d5c60826b963d6ed29efe9e4dfde5e149c316 | 此前全文；固定根/坐标、原 Horner、32 步与 DR.8 门。 |
| INDEPENDENT.md | 68957784dd943eca6968973aeb61a49e4453a3410b816c67e59d4f61384eedc4 | 本最终阶段首次全文，DI.1–20 及来源。 |
| INDEPENDENT_REVIEW.md | f8db95b2549d02c9f28fc84fa8d78ef65c235c646743015194a452a18b4a8b04 | 本最终阶段首次全文，身份和不同条件窗。 |
| exact_difference.py | 842679b23991ae2f3f5a5cd76903e9abf4ebd7a71a230829f99697612ad66030 | 此前完整 723 行静审；本次哈希/字节。 |
| PRIMARY_CODE_REVIEW.md | e3371c5491d9b38dbbeb4fc8a2c69655dceed7a7828e6dfa6a5aa2b193c0cd6d | 本人此前全文自读停稿。 |
| PRIMARY_ROOT_READ.md | e4e9d7ec242da5ff306c901761943281556843a3c458a3efd3d296fd9419cd1e | 本次全文；根源码实读的独立记录。 |
| exact-difference-output.json | 2ecedeb13a1b7f521e286d520e28245964b01a6cde1d3c56232ddb9ae67eff7b | 本次第 1 节定向原字段，完整下界/原窗及已存对象相等比较。 |
| primary-execution.json | a16d978a4599bc55ebeac80bda83d9f0858d35c1892983572e86cb1fd98b4c26 | 本次全文，实际命令/回执和历史 pending。 |
| ALGEBRA.md | 3ec995558d2ece57fcab1fe00ad4a3a0fa7e211bbd988024344a8a24f80901de | 本次全文，DA.1–5；主作者结果转录。 |
| verify_difference.py | 87fd73e0b5a7235f4ff083741c96332e4b663706e5aad492d0a9a32f4b30294a | 此前完整 1415 行静审；本次哈希/字节。 |
| VERIFY_CODE_REVIEW.md | b69df555e3125b4ea7dcbf46fd04a2c101a4bba0755b526b2cf65130f8836f47 | 本人此前全文自读停稿；静态通过不代替实际运行。 |
| VERIFY_ROOT_READ.md | 353e6b6db295ef52bfed9f3664497935408aa258fb52f44165b1ac79cda4e456 | 本次全文，根实读及未运行时身份。 |
| VERIFY_ADAPTATION.md | 19a6a49237e049352e5878959cf19e4d1e358a8cf97f568116cdd75f156a7a7a | 此前全文；核心与实际主 schema 的适配次序。 |
| VERIFY_DESIGN.md | cb991c6e2c82b729424323bae90a673adaecf7253091533d6b0a13e7ff89ccd3 | 本次首次全文；此前仅核哈希的经历不改写。 |
| verify_core_pre_output.py.txt | d65938f58fa364e3da172ed7d98af81c05ee5a80a4c3f5b251005dbe59e3decb | 仅核当前哈希/23548 字节，未全文读该惰性历史核心。 |
| review-difference-output.json | e2d266940b4e98423af01ab6bcaf756d5c2255123cfeb9ab7d587e8c903f5e75 | 本次第 1 节定向类别、原值/窗/路径/六向量/全部来源资源；不是人工全文巨整数手算。 |
| verifier-execution.json | 42adefd2427d40195a733eabf5eb061b165017a1a13f772b2dba8c0887b43f63 | 本次全文，唯一实际执行、外层来源记录。 |
| VERIFY_RESULT.md | 23c5a17d0f237042dbaef06bd7f4d6fb569588b8fc99d1629a9d3fa39778235b | 作者停止后本次全部 124 行全文；程序作者的结果解释，非最终审查。 |
| RESTART_QUESTION.md | 7a67359779a29280bbd3e61abba420f051a863f1cc50d20bfa313039ca987bca | 此前全文及量词预锁；当前哈希。 |
| RESTART_LEMMA.md | c9e0170bb8787bfa1a629485c50b69e46dd9bcc53b485d9f411fe8649c4eb474 | 此前逐式全文审，本次又全文；全部 RL.1–10。 |
| RESTART_REVIEW.md | 928e645788d53cf6606bb808307eef6bdf866ce5cc6f15fcaf6ef59b3887ca54 | 本人此前停稿，本次又全文；h 窗与比例窗区别。 |
| conditional-acceptance.json | dd80dc52e2437cf166eda35ae5de4d9080b3e7e8a39b6c8c03693aae96dab084 | 本次全文；历史八项检查点，不是当前最终接纳。 |
| OUTCOME.md | e0c52ec7ca97a75c01e62ad3968df450b4e548d3415db23c75743fa79196ecea | 本次最终全文。 |
| EXPERIMENTS.md | 10008fe798f05870bb5fb004e282d556de5e036195f69808ce87f06ec22ac42c | 本次最终全文；两次原执行及非科学失误。 |
| experiment-manifest.json | 1456b10cf38b52ab2fa0ecc9fc8bac504043d70676b7feefb007dd2b47f97ce4 | 本次全文，原资源/范围与待最终接纳字段。 |
| figures-manifest.json | 4a261db924a9143aedf73d34cdf0c6c60f032bf50217b66fe8e66c2143cafbda | 本次全文；无新科学图档。 |
| ROOT_COMPARISON.md | d7696cf1573a041813213e7fbd8b8622d106bd156652a8a2ecec52225397d3ba | 本次完整最终文本，历史条件段及后追加实际执行段。 |
| SOURCES.md | eacfef8a09427cbc1ce3719c61ab60cab8dc721f6e541357210a2c556f303b74 | 本次完整最终文本；来源身份和阅读次序。 |
| root-source-binding-check.json | 60f95ae8c92dc51e4d6582487892926f27f08cf3e62b60e5a272657d5976747d | 本次全文；根的 22 条运行输入及八条历史对象元数据核对记录，不是本人执行 Git。 |

以下旧源路径相对 research/reverse，当前 SHA 亦实际复核；没有重复整个旧成果链或把哈希读证写成新全文认证。

| 旧源 | SHA-256 | 本人实际阅读/沿用范围 |
| --- | --- | --- |
| cyclic-six-carrier/PROOF.md | afd6b0009d7b357dd9ed6c9feaeb8dbb15535a5499dbd8be7911883e3c4f2725 | 既有专审/冻结阶段已全文读；本次同字节，沿同 a_*、D、原窗输入。 |
| cyclic-six-carrier/APPLICATION_PROOF.md | 096f626a754654039922eae0b13354e27e870ef113ee0967ffaebd29713955d4 | 本连续任务实际全文读，沿完整 NS 与同数据尾接口。 |
| cyclic-six-carrier/APPLICATION_REVIEW.md | 909e9fab28529f74aa66dc92a9790a3669b791a55ffd2b7709e3ff412b515c1f | 此前已全文读并接纳的非作者应用审查；本次哈希。 |
| cyclic-six-carrier/exact-coefficients-output.json | 9329464c09faa50558bc090b3af8c3ec6f074619e01a9fe2d5eb6d0f1c079ae6 | 本阶段核当前哈希/469369 字节与输入绑定，不重展旧 A 数学数组。 |
| cyclic-six-carrier/exact-roots-output.json | 6fd933ebd18bdf8b129f7cabdbf1f02438de3fd95f9720b18e41887815f31bcb | 旧阶段已定向读所需根/规范/窗；本阶段核哈希/139696 字节及两端保存接口，不重筛全根。 |
| four-leaf-preflight/GENERAL_SOURCE_BRIDGE.md | 59354781b8d04087cf1d5383824dbe741d24b3c0fae8798caa6c50cae24a3ebe | 历史已全文；本连续任务又实际读第 1–180 行，调用 GS.6、8–15，未重建全链。 |
| cyclic-receiver-supply-preflight/PREFLIGHT.md | 841cc7e26a4d8b8c3e8f930e2a2da47824fdcba43cee1fd37e40864a32cf5b58 | 本连续任务实际全文读，固定 F/D、差型唯一二叶与支撑接口。 |
| cyclic-receiver-supply-preflight/REVIEW.md | 960cdc0517b1ac3c36b1cf6ca1ca5d9599876705c553a825fc076ea4f5e16be7 | 本连续任务实际全文读，旧结构预检范围。 |

本文只写本文件；已实际全文自读并复核所列停定来源后停止修改，另报自身最终 SHA，不在自身表中自绑定。没有科学执行/导入/编译、参数或窗口重选、旧程序重跑、Git、外发或发布；未来接纳与冻结记录由根另行完成。
