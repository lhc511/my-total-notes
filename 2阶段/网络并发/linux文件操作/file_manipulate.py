"""
对文件实现读写的基本操作步骤为:打开文件，读写文件，关闭文件
代码实现:day1/file_open.py
代码实现:day1/file_read.py
代码实现:day1/file_write.py
"""
"""打开文件"""
#只读
# try:
#     fd = open('io and input.py', 'r')
#     print(fd)
# except Exception as e:
#     print(e)  # <_io.TextIOWrapper name='io and input.py' mode='r' encoding='UTF-8'>
#
# try:
#     fd = open('io and input', 'r')
#     print(fd)
# except Exception as e:
#     print(e)  # [Errno 2] No such file or directory: 'io and input'


#写入方式
try:
    # fd = open('a.py', 'w')#此时目录里多出一个a.py 并且在每次运行时清空文件
    # fd = open('a.py', 'a')#此时目录里多出一个a.py 并且在每次运行时清空文件
    """普通文本既可以用文本方式打开也可以用二进制方式打开
    但是二进制文件只能用二进制来打开"""
    fd = open('a.py', 'rb')#二进制式

    print(fd)#此时目录里多出一个a.py 并且在每次运行时 不 清空文件
except Exception as e:
    print(e)  # [Errno 2] No such file or directory: 'io and input'

#读写文件


#关闭文件
fd.close()#此后无法进行应用