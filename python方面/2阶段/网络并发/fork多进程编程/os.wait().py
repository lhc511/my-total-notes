"""
os.wait()用于父进程等待任意子进程终止，并获取其退出状态。
此函数会阻塞父进程执行，直到有一个子进程结束，返回包含子进程PID和退出状态码的元组
(pid,status)
"""
import os
# pid, status = os.wait()
import os
import sys
from time import sleep

# 创建子进程
child_pid = os.fork()

if child_pid == 0:  # 子进程
    sleep(3)
    print("子进程开始执行")
    sys.exit(42)    # 子进程退出，状态码42
else:               # 父进程
    print(f"父进程等待子进程 {child_pid}")
    pid, status = os.wait()
    exit_code = os.WEXITSTATUS(status)  # 解析状态码
    print(f"子进程 {pid} 已终止，退出码为 {exit_code}")