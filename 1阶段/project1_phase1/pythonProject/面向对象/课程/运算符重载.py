"""
运算符重载
用于对象之间的加减乘除运算，并且是指定运算对象中的数据想加减
"""


class GridPoint:  # Line: 1, Declaring a class
    def __init__(self, x, y):
        self.x = x
        self.y = y  # Line: 4

    # 当我们使用'+'运算符作为数学加法运算时， __add__()方法被隐式调用。
    def __add__(self, other):  # Equivalent of + operator
        return GridPoint(self.x + other.x, self.y + other.y)

    # 当在下面打印该对象时会打印该内置函数下的返回字符串
    def __str__(self):  # Line: 12, returns the attributes when the object is printed
        string = str(self.x)
        string = string + ", " + str(self.y)
        return string  # Line: 12


point1 = GridPoint(3, 5)  # Line: 14 Creating a grid point
point2 = GridPoint(-1, 4)  # Line: 15, Creating another point
point3 = point1 + point2  # Line: 16, Add two points using __add__() method
print(point3)  # Line: 17, Print the attributes using __str__() method
