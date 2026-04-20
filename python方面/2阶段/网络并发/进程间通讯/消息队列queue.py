# from multiprocessing import Queue
"""
辅助函数：
q.full( 判断队列是否为满
q.empty() 判断队列是否为空
q.qsize()获取队列中消息个数
q.close()关闭队列
"""

"""给队列中存放消息"""
# q = Queue(3)  # 括号内表示该序列最多存放三个对象 多出去就会阻塞(默认为阻塞)
#
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)

# block=False 将其设置为非阻塞，此时队列满了之后会报错
# q.put(4, block=False)  # queue.Full(报错)

# 阻塞5秒 五秒后报错
# q.put(4, timeout=5)
"""获取消息"""
# 先进先出
# print(q.get())  # 1
# print(q.get())  # 2
# print(q.get())  # 3
# q.get(block=False)  # 由于队列已经空了：三个数取完了 报错 _queue.Empty
# q.get(timeout=3)  # ，三秒后报错


"""示例代码"""
from multiprocessing import Queue, Process
from time import sleep
from random import randint

# 创建消息队列
q = Queue(5)


def handle():
    for i in range(6):
        x = randint(1, 34)
        q.put(x)
        q.put(randint(1, 16))


def request():
    while True:
        sleep(0.2)
        try:
            print(q.get(True), end=' ')  # 出队
        except:
            break


p1 = Process(target=handle)
p2 = Process(target=request)
p1.start()
p2.start()
p1.join()
p2.join()
