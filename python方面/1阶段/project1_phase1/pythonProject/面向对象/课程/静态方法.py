"""静态方法"""
list01 = [["00", "01", "02", "03"],
          ["10", "11", "12", "13"],
          ["20", "21", "22", "23"]]


# 实例方法：操纵对象的变量
# 类方法，操作类的变量
# 静态方法：即不需要操纵实例变量，也不要操作类变量
class Vector2:
    """
        二维向量,可以表示位置，方向
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

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
    def get_elements(target, vect_pos, vect_dir, count):  # (目标列表，二维列表的元素位置，元素方向，指定的个数)
        list_result = []
        for item in range(count):
            vect_pos.x += vect_dir.x  # 只是对数字的引用，用于下面对列表进行定位
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]  # 寻找二维列表中元素位置返还给element
            list_result.append(element)
        return list_result


pos01 = Vector2(1, 2)
l01 = Vector2.left()
pos01.x += l01.x
pos01.x += l01.y
print(pos01.x, pos01.y)