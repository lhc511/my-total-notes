"""
httpserver v1.0
基本要求:1.获取来自浏览器的请求
2.判断如果请求内容是 / 将index.html返回给客户
3.如果请求的是其他内容则返回404

"""
# 请求行： get / HTTP/1.1
#         请求头 key:value\r\n 每一个键值对占一行
#               ...
#          空行
#           请求体
from socket import *


# 客户端(浏览器)处理
def request(connfd):
    # 获取请求将请求内容提取出来
    data = connfd.recv(4096)  # 接受客户发的消息
    # 防止浏览器异常退出
    if not data:
        return
    # print(data.decode())
    # 判断是/则返回index.html不是则返回404
    request_line = data.decode().split('\n')[0]
    info = request_line.split(' ')[1]
    if info == '/':
        # \r:使光标回到行首 \n，光标移动到下一行
        with open('static/index.html') as f:
            response = "HTTP/1.1 200 ОК\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"  # 空行
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"  # 空行
        response += "<h1>Sorry......<h1>"

    connfd.send(response.encode())  # 服务器将用户所请求的数据发送到用户


# 搭建tCp网络
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('0.0.0.0', 8000))
sockfd.listen(3)
while True:
    connfd, addr = sockfd.accept()
    request(connfd)  # 处理客户端请求
