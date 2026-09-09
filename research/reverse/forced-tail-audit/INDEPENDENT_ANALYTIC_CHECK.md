# 零投影力区间的解析性与开空区：有界手工检查

2026-09-09，PRIVATE_CORE。本稿是条件解析检查作者稿，非第三份盲证明或外部论文验收；已获根关于固定紧支撑与解析性的提示，未读根本题推导、周期代理稿或新论文正文。经典正时间空间解析性不是本稿的原创定理。

**IA.1 假设。** \(D=\mathbb R^3\) 或连通平坦三维环面，\(\nu>0\)。同一实值无散光滑原解在 \([a,b]\) 满足
\[
\partial_tu-\nu\Delta u=B(u,u),\qquad B(v,w)=-\mathbb P\operatorname{div}(v\otimes w),\qquad u\in C([a,b];A^0).
\tag{IA.1}
\]
原解须有使全域 Leray 投影及 Duhamel 公式成立的衰减/压力资格；例如全空间光滑且 \(C([a,b];H^s)\), \(s>5/2\)，并满足上述投影方程。下证不处理仅局部光滑而无全域控制的场。对受迫原解，(IA.1) 的前提是整个域的 \(\mathbb Pf=0\)，不是核心局部残差为零。

**IA.2 规范和零模。** 全空间取 \(u(x)=\int\widehat u(\xi)e^{ix\cdot\xi}\,d\xi\)，周期用其对偶格的 Fourier 和与归一化 Haar。以下 \(\int_\Xi\) 同时指积分/求和，\(\|u\|_{A^0}=\int_\Xi|\widehat u|\)，向量取 Hermitian 欧氏范数；此规范下乘积对应无额外常数的卷积。\(H^s\to A^0\) 由 Cauchy–Schwarz 与 \(\int_\Xi(1+|\xi|^2)^{-s}<\infty\)（\(s>3/2\)）得到。周期规定 \(\mathbb P_0=I\)，而 div 的零模为0，所以均值保持，未把非零均值删去；全空间单点 \(\xi=0\) 对积分无影响。

**IA.3 热权重。** 将任一重启时刻 \(\tau\) 平移为0，置 \(\|v(t)\|_t=\int_\Xi e^{\sqrt t|\xi|}|\widehat v(t,\xi)|\)，\(K_\nu=e^{1/(4\nu)},\ C_\nu=\nu^{-1/2}e^{1/(2\nu)}\)。由配方及 \(y e^{-y^2/2}\le1\)，对 \(r\ge0,\delta>0\)，
\[
e^{-\nu tr^2+\sqrt t r}\le K_\nu,\qquad
r e^{-\nu\delta r^2+\sqrt\delta r}
\le(\nu\delta)^{-1/2}e^{1/(2\nu)} .
\tag{IA.2}
\]
因此线性项满足 \(\|e^{\nu t\Delta}u(\tau)\|_t\le K_\nu\|u(\tau)\|_{A^0}\)。这没有假设初值已经解析。

**IA.4 完整双线性项。** \(\|\mathbb P_\xi\|_{\mathrm{op}}\le1\)，故完整张量缩并满足
\(|\widehat{B(v,w)}(\xi)|\le|\xi|\int_\Xi|\widehat v(\eta)||\widehat w(\xi-\eta)|\)。
用 \(\sqrt t-\sqrt s\le\sqrt{t-s}\)、\(|\xi|\le|\eta|+|\xi-\eta|\) 和 (IA.2)，
\[
\|\mathcal B(v,w)(t)\|_t
\le C_\nu\int_0^t(t-s)^{-1/2}\|v(s)\|_s\|w(s)\|_s\,ds,\qquad
\|\mathcal B(v,w)\|_{X_h}\le2C_\nu\sqrt h\,\|v\|_{X_h}\|w\|_{X_h},
\tag{IA.3}
\]
其中 \(\mathcal B=\int_0^t e^{\nu(t-s)\Delta}B\,ds\)，\(\|v\|_{X_h}=\sup_{0\le t\le h}\|v(t)\|_t\)。符号/张量次序不影响此完整有序估计；无频率截断，零模亦在规范内。

**IA.5 压缩与原解识别。** 取 \(X_h\) 中同时 \(C([0,h];A^0)\)、实值无散的函数；它在上述范数下完备。热项连续；Duhamel 项的 \(A^0\) 连续性由端段 \(O(\sqrt\delta)\) 控制及其余段热核的强连续性给出。令 \(A=\|u(\tau)\|_{A^0}\)，\(R=2K_\nu(1+A)>0\)，选择 \(h>0\) 使 \(4C_\nu R\sqrt h\le1/2\)。映射 \(v\mapsto e^{\nu t\Delta}u(\tau)+\mathcal B(v,v)\) 在半径 R 的闭球内有界于 \(R/2+R/4\)，Lipschitz 常数至多 \(1/2\)，故得唯一该球内解析加权温和解 v。

为与既有原解识别，不假设原解的加权范数有限。去掉权重，同样有 (IA.3)，常数可取 \(C^0_\nu=\nu^{-1/2}\)。两个 \(C A^0\) 温和解的差在共同长度 \(\ell\) 的零初差段满足
\[
\sup\|u-v\|_{A^0}\le
2C^0_\nu\sqrt\ell\big(\sup\|u\|_{A^0}+\sup\|v\|_{A^0}\big)\sup\|u-v\|_{A^0}.
\tag{IA.4}
\]
选择系数小于1的短段，再正向逐段覆盖，给共同存在区间上的同数据唯一性。原光滑解的 Duhamel 公式由投影方程积分取得，故它就是刚构造的 v；A=0 的零解分支也由此识别。这里没有反向唯一性或延续到潜在奇时的结论。

**IA.6 每个内时刻的解析性。** 在任一紧时间窗内 \(\|u(t)\|_{A^0}\) 有界，所以上述 R/h 可统一选择。给定 \(a<t<b\)，从足够接近且严格早于 t 的 \(\tau\ge a\) 正向重启，就有 \(\int_\Xi e^{\sqrt{t-\tau}|\xi|}|\widehat u(t,\xi)|<\infty\)。Fourier 逆变换在 \(|\operatorname{Im}z|<\sqrt{t-\tau}\) 的每个较小管域绝对局部一致收敛，逐次微分由指数余量控制，因而是全域空间实解析函数；周期情形在覆盖空间解析并下降到环面。

**IA.7 空区与尾段的准确结论。** 若每个 \(t\in(a,b)\) 的 u(t) 都在某个非空开集为零（该集合可随 t 变），实解析恒等原理及 D 的连通性给 \(u(t)\equiv0\)。该原理只用同一切片的解析延拓；\(C A^0\) 连续性还给端点为零，但不向区间以前推理。

于是，对一个在 \([t_*,T)\) 每个紧子窗符合 IA.1 且每切片有开空区的原受迫轨道，若全域 \(\mathbb Pf=0\) 于整个尾段，则 \(u(t)\equiv0\) 对所有 \(t_*<t<T\)。排除这种尾段还须轨道在每个候选尾段中有非零切片，例如同一轨道所声称的临近 T 爆破。仅“更早曾非平凡”不足以排除后来停成零；不推出每一时刻 \(\mathbb Pf\ne0\)，也不给力下界。

全空间固定紧支撑与紧时间窗光滑性可支付本题所需 H^s/A0 资格及外部开空区，但实际支撑/非零/爆破须另核原文。周期化必须另有可核的周期空区和完整投影方程，不能只由全空间支撑直接导入。没有取消此几何前提的无力正则性结论。

**实际来源与未付项。** 全文读取两合同：CONTRACT.md，SHA-256 267f6257dbda8ed0db49d0bff7c3cff29b98455d89c8a51d557d54fcc40104c9；ANALYTIC_TAIL_CONTRACT.md，SHA-256 c2bbe821ec6d1799bad051a40461e37c0c9c635b77ac240541cfe5557798f500。未读新论文正文、未核其主定理或周期化；本文只按明列假设证明。

经典出处作定向定位：[Foias–Temam, Gevrey class regularity, 1989，出版社入口](https://www.sciencedirect.com/science/article/pii/0022123689900153)。本轮该正文入口返回403，仅定位书目信息，未把未读原定理或其适用范围用作上述估计的依赖；IA.2–6 为本轮手工给出的条件论证，基本 Banach 压缩及解析恒等原理不重证。本稿不是原创优先权声明。

仅文本手写与小文件哈希；科学 worker、数组/FFT/参数求值、Lean、Git及外发均0。全文自读后停止修改，交非作者核验；本文本身不验收外部受迫构造，也不恢复此前任何执行合同。
