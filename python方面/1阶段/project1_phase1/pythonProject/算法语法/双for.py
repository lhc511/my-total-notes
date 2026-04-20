# print("*", end=" ")  # 原本会默认分两行打印，end作用:在*之后的一个数据 加一个空格 在同一行打印
# print("*", end=" ")  # * *

"""     *#*#*#
        *#*#*#
        *#*#*#
        *#*#*#    """
# for item in range(4):
#     for count in range(6):
#         if count%2==0:
#             print("*", end="")
#         elif count%2==1:
#             print("#", end="")
#     print()

""" *
    **
    ***
    ****  """
# for item in range(4):
#     for count in range(item+1):
#         print("*", end="")
#     print()


"""[3,80,45,5,7,1],从小到大排序"""
# list_01 = [3, 80, 45, 5, 7, 1]

# for item in range(len(list_01)-1):
#     for count in range(len(list_01) - item):
#         if list_01[item] > list_01[count+item]:
#             temp = list_01[count+item]
#             list_01[count+item] = list_01[item]
#             list_01[item] = temp
# print(list_01)

# 老师
# for r in range(len(list_01) - 1):
#     for i in range(r, len(list_01)):
#         if list_01[r] > list_01[i]:
#             list_01[r], list_01[i] = list_01[i], list_01[r]
# print(list_01)

"""[3,80,45,5,80,1]"""
# list01 = [3, 80, 45, 5, 80, 1]
# for i in range(len(list01) - 1):
#     for a in range(i, len(list01)-1):
#         if list01[i] == list01[a+1]:
#             print("有重复，值为%d" % list01[i])

"""行变列，列变行，转置"""
# list01 = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# 方法一
# for i in range(len(list01)):
#     for a in range(i+1):
#         list01[i][a],list01[a][i]=list01[a][i],list01[i][a]
# print(list01)


# for i in range(1,len(list01)):
#     for a in range(i,len(list01)):
#         list01[a][i-1],list01[i-1][a]=list01[i-1][a],list01[a][i-1]
# print(list01)



# 方法二·（追加）
# list_outside=[]
# for i in range(len(list01)):
#     list_outside.append([])
#     for a in range(len(list01)):
#         list_outside[i].append(list01[a][i])
# print(list_outside)

# list01 = ["a", "b", "c"]
# list02 = ["A", "B", "C"]
# list03 = []
# str02 = ""
# for i in range(3):
#     for a in range(3):
#         if i==a:
#             list03.append(list02[i])
#             list03.append(list01[i])
# str01="".join(list03)
# print(list03)
# print(str01)
#
# list01 = ["a", "b", "c"]
# list02 = ["A", "B"]
# list03=[]
# for i in list01:
#     for r in list02:
#         list03.append(i+r)
# print(list03)
#
# list04=[i+r for i in list01 for r in list02]
# print(list04)