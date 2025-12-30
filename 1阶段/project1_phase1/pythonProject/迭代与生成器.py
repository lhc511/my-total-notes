"""
    可迭代对象
"""
#惰性操作。可延迟操作

# yield返回值后会暂停在某处,下次会接着在该位置继续执行
# 可迭代对象----容器
# list01 = [43, 3, 4, 5, 567]
# 迭代过程
# for item in list01:
#     print(list01)
# 迭代原理
# 面试题：for循环的原理是什么
# 1.获取迭代器
# 2.循环获取写一个元素
# 3.遇到异常停止迭代

# 可以被for的条件是什么
#   具备__iter__()
#
# 1.获取迭代器
# iterator = list01.__iter__()
# 2.循环获取写一个元素
# while True:


#     try:
#         item = iterator.__next__()
#         print(item)
#     except:
#         break
# 3.遇到异常停止迭代


# 练习1:使用迭代器原理，遍历元组. #("铁扇公主"，"铁锤公主"，“扳手王子")
# #练习2:不使用for ,获取字典所有数据。
# {“铁扇公主":101,"铁锤公主":,“扳手王子”}
# tuple01=("铁扇公主","铁锤公主","扳手王子")
# dict01={"铁扇公主","铁锤公主","扳手王子"}
# iter_tuple01=tuple01.__iter__()
# iter_dict01=dict01.__iter__()
# while True:
#     try:
#         tuple_item=iter_tuple01.__next__()
#         print(tuple_item)
#         dict_item=iter_dict01.__next__()
#         print(dict_item)
#     except:
#         break

"""迭代器"""
# 在使用迭代器时，内部或自定的可迭代对象会根据需求获取一个值并在获取后丢弃，可以避免因数值过大而内存不够
# class Skill:
#     pass
#
#
# class SkillIterator:
#     def __init__(self, target):
#         self.__target = target
#         self.__index = 0
#
#     def __next__(self):
#         if self.__index > len(self.__target) - 1:
#             raise StopIteration
#         # 返回下一个数据
#         temp = self.__target[self.__index]
#         self.__index += 1
#         return temp
#
#
# class SkillManage:
#     def __init__(self):
#         self.skills = []
#
#     def add_skill(self, skill):
#         self.skills.append(skill)
#
#     def __iter__(self):  #迭代器需要可迭代对象
#         # 创建一个迭代器对象,并传递需要迭代的数据
#         # 列表，元组，字符串，字典等都属于可迭代对象。
#         return SkillIterator(self.skills)
#
#
# manager = SkillManage()
# manager.add_skill(Skill())
# manager.add_skill(Skill())
# manager.add_skill(Skill())
#
# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except:
#         break


# 练习
# class GraphicIterator:
#     def __init__(self, target):
#         self.target = target
#         self.index = 0
#
#     def __next__(self):
#         if self.index > len(self.target) - 1:
#             raise StopIteration
#         temp = self.target[self.index]
#         self.index += 1
#         return temp
#
#
# class GraphicManager:
#     def __init__(self):
#         self.__graphics = []
#
#     def add_graphic(self, graphic):
#         if isinstance(graphic, Graphic):
#             self.__graphics.append(graphic)
#         else:
#             raise ValueError()
#
#     def __iter__(self):
#         return GraphicIterator(self.__graphics)
#
#
# class Graphic:  # 父类 约束所欲子类达到统一
#     def calculate_area(self):
#         pass
#
#
# manager = GraphicManager()
# manager.add_graphic(Graphic())
# manager.add_graphic(Graphic())
# manager.add_graphic(Graphic())
#
# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except:
#         pass

# if __name__ == "__main__":
#     c01 = Circle(5)
#     r01 = Rectangle(10, 20)
#     manage = GraphicManager()
#     manage.add_graphic(c01)
#     manage.add_graphic(r01)
#     re = manage.get_total_area()
#     print(re)


"""定义range类，并实现功能"""

# for item in range(10):
#     print(item)

# class NumberIterator:
#     def __init__(self, target):
#         self.target = target
#         self.count = 0
#
#     def __next__(self):
#         if self.count == self.target:
#             raise StopIteration
#         temp = self.count
#         self.count += 1
#         return temp
#
# class MyRange:
#     def __init__(self, number):
#         self.number = number
#
#     def __iter__(self):
#         return NumberIterator(self.number)
#
#
# mr = MyRange(10)
# # for item in mr:
# #     print(item)
# iterator = mr.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except:
#         break
# 错误
# while True:
#     try:
#         item = mr.__iter__().__next__()
#         print(item)
#     except:
#         break
"""过渡"""

# class NumberIterator:
#     def __init__(self, target):
#         self.target = target
#         self.count = 0
#
#     def __next__(self):
#         if self.count == self.target:
#             raise StopIteration
#         temp = self.count
#         self.count += 1
#         return temp


# class MyRange:
#     def __init__(self, end_num):
#         self.end_num = end_num
#
#     def __iter__(self):
#         # return NumberIterator(self.number)
#         number = 0
#         while number < self.end_num:
#             # yield坐用将下列代码改成迭代器模式的代码
#             # 生成迭代器代码大致规则：将yield以前的代码定义在next方法中
#             # 将yield中的数据作为next方法的返回值
#             yield number
#             number += 1 #该行代码作为下一个 yield 以前的代码定义到next方法中


#
# mr= MyRange(10)
# iterator = mr.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except:
#         break
# for item in MyRange(10):
#     print(item)

# class Graphic:
#     pass
#
#
# class GraphicManager:
#     def __init__(self):
#         self.__graphics = []
#         self.index = 0
#
#     def add_graphic(self, graphic):
#         if isinstance(graphic, Graphic):
#             self.__graphics.append(graphic)
#         else:
#             raise ValueError()
#
#     def __iter__(self):
#         num = 0
#         while num < len(self.__graphics) - 1:
#             yield self.__graphics[num]
#             num += 1

# list01 = [4, 5, 566, 7, 8, 10]
#
# list_target = []
#
#
# # for item in list01:
# #     if item % 2 == 0:
# #         list_target.append(item)
# # print(list_target)
# def __iter__(target_list):
#     num = 0
#     while num < len(list01):
#         yield target_list[num]
#         num += 1
#
#
# list02 = []
# list_target.append(__iter__(list01))

"""练习:定生成器函数my_enumerate,实现下列现象. 
将元素与索引合成一个元组
"""
# list01 = [3, 4, 55, 6, 71]


# for item in enumerate(list01):
#     # (索引，元素)
#     print(item)
# for index, element in enumerate(list01):
#     print(index, element)


# def my_enumerate(iterator_target):
#     index = 0
#
#     for item in iterator_target:
#         yield item, index  # yield其实是在内部创建了一个函数，执行迭代器的功能 即__next__
#         index += 1
#
#     # for item in range(len(list01)):
#     #     yield item, list01[item]
#
#
# for index, element in my_enumerate(list01):
#     print(index, element)

"""定义生成器my-zip
将多个列表每个元素合成一个元组
"""
# list01 = ["唐", "孙", "猪", "沙僧"]
# list02 = [1, 2, 3, 4]
#
#
# # for item in zip(list01, list02):
# #     print(item)
#
#
# def my_zip(*args):  # args可以不限制的传入多个参数(以数列形式储存和访问)
#     for index in range(len(args[0])):
#         list_result = []
#         # yield args[index], args[index]  # 先在生成器生成的函数（上面提到的迭代器）中返回多需要的值并立刻使用，用完之后丢弃释放内存
#         for item in args:  # 传来的迭代对象数目
#             list_result.append(item[index])  # 目标列表中的相应参数传入新列表中
#         yield list_result  # yield返回值后会暂停在某处,下次会接着在该位置继续执行
#
#
# for pos1, pos2 in my_zip(list01, list02):
#     print(pos1, pos2)
# for i in my_zip(list01, list02):
#     print(i)

"""生成器函数表达式"""
# list01=[3,"32",True,0,1.6,"70",False,0,3.2]

# def find01():
#     for item in list01:
#         if type (item)==int:
#             yield item
# a =find01()
# for item in a:
#     print(item)

# def find01():
#     for item in list01:
#         if type (item)==str:
#             yield item
# a=find01()
# for item in a:
#     print(item)
# g_expression=(item for item in list01 if type (item)==str)#在生成器中只取必须的元素
# for item in g_expression:
#     print(item)
#
# l_expression=[item for item in list01 if type (item)==str]#在列表表达式中会取所有元素
# for item in l_expression:
#     print(item)
#