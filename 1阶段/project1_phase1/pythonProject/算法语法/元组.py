"""sum函数，返回序列中所有元素的和"""

"""元组tuple"""  # 小括号
# ##空间分配
# 列表：一开始就会开辟一块空间，倘若空间充满，则会再次开辟一块更大的空间，可以修改，但是站没存
# 元组：定量分配空间不可以变化，

# 1.创建元组
# 空
# tuple01 = tuple()
# 列表——>元组
# tuple01 = tuple([1, 2, 3])
# print(tuple01)

# 元组——>列表
# list01 = list(tuple01)
# print(list01)

# 如果元组只有一个元素            要加逗号才是元组类型
# tuple01 =(100)
# print(type(tuple01))#<class 'int'>
#
# tuple01 =(100,)
# print(type(tuple01))#<class 'tuple'>

# 获取元素（索引，切片）
# tuple01 = ("a", "b", "c", "d")
# e01=tuple01[1]
# print(type(e01))#<class 'str'>
# e02=tuple01[-2:]
# print(e02)
# print(type(e02))#<class 'tuple'>

# 可以直接将元素赋值给多个变量
# tuple02=(100,200)
# a,b=tuple02
# print(a)#100
# print(b)#200

"""遍历元素"""
# tuple01 = (1, 2, 3, 4, 5, 6)
# for item in tuple01:
#     print(item)

"""练习"""
# month=int(input("请输入月份"))
# if month not in range(1,13):
#     print("输入有误")
# elif month in (2,6,9,11):
#     print("30天")
# else:
#     print("31")

# num=[i for i in range(1,13,1)]
# print(num)

"""录入日期，计算这是今年的第几天"""
# sum_date=0
# sum_month=0
# count=0
# month=int(input("请输入月份："))
# day=int(input("请输入几号："))
# month_days=(31,28,31,30,31,30,31,31,30,31,30,31)#元组
# while count<month:
#     sum_month+=month_days[count]
#     count+=1
# sum_date=sum_month+day
# print(sum_date)

# total_day=sum(month_days[:month])+day
# print(total_day)


