"""在字符串前加上 r，‌告诉 Python 直接按字面意义解释反斜杠，‌而不是作为转义字符。‌"""
import re

# \d 匹配任意数字字符 == [0-9]
# \D 匹配任意非数字字符 == [^0-9]
# data=re.findall(r"\d{1,5}","Mysql:3306,http:80")
# print(data)#['3306', '80']
# data = re.findall(r'\D+', "Mysql: 3306 , http:80")
# print(data)  # ['Mysql: ', ' , http:']

# \w 匹配任意普通字符 ：数字 字母 下划线，汉字
data = re.findall(r"\w+", "Sever_port=8888")
print(data)  # ['Sever_port', '8888']
# data = re.findall(r"\w+", "Sever_port=四个八")
# print(data)  # ['Sever_port', '四个八']
#
# # \W 匹配任意非普通字符 == [^0-9]
# data = re.findall(r"\W+", "Sever_port=8888")
# print(data)  # ['=']
#
# # ·元字符:\s \S
# # ·匹配规则:\s 匹配空字符，\S匹配非空字符
# # ·说明:空字符指 空格 \r \n \t \v \f字符
# data = re.findall(r"\w+\s+\w+", "hello     world")
# print(data)  # ['hello     world']
# data = re.findall(r"\S+", "hello     world")
# print(data)  # ['hello', 'world']

# \A:匹配开头位置 和之前学的一个意思
# \Z匹配结尾位置
# data = re.findall(r"\Ahello", "hello     world")
# print(data)  # ['hello']
# data = re.findall(r"world\Z", "hello     world")
# print(data)  # ['world']
#
# # ·元字符:\b \B
# # ·匹配规则:\b表示单词边界，\B表示非单词边界
# # ·说明:单词边界指 数字字母(汉字)下划线 与其他字符的交界位置。
# data = re.findall(r"\bis\b", "this is apple")
# print(data)  # ['is']
# #左侧是非单词边界，右侧是单词边界
# data = re.findall(r"\Bis\b", "this is apple")
# print(data)  # ['is']这里的is是this里面的
# data = re.findall(r"\b\d+\b", "13 89 num007")
# print(data)  # ['13', '89']

"""特殊符号的匹配"""
# data = re.findall(r"\d+\*\*\d+", "2**18")
# print(data)  # ['2**18']

# data = re.findall(r"-?\d+\.?\d*", "12 -36 28 1.34 -3.8")
# print(data)  # ['2**18']
