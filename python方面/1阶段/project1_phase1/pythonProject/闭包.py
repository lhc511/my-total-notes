# 1.三要素:
#     必须有一个内嵌函数。
#     内嵌函数必须引用外部函数中变量。.
#     外部函数返回值必须是内嵌函数。
# def fun01():
#     a = 1
#
#     def fun02():
#         print(a)
#
#     return fun02
#     # 调用外部函数，返回值是内嵌函数


# result = fun01()  # 调用内嵌函数
# result()


# def give_gife_money(money):
#     print("得到了%d压岁钱" % money)
#
#     def child_buy(target, price):
#         nonlocal money
#         if money > price:
#             money -= price
#             print("孩子花了%.1f钱，购买了%s" % (price, target))
#         else:
#             print("钱不够")
#
#     return child_buy
#
# #下列代码是一个连续的逻辑
# action = give_gife_money(1000)
# action("asuo", 0.5)
# action("asuklsajo", 5000)
# action("asuusahdgo",6000)
