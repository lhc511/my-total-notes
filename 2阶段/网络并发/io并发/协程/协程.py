"""
在应用层通过函数的暂停实现多个任务跳转切换
每个函数都可以从任意位置跳出并重新调用后继续执行

本质是单线程无法用多核资源
"""
# 协程就是一个可以随时挂起重入的函数。也叫做异步编程


# 该协程只能用其内部本身有的函数，所以有较大局限性，当在同一线程中当有一个函数发生阻塞时，会优先执行下一个没有阻塞的函数
# 并在下一次返回时可以继续执行那个没执行完的函数，在io密集型操作时可以提高效率
import asyncio
from time import sleep


# 定义协成函数
async def fun01():
    print("start1")  # 设置跳转阻塞点
    await asyncio.sleep(2)
    print("end1")


async def fun02():
    print("start2")
    await asyncio.sleep(3)
    print("end2")


# 生产协成对象
cor1 = fun01()
cor2 = fun02()
tasks = [asyncio.ensure_future(cor1), asyncio.ensure_future(cor2)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
