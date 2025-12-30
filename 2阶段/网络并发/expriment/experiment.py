# from anyio import sleep

"""文件读写"""

# file=open("test",'r')
# # f=open('/home/ubuntu/图片/萨塔尼亚.jpeg','wb')
# i=0
# while i<3:
#     # file.seek(0,0)
#     for line in file:
#         print(line)
#     i+=1
# while True:
#     data=file.read(10)
#     if not  data:
#         break
#     f.write(data.)
"""带有空格的完整信息接受"""
# str01="aocn aoc  iahwb aiciinc"
# data=str01.split(" ")
# print(data)
# text = ' '.join(data[2:])
# print(text)

from multiprocessing import Process
from time import sleep
import os

"""进程的创建与回收"""
# def th1():
#     sleep(2)
#     print("吃饭")
#     print(os.getppid(), '--', os.getpid())
#
#
# def th2():
#     sleep(3)
#     print("shuijiao")
#     print(os.getppid(), '--', os.getpid())
#
#
# def th3():
#     sleep(4)
#     print("河水")
#     print(os.getppid(), '--', os.getpid())
#
#
# things = [th1, th2, th3]
# jobs = []
# for th in things:
#     p = Process(target=th)
#     jobs.append(p)  # 将进程对象保存
#     p.start()
#     # 一起回收
# for i in jobs:
#     i.join()
"""文件列表的查看"""
# sf = "/home/ubuntu/PycharmProjects/PythonProject/并发通讯网络/sever_file/"  # 路径
#
# files = os.listdir(sf)
# for item in files:
#     print(item)
# print(type(files))  # <class 'list'>

# f=open("/home/ubuntu/PycharmProjects/PythonProject/并发通讯网络/sever_file/","rb")
""""""
# from  socket import socket
# from select import *
# s=socket()
# print(s)
""""""
# import pymysql
# db=pymysql.connect(host="localhost",port=3306,user="root",password="123",database="user",charset="utf8")
# name = input("name:")
# password=input("password:")
# sql="insert into user_dict "

class o:
    def __init__(self,a=None):
        self.a = a
    def add_mm(self):
        b = self.a + '/index.html'
        print(self.a)
        print(b)
o1=o()
o1.add_mm()