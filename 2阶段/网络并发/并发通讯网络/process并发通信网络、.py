from multiprocessing import Process
from socket import *
import os
import signal


def handle(c):
    while True:
        data = c.recv(1024)  # 从客户端收到数据
        if not data:
            break
        c.send(b'ok')  # 向客户端发送数据
        return data


HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)#自动回收子进程
while True:
    try:
        c, addr = s.accept()
        print('connect from', addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    p = Process(target=handle, args=(c,))
    p.daemon = True  # 父进程结束所有进程终止
    p.start()
