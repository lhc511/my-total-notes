class Double_list_helper:
    # # 获取指定位置，指定方向，指定数量的元素
    @staticmethod
    def get_elements_ud(target, vect_pos, vect_dir, count):  # (目标列表，二维列表的元素位置，元素方向，指定的个数)
        """

        :param target: 目标列表
        :param vect_pos: 二维列表的元素位置
        :param vect_dir: 元素方向
        :param count: 指定的个数
        :return: 最终列表
        """
        list_result = []
        for item in range(count):
            vect_pos.x += vect_dir.x  # 只是对数字的引用，用于下面对列表进行定位
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]  # 寻找二维列表中元素位置返还给element
            list_result.append(element)
        return list_result


# 意为：倘若从该文件执行代码做调试或理解，则进入执行代码，若仅仅调用该文件则不执行代码（方便别人理解代码）
# #以下为测试代码，只有从当前模块运行才开始运行
if __name__ == "__main__":
    le = Double_list_helper.get_elements_ud(list01, Vector2(1, 3), Vector2.left(), 3)  # 在调用函数是一定要加括号
    up = Double_list_helper.get_elements_ud(list01, Vector2(2, 2), Vector2.up(), 2)
    down = Double_list_helper.get_elements_ud(list01, Vector2(0, 3), Vector2.down(), 2)
    print()
    print(le)
    print(up)
    print(down)
