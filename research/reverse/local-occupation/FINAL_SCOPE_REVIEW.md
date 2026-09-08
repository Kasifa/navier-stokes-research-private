# 局部 L² 持留与时间占比的合并最终范围复核

2026-09-08，PRIVATE_CORE。结论：当前两阶段的声明范围与最终字节通过本次有限、非盲合并复核。17 份指定现有文件已经逐份实际全文读取，两个 acceptance.json 的 14 个不同文件绑定与当前 SHA-256 全部一致。未发现必须修改的数学、范围或接纳绑定问题。本审查不是第三路独立证明，不证明任何实际候选。

本人是 local-occupation/INDEPENDENT.md 作者，有此前源桥接、代数接口及多轮非作者和最终范围审查经历。本项独立稿形成时只读当时合同及其指定旧输入，未读 weak-local-exit 新稿或 local-occupation 主稿；这些历史在原稿中保留。本次已后读两阶段全部指定文件，属于非盲最终复核，不能把这次阅读改称新的互盲推导。本人不改写任何既有文件。

## FS.1 实际阅读与 14 项接纳绑定

下表路径均相对 research/reverse/，每一行本轮均全文实读并实际取当前散列。表中“绑定”指该阶段 acceptance.json 的 files_sha256 条目，不是引用次数、证明数量或独立审查人数。

| 文件 | 当前 SHA-256 | 接纳绑定核对 |
|---|---|---|
| weak-local-exit/CONTRACT.md | 2eba0d26399480d98c1d29e288b0f1726b33ca14dc103092936e20749689664f | 一致 |
| weak-local-exit/PROOF.md | fb94de563dc2a95dad6cd21209724239c5b924ac27097f3610448d37e718a54d | 一致 |
| weak-local-exit/INDEPENDENT.md | fd9b40918c527ba2e07c54b497bbb7cff4aaddff02ec16eee394dbd237aa436e | 一致 |
| weak-local-exit/REVIEW.md | de57fb3c89a95c7dba14e29f5336985f8afc76f1ab9c2f72c2847595e70f8daa | 一致 |
| weak-local-exit/INDEPENDENT_REVIEW.md | aaaa7719beec4a166be5a6438712c51c5c82f7eb1ff9d1869d65dd6a3938257d | 一致 |
| weak-local-exit/ROOT_COMPARISON.md | b917a7529f6932cae6b8246917146907c70da22c95745ec78e999ff972bca856 | 一致 |
| weak-local-exit/OUTCOME.md | db8ff819f25c43dd9747e7c68d1142b5bdf03f2f843e67792806226de5c7dc99 | 一致 |
| weak-local-exit/acceptance.json | 4f00c055c95d3292b80e5e578cfe1c9b3c1c5571e9ea2c134d0b3acea76d8207 | 接纳表自身，不作自绑定 |
| local-occupation/CONTRACT.md | 368fc878d7f35223b5ebe96dee84cd99b33573cb9ba0208e7e795c0214bd1485 | 一致 |
| local-occupation/PROOF.md | 5195d555303bb3eea702045f7b38e46ab8a73b1c32eeedb9614ff2dad310e22a | 一致；LO.13 修订后最终字节 |
| local-occupation/INDEPENDENT.md | 81fe49793284e79f3a54e7efb52fa6de80c965901e96cd6136017c9cbd2f6f1e | 一致；本审查作者的既有稿 |
| local-occupation/REVIEW.md | 5a2ad398db5561d958a964183d7d3cfed9760945e637ab3d6c9d01824e266894 | 一致 |
| local-occupation/INDEPENDENT_REVIEW.md | a598a86a876084d8d9f0bc17262a69517d6da0148a75b42cdf96e9fff6d2b5c4 | 一致 |
| local-occupation/ROOT_COMPARISON.md | b3dd31384dab5838df298f9acb46078e772fdf32a772c8bee71c852e88e3039e | 一致 |
| local-occupation/OUTCOME.md | fa94bd4c850c539ed531af55215abb96ea369db6ef3cbd33250d34467711cb2b | 一致 |
| local-occupation/acceptance.json | 1a670a45783aad07eb23805f2c2c6e7e444edeb6dd72cae0687ae949672cdeaa | 接纳表自身，不作自绑定 |
| local-occupation/FINAL_OUTCOME.md | 2148279981f5a7c09bd634d5ae723fcf6195d532ee8588ac1c59fbf5f4f95650 | 本次合并范围对象，不冒称已在前两表内 |

两个接纳表各有 7 个不同的 Markdown 文件条目，两组完整路径互异，故共 14 个不同绑定。再加两个接纳表及 FINAL_OUTCOME.md，是本次 17 份现有对象；加入本审查后为 18 份文本。这个计数没有科学质量含义。

旧 exterior-pressure 来源在各作者及审查者原文中有实际阅读范围与散列记录；本次没有再次打开旧源，也不把原文的内部转引计作本次新增实读。这里复核指定两阶段已写论证、实际接纳接口与合并范围，不另扩展旧源定理或核验未读取对象。没有读取 NEXT_DYNAMIC_SCOPE_SCREEN 或其它后续科学稿。

## FS.2 同一固定原解与公共测试接口

两阶段都使用同一固定光滑初值的真实、无外力、单位黏性周期 NS 原解，只在实际存在的时间讨论。旧坐标
\[
\tau=T_*-t,\quad T_*=\frac1{100},\quad s=-\log\tau\ge\log100,\quad
d=\tau^{2/5},\quad F=\tau^{3/5}u(t,dy)
\]
和固定球、固定形状 V、事先固定的非负非零紧支撑测试 chi 不在每个区间重选。全部局部 L² 范数用未归一化 Lebesgue 测度。

两稿使用的真实重标方程都保留
\[
F_s+\frac35F+\frac25(y\cdot\nabla)F
-e^{-s/5}\Delta F+(F\cdot\nabla)F+\nabla P=0,\qquad
\operatorname{div}F=0.
\]
固定 \(\Psi=\operatorname{curl}(\chi e_\theta)\) 紧支撑且无散。chi 可以含方位依赖，实际 F 不要求轴对称；固定 V 的纯方位结构仅用于固定项的配对。完整周期压力严格通过 div Psi 消去，不能描述成忽略外部压力。

共同的正积分为
\[
Q_\chi=16b_2\int_{B_*}\chi\,r(z-3/2)h'(\sigma)h''(\sigma)>0.
\]
正号已在整个固定球而非仅中心一点支付；它不是旧单点常数。固定线性配对为零、固定非线性为负的 \( -Q_\chi\)，与任意实际误差的线性项为零是不同命题。

令 E=F−V，e=||E||₂，m=∫F·Psi。两阶段都核到同一个完整恒等式：
\[
\begin{split}
m'={}&-Q_\chi+
\int E\cdot\left[\frac35\Psi+\frac25(y\cdot\nabla)\Psi
+e^{-s/5}\Delta\Psi\right]\\
&+\int(E\otimes V+V\otimes E+E\otimes E):\nabla\Psi .
\end{split}
\]
梯度约定为 \((\nabla\Psi)_{ij}=\partial_j\Psi_i\)。漂移系数来自 \(3(2/5)-3/5=3/5\)，黏性测试项号为正，两条有序交叉项和平方项都保留。将 E 的空间导数转给固定测试，不等于对实际 F 作 Euler 近似。

## FS.3 连续持留：分别保留两稿常数与整窗条件

weak-local-exit 主稿的
\[
J_\chi=\|\Psi\|_2,\quad M=\|V\|_2,\quad
G_\chi=\|\nabla\Psi\|_{\infty,F},
\]
\[
H_\chi=\|\tfrac35\Psi+\tfrac25y\cdot\nabla\Psi\|_2+
\|\Delta\Psi\|_2,\qquad
L_\chi^{\rm main}=1+H_\chi+G_\chi(2M+1)
\]
用 \(e^{-s/5}\le1\) 及 \(e\le\varepsilon\le1\) 给单线性误差预算。若整个实际区间都满足 e≤epsilon，且
\[
0<\varepsilon\le
\min\{1,Q_\chi/(2L_\chi^{\rm main})\},
\]
则两端点各自 \(|m|\le J_\chi\varepsilon\)，给
\[
\ell=s_1-s_0\le \frac{4J_\chi\varepsilon}{Q_\chi}.
\]
epsilon=0 的正长区间由固定负作用与 m 恒零直接排除，未除以 epsilon。

该阶段独立稿的 \(N_\chi=J_\chi\)、\(B_\chi=G_\chi\)，但同名 \(L_\chi\) 准确为另一常数：
\[
L_\chi^{\rm ind}=
\tfrac35\|\Psi\|_2+\tfrac25\|y\cdot\nabla\Psi\|_2
+100^{-1/5}\|\Delta\Psi\|_2
+2\|V\|_\infty\|\nabla\Psi\|_2 .
\]
它给 \(L_\chi^{\rm ind}e+B_\chi e^2\) 的残差界。独立的一般正分母条件及结论是
\[
\varepsilon\ge0,\quad
Q_\chi-L_\chi^{\rm ind}\varepsilon-B_\chi\varepsilon^2>0,
\qquad
\ell\le
\frac{2N_\chi\varepsilon}
 {Q_\chi-L_\chi^{\rm ind}\varepsilon-B_\chi\varepsilon^2}.
\]
该一般式不预先要求 epsilon≤1；独立便用阈值
\(\min\{1,Q_\chi/[2(L_\chi^{\rm ind}+B_\chi)]\}\)
才给同形式的 \(4N_\chi\varepsilon/Q_\chi\) 界。两个 L 不可等同，未证明它们对所有 chi 有统一大小关系。独立附加的测试点态式、整球显式下界和一般分母式分别归属独立稿，没有倒填主稿。

本阶段必须有一个连续区间上的强局部 L² 近邻条件。“弱测试”不表示弱 L² 收敛或弱解已付时间迹。有限开区间可取紧子区间使用同一常数，不需要未知奇性端点的迹。此阶段只限制每次满足条件的连续持留长度，不单独限制进入次数、多个区间的总测度或累计时长。

## FS.4 占比阶段：全胞能量与两个不同黏性预算

local-occupation 使用真实原解能量，先在整个扩大周期胞换元：
\[
\int_{\tau^{-2/5}(-\pi,\pi)^3}|F|^2\,dy
=\tau^{6/5}\tau^{-6/5}\int_{(-\pi,\pi)^3}|u|^2\,dx
\le\|u_0\|_2^2.
\]
这不是归一化胞均值，也没有对移动胞边界作未付的微分。固定球在各实际扩大胞内，因此先有局部 ||F||₂ 上界，再有全时任意大小误差的三角上界。能量属于同一初值，不能逐段重置。

为避免同名常数串用，该阶段两稿的准确对应为：

| 主稿记号 | 独立稿记号 | 共同含义 |
|---|---|---|
| U* | H | 原初值未归一化全胞 L² 范数 |
| M | v* | 固定 V 的局部 L² 范数 |
| D=U*+M | M=H+v* | 全区间误差上界，e≤D |
| Q | Gamma | FS.2 的正积分 |
| J | p* | Psi 的局部 L² 范数 |
| G | b* | 梯度 Psi 的 Frobenius 范数上确界 |

占比主稿的 H 是测试导数预算，独立稿的 H 是初值能量范数，二者尤其不能混用。令
\[
H_0=\|\tfrac35\Psi+\tfrac25y\cdot\nabla\Psi\|_2,\qquad
d_*=\|\Delta\Psi\|_2 .
\]
采用上表主稿 M、D 时，主稿和独立的系数分别为
\[
C^{\rm main}=1+H_0+d_*+G(2M+D),\quad
a_*=H_0+2GM,\quad C_*=a_*+GD,
\]
所以同一 chi 下准确有 \(C^{\rm main}=1+d_*+C_*\)。

主稿用黏性系数≤1、e²≤De 给全大小残差界 \(|m'+Q|\le C^{\rm main}e\)。两端点来自能量 \(|m(s_k)|\le JU_*\)，不从近邻假设取得。因此
\[
\int_{s_0}^{s_1}e\,ds
\ge\frac{[Q\ell-2JU_*]_+}{C^{\rm main}}.
\]
对 \(0\le\delta<\min\{D,Q/C^{\rm main}\}\)，主稿给
\[
|\{s\in[s_0,s_1]:e(s)>\delta\}|
\ge
\frac{[(Q-C^{\rm main}\delta)\ell-2JU_*]_+}
 {C^{\rm main}(D-\delta)}.
\]
上述主稿结论完全不要求全窗或端点接近 V，亦不要求 e≤1。

独立稿则先保留完整二次残差和正黏性，以 e≤D 将黏性积分支付为
\[
\mathcal B_{01}
=2JU_*+5d_*D(e^{-s_0/5}-e^{-s_1/5}) .
\]
设 \(G_*(x)=a_*x+Gx^2\)。其独立结论准确为
\[
Q\ell\le\mathcal B_{01}+\int G_*(e)\,ds,\qquad
\int e\,ds\ge\frac{[Q\ell-\mathcal B_{01}]_+}{C_*},
\]
\[
|\{e>\delta\}|\ge
\frac{[(Q-G_*(\delta))\ell-\mathcal B_{01}]_+}
 {G_*(D)-G_*(\delta)},\qquad 0\le\delta<\delta_*,
\]
\[
\delta_*=\frac{\sqrt{a_*^2+4GQ}-a_*}{2G},\qquad
G_*(\delta_*)=Q,\quad 0<\delta_*<D.
\]
独立额外结果的黏性预算可积、分区前保留二次项；主稿的黏性包含在逐时线性系数内。两者都支付黏性，但不能把独立的较小系数与主稿仅两端点的预算拼在一起。有限区间的斜率与预算同时不同，本合并不声称哪一个在每个有限区间统一更强。

## FS.5 正性、零支及取极限的存在条件

共同恒等式给 \(0<Q\le GM^2\)，其中此处 M 是主稿的 ||V||₂。因此 G>0、M>0、J>0，D≥M>0；主稿 \(Q<C^{\rm main}D\)，独立 \(G_*(D)>Q\)。所有声明域的分母严格正，所得正渐近比例严格小于一。d*=0 在公式中不被当作分母；U*=0 也未被除去。零初值时真实能量给 F=0、e=M、D=M，各允许阈值都小于 M，离开集合为整个区间，与各式相容。

delta=0 在声明域内。等号 e=delta 的时刻归入补集，分区估计仍成立。独立 delta=delta* 只给零斜率；超过该阈值并不由本证明获得正长期下密度。delta≥D 时离开集合为空，不能在 delta=D 继续套用零分母式。主稿也保留自身的严格阈值。短窗分子可能非正，正部仅给零下界，不表示每个时刻有正误差。

有限区间结论只需要同一原解在该实际区间光滑。只有另有同一初值原解在全部 \(0\le t<T_*\) 光滑，才能固定 s0、令 s1→∞。全局能量上界没有证明这个存在前提。

在该额外前提下，主稿得到平均误差下极限≥\(Q/C^{\rm main}\)，以及离开比例下极限≥
\[
\frac{Q/C^{\rm main}-\delta}{D-\delta}>0.
\]
独立的 \(\mathcal B_{01}\) 有与 s1 无关的有限上界，故其平均误差下极限≥\(Q/C_*\)，离开比例下极限≥
\[
\frac{Q-G_*(\delta)}{G_*(D)-G_*(\delta)}>0.
\]
这些是各自阈值域内的 liminf 声明，不证明平均值或占比本身有极限，不推出逐时误差下界，也不在未知存在区间外延长解。

## FS.6 时间量、持留量与历史记录

准确换元为
\[
ds=\frac{dt}{T_*-t},\qquad
\ell=\log\frac{T_*-t_0}{T_*-t_1},
\]
\[
|\{s\in[s_0,s_1]:e(s)>\delta\}|
=\int_{\{t\in[t_0,t_1]:\,e(-\log(T_*-t))>\delta\}}
 \frac{dt}{T_*-t}.
\]
它不等于无权 dt 测度。有限的物理总时间与无限重标时间相容；正的重标离开比例也不能直接改称普通物理时间比例。

一次连续持留上界、若干区间的总测度、访问或再进入次数、近邻累计时间绝对有限，是不同命题。本包在第一阶段控制每次连续持留，在第二阶段额外控制误差积分与离开集合的对数时间测度。正的离开下密度给近邻上密度小于一，但近邻累计对数时间仍可能无限，本界不排除任意多次重返。本包没有到达邻域或返回轨道的存在结论。

local-occupation/PROOF.md 的 LO.13 曾由根把积分域显式补为 t∈[t0,t1]。该主稿审查记录了初读及修订后再次实际全文读取，并绑定本表最终 5195d555… 字节。ROOT_COMPARISON 与当前 acceptance.json 一致承接这个最终版本。此修订澄清原有限区间，不新增假设、常数或结论；本次没有将旧未限域写法当作最终已审文本。

两个合同如实披露根在正式合同前已有手工路线预检；独立形成不等于整个课题无人先行接触。weak-local-exit 两作者形成时互不读新稿，其两份非作者审查由同一代理先主稿后独立稿作出，第二次为序贯而非互盲审查。local-occupation 两作者形成时互不读新稿，本人当时还未读前项新稿；其两名不同非作者审查人有前项作者或审查经历，各自在当时未读另一新稿。这些接触历史和根的非盲比较都已明确记载。本次后读范围复核不增加独立证明或独立审查人数的宣称。

## FS.7 最终可冻结范围

两个接纳表的 claims、scope 与对应 OUTCOME、ROOT_COMPARISON 以及合并 FINAL_OUTCOME 相容。原稿中形成时的“待审”文字是保留的历史状态，不可冒充当前仍未有审查；当前接纳也不倒写为形成时已获审查。

接纳上限为：同一已固定初值真实光滑 NS 在固定旧坐标、形状和测试下的局部强 L² 连续持留障碍，以及真实能量支持的非小误差积分与对数时间离开测度必要界；长期密度另有明确实际存在前提。不同黏性预算、阈值与附加结果分别保留。没有用一阶段的整窗小误差前提污染占比阶段，也没有把占比阶段的额外结论倒填前阶段。

没有实际新初值、函数、测试、容限、进入时刻或其它时间实例；没有真实再生成、单初值无限尺度、跨代统一无限维误差、弱解时间迹、任意快速平移旋转或其它动态形状、奇性或一般正则性结论。旧 NON-NS 路径仍是负对照，旧失败不追认。后续动态来源适用性筛选完全不在本包，本审查没有读取或接纳 NEXT_DYNAMIC_SCOPE_SCREEN。

当前两表的 formal_release 和 publication_handoff_performed 仍为 false；本次只核文本与散列，不执行源码对象冻结、Git、归档交接或发布。仅供私有归档及用户本地完整阅读，没有公共发布许可。所有操作限于文本读写、手工核对和 SHA 元数据，无科学程序、数组、数值求值、实际选参或扫描。

本文件完成后实际全文自读并重新核对来源字节，报告自身最终 SHA-256 后停改；自身散列不写回自身以制造自绑定。PASS WITHIN THE TWO FIXED CONTRACTS；NONBLIND FINAL SCOPE REVIEW；NO-CANDIDATE；NOT CLAY。
