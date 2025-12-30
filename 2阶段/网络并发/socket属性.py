"""
【1】sockfd.type套接字类型
【2】sockfd.family套接字地址类型
【3】sockfd.getsockname()获取套接字绑定地址
【4】sockfd.fileno()获取套接字的文件描述符
【5】Sockfd.getpeername()获取连接套接字客户端地址
[61 sockfd.setsockopt(level, option, value)
功能.txt:设置套接字选项
参数:level选项类别SOL_SOCKET
option具体选项内容
"""
"""
件描述符是一个非负整数，由操作系统分配给进程中的每一个打开的 I/O 资源（如文件、管道、套接字等）。
一般在在
"""

from socket import *

# 创建套接字
s = socket(AF_INET, SOCK_STREAM)
# 端口断开之后可以立即重用 在绑定地址之前
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s.bind(('127.0.0.1', 8888))
s.listen(3)
c, addr = s.accept()

print("地址类型:", s.family)
print("套接字类型:", s.type)
print("绑定地址:", s.getsockname())
print("文件描述符:", s.fileno())  # I O 操作的描述 系统占用 0,1,2（标准输入，标准输出，标准出错）
print("连接端地址", c.getpeername())
