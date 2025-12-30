import sys
from socket import *
from time import sleep


# 服务器地址
ADDR = ('127.0.0.1', 8080)
CFTP = "/home/ubuntu/PycharmProjects/PythonProject/并发通讯网络/"


# 客户端文件处理类
class FTPClient:
    def __init__(self, s):
        self.s = s

    def get_file(self):
        self.s.send(b"G")
        filename = input("请输入文件名:")

        self.s.send(filename.encode())

        sever_file = self.s.recv(4096).decode()
        sever_dfile = open(sever_file, "rb")  # 读取服务器所请求文件的数据

        client_file = CFTP + filename
        client_dfile = open(client_file, 'ab')

        while True:
            data = sever_dfile.read(1024)
            if not data:
                print("接收完毕")
                break
            client_dfile.write(data)

    def do_list(self):
        self.s.send(b'L')
        data = self.s.recv(128).decode()
        sleep(0.1)
        if data == 'ok':
            data_list = self.s.recv(10240).decode()  # 接收文件列表中
            print(data_list)
        else:
            # 打印为什么不能打印文件列表（接受原因）
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
        if cmd.strip() == "get file":
            ftp.get_file()


if __name__ == "__main__":
    main()
