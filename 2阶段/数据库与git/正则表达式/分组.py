import re

# 有括号
# print(re.search(r'(ab)+', 'abababababab').group())  # 只对查找的第一个位置有效

# # 给子组命名为 "pig" ab前面的是固定起名格式
print(re.search(r'(?P<pig>ab)+', "ababababab").group('pig'))#ab

# print(re.search(r'(王|李)\w{1,3}', "王者荣耀").group())  # 王者荣耀
# # group：可以通过某些接口获取子组对应的部分内容
# print(re.search(r'(王|李)\w{1,3}', "王者荣耀").group(1))  # 王
#

# print(re.search(r'\w{19}', "G610111200504092514").group())#ab

# print(dir(re))