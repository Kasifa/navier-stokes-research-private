# 主输入准备的唯一实际运行

2026-09-09，PRIVATE_CORE。运行前源码提交 c37b516bf668a8b600b084dde91f94b7fe27ddb8；input-pre-run-binding.json 实核 16 件本项文件与 2 项原代数来源的 Git 对象，并确认两输出不存在。固定命令为 `/usr/bin/python3 research/reverse/annular-source-observation/run_input.py --source-commit c37b516bf668a8b600b084dde91f94b7fe27ddb8`。

实际只启动 1 个科学子进程，科学执行计数 1，正常退出 0，完整序列化已完成。监督器从 Popen 前至 wait 后记录墙时 0.041177708 秒，子进程峰值 RSS 16187392 bytes；分别低于预设 5 秒和 268435456 bytes。父进程资源另报，不将其峰值与子峰值相加冒充同时总峰值。执行环境为本机 arm64、Python 3.9.6、标准库 Fraction；未导入 NumPy、FFT 或 NS 求解器。

原输出 input-preparation.json 为 133961 字节，SHA-256 3f51705fbd934ce76d503c1c856566405ee3deb1760474b1c73ef6a6f481c61f；监督记录 input-execution.json 为 2935 字节，a1557535b1beec08f1a80e22444e811bff78a4dba91a5ea7adbfe267f3fed13b。两件原字节保持，不重跑或覆盖。

程序报告按合同完成 80 次二分，十二模重建最大受检整数绝对值为 94229494117058（小于 2^53），并保存五项区间、三种初值误差预算及固定有理 C/T/a。T 的显示近似为 0.00019666375651032945；严格值及其浮点转换误差以原 JSON 为准。这里是执行结果读取，尚未以独立算术核验接纳全部数值。

下一步仅对这些原字节作预定的不同组织核验；其代码尚须停稿、根全文读、非作者审查与运行前提交。主运行成功不证明真实 NS 延续到 T、连续来源门、有限两步机制或奇性。没有新图档或 PDF。
