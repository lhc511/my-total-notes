"""
    sort.py 排序算法序列
"""

# 冒泡
# def bubble(list_):
#     n = len(list_)
#     # 外层表示比较多少轮
#     for i in range(n - 1):
#         # 表示每轮两两比较的次数
#         for j in range(n - 1 - i):
#             # 从小到大排序
#             if list_[j] > list_[j + 1]:
#                 list_[j], list_[j + 1] = list_[j + 1], list_[j]
#
#
# l = [4, 9, 3, 1, 2, 5, 8, 4]
# bubble(l)
# print(l)

"""选择牌序"""
# list_ = [4, 9, 3, 1, 2, 5, 8, 4]
#

# def select_sort(l):
#     for item in range(len(l)):
#         min=item
#         for a in range(item, len(l)):
#             if l[item] > l[a]:
#                 min=a
#                 l[item], l[a] = l[a], l[item]
#         if min !=item:
#         list_[item],list_[min]=list_[min],list_[item]
#
# select_sort(list_)
# print(list_)
"""插入排序"""
# l = [4, 9, 3, 1, 2, 5, 8, 4]
#
#
# def insert_sort(l):
#     for item in range(len(l)):
#         # print(item)
#         for i in range(item , 0, -1):
#             if l[i] > l[i-1]:
#                 l[i-1], l[i] = l[i], l[i-1]
#
#
# insert_sort(l)
# print(l)
# for i in range(3, -1, -1):
#     print(i,end=" ")

"""快速查找"""
l = [4, 9, 3, 1, 2, 5, 8, 1]


def sub_sort(list_, low, high):
    # 选定基准 以该位置的元素为标记，防止数据丢失
    x = list_[low]
    # low向后,high向前
    # 每进行一轮值整理一个大和小的数据
    while low < high:
        # low向后 h ig h向前摆
        # 寻找比标记数小的数字若找到就退出
        while list_[high] >= x and high > low:  # 此时什么都不做，若小于x则退出循环
            high -= 1
        # 后面的小的数往前放
        list_[low] = list_[high]  # 后面的小的数往前放
        print(l, end="")
        print(low, high)
        print()
        # 前面的比标记元素大的数往后放
        while list_[low] < x and low < high:
            low += 1
        # 查找high索引之后都是比标记元素大的数,先把大的放一边,因此赋值
        list_[high] = list_[low]

        print(l, end="")
        print(low, high)
        print()

    # 第一轮 大的和小的 相对于标记元素整理完后
    list_[low] = x  # 由于会发生数据覆盖，并且 low覆盖high 在后面，所以low上会有一组数据重复，因此把原来保存的数据赋值给 low位置上
    print("退出循环")
    return low  # 位置下标（索引）


def quick(list_, low, high):
    # low表示列表第一个元素索引，high表示最后一个元素索引
    if low < high:  # 用来判断是否符合规定(传进来的数值是否low<high) 还有退出函数
        key = sub_sort(list_, low, high)  # 传回来的是已经排好数据的位置
        quick(list_, low, key - 1)  # key-1 是已经排好的数的左边的数据
        quick(list_, key + 1, high)

    print(low, high)


quick(l, 0, len(l) - 1)
print(end=" ")
