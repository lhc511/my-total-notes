""""二进制存储文件"""
import pymysql
#创建数据库
db=pymysql.connect(host='localhost',port=3306,user='root',password='123',database='stu',charset='utf8')
#获取游标
cur=db.cursor()
#存储图片
# with open('image.jpg','rb') as f:
#     data=f.read()
#
# try:
#     sql="update class_1 set image = %s where name='Jame'"
#     #执行sql语句
#     cur.execute(sql,[data])
#     db.commit()
# except:
#     db.rollback()
#获取图片
sql="select image from class_1 where name='Jame'"
cur.execute(sql)
data=cur.fetchone()
with open('girl.jpg', 'wb') as f:
    f.write(data[0])
#提交
db.commit()#可以将一次或者多次的 命令操作 执行
#关闭
cur.close()
db.close()