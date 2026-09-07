# 原第一响应代理在指定 A₋₁ 绝对预算中的障碍

2026-09-07。PRIVATE_CORE。独立手算复核；只检验已经指定的代理与 `ANALYTIC_PREFLIGHT.md` G.15–16，不改初值、黏性、环面或旧冻结文件，不增加响应阶次，不运行 PDE 或控制 ODE。

结论：障碍成立。第一响应代理的完整残差在原六个轴模上留下精确的 \(2te^{-3t}a_k\)，另一个残差项因总坐标奇偶性不能抵消它。该六模贡献已足以迫使 G.15 的控制预算在任何可能通过终点门的时刻超过 1。这里只排除这个代理与这组单调绝对预算的组合，不排除原 NS 解或所有后验方法。

## 1. 固定代理与完整残差

沿用 first-cycle 的
\[
a=2(\cos x_3,\cos x_1,\cos x_2),\qquad
\nu=1,\qquad \mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3,
\]
\[
B_k(f,g)=-iP_k\sum_{p+q=k}(f_p\cdot q)g_q,
\qquad P_k=I-k\otimes k/|k|^2,
\]
以及 \(N=B(a,a)\)、\(C=B(a,N)+B(N,a)\)、\(G=B(N,N)\)。零模为 0，复点积按双线性延拓，系数范数用 Hermitian Euclidean 长度。

既有全场第一响应为
\[
\int_0^t e^{(t-s)\Delta}B(e^{-s}a,e^{-s}a)\,ds
=te^{-2t}N,
\]
因为 \(\Delta a=-a\)、\(\Delta N=-2N\)。故本次代理
\[
v_1(t)=e^{-t}a+te^{-2t}N
\tag{F.1}
\]
确实保留第一响应的真实热半群时间因子，不是新的时间 Taylor 多项式。它仍只是代理，未被识别为完整 NS 解。

精确地，
\[
(\partial_t-\Delta)v_1=e^{-2t}N,
\]
\[
B(v_1,v_1)=e^{-2t}N+te^{-3t}C+t^2e^{-4t}G.
\]
因此完整残差为
\[
\boxed{\mathfrak r_1:=(\partial_t-\Delta)v_1-B(v_1,v_1)
=-te^{-3t}C-t^2e^{-4t}B(N,N).}
\tag{F.2}
\]
两个有序混合作用均在 \(C\) 中，黏性已精确抵消第一响应的线性部分；这里没有省去压力或某个频率通道。

## 2. 从原物理场重算相位与投影

令 \(S(x)=\sin x_1\sin x_2\sin x_3\)。直接微分给
\[
N=4(\cos x_2\sin x_3,\cos x_3\sin x_1,\cos x_1\sin x_2).
\]
各分量不含同序坐标，故 \(N\) 无散。继续直接微分：
\[
-(N\cdot\nabla)a=8\nabla S,
\qquad
-(a\cdot\nabla)N=D+8\nabla S,
\]
其中
\[
D=-8(\cos^2x_2\cos x_3,\cos^2x_3\cos x_1,
\cos^2x_1\cos x_2).
\]
\(D\) 也无散；\(S\) 是周期标量。因此完整 Leray 投影给
\[
B(N,a)=0,\qquad C=D.
\tag{F.3}
\]
反序项为零是其整个梯度场被压力吸收的结果，不能据此删除其他阶的反序项。

为独立核实 Fourier 符号，而不只照录物理式，检查 \(k=e_1\)。原数据为
\(a_{\pm e_1}=e_2,a_{\pm e_2}=e_3,a_{\pm e_3}=e_1\)。由 \(N_2=4\cos x_3\sin x_1\)，
\[
N_{e_1-e_3}=N_{e_1+e_3}=-ie_2.
\]
全部相容的 \(B(a,N)_{e_1}\) 项如下：

| 种子 \(p\) | \(q=e_1-p\) | 完整核贡献 |
| --- | --- | --- |
| \(e_3\) | \(e_1-e_3\) | \(-iP_{e_1}[(e_1\cdot q)(-ie_2)]=-e_2\) |
| \(-e_3\) | \(e_1+e_3\) | \(-iP_{e_1}[(e_1\cdot q)(-ie_2)]=-e_2\) |
| \(\pm e_2\) | \(e_1\mp e_2\) | \(a_p=e_3\)，而 \(q_3=0\)，故为 0 |
| \(e_1,-e_1\) | \(0,2e_1\) | 相应 \(N_q=0\) |

这里 \((-i)(-i)=-1\)，且 \(P_{e_1}e_2=e_2\)。反序 \(B(N,a)_{e_1}\) 中所有有支撑的有序项，其 \(N_p\) 极化与种子波矢 \(q\) 点积均为 0；这与 F.3 的全场压力结论一致。于是 \(C_{e_1}=-2e_2\)。F.3 的循环分量以及实值共轭关系同样给出全部六项：
\[
\boxed{C_{\pm e_j}=-2a_{\pm e_j},\qquad j=1,2,3.}
\tag{F.4}
\]

还可用 \(\cos^2x=(1+\cos2x)/2\) 完整展开 F.3。除了上述六项，\(C\) 只有
\[
C_{(\pm2,\pm1,0)}=-e_3,\quad
C_{(0,\pm2,\pm1)}=-e_1,\quad
C_{(\pm1,0,\pm2)}=-e_2,
\]
每组符号独立。这逐项重现旧 `ALGEBRA.md` §2 的全部十八模结果，保留轴模反馈和原本会出现的三坐标梯度项的投影相消。

## 3. 总坐标奇偶性使轴残差不能相消

定义两个格点类
\[
\mathcal E=\{k:k_1+k_2+k_3\equiv0\pmod2\},
\qquad
\mathcal O=\{k:k_1+k_2+k_3\equiv1\pmod2\}.
\]
\(N\) 的十二个模式均有两个坐标为 \(\pm1\)、一个坐标为 0，故其支撑包含于 \(\mathcal E\)。卷积波矢相加，导数和 Leray 投影均不移动波矢，所以
\[
\operatorname{supp}\widehat{B(N,N)}\subset\mathcal E+\mathcal E
\subset\mathcal E.
\tag{F.5}
\]
这是总坐标和的奇偶性，不是“每个坐标都为偶数”。既不需要计算 \(G\) 的所有系数，也没有声称 \(G=0\)。全部六个轴模在 \(\mathcal O\)，故 \(G_{\pm e_j}=0\) 精确成立。

结合 F.2、F.4，原轴模的完整残差为
\[
\boxed{(\mathfrak r_1)_{\pm e_j}=2te^{-3t}a_{\pm e_j}.}
\tag{F.6}
\]
每个轴模频率长度、\(|a_k|\) 都为 1。因此对齐次范数
\(A_{-1}(f)=\sum_{k\ne0}|f_k|/|k|\)，有
\[
\boxed{A_{-1}(\mathfrak r_1(t))\ge12te^{-3t}.}
\tag{F.7}
\]
这是真实残差的谱子和下界，没有用绝对值上界冒充下界。

实际上 \(C\) 的全部十八模在 \(\mathcal O\)，与 F.5 完全分离。所以还有精确恒等式
\[
A_{-1}(\mathfrak r_1(t))
=te^{-3t}\left(12+\frac{12}{\sqrt5}\right)
+t^2e^{-4t}A_{-1}(G),\qquad t\ge0.
\]
本次障碍只使用更弱且完全已核算的 F.7，不需要为 \(A_{-1}(G)\) 添加新的计算。

## 4. 指定 G.15–16 预算的必失败证明

由于 \(a\) 与 \(N\) 的支撑分离，代理范数精确为
\[
A_{-1}(v_1(t))=6e^{-t}+6\sqrt2\,te^{-2t},\qquad
A_0(v_1(t))=6e^{-t}+12te^{-2t}.
\tag{F.8}
\]
\(v_1(0)=a\)，所以其初始真实误差为零。

`ANALYTIC_PREFLIGHT.md` G.15 要求一个非负绝对连续控制上解 \(\rho\)，在整个 \([0,T]\) 上满足 \(\rho<1\) 及
\[
\rho'\ge\frac{F_0(t)^2\rho}{1-\rho}+R_{-1}(t),
\qquad
R_{-1}(t)\ge A_{-1}(\mathfrak r_1(t)),\quad \rho(0)\ge0.
\]
无论合法的 \(F_0,R_{-1}\) 上界取多保守，非负项及 F.7 都强迫
\[
\rho(T)\ge\int_0^T12t e^{-3t}\,dt
=\frac43\left[1-(1+3T)e^{-3T}\right]=:I(T).
\tag{F.9}
\]
另一方面，终点门 G.16 要求 \(A_{-1}(v_1(T))+\rho(T)<1\)。由 F.8 和非负性，必要条件仍为
\[
T>\log6.
\tag{F.10}
\]
对正 \(T\)，\(I'(T)=12Te^{-3T}>0\)。故 F.10 给
\[
I(T)>I(\log6)
=\frac43\left[1-\frac{1+3\log6}{216}\right].
\]
这里只需一个精确的粗有理比较：
\[
e^2>1+2+\frac{2^2}{2!}+\frac{2^3}{3!}
=\frac{19}{3}>6,
\]
所以 \(\log6<2\)，继而
\[
I(\log6)>\frac43\left(1-\frac7{216}\right)
=\frac{209}{162}>1.
\tag{F.11}
\]
F.9–11 与 \(\rho(T)<1\) 矛盾。因此不存在使用本代理同时通过 G.15 和 G.16 的控制上解。这个结论没有数值积分控制 ODE，只对已经确定的残差下界取精确原函数。

## 5. 结论范围

本次接受的是 `NO-CERTIFICATE-FOR-v1-WITH-G15-G16`：原第一响应代理与这组特定单调绝对预算不相容。相位、轴反馈、全部有序混合项、Leray 投影和黏性都已保留。

F.9 是控制上解必须承担的预算下界，不是 \(A_{-1}(u-v_1)\) 的下界。实际误差可能有本控制丢失的耗散或相消；别的后验不等式也可能有不同的收支。故不能由此排除原解全局光滑，不能宣称爆破，更不能排除所有近似轨道或所有后验方法。本记录不安排继续增加响应阶次。

## 6. 实读来源与字节绑定

本轮完整读 `first-cycle/ALGEBRA.md`，特别是 §1 的相位/有序核、§2 的投影及轴反馈、§3 的热半群第一响应；复读 `first-cycle/PROOF.md` §2 的完整非线性和 §5 的反序梯度说明。G.15–16 的实际控制合同来自已完成的 `ANALYTIC_PREFLIGHT.md`。以上有限代数在本文件独立手算，没有运行或修改旧程序。

| 文件（相对工作树根目录） | SHA-256 |
| --- | --- |
| `research/reverse/first-cycle/ALGEBRA.md` | `8098e84113b10c5ce37320de15e94f33a29e8207b980fb6d62483176c3fd6dc0` |
| `research/reverse/first-cycle/PROOF.md` | `a87672a035f1c80a0225ce8956fca53ffc2eb07fdd4e83092505b4ac657f6120` |
| `research/reverse/first-cycle/CONTRACT.md` | `6311d166a3bba64faa3f7d1afe042535702014f0e7b2dfffa6952acb7eb68cf8` |
| `research/reverse/fixed-seed-global-screen/ANALYTIC_PREFLIGHT.md` | `52793f58abf5eada0b2002b4abbf9a50dc08d52012d706b4753203c9dabde6cd` |
| `research/reverse/fixed-seed-global-screen/CONTRACT.md` | `5ed4bdb7c458a720f48ee9e3ec3206153280df8101e23b3852bb13097c334f9e` |
