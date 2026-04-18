""" 练习:定义对象计数器。
    定义老婆类，创建3个老婆对象。
    可以通过类变量记录老婆对象个数，
    可以通过类方法打印老婆对象个数。
    要求:画出内存图. """

#当用类变量时用 类名 去寻找.
# 不管什么变量 都一定要用类名，对象名（self）来引用，才能访问到其内部变量
class Wife:
    count = 0  # 类变量

    def __init__(self, name, sex, age):  # 实例对象
        self.name = name  # 实例变量
        self.sex = sex
        self.age = age
        Wife.count += 1

    @classmethod
    def wife_count(cls):
        print("wife的个数是%d" % Wife.count)#cls.count 与 类名.count的结果是一样的（count为类变量）


w01 = Wife("lele", "women", "23")  # （每创建一个对象都会执行一次 init 对象中的函数）
w02 = Wife("lili", "women", "25")  # 一定要带类名
w03 = Wife("mimi", "women", "27")
Wife.wife_count()
