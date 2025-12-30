"""
关键字传参和一般传参一样，唯一区别是可以不按照默认位置传参(只要将值赋值给与函数形参名称相同的参数就好)

def happy_birthday(name,age):
    print('祝'+name+'生日快乐')
    print((str(age)+'岁生日快乐'))
happy_birthday('吴某',18)#位置传参
happy_birthday(age=18,name='吴某')#关键字传参
happy_birthday('吴某',age=18)#混合传参需要位置传参在前，关键字传参在后，否则会报错！
"""
# from threading import Thread
# from time import sleep, ctime
#
#
# class MyThread(Thread):
#     def __init__(self, *args,**kwargs): #*args:将任意参数传递作为一个元组
# **kwargs:收集任意多个关键字传参作为字典
#
# def __init__(self, target=None, args=(), kwargs={}):
#     super().__init__()  # 此行不许传参
#     if kwargs is None:
#         kwargs = {}
#     self.target = target
#     self.args = args
#     self.kwargs = kwargs
#
# def run(self):
#     self.target(*self.args, **self.kwargs)  # 将元组和字典中的每一样逐个赋值
#
#
# def player(sec, song):
#     for i in range(3):
#         print("Playing %s:%s" % (song, ctime()))
#         sleep(sec)
#
#
# t = MyThread(target=player, args=(3,),
#              kwargs={'song': '凉凉'})  # 把 键值对 里面的 值 传递给函数中的参数，用 字符串 形式作为 健 来寻找函数中的 形参
#
# t.start()
# t.join()


"""teacher
由于每一个图片在复制的和时候在开头都有一个识别码，而在下半部分没有所以会出问题
父亲创建打开文件，子进程会相互影响
"""
from multiprocessing import Process
import os

filename = '/home/ubuntu/图片/史莱姆.jpeg'
size = os.path.getsize(filename)


# 如果把这句代码放在父进程里，不写在子进程里，会让代码出错
# 因为子进程是将父进程里面的代码拷贝一份。在读取文件会进行 io 操作
# 并操作系统层面上留下痕迹，而子进程在读取文件时会公用父进程上在操作系统留下的痕迹
# 会从上一次读取的位置继续，而且子进程在运行上先后具有随机性，因此可能出问题
# 所以最好在每一个子进程都打开一次文件，防止出错
# fr = open(filename, 'rb')

# 复制上半部分
def top():
    fr = open(filename, 'rb')
    fw = open('top.jpg', 'wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()


def bot():
    fr = open(filename, 'rb')
    fw = open('bot.jpg', 'wb')
    fr.seek(size // 2, 0)  # 以文件开头为基准向后移 size//2个位置
    fw.write(fr.read())
    fr.close()
    fw.close()


p1 = Process(target=top)
p2 = Process(target=bot)
p1.start()
p2.start()
p1.join()
p2.join()
