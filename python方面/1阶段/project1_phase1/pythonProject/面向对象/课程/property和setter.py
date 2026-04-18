"""@property"""

# 可以使用@property装饰器来创建只读属性，@property装饰器会将方法转换为相同名称的只读属性，这样可以防止属性被修改。
# class DataSet(object):
#     @property
#     def method_with_property(self):  ##含有@property
#         return 15
#
#     def method_without_property(self):  ##不含@property
#         return 15
#
#
# obj = DataSet()
# print(obj.method_with_property)  # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加()。
# print(obj.method_without_property())  # 没有加@property , 必须使用正常的调用方法的形式，即在后面加()
"""""""""结果"""""""""""
# 15
# 15

"""@函数名称.setter。setter装饰器用来创建一个可写的属性，它必须在@property装饰器的后面，且被setter修饰的函数的名称必须与property保持一致。"""


class Adult(object):
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        print('getter() method called')
        return self._age

    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError('Sorry, you are a child, games not allowed')
        print('setter() method called')
        self._age = value


xiaoli = Adult()
xiaoli.age = 19  # 相当于写入，被setter拦截
print(xiaoli.age)  # 相当于读取，被property拦截
"""结果"""
# setter() method called
# getter() method called
# 19
