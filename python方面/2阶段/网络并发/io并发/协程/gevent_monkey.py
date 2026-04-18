import gevent
from gevent import monkey

monkey.patch_time()
"""monkey:一个可以修改其他io阻塞函数底层逻辑的脚本，可以将被修改的函数变成协程，即在阻塞时可以执行别的函数
在别的函数阻塞时可以返回继续执行原来的函数，进而提高效率
"""
from time import sleep


# 协程函数
def foo(a, b):
    print("Running foo..", a, b)
    sleep(2)
    print("Foo again..")


def bar():
    print("Running bar..")
    sleep(3)
    print("bar again..")


# 生成协程对象
f = gevent.spawn(foo, 1, 2)  # 传参
b = gevent.spawn(bar)
# gevent.sleep (5)#只有在调用gevent中的阻塞函数的时候，才能够在阻塞的同时执行不阻塞的函数
b = gevent.joinall([f, b])  # 阻塞等待f,b两个协程执行完毕
