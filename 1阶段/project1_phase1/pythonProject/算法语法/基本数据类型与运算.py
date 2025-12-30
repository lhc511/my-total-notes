# input数据类型为字符串类型，有时需要进行数据转换     //为整数商， /为基数商  %取余

"""交换数据"""
# # 该方法仅在Python1中可以用
# data01 = input("请输入一串文字：")
# data02 = input("请再次输入一段文字")
# data01, data02 = data02, data01
# print(data02+"是" + data01)
# print(data01+"是" + data02)
# +表示将两个字符串合并为同一个字符串再输出

"""核心数据类型"""
# None(让该变量内存空间不存储数据)
# 作用：解除关联    占空档（方便之后使用）
# a = "lihaichuan"
# a = None

# int 整形
# num01=20
# num02 = 0b10  # "0b"表示2进制，大小为2
# print(num02)  # print以十进制形式输出
# num03 = 0o10  # "0o"表示8进制，大小为8
# print(num03)  # print以十进制形式输出
# num04 = 0x10  # "0o"表示16进制，大小为16
# print(num04)  # print以十进制形式输出

# float:浮点型
# 小数:1.0  2.5e/E指数
# 1.23e-2=0.0123
# 1.23456e5=123456.0
# print(1.5)
# print(0.00002)

"字符串（str）"
# print("1.5")打印字符串
# print(1.5)打印变量

"""数据类型转换"""
# str_used = input("请输入美元:")
# # 类型转换
# str_used = int(str_used)  # 字符串变整形数字
# result = str_used * 6.9
# print(result)
# result = str(result)  # 数字变字符串
# print("结果是：" + result)#字符串的拼接

"""算术运算符"""
# print(1 + 2)  # *乘法
# print(2.5 + 2)
# print(5 // 2)  # 取商(整数)
# print(5 % 2)  # 取余
# print(5 / 2)  # 取商（较精确可以取小数）
# print(27 % 10)  # 取整数位
# print(3 ** 2)  # 3的2次方

"""增强运算符"""
# number01 = 200
# print(number01 + 1)  # 其地址+1.并不改变值
# print(number01)  # 接过仍为200,
# # 改变方法
# number01 = 200
# number01 = number01 + 1       number01 += 1
# print(number01)  # 接过仍为200,

"""运算符优先级"""
# () > ** > * / % // > +-

"""练习1:买两个25块钱的东西，给六十块，找多少钱"""
# price = float(input("请输入商品单价："))
# num = float(input("请输入商品数量："))
# give = float(input("给出的金额："))
# obtain = give - price * num
#
# if obtain == 0:
#     print("刚刚好")
#
# elif obtain < 0:
#     print("钱不够")
#
# else:
#     print("找回的钱：" + str(obtain))
"""练习2：计算分钟，小时。天数的对应秒数"""
# min = int(input("请输入分数"))
# hour = int(input("请输入小时"))
# day = int(input("请输入天数"))
#
# min_sec = min * 60
# hour_sec = hour * 3600
# day_sec = day * 3600 * 24
# all = day_sec + min_sec + hour_sec
# print("总数为"+str(all))

"""练习三：一斤十六两，输入多少两，转化为几斤几两"""
# num_l = int(input("所求的两数"))
# num_jin = num_l // 16
# num_re_l = num_l % 16
# print("重量为" + str(num_jin) + "斤" + str(num_re_l) + "两")

"""练习四：输入距离时间初速度计算加速度"""
# v = int(input("初速度为："))
# x = int(input("输入距离为:"))
# t = int(input("输入时间为:"))
# a = (x - v * t) * 2 / t ** 2
# print("加速度为："+str(a))

"""练习五：输入一个整数，输出每一个位置的数字的和"""

"""bool类型:取值为True False(大写首字母)      比较运算符，逻辑运算符"""
# 比较运算符：< > >= <= == !=  (结果是bool 类型)
# print(1>2)#结果false

# 逻辑运算符两个bool值关系  与and/或or/非not (取反)
# print(True and True)#True
# print(False and True)#False
# print(True and False)
# print(False and False)

# print(False or True)#True
# print(True  or True)#True
# print(True  or False)
# print(False or False)

# print(not True)
# print(not False)

"""练习：是否为闰年，可被4整除不可被100整除，闰年True，平年False"""
# run_nian = int(input("输入年份："))
# print((run_nian % 4 == 0) and (run_nian % 100 != 0))
