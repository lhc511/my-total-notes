class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class QueueError(Exception):
    pass


class LQueue:
    def __init__(self):
        # 定义队头和队尾的属性变量
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.rear == self.front

    # 入队
    def queue(self, val):
        self.rear.next = Node(val)
        self.rear = self.rear.next

    # 出队   此时front指向该数据时该数据实际上已经 出队列 了
    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("queue is empty")
        self.front = self.front.next
        return self.front.val


if __name__ == "__main__":
    lq = LQueue()
    lq.queue(10)
    lq.queue(20)
    lq.queue(30)
    print(lq.dequeue())
