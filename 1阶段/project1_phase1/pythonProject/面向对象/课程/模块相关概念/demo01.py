"""
    模块相关概念
"""
# 只在模块内部的成员可以以但下划线开头,只限于 * 形式的调用有效
# 能够剔除不需要的函数（在调用时）
# from module01 import *
# fun01()
# 隐藏成员不可以通过from  module01 import *形式调用
# _fun02()
# from module01 import _fun02
# 可以通过其他形式调用隐藏成员
# _fun02()

from module01 import *

Myclass.fun03()
_fun02()
print(__doc__)  # 模块相关概念   打印出注释

print(__file__)  # 打印文件绝对路径
# 模块自身名字，可以判断是否为主模块
print(__name__)  # __main__ 代表该模块为主模块，即执行程序从这个模块第一个开始执行而在 其他模块中 则打出的是该 模块名
# 在module01中 module01
