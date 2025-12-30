"""
    内置可重写函数:以双下划线开头，双下划线结尾的是系统定义的成员，我们可以在自定义类中进行重写，从而改变行为
    例：__str__:将对象变为字符串（对人友好的）
       __repr__：将对象变为字符串（解释器可以识别的）
"""

"""
_repr__()和__str__方法类似是 Python 类中的一个特殊方法,由 object 对象提供,该方法主要实现 "内容描述" 功能：
    当直接打印类的实例化对象时，系统将会自动调用该方法，输出对象的
    自我描述信息,用来告诉外界对象具有的状态信息。
"""
#
# class StudentModel:
#     def __init__(self, name="", age=0, score=0, id=0):  # 赋值必须从右向左进行赋值（在此处赋值是为了让数据有默认值，当未输入数据时其使用默认值）
#         self.name = name
#         self.age = age
#         self.score = score
#         self.id = id
#
#
#     把对象变成字符串
#     def __str__(self):
#         return f"我叫{self.name},年龄是{self.age}"
#         return "我叫%s,年龄是%d的，成绩是%d,编号是%d" % (self.name, self.age, self.score, self.id)
#
#     把对象变成字符串（返回python代码格式的字符串）
#     def __repr__(self):  # 解释器可以识别，有格式
#         return f"我叫{self.name},年龄是{self.age}"
#         return "StudentModel('%s',%d,%d,%d)" % (self.name, self.age, self.score, self.id)


# s01 = StudentModel("乌鸡", 27, 100, 101)
# str01 = str(s01)
# 原本打出的是地址,加了__str__之后变成了可读字符串
# print(str01)
# print(s01)
# str02 = repr(s01)
# print(str02)  # StudentModel('乌鸡',27,100,101)
# 根据字符串执行python代码
# re = eval("1+2*5")
# print(re)  # 11
# 克隆对象
# repr 返回python格式带字符串代码（创建对象格式的语法）
# eval根据字符串执行python代码
# s02 = eval(repr(s01))  # 由于括号内部是一个 学生对象的 字符串 表达，所以eval函数内部会执行 该 字符串 原本表达的代码
# 先转变成字符串，在根据字符串执行代码
# s02.name = "zhang"
# print(s01.name)

"""在打印中f的用法"""
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     # 重写了object.__str__
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
# p = Point(3, 4)
# print(p)  # 输出 (3, 4)，而不是默认的对象地址表示形式


# eval 函数
# 1. 基本的数学运算
#
# result = eval("1 + 1")
# print(result)  # 2
# # 2. 字符串重复
# result = eval("'+' * 5")
# print(result)  # +++++
# # 3. 将字符串转换成列表
# a = "[1, 2, 3, 4]"
# result = type(eval(a))
# print(result)  # <class 'list'>
# result = type(eval("{'name': '小夏', 'age': 30}"))
# print(result)  # <class 'dict'>
