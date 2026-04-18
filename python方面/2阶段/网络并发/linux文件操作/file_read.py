"""
文件读取
"""
# 打开文件
# f = open('test', 'w')  # 以只写方式用read打开会报错 not readable 该行可以执行第七行执行不了
# f = open('test', 'r')  # 以只写方式用read打开会报错 not readable

# # data=f.read()#读所有内容
# data = f.read(8)  # hello wo 换行也是字符
# print(data)

# f = open('test', 'rb')  # 以只写方式用read打开会报错 not readable
# # data=f.read()#读所有内容

# data = f.read(12)  # hello wo 换行也是字符
# print(data)  # b'hello word\n\n' 二进制形式读取
# print(data.decode())  # hello word 转变为字符串形式读取

# 关闭
# f.close()
# 读取图片二进制码
# f = open('/root/systemsoftware/Pictures/img.jpg', 'rb')

# data = f.read()
# print(data)
# f.close()

# read
# f = open('test', 'r')
# while True:
#     data = f.read(10)#一次只读取十个字符
#     if not data:#读到结尾跳出，结尾字符串为空 空就是假
#         break
#     print(data)

# readline

# f = open('test', 'r')
# data = f.readline(10)  # 读取前10个字符
# print("一行内容:", data)
# data = f.readline()  # 读完第一行剩余内容
# print("一行内容:", data)
# 将内容读取为列表，每行为列表一个元素
# 每一行作为列表中的一个元素

# data = f.readlines(18)  # 前18个字符所在的行作为读取对象 ['hello word\n', 'najscbnsajcnsa']
# print(data)  # f为可迭代对象
# for i in f:
#     print(i)
# f.close()
