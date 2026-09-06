# 弱压力兼容性与能量测试：降阶、底部准备及剩余压力项

2026-09-07（Asia/Shanghai）。基线：910e60d0c3e595331cdb4c2dd8e2a8d184f96b9a。
内部接口核验，不是科学发布冻结。G、R216–R217 和一般三维正则性 OPEN / NOT CLAY。

我检查的是 [Yu v1 §8.1](https://arxiv.org/html/2606.08352v1#S8.SS1) 的弱压力兼容性是否能进入真实 NS 的局部能量差测试。结果分成两部分：固定内部图上的底部 \(L^2\) 准备可以直接证明；动态测试仍没有由基本能量闭合。前者不应被旧弱迹障碍一并否定，后者也不能靠前者升级成正则性证明。

## 1. 范围与历史去重

空间维数三，先固定 \(\nu=1\) 和一个内部乘积柱体
\(Q=D\times J\Subset Q_{3/4}\)，\(D=\omega_h\times(a,b)\)。
\(u,p\) 为真实无强迫 NS 解。导数与精确等式先在一个光滑时间闭区间 \([s,t]\) 上计算；用于 suitable 极限时不得预先把粗糙解当成光滑测试。
\(V=(V_h,0)\)、\(\operatorname{div}_hV_h=0\)，若调用比较流方程，则明确另要求
\[
 \partial_tV-\Delta V+(V\cdot\nabla)V+\nabla\pi
 =F_V,\qquad F_V=(0,0,\partial_3\pi).
\]
不假设这个比较流已经构造好或其强界已经由 \(M\) 支付。令 \(W=u-V\)、\(q=p-\pi\)，所以 \(W_3=u_3\) 且 \(\operatorname{div}W=0\)。

使用 Yu 的小量估计时才加入其固定单位柱体假设
\(\Phi(1)\le M\)、\(\delta=\int_{Q_1}|u_3|^3\le1\)。
这不是对 G 中任意候选奇点自动成立的尺度一致输入。
\(p^{\rm rem}\) 是含至少一个 \(u_3\) 因子的局部 CZ 压力部分，
\(P=p-p^{\rm rem}\)，\(\bar P=\langle P\rangle_\zeta\)。
其已有界为 \(\|p^{\rm rem}\|_{L^{3/2}}\le C(M)\delta^{1/3}\)。

实际重读的历史源是 BS 弱迹稿、压力测试耦合合并报告、BT 凸压力迹稿和 BV 有符号混合压力稿。BS.5–BS.7 已说明能量级时间导数不能直接自测；BS.8–BS.14 与 BT.14–BT.17 已说明固定测试合法不等于撤去截断时一致可积；BV.17–BV.22 已区分联合压力消去与单项压力功。它们的原子条件、反时方程和解类不自动移植到本轮 \(u,V\)。

## 2. 竖向原函数的精确降阶

取 \(\zeta\in C_c^\infty(a,b)\)、\(\int_a^b\zeta=1\)，令
\[
 T_\zeta f(z)=\int_a^z f(y)\,dy-Z_\zeta(z)\int_a^b f(y)\,dy,\qquad
 Z_\zeta(z)=\int_a^z\zeta(y)\,dy.
\]
省略 \(x_h,t\) 参数。对 \(\phi_h\in C_c^\infty(Q;\mathbb R^2)\)，定义
\(B_\phi=T_\zeta\operatorname{div}_h\phi_h\)。
源引理的测试半范数是
\[
 \|\phi_h\|_{Y_\zeta}
 =\|(\partial_t+\Delta)B_\phi\|_{3/2}
  +\|\nabla_hB_\phi\|_3+\|\partial_3B_\phi\|_3.
\]
它在水平无散测试场上为零，按商空间理解。

现在取固定光滑空间紧支截止 \(0\le\chi\le1\)，允许它随时间光滑变化，暂不要求在 \(s,t\) 为零。记
\[
 f=\operatorname{div}_h(\chi W_h),\qquad
 F=\nabla\chi\cdot W,\qquad d=\int_a^bF\,dz=\int_a^bf\,dz.
\]
由于 \(\chi u_3\) 在竖向端点附近为零，
\[
 f=F-\partial_3(\chi u_3),\qquad
 B:=B_{\chi W_h}=T_\zeta F-\chi u_3.
 \tag{YT.1}
\]
这里 \(T_\zeta\partial_3(\chi u_3)=\chi u_3\)，不是近似等式。
因此
\[
 \partial_3B=\nabla_h\chi\cdot W_h-\chi\partial_3u_3-\zeta d,\qquad
 \nabla_hB=T_\zeta\nabla_hF-(\nabla_h\chi)u_3-\chi\nabla_hu_3.
 \tag{YT.2}
\]
这确实把表面上的二阶水平导数降为一阶解导数。但能量只控制这些导数的 \(L^2\)；源半范数要 \(L^3\)，不能据此宣布已经匹配。

## 3. 时间导数没有同时降阶

令 \(L_+=\partial_t+\Delta\)。对在竖向端点附近为零的光滑 \(F\)，直接求导得
\[
 [L_+,T_\zeta]F=-\zeta'\int_a^bF,\qquad
 L_+B=T_\zeta L_+F-\zeta'd-L_+(\chi u_3).
 \tag{YT.3}
\]
核对：\(\partial_3^2T_\zeta F=\partial_3F-\zeta'\int F\)，而
\(T_\zeta\partial_3^2F=\partial_3F\)。紧支假设消去端点导数；若不用紧支截止，不能沿用该式省略竖向边界项。

完整展开为
\[
 L_+F=\sum_i\left[
 (\partial_i\chi)L_+W_i+
 (L_+\partial_i\chi)W_i+
 2\nabla\partial_i\chi\cdot\nabla W_i\right],
\]
\[
 L_+(\chi u_3)=\chi L_+u_3+u_3L_+\chi+2\nabla\chi\cdot\nabla u_3.
\]
差分 NS 与第三分量分别给
\[
 L_+W=2\Delta W-u\cdot\nabla W-W\cdot\nabla V-\nabla q-F_V,
 \qquad
 L_+u_3=2\Delta u_3-\operatorname{div}(uu_3)-\partial_3p.
 \tag{YT.4}
\]
所以直接代入又引入二阶解导数、原压力梯度、比较流及其压力。此处的 \(+\Delta\) 是源测试的伴随符号，不能误换成 NS 的 \(-\Delta\) 来删除二阶项。

这是对这条估计的输入核验，不是证明真实 NS 不可能有更强界。尤其不能声称“固定 \(M\) 且分量足够小时，任意更小内部柱体都不可能有导数界”：已有正则性定理可以先给正则半径。先调用该出口再反过来声称产生了它的假设，不是本轮需要的非循环进展。

## 4. 两部分测试成本有不同尺度

将固定单位图缩放到 \(Q_R=R D\times R^2J\)，采用
\(W_R=R^{-1}W(x/R,t/R^2)\)、\(\chi_R=\chi(x/R,t/R^2)\)、
\(\zeta_R=R^{-1}\zeta(x_3/R)\)。同时令
\(u_R=R^{-1}u(x/R,t/R^2)\)、\(P_R=R^{-2}P(x/R,t/R^2)\)、
\(\phi_{h,R}=\chi_RW_{h,R}\)，并保留完整父柱体
\(\mathcal Q_R=\{(x,t):|x|<R,\ -R^2<t<0\}\)。
则测试原函数 \(B_R=R^{-1}B(x/R,t/R^2)\)，换元得到
\[
 \|L_+B_R\|_{L^{3/2}(Q_R)}=R^{1/3}\|L_+B\|_{3/2},\qquad
 \|\nabla B_R\|_{L^3(Q_R)}=R^{-1/3}\|\nabla B\|_3.
 \tag{YT.5}
\]
实际临界组合是
\[
 \mathcal Y_R=
 R^{-1/3}\|L_+B_R\|_{3/2}
 +R^{1/3}\big(\|\nabla_hB_R\|_3+\|\partial_3B_R\|_3\big).
\]
对时间紧支的测试，若缩放后的单位柱体满足同一个 \(M\)，源引理只给
\(R^{-1}|\langle\nabla_h\Pi_{\zeta_R}P_R,\phi_{h,R}\rangle|
\le C(M,D,J,\zeta)\delta_R^{1/3}\mathcal Y_R\)，
其中 \(\delta_R=R^{-2}\int_{\mathcal Q_R}|u_{R,3}|^3\)，使用完整父柱体，而非仅用内部乘积图的小量。
若测试在时间端点非零，还须加入 YT.7 对应的缩放端点项；不能直接套用此处的无端点不等式。
没有从能量得到 \(\delta_R^{1/3}\mathcal Y_R\to0\)。
源引理在固定图上没有尺度错误；错误将是把其依图常数当成跨尺度已付预算。移动中心还会产生相应的时间漂移项，本轮没有把固定柱体计算直接改称 G 的移动窗口结论。

## 5. 重新拼回完整压力，只回到局部压力功

以下在光滑时间带积分。令 \(H(x_h,t)=\int_a^b\chi W_h\,dz\)，则
\(\operatorname{div}_hH=d\)。
源配对是
\(J_{\rm osc}=\langle\nabla_h(P-\bar P),\chi W_h\rangle
=\int \partial_3P\,B\)。
水平平均项为
\(J_{\rm avg}=\int\nabla_h\bar P\cdot H=-\int\bar P\,d\)。
YT.1 给
\[
 J_{\rm osc}+\int\chi u_3\partial_3P
 =\int T_\zeta F\,\partial_3P
 =-\int PF+\int\bar P\,d,\qquad
 \int\chi W\cdot\nabla q=-\int(p-\pi)F.
 \tag{YT.6}
\]
最后一步同时加回 \(J_{\rm avg}\)、完整 \(p^{\rm rem}\) 和比较压力 \(\pi\)。因此平均项不是零；它与其他项合并后才恢复原来的 cutoff 压力功。组合消去不产生新的正耗散或单项压力上界。

第三分量方程的合法有端点形式是
\[
 J_{\rm osc}
 =-\left[\int_Du_3B\right]_s^t+
 \int_s^t\!\!\int_D
 \left\{u_3L_+B+u_hu_3\cdot\nabla_hB+
       (u_3^2+p^{\rm rem})\partial_3B\right\}.
 \tag{YT.7}
\]
原文光滑紧支时间测试没有端点；能量测试使用 \(s,t\) 时必须把它补回。若用 \(\eta_\varepsilon\) 把底部时间截掉，则
\(L_+(\eta_\varepsilon B)=\eta_\varepsilon L_+B+\eta_\varepsilon'B\)。
即便 \(B\) 光滑，若 \(B(s)\ne0\) 于空间 \(L^{3/2}\)，一个固定剖面、宽度 \(\varepsilon\) 的非平凡上升沿会产生
\(\|\eta_\varepsilon'B\|_{L^{3/2}}\asymp\varepsilon^{-1/3}\)。
这只是时间截止项的显式成本，不是奇异 NS 的构造；强迹可另行支付端点，不能用紧支测试的原式直接删掉端点。

## 6. 单固定内部图可以付清一项底部准备

这一部分不要求比较流已存在。只用 \(u\) 的无散性、固定 \(\Phi(1)\le M\) 和 \(\delta\)。
取一个固定矩形乘积图
\(D_0=(0,L_1)\times(0,L_2)\times I\Subset B_{3/4}\)，平移记号不影响论证。
取固定正长度时间带 \(J_-\Subset(-9/16,0)\)。

对
\(A(s)=\|u(s)\|_{H^1(D_0)}^2\) 和
\(D_3(s)=\|u_3(s)\|_{L^3(D_0)}^3\) 联合使用 Chebyshev：
各自超过平均值四倍的时间集至多占 \(|J_-|/4\)，所以可在公共好时间集选同一个 \(s\)，满足
\[
 \|u(s)\|_{H^1(D_0)}\le K(M,D_0,J_-),\qquad
 \|u_3(s)\|_{L^3(D_0)}
 \le (4/|J_-|)^{1/3}\delta^{1/3}.
 \tag{YT.8}
\]
第一项来自 \(A(1)+E(1)\)；若相应平均为零则该量几乎处处为零，直接取公共全测集。\(\delta=0\) 同样如此。这不是趋近奇点时的统一逐时 \(H^1\) 界。

在水平矩形 \(\omega_h=(0,L_1)\times(0,L_2)\) 定义
\[
 K_h=\nabla_h\Delta_{h,D}^{-1},\qquad
 P_D=I-K_h\operatorname{div}_h,\qquad
 a_h=P_Du_h(s),\quad g=u_h(s)-a_h.
\]
\(\Delta_{h,D}^{-1}\) 是零 Dirichlet 标量 Poisson 解算子。此处 \(P_D\) 不附加速度的零法向边界条件，不把它混同于通常带零法向条件的 Leray 投影。

有界性可以直接检查。取归一化二维正弦基，特征值
\(\lambda_{mn}=(m\pi/L_1)^2+(n\pi/L_2)^2\)，\(m,n\ge1\)。
对 \(w=\Delta_{h,D}^{-1}f\)，逐项微分和正弦/余弦正交给
\(\|D_h^2w\|_2^2=\sum\lambda_{mn}^2|w_{mn}|^2=\|f\|_2^2\)，
且 \(\|K_hf\|_2\le\lambda_{11}^{-1/2}\|f\|_2\)。
对右端 \(\operatorname{div}_hb_h\)，弱 Dirichlet 能量式
\(\int\nabla_hw\cdot\nabla_h\psi=\int b_h\cdot\nabla_h\psi\)
给 \(\|\nabla_hw\|_2\le\|b_h\|_2\)。
于是 \(P_D\) 在水平 \(L^2,H^1\) 有界；固定算子与 \(\partial_3\) 交换，得到完整三维 \(H^1(D_0)\) 有界。

因此
\[
 \operatorname{div}_ha_h=0,\qquad
 \|a_h\|_{H^1}+\|g\|_{H^1}\le C_{\omega_h}\|u_h(s)\|_{H^1},\qquad
 g=-\partial_3K_hu_3(s),\quad
 \|g\|_{H^{-1}(D_0)}\le C_{\omega_h}\|u_3(s)\|_2.
 \tag{YT.9}
\]
这里 \(H^{-1}(D_0)=(H_0^1(D_0))'\)。最后一式对测试函数转移竖向导数，再用 \(K_h\) 的 \(L^2\) 界，不假设 \(u_3\) 在竖向边界为零。

取任意固定实值 \(\xi\in C_c^\infty(D_0)\)。
因为 \(\xi^2g\in H_0^1(D_0)\)，
\[
 \|\xi g\|_2^2
 =\langle g,\xi^2g\rangle
 \le C_\xi\|g\|_{H^{-1}}\|g\|_{H^1}
 \le C(M,D_0,J_-,\xi)\delta^{1/3},
 \qquad
 \|\xi(u(s)-(a_h,0))\|_2\le C\delta^{1/6}.
 \tag{YT.10}
\]
竖分量的 \(L^2\) 实际有 \(O(\delta^{1/3})\)，用 \(0\le\delta\le1\) 合并成上述界。内部截止避免把不满足零边界条件的 \(g\) 直接当作 \(H_0^1\) 测试。
在物理尺度 \(R\)，对应的归一化底部能量满足
\(R^{-1}\|\xi_R(u(s_R)-A_R)\|_2^2\le C\delta_R^{1/3}\)，前提是所有图、时间带和输入先按 NS 缩放归一化。

这是单个固定内部图的实际底部改进，不是只重写弱迹。BS 只有初端弱 \(L^2\) 迹和时间积分的 \(H^1\) 控制，没有这里同一好时刻的点态 \(H^1\) 界。反过来，本节没有完成多图拼接、边界/全局兼容或比较流的构造；不能据此声称源文 Assumption 8.3 或 8.5 已证。

## 7. 压力余项的可付部分也要保留

如果 \(V\) 是第1节的光滑比较流，完整相对能量恒等式为
\[
 \frac d{dt}\int\frac{\chi|W|^2}{2}+\int\chi|\nabla W|^2
 =\int\frac{|W|^2}{2}(\partial_t\chi+\Delta\chi+u\cdot\nabla\chi)
  +\int q\,W\cdot\nabla\chi
  -\int\chi W_iW_j\partial_jV_i
  -\int\chi u_3\partial_3\pi.
 \tag{YT.11}
\]
积分形式必须包含底部的相对能量。YT.10 只在固定内部图上支付这一项，并不支付其余右端。

不能笼统声称 \(p^{\rm rem}\) 必须与 \(\nabla W\in L^3\) 配对。那只是拆开的水平体积分的困难；完整向量压力合并后，其余项已有
\[
 \left|\int_Qp^{\rm rem}W\cdot\nabla\chi\right|
 \le C(M)\delta^{1/3}\|\nabla\chi\|_\infty
       \big(\|u\|_{L^3(Q)}+\|V\|_{L^3(Q)}\big).
 \tag{YT.12}
\]
这是对已记录 \(V\) 的 \(L^3\) 大小的显式依赖；不能无证明把它改写成只依赖 \(M\)。取 \(V=0\) 时该项确实由当前局部输入支付，但水平主压力与调和部分仍在。

YT.11 中尚未支付的内容包括比较流强界、其压力残差、主压力的完整 cutoff 功，以及从底部小量到全窗口差的小性的传播。直接吸收三次输运项还会需要相应临界控制。源文先假设的局部 \(L^3\) 稳定性不能再作为这里的证明。
上述恒等式没有省略平均压力，也未因重新组合而产生新的强制耗散。

## 8. 接口结论与下一步

本轮付清的是单图底部准备 YT.8–YT.10，以及保留比较场大小的余项估计 YT.12。测试函数的空间降阶、正确尺度和完整压力重组也已明确。
但直接将 Yu Lemma8.2 用作能量差估计的路线没有闭合；其动态导数成本和主压力功仍未支付。这个接口到此停止，不自动进入 shadowing、时间正则化参数扫描或仿真。

尤其，\(\delta\) 小与固定 \(M\) 本身已经是已有单分量正则出口的输入。本轮没有从一般初值、每个指定候选奇点产生它们。局部底部准备不是 G 或一般首次奇点排除。

下一步先作一次策略复评，而不是继续相邻测试范数：以当前 G 合同与已核实的原子条件链为源，区分最终目标、足够条件、已证明恒等式和真正未付的动态输入；检查是否有被误当必要条件的足够成本可以合法撤去。最多提出一个明确的真实 NS 不等式候选，必须说明区别于已停止路线的结构与验证方式；没有这样的候选就保留未选定状态，不用重复筛查制造版本。此项复评不改变一般初值、指定中心及完整时间窗量词。

无独立新颖性或投稿价值结论，无奇点构造，无新读者产物、仿真或 DGX。本文属于内部研究记录，不触发发布；已有科学冻结和一次交接记录不变。
