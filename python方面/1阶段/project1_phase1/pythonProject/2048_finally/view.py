import controller
from module import DirectionModule
import random
from module import Location

"""老师的"""


# class GameConsoleView:
#     def __init__(self):
#         self.control = controller.Controller_Game()
#     def main(self):
#         self.start()
#         self.up_date()
#     def start(self):
#         # 产生两个数字
#         self.control.generate_new_number()
#         self.control.generate_new_number()  # 绘制界面pass
#         self.draw_map()
#
#     def draw_map(self):
#         for line in self.control.list_map:
#             for item in line:
#                 print(item, end="")
#             print()
#     def up_date(self):

"""自己的"""
# class ViewManage:
#     def __init__(self):
#         self.__manage = self.control.self.control_Game()  # 创建类的对象
#
#     def main(self):
#         self.view_screen()
#         self.view_selection()
#
#     @staticmethod
#     def view_screen():
#         print("输入a则向左移动")
#         print("输入w则向上移动")
#         print("输入s则向下移动")
#         print("输入d则向右移动")
#         print("输入0则退出")
#
#     def view_selection(self):
#         print("初始列表为如下")
#         self.__manage.generate_new_number()
#         self.__manage.print_list()
#
#         while True:
#             direction = input("请输入方向")
#             if direction == "a":
#                 self.__manage.move_left()  # move_left是一个实例方法，所以应该创建一个对象调用，见 __init__()
#                 self.__manage.generate_new_number()
#                 self.__manage.print_list()
#             if direction == "s":
#                 self.__manage.move_down()
#                 self.__manage.generate_new_number()
#                 self.__manage.print_list()
#             if direction == "d":
#                 self.__manage.move_right()
#                 self.__manage.generate_new_number()
#                 self.__manage.print_list()
#             if direction == "w":
#                 self.__manage.move_up()
#                 self.__manage.generate_new_number()
#                 self.__manage.print_list()
#             if direction == "0":
#                 break
