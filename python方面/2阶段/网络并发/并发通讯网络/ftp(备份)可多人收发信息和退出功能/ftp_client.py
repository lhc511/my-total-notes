"""
ftp文件服务，客户端
"""
import sys
from socket import *


# 服务器地址ADDR=(127.0.0.1',8080)
# 客户端文件处理类
class FTPClient:
    """
    客户端处理查看，上传，下载，退出
    """
    def __init__(self):
        pass
    def look_up(self):
        pass
    def post(self):
        pass
    def download(self):
        pass

    @staticmethod
    def quit(op,s):
        if op == "Q":
            s.send(b'Q')
            sys.exit()

    @staticmethod
    def view():
        print("L 请求文件列表")
        print("G 下在文件")
        print("P 上传文件")
        print("Q 退出")

    def fun_select(self,op,s):
        if op == "Q":
            self.quit(op,s)



def msg_interact(s):
    ftp=FTPClient()
    ftp.view()
    while True:
        try:
            op = input("请输入选项>>")
        except KeyboardInterrupt:
            s.send(b'Q')
            print("\nclient exit")
            break
        except Exception as e:
            s.send(b'Q')
            print(e)
            break
        if not op:
            s.send(b'Q')
            break
        # 接收服务器信息
        s.send(op.encode())
        back=s.recv(1024)
        print(back.decode())
        ftp.fun_select(op,s)


# 连接服务器
def main():
    ADDR = ('127.0.0.1', 8888)
    s = socket()
    s.connect(ADDR)

    msg_interact(s)  # 用户与服务器信息信息交互



if __name__ == "__main__":
    main()
