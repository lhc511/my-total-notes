"""计算通用加法，总和攻击，血量，防御"""


class Enemy:
    def __init__(self, name, atk, defence, hp):
        self.name = name
        self.atk = atk
        self.defence = defence
        self.hp = hp

    def __str__(self):
        return f"名称:{self.name},攻击:{self.atk},防御:{self.defence},血量:{self.hp}"


class EnemyController:
    def __init__(self):
        self.enemy_list = []
        self.sum_value = 0

    def add_list(self, target_enemy):
        self.enemy_list.append(target_enemy)

    def get_name(self, fun_filter):
        list_name = []
        for item in self.enemy_list:
            list_name.append(fun_filter(item))
        yield list_name

    def find(self, fun):
        for item in self.enemy_list:
            # if lambda item: item == "灭霸":
            yield item

    def add_value(self, add_fun):
        count = 0
        for item in self.enemy_list:
            control.sum_value += add_fun(item)
            count += 1
        yield self.sum_value

    def sort_up(self, fun_sort):
        for i in range(len(self.enemy_list) - 1):
            for a in range(len(self.enemy_list) - 1):
                if fun_sort(self.enemy_list[0]) < fun_sort(self.enemy_list[i]):
                    self.enemy_list[i], self.enemy_list[a] = self.enemy_list[a], self.enemy_list[i]

    def max_value(self, fun_max):
        i = 0
        for item in self.enemy_list:
            if i < fun_max(item):
                i = fun_max(item)
        yield i
        yield self.enemy_list[0]

    def del_message(self, fun_del):
        for item in range(len(self.enemy_list) - 1):
            if fun_del(self.enemy_list[item]):
                del self.enemy_list[item]


def condition05(item):
    return item.name == "灭霸"


def condition03(item):
    return item.hp


def condition01(item):
    # if control.count == len(control.enemy_list):
    return item.hp


def condition02(item):
    return item.name


def condition04(item):
    return item.hp


control = EnemyController()
e01 = Enemy("成昆", 20, 50, 100)
e02 = Enemy("灭霸", 1, 5, 220)
e03 = Enemy("昆", 3, 5, 0)
control.add_list(e01)
control.add_list(e02)
control.add_list(e03)

# control.sort_up(condition04)
# for item in control.enemy_list:
#     print(item)
#
# re03 = control.max_value(condition03)
# for item in re03:
#     print(item)
# re = control.add_value(condition01)
# print(re)
# for a in re:
#     if a is not None:
#         print(a)
# re01 = control.get_name(condition02)
# for item in re01:
#     print(item)

control.del_message(condition05)
for item in control.enemy_list:
    print(item)
