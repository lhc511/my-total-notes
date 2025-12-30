
# 每次修改完数据都要做以下两步
#c
    # 会从installed_app里面向下检测若未发现modules有对应则向下一个app继续检测
    # 检测模型变化：
    #     Django 会检查你在 models.py 文件中对模型（Model）所做的更改，例如新增字段、修改字段类型、删除字段等。
    # 生成迁移文件：
    #     根据检测到的模型变化，生成一组迁移文件（通常存储在 migrations 文件夹中）。这些迁移文件是描述数据库结构变化的蓝图，包含了如何将数据库同步到最新模型状态的指令。
    # 准备数据库更新：
    #     它不会直接修改数据库，而是为后续的 python3 manage.py migrate 命令做好准备

#python3 manage.py migrate
    # python3 manage.py migrate 的作用是将数据库迁移文件中的更改应用到实际的数据库中。
