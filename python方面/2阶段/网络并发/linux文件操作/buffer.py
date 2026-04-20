"""缓冲刷新条件:
1.缓冲区满了
2.行缓冲换行时会自动刷新
3.程序运行结束或者文件close关闭
4.调用flush()函数
"""
# f= open('test','w')#表示行缓冲 若没有 1 则退出后才能写入文件
# while True:
#     data =input(">>")
#     if not data:
#         break
#     f.write(data+'\n')
# #######
# f= open('test','w',1)#表示行缓冲 若没有 1 则退出后才能写入文件
# while True:
#     data =input(">>")
#     if not data:
#         break
#     f.write(data+'\n')
#######
f= open('test', 'w')#表示行缓冲 若没有 1 则退出后才能写入文件
while True:
    data =input(">>")
    if not data:
        break
    f.write(data+'\n')
    f.flush()

f.close()