"""
threadl.py线程基础使用
步骤:基本同Process
1.封装线程函数Ln
2.创建线程对象0
3.启动线程7
4.回收线程
"""
# import threading
# from time import sleep
# import os
#
# a=1
# # 线程函数
# def music():
#     for i in range(3):
#         sleep(2)
#         print(os.getpid(), "播放:黄河大合唱")
#     global a
#     print("a=", a)
#     a = 1000  # 线程中公用一个a
#
#
# # 创建线程对象
# t = threading.Thread(target=music)
# t.start()  # 启动线程
#
# for i in range(4):
#     sleep(1)
#     print(os.getpid(), "播放:葫芦娃")
#
# t.join()  # 回收线程
# print('a:a',a)

"""线程函数参数传递"""
from threading import Thread
from time import sleep


# 含有参数的线程函数
def fun(sec, name):
    print("线程函数参数")
    sleep(sec)
    print("%s执行完毕" % name)

    # 创建多个线程


jobs = []
for i in range(5):
    t = Thread(target=fun, args=(2,),
               kwargs={'name': 'T%d' % i})
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()
