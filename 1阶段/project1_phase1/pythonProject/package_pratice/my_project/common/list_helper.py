list01 = [["00", "01", "02", "03"],
          ["10", "11", "12", "13"],
          ["20", "21", "22", "23"]]
print(list01)


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


import sys
from main import main_fun01
sys.path.append("C:\\Users\\Administrator\\Desktop\\python(学习练习)\\pythonProject\\package_pratice\\my_project")
print(sys.path)  # 文件路径
main_fun01()
