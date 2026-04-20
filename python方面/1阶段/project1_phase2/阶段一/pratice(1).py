"""
一段文字中有()[]{}，编写一个接口程序判断括号是否匹配正确
"""
from link_stack import *

text = "The core (of) extensible  programming [[is] defining functions. Python allows {mandatory [and]} " \
       "optional (arguments,{keyword} arguments), and even arbitrary argument lists."
# 将验证条件提前定义好
parens = "()[]{}"  # 特殊处理的字符集
left_parens = "([{"  # 入栈字符集
# #验证匹配关系
opposite = {'}': '{', ']': '[', ')': '('}
ls = LStack()  # 存储括号的栈


# 函数作用：寻找段落中的所有括号 并返回括号和括号所在位置
def parent(text):
    # i 遍历字符串的索引位置
    i, text_len = 0, len(text)

    # 开始遍历字符串
    while True:
        while i < text_len and text[i] not in parens:  # 翻译：在字符串内部并且不属于桑括号
            i += 1
        # 到字符串结尾了
        if i >= text_len:
            return
        else:
            yield text[i], i
            i += 1


for i, j in parent(text):
    print(i, j)


# 功能函数:判断提供的括号是否匹配
def ver():
    # 调用生成器 （里面的都是元组） 元组第一个位置上是 括号字符 第二个位置是 位置索引
    for pr, i in parent(text):  # pr:括号，索引 parent(text)找出的是括号

        if pr in left_parens:  # 如果属于左括号那就入栈

            ls.push((pr, i))  # (左括号(这个字符)，索引) 一个元组  入栈

        # 如果链表是空或者 弹出的元组中的第一个数据(即段落中字符)
        # opposite = {'}': '{', ']': '[', ')': '('}

        #                        通过 键右括号 找值左括号
        # 在 只有右括号(此时栈中无数据) 或者便利括号的过程中如果在遍历到 右括号 时链表栈中添加的最后一个左括号与之对应的左括号
        elif ls.is_empty() or opposite[pr] != ls.pop()[0]:  # 如果栈是空的  (此时pr为段落中的 当前的右括号)
            print("Unmatching is found at %d for %s" % (i, pr))  # (位置，字符) #没有在i位置找到 该字符
            break  # python当中的语法:在退出循环之后，下方的 else 和上方的 if elif 是同一组
    else:
        if ls.is_empty():
            print("all parentheses are matched")
        else:
            # 左括号多了
            d = ls.pop()  # 这里弹出的是一个元组
            print("Unmatching is found at %d for %s" % (d[1], d[0]))


ver()
