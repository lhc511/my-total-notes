from select import select
from socket import *

# 创建监听的套接字作为关注的io
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 设置关注列表
rlist = [s]  # s用于等待处理链接
wlist = []
xlist = []
# 循环监控IO
while True:
    # 这里会进行阻塞直到select函数返回了对应的值
    # 当有客户端连接 s 准备就绪返回s
    # 当有客户端发消息 c 准备就绪 返回c
    # 有了返回值之后停止阻塞

    rs, ws, xs = select(rlist, wlist, xlist)  # 返回准备就绪的io 客户端连接后发消息只返回i客户端的地址和接口
    # print(1, rs) #第一次请求连接 服务端，第二次发消息 客户端

    # 遍历 返回值 列表(里面可以有多个对象)，处理就绪的IO
    for r in rs:
        if r is s:
            c, addr = r.accept()  # 由于此时只有一个io 即s套接字，所以必定可以用accept阻塞
            # print("connect from", addr)
            rlist.append(c)  # 将相应的客户端追加到rlist中
            print(2, rlist)  # 两个，客户端，服务端都有
            print(3, rs)  # 服务端
        # 给客户端发消息
        else:
            # 不用循环就可以重复发送消息，
            # 套用外面的大循环，当遍历到对应的客户端时给该客户端收发消息

            data = r.recv(1024).decode()  # *等待* 客户端发来消息的时候 客户端连接套接字 准备就绪 客户端未发消息时可以类似看作
            # 一个阻塞，当客户端输入消息按下enter后，进入函数，客户端c准备就绪，监管select 返回c给rs

            if not data:  # 当客户端退出的时候会发空
                rlist.remove(r)  # 取消对客户端的关注
                r.close()
                continue
            # print(data)
            # r.send(b'ok')
            wlist.append(r)  # 客户端具备收发消息的能力，而发消息是主动处理事件，所以可以给 写列表 添加
            # print(ws)
    for w in ws:
        w.send(b"ok")
        """
        当一个文件描述符已经完成写入操作后，如果不将其从 wlist 中移除，那么下一次调用 select 时，这个文件描述符仍然会被认为是可以写入的，
        从而再次进入 wlist 返回的结果中2。这可能导致程序反复尝试对该文件描述符执行写操作，即使实际上并没有新的数据需要写入
        """
        wlist.remove(w)  # 移除对象
    for x in xs:
        pass
