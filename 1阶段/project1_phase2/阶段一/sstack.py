# 顺序栈类
class StackError(Exception):
    pass


class SStack:
    def __init__(self):
        # 空列表就是栈的存储空间
        # #列表的最后一个元素作为栈顶
        self.__elems = []

    def is_empty(self):
        return self.__elems == []

    # 入栈
    def push(self, val):
        self.__elems.append(val)

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        # 弹出并返回
        return self.__elems.pop()  # pop函数：无输入默认返回最后一个值，有则返回相对应值

    # 查找栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self.__elems[-1]


if __name__ == "__main__":
    st = SStack()  # 初始化栈
    st.push(10)
    st.push(20)
    st.push(30)
    if not st.is_empty():
        print(st.pop())
