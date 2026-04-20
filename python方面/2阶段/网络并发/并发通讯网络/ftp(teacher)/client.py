import os
import sys
import time
from socket import *
from time import sleep

# 服务器地址
ADDR = ('127.0.0.1', 8080)
CFTP = "/home/ubuntu/PycharmProjects/PythonProject/并发通讯网络/client_file/"


# 客户端文件处理类
class FTPClient:
    def __init__(self, s):
        self.s = s

    def do_list(self):
        self.s.send(b'L')
        data = self.s.recv(128).decode()
        if data == 'ok':
            data = self.s.recv(8192)  # 接收文件列表中
            # sleep(0.1)
            print(data.decode())
        else:
            # 打印 为什么不能打印文件列表（不能接受原因）
            print(data)

    def do_quit(self):
        self.s.send(b"Q")  # 请求退出
        self.s.close()
        sys.exit()

    # 下载文件
    def do_get(self, filename):  # 要传输文件的名字
        self.s.send(('G ' + filename).encode())
        data = self.s.recv(128).decode()  # 接收是否有所求文件
        if data == "ok":
            f = open(CFTP + filename, 'ab')  # 给客户端文件夹写入普通文件
            while True:
                data = self.s.recv(1024)  # 接收服务端发来的消息(服务端文件的二进制内容)
                if data == b"##":  # 特殊标志表示传送文件完成
                    break
                f.write(data)  # 一边接收一边写入
            f.close()
        else:
            print(data)

    """ 上传文件(自己写的)"""
    # def do_post(self, filename):
    #
    #     try:
    #         f = open(CFTP + filename, "rb")  # 以只读的方式打开，不存在则报错
    #     except Exception:
    #         print("文件不存在")
    #         return
    #     # filelist=os.listdir()
    #     self.s.send(b"P")
    #     data = self.s.recv(128)
    #     if data == b"ok":  # 如果服务器里没有这个文件，就发来ok
    #         self.s.send(filename.encode())
    #         while True:
    #             data = f.read(1024)
    #             if not data:
    #                 self.s.send(b"##")
    #                 break
    #             self.s.send(data)  # 给服务器发文件内容
    #     elif data == b'repeat':
    #         print("文件已存在")
    #         return
    """老师的"""

    def do_post(self, filename):
        try:
            f = open(CFTP + filename, 'rb')
        except Exception:
            print("该文件不存在")
            return
        # 获取文件名 有可能是绝对路径 所以取最后一个
        filename = filename.split('/')[-1]  # 根据文件的路径按照斜杠分割
        # 发送请求
        self.s.send(('P ' + filename).encode())
        # 接收反馈
        data = self.s.recv(128).decode()
        if data == 'ok':
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.s.send(b'##')
                    break
                self.s.send(data)
            f.close()
        else:
            print(data)


def main():
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return
    ftp = FTPClient(s)
    while True:
        print("\n============命令选项============")
        print("******      list         *******")
        print("*****       get file   ******** ")
        print("*****       put file   ******** ")
        print("*****           quit   ******** ")
        print("================================")
        cmd = input("输入命令:")
        if cmd.strip() == "list":
            ftp.do_list()
        elif cmd.strip() == "quit":
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename = cmd.strip().split(" ")[-1]  # 去掉两边的空格后找最后一个数据，也就是文件名
            ftp.do_get(filename)
        elif cmd[:3] == "put":
            filename = cmd.strip().split(" ")[-1]  # 有可能传的是路径
            ftp.do_post(filename)
        else:
            print("请输入正确命令")


if __name__ == "__main__":
    main()
