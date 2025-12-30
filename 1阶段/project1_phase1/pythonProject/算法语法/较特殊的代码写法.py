"""列表推导式"""
"""list所有元素增加1后放入list02中"""
###写法1
# list01 = [5, 56, 6, 7, 7, 8, 9]
# list02 = []
# for item in list01:
#     list02.append(item + 1)  # [6, 57, 7, 8, 8, 9, 10]
# print(list02)
###第二种写法(二者等价)
# list02 = [item + 1 for item in list01]
# print(list02)

# 语法：变量=[表达式 for 变量 in 可迭代对象]
#     变量=[表达式 for 变量 in 可迭代对象 if 条件]
"""list大于10元素增加1后放入list02中"""
# list02 = [item + 1 for item in list01 if item > 10]
# print(list02)

""""""
# num=[i for i in range(1,13,1)]
# print(num)
#生成器函数表达式
# re =(item for item in list01 if type(item) == int)