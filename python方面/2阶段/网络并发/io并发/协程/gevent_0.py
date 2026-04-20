import gevent


# 协程函数
def foo(a, b):
    print("Running foo..", a, b)
    gevent.sleep(2)
    print("Foo again..")


def bar():
    print("Running bar..")
    gevent.sleep(3)
    print("bar again..")


# 生成协程对象
f = gevent.spawn(foo, 1, 2)  # 传参
b = gevent.spawn(bar)
# gevent.sleep (5)#只有在调用gevent中的阻塞函数的时候，才能够在阻塞的同时执行不阻塞的函数
b = gevent.joinall([f, b])#阻塞等待f,b两个协程执行完毕
