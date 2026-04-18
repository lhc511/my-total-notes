class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def go_to(self, str_position, type):
        # print(self.name, "去", str_position)
        type.run(str_position)


class Car:
    def run(self, str_position):
        print("行驶到", str_position)


lz = Person("老张")
car = Car()
lz.go_to("东北", car)

"""练习：小明在银行取钱"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):  # 读取
        return self.__name

    @name.setter
    def name(self, value):  # 写入
        self.__name = value

    def go_to(self, str_position, type):
        # print(self.name, "去", str_position)
        type.gain_money(str_position)


class Place:
    @staticmethod
    def gain_money(str_position):
        print("行驶到", str_position)


lz = Person("小名")  # 给类中的对象给予名字
bank = Place()
lz.go_to("银行", bank)
