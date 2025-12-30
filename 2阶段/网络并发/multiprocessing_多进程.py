"""
1.编写进程函数4
2.生产进程对象5
3.启动进程6
4.回收进程7
"""
import multiprocessing as mp
# from time import sleep
#
#
# def fun():
#     print("开始一个进程")
#     sleep(5)
#     print("子进程结1")
#
#
# # 创建进程对象
# p = mp.Process(target=fun)
# p.start()  # 启动进程 子进程
#
# # 父进程
# sleep(3)
# print("父进程")

# p.join()  # 回收进程  阻塞

"""
#创建进程对象,上面的与下面的等效果

pid=os.fork()
if pid==0:
    fun()
    os._exit()
else:
    os.wait()  父进程不会结束
"""

"""
multiprocessing 创建多个进程
"""

from multiprocessing import Process
from time import sleep
import os


def th1():
    sleep(2)
    print("吃饭")
    print(os.getppid(), '--', os.getpid())


def th2():
    sleep(3)
    print("shuijiao")
    print(os.getppid(), '--', os.getpid())


def th3():
    sleep(4)
    print("河水")
    print(os.getppid(), '--', os.getpid())


things = [th1, th2, th3]
jobs = []
for th in things:
    p = Process(target=th)
    jobs.append(p)  # 将进程对象保存
    p.start()
    # 一起回收
for i in jobs:
    i.join()
