from threading import Thread
from socket import *
import sys


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

print("Listen the port 8888...")
# 循环等待客户端链接
while True:
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        sys.exit("退出服务器")
    except Exception as e:
        print(e)
        continue

    # 创建线程处理请求
    t = Thread(target=handle, args=(c,))  # 创建一个线程，在处理客户端请求的同时 返回上面继续接收客户大u端连接
    t.Daemon = True#主线程退出时所有子线程都退出
    t.start()
