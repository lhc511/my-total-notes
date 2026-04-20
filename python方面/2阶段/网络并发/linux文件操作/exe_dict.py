"""
终端输入一个单词
从单词本找到单词，打印解释内容
若没找到就打印“找不到”
"""
word = "abandon"

f = open("/home/ubuntu/桌面/dict.txt", "r")
# for line in f:
#     w=line.split(" ")[0]
#     if w>word:
#         print("没找到")
#         break
#     if w==word:
#         print(line)
#         break
# else:
#         print("没找到")

for line in f:
    w=line.split(" ")[0]
    if w==word:
        print(line)
    elif w>word:
        print("没找到")
        break
else:
    print("没找到")

f.close
