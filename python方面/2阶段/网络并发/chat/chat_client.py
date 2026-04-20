"""
chat room 客户端
发送请求，展示结果
"""

from socket import *
import os, sys

# 服务器地址
ADDR = ('192.168.129.130', 8888)


# 发送消息
def send_msg(s, name):
    while True:
        try:
            text = input("发言：")
        # 当输入消息的时候用键盘退出时 向服务器发送 的内容就是quit
        except KeyboardInterrupt:
            text = 'quit'

        # 客户端输入quit直接退出
        if text.strip() == 'quit':  # .strip 去掉两侧空格
            msg = 'Q ' + name
            s.sendto(msg.encode(), ADDR)
            # 不用收到服务器回馈，可以直接退出
            sys.exit("退出聊天室")
        msg = 'C %s %s' % (name, text)
        s.sendto(msg.encode(), ADDR)


# 客户端接受消息
def recv_msg(s):
    while True:
        try:
            data, addr = s.recvfrom(4096)
        except KeyboardInterrupt:  # 好像也没有用 可以直接收
            sys.exit()
        # data, addr = s.recvfrom(4096)

        # 从服务器受到EXIT退出
        # 此处是键盘打断的函数，当键盘退出程序相当于对服务器发送一个quit 见上一个函数，此时收到的就是EXIT
        if data.decode() == 'EXIT':
            sys.exit()

        print(data.decode() + '\n发言', end=" ")  # 这里的data是名字和内容


# 客户端启动函数
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    # 进入聊天室
    while True:
        name = input("请输入名字:>>")
        msg = 'L ' + name  # L申请加入聊天室
        s.sendto(msg.encode(), ADDR)
        data, addr = s.recvfrom(1024)
        if data.decode() == 'ok':
            print("您已进入聊天室")
            break
        else:
            print(data.decode())

    # 已经进入聊天室
    pid = os.fork()
    if pid < 0:
        sys.exit("Error")
    elif pid == 0:
        send_msg(s, name)  # 子进程发送消息
    else:
        recv_msg(s)  # 父进程接受消息


main()
