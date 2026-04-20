"""
    Squeue.py 队列的顺序存储
敏思路分析: 1.基于列表完成数居存储
2.通过封装规定数据操作
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    # 自定义队列异常


class QueueError(Exception):
    pass


# 队列操作
class SQueue:
    def __init__(self):
        self.__elems = []

    def is_empty(self):
        return self.__elems == []

    # 入队
    def queue(self,val):
        self.__elems.append(val)

    # 出队
    def dequeue(self):
        if not self.__elems:
            raise QueueError("queue is empty")
        return self.__elems.pop(0)


if __name__ == "__main__":
    sq = SQueue()
    for i in range(10):
        sq.queue(i)
    from sstack import *
    #倒序
    st=SStack()
    while not sq.is_empty():
        st.push(sq.dequeue())#将队列中的数据放入栈中
    while not st.is_empty():
        sq.queue(sq.dequeue())#将栈中的数据放入中
    while not sq.is_empty():
        print(sq.dequeue())
