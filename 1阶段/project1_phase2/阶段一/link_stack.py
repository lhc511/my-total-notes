# 思路分析: 1.源于链表结构
# 2.封装栈的操作方法(入栈，出栈，栈空，栈顶元素)
# 3.链表的开头作为栈顶？(不用每次遍历)
# 自定义异常
class StackError(Exception):
    pass


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


"""teacher"""


class LStack:
    def __init__(self):
        # 标记栈顶位置
        self.__top = None

    def is_empty(self):
        return self.__top is None

    def push(self, val):
        # 合并语句
        self.__top = Node(val, self.__top)
        # node = Node(val)
        # node.next = self.__top  # 为node.next=None 把None赋值给node.next
        # self.__top = node  # 把节点赋值给self.__top(栈顶标记)

    # 找添加的最后一个数据
    def pop(self):
        if self.__top is None:
            raise StackError("stack is empty")
        value = self.__top.val
        self.__top = self.__top.next
        return value

    # 找栈顶的数据
    def top(self):
        if self.__top is None:
            raise StackError("stack is empty")
        return self.__top.val  # 返回栈顶的数据


"""mine"""

# class LStack():
#     def __init__(self):
#         self.__top = None
#
#     def is_empty(self):
#         if self.__top is None:
#             raise StackError("stack is None")
#
#     def push(self, val):
#         self.__top = Node(val, self.__top)#第一个 self.top是新介入的 节点，第二个是老节点
#
#     def pop(self):
#         if self.__top is None:
#             raise StackError("stack is None")
#         value=self.__top.val
#         self.__top=self.__top.next
#         return value
#
#     def top(self):
#         return self.__top.val


if __name__ == "__main__":
    ls = LStack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    print(ls.pop())
