from socket import *
import json
from settings import *
from select import select


class Application:
    def __init__(self):
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)
        self.sockfd.bind((frame_ip, frame_port))

    def start(self):
        self.sockfd.listen(5)
        print("start app listen %s" % frame_port)
        self.rlist.append(self.sockfd)
        # select循环监控
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd, addr = r.accept()
                    self.rlist.append(connfd)
                else:
                    self.handle(r)
                    self.rlist.remove(r)

    def handle(self, connfd):
        request = connfd.recv(1024).decode()
        request = json.loads(request)  # 把发来的字符串在变成字典  变回 {'method': 'GET', 'info': '/'}
        if request['method'] == 'GET':
            if request['info'][-5:] == '.html' or request['info'] == '/':  # 如果发来的是请求网页的请求
                response = self.get_html(request["info"])  # 传递的是请求的网页内容

            else:
                response = {"status": '200', 'data' : 'xx'}
        elif request["method"] == "post":
            # response = {"status": '200', 'data' : 'xx'}
            pass
        response = json.dumps(response)  # 把response变成字符串
        connfd.send(response.encode())
        connfd.close()

    def get_html(self, info):
        if info == '/':
            # 请求主页
            filename = STATIC_DIR + '/index.html'
        else:
            filename = STATIC_DIR + info  # 请求具体网页
        try:
            fd = open(filename)
        except Exception:
            # 网页不存在
            fd = open(STATIC_DIR + "/404.html")
            return {'status': '404', 'data': fd.read()}
        else:
            # 网页存在
            return {'status': '200', 'data': fd.read()}


app = Application()
app.start()
