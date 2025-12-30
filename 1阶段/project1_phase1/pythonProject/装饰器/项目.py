"""在不改变原有功能(fun01fun02)调用与定义情况下 ， 为其增加新功能(打印函数执行时间). """
import time

def count_time(func):
    def wrapper(*args,**kwargs):
        time01 = time.time()
        result=func(*args,**kwargs)
        t02 = time.time()
        print(t02 - time01)
        return result#由于调用的方法可能有返回值所以用return，具体听老师讲
    return wrapper

@count_time
def fun01():
    time.sleep(0.22)  # 睡眠2秒，用于模拟程序执行的过程print("fun01执行完毕喽“)

@count_time
def fun02(a):
    time.sleep(0.2)
    print("fun02执行完毕喽，参数是:", a)
    return 1



# fun01()
fun02(100)
