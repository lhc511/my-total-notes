import re

"""
re.finditer(pattern,string,flags = 0)
功能.txt: 根据正则表达式匹配目标字符串内容
参数: pattern 正则表达式
string 目标字符串
flags 功能标志位,扩展正则表达式的匹配
返回值: 匹配结果的迭代器
"""
# 迭代器中的每一个返回的对象都对应一处匹配到的字符
s = "今年是2019年，建国70周年"
pattern = r'\d+'
# 返回选代对象
# it = re.finditer(pattern, s)
# for i in it:
#     print(i)  # 打印的是对象
#     print(i.group())  # 打印数据

"""
re.fullmatch(pattern,string,flags=0)
功能.txt：完全匹配某个目标字符串
参数：pattern 正则
string 目标字符串
返回值：匹配内容match object
"""
# m = re.fullmatch(r'[,\w]+', s)  # 若匹配不到会返回空，而空，没有group()方法
# print(m.group())

"""
re.match(pattern,string,flags=0)
功能.txt：匹配某个目标字符串开始位置
参数：pattern 正则
string 目标字符串
返回值：匹配内容match object
"""
#逗号不属于 \w 的一部分，所以后面就不算开始位置了
m = re.match(r'\w+', s)  # 若匹配不到会返回空，而空，没有group()方法
print(m.group())
