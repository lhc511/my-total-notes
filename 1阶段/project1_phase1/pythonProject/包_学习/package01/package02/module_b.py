def fun02():
    print("a--fun02")


# 从包中导入时从 根目录 开始，找绝对路径
from package01.module_a import fun01

fun01()
