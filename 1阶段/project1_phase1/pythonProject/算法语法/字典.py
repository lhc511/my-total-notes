"""字典"""  # 在录入与字典中原数据相同是则会修改原有的数据
# 创建
# 空
dict01 = {}
dict01 = dict()
# 默认值
dict01 = {"1": 100, "2": 200, "3": 300}  # 字符1,2,3,是建，100,200,300是值
# dict01 = dict([("a", "b"), ("c", "d")])  #a,c是建，b,d是值
# print(dict01)
# # 查找元素(若不存在则会报错)
# print(dict01["1"])  # 查找第一个dict01  100
# # 修改元素
# dict01["1"] = "bb"
# print(dict01["1"])  # bb
# # 添加                   箱单与直接加入
# dict01["e"] = "AA"
# print(dict01)  # {'1': 'bb', '2': 200, 3: 300, 'e': 'AA'}
# # 删除
# del dict01["1"]
# print(dict01)  # {'2': 200, 3: 300, 'e': 'AA'}
# # 遍历,获取建
# for key in dict01:
#     print(key)  # 2,3,e
#     print(dict01[key])  # 200,300,AA

# 遍历,获取值
# for value in dict01.values(): # 取字典中的每一个值
#     print(value)  # 200,300,AA

# 遍历,获取值与建（元祖）
# 方法一
# for item in dict01.items():  # 这里的item是将一个键和值看做一个整体（元祖），并为一个元素，在里面用索引来寻找元组中的元素
#     print(item[0])
#     print(item[1])

# 方法二：
# for k, v in dict01.items():  # a,b=(元素1，元素2)，这里与元组的赋值方法类似，k,v分别代表一个元组中的第一个元素键和第二个元素值
#     print(k)
#     print(v)

"""练习：、、控制台中循环录入商品信息（名字，价格），输入空字符则退出，逐行打印"""
# dict01 = {}
# while True:
#     stuff = input("请输入商品名字：")
#     if stuff == "":
#         break
#     price = int(input("请输入价格:"))
#     dict01[stuff] = price
#     print(dict01.items())
# for k, v in dict01.items():
#     print(k)
#     print(v)

"""练习：、、控制台中循环录入学生信息（名字，年龄，成绩，性别），输入空字符则退出，逐行打印"""
# dict_student_info = {}
# while True:
#     list_info=[]
#     student = input("请输入学生名字：")
#     if student == "":
#         break
#     while True:
#         info = input("请输入信息:")
#         if info=="":
#             break
#         list_info.append(info)
#     dict_student_info[student] = list_info
#     print(dict_student_info.items())
# for k, v in dict_student_info.items():
#     print(k)
#     print(v)

"""老师做法1.字典内嵌列表"""
# con=0
# dict_commodity_info = {}
# while True:
#     name = input("请输入姓名：")
#     if name == "":
#         break
#     age = int(input("请输入年龄"))
#     score = int(input("请输入分数"))
#     sex = input("请输入性别")
#     dict_commodity_info[name] = [age, score, sex]

# for name, list_info in dict_commodity_info.items():#in 前后分别对应键和值这一元组，因此整体才是一个元素，遍历时才加1
# print("名字是：%s,年龄是：%d，分数是：%d，性别是：%s，" % (name, list_info[0], list_info[1], list_info[2]))#可读性不好

# """老师做法2.字典内嵌字典"""
# dict_student_info = {}
# while True:
#     name = input("请输入姓名：")
#     if name == "":
#         break
#     age = int(input("请输入年龄"))
#     score = int(input("请输入分数"))
#     sex = input("请输入性别")
#     dict_student_info[name] = {"age": age, "score": score, "sex": sex}
#
# for name, dict_info in dict_student_info.items():
#     print("名字是：%s,年龄是：%d，分数是：%d，性别是：%s，" % (name, dict_info["age"], dict_info["score"], dict_info["sex"]))

"""老师做法2.列表内嵌字典"""
# 由于字典内部是无序排布的，无法用索引或者切片去寻找数据位置，因此需要将字典换成列表
# dict_student_info = {}
# list_student_info=[]
# while True:
#     name = input("请输入姓名：")
#     if name == "":
#         break
#     age = int(input("请输入年龄"))
#     score = int(input("请输入分数"))
#     sex = input("请输入性别")
#     dict_student_info = {"name":name,"age": age, "score": score, "sex": sex}
#     list_student_info.append(dict_student_info)
# for item in range(len(list_student_info)):
#     print(list_student_info[item])

"""练习：控制台同时录入多人的喜好，空字符退出,打印所有人喜好"""
# dict_hobby = {}
# list_hobby = []
# while True:
#     name = input("请输入姓名")
#     if name == "":
#         break
#     hobby = input("请输入爱好")
#     dict_hobby = {"name": name, "hobby": hobby}
#     list_hobby.append(dict_hobby)
# for item in range(len(list_hobby)):
#     print(list_hobby[item])
#
# dict_hobby = {}
# list_hobby=[]
# while True:
#     list_hobby1 = []
#     name = input("请输入姓名")
#     if name == "":
#         break
#     hobby = input("请输入爱好")
#     list_hobby1.append(hobby)
#     dict_hobby = {name:list_hobby1}
#     list_hobby.append(dict_hobby)
# for item in range(len(list_hobby)):
#     print(list_hobby[item])


"""3.将1970年到2050年中的闰年，存入列表·"""
# list_runnian=[]
# for item in range(1970,2051):
#     if item%400==0 or item%4==0 and item%100!=0:
#         list_runnian.append(item)
# print(list_runnian)


""""4.存储全国各个城市的景区与美食，在控制台中显示出来.
北京:
景区:故宫，天安门，天坛. 美食:烤鸭，豆汁，卤煮. 
四川:
景区:九寨沟，峨眉山，春熙路· 美食:火锅，串串香，兔头.
"""
# 不看
# dict_tour = {}
# while True:
#     city = input("请输入城市：")
#     if city == "":
#         break
#     dict_tour = {city: [[], []]}
#     while True:
#         scene = input("请输入景区：")
#         if scene == "":
#             break
#         dict_tour[city][0].append(scene)
#     while True:
#
#         food = input("请输入食物")
#         if food == "":
#             break
#         dict_tour[city][1].append(food)
#
# for item,value1 in dict_tour.items():
#     print( "城市为：%s 景区为：%s", "食物为：%s" % (item, dict_tour[city][0],dict_tour[city][1]))
# range(len(dict_tour))    "城市为：%s 景区为：%s", "食物为：%s" % (city, food_scene[0], food_scene[1])
"""计算一个字符串中的字符以及出现的次数. abcdefce a1 b1  C2  d1  e2 f2 """
# i=0
# str_input = input("请输入一串字符：")
# for item in range(len(str_input)):
#     appear_number=0
#     for count in range(len(str_input)):
#         if str_input[item] == str_input[count]:
#             appear_number+=1
#             i=count
#     if item <i or appear_number==1:
#         print("%s出现的次数是：%d"%(str_input[item],appear_number))

# 字典嵌套字典
# dict_01={"中国":{"江西":100}}
# print(dict_01["中国"])

"""字典推导式"""
# dict01={}
# for item in range(1,11):
#     dict01[item]=item**2
# print(dict01)
#
#
# dict02={item:item**2 for item in range(1,11)}
# print(dict02)
#
# dict03={item:item**2 for item in range(1,11) if item >5}
# print(dict03)

# 方法一
# dict_01={}
# list_01=["wj","zm","zzr"]
# for item in range(len(list_01)):
#     dict_01[list_01[item]]=len(list_01[item])
# print(dict_01)
# #方法二
# dict_01={}
# list_01=["wj","zm","zzr"]
# for item in list_01:
#     dict_01[item]=len(list_01)
# print(dict_01)

# dict_01={item:len(list_01) for item in list_01}#推导式
# print(dict_01)

# dict_02={}
# list_02=["wj","zm","zr"]
# list_03=[101,102,103]
# for item in range(len(list_02)):
#     dict_02[list_02[item]]=list_03[item]
# print(dict_02)
