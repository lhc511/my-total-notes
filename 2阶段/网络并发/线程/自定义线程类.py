import os
import time
from threading import Thread
from time import sleep

"""当在线程类当中  会自动运行类里的run函数"""


# 自定义线程类
class ThreadClass(Thread):
    # 重写父类init
    def __init__(self, *args, **kwargs):
        self.attr = args[0]
        super().__init__()  # 加载父类init

    # 假设需要很多步骤完成功能
    def f1(self):
        sleep(1)
        print("step 1")

    def f2(self):
        sleep(1)
        print("step 12")

    # 重写run
    def run(self):
        t1 = time.time()
        self.f1()
        self.f2()
        t2 = time.time()
        print("%f" % (t2 - t1))
while True:
    t = ThreadClass('abc')
    t2=ThreadClass('bba')
    t2.start()
    t.start()
    t.join()

    t3=time.time()
    t.f2()
    t.f1()
    t4=time.time()
    print("%f"%(t4-t3))