"""线程之间通过全局变量来通讯"""
"""
锁 是用于防止线程之间互相抢占资源导致混乱
"""
from time import sleep

# from threading import Event

# e = Event()  # 创建线程event对象
# # e.wait()#阻塞等待e被set
# # print(e.wait(2))  # 阻塞两秒后 返回False 程序结束
#
# e.set()  # 设置e，使wait结束阻塞
# print(e.wait(2))  # 有set不会阻塞并 返回True
# e.clear()  # 使e回到未被设置状态
# e.is_set()  # 查看当前e是否被设置
"""pratice"""
"""Event"""
# from threading import Thread, Event
#
# s = None  # 用于通信
# e = Event()  # 事件对象
#
#
# def yang():
#     print("杨子荣前来拜山头")
#     global s
#     s = "天王盖地虎"
#     e.set()  # 当需要的函数执行完后用来结束阻塞函数
#
#
# t = Thread(target=yang)
# t.start()
# print("说对口令就是自已人")
# e.wait()  # 阻塞等待需要的函数执行完
# if s == "天王盖地虎":
#     print("宝塔镇河妖")
#     print("确认过眼神，你是对的人")
# else:
#     print("hit")
# t.join()

"""lock
当上锁之后必须先将上锁的地方执行完才会执行别的，其他执行会阻塞
"""

# from threading import Thread, Lock
#
# lock = Lock()  # 定义锁
# a = b = 0
#
#
# def value():
#     while True:
#         lock.acquire()  # 上锁
#         if a != b:
#             # sleep(0.5)
#             print("a=%d,b=%d" % (a, b))
#         lock.release()  # 解锁
#
#
# t = Thread(target=value)  # 创建一个子线程
# t.start()  # 开始执行子线程
# while True:
#     with lock:  # 上锁
#         a += 1
#         b += 1
#         # with语句块结束后自动解锁
# t.join()

