"""进程池使用示例"""

from multiprocessing import Pool
from time import sleep, ctime


# 进程池事件
def worker(msg):
    sleep(2)
    print(ctime(), '--', msg)
# 创建进程池
pool = Pool()

# 向进程池队列添加事件
for i in range(10):#这里一次执行四个是因为 为给虚拟机设置的 4核
    msg = "Tedu %d" % i
    pool.apply_async(func=worker, args=(msg,))  # $向进程池添加功能函数apply_async()

# 关闭进程池
pool.close()
# 回收进程池
pool.join()
