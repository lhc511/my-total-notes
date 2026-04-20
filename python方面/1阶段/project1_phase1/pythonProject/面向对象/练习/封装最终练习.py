"""请用面向对象思想，描述以下场景:"""

# __slots__:限定一个类创建的实例只能有固定的实例变量

# 张无忌教赵敏九阳神功
# 赵敏教张无忌化妆
# 张无忌上班挣了10000
# 赵敏上班挣了6000

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     @property  # 拦截读取
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     def teach(self, other, skill):
#         print(self.name, "教", other.name, skill)
#
#     def work(self, money):
#         print(self.name, "上班赚了%d元" % money)
#
#
# zwj = Person("乌鸡")
# zm = Person("赵敏")
# zwj.teach(zm, "神功")
# zwj.work(1000)
# zm.work(199)
"""思考:变化点是数据的不同还是行为的不同。 请用面向对象思想，描述以下场景:"""

# 玩家攻击敌人，敌人受伤后掉血，还可能死亡(掉装备，加分)
# 敌人攻击玩家，玩家受伤后掉血/碎屏，还可能死亡(游戏结束)。
# 要想在一个类中调用另一个类，应该创建被调用类的对象，通过对象调用该类中的方法
# class Player:
#     def __init__(self, hp, atk):
#         self.hp = hp
#         self.atk = atk
#
#     def attack(self, enemy):
#         print("玩家攻击敌人")
#         # 要调用实例方法就一定要找到其对象
#         enemy.damage(self.atk)  # 将 玩家的伤害 传到 敌人收到伤害的函数 中
#
#     # 受到伤害
#     def damage(self, value):
#         self.hp -= value
#         print("玩家受伤")
#         if self.hp <= 0:
#             self.__death()
#
#     def __death(self):
#         print("玩家死亡")
#         print("游戏结束")
#
#
# class Enemy:
#     def __init__(self, hp, atk):
#         self.hp = hp  # (实例变量)
#         self.atk = atk
#
#     # 受到伤害
#     def damage(self, value):  # value是玩家的攻击力数值
#         self.hp -= value
#         print("敌人受伤")
#         if self.hp <= 0:
#             self.__death()
#
#         # 私有的死亡方法
#
#     def __death(self):
#         print("死亡")
#         print("掉装备")
#         print("加分")
#
#     def attack(self, other):
#         print("攻击玩家")
#         p01.damage(self.atk)
#
#     # 将 e01 传递给 类Player 中的 atk函数 中的 形参enemy
#
#
# p01 = Player(1000, 100)  # （血量，攻击）
# e01 = Enemy(200, 10)
# p01.attack(e01)
# e01.attack(p01)
# p01.attack(e01)
"""思考:变化点是数据的不同还是行为的不同。 请用面向对象思想，描述以下场景:"""


# 玩家攻击敌人，敌人受伤后掉血，还可能死亡(掉装备，加分)
# 敌人攻击玩家，玩家受伤后掉血/碎屏，还可能死亡(游戏结束)。
# 要想在一个类中调用另一个类，应该创建被调用类的对象，通过对象调用该类中的方法
# class Player:
#     def __init__(self, hp, atk):
#         self.atk = atk
#         self.hp = hp
#
#     # 在哪一个类中 self. 调用哪个里面的数据
#     def attack(self, enemy):
#         print("玩家攻击敌人")
#         enemy.get_damage(self.atk)
#
#     def get_damage(self, attack_value):  # 受到伤害
#         self.hp -= attack_value
#         if self.hp <= 0:
#             print("你已死亡")
#         else:
#             print("你受到伤害hp-" + str(attack_value))
#
#
# class Enemy:
#     def __init__(self, hp, atk):
#         self.atk = atk
#         self.hp = hp
#
#     def attack(self, player):
#         print("敌人攻击玩家")
#         player.get_damage(self.atk)
#
#     def get_damage(self, attack_value):
#         self.hp -= attack_value
#         if self.hp <= 0:
#             self.death_fall()
#
#     def death_fall(self):
#         print("掉经验")
#         print("掉装备")
#         print("掉道具")
#
#
# e01 = Enemy(100, 10)
# player01 = Player(1000, 50)
# player01.attack(e01)
# e01.attack(player01)