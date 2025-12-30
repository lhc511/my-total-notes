"""字符串"""
# str编码
# ord:用于字母向数字转化    chr:用于数字向字母转化    一次只能转化一个字符或者数字，因此为了将所有字符打印出来会用到   for循环
#      字符---->数字
# str01=ord("a")
# print(str01)#97
#
# #      数---->字
# str02=chr(97)
# print(str02)#a

""""获取一字符串，并打印其每一个编码值"""
# str_1 = input("请输入一串字符：")
# for item in str_1:  # item遍历str_1的每一个对象
#     print(ord(str_1))

"""字符串字面值"""

# name="洋"#python中单双引号都一样，但以外的双引号为主流
# name='洋'

# 代码敲成什么样打印成什么样（三引号）
# # name="""洋"""
# name='''
#
#
#
#    洋'''
# print(name)

# message = '我叫"洋"'  # 想在引号里套字符
# info="我叫'洋'"
# info1=""" '我叫"洋"' """ #有单有双用三引号
# print(message)
# print(info)
# print(info1)

"""转译符号"""
# info = "我叫\"洋\""  # \
# print(info)
# info1 = "我叫\n洋"  # 换行
# print(info1)
# info1 = "我叫\t洋"  # \t相当于 tab建
# print(info1)
# info1 = "我叫\\n洋"  # \\：转译回去了
# print(info1)

"""字符串格式化1"""
# %s字符串      %d整数         %f浮点数
# a = "1"
# b = "2"
# print("请输入" + a + "+" + b + "=?")
# print("请输入%s+%s=?" % (a, b))  # %s是占位符
# print("请输入%s+%.1f=?" % ("1", 10.5))#   .1f:保留一位小数  .2f保留两位小数

"""容器类通用练习"""
# str1 = "我是"
# str2 = "洋"
# # 字符串拼接
# str3 = str1 + str2
# print(str3)  # 我是洋
# # 字符串累加
# str1 += str2
# print(str1)  # 我是洋（改变本身）
# # 重复生成元素
# print(str2 * 2)  # 我是洋我是洋
#
# str2 *= 2
# print(str2)  # 我是洋我是洋（改变本身）
# 依次比较两容器中的元素，一旦不同则返回比较结果
# print("b悟空">"a八戒")#a,b之间比编码值

# """成员运算符"""
# print("我洋" in "我叫洋")#in 判断后面的字符串是否包含前面的字符串（顺序，和是否一样，不可以分隔开）

"""索引（不可以越界）   切片（可以越界不报错）"""  # 打印字符顺序都是从小到大
# #索引分正反向：正向：0，1，2，3...  反向（从后往前）：-1，-2，-3-，4。。。
# info = "我叫洋，汪洋的洋"
# print(info[3])#获取正数第四个字
# print(info[-1])#获取最后一个字

# 切片
# 容器中取出元素组成新的容器
# print(info[0:2])  # [开始值:结束值:间隔]        我叫
# print(info[:2])  # 我叫
# print(info[-2:])  # 的圣    （想要包含最后一个字不写就好了）
# print(info[:])  # 我叫洋，汪洋的洋

# 洋叫我
# print(info[-2:-5:-1])  # 不管正反都只能到前一个字       的洋汪
# print(info[::-1])  # 全反
#
# print(info[1:1])#空
# print(info[3:1])#空        """开始值不能大于结束值"""
# print(info[-2:1])#空

"""输入一串字符，1.打印第一个，最后一个，倒数第三个，前两个字符。倒序打印字符。若字符个数为奇数，打印中间字符"""
"""len(x):返回序列长度  max(x):返回序列最大值元素  min(x):返回序列最小值元素  sum(x):返回序列中所有元素的和"""
# print(str_1[0])  # 第一个
# print(str_1[-1])  # 最后一个
# print(str_1[-3])  # 倒数第三个
# print(str_1[:2])  # 前两个
# print(str_1[::-1])  # 倒序
#
# if len(info) % 2 != 0:
#     print(info[len(info)//2])  # 奇数个印中间    info[]:可寻找字符最大值为其字符个数-1（以0开头），倘若直接用长度来找则会溢出导致程序出错
# print(len(info))

"""输入一个数字，打印长宽星号个数相等的矩形"""
# num = int(input("请输入一个数"))
# print("*" * num)
# for item in range(num-2):
#     print("*"+" "*(num-2)+"*")#打印本身是一行一行的打印的
# print("*" * num)

"""录入一个字符串，判断是否为回文（正反都一样）"""
# str_1=input("请输入一串字符")
# if str_1[::-1]==str_1:
#     print("是回文")
# else:
#     print("不是")

"""小球从一百米高度落下每次弹回原高度一半，公弹多少次，走了多少米（最小0.01米）"""
# height = 100
# height_bound = height
# count = 0
# distance = 0
# while height_bound/2 > 0.01:
#     height_bound = height_bound / 2
#     distance = distance + height
#     height = height / 2
#     count += 1
#     print("第%d次弹起的高度为%f"%(count,height_bound))
# distance=distance+100
# print("共走了%fm" % (distance))
# print("总共弹起来了%d次" % (count))

# for item in range(2):#z执行两次循环 遍历每一个元素
#     print(1)

# 语法
# name="悟空"
# age=800
# score=99.5
# print("我叫%s,年龄是%d，得分是%.1f"%(name,age,score))
