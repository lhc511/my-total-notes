import re

# =re.findall('[a-zA-Z]*','How are you')#匹配单词
# print()#['How', '', 'are', '', 'you', '']
# =re.findall('[0-9]*',"I'm 18" )#匹配单词
# print()#['', '', '', '', '18', '']

"""
匹配：第一个字母是大写字母 后面的小写字母出现0次或多次的单词
"""
# =re.findall('[A-Z][a-z]*','How are you? Fine Jame')#匹配大写字母开头单词
# print()#['How']

"""
匹配：第一个字母是大写字母 后面的小写字母出现1次或多次的单词
"""
# =re.findall('[A-Z][a-z]+','How are you? Fine Jame')#匹配大写字母开头单词
# =re.findall('[A-Z][a-z]+','I am a boy')#不能匹配单个字母  []
# print()#['How']

#  = re.findall("-?[0-9]*", "167 -28 29 -8")  # 匹配数字 ['167', '', '-28', '', '29', '', '-8', '']
#  = re.findall("-?[0-9]+", "167 -28 29 -8")  # 匹配数字 ['167', '-28', '29', '-8']
#  = re.findall("[-0-9]?", "167 -2228 29 -8")  # 匹配数字(所有出现0次到1次都匹配)
# print()

# =re.findall('[A-Z#%][@a-z0-9A-Z]+',"Port Error #404# %@STD")
# =re.findall('[^ ]+',"Port Error #404# %@STD")
# print()

"""
1.匹配一个.com邮箱格式字符串
2.匹配一个密码8-12位数字字母下划线构成
3.匹配一个数字正数，负数，整数，小数， 分数1/2,百分数45% 
4.匹配一段文字中以大写字母开头的单词，注意文字中可能有iPython(不算) H-base (算) 单词可能有大写字母小写字母-
"""
# 1
# print(re.findall(r"\w+@\w+\.com","邮箱账号: 16982769397@163.com"))
# #2
# print(re.findall(r"\w{8,12}","176adl_o"))
# #3
# print(re.findall(r"-?\d+/?\.?\d+%?","167 -28 29 -8 1/3 46%"))
# 4
# print(re.findall(r"\b[A-Z][-_a-zA-Z]*","Hello ipython2 H-base BSD"))

"""在文件中寻找设备名称的相应地址"""
"""自己的"""
# f=open('/home/ubuntu/桌面/exc.txt','r')
# port=input("请输入名称")
# list_g=[]
# while True:
#     text=''
#     for line in f:
#         if line =='\n':
#             break
#         text+=line
#     list_g.append(text)
#     if not text:
#         break
# 
# for passage in list_g:
#     tmp=passage.split(' ')[0]#存放名称
#     if port==tmp:
#         list_line=passage.split('\n')
#          = 'address'
#         for line in list_line:#找到列表中存放的对应行  BVI1
#             if re.findall(,line):
#                 # print(re.findall(,line))
#                 # print(line)
#                 list_line=line.split(',')
#                 print(list_line[-1])
#                 # sys.exit()
#             else:
#                 continue
"""老师的"""



def get_address(port):
    f = open('/home/ubuntu/桌面/exc.txt', 'r')
    while True:
        data=''
        #每一次读取一段，下议论回接着文件的上次位置继续读取直到结束
        for line in f:
            if line =='\n':
                break
            data+=line
        # list_g.append(data)
        if not data:
            break
        obj=re.match(port,data)#将名称和段落开头进行匹配并返回开头
        if obj:
            pattern=r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            obj=re.search(pattern,data)
            return obj.group()
    print("没有")

if __name__=='__main__':
    port = input("请输入名称")
    print(get_address(port))