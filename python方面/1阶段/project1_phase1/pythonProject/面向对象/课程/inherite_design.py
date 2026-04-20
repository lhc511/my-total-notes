"""
    继承————设计
"""

"""定义 多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果；"""
class Vehicle:
    """
        交通工具
        隔离子类变化
    """

    def transport(self, str_transport):
        # 因父类太过抽象，写不出方法体
        pass


class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, vehicle, str_position):
        # 调用的是交通工具的运输方法
        # 多态调用父，执行子
        # 执行的是飞机运输或者汽车运输的方法
        vehicle.transport(str_position)


class Car(Vehicle):
    def transport(self, str_position):
        print("汽车开到", str_position)


class Airplane(Vehicle):
    def transport(self, str_position):
        print("飞机飞到", str_position)


p01 = Person("老张")
c01 = Car()
a01 = Airplane()
p01.go_to(c01, "东北")
p01.go_to(a01, "东北")
