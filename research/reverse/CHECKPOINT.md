# Reverse research checkpoint

2026-09-08 当前完成项：同一 n1280、t=5/8 的完整参照残差已通过两套实际精确计算、完整对照和非作者终审。科学运行源10df40f9bbebbe3086f3a7d0bc1a1d5301fb4505，主/独立7.769/15.008秒；比较器源b9921bdd，359370张量标量、215622残差分量、35937V/S全部通过，10个负对照拒绝。Rawls终审PASS；根全文读并实际核30项终审绑定。原r0节点门通过；原r2*exp(5/4)>2.38018447116e-7，所以指定epsilon=2e-7统一包络严格失败。它只排除这一参照预算，不排除原NS解。读 fixed-seed-global-screen/FULL_NODAL_RESIDUAL_OUTCOME.md、FULL_NODAL_RESIDUAL_FINAL_REVIEW.md 与 full-nodal-agreement.json；两个科学核和完整比较器均不得重跑。

NODAL_VS_CONTROL_INTERFACE.md 已由根非作者审查PASS，7来源绑定与NC.4实际交叉乘法通过：旧粗界保证的较小充分窗口与节点需求不相容，但整个显式控制函数族未判定；没有选择第三个epsilon。用户持续授权有效，平台目标active且无token预算，不需常规确认。原固定初值仍 NO-CERTIFICATE-YET-FOR-FIXED-a。

下一已开工项：Pascal（driver_independent_certificate）正写 ONE_SEGMENT_RESIDUAL_INCREMENT_PREFLIGHT.md，仅限同一既存 I=[1280/2048,1281/2048]。目标为复用当前已验全部六个常数张量与完整节点Rhat0，分析三次时间中心C0/QP+g(theta)、g(0)=0的完整保守增量残差、全theta扰动及Bernstein接口；至多比较直接四维打包与增量打包两种算术布局，给先验位宽/档案/乘法数。尚无新代码、预算或科学执行。先读其最终稿，再安排独立审查；不重复派活，不重推已验C1/CR引理，不增加节点、参数或全窗扫描。

所有科学写入与Git只在本反向树。此前五个正式包均已一次PRIVATE_ARCHIVE交接，记录见HANDOFF_LOG.json，不重发或监控。本轮为同一参照的内部证书与条件障碍，不另拆正式发布包；全部PRIVATE_CORE。已闭合证书不重算，连续余项、原解误差及奇性仍OPEN。

Previous checkpoints are preserved verbatim in `checkpoint-history/20260908-before-full-nodal-close.md`. Its historical next-action text must not override this page or `.workflow/reverse-current.json`.
