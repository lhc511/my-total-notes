import json
from socket import *
import sys
from threading import Thread
from config import *
import re

ADDR = (HOST, PORT)


# 在调用函数时每调用一次相当于在子线程中创建了一个套接字，可以分开处理请求，达到提高效率
def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip, frame_port))
    except Exception as e:
        print(e)
        return
    else:
        # 将字典转化为json   字符串
        data = json.dumps(env)  # "{'method': 'GET', 'info': '/'}"
        # 发送   解析后的字典(字符串)   与类型 请求给webframe
        s.send(data.encode())
        # 接收webfram的数据
        data = s.recv(4090 * 100).decode()
        return json.loads(data)


# 封装基本功能为类
class HTTPSever:
    def __init__(self):
        self.address = ADDR
        self.create_socket()  # 和浏览器交互
        # self.connect_socket()  # 和webframe框架交互
        self.bind()

    # def connect_socket(self):
    #     self.connect_sockfd = socket()
    #     frame_addr = (frame_ip, frame_port)
    #     try:
    #         self.connect_sockfd.connect(frame_addr)
    #     except Exception as e:
    #         print(e)
    #         sys.exit()

    def create_socket(self):
        self.sockfd = socket()  # 由于self.sockfd套接字是全局变量，所以当连接webframe时只能一条一条去处理导致处理速度很慢
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    def bind(self):
        self.sockfd.bind(self.address)
        self.ip = self.address[0]
        self.port = self.address[1]

    # 启动服务
    def sever_forever(self):
        self.sockfd.listen(5)
        print("listen the port %d" % self.port)
        while True:
            connfd, addr = self.sockfd.accept()
            print("connect", addr)
            client = Thread(target=self.handle, args=(connfd,))
            client.daemon = True
            client.start()

    def handle(self, connfd):
        # 获取http请求
        request = connfd.recv(4096).decode()  # 这里是http请求协议个时当中的内容
        #            请求类型   请求内容
        # pattern = r'([A-Z]+)\s+(/\S*)'  # 1-多个个大写首字母 空字符 斜杠  0-多个非空字符
        #            ?P<method>  用来捕获组并起名
        pattern = r'(?P<method>[A-Z]+)\s+(?P<info>/\S*)'  # 1-多个个大写首字母 空字符 斜杠  0-多个非空字符
        try:
            # env=re.match(pattern,request)#用pattern匹配request中开始位置
            env = re.match(pattern, request).groupdict()  # 返回捕获组 组名 与 内容 组成的字典  组名:内容 {'method': 'GET', 'info': '/'}
        except:
            # 客户端断开
            return
        else:  # 当没有异常时执行代码   finally:无论是否发生异常都执行代码
            data = connect_frame(env)
            if data:
                self.response(connfd, data)  # 将请求的各式格式发送给frame框架

    def response(self, cnnfd, data):
        # data={'status':'200','data':"xxxxxxxxxxxxx"}
        if data['status'] == '200':
            responseHeaders = "HTTP/1.1 200 ok\r\n"
            responseHeaders += "Content-type:text/html\r\n"
            responseHeaders += '\r\n'
            responseBody = data['data']
        elif data['status'] == '404':
            responseHeaders = "HTTP/1.1 404 not found\r\n"
            responseHeaders += "Content-type:text/html\r\n"
            responseHeaders += '\r\n'
            responseBody = data['data']
            # 数据发送给浏览器
        response_data = responseHeaders + responseBody
        cnnfd.send(response_data.encode())


httpd = HTTPSever()
httpd.sever_forever()
