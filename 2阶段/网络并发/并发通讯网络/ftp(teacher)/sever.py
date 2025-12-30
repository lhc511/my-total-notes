import os
import time
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
        files = os.listdir(FTP)  # 里面的参数是文件夹的绝对路径
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'ok')  # 由于ok后面发送文件列表，为了防止粘包，所以sleep
            sleep(0.1)
        # 拼接文件
        filelist = ""
        for file in files:  # file 每一个文件名
            # linux下文件第一个字符为 "." 默认为隐藏文件
            # isfile 判断文件是否为普通文件，若是返回True
            if file[0] != '.' and os.path.isfile(FTP + file):  # FTP + file:拼接 文件路径+文件名
                filelist = filelist + (file + "\n")  # 用 ”\n“ 来拼接，作为分割符
        self.connfd.send(filelist.encode())

    def do_get(self, filename):
        try:
            f = open(FTP + filename, 'rb')
        except Exception:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b"ok")
            time.sleep(0.1)
        while True:
            data = f.read(1024)  # 绝对路径文件夹里读取的文件二进制内容
            if not data:
                time.sleep(0.1)  # 防止在文件读取完后与之前的内容粘包
                self.connfd.send(b"##")
                break
            self.connfd.send(data)  # 将读取的内容发送(二进制)

    """自己的"""
    # def do_put(self):
    #     filelist=os.listdir(FTP)
    #     self.connfd.send(b'ok')
    #     filename=self.connfd.recv(1024).decode()
    #     for item in filelist:
    #         if filename==item:
    #             self.connfd.send("repeat".encode())
    #             return
    #     f = open(FTP+filename, "wb")
    #     while True:
    #         data=self.connfd.recv(1024)#客户端发来的文件内容
    #         if data==b'##':
    #             return
    #         f.write(data)

    # 循环接受请求，看情况调用函数
    """老师的"""

    def do_put(self, filename):
        if os.path.exists(FTP + filename):
            print("文件存在".encode())
        else:
            self.connfd.send(b'ok')
        f = open(FTP + filename, 'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()

    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == None:  # 当用户用非常规退出时会返回空
                return  # 线程结束
            elif data == 'L':
                self.do_list()
            elif data[0] == "G":
                filename = data.split(" ")[-1]
                self.do_get(filename)
            # 自己写的
            # elif data=="P":
            #     self.do_put()
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)


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
