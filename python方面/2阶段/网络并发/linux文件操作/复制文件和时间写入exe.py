import time

# 将一个文件里面的内容复制到另一个文件里面
# filename = "test"
# try:
#     fr = open(filename, 'rb')  # 二进制打开
# except FileNotFoundError as e:
#     print(e)
# else:
#     fw = open('img.jpg', 'wb')  # 二进制写入
#     # 循环读取文件知道最后
#     while True:
#         data = fr.read(1024)
#         if not data:  # 文件结束19
#             break
#         fw.write(data)  # 将读取内容写入
#     fr.close()
#     fw.close()
"""my"""
# filename = "/home/ubuntu/图片/img.jpg"
# target_file = "img.jpg"
# try:
#     fr = open(filename, 'rb')
# except FileNotFoundError as m:
#     print(m)
# else:
#     wf = open(target_file, "wb")
#     while True:
#         data = fr.read(100)
#         if not data:
#             break
#         wf.write(data)
#     fr.close()
#     wf.close()

f = open("test", "a+")  # 由于a+是从末尾开始追加写入，所以计数要从头开始
f.seek(0, 0)
i = 0
for line in f:
    i += 1

while i < 100:
    i+=1
    time.sleep(1)
    f.write("%d %s\n" % (i, time.ctime()))
    f.flush()
