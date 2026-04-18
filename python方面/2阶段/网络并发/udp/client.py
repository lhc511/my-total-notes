"""两种不同的写法"""
# import socket
# s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
from socket import *
# s= socket(AF_INET,SOCK_DGRAM)

#服务器地址
ADDR=('127.0.0.1',8888) 
 #创建套接字
s= socket(AF_INET,SOCK_DGRAM)
#循环收发消息
while True: 
    data = input ("Msg>>")#在启动服务端前客户端向他发送消息会丢失
    if not data:
        break
    s.sendto(data.encode(),ADDR)
    msg,addr = s.recvfrom (1024)
    print("From server:", msg.decode())
s.close()