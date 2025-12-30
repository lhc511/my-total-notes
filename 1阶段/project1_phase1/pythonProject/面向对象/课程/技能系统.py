class SkillImpactEffect:
    """
        技能影响效果
    """

    def impact(self):
        raise NotImplementedError()


class DamageEffect(SkillImpactEffect):
    """
        伤害生命效果
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print("扣你%d血" % self.value)


class LowerDefenseEffect(SkillImpactEffect):
    """
        降低防御力
    """

    def __init__(self, value, time):
        self.value = value
        self.time = time

    def impact(self):
        print("降低%d防御力，持续%d秒" % (self.value, self.time))


class DizzinessEffect(SkillImpactEffect):
    """
        降低防御力
    """

    def __init__(self, time):
        self.time = time

    def impact(self):
        print("眩晕%d秒" % self.time)


class SkillDeployer:
    """
        技能释放器
    """

    # 生成技能(执行效果)
    def __init__(self, name):
        self.name = name
        # 加载配置文件[技能名称:[效果1，效果2...],.:
        self.__dict_skill_config = self.load_config_file()
        # #创建效果对象  也就是不同效果互相组合形成的技能
        self.__effect_object = self.creat_effect_objects()

    def load_config_file(self):
        # 加载文件
        # 返回了两个字典
        return {
            "降龙十八掌": ["DamageEffect(200)", "LowerDefenseEffect(-10,5)", "DizzinessEffect(6)"],
            "六脉神剑": ["DamageEffect(100)", "DizzinessEffect(6)"]
        }

    def creat_effect_objects(self):
        # 根据name创建相应的技能对象
        # 降龙十八掌——>[技能一,技能二]
        list_effect_name = self.__dict_skill_config[self.name]  # self.name 是在建立对象时传入的参数，访问文件中的键，赋值列表
        list_effect_object = []
        for item in list_effect_name:
            # "技能一"————>技能一的对象
            # eval("DamageEffect(200)")
            list_effect_object.append(eval(item))  # 以python代码形式添加传入字典中列表的对象
        return list_effect_object  # 最终该列表中都是技能效果（例如造成伤害，眩晕等等），并在最后返回

    # 生成技能（执行效果）
    def generate_skill(self):
        print(self.name, "技能释放")  # 传入的技能名字
        for item in self.__effect_object:  # 列表中的技能小郭
            item.impact()


xlsbz = SkillDeployer("降龙十八掌")
xlsbz.generate_skill()

lmsj = SkillDeployer("六脉神剑")
lmsj.generate_skill()
