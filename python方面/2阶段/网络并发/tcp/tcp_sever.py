"""
作为服务器去被连接

tcp_server.py tcp套接字服务端流程重点代码
注意:功能性代码，注重流程和函数使用
"""
"""tcp中收发消息以创建的客户端套接字为主"""
import socket

"""
套接字是网络编程中的一种通信机制，用于支持 TCP/IP 的网络通信。
它是应用层与传输层之间的接口，允许不同主机之间的进程进行双向通信。
简单来说，套接字是通信双方的一种约定，通过套接字中的相关函数来完成通信过程
"""

"""1"""
# 创建tcp套接字
#                        ipv4              tcp协议
# 用套接字创建一个接口 并赋值给sockfd
# sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 可以直接写 socket.socket() 里面的参数默认就是(前面括号里面的)
#
# # 给sockfd绑定地址
# sockfd.bind(('0.0.0.0', 8888))  # 0.0.0.0会自动寻找合适的ip
#
# # 监听
# sockfd.listen(5)
# # 阻塞等待处理连接
# print("Waiting for connect...")
#
# # 接受一个客户端连接请求 并返回一个新的套接字（该客户端专有的套接字）
# connfd, addr = sockfd.accept()  # 阻塞等待接受信息   connfd:客户端连接套接字
# print("Connect from", addr)  # 打印链接的客户端地址
# while True:
#     # 收发消息
#     data = connfd.recv(1024)
#     print("收到:", data.decode())
#     if not data.decode() == "quit":
#         n = connfd.send(b'Thanks quite successfully')  # 发送字节串
#         break
#     n = connfd.send(b' ')

"""2"""
while True:
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 可以直接写 socket.socket() 里面的参数默认就是(前面括号里面的)

    # 给sockfd绑定地址
    sockfd.bind(('0.0.0.0', 8888))  # 0.0.0.0会自动寻找合适的ip

    # 监听
    sockfd.listen(5)
    # 阻塞等待处理连接
    print("Waiting for connect...")
    try:
        # 接受一个客户端连接请求 并返回一个新的套接字（该客户端专有的套接字）
        connfd, addr = sockfd.accept()  # 阻塞等待接受信息   connfd:客户端连接套接字
        print("Connect from", addr)  # 打印链接的客户端地址
    except KeyboardInterrupt:
        print('sever exit')
        break
    except Exception as e:
        print(e)
        continue

    while True:
        # 收发消息
        data = connfd.recv(5)
        if not data:  # 在客户端那边先断开后 会默认受到一个 空字符串
            break
        print("收到:", data.decode())
        n = connfd.send(b'thanks')
    # 关闭
    connfd.close()
sockfd.close()
