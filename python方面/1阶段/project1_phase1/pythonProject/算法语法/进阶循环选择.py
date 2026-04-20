"""del语句：作用是删除变量，解除关系"""
# a = "手机号"  # 被变量a引用，对象“手机号“引用计数器加一
# b = a  # "手机号"被变量a引用，对象“手机号“引用计数器加一
# c = a  # 被变量a引用，对象“手机号“引用计数器加一
# # 删除变量a,b，但不释放对象 "手机号"解除a,b对“手机号"的引用
# del a, b
# c = None  # "空引用"，只用于开创一个变量

"""小整数对象池（-5到256）在终端中由于经常使用所以使用赋值给变量时地址相同，以外地址不同"""  # 提高内存利用率吧
"""下方是文件式python，于上方不同"""
"""身份运算符"""
"""is"""
# a = 800
# b = 1000
# # id:获取变量存储对象的地址
# print(id(a))
# print(id(b))
# print(a is b)  # 判断a,b存储的对象是否一样，一样返回True,不一样返回False
# c = a
# print(id(c))
# print(c is a)
# d = 1000
# print(d is b)

"""练习：输入总秒数，计算几时几分几秒"""
# sec=int(input("请输入总秒数"))
# hour=sec//60//60
# min=sec//60-hour*60
# sec_remain=sec-min*60-hour*3600
# print("结果为："+str(hour)+"时"+str(min)+"分"+str(sec_remain)+"秒")

"""行"""
# 三个物理行，三个逻辑行
# a=1
# b=a+2
# c=b+1
# #一个物理行，三个逻辑行
# a=1;b=a+2;c=b+1
# a = 1 + 2 + 3 + 4  # (y一个物理行，一个逻辑行)
# """一个物理行，两个逻辑行"""  # \表示折行符号
# d = 1 + 2 + \
#     3 + 4
# #4个物理行，一个逻辑行
# d = (1 +
#      2 +
#      3 +
#    4)

# pass 填充语法空白

"""选择语句"""
# sex = input("请输入性别：")
# if sex == "男":
#     print("你好，先生")
# elif sex == "女":
#     print("你好，女士")
# else:
#     print("输入错误")

"""输入四个数字取最大值"""
# num01 = int(input("请输入第1个数字："))
# num02 = int(input("请输入第2个数字："))
# num03 = int(input("请输入第3个数字："))
# num04 = int(input("请输入第4个数字："))
#
# if num01 > num02:
#     num02 = num01
# if num02 > num03:
#     num03 = num02
# if num03 > num04:
#     num04 = num03
# print(num04)

"""真值表达式，条件表达式"""
# if 1:  # 非零为真
#     print("真")
#     if input():
#         print("输入的字符串不是空的")


# sex = None
# if input("请输入性别：") == "男":
#     sex = 1
# else:
#     sex = 0
# print(sex)
# # ###上下结果一致
# sex = 1 if input("请输入性别：") == "男" else 0#*************************（另一种写法）
# print(sex)

"""练习一：获取一个整数，若为偶数为state赋值偶数，否则奇数"""
# num = int(input("请输入一个整数"))
# state = None
# if num % 2:
#     state = num + 1
# else:
#     state = num
# print(state)
#
# state = num + 1 if num % 2 else num  # ##第二种写法：

"""练习二：输入一个年份，闰年赋值29，平年28"""
# day = None
# year = int(input("请输入一个年份"))
# day = 28 if year % 4 == 0 and year % 100 or year % 400 == 0 else 29
# print(day)

"""循环语句
        while 条件:
            循环体
"""
# while True:
#     dollar = int(input("请输入美元"))
#     print(dollar * 6.9)
#     if input("输入e退出") == "e":
#         break
# count=0
# while count<3:
#     count+=1
#     dollar = int(input("请输入美元"))
#     print(dollar * 6.9)
#     if input("输入e退出") == "e":
#         break

# count=0
# while count<3:
#     print(count)
#     count+=1

"""练习"""

# while True:
#     old = input("请输入年龄")
#     if old == "p":
#         break
#     year = int(old)
#     if year < 0:
#         print("输入错误")
#     elif year < 2:
#         print("婴儿")
#     elif 2 < year < 13:
#         print("儿童")
#     elif 13 < year < 20:
#         print("青少年")
#     elif 20 < year < 65:
#         print("成年人")
#     elif 65 < year < 150:
#         print("老年人")
#     else:
#         print("输入错误")
"""5的平方"""
# u=5**2
# print(u)

# con = 3
# while con < 9:
#     con += 1
#     print(con)

# con = 0
# height = 1 * 10 ** -5
# while height < 8844.43:
#     height = height * 2
#     con += 1
# print(con)

"""猜数字游戏"""
# i=0
# print("猜的次数不可以超过三次")
# import random
# random_number=random.randint(1,100)
# while i<3:
#     i+=1
#     guess_num=int(input("请输入猜的数字："))
#     if random_number>guess_num:
#         print("小了")
#     elif random_number<guess_num:
#         print("大了")
#     elif random_number==guess_num:
#         print("对了")
#         break
#     else:
#         print("输入错误请再次输入")
# if i==3:
#     print("您已失败")

"""for循环，range"""
# for 变量 in 可迭代对象 :
#     循环体

# str01="神奇的海洋"
#  item存储的是字符串中每个字符的地址          已知长度列表或固定次数循环（列表，字符串，元组等）
# for item in str01:
#     print(item)

# 整数生成器 range(开始值,结束值,间隔),不会等于结束值
# for item in range(1,5,1):#从1开始
#     print(item)
# # 只写一个数字为结束值
# for item in range(5):#从0开始
#     print(item)

# thickness=0.000001
# for i in range(10):#循环10次
#     thickness*=2

# for:预定次数   while:根据条件循环

"""累加1----100"""
# i=0
# for num in range(1,101):
#     i=i+num
# print(i)
"""累加1--100间偶数和"""
# sum=0
# for num1 in range(2,101,2):
#     sum=sum+num1
# print(sum)
"""累加10--36间偶数和"""
# sum=0
# for num1 in range(10,37):
#     sum=sum+num1
# print(sum)

"""随机数加法练习"""
# i=0
# score=0
# while i<3:
#     i+=1
#     import random
#     random_num1=random.randint(1,10)
#     print(random_num1)
#     random_num2=random.randint(1,10)
#     print(random_num2)
#     customer_num3=int(input("请输入你的猜数字"))
#     if customer_num3==random_num1+random_num2:
#         print("输入正确")
#         score+=10
#     elif customer_num3!=random_num1+random_num2:
#         print("答错了")
#
# print(score)

"""输入一个数，判断是否为素数（只可以被1和自身整除的数）"""
# num=int(input("请输入一个数"))
# for divide_num in range(2,num):
#     if num%divide_num==0:
#         print("不是素数")
#         break
#     else:
#         print("为素数")
#         break

"""continue语句:若不满足条件则跳过本次循环，执行下次循环"""
#1--100间被5整除的数
# i=0
# for item in range(1,101):
#     if item%5!=0:
#         continue
#     i=i+item
# print(i)

"""累加10--50间各位不是2 5 9的整数"""
# sum=0
# for add_num in range(10,51):
#     if add_num%10!=2 and add_num%10!=5 and add_num%10!=9:
#         sum = sum+add_num
# print(sum)

# for i in range(0,3):
#     print(i)