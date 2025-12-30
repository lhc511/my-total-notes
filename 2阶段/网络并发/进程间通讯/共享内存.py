# from multiprocessing import Process, Value
# import time
import random

"""
from multiprocessing import Value, Array
obj= Value(ctype, data)  ctype是什么类型 data中的内容必须与ctype保持一致
功能.txt:开辟共享内存
参数: ctype 表示共享内存空间类型"i' 'f' 'c'    分别为 整形 浮点型 字节型
data共享内存空间初始数据
返回值:共享内存对象
obj.value 对该属性的修改查看即对共享内存读写

obj=Array(ctype,data)
功能.txt:开辟共享内存空间
参数: ctype 表示共享内存数据类型
data 整数则表示开辟空间的大小，其他数据类型表示开辟空间
"""

# 创建共享内存
"""
共享内存在下一次赋值数据时会清空前一次数据
但是由于是通过地址来寻找，不改变内存结构，所以访问速度更快
"""
# money = Value('i', 5000) #(类型，初始数据)
#
#
# # 操作共享内存
# def man():
#     for i in range(30):
#         time.sleep(0.2)
#         money.value += random.randint(1, 1000)
#
#
# def girl():
#     for i in range(30):
#         time.sleep(0.15)
#         money.value -= random.randint(100, 800)
#
#
# p1 = Process(target=man)
# p2 = Process(target=girl)
# p1.start()
# p2.start()
# p1.join()
# p2.join()
# # 获取共享内存里面的数
# print(money.value)

"""
array.py
共享内存存放一组数据
"""
from multiprocessing import Process, Array

# 创建共享内存
# shm = Array('i', [1, 2, 3, 4])  # 数据类型(i,c,f) 数组/列表
# shm = Array('i', 5)  # 开辟了一块包含了五个整形元素的空间 并初始值赋值0 [0,0,0,0,0]
shm = Array('c', b'hello')  # 字节串 此时下方修改也只能改成其他字符并且也 加b


def fun():
    # array 创建共享内存对象可迭代
    for i in shm:
        print(i)
    # shm[1] = 1000  # 在子线程中修改，父进程中也会被修改 数目也要相同
    shm[0] = b'j'


p = Process(target=fun)
p.start()
p.join()
# 子进程结束，进入父进程
for i in shm:
    print(i)
# 只能打印字节串
print(shm.value)  # b'jello'
