"""
p = select.poll()
功能.txt ： 创建poll对象
返回值： poll对象

p.register(fd,event)
    功能.txt: 注册关注的IO事件
    参数：fd 要关注的IO

event 要关注的IO事件类型
常用类型：
    POLLIN 读IO事件（rlist）
    POLLOUT 写IO事件 (wlist)
    POLLERR 异常IO （xlist）
    POLLHUP 断开连接
    e.g. p.register(sockfd,POLLIN|POLLERR)

p.unregister(fd)
    功能.txt：取消对IO的关注
    参数：IO对象或者IO对象的 fileno(文件描述符)

events = p.poll()
    功能.txt： 阻塞等待监控的IO事件发生
    返回值： 返回发生的IO
events格式 [(fileno,event),()....]
每个元组为一个就绪IO，元组第一项是该IO的fileno，第二项为该IO就绪的事件类型
"""
from select import *
from socket import *
from time import sleep

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 创建poll对象
"""
p=poll()：这行代码创建了一个poll对象p。  poll()是select模块中的一个函数，用于创建一个poll对象。
这个对象可以用来监控多个文件描述符（如套接字）的状态变化‌
"""
p = poll()  # poll()包含在select函数内部，所以可以直接调用

# 始终和register的io保持一致
# 每进行一个io操作的时候 系统都会给这个操作分配i一个唯一的文件描述符
fdmap = {s.fileno(): s}  # 通过这个io的文件描述符来找到其本身

# 关注s  第二个参数不传表示关注所有套接字
p.register(s, POLLIN)  # 在读io事件中关注(被动接收的操作 例如accept():等待连接，recv()：等待接收消息)
# p.register(s, POLLIN | POLLERR)  # 在读io事件和异常io事件中关

# 循环监控io发生
while True:
    """
    p.poll(): 这行代码调用  ***poll对象的poll()方法***  ，该方法会阻塞等待监控的IO事件。
    当任何一个文件描述符的状态发生变化时（例如，有数据可读或可写），    poll()方法会返回一个列表  ，
    列表中的每个元素是一个元组，包含文件描述符（fileno）和事件类型（event）。
    例如，[(fileno, POLLIN)]表示文件描述符fileno上有数据可读‌
    """
    events = p.poll()  # 阻塞等待 s(被动接收) 发生，或者客户端c发来了消息(此前c已经在s.accept中加入字典被关注了)
    # print(events)#[(3, 1)]: 3:fileno(文件描述符) 1：IO就绪的事件类型
    # sleep(1)
    for fd, event in events:  # fd:文件描述符  event:事件类型
        # 区分哪个io发生
        if fd == s.fileno():  # 返回的阻塞接收描述符与套接字s的描述符相同，表示s.accept发生(即有客户端连接)
            c, addr = fdmap[fd].accept()
            print("connect from...", addr)
            p.register(c, POLLIN | POLLERR)  # 再关注c
            fdmap[c.fileno()] = c  # 将关注的对象c添加到字典里面

        elif event & POLLIN:  # 只在读操作时才进入函数
            data = fdmap[fd].recv(1024)# 客户端套接字c
            if not data:
                p.unregister(fd)  # 取消关注
                fdmap[fd].close()  # 关闭关注的对象,即客户端套接字
                del fdmap[fd]  # 从字典删除
                continue
            print(data)
            fdmap[fd].send(b'ok')
