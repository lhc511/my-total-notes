import os
from socket import *
from threading import Thread
import sys
from time import sleep

HOST = "0.0.0.0"
PORT = 8080
ADDR = (HOST, PORT)
FTP = "/home/ubuntu/PycharmProjects/PythonProject/并发通讯网络/sever_file/"  # 文件库位置 最后一个斜杠是为了方便拼接


class FTPSever(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd

    def do_list(self):
        # 该函数用于获取文件列表
        files = os.listdir(FTP)  # 列出文件列表
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'ok\n')  # 由于ok后面发送文件列表，为了防止粘包，所以sleep
            sleep(0.1)
        # 拼接文件
        filelist = ""
        for file in files:  # file 每一个文件名
            # linux下文件第一个字符为 "." 默认为隐藏文件
            # isfile 判断文件是否为普通文件，若是返回True 即不是文件夹
            if file[0] != '.' and os.path.isfile(FTP + file):  # FTP + file:拼接 文件路径+文件名
                filelist = file + "\n"  # 用 ”\n“ 来拼接，作为分割符
                self.connfd.send(filelist.encode())

    def send_file(self):
        name = self.connfd.recv(4096).decode()  # 用户请求接收的文件名称
        files = os.listdir(FTP)  # 获取文件夹下文件名称列表
        for file in files:
            if name == file:
                target_name = FTP + name  # 文件下载位置绝对路径
                self.connfd.send(target_name.encode())  # 发送的是文件绝对路径的二进制
        else:
            self.connfd.send("不存在".encode())

    # 循环接受请求，看情况调用函数
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if data == 'L':
                self.do_list()
            if data == 'G':
                self.send_file()


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)

    print("Listen the port 8080...")
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
        client = FTPSever(c)
        client.Daemon = True  # 主线程退出时所有子线程都退出
        client.start()


if __name__ == "__main__":
    main()
