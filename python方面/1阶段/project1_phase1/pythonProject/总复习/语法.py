str01 = "最后一堂课"
# 预留空间
list01 = [4, 5, 5, 5, 6]
# 按需分配
dict01 = {"键": "值"}
tuple01 = (5, 6, 7, 8)
# 容器相互转换
list02 = list(str01)
print(list02)
str02 = "".join(list02)
print(str02)
tuple02 = tuple(list01)
print(tuple02)
""""""
# 通用操作
# print(id(list01))
# list01 +=["a"]
# print(list01)
# print(id(list01))#在原列表后面添加数据
print(id(tuple01))  # 2558212040720
tuple01 += ("b",)  # 若在括号里面单个数据后面 加逗号 则为元组，否则为数据形式本身
print(tuple01)
print(id(tuple01))  # 2558212897904 创建了一个新的元组

# -5 -4 -2 -2 -1
# 反向索引郑正序获取
for i in range(-len(str01), 0):
    print(str01[i], end="")
# 4 3 2 1 0
# 正向索引郑倒序获取
# for i in range (len(list01)-1,-1,-1):
#     del list01[i]
# # -5 -4 -3 -2 -1
# 反向索引郑正序获取
for i in range(-len(str01), 0):
    del list01[i]
print(list01)
