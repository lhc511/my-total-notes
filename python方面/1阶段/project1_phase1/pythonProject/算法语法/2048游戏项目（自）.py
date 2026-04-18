list_map = [[2, 0, 0, 2],
            [2, 0, 0, 2],
            [2, 0, 0, 2],
            [2, 0, 0, 2], ]
list_merge = None


# 零元素移至末尾
# 方法一
def zero_move_end(list_target):
    """
        零元素移动到末尾
    """
    for item in range(len(list_target) - 1):
        for i in range(item, len(list_target) - 1):
            if list_target[i] == 0:
                list_target[i + 1], list_target[i] = list_target[i], list_target[i + 1]


def double_0_to_end():
    for item in range(len(list_map)):
        for i in range(len(list_map) - 1, -1, -1):
            if list_map[item][i] == 0:
                del list_map[item][i]
                list_map[item].append(0)


def merge_left():
    for item in range(len(list_map)):
        for i in range(len(list_map) - 1):
            if list_map[item][i] == list_map[item][i + 1]:
                list_map[item][i] += list_map[item][i + 1]
                del list_map[item][i + 1]
                list_map[item].append(0)


def move_left():
    """
        合并
    """
    # 每一行0元素移到末尾
    double_0_to_end()
    # 每一行元素合并
    merge_left()


def move_right():
    """
        向右合并
    """
    i = 0
    for line in list_map:
        global list_merge
        list_merge = line[::-1]  # 切片在原来的家畜上创建了一个新的列表，和list_map是分开的
        merge_left()
        list_map[i] = list_merge[::-1]
        i += 1


move_left()

print(list_map)
