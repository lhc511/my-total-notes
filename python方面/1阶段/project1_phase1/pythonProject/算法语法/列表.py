"""不论是链表还是range，顺序打印开始值均大于结束值，逆序打印结束值大于开始值，否则为空"""
"""列表"""
# 创建空列表格式（二者一样）
# list01=[]
# list01=list()

# 填入默认值格式（不同）
# list02=["悟空",100,True]  #将其中的每个数据看成一个元素，可以分开       ['悟空', 100, True]
# list02 = list("我是齐天大圣")  # 将其中的一串字符单个拆分
# print(list02)  # ['我', '是', '齐', '天', '大', '圣']
# 获取元素方式（索引对字符进行单个引用，切片则是获得某一片信息）
# 1.索引
# print(list02[2])#齐
# 2.切片
# print(list02[-4:])#['齐', '天', '大', '圣']


# 3.添加元素（在末尾追加）   .append
# list02.append("八戒")
# print(list02)#['我', '是', '齐', '天', '大', '圣', '八戒']

# 插入(在元素对应位置插入)          .insert
# list02.insert(1,True)#在索引为1（第二个）位置上添加True
# print(list02)#['我', True, '是', '齐', '天', '大', '圣', '八戒']

# 删除元素   remove    del
# 1.根据元素删除删除第一个位置的元素
# list02.remove("是")
# print(list02)#['我', '齐', '天', '大', '圣']

# 根据位置删除
# print(list02)
# del list02[0]#删除该位置的元素
# print(list02)#['齐', '天', '大', '圣']

# 5.定位元素
# 切片
# list02=['我', '是', '齐', '天', '大', '圣']
# del list02[1:3]
# print(list02)#['我', '天', '大', '圣']

# 修改数据
# list02[1:3]=["a","b"]
# print(list02)#['我', 'a', 'b', '圣']
#
# list02[1:3]=[1,2,3,4,5,6]
# print(list02)#['我', 1, 2, 3, 4, 5, 6, '圣']
#
# list02[1:7]=[]
# print(list02)#['我', '圣']

"""遍历列表"""
# list02=list("我是洋")
# for item in list02:
#     print(item)#我
#                是
#                洋

# 倒序获得所有元素
# 不建议：因为会造成空间浪费（此方法会再建立一个新的列表）
# list01 = list("我是齐天大圣")
# for item in list01:
#     print(item[::-1])#我是齐天大圣（竖着 见上面）

# 5,4,3,2,1,0
# for i in range(len(list01) - 1, -1, -1):  # 从(len-1)开始，到-1的前一个数截止
#     print(i)

# -1，-2，-3，-4
# for i in range(-1, -5, -1):  # 从(len-1)开始，到-1的前一个数截止
#     print(i)

"""练习：输入西游记中喜欢的人物，输入空字符串退出，一行一个打印所有人物"""
# list_people = list()  # 创立一个列表
# while True:
#     str_input = input("请输入你喜欢的名称：")
#     if str_input == "":
#         break
#     list_people.append(str_input)
# for item in list_people:
#     print(item)

"""练习：录入所有学生成绩，空字符退出，一行一个，并打印最高，最低，平均均分"""
# list_score = []
# list_maxscore = []
# list_leastscore = []
# count = 1
# summary = 0
# average = 0
# while True:
#     score = input("请输入成绩：")
#     if score == "":
#         break
#     elif score != "":
#         list_score.append(score)
#         list_maxscore.append(score)
#         list_leastscore.append(score)
#
# for exchange_max in list_maxscore:
#     if list_maxscore[0] < list_maxscore[count - 1]:
#         list_maxscore[0] = list_maxscore[count - 1]
#     count += 1
#
# count = 1
# for exchange_least in list_leastscore:
#     if list_leastscore[0] > list_leastscore[count - 1]:
#         list_leastscore[0] = list_leastscore[count - 1]
#     count += 1
#
# for item in list_score:
#     print("学生的成绩为:%s" % item)
#
# for item in list_score:
#     item = int(item)
#     summary += item
# average = summary / len(list_score)
#
# print("最小的数为：%s" % list_leastscore[0])
# print("最大的数为：%s" % list_maxscore[0])
# print("平均值为：%.1f" % average)


"""max min 函数"""
# list_code=[]
# while True:
#     num_input=input("请输入数字：")
#     if num_input=="":
#         break
#     list_code.append(num_input)
#
# print(max(list_code))
# print(min(list_code))
# print(len(list_code))

"""录入学生姓名，若重复则提示已存在，若录入空字符串则倒序打印所有学生"""
"""in      not in:用来判断字符串中是否包含另一字符串"""
# 方法一：遍历法
# name_list = []
# while True:
#     # 准备好名单
#     name = input("请输入学生姓名：")
#     name_list.append(name)
#     forward = 0
#     # 倒序打印名单
#     if name == "":
#         # name_list.remove(" ")
#         print(name_list[-1:-len(name_list):-1])
#         break
#     # 判断名单中是否有重复
#     if len(name_list) >= 2:
#         for item in name_list:
#             if forward == len(name_list) - 1:
#                 break
#             # if item[forward] == item[len(name_list) - 1]:#item是将列表中的某个单独的元素拿出来，只有一个位置（错误）
#             if name_list[forward] == name_list[len(name_list) - 1]:
#                 print("姓名已存在")
#                 del name_list[len(name_list)-1]
#                 forward -= 1
#                 break
#             forward += 1

"in 方法"
# list_name = []
# while True:
#     name = input("请输入名称")
#     if name == "":
#         break
#     if name in list_name:  # if name not in list_name:
#         print("有重复名称")  # list_name.append(name)
#         continue
#     list_name.append(name)
#
# for item in list_name[-1:-len(list_name) - 1:-1]:
#     print(item)

""""""
# 一改均改
# list01=["张无忌","着迷"]
# list02=list01
# list02[0]="五级"
# print(list01)#['五级', '着迷']
# print(list02)#['五级', '着迷']
#
# list01=["张无忌","着迷"]
# list02=list01
# list01=["五级"]
# print(list01)#['五级']
# print(list02)#['张无忌', '着迷']


"""指向与修改"""
# list01=["张无忌","着迷"]
# list02=list01[:]#通过切片获得元素            #将list01中的地址指向拷贝到list02里面，不拷贝内容
# list01[0]="五级"                           #修改list01中的指向，使其指向新内容，并不修改原指向地址的内容
# print(list02[0])#张无忌                    #list02与list01的原地址共同指向一个内容，因此不变
# list01=500                                #修改list01指向，使其有新内容
# print(list02[0])#张无忌


# list01=[800,[1000,500]]#两个元素
# list02=list01
# list01[1][0]=900#将list01的第二个元素（列表）的第一个元素（1000）改为900
# print(list02[1][0])

# list01 = [800, [1000, 500]]  # 两个元素
# list02 = list01[:]  # 只拿其中的地址
# list01[1][0] = 900  # 将list01的第二个元素（列表）的第一个元素（1000）改为900
# print(list02[1][0])#900
#
# list01 = [800, [1000, 500]]
# # 浅拷贝
# list02 = list01[:]  # 二者等效
# list02 = list01.copy()  # 二者等效
# list01[1][0] = 900
# print(list02[1][0])#900

# 深拷贝         与C语言中的变量赋值方法相似，整体复制一份去运行（较耗费内存）
# import copy
# list01 = [800, [1000, 500]]
# list02 = copy.deepcopy(list01)  # 二者等效
# list01[1][0] = 900
# print(list02[1][0])#

"""练习：将[54，25，12，42，35，17]中大于30的数字存在另一个列表"""
# list01=[54,25,12,42,35,17]#储存的是每一个元素的地址，指向元素
# list02=[]
# for item in list01:
#     if item >30:
#         list02.append(item) #给链表中追加的是指向数字的地址，
# print(list02)


"""录入五个数字，打印最大值"""
# ####方法一
# number_sum=[]
# count=0
# while count<5:
#     add_num=input("请输入五个数字")
#     number_sum.append(add_num)
# print(max(number_sum))

# ####方法二
# number_sum = []
# count = 0
# count_sum=0
# print("请输入五个数字")
# while count < 5:
#     count += 1
#     add_num = int(input())
#     number_sum.append(add_num)
# for item in number_sum:
#     if number_sum[0] < number_sum[count_sum-1]:
#         number_sum[0] = number_sum[count_sum-1]
#     count_sum+=1
# print("最大的数字是：%d" % number_sum[0])
"""老师打的"""
# max=0
# for item in range(5):
#     num=int(input("请输入数字"))
#     if num>max:
#         max=num
# print(max)

"""练习：在[54,25,12,42,35,17]找到最大值"""
# max_num=0
# num_list=[54,25,12,42,35,17]
# for item in num_list:
#     if item>max_num:
#         max_num=item
# print(max_num)

# max_num=0
# count=0
# num_list=[54,25,12,42,35,17]
# print(max(num_list))

"""练习：在[9,25,12,8]删除大于10的数"""  # 在删除中后面的数据会覆盖前面的数据，从而导致跳过数据漏删，因此最好从后往前删数据
# list01 = [9, 25, 12, 8]
# for item in range(len(list01)-1,-1,-1):#整数生成器（生成倒序整数）
#     if list01[item] > 10:
#         list01.remove(list01[item])
# print(list01)


"""result="连接符".join(列表)
   列表="a-b-c-d".split("分隔符")"""

"""拼接字符串成0123456789"""
# 不能用字符串拼接，因为字符串不可变，每次改变是都会生成一个新的字符串  用 .append
# list_temp = []
# for item in range(10):
#     list_temp.append(str(item))
# result = "".join(list_temp)  # 用于将列表变为字符串
# print(type(result))  # type可以显示数据类型
# print(result)  # 0123456789
#
# result1 = " ".join(list_temp)  # 用于将列表变为字符串
# print(result1)  # 0 1 2 3 4 5 6 7 8 9
#
# result2 = "*".join(list_temp)  # 用于将列表变为字符串
# print(result2)  # 0*1*2*3*4*5*6*7*8*9

"""循环输入字符串，输入空则停止，打印拼接后的内容"""
# list_num = []
# while True:
#     number = input("请输入要打印的字符")
#     if number == "":
#         break
#     list_num.append(number)
# result = "".join(list_num)
# print(result)

# str01 = "11-22-33-44"
# list_result = str01.split("-")  # 字符串分割后变成列表
# print(list_result)

"""how are you --> you are how"""
# str01="how are you"
# list_str01=str01.split(" ")
# #print(list_str01[-1:-len(str01)-1:-1])
# print(list_str01[::-1])
# result=" ".join(list_str01[::-1])
# print(result)


"""练习：彩票双色球: 
    红球:6个，1--33之间的整数       不能重复7
    蓝球:1个，1--16之间的整数00 
    (1)随机产生一注彩票[6个红球1个蓝球]."""

# ball_number = []
# while len(ball_number) < 6:
#     import random
#
#     red_number = str(random.randint(1, 33))
#     if red_number in ball_number:
#         continue
#     elif red_number not in ball_number:
#         ball_number.append(red_number)

# ball_number.append(str(random.randint(1,16)))#篮球可以重复
# result_generate = " ".join(ball_number)
# print(result_generate)

# while True:
#     import random
#     blue_number = str(random.randint(1, 16))
#     if blue_number not in ball_number:
#         ball_number.append(blue_number)
#         break
#
# # 结果检测
# result_generate = " ".join(ball_number)
# print(result_generate)

"""练习：(2)在控制台中购买一注彩票u 提示: 
    "请输入第1个红球号码:" 
    "请输入第2个红球号码:" 
    "号码不在范围内" 
    "号码已经重复" 
    "请输入蓝球号码:"""
# guess_number = []
# i = 1
# while len(guess_number) < 6:
#     input_num = int(input("请输入第%d个红球号码" % i))
#
#     if input_num < 1 or input_num > 33:
#         print("号码不在范围内")
#         continue
#     elif input_num in guess_number:
#         print("号码重复请重新输入")
#         continue
#     else:
#         guess_number.append(input_num)
#         i += 1
#
# while len(guess_number) < 7:
#     input_blue_num = int(input("请输入蓝球号码"))
#
#     if input_blue_num < 1 or input_blue_num > 16:
#         print("号码不在范围内")
#         continue
#     elif input_blue_num in guess_number:
#         print("号码重复请重新输入")
#         continue
#     else:
#         guess_number.append(input_blue_num)
#         break
#
# for item in range(7):
#     guess_number[item] = str(guess_number[item])
# result_input = " ".join(guess_number)
#
# print(result_input)

"""算最小值[43,54,5,6,7,8]"""
# #方法一
# list_num=[43,54,5,6,7,8]
# print(min(list_num))
# #方法二
# min_num=list_num[0]
# for item in range(len(list_num)):
#     if min_num>list_num[item]:
#         min_num=list_num[item]
# print(min_num)

"""列表推导式"""
"""list所有元素增加1后放入list02中"""
# ##写法1
# list01 = [5, 56, 6, 7, 7, 8, 9]
# list02=[]
# for item in list01:
#     list02.append(item+1)
# print(list02)
# ##第二种写法(二者等价)
# list02=[item+1 for item in list01]
# print(list02)

# 语法：变量=[表达式 for 变量 in 可迭代对象]
#     变量=[表达式 for 变量 in 可迭代对象 if 条件]

"""list大于10元素增加1后放入list02中"""
# list02 = [item + 1 for item in list01 if item > 10]
# print(list02)

"""练习"""
# 练习:使用range生成1--10之间的数字，将数字的平方存人list01
# 将1ist01中所有奇数存入list02
# 将1ist01中所有偶数存入list03
# 将1ist01中所有偶数大于5的数字增加1后存入list04
# list01 = []
# list02 = []
# list03 = []
# list04 = []
# for item in range(1, 11):
#     list01.append(item ** 2)
# for count in range(len(list01)):
#     if list01[count] % 2 == 1:
#         list02.append(list01[count])
#     elif list01[count] % 2 == 0:
#         list03.append(list01[count])
#     if list01[count] % 2 == 0 and list01[count] > 5:
#         list04.append(list01[count] + 1)
# print(list01)
# print(list02)
# print(list03)
# print(list04)

# 合并的方法
# 语法：变量=[表达式 for 变量 in 可迭代对象]
#     变量=[表达式 for 变量 in 可迭代对象 if 条件]
# list01 = [item ** 2 for item in range(1, 11)]
# list02 = [list01[count] for count in range(len(list01)) if list01[count] % 2 == 1]
# list03 = [list01[count] for count in range(len(list01)) if list01[count] % 2 == 0]
# list04 = [list01[count]+1 for count in range(len(list01)) if list01[count] % 2 == 0 and list01[count] > 5]
# print(list01)
# print(list02)
# print(list03)
# print(list04)

# 师
# for item in list01:
#     if item%2==1:
#         list02.append(item)
# print(list02)
