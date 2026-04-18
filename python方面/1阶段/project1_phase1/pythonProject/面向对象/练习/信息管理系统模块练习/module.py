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