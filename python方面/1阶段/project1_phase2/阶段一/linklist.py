"""
    链式列表
"""


# 创建节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


#
# node1 = Node(1)
# node2 = Node(2, node1)  # node2.next - node1
# node3 = Node(3, node2)  # node3. next- node2
# a = 1
# b = (2, a)
# c = (3, b)
# print(c)  # (3, (2, 1))


class LinkList:
    """
        思路:
            单链表类，生成对象可以进行增删改查操作
            具体操作通过调用具体方法完成
    """

    def __init__(self):
        """
        初始化链表，标记一个链表的开端，以便于获取后续的节点
        """
        self.head = Node(None)

    # 为链表添加一组节点
    def init_list(self, list_target):
        p = self.head  # p本身也是一个对象（在此处）
        for item in list_target:
            p.next = Node(item)  # next存储的是下一个对象
            p = p.next  # 一个对象里面嵌套着另一个对象

    # 判断列表是否为空
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    # 清空列表      python内部的清理机制：虽然把链表的第一个节点为None无法查找后面链表的数据，但python内部的清理器会在需要时将其清除
    def clear(self):
        self.head.next = None

    # 遍历链表
    def show(self):
        p = self.head.next  # 有效节点
        while p is not None:
            print(p.val)
            p = p.next  # p向后移动

    # 尾部插入 无效率因为会在遍历链表到最后一个再加
    def append(self, val):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 头部插入
    def head_insert(self, val):
        # 不能变顺序
        node = Node(val)  # 创建一个节点
        node.next = self.head.next  # 把原链表中初始链表的 下一个节点 赋值给新创建的节点中的next(查找)
        self.head.next = node  # 把新节点赋值给 初始数据（对象）的 查找位置

    # 指定插入位置
    def insert(self, index, val):
        node = Node(val)
        p = self.head
        for item in range(index):
            if p.next is None:  # 若超过界限则退出，并在尾部加数据
                break
            p = p.next
        node.next = p.next  # p.next实际上是下一个对象，赋值给node中的 查找位置2
        p.next = node

    # 删除节点
    def delete(self, x):
        p = self.head
        # 结束循环必然两个条件其一为假
        while p.next and p.next.val != x:
            p = p.next

        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next = p.next.next

    # 获取某个节点值，传入节点位置获取节点值
    def get_index(self, index):
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("list index out of range")
            p = p.next
        return p.val


if __name__ == "__main__":
    l = LinkList()
    l.head = Node(1)
    l.init_list([1, 2, 3, 4, 5])
    l.show()
