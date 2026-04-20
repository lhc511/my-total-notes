class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration


list_skill = [SkillData(101, "乾坤大挪移:", 5, 10), SkillData(102, "降龙十八掌", 8, 5), SkillData(103, "葵花宝典", 10, 2)]


# 练习1:获取攻击比例大于6的所有技能 #要求:使用生成器函数/生成器表达式完成
# def fun01():
#     for item in list_skill:
#         if item.atk_ratio > 6:
#             yield item
#
#
# a = fun01()
# print(type(a))
# for item01 in a:
#     print(item01.atk_ratio)
# b=(item for item in list_skill if item.atk_ratio>6)
# for item in b:
#     print(item.atk_ratio)
#
#
def fun02():
    for item in list_skill:
        if item.duration < 6 and 4< len(item.name):
            yield item


a = fun02()
print(type(a))
for item01 in a:
    print(item01.duration)
b=(item for item in list_skill if item.duration<6 and 4< len(item.name))
for item in b:
    print(item.name)