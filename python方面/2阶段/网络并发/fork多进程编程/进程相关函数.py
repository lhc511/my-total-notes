import os, sys
from time import sleep

"""获取pid"""
# pid = os.fork()
# if pid < 0:
#     print("Error")
# elif pid == 0:
#     print("Child PID:", os.getpid())  # 子PID
#     print("Get parent P:", os.getppid())  # 父PID
# else:
#     print("Get child PID:", pid)  # 子PID
#     print("Parent PID:", os.getpid())  # 父PID

"""
exit：父子进程的退出不会影响另一个
"""

# 退出进程#不用管黄色波浪线
# os._exit(0)
# sys.exit("退出")  # 退出 打印括号内字符串
# print("acascasa")

"""
孤儿进程:父进程已经执行完了，子进程还在执行，此时系统会个u这个子进程再分配一个父进程 、
要在终端运行
"""
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    sleep(1)
    print("Child PID:", os.getpid())  # 子PID
    print("Get parent P:", os.getppid())  # 父PID
else:
    print("Get child PID:", pid)  # 子PID
    print("Parent PID:", os.getpid())  # 父PID
