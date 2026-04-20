class Enemy:
    def __init__(self, name, HP, ATK):
        self.name = name  # 将等号后面的值赋值给前面

        self.__HP = HP

        self.__ATK = ATK
        self.set_atk(ATK)

    def set_atk(self, value):
        self.__ATK = value

    def get_atk(self):
        return self.__ATK

    def set_hp(self, value):  # 从本质上修改类中数据的值
        self.__HP = value

    def get_hp(self):  # 得到新设置的血量数据只获得)
        return self.__HP


w01 = Enemy("yaya", 100, 200)  # 将括号中的数据传递给类中的 init ,用于赋值给对象
# w01.set_hp(200)  # 给指定对象设置血量
print(w01.get_atk())  # 获得并输出对象一修改过的数据
