import re  # re是python 提供的正则表达式模块

# 作用：在目标字符串内匹配符合正则表达式规则的内容
# s="lao:qtx@tedu.cn"
# data=re.findall('\w+@\w+\.cn', s)  # 第一个参数，正则表达式 第二个：目标字符串
# print(data)#['qtx@tedu.cn']

# data=re.findall('a','abscasoj')#普通字符只匹配他的对应字符
# print(data)#['a', 'a']

# data=re.findall('a|c',"ascajoievno")#竖线表示匹配竖线两侧两个条件的都可以
# print(data)#['a', 'c', 'a']

# data = re.findall("l.c", 'loc,lic,lpc')  # . 一个点 可以表示任意一个字符 但是不能匹配换行符 \n
# print(data)  # ['loc', 'lic', 'lpc']

# [aopli]：表示字符集，可以匹配字符集内部任何一个字符，逐个找出
# data = re.findall('[aopli]', 'hello world')
# print(data)  # ['l', 'l', 'o', 'o', 'l']
# data01 = re.findall('[1-9]', '2005')  # 可以匹配1到9之间的数字 a-z,A-Z同理
# print(data01)  # ['2', '5']
# # 混合写
# data02 = re.findall('[#_1-9a-m]', '#2005bzpf')  # 一般单个字符写在前面，区间写在后面
# print(data02)  # ['#', '2', '5', 'b', 'f']

# 字符集取反：表示取除了字符集意外所有的字符
# data = re.findall('[^#_1-9a-m]', '#2005bz-pf')
# print(data)  # ['0', '0', 'z', '-', 'p']

# 只匹配字符串开头位置 ^
# data=re.findall("^jame","jame,sfewv")
# print(data)#['jame']
# data=re.findall("^jame","sfewv,jame")
# print(data)#[]

# 只匹配字符串结尾位置 $
# data=re.findall("jame$","jame,sfewv")
# print(data)#[]
# data=re.findall("jame$","sfewv,jame")
# print(data)#['jame']
# 匹配字符串开头和结尾位置 ^ $
# data=re.findall("^jame$","jame")##完全匹配：正则表达式中的字符串和目标字符串完全一样才行
# print(data)#[]

# 重复元字符：* 匹配该符号的前一个字符出现0次或者多次
# data = re.findall("wo*", "woooooo~~wbbbbw!")  # 一个w后面跟0个或者多个o#对这个规则的描述
# print(data)  # ['woooooo', 'w'][o出现多次，o出现的0次] 把符合条件字符串作为数组的一个元素 不符合的字符作空格

# data = re.findall("wo+", "woooooo~~w!")  # 一个w后面跟0个或者多个o#对这个规则的描述
# data = re.findall("[wo]+", "woooooo~~wwwwwaawwoowoa!")  # w或者o的任意零个或者多个#对这个规则的描述
# print(data)  # ['woooooo'][o出现1次或多次] 把符合条件字符串作为数组的一个元素 不符合的字符作空格

# ?:#匹配前面出现了0次或者1次的字符
# data=re.findall("ab?","abbbbb,abcbdea")
# 匹配a + 0次或一次的b
# print(data)#['ab', 'ab', 'a']

# {n}: 前面一个字符出现n次 {m,n}: 前面一个字符出现 m到n次
# data = re.findall("ab{3}", "abbbbb,abcbdea")
# print(data)  # ['abbb']
# data = re.findall("1[0-9]{10}", "章三：16789857643")
# print(data)  # ['16789857643']
# data = re.findall("李.{3}", "李与会者")  # 后面的字数要和{}中的数字匹配
# print(data)  # ['李与会者']
# data = re.findall("ab{3,6}", "abbbb,abbbbbbb,abba,aaabbbb")  # 后面的字数要和{}中的数字匹配
# print(data)  # ['abbbb', 'abbbbbb', 'abbbb']
