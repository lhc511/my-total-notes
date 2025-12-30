import  controller
import module
class StudentManagerView:
    """
        学生管理视图
    """

    def __init__(self):  # 调实例方法用对象去点，对象创建根据不同需求来定
        self.__manager = controller.StudentManagerController()  #

    def __display_menu(self):
        print("1:添加学生")
        print("2:显示学生")
        print("3:删除学生")
        print("4:修改学生")
        print("5:按成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        if item == "2":
            self.__output_students(self.__manager.stu_list)
        if item == "3":
            self.__delete_student()
        if item == "4":
            self.__modify_student()
        if item == "5":
            self.__order_by_grade(self.__manager.stu_list)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        while True:
            name = input("请输入姓名")
            if name == "":
                break
            age = int(input("请输入年龄"))
            score = int(input("请输入成绩"))
            stu = module.StudentModel(name, age, score)
            self.__manager.add_student(stu)

    def __output_students(self, list_output):
        for item in list_output:
            print(item.name, item.age, item.score, item.id)

    def __delete_student(self):
        id = int(input("请输入学号"))
        if self.__manager.remove_stu(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = module.StudentModel()
        stu.id = int(input("请输入需要修改的学生编号"))
        stu.name = input("请输入学生名称")
        stu.age = int(input("请输入学生年龄"))
        stu.score = int(input("请输入学生成绩"))
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __order_by_grade(self, stu_list):
        print("按成绩升序排列学生")
        order_num = stu_list
        list_num = self.__manager.list_count()
        # print(order_num)
        for item in range(list_num):
            for count in range(1, list_num - item):
                if order_num[item].score < order_num[item + count].score:
                    order_num[item].score, order_num[item + count].score = \
                        order_num[item + count].score, order_num[item].score
        for num in range(list_num):
            print(order_num[num].name, order_num[num].age, order_num[num].score, order_num[num].id)