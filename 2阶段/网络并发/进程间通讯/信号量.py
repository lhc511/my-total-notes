"""
from multiprocessing import Semaphore
sem Semaphore (num) num信号量初始数量
功能.txt: 创建信号量对像
参数:信号量的初始值
返回值:信号量对象

sem.acquire()将信号量减1 任务执行要消耗信号量 止当信号量为0时阻塞
sem.release() 将信号量加1 任务执行完毕后释放一个信号量
sem.get_value()获取信号量数量
"""

"""
sem.py 信号量演示   用于限制任务进行的数量 
思路:信号量数量相当与资源，执行任务必须消耗资源
"""
from multiprocessing import Process, Semaphore
from time import sleep
import os

# 创建信号量(最多允许3个任务同时执行)
sem = Semaphore(3)


# 任务函数
def handle():
    sem.acquire()  # 想执行必须消耗一个信号量
    print("%s执行任务" % os.getpid())

    sleep(2)
    print("%s执行任务完毕" % os.getpid())
    sem.release()  # 归还信号量


# 10个任务需要执行  三个三个一起执行
for i in range(10):
    p = Process(target=handle)
    p.start()
    p.join()
