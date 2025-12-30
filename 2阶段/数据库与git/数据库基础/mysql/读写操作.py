import pymysql
#创建数据库
db=pymysql.connect(host='localhost',port=3306,user='root',password='123',database='stu',charset='utf8')
#获取游标
cur=db.cursor()
#从数据库读取
sql="select * from class_1 where gender='m'"
cur.execute(sql)

"""每获取一个相当于迭代一个，会从前一个迭代对象的下一个继续查找"""
#获取一个查询结果
# one_row =cur.fetchone()
# print(one_row)#元组 (2, 'Baron', 18, 'm', 93.0, datetime.date(2020, 2, 29))
# print(one_row[5])#2020-02-29
#获取多个查询结果
# many_row=cur.fetchmany(2)#获取两个 元组套元组
# print(many_row)#((3, 'Levi', 19, 'm', 90.0, datetime.date(2019, 6, 18)), (6, 'Jame', 17, 'm', 90.5, datetime.date(2020, 4, 28)))
# 获取所有查询结果
# all_row=cur.fetchall()
# print(all_row)

"""通用做法1：需要与数据库表格中的数据类型相对应"""
# try:
#     写sql语句执行
    # name=input('name:')
    # age=int(input('age:'))
    # score=float(input('score:'))
    # sql="insert into class_1 (name,age,score) values ('%s',%d,%f)"%(name,age,score)
    # print(sql)
    # cur.execute(sql)
    # db.commit()

"""通用做法2方便"""
try:
    #写sql语句执行
    # name=input('name:')
    # age=input('age:')
    # score=input('score:')

    #添加
    # sql="insert into class_1 (name,age,score) values (%s,%s,%s)"
    # cur.execute(sql,[name,age,score])#列表只能给value传值
    #修改
    # sql="update interest set price=11800 where name = 'Abby'"
    # cur.execute(sql)
    #删除
    sql="delete from class_1 where score<80"
    cur.execute(sql)
    db.commit()


except Exception as e:
    db.rollback()#退回到commit执行之前的数据库状态
    print(e)

#关闭(
cur.close()
db.close()