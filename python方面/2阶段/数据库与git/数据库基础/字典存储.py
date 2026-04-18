import re

import pymysql
a=1
f=open('/PythonProject/第二阶段/数据库与git/数据库基础/mysql/dict.txt', 'r')
db=pymysql.connect(host='localhost',port=3306,user='root',password='123',database='user',charset='utf8')
cur=db.cursor()
#自己的
# sql="insert into word values (%s,%s,%s)"
# for line in f:
#     # list_word.append(line.split(' ')[0])#将单词放在列表中
#     # list_interpret.append(line[17:])
#     word=line.split(' ')[0]
#     interpret=line[17:]
#     cur.execute(sql,[str(a),word,interpret])
#     a+=1
#     db.commit()
#老师的
sql="insert into word (word,explatation) values (%s,%s)"
for line in f:
    ######################
    # tmp=line.split(' ')
    # word=tmp[0]
    # interpret=' '.join(tmp[1:]).strip()#从第一个元素开始拼接并去掉空格
    # cur.execute(sql,[str(a),word,interpret])
    # a+=1
    #########正则表达式#################
    #当正则表达式有子组的时候只会以元组形式返回子组内容 (\S,\s)
    tup=re.findall(r"(\S+)\s+(.*)",line)[0]#返回一个元组,第一个元素是单词,第二个是解释
    try:
        cur.execute(sql,tup)
        db.commit()
    except:
        db.rollback()
db.close()
cur.close()
f.close()