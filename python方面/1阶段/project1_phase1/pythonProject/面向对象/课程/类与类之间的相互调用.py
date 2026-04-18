# class XXController:
#     def add_xx(self,a):
#         print("Controller 添加了数据",a)
#     @staticmethod
#     def fun01():
#         pass
#
#
# class XXView:
#     def __init__(self):
#         self.c=XXController()#将XXController赋值给 self.c(即该类中 自己的变量 c )
#     def input_xx(self):
#     # 需求:调用XXController类中的实例方法add_xx
#         self.c.add_xx(100)
#
# v=XXView()
# v.input_xx()


# class XXView:
# #需求:调用XXController类中的实例方法add_xx
#     def input_xx(self):
#         XXController.fun01()#调用类方法（用类名直接点）
#
#         c=XXController#调用实例方法，创建一个实例再去点
#         c.add_xx()
