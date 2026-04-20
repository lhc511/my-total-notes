import re

"""
re.findall(pattern,string,flags = 0)
功能.txt: 根据正则表达式匹配目标字符串内容
参数: pattern 正则表达式
string 目标字符串
flags 功能标志位,扩展正则表达式的匹配
返回值: 匹配到的内容列表,如果正则表达式有子组则只能获取到子组对应的内容
"""
# 目标字符串
s = "Alex:1994,Sunny:1996"
pattern = r"\w+:\d+"  # 正则表达式
# pattern1 = r"(\w+):\d+"  # 正则表达式

# # re 模块调用findall
# l = re.findall(pattern, s)  # ['Alex:1994', 'Sunny:1996']

# # findall函数中若用括号括出字组则只会打印符合表达式中子组的数据
# l1 = re.findall(pattern1, s)  # ['Alex', 'Sunny']
# print(l)
# print(l1)

"""
regex= compile(pattern,flags-0) 
功能.txt:生产正则表达式对象参数:
pattern 正则表达式
flags 功能标志位，扩展正则表达式的匹配
返回值:正则表达式对象
"""
regex = re.compile(pattern)
l = regex.findall(s)
# print(l)  # ['Alex:1994', 'Sunny:1996']
"""
regex.findall(string,pos, endpos) 
功能.txt:根据正则表达式匹配目标字符串内容
参数:string 目标字符串
pos截取目标字符串的开始匹配位置
endpos 截取目标字符串的结束匹配位置
返回值:匹配到的内容列表，如果正则表达式有子组则只能获取到子组
"""
l = regex.findall(s, 0, 12)  # 截取0到第11个字符进行匹配
print(l)  # ['Alex:1994', 'Sunny:1996']

"""
re.split(pattern,string,max，flags = 0)
功能.txt: 使用正则表达式匹配内容,切割目标字符串
参数: pattern 正则表达式
string 目标字符串
max 最多切割几部分
flags 功能标志位,扩展正则表达式的匹配
返回值: 切割后的内容列表
"""
s = "Alex:1994,Sunny:1996"
pattern = r"\w+:\d+"  # 正则表达式
pattern1 = r"(\w+):\d+"  # 正则表达式
# l = re.split(r'[:,]', s)  # 按照冒号和逗号切割字符串
# print(l)  # ['Alex', '1994', 'Sunny', '1996']

"""
re.sub(pattern,replace,string,count,flags = 0)
功能.txt: 使用一个字符串替换正则表达式匹配到的内容
参数: pattern 正则表达式
replace 替换的字符串
string 目标字符串
count 最多替换几处,默认替换全部
flags 功能标志位,扩展正则表达式的匹配
返回值: 替换后的字符串
"""
# s=re.sub(r":",'-',s)#用 : 匹配字符串 并用 - 来替换匹配到的内容
# print(s)#Alex-1994,Sunny-1996
# s=re.sub(r":",'-',s,1)#用 : 匹配字符串 并用 - 来替换匹配到的内容 只替换1处
# print(s)#Alex-1994,Sunny:1996

# a = re.subn(r":", '-', s, 1)  # 多了一个返回值，有几处被替换了
# print(a)  # ('Alex-1994,Sunny:1996', 1)
