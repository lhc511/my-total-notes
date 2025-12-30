"""3.创建两个进程，分别复制一个文件的上下半部分,将复制内容放到两个新的文件中"""
from multiprocessing import Process
from time import sleep
import os


def copy_up():
    f = open('text', 'r+')
    f_up = open('text_up', 'w')
    count = 0
    half_count = 0
    for line in f:
        count += 1
    # print(count)
    f.seek(0, 0)
    for line in f:
        # print(line.decode())
        half_count += 1
        if half_count > count // 2:
            break
        f_up.write(line)



def copy_down():
    f = open('text', 'w')
    f_down = open('text_down', 'a')
    count = 0
    half_count = 0
    for line in f:
        count += 1
    # print(count)
    f.seek(0, 0)
    for line in f:
        # print(line.decode())
        half_count += 1
        if half_count > count // 2:
            f_down.write(line)


copy_list = [copy_up, copy_down, copy_up, copy_down, copy_up, copy_down, copy_up,
             copy_down, copy_up, copy_down, copy_up, copy_down, copy_up, copy_down]

end_funs =[]
for co in copy_list:
    p = Process(target=co)
    end_funs.append(p)#这里需要的参数是多线程编程里面的p
    p.start()
print(end_funs)

for i in end_funs:
    i.join()
