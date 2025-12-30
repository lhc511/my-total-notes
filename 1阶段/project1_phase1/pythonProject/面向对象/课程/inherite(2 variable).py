# class Person:
#     def __init__(self, name):
#         self.name = name


"""
class Student(Person):
    #若子类没有构造函数则使用父类
    pass


s01 = Student()
print(s01.name)
"""

# class Student(Person):
#     子类若具有构造函数，则必须先调用父类构造函数
# def __init__(self, name, score):
#     super().__init__(name)  # super() 一个用来调用父类构造函数的函数
#     self.score = score
# p01=Person("Jisi")
# print(p01.name)
#
# s01 = Student("zhangsan", 100)
# print(s01.score)
# print(s01.name)


"""
2定义父类
车(数据:品牌，速度) 
定义子类
电动车(数据:电池容量，充电功率) 
创建两个对象
画出内存图. 
"""


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Electric_Car(Car):
    def __init__(self, brand, speed, volume, charge_power):
        super().__init__(brand, speed)

        self.volume = volume
        self.charge_power = charge_power


c01 = Car("奥迪",100)
print(c01.brand)

E01 = Electric_Car("奥迪",100,"100L","55kw/h")
print(E01.volume)