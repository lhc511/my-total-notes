"""
作为客户端去连接服务器
服务端ip不变化，因此只要客户端去连接就好
"""
from socket import *

"""1"""
# # 创建tcp口套接字
# sockfd = socket()  # 使用默认参数一>tcp套接字
# # 连接服务器
# server_addr = ('127.0.0.1', 8888)  # 表明服务器地址
# # 服务端地址 通过sockfd 接口去连接服务器
# sockfd.connect(server_addr)
# while True:
#     data = input("Msg>>")
#     if data == 'quit':
#         sockfd.send(data.encode())  # send发送字节串，所以要把字符串变成字节串
#         break
#     data = sockfd.recv(1024)
#     print("sever", data.decode())

"""2"""
# 创建tcp口套接字
sockfd = socket()  # 使用默认参数一>tcp套接字
# 连接服务器
server_addr = ('127.0.0.1', 8888)  # 表明服务器地址
# 服务端地址 通过sockfd 接口去连接服务器
sockfd.connect(server_addr)
while True:
    data = input("Msg>>")
    if not data :
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("sever", data.decode())
sockfd.close()
