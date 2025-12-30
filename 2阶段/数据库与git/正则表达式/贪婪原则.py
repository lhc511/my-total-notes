"""在正则表达式中匹配到的字符总会倾向于选择多的，但在尾端添加一个?就会选择较少的"""
import re

# data = re.findall('аb*? ', "аbbbbbbbbсd")  # []
# print(data)
# data = re.findall(r'ab+?', "abbbbbbbbbcd")  # ['ab']
# print(data)
# data = re.findall(r'ab?', "abbbbbbbbbcd")  # ['ab']
# print(data)
# data = re.findall(r'ab{3,5}?', "abbbbbbbbbcd")  # ['abbb']
# print(data)

s = "[花千骨]，[陆贞传奇]，[新还珠格格][楚乔传]"
print(re.findall(r'\[\w+]', s))  # ['[花千骨]', '[陆贞传奇]', '[新还珠格格]', '[楚乔传]']

# 在贪婪模式下会默认选择最多的，所以选择从左到右范围最大的中括号，因此变为一个整体元素
print(re.findall(r'\[.+]', s))  # ['[花千骨]，[陆贞传奇]，[新还珠格格][楚乔传]']

# 而在加了？之后变为取最小范围 因此每个中括号都是一个元素
print(re.findall(r'\[.+?]', s))  # ['[花千骨]', '[陆贞传奇]', '[新还珠格格]', '[楚乔传]']
