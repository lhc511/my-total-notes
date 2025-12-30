from socket import *
from time import ctime, sleep

# 日志文件
f = open('log.txt', 'a+')
# tcp套接字
sockfd = socket()
sockfd.bind(('127.0.0.1', 8888))
sockfd.listen(3)
# 设置套接字是非阻塞
# 有些报异常，有些直接过
# 该对象调用的所有函数都是非阻塞
# sockfd.setblocking(False)  # [Errno 11] Resource temporarily unavailable
# while True:
#     print("Waiting for connect...")
#     # 客户端每隔三秒写一条日至
#     try:
#         connfd, addr = sockfd.accept()
#     except BlockingIOError as e:
#         sleep(3)
#         f.write("%s:%s\n" % (ctime(), e))
#         f.flush()
#     else:
#         print("Connect from", addr)
#         data = connfd.recv(1024).decode()  # connfd调用的函数依旧会阻塞，需要专门设置才有非阻塞
#         print(data)

"""设置超时检测"""
sockfd.settimeout(3)  # 调用函数最多等待3秒
while True:
    print("Waiting for connect...")
    # 客户端每隔三秒写一条日至
    try:
        connfd, addr = sockfd.accept()  # TimeoutError: timed out
    except (BlockingIOError, timeout) as e:  # 同时捕获多个异常要加括号
        sleep(3)
        f.write("%s:%s\n" % (ctime(), e))
        f.flush()
    else:
        print("Connect from", addr)
        data = connfd.recv(1024).decode()  # connfd调用的函数依旧会阻塞，需要专门设置才有非阻塞
        print(data)
