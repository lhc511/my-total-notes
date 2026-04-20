# class Wife:


# def __init__(self, name, age, weight):
#     self.name = name
#     # 本质:障眼法(实际将变量名改为:_类名__age)
#     self.__age = age
#     self.set_age(age)  # 对数据进行判断
#     self.set_weight(weight)
#     self.__weight = weight
#
# def get_age(self):
#     return self.__age
#
# def set_age(self, value):
#     if 21 <= value <= 31:
#         self.__age = value
#     else:
#         raise ValueError("我不要")  # 用来提示报错，是程序中断
#
# def get_weight(self):
#     return self.__weight
#
# def set_weight(self, value):
#     if 50 <= value <= 80:
#         self.__weight = value
#     else:
#         raise ValueError("我不要")  # 用来提示报错，是程序中断


# w01 = Wife("铁锤公主", 87, 87)  # 重新创建了新实例变量(没有改变类中定义的age)
# w01.__age = 107  # 并未修改实例变量，而是创建了一个新的实例变量
# w01._Wife__age = 107  # (修改了类中定义的私有变量，修改本质)
# print(w01.name)
# print(w01.__dict__)  # python内置变量，用于存储对象的实例变量

# w01 = Wife("铁锤公主", 25, 50)
# w01.set_age(22)
# print(w01.get_age())
# w01.set_weight()
# print(w01.get_weight())


# list_01 = []
# stu = None
#
#
# class Student:
#     def __init__(self, name, grade, age, sex):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.sex = sex
#
#     @staticmethod
#     def behavior_02():
#         name = input("please write the student's name:")
#         grade = input("please write the student's grade:")
#         age = input("please write the student's age:")
#         sex = input("please write the student's sex:")
#         stu = Student(name, grade, age, sex)
#         list_01.append(stu)
#
# Student.behavior_02()
# for item in list_01:
#     print(item.name,item.grade)







# class Student_behavior:
#
#     def behavior_1(self):
#         print("%s 成绩为 %d" % (Student.name, Student.age))
#
#     @classmethod
#     def print_data(cls):
#         print()
#
#     @staticmethod
#     def print_02():
#         print()
#
#
# # a = Student()
# b = Student_behavior()
# # 实例方法调用  要先创建一个对象
# Student.behavior_02()
# b.behavior_1()
#
# # 类方法调用函数
# Student.behavior_02()  # 直接用类调用要传递 参数 对应 类中函数的self 即传递类本身
# Student_behavior.behavior_1(b)
# # 若调用的是类方法或者静态方法则不用传递参数
# Student_behavior.print_data()
# Student_behavior.print_02()
