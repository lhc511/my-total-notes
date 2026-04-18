from socket import *
from select import *


class HTTPSever():
    def __init__(self, host='0.0.0.0', port=8000, dir=None):
        self.host = host
        self.port = port
        self.dir = dir  # 网页存储位置
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.address = (host, port)
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

    def handle(self, connfd):
        request = connfd.recv(4096)
        print(request, '\n')
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        request_line = request.splitlines()[0]  # 将字节串按行切割，并取首元素获得请求行
        info = request_line.decode().split(' ')[1]  # 获取请求命令
        # print(request_line)  # GET /ilouf HTTP/1.1 :请求方法 /请求内容/ HTTP协议和版本
        # print(connfd.getpeername(), ':', info)  # getpeername():获取连接的客户端地址

        # 根据请求类型处理数据
        # 两类：1.网页 2.其他
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd, info)
        else:
            self.get_data(connfd, info)

    def get_html(self, connfd, info):
        if info == '/':
            # 请求主页
            filename = self.dir + '/index.html'
        else:
            filename = self.dir + info  # 请求具体网页
        try:
            fd = open(filename)
        except Exception:
            # 网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"  # 空行
            response += "<h1>Sorry......<h1>"
        else:
            # 网页存在
            response = "HTTP/1.1 200 ОК\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"  # 空行
            response += fd.read()
        finally:
            # 将响应发送给浏览器
            connfd.send(response.encode())

    def get_data(self, connfd, info):
        response = "HTTP/1.1 200 ОК\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"  # 空行
        response += "<h1>wait for http3<h1>"
        connfd.send(response.encode())

    # 启动服务函数(select方法)
    def sever_forever(self):
        self.sockfd.listen(3)
        # print('connect from the port', self.port)
        # 用io多路复用接收客户端请求
        self.rlist.append(self.sockfd)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for item in rs:
                if item is self.sockfd:
                    c, addr = self.sockfd.accept()
                    # print('connect from address', addr)
                    self.rlist.append(c)
                else:
                    #########方法2#########
                    self.handle(item)

                    ######方法一########
                    # 当客户端断开的时候 c 套接字也会发送请求(即发送空)，而服务端对请求的方式一般来说都是用水平触发(详见 io并发/水平触发)
                    # 所以会一直弹出消息
                    # data = item.recv(1024)
                    # print(data)
                    # if not data:
                    #     self.rlist.remove(item)
                    #     continue
                    # item.send(b'ok')


if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 8000
    DIR = 'static'  # 网页存储位置 后面不加 / 是因为一般请求自带斜杠
    httpd = HTTPSever(HOST, PORT, DIR)
    httpd.sever_forever()
