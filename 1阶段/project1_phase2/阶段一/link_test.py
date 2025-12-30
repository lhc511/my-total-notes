from linklist import *
import time

l = range(999999)
link = LinkList()
link.init_list(1)
tm = time.time()
# for i in l:
#     print(i)
link.show()
print("time: ", time.time() - tm)
