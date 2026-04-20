"""
    练习1:定义函数，根据年月日，返回星期数。
    "星期一"
    "星期二"
    "星期三"
    思路:年月日-->时间元组
    时间元组-->星期
    星期-->格式
"""

# def get_week(year, month, day):
# #字符串变元组
#     tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")  # 前面是打印的字符串，后面是格式，并且格式相对应
#     dict_weeks = {
#         0: "星期一",
#         1: "星期二",
#         2: "星期三",
#         3: "星期四",
#         4: "星期五",
#         5: "星期六",
#         6: "星期日",
#     }
#     return dict_weeks[tuple_time[6]]
#
#
# re = get_week(2025, 2, 25)
# print(re)
import time

"""计算从出生到现在活了多少天"""
time_c = time.time()


def birth_day(year, month, day):
    target_tuple = time.strptime("%d / %d / %d" % (year, month, day), "%Y / %m / %d")
    time_p = time.mktime(target_tuple)
    return time_p


se = birth_day(2005, 4, 9)
total_se = time_c - se
day01=total_se//(24*3600)
print(day01)
print(total_se)

print(time.localtime(total_se))
