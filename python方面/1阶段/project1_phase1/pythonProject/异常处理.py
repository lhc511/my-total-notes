"""只是以自己想要的输出形式报错"""
# # raise ValueError("aho")#ValueError: aho
# # raise ValueError
# raise Exception("jkacn")# jkacn

"""
try:

except:

当报错后继续执行下面的代码
"""

# def div_apple(apple_count):
#     # ValueError
#     person_count = int(input("请输入人数:"))
#     # ZeroDivision
#     result = apple_count / person_count
#     print("每人%d个苹果" % result)


"""     报错范围太宽泛不建议这样做

    try:  # 放可能出错的代码 #让后续逻辑正常运行
        div_apple(10)
    except:
        print("出错")
"""
"""
    #建议分门别类处理错误
try:  # 放可能出错的代码 #让后续逻辑正常运行
    div_apple(10)
except ValueError:
    print("输入的需为整数")
except ZeroDivisionError:
    print("不能输入零")
except Exception:
    print("未知出错")
"""

"""
    #建议分门别类处理错误
try:  # 放可能出错的代码 #让后续逻辑正常运行
    div_apple(10)
except Exception:
    print("未知出错")
#如果不出错不执行else语句
else:
    print("未出错代码")

"""
# #建议分门别类处理错误
# try:  # 放可能出错的代码 #让后续逻辑正常运行
#     div_apple(10)
# except Exception:
#     print("未知出错")
# #不论是否异常均执行，一般不能处理的错，但是有一定要执行的代码
# finally:
#     print("finally")
#
# print("后续逻辑.")

"""raise语句"""

#
class AgeError(Exception):
    def __init__(self, message, age_value, code_line, error_number):
        self.message = message
        self.age_value = age_value
        self.code_line = code_line
        self.error_number = error_number


class Wife:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            # raise ValueError("我不要")
            raise AgeError("超过范围", value, 26, 1001)


w01 = Wife(80)
print(w01)  # __main__.AgeError: ('超过范围', 80, 26, 1001)
# 在try之后数据本来应该报错中断，但是在 try except 函数下会继续执行 except 后的代码
# 而ValueError,AgeError本质上是 类 ，在执行过程中 创建了 该类的对象，若没有 try except 则报错原本类中存放其自身的数据（见上两行代码）

# try:
#     w01 = Wife(80)
# except ValueError as v:
#     print(v.args)
# except AgeError as a:
#     print(a.message)
#     print(a.age_value)
#     print(a.code_line)
#     print(a.error_number)

##

# try:
#     a = input("输入一个数：")
#     if not a.isdigit():
#         raise ValueError("a 必须是数字")
# except ValueError as e:
#     print("引发异常：", repr(e))
#     # raise

# ##1
# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e: # 未捕获到异常，程序直接报错 该类与程序错误类型不符
#     print (e)

# ###2
# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)

# except ValueError as e:  # 只有这个函数可以正常处理报错（即主动报错）
#     print(e)

# #######3
# s1 = 'hello'
# try:
#     int(s1)
# except Exception as e:  # 所有异常都可以报错
#     print(e)

#########4
# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)

# except ValueError as e: #下面这两条都可以正常主动报错
#     print(e)
# except Exception as e:
#     print(e)

# 自定义异常

# class Networkerror(BaseException):
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __str__(self):
#         return self.msg
#
#
# try:
#     # raise Networkerror('类型错误')
#     raise Networkerror("错了")
# except Networkerror as e:
#     # print(e)
#     print(e)
