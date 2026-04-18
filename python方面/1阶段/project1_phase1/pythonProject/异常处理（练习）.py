"""
    定义函数，在控制台中获取成绩的函数.
    要求:如果异常，继续获取成绩，直到得到正确的成绩为止.
    成绩还必须在0--100之间
"""


# def get_grade(grade):
#     if 0 <= grade <= 100:
#         print(grade)
#
#
# try:
#     get_grade(ncab)
# except Exception:
#     print("错误")


# 老师
# def get_score():
#     while True:
#         str_result = input("请输入成绩")
#         try:
#             score = int(str_result)
#         except:
#             continue
#         if 0 <= score <= 100:
#             return score
#
#
# print(get_score())

class EnemyError(Exception):
    def __init__(self, message, error_line, atk, error_code):
        self.message = message
        self.error_line = error_line
        self.atk = atk
        self.error_code = error_code


class Enemy:
    def __init__(self, atk):
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
            print(self.__atk)
        else:
            raise EnemyError("数值出错", 37, value, 7686)


try:
    e01 = Enemy(120)
except EnemyError as e:
    print(e)  # ('数值出错', 37, 120, 7686)

e02 = Enemy(230)  # __main__.EnemyError: ('数值出错', 37, 230, 7686)
