"""
可以在子进程里面创建二级子进程来解决僵尸进程问题
在一级子进程已进入就立马结束，让在其内部创建的二级子进程变成孤儿进程
而孤儿进程会由系统自动分配父进程，由此解决僵尸进程
"""
import sys
from time import sleep
import os


def f1():
    for i in range(3):
        sleep(2)
        print("写代码")


def f2():
    for i in range(2):
        sleep(4)
        print("测代码")


pid = os.fork()
if pid < 0:
    print("创建失败")

elif pid == 0:
    pid01 = os.fork()  # 创建二级子进程
    if pid01 < 0:
        print("失败")
    elif pid01 == 0:
        print("第二进程创建成功")
        f2()
    else:
        sys.exit()
else:
    os.wait()  # 等待一级子进程退出
    f1()
    print("父进程")
