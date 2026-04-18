"""
列表助手模块
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """通用的查找某个条件的所有元素方法
        :param list_target:需要查找的列表
        :param func_condition:需要查找的条件，函数类型
                画数名(参数)一-> bo0l
        :return:需要查找的元素
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_name(target_object, target_name):
        return target_object.name == target_name

    @staticmethod
    def find_duration(target_object):
        return target_object.time > 0

    @staticmethod
    def find_id(target_object, target_id):
        return target_object.id == target_id

    @staticmethod
    def find_a(fun_l, target_list):
        for item in target_list:
            if fun_l(item):
                yield item
