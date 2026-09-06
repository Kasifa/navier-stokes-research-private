# 双尺度误差界与归一化第二类 Chebyshev 验证

日期：2026-09-06。状态：**PROVED；解析证明和独立自动化交叉审计已完成**。完整英文证明见 [quantitative-edge.tex](../sections/quantitative-edge.tex)，独立审计见 [quantitative-cross-audit.md](../audits/quantitative-cross-audit.md)。自动化交叉审计不是真人同行评审。

本文件与英文稿记录同一结果。没有把有限计算当作证明，没有主张最优误差阶，也没有主张经典 Gaussian/Laplace 方法为新方法。

## 结果

固定 $0<s_0\le s_1<\infty$、$C_0\ge0$。取 $p_n=T_n$ 或 $p_n=U_{n-1}/n$，定义

$$
Q^p_{n,A}(s,c)=(e^{sA^{-2}D^2}p_n)(1+c/A),\qquad
\mu=(n^2/A)^{1/3},\qquad \epsilon=\mu/A.
$$

存在仅由 $s_0,s_1,C_0$ 计算的 $C,\mu_*,\epsilon_*>0$，使 $\mu\ge\mu_*$、$0<\epsilon\le\epsilon_*$ 时，$Q^p(s,c)>0$，并且

$$
\left|\mu^{-2}\log Q^p(s,0)-3\,2^{-4/3}s^{1/3}\right|
\le C\left(\epsilon+\frac{\log(2+\mu)}{\mu^2}\right),
$$

$$
\left|\mu^{-1}\log\frac{Q^p(s,c_2)}{Q^p(s,c_1)}
-2^{-2/3}s^{-1/3}(c_2-c_1)\right|
\le C|c_2-c_1|\left(\sqrt{\epsilon}
+\frac{\sqrt{\log(2+\mu)}}{\mu}\right).
$$

两式对 $s\in[s_0,s_1]$、$|c_i|\le C_0$ 一致。没有在原范围 $A\to\infty$、$\mu\to\infty$、$\mu/A\to0$ 外增加条件。尤其不要求 $\log A=o(\mu^2)$，也不要求 $\mu\epsilon\to0$。

## 可复用轮廓条件

设 $\psi(z)=\sqrt{2z}$、$z_-=2^{1/3}s_0^{2/3}$、$z_+=2^{1/3}s_1^{2/3}$、$Z=z_++1$、$J=[z_-,Z]$。对于实可测轮廓 $p=p_{\mu,A}$，要求存在固定 $k>0,b,d\ge0$，使下列条件在 $\mu\ge\mu_0\ge1$、$0<\epsilon\le\epsilon_0\le1$ 成立：

1. $|p(x)|\le1$ 于 $|x|\le1$。
2. 所有 $z\ge0$ 上，$0<p(1+\mu z/A)\le e^{\mu^2\psi(z)}$，且 $|p(-1-\mu z/A)|\le e^{\mu^2\psi(z)}$。
3. $z\in J$ 上，$p(1+\mu z/A)\ge k\mu^{-b}e^{\mu^2(\psi(z)-d\epsilon)}$。

对 Gaussian 卷积定义的 $Q^p$，同样结论成立。条件包括正外侧的正性、两端的全局包络、内部界和鞍点邻域的定量下界，不能仅凭点态边缘展开套用。它允许鞍点振幅带代数因子 $\mu^{-b}$。

## 常数和非循环阈值

以下全部量在选取 $\mu,A$ 之前确定。记 $\log_+x=\max(0,\log x)$，并令

$$
\begin{aligned}
F_*&=3\,2^{-4/3}s_0^{1/3},
&D_*&=(2z_-)^{-3/2}+(2s_0)^{-1},
&a_*&=(8s_1)^{-1},\\
H_*&=C_0^2s_1/(2s_0^2),
&L_*&=\frac{k}{\sqrt{4\pi s_1}}e^{-D_*/2-C_0/(2s_0)},
&V_*&=\sqrt{2s_1/s_0}e^{H_*},\\
K_*&=\frac{e^{H_*}}{\sqrt{4\pi s_0}L_*},
&H_{\rm tail}&=3\,2^{-4/3}(2s_1)^{1/3},
&E_0&=1+\sqrt{s_1/(2s_0)},\\
E_1&=\frac1{\sqrt{\pi s_0}}+
\frac{6\sqrt{s_1/e}\sqrt{2\pi s_1}+4s_1}
{2s_0\sqrt{4\pi s_0}},
&\kappa&=F_*/4.
\end{aligned}
$$

设

$$
r^2=\frac{d\epsilon}{a_*}
+\frac{(b+1)\log\mu+\log_+(K_*/a_*)}{a_*\mu^2},
\qquad \rho=r+\mu^{-2},
$$

$$
\rho_*=\sqrt{\frac{d+b+1+\log_+(K_*/a_*)}{a_*}}+1,
\qquad M_*=(z_++\rho_*+C_0)/(2s_0),
\qquad E_2=2(E_1+E_0M_*).
$$

选取

$$
\epsilon_*=\min\{\epsilon_0,(8s_1H_{\rm tail})^{-1/2},F_*/(4d)\},
$$

其中 $d=0$ 时删除最后一项，以及

$$
\mu_*=\max\left\{2,C_0,\mu_0,
\frac{2C_0z_+}{s_0F_*},\frac{8b}{F_*},
\sqrt{\frac{8(\log_+(1/L_*)+C_0^2/(4s_0))}{F_*}},
\sqrt{\frac{\log(2E_0)}{\kappa}}\right\}.
$$

更精确且可直接代入的误差为

$$
E_{\rm amp}=d\epsilon+
\frac{b\log\mu+\max(\log_+(1/L_*),\log_+V_*)
+2E_0e^{-\kappa\mu^2}}{\mu^2},
$$

$$
E_{\rm tilt}=|c_2-c_1|\left\{
\frac{\rho+C_0/\mu}{2s_0}+E_2e^{-\kappa\mu^2}\right\}.
$$

这些显式常数较保守；误差阶也未声称最佳。

## 完整证明

Gaussian 卷积与多项式的有限热展开由逐单项式取 Gaussian 矩相等：

$$
Q^p(s,c)=\frac1{\sqrt{4\pi s}}\int_{\mathbb R}
p(1+y/A)e^{-(y-c)^2/(4s)}\,dy.
$$

保留 $y\ge0$ 的正积分 $I(s,c)$，设 $y=\mu z$、$z_s=2^{1/3}s^{2/3}$、$\Phi_s(z)=\sqrt{2z}-z^2/(4s)$、$F_s=\Phi_s(z_s)$。有

$$
\Phi_s''(z)=-(2z)^{-3/2}-(2s)^{-1}\le-(2s_1)^{-1},
\qquad
\Phi_s(z)\le F_s-(z-z_s)^2/(4s_1).
$$

后式在零点由连续延伸成立。在区间 $[z_s,z_s+1/\mu]\subset J$ 上，二阶导数绝对值不超过 $D_*$，线性倾斜的变化不超过 $C_0/(2s_0)$。写

$$
\mathcal B=\mu^2F_s+c\mu z_s/(2s)-c^2/(4s).
$$

局部下界积分给出

$$
I(s,c)\ge L_*\mu^{-b}e^{\mathcal B-d\mu^2\epsilon}.
$$

另一方面，由

$$
c\mu(z-z_s)/(2s)\le\mu^2(z-z_s)^2/(8s_1)+H_*
$$

及全局包络，把 Gaussian 上界积分扩展至全实轴，得到

$$
I(s,c)\le V_*e^{\mathcal B}.
$$

每个 $c$ 下分别归一化正积分，得到 $Z=y/\mu$ 的密度界

$$
f_{s,c}(z)\le K_*\mu^{b+1}e^{d\mu^2\epsilon}
e^{-a_*\mu^2(z-z_s)^2},\qquad z\ge0.
$$

分割 $|Z-z_s|\le r$ 与补集，Gaussian 尾部的一阶矩显式为

$$
\int_{|w|>r}|w|e^{-a_*\mu^2w^2}\,dw
=(a_*\mu^2)^{-1}e^{-a_*\mu^2r^2}.
$$

因此

$$
\mathbb E_{s,c}|Z-z_s|
\le r+(K_*/a_*)\mu^{b-1}e^{d\mu^2\epsilon-a_*\mu^2r^2}
\le r+\mu^{-2}=\rho.
$$

所选 $r$ 精确保证最后一步。对 Gaussian 核求导，设 $G_s=z_s/(2s)=2^{-2/3}s^{-1/3}$，得到

$$
\partial_c\log I=(\mu\mathbb E_{s,c}Z-c)/(2s),
\qquad
\left|\mu^{-1}\partial_c\log I-G_s\right|
\le(\rho+C_0/\mu)/(2s_0).
$$

这一处是比值证明的关键：直接控制每一个有界位移下的加权均值，不相除两个粗振幅渐近，且正负 $c$ 均适用。全局包络保证求导与积分交换。

恢复有符号余项 $\mathcal R=Q^p-I$。内部 $-2A\le y\le0$ 的绝对值不超过 $1$，导数绝对值不超过 $(\pi s_0)^{-1/2}$。负外部令 $y=-2A-u$、$u\ge0$。阈值给出 $A\ge C_0$，故

$$
\mu^2\psi(u/\mu)-(2A+u+c)^2/(4s)
\le-A^2/(4s_1)+H_{\rm tail}\mu^2-u^2/(8s_1)
\le-A^2/(8s_1)-u^2/(8s_1).
$$

第一步用了 $(A+u)^2\ge A^2+u^2$，以及

$$
\max_{z\ge0}(\sqrt{2z}-z^2/(8s_1))=H_{\rm tail}.
$$

第二步正是 $\epsilon\le(8s_1H_{\rm tail})^{-1/2}$。由 Gaussian 积分得 $|\mathcal R|\le E_0$。求导多出 $|2A+u+c|/(2s)\le(3A+u)/(2s_0)$。再用

$$
\int_0^\infty e^{-u^2/(8s_1)}du=\sqrt{2\pi s_1},
\qquad
\int_0^\infty ue^{-u^2/(8s_1)}du=4s_1,
\qquad
\sup_{A\ge0}Ae^{-A^2/(8s_1)}=2\sqrt{s_1/e},
$$

得到 $|\partial_c\mathcal R|\le E_1$。没有假设内部或负外部的符号。

阈值逐项保证：$d\epsilon\le F_*/4$；$|c|\mu z_s/(2s)\le F_*\mu^2/4$；$b\log\mu\le F_*\mu^2/8$；$\log_+(1/L_*)+C_0^2/(4s_0)\le F_*\mu^2/8$。所以

$$
I(s,c)\ge e^{\kappa\mu^2},
\qquad
|\mathcal R/I|\le E_0e^{-\kappa\mu^2}\le1/2.
$$

于是 $Q^p>0$，且 $|\log Q^p-\log I|\le2E_0e^{-\kappa\mu^2}$。由 $\epsilon\le1$、$\log\mu\le\mu^2$，有 $\rho\le\rho_*$ 及 $|\partial_c\log I|\le\mu M_*$。故

$$
\mu^{-1}|\partial_c\log Q^p-\partial_c\log I|
\le\mu^{-1}\frac{|\partial_c\mathcal R|
+|\mathcal R||\partial_c\log I|}{I-|\mathcal R|}
\le E_2e^{-\kappa\mu^2}.
$$

在 $c_1,c_2$ 间积分给出 $E_{\rm tilt}$，所以 $c_1=c_2$ 时误差界也精确为零。共同振幅则在 $c=0$ 使用 $I$ 的上下界与余项对数界，得到 $E_{\rm amp}$。利用 $e^{-\kappa\mu^2}\le(2e\kappa)^{-1/2}/\mu$，以及 $\log(2+\mu)\ge1$，即得开头的简化误差阶。证毕。

## 两家族逐项验证

令 $\theta=\operatorname{arcosh}(1+\epsilon z)$。直接积分导数给出所有 $u\ge0$ 上的三个初等不等式：

$$
\sqrt{2u}(1-u/12)\le\operatorname{arcosh}(1+u)\le\sqrt{2u},
\qquad
\operatorname{arcosh}(1+u)\ge\frac{\sqrt{2u}}{\sqrt{1+u/2}}.
$$

第一下界由 $(1+v)^{-1/2}\ge1-v/2$；第二下界由积分中递减因子的最小值。因 $n\sqrt{\epsilon}=\mu^2$，$z\in J$ 上有

$$
\mu^2(\psi(z)-d\epsilon)\le n\theta\le\mu^2\psi(z),
\qquad d=\sqrt2 Z^{3/2}/12.
$$

**第一类。** $T_n(\cosh\theta)=\cosh(n\theta)$ 立即给全局包络和局部下界，参数为 $k=1/2,b=0,\mu_0=1,\epsilon_0=1$。内部界与奇偶性给其余条件。

**第二类。** 有

$$
\frac{U_{n-1}(\cosh\theta)}n
=\frac1n\sum_{j=0}^{n-1}e^{(n-1-2j)\theta}
=\frac{\sinh(n\theta)}{n\sinh\theta}>0.
$$

有限和给上界 $e^{n\theta}$，对应的三角有限和给内部模不超过 $1$，端点由连续性成立。奇偶性给负外包络。分母有精确恒等式

$$
n\sinh\theta=\mu^2\sqrt{z(2+\epsilon z)}
\le\mu^2\sqrt{Z(2+Z)}.
$$

设 $h_*=\sqrt{2z_-}/\sqrt{1+Z/2}$、$\mu_0=\max(1,h_*^{-1/2})$，则 $n\theta\ge\mu^2h_*\ge1$。所以

$$
\frac{U_{n-1}(1+\epsilon z)}n
\ge\frac{1-e^{-2}}{2\sqrt{Z(2+Z)}}\mu^{-2}
e^{\mu^2(\psi(z)-d\epsilon)}.
$$

据此取 $b=2$、$k=(1-e^{-2})/(2\sqrt{Z(2+Z)})$、$\epsilon_0=1$。全部假设已核清。

## 归一化为何不可省略

未归一化 $U_{n-1}$ 的比值与归一化者相同，但共同振幅多出 $\mu^{-2}\log n$，原范围并不控制这一项。例如 $n_j=\lceil e^{j^3}\rceil$、$A_j=n_j^2/j^3$，则 $\mu_j=j$、$\epsilon_j=j^4/n_j^2\to0$，而 $\mu_j^{-2}\log n_j\sim j$。因此不归一化时，直接复制第一类的共同振幅极限是错误命题。归一化后只剩显式的局部前因子 $\mu^{-2}$ 和损失 $2\log\mu$。

## 文献与主张边界

- 热多项式、Chebyshev 操作表示、Laplace/Gaussian 倾斜及强凹集中思想均属已有工具；本文件不就其提出新颖性主张。
- 当前新增证明是上述联合范围内的明确统一误差及轮廓条件，并验证归一化第二类家族。最相邻终止超几何和热边缘原文的覆盖情况见专责文献核查 [novelty-update.md](../literature/novelty-update.md)。只给固定参数 $\,{}_0F_2$ 的指数渐近并不自动覆盖本定理。
- 没有证明任意 Jacobi 家族，未证明最佳误差阶，也未把第二类家族延伸成新的 NS 动态实现或普适动态上下界。
- 文件是完整解析推导；独立自动化交叉审计已完成，参见 [审计记录](../audits/quantitative-cross-audit.md)。任何脚本抽查只用于发现代数或实现错误，不能认证无穷参数定理，也不代替真人同行评审。
