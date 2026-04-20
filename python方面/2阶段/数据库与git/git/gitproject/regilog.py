import pymysql

"""我的"""
# db = pymysql.connect(host='localhost', port=3306, user='root', password='123', database='user', charset='utf8')
# cur = db.cursor()
#
#
# def repeat(user_name):
#     sql = "select name from user;"
#     cur.execute(sql)
#     data = cur.fetchall()
#     for item in data:
#         if item[0] == user_name:
#             return True
#     return False
#
#
# def login():
#     while True:
#         try:
#             user_name = input('请输入用户名')
#             if user_name == "":
#                 break
#             password = input("请输入密码：")
#             sql = "insert into user values (%s,%s);"
#             if not repeat(user_name):
#                 cur.execute(sql, [user_name, password])
#             else:
#                 print("用户名重复")
#             db.commit()
#         except:
#             db.rollback()
#
#
# login()
# # judge()

"""老师的"""
def register():
    name=input("用户名：")
    password=input("密码：")
    sql="select * from user where name='%s'"%name
    cur.execute(sql)
    result=cur.fetchone()
    if result:
        return False
    try:
        sql="insert into user (name,password) values (%s,%s)"
        cur.execute(sql,[name,password])
        db.commit()
        return True
    except:
        db.rollback()
        return False

def login():
    name = input("用户名：")
    password = input("密码：")
    sql="select * from user where name='%s' and password='%s'"%(name,password)
    cur.execute(sql)
    result=cur.fetchone()
    if result:
        return True



db = pymysql.connect(host='localhost', port=3306, user='root', password='123', database='stu', charset='utf8')
cur = db.cursor()
while True:
    print("""====================
            1.注册为        2.登陆
            =====================
    """)
    cmd=int(input("请输入命令"))
    if cmd==1:
        #注册
        if register():
            print("成功")
        else:
            print("失败")
    elif cmd==2:
        #登陆
        if login():
            print("登陆成功")
            break
        else:
            print("登陆失败")

    else:
        print("失败")