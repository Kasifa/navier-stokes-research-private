# 完整 n1280 节点残差合同独立数学审查

2026-09-08。PRIVATE_CORE。**PASS：仅为指定解析合同的有限范围数学审查；新完整残差尚无执行结果。**

被审稿为 FULL_NODAL_RESIDUAL_CONTRACT.md。审查者未编写该稿，也未参与根代理提出的 NR.6、NR.9、NR.10 原式；本次从 Fourier 方程、投影和 Parseval 独立手推后核对全文。C1 合同及前项最终审查有本审查者自己的旧工作，作为已接受的定义和输入接口使用，不冒称另一次非作者复证。下述推导不以根代理或被审作者的结论作数学证明。

本轮只读正文、必要旧解析接口和已接受的记录，并对下表六个小文件核实际字节 SHA。没有重读前项二进制数组、重建节点、作卷积或根号核，没有运行 PDE、ODE、FFT 或新的科学证书，也没有选择后续根号精度、实现或计算预算。

## 1. 同一节点与共同分母

对象保持为同一个固定初值所定义问题中的唯一 Hermite 参照，在 n1280、物理时间 \(t_*=5/8\) 的值 \(c\) 和时间导数 \(d\)。参照不被当作原 NS 解。原时间斜率须从已保存的 slope_q52 解码；值中心或旧 \(T^{12}\) 都不能给出该斜率。

为核 NR.1，设原值的 Gaussian 整数编码为 \(Z_k\)，令 \(W_k=Z_k+\overline{Z_{-k}}\)、\(s=|k|^2\)。共轭平均后投影得到
\[
c_k=\frac{sW_k-k(k\cdot W_k)}{2Qs}
    =\frac{A_k}{D},\qquad
A_k=\frac{L_*}{s}\bigl[sW_k-k(k\cdot W_k)\bigr],\quad D=2QL_*.
\]
因 \(s\mid L_*\)，\(A_k\) 为 Gaussian 整数向量。同式对另一份斜率编码给 \(J_k\)，故 \(d_k=J_k/D\)。这证明共同分母可用，不要求 \(A_k/D\) 已约分。投影后 \(k\cdot A_k=k\cdot J_k=0\)，且保留共轭。

逐实虚标量的最近整数、平局取偶舍入是奇函数，因此从共轭的 \(c\) 得到共轭的 \(C\)。但分量舍入一般不保留 \(k\cdot C_k=0\)。本合同没有把这一点忽略，也没有再次投影中心而偷偷改变旧数据。

## 2. 六张量、保守算子和完整复符号

在全部有序 \(p+q=k\) 输入上，交换 \(p,q\) 得 \(T^{j\ell}=T^{\ell j}\)。输出收缩的三个分量明确为
\[
\begin{aligned}
F^1&=k_1T^{11}+k_2T^{12}+k_3T^{13},\\
F^2&=k_1T^{12}+k_2T^{22}+k_3T^{23},\\
F^3&=k_1T^{13}+k_2T^{23}+k_3T^{33}.
\end{aligned}
\]
非对角项进入不同输出分量，各有相应 \(k_j\)；不存在额外的系数 2。六项的对称性不准许删掉输入的空间反序。旧 \(T^{12}\) 的完整证据只供复用该项，其余五项仍须实际计算和审查。

Fourier 约定为
\[
B(c,c)_k=-iP_k\sum_{p+q=k}(c_p\cdot q)c_q.
\]
对原精确无散 \(c\)，有 \(c_p\cdot q=c_p\cdot k\)，故等于保守形式 \(\mathcal C_{\rm cons}(c,c)\)。对舍入后的非无散中心只使用保守形式；不能用中心的对流形式替代它。非零输出上
\[
P_kF_k=\frac{sF_k-k(k\cdot F_k)}s=\frac{N_k}s.
\]
由 \(u_t=\Delta u+B(u,u)\)，参照残差的符号为 \(d-\Delta c-B(c,c)\)。又 \(-\Delta c_k=sc_k\)，因此
\[
\widehat R_k=\frac{J_k+sA_k}{D}
             +\frac{iN_k}{sQP^2}
             =\frac{sQP^2L_k+iDN_k}{DsQP^2}.
\]
NR.5—NR.7 的黏性正号、非线性 \(+i\)、两个分母及实虚交叉号均正确。尤其 \(\Re(iDN)=-D\Im N\)、\(\Im(iDN)=D\Re N\)。先形成完整有符号 \(V_k\)，再平方，保留了线性与非线性之间的实际相消；这不等价于三个范数的三角和。

G 外只有 \(L_k=0\)；\(F_k,N_k,V_k\) 仍须在完整 H 上形成。压力投影使用物理输出 \(k\)，不能用打包位置或再截回 G。有限参照的完整残差支持包含于 H，不表示原 NS 解的谱也限制于 H。

## 3. 零模、共轭与投影

在 \(k\mapsto-k\) 下，张量变为共轭，继而
\[
F_{-k}=-\overline{F_k},\qquad
N_{-k}=-\overline{N_k},\qquad
iN_{-k}=\overline{iN_k}.
\]
结合 \(L_{-k}=\overline{L_k}\)，得到 \(V_{-k}=\overline{V_k}\)。不能误把 \(F,N\) 本身写成普通共轭。直接代数又给
\[
k\cdot N=s(k\cdot F)-s(k\cdot F)=0,\qquad
k\cdot L=0,\qquad k\cdot V=0.
\]
这些是必要一致性检查，不能替代独立完整卷积。

零频率的张量一般非零，须保留其数据；保守收缩中的输出因子 \(k=0\) 使非线性向量为零。原值和斜率的零模亦为零，所以 \(R_0=\widehat R_0=0\)。应直接作此定义，不在零模使用 \(1/s\)，也不额外加入压力均值项。

## 4. 平方范数、商余和根号包围

归一化 Parseval 用完整正负谱。全有序二阶导数的乘数和为
\[
\sum_{a,b=1}^3(k_ak_b)^2
  =\left(\sum_{a=1}^3k_a^2\right)^2=s^2.
\]
因此，以 \(S_k=|V_k|^2\)、\(H_0=D^2QP^4\)，有
\[
\|D^2\widehat R\|_2^2
=\sum_{k\ne0}\frac{s^2S_k}{H_0s^2}
=\frac{\sum_{k\ne0}S_k}{H_0},
\qquad
\|\widehat R\|_2^2=\frac1{H_0}\sum_{k\ne0}\frac{S_k}{s^2}.
\]
NR.9、NR.10 正确；不漏三个向量分量，也不再乘 9 或因共轭再乘 2。

每个 \(S_k\) 是非负整数。写 \(S_k=s^2a_k+\rho_k\)，则
\[
a_k\le S_k/s^2\le a_k+\mathbf1_{\rho_k\ne0}.
\]
完整 35936 个非零输出求和即得 NR.11、NR.12。余数为零的模式不增加上端；粗间隙至多 \(35936/H_0\) 合法。这里包围的是最后的平方范数，不是舍入每模 \(V\) 或 \(S\)。完整逐模数据与总和的来源连接是必要证据，仅给三个孤立总数不够。

独立核 NR.13：设 \(y=P^2A/H_0\ge0\)，\(\ell=\operatorname{isqrt}(\lfloor y\rfloor)\)。有
\[
\ell^2\le\lfloor y\rfloor\le y<(\ell+1)^2.
\]
最后一步成立，因为 \((\ell+1)^2\) 是严格大于 \(\lfloor y\rfloor\) 的整数。若且唯若 \(\ell^2H_0=P^2A\)，下端恰等根号；否则上端须取 \((\ell+1)/P\)。因此稿中根据有理数本身的精确等号决定 \(u\) 正确，不能只检测 \(\lfloor y\rfloor\) 是否平方数。\(A=0\) 时两个端点都为零。

零阶下端由 \(A_0^-\) 形成、上端由 \(A_0^+\) 形成，利用根号单调性合法；二阶两端共用精确 \(A_2\)。这里证明了任意预先固定非负整数位数 \(b\) 的公式，没有选择 \(b\)，也没有实际执行根号。

## 5. 原节点的双边连接

令 \(e=c-\widetilde c\)。保守双线性差完整展开为
\[
\mathcal C(c,c)-\mathcal C(\widetilde c,\widetilde c)
=\mathcal C(c,e)+\mathcal C(e,c)-\mathcal C(e,e).
\]
两份残差采用同一精确 \(c,d\)，故其线性部分严格相消；上述三项正是需要支付的差。对每个输出，Leray 在复 Euclidean 向量范数下收缩，收缩频率只贡献一个 \(|k|\)。完整 H 上 \(|k|\le16\sqrt3<28\)，再用标量实虚绝对和控制 Euclidean 系数、卷积的 \(\ell^1\) 界和 \(\ell^2\le\ell^1\)，得到
\[
\|D^j(R-\widehat R)\|_2
\le28^{j+1}(2M\delta+\delta^2)=E_j,\qquad j=0,2.
\]
这是对已有 CR 接口的独立手推复核；无需假设中心无散。实际使用旧 \(M,\delta\) 仍要求与同一 \(c,C,QP\) 绑定，不能把以前很小的一个数直接挪给另一中心。

三角及反三角不等式给
\[
\max(0,\underline h_j-E_j)\le r_j\le\overline h_j+E_j.
\]
NR.15 两侧均正确。\(E_j\) 加减于范数层面，不能从整数平方和减它，也不能当作平方范数误差。该引理本身没有给本节点新的 \(r_0,r_2\) 数值。

## 6. 结论和未支付事项

未发现阻断上述数学合同的错误，无需修改被审稿。稿中的“两个节点门”在此明确指同一节点的 \(r_0,r_2\) 两个范数门，不是两个时间点。

在 \(t_*=5/8\)，原残差幅度靶标 \(e^{-2t_*}\) 确为 \(e^{-5/4}\)；若比较平方范数才出现 \(e^{-5/2}\)。NR.16 使用幅度层面，指数正确。未来严格下界超过经有理外包的靶标，才可拒绝这个指定参照的指定包络；上界低于靶标也只认证本节点。当前不把旧浮点诊断用于否定 \(\varepsilon=2\times10^{-7}\)。

本 PASS 不包含新五张量、原斜率解码、完整 \(V,S\)、总和、根号区间、指数比较的执行正确性或成本。源码、一次预算、根号精度、独立计算方案和输出证据仍待固定及审查；不从旧单张量耗时外推。一次节点通过不产生邻域、全段或全时间窗界，也不接通原 NS 误差比较、延拓或奇性结论。

## 7. 实际输入绑定与审查来源

全文实读本次新合同；C1 定义及 CR 解析接口沿用已读文本并复核所用公式。旧 Kronecker 最终审查和精确比较记录在前项已完成实读及验收，本轮只核其文件字节，作为同一输入接口复用，不重新验收旧科学块。前项二进制与原节点档案的实际绑定由这两份已接受记录承载，本轮不重新读取它们。

下表路径相对反向科学工作树根目录。哈希核对只是字节绑定，不是新的科学计算。

| 输入 | SHA-256 |
| --- | --- |
| research/reverse/fixed-seed-global-screen/FULL_NODAL_RESIDUAL_CONTRACT.md | f3c5327e59931a2e638c039078f78175f4138c53eec139cc57c1ae5fd2cb513b |
| research/reverse/fixed-seed-global-screen/C1_RESIDUAL_CONTRACT.md | a001077c4e1828827a3e7738e154bdd1b02541ff44d63032a475e2f0b5017251 |
| research/reverse/fixed-seed-global-screen/CONTINUOUS_RESIDUAL_COST_PREFLIGHT.md | 0c7ea4b3d33d152f298058a909e446505150d1004529f1a4518c2e1fedc7f796 |
| research/reverse/fixed-seed-global-screen/CONTINUOUS_RESIDUAL_COST_ROOT_REVIEW.md | 4865cf0639e20bc6d8d6c2546e8382c08b59366814168ff2f0b309bc8ef4e5da |
| research/reverse/fixed-seed-global-screen/KRONECKER_COMPLETE_FINAL_REVIEW.md | f72989cbc34a828132d317fb0f62277568fb8691ef582b501e483fdeb14c3b1f |
| research/reverse/fixed-seed-global-screen/kronecker-independent-agreement.json | 5510285fed346165e428bac4dfcb572548283322937a712be6465829481b5779 |
