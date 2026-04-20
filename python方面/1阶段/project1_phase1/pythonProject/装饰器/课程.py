"""
    装饰器
"""
# 定义:在不改变原函数的调用以及内部代码情况下，为其
# 2.语法
# def 函数装饰器名称(func):
#     def 内嵌函数(*args,**kwargs):
#         需要添加的新功能
#         return func (*args,**kwargs)
#     return wrapper,
# @函数装饰器名称。
# def 原函数名称(参数):
#     函数体

"""方法一"""
# # 需要增加的功能
# def verify_permissions(func):
#     def wrapper():
#         print("权限验证")
#         func()
#     return  wrapper
# # 已有功能
# def enter_background():
#     print("进入后台")
#
#
# def delete_order():
#     print("删除订单")
#
# enter_background= verify_permissions(enter_background)
# delete_order=verify_permissions(delete_order)
# enter_background()
# delete_order()
"""方法二"""

# 需要增加的功能
# 装饰器
# def verify_permissions(func):
#     def wrapper(*args, **kwargs):  # 形参中的 * 是把多个数据放到一个元组中
#         print("权限验证")
#         return func(*args, **kwargs)  # #实参中的 * 是把元组中的数据拆成多个数据
#
#     return wrapper
#
#
# # 已有功能
# # enter_background = verify_permissions(enter_background)   将新函数作为返回值赋值给 变量(与原函数名相同)，这里即wrapper
# @verify_permissions #会把所需的功能函数作为 参数 拦截传递给 装饰器
# def enter_background(login_in, pwd):
#     print("进入后台")
#
#
# # delete_order = verify_permissions(delete_order)
# @verify_permissions  # 在该函数调用时进行拦截  相当于上面， property 同理
# def delete_order(id):
#     print("删除订单", id)
#
#
# enter_background("abc",123)
# delete_order(101)


"""练习:在不该变原有功能(存取钱)的定义与调用情况下. 
增加验证账号的功能· 
"""

#
# def verify_permissions(func):
#     def wrapper(*args, **kwargs):
#         print("验证")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @verify_permissions
# def deposit(money):
#     print("存%d钱喽" % money)
#
#
# @verify_permissions
# def withdraw(login_id, pwd):
#     print("取钱喽", login_id, pwd)
#
#
# deposit(10000)
# withdraw("Zs", 123)
