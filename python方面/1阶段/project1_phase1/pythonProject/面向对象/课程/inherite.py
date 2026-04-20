"""
    继承
"""

# 多个子类概念上一至，便可以抽象出一个父类概念
# 多个子类共性，可以提取到父类中
# 先有子，在有父
"""原版"""


#
class Student():
    def study(self):
        print("学习")

    def say(self):
        print("说话")


class Teacher():
    def teach(self):
        print("讲课")

    def say(self):
        print("说话")


#
#
# """改后"""
#
class Person:
    def say(self):
        print("说话")


class Student(Person):
    def study(self):
        print("学习")


class Teacher(Person):
    def teach(self):
        print("讲课")


s01 = Student()
# 子类对象可以调用子类成员，也可以调用父类成员。
s01.say()
s01.study()

p01 = Person()
# 父类对象只可以调父类成员
p01.say()

t01 = Teacher()
# 内置函数   判断对象是否属于一个类型（前者是否属于后者）
print(isinstance(t01, Teacher))  # True
print(isinstance(t01, Student))  # False
print(isinstance(t01, Person))  # True

# 内置函数   判断类型是否属于一个类型（前者是否属于后者）
print(issubclass(Student, Teacher))  # False
print(issubclass(Person, Teacher))  # False   人属于老师
print(issubclass(Student, Person))  # True    学生属于人
#
#
"""
    继承  变量
"""


class Person:
    def __init__(self, name):
        self.name = name


"""class Student(Person):
    pass


# 子类若没有构造函数，使用父类的
s01 = Student()
print(s01.name)
"""


class Student(Person):
    def __init__(self, score):
        self.score = score


s01 = Student()
print(s01.score)
print(s01.name)


# """如果子类内部写了与父类相同的函数，则父类会被重写，执行结果以子类为准"""
# class Animals(object):
#     def eat(self):
#         print('i can eat')
#
#     def call(self):
#         print('i can call phone ')
#
#
# class Dog(Animals):
#     def eat(self):
#         print(' i like eat gutouts')
#
#
# class Cat(Animals):
#     def eat(self):
#         print('i can 捉老鼠')
#
#
# wangcai = Dog()
# wangcai.eat()
# wangcai.call()
#
# miao = Cat()
# miao.eat()
# miao.call()
