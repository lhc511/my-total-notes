"""类成员"""


# self 实例对象， cls:类方法
class ICBC:
    """
        工间银行
    """
    # 表示总行的钱
    total_money = 1000000  # 所有实例对象公用类变量。

    # 因为类方法没有对象地址self，所以不能访问实例成员
    @classmethod  # 表示之后的定义为类方法
    def print_total_money(cls):  # 类方法，用于操作  类变量
        # print(id(cls),id(ICBC))
        print("总行还剩%d钱" % ICBC.total_money)

    def __init__(self, name, money):  # 在创建对象的时候就会执行一次该函数
        self.name = name  # 实例变量
        self.money = money
    # 表示从总行中扣除当前支行使用的金额
        ICBC.total_money -= money


i01 = ICBC("广渠门支行", 100000)
i02 = ICBC("陶然亭支行", 100000)
print("总行还剩%d钱:" % ICBC.total_money)

# 通过类名访问类方法，会将类名传入类方法.
ICBC.print_total_money()
