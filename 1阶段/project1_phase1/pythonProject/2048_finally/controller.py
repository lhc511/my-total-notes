"""
    2048 游戏核心算法
"""
from module import DirectionModule
import random
from module import Location


class Controller_Game:
    def __init__(self):
        self.__list_map = [[0, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0], ]
        self.__list_merge = None

    def print_list(self):
        for item in self.list_map:
            print(item)

    @property
    def list_map(self):  # 将这个数据设置为只读属性，即只能在别的文件中读取
        return self.__list_map

    def __transposition(self):
        """
            将方阵转置
        """
        for i in range(len(self.__list_map)):
            for a in range(i):
                self.__list_map[i][a], self.__list_map[a][i] = self.__list_map[a][i], self.__list_map[i][a]

    # 零元素移至末尾
    def __zero_move_end(self):
        """
            零元素移动到末尾
        """
        # 方法二
        # for i in range(len(self.__list_merge)):  # 若该位置元素为 0 ，则删除该元素并在末尾追加 0 元素
        #     if self.__list_merge[0] == 0:
        #         del self.__list_merge[0]
        #         self.__list_merge.append(0)
        for i in range(len(self.__list_merge) - 1, -1, -1):  # 若该位置元素为 0 ，则删除该元素并在末尾追加 0 元素
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge_left(self):
        """
            合并(一个列表)
        """

        if 0 in self.__list_merge:  # 若该位置元素为 0 ，则删除该元素并在末尾追加 0 元素
            self.__zero_move_end()
        for i in range(len(self.__list_merge) - 1):  # 0置于末尾后，从第一个元素位置逐个向后检查，若有相同则相加后付给前面的元素并删除后面的元素，最后列表末尾追加零
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)
        # for i in range(len(self.__list_merge)):  # 0置于末尾后，从第一个元素位置逐个向后检查，若有相同则相加后付给前面的元素并删除后面的元素，最后列表末尾追加零
        #     for a in range(1,len(self.__list_merge)):
        #         if self.__list_merge[i] == self.__list_merge[a]:
        #             self.__list_merge[i] += self.__list_merge[a]
        #             del self.__list_merge[a]
        #             self.__list_merge.append(0)

    def move_left(self):
        """
            复合向左合并
        """
        for line in self.__list_map:  # line 列表中的每一个 列表 元素
            self.__list_merge = line
            self.__merge_left()  # 将每一行元素都向左合并

    # 列表中储存的是对内容的指向地址。
    def move_right(self):
        """
            复合向右合并
        """
        for line in self.__list_map:  # line 总数组中的每一个小数组元素
            self.__list_merge = line[::-1]  # 切片在原来的家畜上创建了一个新的列表，和__list_map是分开的
            self.__merge_left()
            # 通过切片还数据会产生新列表，儿将数据给切片不会产生，将self.__self.__list_merge的内容交给line的最终对象，而line与__list_map的最终对象是同一个
            line[::-1] = self.__list_merge

    def move_up(self):
        self.__transposition()
        self.move_left()
        self.__transposition()

    def move_down(self):
        self.__transposition()
        self.move_right()
        self.__transposition()

    def move(self, dir):
        if dir == DirectionModule.UP:
            self.move_up()

        elif dir == DirectionModule.DOWN:
            self.move_down()

        elif dir == DirectionModule.LEFT:
            self.move_left()

        elif dir == DirectionModule.RIGHT:
            self.move_right()

    def generate_new_number(self):
        if not self.__is_game_over():
            print("游戏结束")
            return
        else:
            list_empty_location = self.__get_empty_position()  # 返回的是一个元组
            if len(list_empty_location) == 0:
                return
            loc = random.choice(list_empty_location)  # 可以在容器中直接随机取一个元素   元组中记录者空位置的二维坐标
            if random.randint(1, 10) == 1:
                self.__list_map[loc.r_index][loc.c_index] = 4
            else:
                self.__list_map[loc.r_index][loc.c_index] = 2
            self.__get_empty_position().remove(loc)
    def __get_empty_position(self):
        list_empty_location = []
        # 确定哪个空白位置1 0
        # 思路:选出所有的空白位置(行/列)，再随机挑选一个.
        for r in range(len(self.__list_map)):  # 0 123
            for c in range(len(self.__list_map[r])):
                # 记录r C -->元组
                if self.__list_map[r][c] == 0:
                    list_empty_location.append(Location(r, c))
        return list_empty_location

    def __is_game_over(self):
        result01 = self.__is_have_empty_position()
        result02 = self.__is_vertical_and_line_repeat()
        if result01 | result02 is True:
            return True
        else:
            return False

    def __is_vertical_and_line_repeat(self):
        for r in range(len(self.__list_map)):  # 0 123
            for c in range(len(self.__list_map[r]) - 1):
                # 记录r C -->元组
                if self.__list_map[c][r] == self.__list_map[c + 1][r] | self.__list_map[r][c] == self.__list_map[r][c + 1]:
                    return True

    def __is_have_empty_position(self):
        for r in range(len(self.__list_map)):  # 0 123
            for c in range(len(self.__list_map[r])):
                # 记录r C -->元组
                if self.__list_map[r][c] == 0:
                    return True

    # def __is_game_over(self):
    #     result01 = self.__is_have_empty_position()
    #     result02 = self.__is_repeat_line()
    #     result03 = self.__is_vertical_repeat()
    #     if result03 | result01 | result02 is True:
    #         return True
    #     else:
    #         return False
    #
    # def __is_vertical_repeat(self):
    #     for r in range(len(self.__list_map)):  # 0 123
    #         for c in range(len(self.__list_map[r]) - 1):
    #             # 记录r C -->元组
    #             if self.__list_map[c][r] == self.__list_map[c + 1][r]:
    #                 return True
    #
    # def __is_repeat_line(self):
    #     for r in range(len(self.__list_map)):  # 0 123
    #         for c in range(len(self.__list_map[r]) - 1):
    #             # 记录r C -->元组
    #             if self.__list_map[r][c] == self.__list_map[r][c + 1]:
    #                 return True
    #
    # def __is_have_empty_position(self):
    #     for r in range(len(self.__list_map)):  # 0 123
    #         for c in range(len(self.__list_map[r])):
    #             # 记录r C -->元组
    #             if self.__list_map[r][c] == 0:
    #                 return True


"""自己的
    def __random_list__add_num(self):
        for a in range(len(self.__list_map)):
            for b in range(len(self.__list_map)):
                if self.__list_map[a][b] == 0:
                    while True:
                        line = random.randint(0, 3)
                        arrange = random.randint(0, 3)
                        if self.__list_map[line][arrange] == 0:
                            self.__list_map[line][arrange] = self.__random_num()
                            return
                

    def __random_num(self):
        num = random.randint(1, 10)
        if num != 4:
            num = 2
        return num

    def move(self, dir):
        if dir == DirectionModule.UP:
            self.move_up()
            self.__random_list__add_num()
        elif dir == DirectionModule.DOWN:
            self.move_down()
            self.__random_list__add_num()
        elif dir == DirectionModule.LEFT:
            self.move_left()
            self.__random_list__add_num()
        elif dir == DirectionModule.RIGHT:
            self.move_right()
            self.__random_list__add_num()
"""

# 测试代码
if __name__ == "__main__":
    controller = Controller_Game()
    # controller.move left()
    # print(controller.map)
    # controller.move_down()
    # controller.move(DirectionModule.UP)

    controller.generate_new_number()
    print(controller.list_map)
    controller.move_left()
    for item in controller.list_map:
        print(item)
