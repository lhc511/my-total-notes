"""
t.name线程名称
t.setName()设置线程名称
t.getName()获取线程名称
t.is_alive()查看线程是否在生命周期
t.daemon设置主线程和分支线程的退出关系
t.setDaemon()设置daemon属性值
t.isDaemon()查看daemon属性值

daemon为True时主线程退出分支线程也退出。要在start前设置，通常不和join一起使用。
"""
from threading import Thread
from time import sleep


def fun():
    sleep(3)
    print("线程属性测试")


# t = Thread(target=fun,name='aaa')

# 这两个方法在莫个版本被弃用了
# t.setName("nugv")
# print(t.getName())

"""正确"""
# 创建线程时命名(或修改名字)
t = Thread(name="MyThread", target=fun)

# 动态修改名称
# t.name = "NewName"  # 替代旧版setName()
# print(t.name)#访问名字

# t.setDaemon(True)  # 主线程退出分支也退出
t.daemon = True  # 主线程退出分支也退出 新版

print("is_alive", t.is_alive())  # is_alive False
t.start()
print("is_alive", t.is_alive())  # is_alive True
print("daemon", t.daemon)
