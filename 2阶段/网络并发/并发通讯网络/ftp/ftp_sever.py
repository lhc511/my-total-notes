"""
ftp文件服务器，服务端
env:python3.6
多进程/线程并发Socket
"""
import sys
from socket import *
from multiprocessing import Process
import signal

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
FTP="/home/ubuntu/PycharmProjects/PythonProject/并发通讯网络/sever_file/"#文件库位置 最后一个斜杠是为了方便拼接

# 创建类实现服务器文件处理功能
class FTPServer:
    """
        查看列表，下载，上传，退出处理
    """
    @staticmethod
    def look_up():
        pass
    def post(self):
        pass
    def download(self):
        pass
    @staticmethod
    def quit():
        print('用户退出')
        sys.exit()


def fun_conduct(data):
    if data == "Q":
        FTPServer.quit()
    if data=="L":
        FTPServer.look_up()



def msg_interact(c):
    while True:
        data = c.recv(1024)
        if not data:
            sys.exit("用户退出")
        #接收客户端信息反馈
        c.send(b'be received')
        fun_conduct(data.decode())


# 搭建网络服务端模型:
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    s.listen(5)

    while True:
        try:
            c, addr = s.accept()
            print('connect from', addr)
        except KeyboardInterrupt:
            sys.exit("服务器退出")
        except Exception as e:
            print('意外错误')
            continue

        p = Process(target=msg_interact, args=(c,))  # 用户与服务器信息信息交互
        p.start()


if __name__ == "__main__":
    main()
