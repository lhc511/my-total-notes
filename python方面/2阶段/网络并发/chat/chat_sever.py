"""
chat room
env: python3.10
socket udp & fork
"""
from socket import *
import os, sys

"""
全局变量:很多封装模块都要用或者有一定的固定含义
"""
# 服务器地址
ADDR = ('192.168.129.130', 8888)
# 存储用户 {name:address}
user = {}


def do_login(s, name, addr):
    if name in user:
        s.sendto('该用户存在'.encode(), addr)
        return
    s.sendto(b'ok', addr)
    # 通知别人
    msg = "\n欢迎'%s'进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])

    user[name] = addr  # 将新的用户插入字典


# 聊天
def do_chat(s, name, text):
    msg = "\n%s %s" % (name, text)
    for i in user:  # 在字典中遍历的是建，第二个变量才是值
        # 不包括本人 在聊天的过程当中，已经登入
        if i != name:
            s.sendto(msg.encode(), user[i])  # 信息 地址


# 退出
def do_quit(s, name):
    msg = "%s 退出聊天室" % name
    for i in user:  # 在字典中遍历的是建，第二个变量才是值
        if i != name:  # 给其他人发送某人退出的消息
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b'EXIT', user[i])
    del user[name]  # 删除


# 处理请求s.sendto(msg.encode(), user[i])
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)  # data 是 “模式选择C” “姓名” 和 “要说的内容”

        # 倘若发送的数据里面有空格 就用空格先将其分开 作为列表中的多项数据 最后在下面传输的时候用 " ".join 函数加入空格来还原数据
        tmp = data.decode().split(' ')  # 拆分请求 将data用空格拆分为列表

        # 根据不同请求类型执行不同事情
        # L 进入 C 聊天 Q 聊天
        if tmp[0] == 'L':
            do_login(s, tmp[1], addr)  # 执行具体工作  套接字 名字 地址
        elif tmp[0] == 'C':
            # 从第三个元素之后每一个元素之间都加空格
            text = ' '.join(tmp[2:])  # 从列表中 第三项数据 开始按照空格进行拼接
            do_chat(s, tmp[1], text)  # 客户端 名字 说话内容
        elif tmp[0] == 'Q':
            do_quit(s, tmp[1])


def main():
    # udp服务端
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    # 主进程作服务器的创建 和客户端发来的请求处理

    pid = os.fork()
    # 子线程负责发送管理员消息
    if pid == 0:
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员" + msg
            s.sendto(msg.encode(), ADDR)  # 给本服务器地址发送消息
    # 请求处理函数
    do_request(s)


main()
