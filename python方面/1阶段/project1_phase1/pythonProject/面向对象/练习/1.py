"""学生管理系统项目计划:
1.完成数据模型类StudentModel
2.创建逻辑控制类StudentManagerController
3.完成数据:学生列表__stu_list
4.行为:获取列表stu_list,
5.添加学生方法add_student
6.根据编号删除学生remove_student
7.根据编号修改学生update_student
8.创建学生管理视图（包含显示选项界面以及内部的操作)界面视图类：StudentManagerView
9.在界面视图类中输入学生信息
10.在界面视图类中显示学生信息
11.在界面视图类中删除学生信息
12.在界面试图中修改学生信息
13.根据成绩排序order_by_score
-14:30-"""


class StudentModel:
    """
        学生数据
    """

    def __init__(self, name="", age=0, score=0, id=0):
        """
            学生信息
        :param name: 学生名称 str型
        :param age: 学生年龄 int型
        :param score: 学生分数 int型
        :param id:学生编号 int型
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    """
        信息管理方法控制器
    """
    manager = StudentModel()
    __stu_id = 0

    def __init__(self):  # 从界面视图中操作列表，因此是从外部获取数据，因此直接创建列表，不返回本身
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu_case):
        """
            添加学生信息
        """
        self.__stu_id += 1
        stu_case.id = self.__stu_id
        self.__stu_list.append(stu_case)

    def remove_student(self, id):
        """
            根据学生编号来删除对应信息
        :param id: 被删除学生的编号
        :return:
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)

    def update_student(self, id):
        for item in self.__stu_list:
            if item.id == id:
                item.name = input("请输入要修改学生的姓名")
                item.age = input("请输入要修改学生的年龄")
                item.score = input("请输入要修改学生的分数")

    def order_by_score(self):
        for i in range(len(self.__stu_list)-1):
            for item in range(i+1,len(self.__stu_list)):
                if self.__stu_list[i].score < self.__stu_list[item].score:
                    self.__stu_list[i], self.__stu_list[item] = self.__stu_list[item], self.__stu_list[i]




"""测试添加学生功能"""
# controller = StudentManagerController()
# stu1 = StudentModel("zs", 23, 87, 0)
# stu2 = StudentModel("ls", 25, 99, 0)
# controller.add_student(stu1)
# controller.add_student(stu2)
# for item in controller.stu_list:
#     print(item.name, item.age, item.score, item.id)

"""测试移除学生功能"""
# controller = StudentManagerController()
# stu1 = StudentModel("zs", 23, 87, 0)
# stu2 = StudentModel("ls", 25, 99, 0)
# controller.add_student(stu1)
# controller.add_student(stu2)
# controller.remove_student(1)
# for item in controller.stu_list:
#     print(item.name, item.age, item.score, item.id)

"""测试修改学生功能"""


# controller = StudentManagerController()
# stu1 = StudentModel("zs", 23, 87, 0)
# stu2 = StudentModel("ls", 25, 99, 0)
# controller.add_student(stu1)
# controller.add_student(stu2)
# for item in controller.stu_list:
#     print(item.name, item.age, item.score, item.id)
#
# controller.update_student(1)
# for item in controller.stu_list:
#     print(item.name, item.age, item.score, item.id)

class StudentManagerView:
    controller = StudentManagerController()

    def menu(self):
        print("1)请输入学生信息")
        print("2)输出学生信息")
        print("3)删除学生信息")
        print("4)修改学生信息")
        print("5)按成绩输出学生信息")
        print("6)退出")

    def selection(self):
        while True:
            value = int(input("请输入选项"))
            if value == 1:
                self.__input_student()
            elif value == 2:
                self.__output_student()
            elif value == 3:
                self.__delete_student()
            elif value == 4:
                self.__modify_student()
            elif value == 5:
                self.__output_student_order()
            elif value == 6:
                break

    def main(self):
        self.menu()
        self.selection()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名")
        stu.age = input("请输入学生年龄")
        stu.score = input("请输入学生得分")
        self.controller.add_student(stu)

    def __output_student(self):
        """
            显示学生信息
        :return:
        """
        for item in self.controller.stu_list:
            print(item.name, item.age, item.score, item.id)

    def __delete_student(self):
        id = int(input("请输入要删除学生的id："))
        self.controller.remove_student(id)

    def __modify_student(self):
        id = int(input("请输入要修改信息的Id"))
        self.controller.update_student(id)

    def __output_student_order(self):
        self.controller.order_by_score()
        self.__output_student()


view = StudentManagerView()
view.main()
