import time

# 1.获取当前时间戳(从1970年1月1日到现在经过的秒数)
# 1560998261.108855
# print(time.time())
# 2.时间元组(年，月，日，时，分，秒，一周的几天，一年的第几天，夏令时)
# 时间戳变成时间元组
# print(time.localtime(1560998261))  # 以元组形式表现时间
# tuple_time = time.localtime()
# for item in tuple_time:
#     print(item)

# print(tuple_time[1])
# print(type(tuple_time))
# print(time.struct_time)  # 打出的是类型
# print(tuple_time.tm_year)

# 时间元组变成时间戳
# print(time.mktime(tuple_time))  # 1.获取当前时间戳(从1970年1月1日到现在经过的秒数)
#
# # 时间元组变成字符串——>str
#
# # 25 / 02 / 25 / 15 ： 26 ： 58
# str_time01 = time.strftime("%y / %m / %d / %H ： %M ： %S ", tuple_time)  # (年/月/日/时/分/秒,元组) 前面的符号均为规定,用元组里面的去给前面赋值
# print(str_time01)
# # 2025 / 02 / 25 / 15 ： 29 ： 07
# str_time01 = time.strftime("%Y / %m / %d / %H ： %M ： %S ", tuple_time)  # (年/月/日/时/分/秒,元组) 前面的符号均为规定
# print(str_time01)
#
# # str-->元组
#
# target_tuple = time.strptime(str_time01, "%Y / %m / %d / %H ： %M ： %S ")
# # time.struct_time(tm_year=2025, tm_mon=2, tm_mday=25, tm_hour=15, tm_min=32, tm_sec=17, tm_wday=1,
# # tm_yday=56, tm_isdst=-1)
# print(target_tuple)

tuple_time01=time.localtime()
print(tuple_time01)
total_second=time.mktime(tuple_time01)
print(total_second)
#元组变成字符串
str_tuple=time.strftime("%Y,%m,%d",tuple_time01)
print(str_tuple)
#字符串变成元组
tuple_time01=time.strptime(str_tuple,"%Y,%m,%d")
print(tuple_time01)