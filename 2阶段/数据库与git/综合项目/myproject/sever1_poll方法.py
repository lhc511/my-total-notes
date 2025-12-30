from socket import *
import pymysql
from multiprocessing import *
import sys
import signal
import os
from select import *


class DictSever:
    def __init__(self):
        self.s = socket()
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)
        self.s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.ADDR = '0.0.0.0'
        self.PORT = 8888
        self.addr = (self.ADDR, self.PORT)
        self.s.bind(self.addr)
        self.s.listen(5)
        self.db = pymysql.connect(host='localhost', port=3306, user='root', password='123', database='user',
                                  charset='utf8')
        self.cur = self.db.cursor()
        self.db_word = pymysql.connect(host="localhost", port=3306, user="root", password="123", database="dict",
                                       charset="utf8")
        self.cur_word = self.db_word.cursor()
        self.db_record = pymysql.connect(host="localhost", port=3306, user="root", password="123", database="user",
                                         charset="utf8")
        self.cur_record = self.db_record.cursor()


    def login(self, c):
        msg = c.recv(1024).decode()  # 已经解码过的信息[name,password]
        list_umsg = msg.split(' ')
        self.seek_msg_login(list_umsg[0], list_umsg[1], c)  # 查找在登陆时用户是否注册过账号
        
    def password_verify(self, name, password, c):
        sql = "select password from user_dict where name='%s'" % name
        self.cur.execute(sql)
        if self.cur.fetchone()[0] == password:  # 密码正确
            c.send(b'ok')
            self.function_second(c)
        else:
            c.send(b'password wrong')

    def seek_msg_login(self, name, password, c):
        sql = "select name from user_dict where name='%s'" % name
        self.cur.execute(sql)
        ####错误示范#######   报错：'NoneType' object is not subscriptable
        # data=self.cur.fetchone()[0]#代码尝试对None值进行类似列表或字典的下标访问操作（如obj[0]或obj["key"]）
        if self.cur.fetchone():  # 如果找到了
            self.password_verify(name, password, c)
        else:
            c.send(b"not find,please register account")

    def seek_repeat_register(self, name, c):
        sql = "select name from user_dict where name='%s'" % name
        self.cur.execute(sql)
        # print(self.cur.fetchall())
        if self.cur.fetchall():  # 如果找到重复了
            c.send(b'account existed')
            return None
        else:
            c.send(b'register successfully0')
            return True

    def register_(self, c):
        msg = c.recv(1024).decode()  # 已经解码过的信息
        list_umsg = msg.split(' ')  # [name,password]
        print(list_umsg)
        if self.seek_repeat_register(list_umsg[0], c):  # 如果注册用户名没有重复
            self.function_second(c)
            insert_msg = "insert into user_dict (name,password) values (%s,%s)"
            self.cur.execute(insert_msg, [list_umsg[0], list_umsg[1]])
            self.db.commit()

    def exit(self, c):
        c.send(b'exit already')
        c.close()
        print("用户退出")

    #############   二级查询功能   #############
    def function_second(self, c):
        while True:
            option = int(c.recv(1024).decode())
            if option == 1:
                word = c.recv(1024).decode()
                if word == '0':
                    # c.close()
                    break
                self.find_word(c, word)
            elif option == 2:
                self.output_record(c)
            elif option == 3:
                self.exit(c)
                break

    def find_word(self, c, word):
        list_data = word.split(" ")  # [word,name]
        print(list_data)
        seek_word_sql = "select * from word where word='%s'" % list_data[0]
        self.cur_word.execute(seek_word_sql)
        data = self.cur_word.fetchone()
        if data:  # 找到了
            data = "ok" + data[1] + ":" + data[2]
            c.send(data.encode())
            self.insert_record(data[2:], list_data[1])
            print(data[2],data[1])
        else:
            c.send(b'not find')

    def insert_record(self, word, name):
        list_word = word.split(":")
        print(list_word)
        insert_word_sql = "insert into wordrecord values (%s,%s)"
        self.cur_record.execute(insert_word_sql, [name, list_word[0]])
        self.db_record.commit()

    def output_record(self, c):
        data_list = c.recv(1024).decode().split(" ")  # [name,option]
        get_record_sql = "select * from wordrecord where name='%s'" % data_list[0]
        self.cur_record.execute(get_record_sql)
        send_msg1 = "#"
        if data_list[1] == '1':  # 查十条
            data = self.cur_record.fetchmany(10)
            self.record_existed_judge(c, data, send_msg1)
        else:
            data = self.cur_record.fetchall()
            self.record_existed_judge(c, data, send_msg1)

    def record_existed_judge(self, c, data, send_msg1):
        if not data:
            c.send(b"no historical record")
        else:
            for item in data:
                send_msg1 = send_msg1 + item[0] + " " + item[1] + ":" + item[2] + "#"
            c.send(send_msg1.encode())

    def fun_select(self, c):
        option = c.recv(1024).decode()
        if option == '1':
            self.login(c)
            # c.close()
        elif option == '2':
            self.register_(c)
            # c.close()
        elif not option or option == '3':
            self.exit(c)

    ###########      main      ###############
    def main(self):
        # p1 = Process(target=self.fun_select())
        while True:
            try:
                # self.spy_port()
                c, addr = self.s.accept()
                p1 = Process(target=self.fun_select, args=(c,))
                p1.daemon = True
                p1.start()
            except KeyboardInterrupt:
                pass
            except Exception as e:
                print(e)


if __name__ == "__main__":
    dt = DictSever()
    dt.main()

    # def main(self):
    #     # p1 = Process(target=self.fun_select())
    #     while True:
    #         try:
    #             # dt.sever_exit()
    #             events = self.p.poll()
    #             for c, event in events:
    #                 if c == self.s.fileno():
    #                     c, addr = self.s.accept()
    #                     self.p.register(c, POLLIN)
    #                     self.cmap[c.fileno()] = c
    #                 elif event & POLLIN:
    #                     if not self.fun_select(c):
    #                         c.close()
    #                         del c
    #                         continue
    #         except KeyboardInterrupt:
    #             self.sever_exit(c)
    #         except Exception as e:
    #             print(e)

    # def __init__(self):
    #     self.s = socket()
    #     signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    #     self.s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    #     self.ADDR = '0.0.0.0'
    #     self.PORT = 8888
    #     self.addr = (self.ADDR, self.PORT)
    #     self.s.bind(self.addr)
    #     self.s.listen(5)
    #     self.db = pymysql.connect(host='localhost', port=3306, user='root', password='123', database='user',
    #                               charset='utf8')
    #     self.cur = self.db.cursor()
    #     self.db_word = pymysql.connect(host="localhost", port=3306, user="root", password="123", database="dict",
    #                                    charset="utf8")
    #     self.cur_word = self.db_word.cursor()
    #     self.db_record = pymysql.connect(host="localhost", port=3306, user="root", password="123", database="user",
    #                                      charset="utf8")
    #     self.cur_record = self.db_record.cursor()
    #
    #     self.p = poll()
    #     self.cmap = {self.s.fileno(): self.s}
    #     self.p.register(self.s, POLLIN)
