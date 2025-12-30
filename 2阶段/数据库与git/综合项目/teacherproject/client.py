""""""
from socket import *
from getpass import getpass
import sys

ADDR = ('127.0.0.1', 8000)
s = socket()
s.connect(ADDR)
def show_history(name):
    msg="S %s"%name
    s.send(msg.encode())
    data=s.recv(4086).decode()
    list_data=data.split("$")
    for item in list_data:
        print(item)

def do_query(name):
    while True:
        word = input("单词：")
        if word == "##":
            break
        msg = "Q %s %s" % (name, word)
        s.send(msg.encode())
        data = s.recv(2048).decode()
        print(data)


# 登陆后的界面
def login(name):
    while True:
        print("""===========================
                 1.查单词    2.历史记录  3.注销
        """)
        cmd = input("输入选项")
        if cmd == '1':
            do_query(name)
        elif cmd == "2":
            show_history(name)
        elif cmd == "3":
            break
        else:
            print("请输入正确选项")


def do_register():
    while True:
        name = input("user:")
        passwd = getpass()
        passwd1 = getpass("again:")
        if passwd != passwd1:
            print("两次输入不一致")
            continue
        if " " in name or " " in passwd:
            print("不允许空格")
            continue

        msg = "R %s %s" % (name, passwd)
        s.send(msg.encode())
        data = s.recv(1024).decode()
        if data == "ok":
            print("注册成功")
            login(name)
        else:
            print("注册失败")
        return


def do_login():
    name = input("user:")
    passwd = getpass()
    msg = "L %s %s" % (name, passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == "ok":
        print("登陆成功")
        login(name)
    else:
        print("登陆失败")


# 搭建客户端网络
def main():
    while True:
        print("""===========================
                 1.注册    2.登陆       3.退出
        """)
        cmd = input("输入选项")
        if cmd == '1':
            do_register()
        elif cmd == "2":
            do_login()
        elif cmd == "3":
            s.send(b"E")
            sys.exit("谢谢使用")
        else:
            print("请输入正确选项")


if __name__ == "__main__":
    main()
