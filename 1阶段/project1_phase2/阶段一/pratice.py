# 创建两个链表，并将一个链表按顺序插入另一个
from linklist import *

list01 = [1, 5, 7, 8, 10, 12, 13, 19]
list02 = [0, 3, 4, 9]
l01 = LinkList()
l02 = LinkList()

l01.init_list(list01)
l02.init_list(list02)

# l01.show()
# l02.show()

"""MyFunction"""


# list01 = [1, 5, 7, 8, 10, 12, 13, 19]   p
# list02 = [
#  , 3, 4, 9]                   q
def merge(l1, l2):
    p = l1.head  # 初始位置上 值(val) 为None
    q = l2.head.next
    while True:
        # 均为链表中的第一个数据
        if q.val > p.next.val:
            p = p.next
        else:
            tmp = p.next
            p.next = q
            p=p.next
            q = tmp


"""teacher"""
# def merge(l01, l02):
#     # l02合并到l01中
#     p = l01.head  # 找的是起点
#     q = l02.head.next  # 找的是起点后的对象，链表2的第一个数据
#     # 不断的中断链表 并将链表中断处以后的数据 根据条件不断交换赋值链表
#     while p.next is not None:
#         if p.next.val < q.val:  # 链表一中第一个对象的值(并非起始位置) < 链表二中第一个对象的值
#             p = p.next  # 继续寻找下一个对象
#         else:
#             tmp = p.next  # 把该位置的下一个对象赋值给tmp
#             p.next = q  # 把q赋值给 p 原本的下一个位子 链表二中的对象
#             p = p.next  # 链表二中的对象(及其之后的链表)赋值给p，向下寻找
#             q = tmp  #
#     p.next = q
#
# merge(l01, l02)
#
# l01.show()
