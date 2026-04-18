from socket import *
import sys
from multiprocessing import *
import signal


class ClientLogin:
    def __init__(self):
        self.s = socket()
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)
        self.s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.addr = ('127.0.0.1', 8888)
        self.s.connect(self.addr)

    def login(self):
        try:
            name = input("请输入用户名：")
            data = self.pwd_name_send(name)
            if data == "ok":
                self.function_view(name)
            else:
                print(data)
        except KeyboardInterrupt:
            self.exit()
        except Exception as e:
            print(e)
            self.exit()

    def register(self):
        try:
            name = input("请输入用户名：")
            data = self.pwd_name_send(name)
            print(data[0:len(data) - 1])  # account existed  or registered successfully0
            if data[-1] == '0':  # 如果注册成功
                while True:
                    print("""=========================
                             1.进入功能页面  2返回登陆页面
                    """)
                    option = int(input("请输入选项"))
                    if option == 1:
                        back = self.function_view(name)
                        if back:
                            break
                    elif option == 2:
                        return
                    else:
                        print("请重新输入")

        except KeyboardInterrupt:
            print("您已退出")
            self.exit()
        except Exception as e:
            print(e)
            self.exit()

    def pwd_name_send(self, name):
        password = input("请输入密码")
        send_msg = name + ' ' + password
        self.s.send(send_msg.encode())
        data = self.s.recv(1024).decode()
        return data

    def exit(self):
        print(self.s.recv(1024))  # 服务端发来的退出信息
        self.s.close()
        sys.exit()

    ################     二级功能查询     #################
    def check_word(self, name):
        word = input("请输入要查询的单词")
        if not word:
            self.s.send(b'0')
            return None
        word = word + " " + name
        self.s.send(word.encode())
        data = self.s.recv(1024).decode()
        if data[0:2] == "ok":
            print(data[2:])
        else:
            print(data)

    def get_record(self,name):
        while True:
            option = input("""============================
                                1.查询十条记录    2.查询所有记录
                                """)
            if option == '1' or option == '2':
                break
            else:
                print("输入错误清重新输入")
        data=name+" "+option
        self.s.send(data.encode())
        data=self.s.recv(32768).decode()
        list_record=data.split("#")
        for item in list_record:
            print(item)
    def get_out(self):
        # self.s.send(b'3')
        print("返回至上一界面")

    def function_view(self, name):
        while True:
            try:
                print("""  ==========================
                                              1.查单词   2.历史记录  3.返回
                                   """)
                option = input("请输入选项:")
                if option == '1':
                    self.s.send(option.encode())
                    self.check_word(name)  # 退出查单词
                elif option == '2':
                    self.s.send(option.encode())
                    self.get_record(name)
                elif option == '3':
                    self.s.send(option.encode())
                    self.get_out()
                    return True
            except KeyboardInterrupt:
                print("\n您已退出")
                sys.exit()
            except Exception as e:
                print(e)


class LoginView:
    def __init__(self):
        self.cl = ClientLogin()
        # pass

    def login_view(self):
        while True:
            print("""========================
                         1.登陆    2.注册    3.退出
                                """)
            option = input("请输入选项：")

            self.cl.s.send(option.encode())
            if option == '1':
                self.cl.login()
            elif option == '2':
                self.cl.register()
            elif option == '3':
                self.cl.exit()
            else:
                print("输入错误清重新输入")

    def main(self):
        try:
            # self.sever_exit()
            self.login_view()
        except KeyboardInterrupt:
            self.cl.s.send('3'.encode())
            self.cl.exit()
        except Exception as e:
            print(e)
            # pass
    # def listen_sever(self):
    #     data=self.cl.s.recv(1024).decode()
    #     if data=='404':
    #         self.sever_exit()
    #     else:
    #         self.cl.exit(data)

    # def sever_exit(self):
    #     self.cl.s.close()
    #     sys.exit("服务器关闭")


if __name__ == "__main__":
    cv = LoginView()
    cv.main()
