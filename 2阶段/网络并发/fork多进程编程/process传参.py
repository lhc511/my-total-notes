"""
Proces给进程函数传参
"""

"""
multiprocessing 中无法使用标准输入 就是input("")

"""
#
# from multiprocessing import Process
# from time import sleep
#
#
# # 带参数的进程函数
# def worker(sec, name):
#     for i in range(3):
#         sleep(sec)
#         print("I'm %s" % name)
#         print("I'm working..")
#

"""三种方法的等效"""
# p= Process(target=worker,args=(2,'n'))
# p = Process(target=worker,
#             kwargs={'sec': 2, 'name': 'n'})  # 传递的值
# p = Process(target=worker, args=(2,),
#             kwargs={'name': 'n'})

# p.start()
# p.join()
