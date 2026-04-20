"""测试用例"""
import time
from multiprocessing import Process
from threading import Thread


# 用十个进程，十个线程，和本来的分别计算时间
# 计算
def count(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1


def time_p():
    t1 = time.time()
    for item in range(10):
        p = Process(target=count, args=(0, 0))
    t2 = time.time()
    return t2 - t1


def time_t():
    t1 = time.time()
    for item in range(10):
        t = Thread(target=count, args=(0, 0))
    t2 = time.time()
    return t2 - t1


def time_count():
    t1 = time.time()
    count(0, 0)
    t2 = time.time()
    return t2 - t1


print('sig:%f'%time_count())
print('process:%f' % time_p())
print('thread:%f' % time_t())

"""2"""
import time
from multiprocessing import Process
from threading import Thread

#
# def io():
#     write()
#     read()
#
#
# def write():
#     f = open('test', 'w')
#     for i in range(1800000):
#         f.write("Hello world\n")
#     f.close()
#
#
# def read():
#     f = open('test')
#     lines = f.readlines()
#     f.close()
#
#
# def io_time():
#     t1 = time.time()
#     io()
#     t2 = time.time()
#     return t2 - t1
#
#
# def time_t():
#     t1 = time.time()
#     t_array = []
#     for item in range(10):
#         t = Thread(target=io)
#         t_array.append(t)
#         t.start()
#     t2 = time.time()
#     # for item in t_array:
#     #     item.join()
#     # return t2 - t1
#
#
# def time_p():
#     t1 = time.time()
#     p_array = []
#     for item in range(10):
#         p = Process(target=io)
#         p_array.append(p)
#         p.start()
#     t2 = time.time()
#     for item in p_array:
#         item.join()
#     return t2 - t1


# print('time_t:%f' % time_t())
# print('time_p:%f' % time_p())
# print('io:%f' % io_time())
