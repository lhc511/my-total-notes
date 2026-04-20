from greenlet import greenlet


def fun01():
    print("执行fun1")
    gr2.switch()
    print("结束fun1")


def fun02():
    print("执行fun2")
    gr1.switch()
    print("结束fun2")


# 将函数变为协程
gr1 = greenlet(fun01)
gr2 = greenlet(fun02)
gr1.switch()  # 选择执行哪个协程、
"""
结果：
执行fun1
执行fun2
结束fun1
"""
