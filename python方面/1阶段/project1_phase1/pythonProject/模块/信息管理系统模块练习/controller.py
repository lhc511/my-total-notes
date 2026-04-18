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
