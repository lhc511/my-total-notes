list01 = [["00", "01", "02", "03"],
          ["10", "11", "12", "13"],
          ["20", "21", "22", "23"]]


# 在二维列表中，获取13位置，向左3个元素
# 在二维列表中，获取22位置，向上2个元素
# 在二维列表中，获取03位置，

class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 表示上边方向
    @staticmethod  # 静态方法，将函数移到类中
    def up():
        return Vector2(-1, 0)  # 行索引不变，行索引-1   一个对象，可以对其进行引用

    # 表示向下方向
    @staticmethod
    def down():
        return Vector2(1, 0)  # 行索引不变，行索引+1

    # 表示左边方向
    @staticmethod  # 静态方法，将函数移到类中
    def left():
        return Vector2(0, -1)  # 行索引不变，列索引-1   一个对象，可以对其进行引用

    # 表示向右方向
    @staticmethod
    def right():
        return Vector2(0, 1)  # 行索引不变，列索引+1


class Double_list_helper:
    # # 获取指定位置，指定方向，指定数量的元素
    @staticmethod
    def get_elements_ud(target, vect_pos, vect_dir, count):  # (目标列表，二维列表的元素位置，元素方向，指定的个数)
        """

        :param target: 目标列表
        :param vect_pos: 二维列表的元素位置
        :param vect_dir: 元素方向
        :param count: 指定的个数
        :return: 最终列表
        """
        list_result = []
        for item in range(count):
            vect_pos.x += vect_dir.x  # 只是对数字的引用，用于下面对列表进行定位
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]  # 寻找二维列表中元素位置返还给element
            list_result.append(element)
        return list_result


le = Double_list_helper.get_elements_ud(list01, Vector2(1, 3), Vector2.left(), 3)  # 在调用函数是一定要加括号
up = Double_list_helper.get_elements_ud(list01, Vector2(2, 2), Vector2.up(), 2)
down = Double_list_helper.get_elements_ud(list01, Vector2(0, 3), Vector2.down(), 2)
print()
print(le)
print(up)
print(down)

# ['12', '11', '10']
# ['12', '02']
# ['13', '23']
