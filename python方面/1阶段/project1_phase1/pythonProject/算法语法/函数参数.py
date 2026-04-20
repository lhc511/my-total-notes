"""函数参数"""
# 单星号元组，双星号字典

""" 实参："""
list01 = ["a", "b", "c", "d"]
dict01 = {"a": 1, "b": 2, "c": 3, "d": 4}


def fun(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


#
#
# fun(d=1, a=3, b=2, c=4)  # 3,2,4,1  关键字实参
# fun(1, 2, 3, 4)  # 1,2,3,4    位置实参
# fun(list01)#报错

# fun(*list01)#*将序列拆分后按位置与形参进行对应    a,b,c,d
# *的作用是将tuple或者list中的元素进行unpack，分开传入，作为多个参数。
# def func(a,b,c)
# 	print(a,b,c)
#
# alist = [1,2,3] # 这里alist的长度必须和函数中参数的个数相同，否则会报错
# func(*alist) 	# 等同于 func(1, 2, 3)
#
# 1 2 3


# fun(*dict01)  # a,b,c,d  一个*分割 键 后按位置与形参进行对应（传递键）


# **的作用是unpack字典，并将字典中的 数据 项作为 键值参数 传给函数。（键指向的数据）
# def func(a, b, c):
#     print(a, b, c)
#
#
# if __name__ == "__main__":
#     dic = {'b': 2, 'c': 3}
#     func(1, b=2, c=3) # 将2,3的数据作为参数传递给函数
#     func(1, **dic) # 将键中 2,3 的数据作为参数传递给函数中参数的对应位置 b,c 上(字典中的值)
#
# 结果
# 1
# 2
# 3

# 1
# 2
# 3
# fun(**dict01)  # 1,2,3,4  **分割值后按位置与形参进行对应

#
""" 形参："""
# 缺省(默认)参数:如果实参不提供，可以使用默认值.   具有默认值的参数就叫做缺省参数
# 默认参数是指当函数被调用时未给某些参数赋值，则这些参数会自动采用预先设定好的默认值。这使得函数更加灵活，减少了强制性的输入需求。
# def fun01(a=0, b=0, c=0, d=0):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#

# 结果为0,2，3,0

# 关键字实参+缺省形参:调用者可以随意传递参数，
# fun01(b=2, c=3)

"""练习:定义函数，根据小时，分钟，秒，计算总秒数，"""
# 要求:可以只计算小时--秒
# 可以只计算分钟-->秒
# 可以只计算小时+分钟-->秒
# hour = int(input("请输入小时"))
# minint = int(input("请输入分钟"))
# second = int(input("请输入秒钟"))
#
#
# def sum_second(hour_=0, minint_=0, second_=0):
#     """
#     获取一共多少秒
#     :param hour_: 小时
#     :param minint_:分钟
#     :param second_: 秒钟
#     :return: 总秒数
#     """
#     hour_ = second_ * 3600
#     minint_ = second_ * 60
#     second_ += hour_ + minint_
#     return second_
#
# print(sum_second())

"""星号元组形参，* 将所有实参合并为一个元组   作用：让实参数无限个"""

# def fun03(*args):  # 一般元组作参数时用 *args 来写
#     print(args)
#
#
# fun03()  # ()
# fun03(1)  # (1,)
# fun03(1, "2")  # (1,'2')

""""""

# 命名关键字形参:在星号元组形参以后的位置形参
# 目的:要求实参必须使用关键字实参，
# def fun04(a, *args, b):
#     print(a)
#     print(args)
#     print(b)
#
#
# fun04(1, b=2)  # a=1  args=()  b=2
# fun04(1, 2, 3, 4, b=2)  # a=1  args=(2, 3, 4)  b=2

"""字典形参"""

# 双星号实参字典：将实参合并为字典。 填kwargs
# 实参可以传递数量无限的关键字实参
# def fun04(**kwargs):
#     print(kwargs)
#
#
# fun04(a=1, b=2)  # {'a': 1, 'b': 2}


"""调用就好"""
"""顺序：位置形参，星号元组形参，命名关键字形参，双星浩字典形参"""
# def fun01(a, b, *args, c, d, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(c)
#     print(d)
#     print(kwargs)
#
#
# fun01(1, 2, 3, 4, 5, c=1, d=10,e=99, x=5)

"""字符串: "校 训:自  强不息、厚德载物。"""
# 查找空格的数量删除字符串前后空格
# 删除字符串所有空格9
# 查找"载物"的位置
# 判断字符串是否以"校训"开头.
# str01 = "校 训:自  强不息、厚德载物。"
# count = 0

""" 删除空格"""

# def delete_blank(str_target):
#     """
#         删除空格
#     :param str_target:目标字符串
#     :return: 删除空格后的字符串
#     """
#     global count
#     count = 0
#     list01 = list(str_target)
#     for item in range(len(list01) - 1, 0, -1):
#         if list01[item] == " ":
#             count += 1
#             for i in range(item + 1, len(list01) - 1):
#                 list01[i - 1] = list01[i]
#     str_target = "".join(list01)
#     return str_target


"""删除在后方重复的字符"""

# def delete_repeat_end(str_target):
#     """
#         删除在后方重复的字符
#     :param str_target:目标字符串
#     :return: 删除重复字符后的字符串
#     """
#     list01 = list(str_target)
#     for item in range(len(list01) - 1, 0, -1):
#         for i in range(item - 1, 0, -1):
#             if list01[item] == list01[i]:
#                 del list01[i]  # 在删除之后内部的数据就已经减少
#                 # print(list01)
#     str_target = "".join(list01)
#     return str_target
#
#
# str_income = delete_blank(str01)
# str_end = delete_repeat_end(str_income)
# print(str_income)
# print(str_end)
# print(count)

""" 4.定义函数，计算指定范围内的素数"""

# def seek_prime_number(deliver_number):
#     """
#         一个数字是否为素数
#     :param deliver_number: 要判断的数字
#     :return: 布尔函数
#     """
#     for item in range(2, deliver_number):
#         if deliver_number % item == 0:
#             return True
#         else:
#             return False
#
#
# number = int(input("请输入数字"))
# result = seek_prime_number(number)
# if result is True:
#     print("不是素数")
# if result is False:
#     print("是素数")

# def get_prime(begin, end):
#     list_result = []
#     for number in range(begin, end):
#         #判断素数   ctrl+alt+m ： 生成函数
#         is_prime(number)
#     return list_result
#
#
# def is_prime(number):
#     for item in range(2, number):
#         if number % item == 0:
#             break
#         else:
#             list_result.append(number)
#
#
# print(get_prime(5, 30))
