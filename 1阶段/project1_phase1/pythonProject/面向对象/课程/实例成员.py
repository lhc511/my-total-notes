list_student_info = []


def record_info():
    global stu  # 若没有global只可以在该函数中使用
    while True:
        name = input("请输入姓名：")
        if name == "":
            break
        age = int(input("请输入年龄："))
        grade = int(input("请输入成绩："))
        sex = input("请输入性别：")

        stu = Student(name, age, grade, sex)  # 将对象的地址传入方法（将数据传入变量中），此时的

        print(type(stu))
        list_student_info.append(stu)  # 列表中追加的每一个数据都是类的对象【列表】：因此在后面可以直接引用

    print(list_student_info)
    # 打印的是地址 [<__main__.Student object at 0x0000021CDC8CC880>, <__main__.Student object at 0x0000021CDC8CC820>]

    print()
    print(list_student_info[0])  # <__main__.Student object at 0x0000021CDC8CC880>  对应元素的地址


class Student:
    def __init__(self, name, age, grade, sex):
        self.name = name
        self.age = age
        self.grade = grade
        self.sex = sex

    def behavior(self):
        print("学生的姓名是%s,年龄是%d,成绩是%d,性别是%s" % (self.name, self.age, self.grade, self.sex))  # 通过self对象来寻找数据


record_info()
for stu in list_student_info:
    stu.behavior()  # 通过stu对象来访问其行为
info = list_student_info[0]
info.behavior()
a = list_student_info[1]  # 是吧一个类的对象赋值給a（因此可以直接调用类中的行为）
a.behavior()

# list01 = [
#     Student("赵敏", 28, 100, "女"),
#     Student("苏大强", 68, 62, "男"),
#     Student("明玉", 30, 95, "女"),
#     Student("无恳", 29, 70, "男"),
#     Student("张三丰", 130, 96, "男"), ]
""""""
# 练习1:定义函数，在list01中查找name是"苏大强"的对象，
# 将名称年龄打印在控制台中
# def check():
#     for item in list01:
#         if item.name == "苏大强":
#             return item


# python中，默认的无返回值是None

# stu = check()

""""""
# print(stu.name, stu.age)
# 找所有女同学：
# list_girl = []
#
#
# def find_girls():
#     for item in list01:
#         if item.sex == "女":
#             list_girl.append(item)
#     return list_girl
#
#
# result = find_girls()
# for item in result:
#     print(item.age,item.name)

""""""
# 寻找大于三十岁人的个数
# list_age30 = []
# count = 0
#
#
# def find_age():
#     for item in list01:
#         if item.age > 30:
#             list_age30.append(item)
#             global count
#             count += 1
#     return count
#
#
# print(find_age())
""""""
# list01中所有成绩归零
# list_grade = []
#
#
# def modify_grade():
#     for i in list01:
#         i.grade = 0
#
#
# modify_grade()
# for item in range(len(list01)):
#     print(list01[item].grade)

""""""
# 获取学生中所有名字
# for item in list01:
#     print(item.name)
""""""

# 查找年龄最大的对象：


# def find_max():
#     for item in range(len(list01) - 1):
#         if list01[item].age < list01[item + 1].age:
#             max_age = list01[item + 1]
#     return max_age
#
#
# result = find_max()
# print(result.age)
