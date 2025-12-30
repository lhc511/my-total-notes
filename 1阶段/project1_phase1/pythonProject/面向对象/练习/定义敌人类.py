# 实例方法：操纵对象的变量(操纵该类中的数据)
# 类方法，操作类的变量
# 静态方法：即不需要操纵实例变量，也不要操作类变量
"""定义敌人类"""


# 实例成员，行为直接定义就好，类成员，行为则需要@的前缀，类变量则在类中直接定义

# 数据:姓名，血量，基础攻击力，防御力
# 行为:打印个人信息
# 创建敌人列表(至少4个元素)，并画出内存图。
# 查找姓名是"灭霸"的敌人对象
# 查找所有死亡的敌人
# 计算所有敌人的平均攻击力
# 删除防御力小于10的敌人
# 将所有敌人攻击力增加50
class Enemy:
    def __init__(self, name, HP, ATK, DEF):
        self.name = name

        self.HP = HP
        self.set_hp(HP)

        self.ATK = ATK
        self.set_atk(ATK)

        self.DEF = DEF

    def print_self_info(self):
        print("敌人的名字是:%s,血量是%d:,攻击力是：%d,防御力是：%d" % (self.name, self.HP, self.ATK, self.DEF))

    def set_atk(self, value):
        if 10 <= value <= 50:
            self.ATK = value
        else:
            raise ValueError("越界")  # 用来提示报错，是程序中断

    def set_hp(self, value):
        if 100 <= value <= 200:
            self.HP = value
        else:
            raise ValueError("越界")  # 用来提示报错，是程序中断


class Check_data:
    @staticmethod
    def check_name():
        for item01 in range(len(list_enemy)):
            if list_enemy[item01].name == "灭霸":
                return list_enemy[item01]

    @staticmethod
    def check_dead():
        list_dead = []
        for item02 in range(len(list_enemy)):
            if list_enemy[item02].HP == 0:
                list_dead.append(list_enemy[item02])
                return list_dead  # 相当于直接返回对象

    @staticmethod
    def calculate_average_attack():
        i = 0
        for item03 in range(len(list_enemy)):
            i += list_enemy[item03].ATK
        return str(i / len(list_enemy))

    @staticmethod
    def def_lower_10():
        for item04 in range(len(list_enemy)):
            if list_enemy[item04].DEF < 10:
                del list_enemy[item04]

    @staticmethod
    def enhance_atk_50():
        for item05 in list_enemy:
            item05.ATK = item05.ATK + 50


class Judge:
    @staticmethod
    def is_dead():
        death = Check_data.check_dead()
        if death is not None:
            print(death)
        else:
            print("无死亡敌人")


Enemy01 = Enemy("灭霸", 150, 10, 10000)
Enemy02 = Enemy("奥特曼", 130, 10, 400)
Enemy03 = Enemy("怪兽", 170, 25, 500)
Enemy04 = Enemy("马克", 160, 40, 6)
list_enemy = [Enemy01, Enemy02, Enemy03, Enemy04]

Check_data.check_name().print_self_info()  # 相当于 对象.实例方法

Judge.is_dead()
print("敌人的平均攻击力是" + Check_data.calculate_average_attack())

Check_data.def_lower_10()
for item in list_enemy:
    Enemy.print_self_info(item)

Check_data.enhance_atk_50()
for item in list_enemy:
    Enemy.print_self_info(item)
