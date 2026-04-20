# def num_square(num):
#     i = 1
#     for item in range(1, num + 1):
#         print(item)
#         i = i * item
#     return i
#
#
# print(num_square(5))

# 二叉树顺序存储:
# 二叉树本身是一种递归结构，可以使用Python list进行存储。但是如果二
# 叉树的结构比较稀疏的话浪费的空间是比较多的。
# 1.空结点用None表示
# 2.非空二叉树用包含三个元素的列表[d,l,r]表示，其中d表示根结点，
# l,r左子树和右子树。
# list01 =['A',['B', None, None
#              ],
#              ["C",['D',['F',None,None],
#                        ['G',None,None],
#                   ],
#                   ['E',['H',None,None],
#                        ['I',None,None],
#                   ],
#               ]
#          ]
# 思路分析:
# 1.使用链式存储，一个Node表示一个树的节点
# 2.节点考虑使用两个属性变量分别表示左连接和右连接

# 二叉树节点
from queue_class import *


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BitTree:
    def __init__(self, root=None):
        self.root = root

    # 先序遍历
    def preOrder(self, node):
        if node is None:  # 终止条件
            return
        print(node.val, end=" ")  # A B C D F G E I H
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序遍历
    def middleOrder(self, node):
        if node is None:  # 终止条件
            return
        self.preOrder(node.left)
        print(node.val)
        self.preOrder(node.right)

    # 层次遍历
    def levelOrder(self, node):
        """
            让初始节点先入队，谁出队就遍历谁，并且让它的左右孩子分别入队，直到队列为空
        """
        sq = SQueue()
        sq.queue(node)  # 初始节点入队
        while not sq.is_empty():  # 当顺序队列[一个列表]不是空的时候
            node = sq.dequeue()#出栈
            # 打印出队元素
            print(node.val, end="")
            if node.left:  # 倘若左子节点不为None,就把该节点加入队列
                sq.queue(node.left)
            if node.right:
                sq.queue(node.right)

    # 后序遍历
    def belowOrder(self, node):
        if node is None:  # 终止条件
            return
        self.preOrder(node.left)
        self.preOrder(node.right)
        print(node.val)


if __name__ == "__main__":
    # В F G DТ H Е С А

    b = Node('B')
    f = Node('F')
    g = Node('G')
    d = Node('D', f, g)
    i = Node('I')
    h = Node('H')
    e = Node('E', i, h)
    c = Node('C', d, e)
    a = Node('A', b, c)

    # 将A作为遍历起始位置
    bt = BitTree(a)
    bt.preOrder(bt.root)
