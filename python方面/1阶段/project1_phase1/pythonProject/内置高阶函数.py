# 将函数作为参数的就叫高阶函数
# 将函数作为参数的就叫高阶函数，而python内部本身做好的就叫内置高阶函数
class Enemy:
    def __init__(self, name, atk, defence, hp):
        self.name = name
        self.atk = atk
        self.defence = defence
        self.hp = hp

    def __str__(self):
        return f"名称:{self.name},攻击:{self.atk},防御:{self.defence},血量:{self.hp}"


class EnemyController:
    def __init__(self):
        self.enemy_list = []
        self.sum_value = 0

    def add_list(self, target_enemy):
        self.enemy_list.append(target_enemy)

    def get_name(self, fun_filter):
        list_name = []
        for item in self.enemy_list:
            list_name.append(fun_filter(item))
        yield list_name

    def find(self, fun):
        for item in self.enemy_list:
            # if lambda item: item == "灭霸":
            yield item

    def add_value(self, add_fun):
        count = 0
        for item in self.enemy_list:
            control.sum_value += add_fun(item)
            count += 1
        yield self.sum_value

    def sort_up(self, fun_sort):
        for i in range(len(self.enemy_list) - 1):
            for a in range(len(self.enemy_list) - 1):
                if fun_sort(self.enemy_list[0]) < fun_sort(self.enemy_list[i]):
                    self.enemy_list[i], self.enemy_list[a] = self.enemy_list[a], self.enemy_list[i]

    def max_value(self, fun_max):
        i = 0
        for item in self.enemy_list:
            if i < fun_max(item):
                i = fun_max(item)
        yield i
        yield self.enemy_list[0]

    def del_message(self, fun_del):
        for item in range(len(self.enemy_list) - 1):
            if fun_del(self.enemy_list[item]):
                del self.enemy_list[item]


control = EnemyController()
e01 = Enemy("成昆", 200, 50, 100)
e02 = Enemy("灭霸", 1, 500, 220)
e03 = Enemy("昆", 3, 5, 0)
control.add_list(e01)
control.add_list(e02)
control.add_list(e03)

# #需求:获取所有死人I

"""filter"""
# re =filter(lambda item:item. hp==0,control.enemy_list)#（过滤条件，可迭代对象）
# for item in re:
#     print(item)
"""sort"""
# # 列表中的元素都为为数字类型
# my_list = [5, 2, 9, 1, 5, 6]
# my_list.sort()  # 默认升序排序，
# print(my_list)  # 输出: [1, 2, 5, 5, 6, 9]
#
# # 列表中的元素都为字符串类型
# words = ["apple", "orange", "banana", "pear"]
# words.sort()
# print(words)  # 输出: ['apple', 'banana', 'orange', 'pear']
#
# # 列表中的元素都为为数字类型
# my_list = [5, 2, 9, 1, 5, 6]
# my_list.sort(reverse=True)  # 降序排序，可以传递 reverse=True 参数
# print(my_list)  # 输出: [9, 6, 5, 5, 2, 1]
#
# # 列表中的元素都为字符串类型
# words = ["apple", "orange", "banana", "pear"]
# words.sort(reverse=True)
# print(words)  # 输出: ['pear', 'orange', 'banana', 'apple']

"""max"""
# # max(iterable, *[, key, default])
# #
# # max(arg1, arg2, *args[, key])
#
# print(max(1, 2, 3, 4))  # 输出4
# # 函数至少传入两个参数，但是有只传入一个参数的例外，此时参数必须为可迭代对象，返回的是可迭代对象中的最大元素。
#
#
# # print(max(1))  # 传入1个参数报错
# # TypeError: 'int' object is not iterable（不可迭代的）
# s = '12345'
#
# print(max(s))  # 5
# # 传入可迭代对象为空时，必须指定参数default，用来返回默认值输出
# print(max((), default=1))
#
# print(max(()))  # 报错 ValueError: max() arg is an empty sequence
# # 当存在多个相同的最大值时，返回的是最先出现的那个最大值。
# # 定义a、b、c 3个列表
# a = [1, 2]
# b = [1, 1]
# c = [1, 2]
#
# # 查看a、b、c 的id
# id(a)
# # 68128320
# id(b)
# # 68128680
# id(c)
# # 68128240
#
# # 取最大值
# d = max(a, b, c)
# id(d)
# # 68128320
#
#
# # 验证是否最大值是否是a
# # id(a) == id(d)#True/
# """map"""
# # # 定义一个获取数字平方的函数
# def square(number):
#     return number * number
#
#
# # 一个数字列表
# numbers = [1, 2, 3, 4, 5]
#
# # 使用map函数
# squared = map(square, numbers)
#
# # 因为map返回的是迭代器，所以我们可以用list将其转换为列表
# squared_numbers = list(squared)
#
# print(squared_numbers)
#
# numbers = [1, 2, 3, 4, 5]
#
# # 直接在map中使用lambda表达式
# squared_numbers = list(map(lambda x: x * x, numbers))
#
# print(squared_numbers)
#
# # 两个数字列表
# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
#
# # 使用map来将对应元素相加
# result = list(map(lambda x, y: x + y, numbers1, numbers2))
#
# print(result)

"""min 与max相反"""
# students = [
#     {'name': 'Alice', 'grade': 90},
#     {'name': 'Bob', 'grade': 85},
#     {'name': 'Charlie', 'grade': 95}
# ]
# best_student = min(students, key=lambda x: x['grade'])
# print(best_student['name'])  # 输出: 'Bob'

# tuple01 = ([1, 1, 1], [2, 2], [3, 3, 3,3])
# ma = max(tuple01, key=lambda item: len(item))
# print(ma)
# fi = filter(lambda ii: ii.atk > 100, control.enemy_list)
# for i in fi:
#     print(i)
re=sorted(control.enemy_list, key=lambda item: item.atk, reverse=True)
for item in re:
    print(item)
#获取数据
# po=map(lambda item:(item.name,item.atk,item.hp),control.enemy_list)
# for item in po:
#     print(item)