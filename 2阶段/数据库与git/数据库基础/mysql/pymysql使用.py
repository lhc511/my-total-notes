import pymysql
#创建数据库
db=pymysql.connect(host='localhost',port=3306,user='root',password='123',database='stu',charset='utf8')
#获取游标
cur=db.cursor()
#执行sql语句
sql="insert into class_1 values (7,'Emma',17,'w',76.5,'2019-08-08')"
cur.execute(sql)
#提交
db.commit()#可以将一次或者多次的 命令操作 执行
#关闭
cur.close()
db.close()