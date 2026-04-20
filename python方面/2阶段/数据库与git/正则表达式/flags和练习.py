"""
A == ASCII 元字符只能匹配ascii码
I == IGNORECASE 匹配忽略字母大小写
S == DOTALL 使 . 可以匹配换行
M == MULTILINE 使 ^ $可以匹配每一行的开头结尾位置
"""
import re

# 此处有一个换行符
s = """Hello 
北京
"""
# A 只能匹配ASCII编码
# regex = re.compile(r'\w+',flags=re.A)
# l= regex.findall(s)
# print(l)#['Hello']
#
# regex = re.compile(r'\w+')
# l= regex.findall(s)
# print(l)#['Hello', '北京']

# I 不区分大小写
# regex = re.compile(r'[a-z]+', flags=re.I)
# l = regex.findall(s)
# print(l)  # ['Hello']
#
# S 可以匹配换行
# regex = re.compile(r'.+', flags=re.S)
# l = regex.findall(s)
# print(l)  # ['Hello \n北京']

# ^ $可以匹配每一行的开头结尾位置
# M 将匹配开头结尾的范围变成了每一行
# regex = re.compile(r'^北京', flags=re.M)
# l = regex.findall(s)
# print(l)  # ['北京']
# regex = re.compile(r'北京$', flags=re.M)
# l = regex.findall(s)
# print(l)  # ['北京']
