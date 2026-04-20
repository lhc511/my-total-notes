"""导入方式1"""
# 本质：使用变量名module01关联模块地址
# import module01#只执行一体次
# import module01
# module01.fun01()
# my02=module01.Myclass02()
# my02.fun02()

"""as"""  # 起一个别名 用别名调用
import module01 as m01

m01.fun01()
my02 = m01.Myclass02()
my02.fun02()

"""导入方式2"""  # 导入后可以直接用  不要冲突（重名），否则先执行哪一条代码就按哪条当结果
# 本质：把指定成员导入到当前模块作用域当中
# from module01 import Myclass02
# from module01 import fun01
#
# def fun01():
#     print("当亲模块fun01")
#
# fun01()
# my02 = Myclass02()
# my02.fun02()

"""导入方式3"""  # 不要让导入进来的成员和其他模块冲突
# 本质：把指定模块所有成员导入到当前模块作用域当中
# from module01 import *  # 星号是指导入另一个文件的全部
#
# fun01()
# my02 = Myclass02()
# my02.fun02()




