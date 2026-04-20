"""
接收1.创建udp套接字
2.设置套接字可以发送接收广播(setsockopt)
3.选择接收的端口
4.接收广播


"""
from socket import *
s= socket (AF_INET, SOCK_DGRAM)

#设置套接字接收广播
s. setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.bind(('0.0.0.0',9999))
while True:
    msg,addr=s.recvfrom (1024)
    print (msg.decode())