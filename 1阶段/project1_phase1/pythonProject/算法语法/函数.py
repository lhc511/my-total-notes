# 打印一维列表的函数 每个元素一行
# def list_print(list_01):
#     for item in list_01:
#         print(item)
#
#
# list01 = [1, 2, 3]
# list_print(list01)


# def list_print(list_01):
#     for item in range(len(list_01)):
#         for i in range(len(list_01[item])):
#             print(list_01[item][i],end="")
#         print()
#
# list01 = [[1, 2, 3, 44],[4, 5, 5, 5, 6, 5, 6, 87], [7, 5]]
# list_print(list01)

"""函数返回值"""
# F7：进入函数，F8不进入函数

"""输入四位数，计算每一位相加之和"""

# def each_unit_sum(number):
#     """
#         计算整数每位相加和
#     :param number: 四位整数
#     :return: 相加结果
#     """
#     result = number % 10
#     result += number // 10 % 10
#     result += number // 100 % 10
#     result + - number // 1000
#     return result
#
#
# number = int(input("请输入四位整数"))
# result = each_unit_sum(number)
# print("结果是:" + str(result))

"""练习2:定义根据两，计算几斤零几两的函数"""
# def weight(liang):
#     """
#         根据两，计算几斤零几两的函数
#     :param liang: 需要计算的两
#     :return: 元组（斤，两）
#     """
#
#     jin = weight_liang // 16
#     liang = weight_liang % 16
#     return (jin, liang)
#
#
# weight_liang = int(input("请输入两:"))
# jin, liang = weight(weight_liang)
# print(str(jin) + "斤零" + str(liang) + "两")
# print()
"""练习:定义根据成绩计算等级的函数"""
# def assess_class(score):
#     if score > 100 or score < 0:
#         return "输入有误"
#     elif 90 <= score:
#         return "优秀"
#     elif 80 < score:
#         return"良好"
#     elif 60 <= score:
#         return "及格"
#     return "不及格"
#
#
# score = int(input("请输入成绩:"))
# assess_class(score)

"""是否有相同项"""
# list01 = [3, 81, 3, 5, 51,3]
#
#
# def identify_same(list_transform):
#     """
#         用于计算列表中是否有相同的数
#     :param list_transform: 目标列表
#     :return: True(有相同项),False(无相同项)
#     """
#     for r in range(0, len(list01) - 1):
#         for c in range(r + 1, len(list01)):
#             if list01[r] == list01[c]:
#                 return True
#     return False
#
#
# consequence = identify_same(list01)
# if consequence is False:
#     print("没有相同项")
# if consequence is True:
#     print("有相同项")

"""python中不要在函数中的返回值为多种类型，遵循一个函数只实现一个功能"""
# 函数传参时分为 不可变类型 和 可变类型 数据，在函数内部分别 不可以改变 和 可以改变 源数据类型

"""#定义列表升序排列的函数"""
# list01 = [43, 4, 5, 6, 71]
#
#
# def sort_small_to_big(list_target):
#     for r in range(len(list_target) - 1):
#         for c in range(r + 1, len(list_target)):
#             if list_target[r] > list_target[c]:
#                 list_target[r], list_target[c] = list_target[c], list_target[r]
#
#
# sort_small_to_big(list01)
# print(list01)

"""方阵转置"""
# list_01 = [[1, 2, 3, 4],
#            [5, 6, 7, 8],
#            [9, 10, 11, 12],
#            [13, 14, 15, 16]]
#
#
# def transposition(list_target):
#     """
#     转置方阵
#     :param list_target:目标方阵
#     """
#     for i in range(1, len(list_target)):
#         for a in range(i, len(list_target)):
#             list_target[a][i - 1], list_target[i - 1][a] = list_target[i - 1][a], list_target[a][i - 1]
#
#
# transposition(list_01)
# print(list_01)

"""作用域"""
# 作用域:变量起作用的范围。
# 2.Local局部作用域:函数内部。
# 3. Enclosing外部嵌套作用域:函数嵌套。
# 4.Global全局作用域:模块(.py文件)内部。"
# 5. Builtin内置模块作用域:builtins.py文件。
"""global：全局变量"""
# #
# g01 = "ok"
# g02 = ""
#
#
# def fun():
#     global g02  # 用来定义全局变量
#     global g01  # 原本g01是fun函数内部的局部变量，但global使其变为全局变量，在总体上可以修改,若去掉则值不变
#     g01 = "no"
#     g02 = 250
#
#
# fun()
# print(g01)
# print(g02)
# g02 = ""
# count = 0
#
#
# def fun():
#     global g02
#     g02 = 1
#     global count
#     count += 1
#
# fun()
# fun()
# fun()
# fun()
# print(count)