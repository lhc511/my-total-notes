"""
    新方法封装
"""


# 当只能写或者读的实时候，# age = property(None, set_age)或者另一个
# 设置一个类变量，通过property来进行读写操作，使用类中的对实例的读写函数，最终操作读写函数中的实例变量
# 当把函数作为变量赋值时会触发@xxx.setter对应的函数，    写入
# 当把函数作为变量读取时会触发@property对应的函数，      读取

class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age  # 并不是一个实例数据，是一个类变量   原本写为一个函数，但是看起来不好，所以变为如下方式
        self.weight = weight

    @property  # 创建property对象。但是只负责拦截读取
    def age(self):
        return self.__age  # 前面加__是指被隐藏的数据

    @age.setter  # 只负责拦截写入操作
    def age(self, value):
        if 21 <= value <= 31:
            self.__age = value  # self.__age是实际操作的数据,是实例变量，对内__age，对外_Wife__age
        else:
            raise ValueError("我不要")  # 用来提示报错，是程序中断

    # 属性：拦截后面对类变量的草错，使其转化为一个对方法的操作
    @property
    def weight(self):
        return self.__weight  # self.__weight是实际操作的数据

    @weight.setter
    def weight(self, value):
        if 50 <= value <= 80:
            self.__weight = value  # (实际背操作的实例变量)
        else:
            raise ValueError("我不要")  # 用来提示报错，是程序中断


w01 = Wife("铁锤公主", 25, 50)
print(w01.age)  # _Wife__age（被操纵的实例变量）
print(w01.weight)  # _Wife__weight（被操纵的实例变量）

print(w01.__dict__)  # 打印类中的实例数据（实例数据在内存中以字典形式储存）

# age = property(None, set_age)   只写
# age = property(get_age, None)   只读
