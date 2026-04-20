from select import poll, POLLIN, POLLERR
from socket import *


class HTTPSever():
    def __init__(self, host='0.0.0.0', port=8000, dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host, port)
        self.fdmap = {}
        self.p = poll()
        # 创建实例化对象的时候直接创建套接字
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)

    # 启动服务函数
    def sever_forever(self):
        self.sockfd.listen((3))
        print('connect from the port', self.port)
        self.p.register(self.sockfd, POLLIN | POLLERR)
        self.fdmap[self.sockfd.fileno()]=self.sockfd
        # 用io多路复用接收客户端请求
        while True:
            event = self.p.poll()
            for fd,event in event:
                if fd == self.sockfd.fileno():
                    c, addr = self.sockfd.accept()
                    print('connect from ', addr)
                    self.fdmap[c.fileno()] = c
                    self.p.register(c,POLLIN|POLLERR)
                else:
                    data = self.fdmap[fd].recv(1024)
                    if not data:
                        self.p.unregister(self.fdmap[fd])
                        self.fdmap[fd].close()
                        del self.fdmap[fd]
                        continue
                    self.fdmap[fd].send(b'ok')


if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 8000
    DIR = 'static'  # 网页存储位置
    httpd = HTTPSever(HOST, PORT, DIR)
    httpd.sever_forever()
