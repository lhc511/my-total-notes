"""
fork _server.py 基于fork的多进程并发
重点代码
1.创建监听套接字
2.等待接收客户端请求
3.客户端连接创建新的进程处理客户端请求4.
原进程继续等待其他客户端连接5.如果客户端退出，则销毁对应的进程
"""
from socket import *
import os
import signal

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print('listen the port 8888...')


# 具体处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


while True:
    # 循环处理客户端链接
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        os.exit(0)
    except Exception as e:
        print(e)
        continue

    """
        在子进程运行的同时父进程会继续执行，进入大循环再创建一个线程，从而继续接收客户端的连接
    """
    # 每有一个客户端连接就会创建一个子进程
    # 创建子进程处理客户端事物
    pid = os.fork()
    if pid == 0:
        s.close()  # 在子进程中只用客户端套接字，而其已经在客户端连接阻塞的时候创建，所以可以关掉服务端套接字
        handle(c)  # 处理具体事物
        # 由于大循环函数子进程退出后会返回上面，fork子进程会完全继承父代码，但会从fork后开始执行，所以在此处会循环到上面
        os.exit(0)  # 客户端退出后子进程销毁
    # 无论父进程还是fork出错都要回去继续处理连接
    else:
        c.close()  # 父进程不需要和客户端通信
