"""方法一"""
# import double_list_helper  # 会将导入文件中的代码执行一遍
#
# e_list01 = double_list_helper.list01  # 将定义文件中的list01调用并赋值给 e_list01
# print(e_list01)
#
# v = double_list_helper.Vector2
# d = double_list_helper.Double_list_helper
#
# # 在二维列表中，获取13位置，向左3个元素
# e = d.get_elements_ud(e_list01, v(1, 3), v.left(), 3)
# print(e)
# up = d.get_elements_ud(e_list01, v(2, 2), v.up(), 2)
# print(up)
# down = d.get_elements_ud(e_list01, v(0, 3), v.down(), 2)
# print(down)

"""方法二"""
from double_list_helper import Vector2
from double_list_helper import Double_list_helper
from double_list_helper import list01

le = Double_list_helper.get_elements_ud(list01, Vector2(1, 3), Vector2.left(), 3)  # 在调用函数是一定要加括号
up = Double_list_helper.get_elements_ud(list01, Vector2(2, 2), Vector2.up(), 2)
down = Double_list_helper.get_elements_ud(list01, Vector2(0, 3), Vector2.down(), 2)
print()
print(le)
print(up)
print(down)