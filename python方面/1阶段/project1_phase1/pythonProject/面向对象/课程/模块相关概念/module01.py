__all__ = ["fun01", "Myclass", "_fun02"]  # 定义可导出成员，在列表内的以字符串形式做表现出的 python代码，在列表内的才能被导出
print("模块一")

print(__name__)  # module01
# 限制，只有从当前模块运行才可以（主模块代码）
# 测试代码：不是主模块不执行


def fun01():
    print("模块一的fun01")


# 只在模块内部的成员可以以但下划线开头,只限于 * 形式的调用有效
# 能够剔除不需要的函数（在调用时）
def _fun02():
    # 可以通过其他形式调用隐藏成员
    print("模块一的fun02")


class Myclass:
    @staticmethod
    def fun03():
        print("Myclass02--fun03")
