"""
    2048 游戏核心算法
"""
list_map = [[2, 4, 2, 2],
            [2, 4, 4, 2],
            [2, 0, 4, 2],
            [2, 2, 0, 2], ]

list_merge = None


def transposition():
    """
        将方阵转置
    """
    for i in range(len(list_map)):
        for a in range(i):
            list_map[i][a], list_map[a][i] = list_map[a][i], list_map[i][a]


# 零元素移至末尾
# 方法一
def zero_move_end():
    """
        零元素移动到末尾
    """

    # 方法二
    for i in range(-1, -len(list_merge) - 1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


def merge_left():
    """
        合并(一个列表)
    """

    if 0 in list_merge:
        zero_move_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


def move_left():
    """
        复合向左合并
    """
    for line in list_map:
        global list_merge
        list_merge = line
        merge_left()


# 列表中储存的是对内容的指向地址。
def move_right():
    """
        复合向右合并
    """
    for line in list_map:
        global list_merge
        list_merge = line[::-1]  # 切片在原来的家畜上创建了一个新的列表，和list_map是分开的
        merge_left()
        # 通过切片还数据会产生新列表，儿将数据给切片不会产生，将list_merge的内容交给line的最终对象，而line与list_map的最终对象是同一个
        line[::-1] = list_merge


def move_up():
    transposition()
    move_left()
    transposition()


def move_down():
    transposition()
    move_right()
    transposition()


# move_up()
move_down()
# move_right()
# move_left()
print(list_map)
