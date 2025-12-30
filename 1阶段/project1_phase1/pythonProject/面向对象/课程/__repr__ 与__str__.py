# class A(object):
#     def __init__(self):
#         pass
#
#
# a = A()
# print(a)  # 此时输出的结果,是当前的类的实例,以及对应的内存地址  <__main__.A object at 0x00000226AEF8BA00>
"""
_repr__()和__str__方法类似是 Python 类中的一个特殊方法,由 object 对象提供,该方法主要实现 "内容描述" 功能：
当直接打印类的实例化对象时，系统将会自动调用该方法，输出对象的
自我描述信息,用来告诉外界对象具有的状态信息。
"""

# class A(object):
#     def __init__(self):
#         pass
#
#     def __repr__(self):
#         return "repr"
#
#
# a = A()
# print(a)  # repr

# 示例
# class A(object):
#     def __init__(self):
#         pass
#
#     def __repr__(self):
#         return "repr"
#
#
# a = A()
# print(a)#repr

"""【_repr__ 方法 和 __str__方法同时存在】【命令行下print和直接输出的对比】"""


class A(object):
    def __repr__(self):
        return 'repr'

    def __str__(self):
        return 'str'


a = A()
# a    #直接输出调用的是repr方法
print(a)  # print调用的是str方法   str

"""命令行下直接输出对象调用的是对象的repr方法，而print输出调用的是str方法。可以看到str的优先级比repr方法要高。在没有str方法时会自动调用repr方法，
两个方法都不存在时,则继承 object 的__str__ 方法。"""