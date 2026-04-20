"""学生管理系统项目计划:
1.完成数据模型类StudentModel
2.创建逻辑控制类StudentManagerController
3.完成数据:学生列表__stu_list
4.行为:获取列表stu_list
5.添加学生方法add_student
6.根据编号删除学生remove_student
7.根据编号修改学生update_student
8.创建学生管理视图（包含显示选项界面以及内部的操作
9.在界面视图类中输入学生信息
10.在界面视图类中显示学生信息
11.在界面视图类中删除学生信息
12.在界面试图中修改学生信息
-14:30-"""


class StudentModel:
    """
        学生信息模型
    """

    def __init__(self, name="", age=0, score=0, id=0):  # 赋值必须从右向左进行赋值（在此处赋值是为了让数据有默认值，当未输入数据时其使用默认值）
        """
            创建学生对象
        :param name: 名字，str类型
        :param age:年龄，int类型
        :param score:成绩，float型
        :param id: 编号（该学生对象唯一标识）
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id  # 若无默认值则必须填所有值


class StudentManagerController:
    """
        控制对学生信息的增删改查
    """
    # 类变量，初始编号
    __init_id = 1000

    def __init__(self):  # 内部不加__stu_list是因为由要求可以知道其值是从外部按照需求获取，而不是从内部获取
        self.__stu_list = []  # 用于记录学生信息的列表

    # 属性
    # 当把函数作为变量赋值时会触发@xxx.setter对应的函数，    写入
    # 当把函数作为变量读取时会触发@property对应的函数，      读取
    # 可以使用@property装饰器来创建只读属性，@property装饰器会将方法转换为相同名称的只读属性，这样可以防止属性被修改。
    # @函数名称.setter。 setter装饰器用来创建一个可写的属性，
    @property  # 创建property对象。但是只负责拦截读取，将拦截到的值交给__stu_list
    def stu_list(self):
        """
            存储学生对象的列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list  # 此时的__stu_list只能读取

    def add_student(self, stu_info):
        """
            添加一个学生
        :param stu_info:没有编号的学生信息
        :return:
        """
        stu_info.id = self.__generate_id(stu_info)  # 将产生的id赋值给StudentModle中的id
        self.__stu_list.append(stu_info)  # 在追加时追加的数据被拦截，返还给__stu_list列表中

    def __generate_id(self, stu_info):
        """
            产生学生的ID
        :param stu_info:生成id的学生信息
        :return: 生成的ID
        """
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_stu(self, id):
        """
            根据编号移除信息
        :param id: 被移除学生的id
        :return:
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                print("删除成功")
            else:
                print("删除失败")

    def update_student(self, stu_info):  # stu_info就是用来接受下方stu的参数，stu就是赋值StudentModel的变量
        """
            根据编号修改学生信息
        :param id: 被修改学生的编号
        :return:
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True  # 修改成功
        return False  # 修改失败
    
    def list_count(self):
        return len(self.stu_list)

"""测试添加学生功能"""
# manager = StudentManagerController()
# s01 = StudentModel(0, "zs", 24, 100)
# s02 = StudentModel(0, "ls", 35, 80)
# manager.add_student(s01)
# manager.add_student(s02)
# for item in manager.stu_list:
#     print(item.name,item.id)

"""测试删除学生"""
# manager = StudentManagerController()
# manager.add_student(StudentModel("zs"))  # 在第一个位置上放zs
# manager.add_student(StudentModel("ls"))
# manager.remove_stu(1001)
# for item in manager.stu_list:
#     print(item.name, item.id, item.score)

"""测试修改学生信息"""


# manager = StudentManagerController()
# manager.add_student(StudentModel("zs"))  # 在第一个位置上放zs
# manager.add_student(StudentModel("ls"))
# manager.update_student(StudentModel("ww", 27, 89, 1001))
# print("修改后****")
# for item in manager.stu_list:
#     print(item.name, item.age, item.score, item.id)

class StudentManagerView:
    """
        学生管理视图
    """

    def __init__(self):  # 调实例方法用对象去点，对象创建根据不同需求来定
        self.__manager = StudentManagerController()  #

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
            if name=="":
                break
            age = int(input("请输入年龄"))
            score = int(input("请输入成绩"))
            stu = StudentModel(name, age, score)
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
        stu = StudentModel()
        stu.id = int(input("请输入需要修改的学生编号"))
        stu.name = input("请输入学生名称")
        stu.age = int(input("请输入学生年龄"))
        stu.score = int(input("请输入学生成绩"))
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __order_by_grade(self,stu_list):
        print("按成绩升序排列学生")
        order_num = stu_list
        list_num=self.__manager.list_count()
        # print(order_num)
        for item in range(list_num):
            for count in range(1, list_num - item):
                if order_num[item].score < order_num[item + count].score:
                    order_num[item].score, order_num[item + count].score = \
                        order_num[item + count].score, order_num[item].score
        for num in range(list_num):
            print(order_num[num].name,order_num[num].age,order_num[num].score,order_num[num].id)
#

view = StudentManagerView()
view.main()

# c=StudentManagerController()
# c.list_count()