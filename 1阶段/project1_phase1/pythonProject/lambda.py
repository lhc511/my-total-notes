# lambda可以作为一个参数传递给其他函数
"""格式：lambda 参数:返回值（可以是一段代码，但不能给参数用等号赋值）"""

# # 无参数函数-->lambda
# def fun01():
#     return 100
#
#
# a = lambda: 100
# re = a()
# print(re)
#
#
# # 多参数函数-->lambda
# def fun02(p1, p2):
#     return p1 > p2
#
#
# b = lambda p1, p2: p1 > p2
# re = b(1, 2)
# print(re)
#
#
# # 无返回值函数-->lambda
# def fun03(p1):
#     print("参数是:", p1)
#
#
# c = lambda p1: print("参数是:", p1)
# c(100)
#
#
# def fun04(p1):
#     p1 = 2
# # 方法体只能有一条语句，且不支持赋值语句
#     d= lambda p1:p1=2
"""练习"""
# 需求1:在列表中查找所有偶数
# #需求2:在列表中查找所有大于10的数
# #需求3:在列表中查找所有范围在10--50之间的数
# #1.使用生成器函数实现以上3个需求
# #2.体会函数式编程的"封装"
# 将三个函数变化点提取到另外三个函数中， 中将共性提取到另外一个函数中
# #3.体会函数式编程的"继承"与"多态"
# 使用变量隔离变化点，在共性函数中调用变量.
# #3.测试(执行上迹功能)
list01 = [43, 4, 5, 5, 6, 7, 87]

"""示例代码
def fun01(item):
    return item % 2 == 0


def fun02(item):
    return item > 10


def fun03(item):
    return 10 < item < 50


def find(func_condition):
    for item in list01:
        # "多态" #调用:具体条件的抽象#执行:具体条件的函数
        if func_condition(item):
            yield item


for item in find(fun02):
    print(item)
"""

"""filter()函数用于过滤序列中的元素，接受一个函数和一个可迭代对象作为参数，然后根据函数的返回值是True还是False来决定是否保留元素。

"""
# 使用Lambda函数和filter()函数筛选出列表中的偶数
# numbers=[1,2,3,4,5]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # 输出: [2, 4]
