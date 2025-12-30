
"""
Python 类 __init__() 方法的作用
__init__() 是 Python 中的一个特殊方法，在创建一个新的对象实例时自动调用。此方法的主要职责是对新创建的对象进行必要的初始化操作，比如设置初始属性值
或其他准备工作1。

该方法的第一个参数总是 self，代表当前正在被处理的对象实例本身。其余参数则取决于开发者的需求来定义，用于传递给新对象的特定数据或配置选项2。

当定义一个类并希望每次实例化时都执行某些设定动作，则可以在类内部实现这个特殊的构造函数。如果未显式提供 __init__() 函数，默认情况下会有一个不带任何
额外参数（除了 self）的版本存在。

下面给出一段简单的代码示例展示如何使用 __init__() 来初始化对象：
"""

"""
self是对“对象”自身的引用。相当于c++中的this。python中self在类的方法中必须以传入参数写在函数的参数列表中。它实际上是指向类的对象的一个类似于C++中指针的私有变量。
python规定：访问类成员时，需要在前面加上self。这里，self.name = name表示为Person类添加了属性name。
如果变量前不加this，则视为局部变量。这个变量会在方法运行结束后失效。而属性在整个类的范围内都是有效的。
self是只有在类中才会有的。self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
"""

class Person:
    def __init__(self, name, age):
        self.name = name  # 设置人的名字
        self.age = age  # 设置人的年龄

    def introduce(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")


# 创建两个不同的Person对象，并传入各自的name和age作为参数
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# 调用各自的方法打印介绍信息
person1.introduce()
person2.introduce()