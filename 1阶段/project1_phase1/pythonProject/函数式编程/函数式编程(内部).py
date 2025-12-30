"""
    函数式编程
"""
# 生成器缺点：获取结果不灵活（不要能通过索引，切片获取数据）

# def fun01():
#     print("fun01执行喽")
#
#
# # 调用方法，执行方法体
# re = fun01
# print(re)
# # 将函数赋值给变量
# re2 = fun01
# # 通过变量，调用函数
# re()
#
#
# def fun02():
#     print("fun02执行喽")
#     # 将函数作为函数的参数进行传递
#
#
# def fun03(func):
#     print("fun03执行喽")
#     func()
#
#
# fun03(fun01)
# fun03(fun02)

list01 = [43, 4, 5, 5, 6, 7, 87]

# 需求1:在列表中查找所有偶数
# #需求2:在列表中查找所有大于10的数
# #需求3:在列表中查找所有范围在10--50之间的数
# #1.使用生成器函数实现以上3个需求
# #2.体会函数式编程的"封装"
# 将三个函数变化点提取到另外三个函数中， 中将共性提取到另外一个函数中
# #3.体会函数式编程的"继承"与"多态"
# 使用变量隔离变化点，在共性函数中调用变量.
# #3.测试(执行上迹功能)
#
# def fun01(item):
#     return item % 2 == 0
#
#
# def fun02(item):
#     return item > 10
#
#
# def fun03(item):
#     return 10 < item < 50
#
#
# def find(func_condition):
#     for item in list01:
#         # "多态" #调用:具体条件的抽象#执行:具体条件的函数
#         if func_condition(item):
#             yield item
#
#
# for item in find(fun02):
#     print(item)
# 方法参数，如果传递10/"无忌"/True,叫做传递数据
# 方法参数，如果函数1/函数2/函数3，叫做传递逻辑

"""
3. 定义敌人类(姓名，攻击力，防御力，血量) 
创建敌人列表，使用1ist_helper实现下列功能. 
(1)查找姓名是"灭霸"的敌人
(2)查找攻击力大于10的所有敌人
(3)查找活的敌人数量 
4.在list helper中增加判断是否存在某个对象的方法，返回值:tru 案例1:判断敌人列表中是否存在"成昆" 
案例2:判断敌人列表中是否攻击力小于5或者防御力小于10的敌人步骤: 
实现每个需求/单独封装变化/定义不变的函数("继承"/"多态") 将不变的函数提取到List helper.py中体会:函数式编程的思想("封装，继承，多态")"""


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

    def add(self, target_enemy):
        self.enemy_list.append(target_enemy)

    @staticmethod
    def find(fun):
        for item in control.enemy_list:
            if fun(item):
                # if lambda item: item == "灭霸":
                yield item

    @staticmethod
    def find02(fun):
        for item in control.enemy_list:
            if fun(item):
                # if lambda item: item == "灭霸":
                yield fun(item)

    @staticmethod
    def condition01(item):
        return item.name == "灭霸"

    @staticmethod
    def condition02(item):
        return item.atk > 10


control = EnemyController()
e01 = Enemy("成昆", 20, 50, 100)
e02 = Enemy("灭霸", 1, 5, 10)
e03 = Enemy("昆", 3, 5, 0)
control.add(e01)
control.add(e02)
control.add(e03)

re = control.find(control.condition01)
re01 = control.find(lambda item: item.name == "灭霸")  # 其实是将 lambda匿名参数 后面的 表达式 以 函数参数 形式返还给 生成器
for i in re:
    print(i.name)
for i in re01:
    print(i.name)

# def condition03(item):
#     return item == "灭霸"
#
#
# def condition04(item):
#     return item == "灭霸"


# 生成器-->惰性操作
# 优势:节省内存
# 缺点:获取结果不灵活(不能使用索引/切片访问结果)
# 解决:情性操作-->立即操作
# generator = find(condition01)

# 生成器方法
# generator = find(condition02)
# generator_judge = find02(condition01)
# for c in generator_judge:
#     print(c)
# for b in generator:
#     print(b)

# 列表方法
# list_result = list(generator)  # 将原本生成器中的值全部转化到一个列表当中
# for a in list_result[:2]:
#     print(a)
