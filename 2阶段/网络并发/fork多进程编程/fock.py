import os
from time import sleep

"""

os.fork()会创建一个子进程，并且会在执行完后有一个标识，子进程会继承这个标识，即从os.fork()的下一句开始执行（子进程会继承父进程的代码）
父进程会得到子进程的pid号
而子进程会根据进程是否创建成功来返回相应的值
终端给进程分配的 值（pid) 默认大于零

"""

# #创建子进程
# pid = os.fork()
# if pid < 0:
#     print("Create process failed")
# #子进程执行部分
# elif pid == 0:
#     sleep(3)#两个进程会同时行进，不必一个一个执行，共用时4s
#     print("The new process")
# #父进程执行部分
# else:
#     sleep(4)
#     print("The old process")
# #都执行
# print("Fork test over")

""""""
# print("================================")
# a = 1  # 开辟一块空间来存储a 在父进程
#
# pid = os.fork()  # 子进程只拷贝fork以下的代码
# if pid < 0:sleep(4)

#     print("Create process failed")
# elif pid == 0:
#     """在应用层面来讲 可以理解成子进程复制父进程全部空间，实际为写实拷贝（不用深究）"""
#     print("a=", a)  # 1
#     print("The new process")
#     a = 10000  # 修改的是子进程开辟的空间里面的a
# else:
#     sleep(1)  # 用来分割父子进程的时间 sleep之后子进程已经执行完了
#     print("The old process")
#     print(a)  # 1
# print("Fork test over")
#
# print("a:", a)  ##打印两遍由于不再父子进程内部 所以两个进程都执行一遍
