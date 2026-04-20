"""
select方法只能同时监控1024个，太少了，而 poll 可以同时监控上万个对象

poll方法：在将监控的对象给操作系统的时候是拷贝进去的，当操作系统检测到其中被关注的io事件触发时
会将整体全部返回，再从poll中逐个遍历，直到找出被触发的对象

epoll：在继承poll优点的同时，不再应用层面添加，而是直接给操作系统，在检测到触发的io操作时直接将其返回，
相比poll方法省区很多步骤，效率更高
"""
"""注解在poll方法"""
from select import *
from socket import *
from time import sleep

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)
# 创建epoll对象
ep = epoll()  # epoll()包含在select函数内部，所以可以直接调用

fdmap = {s.fileno(): s}  # 通过这个io的文件描述符来找到其本身

# 关注s
ep.register(s, EPOLLIN)  # 在读io事件中关注(被动接收的操作 例如accept():等待连接，recv()：等待接收消息)

# 循环监控io发生
while True:
    events = ep.poll()  # 阻塞等待 s(被动接收) 发生
    for fd, event in events:
        # 区分哪个io发生
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("connect from...", addr)
            #水平触发
            ep.register(c, EPOLLIN | EPOLLERR)  # 再关注c

            #边缘触发,（在没有处理方法时）只有在有io操作的处理请求时才触发，例如客户端发送一次连接服务器请求触发一次
            ep.register(c, EPOLLIN | EPOLLET)  # 再关注c

            # ep.register(c, EPOLLIN | EPOLLERR)  # epoll不允许注册两个io对象回，会报错 但是poll可以，只是后一个会覆盖前一个
            fdmap[c.fileno()] = c  # 将关注的对象c添加到字典里面

        elif event & EPOLLIN:  # 只在读操作时才进入函数
            data = fdmap[fd].recv(1024)
            if not data:
                ep.unregister(fd)  # 取消关注
                fdmap[fd].close()  # 关闭关注的对象,即客户端套接字
                del fdmap[fd]  # 从字典删除
                continue
            print(data)
            fdmap[fd].send(b'ok')
