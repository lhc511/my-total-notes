"""集合"""  # 无序的，类似于字典中只有键
# 创建一个集合
# set_01 = set()
# set01 = set("abcba")
# set02 = {"a", "b", "c", "c"}
#
# print(set_01)
# print(set01)  # {'b', 'a', 'c'} {'c', 'a', 'b'}。。。 集合会自动去掉其中重复的值
# print(set02)  # {'b', 'a', 'c'} {'c', 'a', 'b'}。。。 集合会自动去掉其中重复的值
# # # 变为字符串
# list01 = list(set01)
# str01 = "".join(list01)  # 将列表元素合成一个字符串，并加入双引号之间的符号，若无符号则不添加
# print(str01)  # cab acb。。。顺序随机
# str02 = " ".join(list01)
# print(str02)  # a b c 顺序随机
# 增加
# set02={"a","b","c"}
# set02.add("sss")
# print(set02)#{'a', 'c', 'sss', 'b'} {'sss', 'b', 'a', 'c'}...结果也是随机的
# #删除
# set02.remove("a")
# print(set02)#{'sss', 'b', 'c'}...随机结果
# #获取所有元素
# for item in set02:
#     print(item)#随机

"""数学运算"""
# set01 = {1, 2, 3}
# set02 = {2, 3, 4}
# # 交集
# print(set01 & set02)  # [2,3]
# # #并集
# print(set01 | set02)  # {1, 2,3,4}
# # #补集
# print(set01 ^ set02)  # {1,4}
# # 子集
# set03 = {1, 2}
# print(set03 < set01)
# # #超集
# print(set01 > set03)

"""练习1:在控制台中循环录入字符串，输入空字符停止，打印所有不重复的文字"""
# set01 = set()
# while True:
#     str01 = input("请输入字符串：")
#     if str01 == "":
#         break
#     set01.add(str01)
# print(set01)
"""练习2:"""
# 经理:曹操，刘备，孙权
# 技术:曹操，刘备，张飞，关羽
# 请计算:
# (1)是经理也是技术的有谁？
# (2)是经理，不是技术的有谁？
# (3)是技术，不是经理的有谁？
# (4)张飞是经理吗？
# (5)身兼一职的都有谁？
# (6)经理和技术总共有都少人？
# set_manager={"曹操","孙权","刘备"}
# set_tech={"曹操","刘备","张飞","关羽"}
#
# print("是经理也是技术的有："+str(set_manager & set_tech))
#
# print("是经理不是技术的有："+str(set_manager-(set_manager & set_tech)))
# print("不是经理是技术的有："+str(set_tech-(set_manager & set_tech)))
# print("张飞是经理吗："+str("张飞" in set_manager) )
# print("身兼一职的都有谁："+str(set_manager^set_tech))
# print("经理和技术总共有%d人："%len(set_tech|set_manager))

"""固定集合"""  # 无法改变的，已分配好 不会再随机顺序
# set01 = frozenset([1, 2, 3, 4, 5, 2])
# list02 = list(set01)
# print(set01)  # frozenset({1, 2, 3, 4, 5})
# print(list02)  # [1, 2, 3, 4, 5]
