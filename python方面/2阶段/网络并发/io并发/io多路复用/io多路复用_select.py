"""
总结，**在同一个线程** 当有一个函数阻塞时 会自动寻找并执行不阻塞的函数

rs, ws, xs=select(rlist, wlist, xlist[,timeout])
功能.txt:监控I0事件，阻塞等待IO发生
参数:rlist 列表存放关注的等待发生的IO事件  例如：s.accept()
wlist 列表存放关注的要主动处理的IO事件   例如：f = open("log.txt", "r+")  此处f具有写入的功能，并且可以随时主动执行
xlist 列表存放关注的出现异常要处理的I0
timeout 超时时间

返回值:
rs列表rlist中准备就绪的IO  此处指已经停止阻塞进入函数内部开始执行 例：input("") 在输入内容后按下 enter 执行函数 方为准备就绪
WS列表wlist中准备就绪的IO
xS列表xlist中准备就绪的IO
"""

from select import select
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

f = open("../log.txt", "r+")

print("监控IO")
rs, ws, xs = select([s], [f], [])  # 其中有任意一个io就绪就会返回
print("rlist:", rs)  # 被动操作 例如服务器里面的等待客户端连接和发送消息 当链接上后立刻返回
print("wlist:", ws)  # 主动操作 例如写入文件
print("xlist:", xs)  # 异常
