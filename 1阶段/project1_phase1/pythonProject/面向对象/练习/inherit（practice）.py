# class Animal:
#     def scream(self):
#         print("叫")
#
#
# class Dog(Animal):
#     def run(self):
#         print("炮")
#
#
# class Bird(Animal):
#     def fly(self):
#         print("飞")
#
#
# an1 = Animal()
# d1 = Dog()
# b1 = Bird()
# print(isinstance(d1, Dog))  # True
# print(isinstance(d1, Animal))  # True
# print(isinstance(b1, Bird))  # True
# print(isinstance(b1, Animal))  # True
#
# print(issubclass(Dog, Animal))  # True
# print(issubclass(Bird, Animal))  # True

"""
手雷炸了，可能伤害敌人/玩家的生命，
还可能伤害未知事物(鸭子，房子....) 十关注S 要求:增加了新事物，不影响手雷。
继承的作用
多态的体现设计原则
开闭原则单一职责依赖倒置画出设计图1
"""

# #############################自己
# class Damage:
#     def get_damage(self, name, dmg, target_name):
#         pass
#
#
# class Grenade:
#     def __init__(self, name):
#         self.name = name
#
#     def hurt(self, target, name_weapon, name_target, dmg):
#         target.get_damage(name_weapon, name_target, dmg)
#
#
# class Enemy(Damage):
#     def __init__(self):
#         self.name = "敌人"
#
#     def get_damage(self, name, dmg, target_name):
#         print(name, "使" + target_name + "收到了" + dmg + "伤害")
#
#
# class Player(Damage):
#     def __init__(self):
#         self.name = "玩家"
#
#     def get_damage(self, name, dmg, target_name):
#         print(name + "使" + target_name + "收到了" + dmg + "伤害")
#
#
# g01 = Grenade("手雷")
# d01 = Damage()
# e01 = Enemy()
# p01 = Player()
#
# g01.hurt(e01, g01.name, "100", e01.name)


# ##################################老师
# 多态
# class Grenade:
#     def __init__(self, atk):
#         self.atk = atk
#
#     def explode(self, damage_target):
#         print("爆炸")
#         # 调用父类代表（玩家/敌人）     多态
#         # 执行子类
#         damage_target.damage(self.atk)
#
#
# # 继承
# class Damaged:
#     """
#         受伤者
#         继承：统一多个子类概念，隔离变化
#     """
#
#     def damage(self, value):
#         pass
#
#
# # 之后都是变化点
# class Player(Damaged):
#     def __init__(self, hp):
#         self.hp = hp
#
#     def damage(self, value):
#         self.hp -= value
#         print("玩家受伤")
#         print("碎屏")
#
#
# class Enemy(Damaged):
#     def __init__(self, hp):
#         self.hp = hp
#
#     def damage(self, value):
#         self.hp -= value
#         print("敌人受伤")
#         print("显示伤害")
#
#
# g01 = Grenade(100)
# e01 = Enemy(200)
# p01 = Player(300)
# g01.explode(p01)


"""
定义图形管理器类
1.管理所有图形
2.提供计算所有图形总面积的方法
具体图形: 
圆形(pi X r ** 2) 
矩形(长*宽) 
··· 
测试: 
创建1个圆形对象，1个矩形对象，添加到图形管理器中， 
调用图形管理器的计算面积方法，输出结果。 
要求:增加新图形，不修改图形管理器的代码. 
体会:面向对象三大特征: 
封装/继承/多奥
"""

# ##########################自己
# 只能计算单个面积（失败）
# class Manage_graphic:
#     def target_graphic(self, graphic):
#         graphic.calculate_area()
#
#
# class Graphic:
#     def calculate_area(self):
#         pass
#
#
# class Circle_area:
#     def calculate_area(self):
#         r = int(input("请输入半径大小"))
#         s = 3.14 * r ** 2
#         print(s)
#
#
# class Square_area:
#     def calculate_area(self):
#         a = int(input("请输入长度"))
#         b = int(input("请输入宽度"))
#         s = a * b
#         print(s)
#
#
# m = Manage_graphic()
# c = Circle_area()
# square = Square_area()
# m.target_graphic(c)


# #########################################老师
# class GraphicManager:
#     def __init__(self):
#         self.__graphics = []
#
#     def add_graphic(self, graphic):
#         if isinstance(graphic, Graphic):
#             self.__graphics.append(graphic)
#         else:
#             raise ValueError()
#
#     def get_total_area(self):
#         total_area = 0
#         for item in self.__graphics:
#             # 多态
#             # 调用不同子类中被父类统一的函数
#             total_area += item.calculate_area()
#         return total_area
#
#
# class Graphic:  # 父类 约束所欲子类达到统一
#     def calculate_area(self):
#         pass
#
#
# class Circle(Graphic):
#     def __init__(self, r):
#         self.r = r
#
#     def calculate_area(self):
#         return 3.14 * self.r ** 2
#
#
# class Rectangle(Graphic):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def calculate_area(self):
#         return self.length * self.width
#
#
# c01 = Circle(5)
# r01 = Rectangle(10, 20)
# manage = GraphicManager()
# manage.add_graphic(c01)
# manage.add_graphic(r01)
# re = manage.get_total_area()
# print(re)

"""
定义员工管理器
管理所有员工
计算所有员工工资
员工: 
程序员:底薪+项目分红 销售:底薪+销售额
要求:增加新岗位，员工管理器不变.
"""

# class EmployeeManager:
#     def __init__(self):
#         self.list_employee=[]
#
#     def add_person(self,employee):
#         self.list_employee.append(employee)
#
#     def total_money(self):
#         total=0
#         for item in self.list_employee:
#             total=total+item.calculate_personal()
#         print(total)
#
#
# class Employee:
#     def __init__(self,salary,bonus):
#         self.salary=salary
#         self.bonus=bonus
#
#     def calculate_personal(self):
#         pass
#
#
# class Salesperson(Employee):
#     def __init__(self,salary,bonus):
#         super().__init__(salary,bonus)
#
#     def calculate_personal(self):
#         total_personal=self.salary+self.bonus
#         return total_personal
#
#
# class Programmer(Employee):
#     def __init__(self, salary, bonus):
#         super().__init__(salary, bonus)
#
#     def calculate_personal(self):
#         total_personal=self.salary+self.bonus
#         return total_personal
#
#
# s01=Salesperson(100,50)
# p01=Programmer(300,20)
# manager=EmployeeManager()
# manager.add_person(s01)
# manager.add_person(p01)
# manager.total_money()
""""""
# class Enemy:
#     def __init__(self, name, hp, atk, defen):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#         self.defen = defen
#
#     def __repr__(self):
#         return "Enemy('%s',%d,%d,%d)" % (self.name, self.hp, self.atk, self.defen)  # 里面用单引号表示字符串
#
#
# e01 = Enemy("小怪", 100, 16, 5)
# # 克隆了一个恶对象
# e02 = eval(repr(e01))
# print(e01)
# e02.name = "wddw"
# print(e02)
"""实现自定义类的减法乘法运算"""


# 对象与对象之间
# class Multiplication:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __mul__(self, other):
#         return Multiplication(self.x * other.x, self.y * other.y)
#
#     def __str__(self):
#         return f"Multiplication({self.x},{self.y})"
#
#
# m01 = Multiplication(3, 5)
# m02 = Multiplication(2, 3)
# print(m01 * m02)

# 数值与对象之间(对象在左边)
# class Multiplication:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __mul__(self, other):
#         return Multiplication(self.x * other, self.y * other)
#
#     def __str__(self):
#         return f"Multiplication({self.x},{self.y})"
#
#
# m01 = Multiplication(3, 5)
#
# print(m01 * 3)  # Multiplication(9,15)


# 数值与对象之间(对象在右边)
# class Multiplication:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __rmul__(self, other):  # 函数名的变化
#         return Multiplication(self.x * other, self.y * other)
#
#     def __str__(self):
#         return f"Multiplication({self.x},{self.y})"
#
#
# m01 = Multiplication(3, 5)
# print(3 * m01)  # Multiplication(9,15)


class Vector1:
    def __init__(self, x):
        self.x = x

    def __str__(self):  # 需要返回一个字符串
        return "一维向量的分量是i:" + str(self.x)

    def __add__(self, other):
        return Vector1(self.x + other)

    def __iadd__(self, other):#复合运算符
        return Vector1(self.x + other)


v01 = Vector1(10)
print(v01 + 2)  # vO1.add_(2)
print(id(v01))
v01 += 2
print(v01, id(v01))


# list01 = [1]
# print(id(list01))
#
# re = list01 + [2]  # 在列表中新增一个数据 [1, 2]# 生成新对象
# print(re, id(re))
# # 在原有对象基础上，累加，
# list01 += [2]
# print(list01, id(list01))

"""比较运算符"""