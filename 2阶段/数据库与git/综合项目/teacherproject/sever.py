from socket import *
from multiprocessing import Process
import sys
import signal
from mysql import *

HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST, PORT)
db = Database(database="user")


def show_history(c, data):
    name = data.split(" ")[1]
    record = db.show_history(name)
    if not record:
        c.send(b'not find')
        return
    msg = '$'
    for item in record:
        msg01 = item[0] + " " + item[1]+"$"
        msg = msg + msg01
    c.send(msg.encode())


def do_query(c, data):
    tmp = data.split(" ")
    name = tmp[1]
    word = tmp[2]

    db.do_insert_hist(name, word)

    # 如果没找到返回None
    mean = db.query(word)
    if not mean:
        c.send("not find".encode())
    else:
        msg = "%s : %s" % (word, mean)
        c.send(msg.encode())


def do_register(c, data):
    tmp = data.split(" ")
    name = tmp[1]
    passwd = tmp[2]
    # True表示注册成功
    if db.register(name, passwd):
        c.send(b'ok')
    else:
        c.send(b'fail')


# 登陆
def do_login(c, data):
    tmp = data.split(" ")
    name = tmp[1]
    passwd = tmp[2]
    if db.login(name, passwd):
        c.send(b'ok')
    else:
        c.send(b"fail")


def request(c):
    db.create_cursor()  # 每个子进程单独创建一个游标
    while True:
        data = c.recv(1024).decode()
        if not data or data[0] == "E":
            sys.exit()  # 对应的子进程退出
        print(c.getpeername(), ":", data)
        if data[0] == "R":
            do_register(c, data)
        elif data[0] == "L":
            do_login(c,data)
        elif data[0] == "Q":
            do_query(c, data)
        elif data[0] == "S":
            show_history(c, data)


# 搭建网络
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    # 循环等待客户端连接
    print("listen the port 8000")
    while True:
        try:
            c, addr = s.accept()
            print("Connect", addr)
        except KeyboardInterrupt:
            s.close()
            db.close()
            sys.exit()
        except Exception as e:
            print(e)
            continue
        # 为客户端创建子进程
        p = Process(target=request, args=(c,))
        p.daemon = True
        p.start()


if __name__ == "__main__":
    main()
