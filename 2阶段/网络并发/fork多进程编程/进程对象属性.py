from multiprocessing import Process
import time

"""默认情况下子进程不会受父进程影响，父进程退出子进程依旧可以执行"""


def tm():
    for i in range(3):
        time.sleep(2)
        print(time.ctime())


p = Process(target=tm)
"""p.name"""
# print("Name:",p.name)#进程名秘  Name: Process-1（默认）
# p = Process(target=tm, name="lll")  # 名字可修改
# print("Name:", p.name)  # 进程名秘  Name: lll  (修改后)
"""p.pid"""
# print("pid:", p.pid)  # 对应子进程 PID  pid: None
# p.start()
# print("pid:", p.pid)  #只有在执行后才有pid 即p.start()  pid: 6378
"""is_alive:
判断这个程序是否有生命周期，是返回 True， 否：返回 False
"""
# print('is_alive', p.is_alive())  # is_alive False
# p.start()
# print('is_alive', p.is_alive())  # is_alive True
"""
daemon：  
p.daemon设置父子进程的退出关系
    ·如果设置为True则子进程会随父进程的退出而结束
    ·要求必须在start()前设置
    ·如果daemon设置成True通常就不会使用join()
"""
p.daemon=True
p.start()
print("pid:", p.pid)