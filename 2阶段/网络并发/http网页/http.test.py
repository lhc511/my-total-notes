from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 8000))
s.listen(3)
c, addr = s.accept()
print("Connect from", addr)
data = c.recv(4096)  # 接受http请求
print(data)
# c.send(b'ok')#只能被火狐这类比较温和的浏览器接受
#          版本信息  响应码 附加信息
response="""HTTP/1.1 200 ok
Content-Type:text/html

<h1>helo world<h1>
"""
c.send(response.encode())

c.close()
s.close()
