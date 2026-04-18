import pymysql
import hashlib

SALT = "%&Aid"


class Database:
    def __init__(self, host="localhost", port=3306, user="root", password="123", charset="utf8", database=None):
        self.cur = None
        self.db = None
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.charset = charset
        self.database = database
        self.connect_database()  # 连接数据库

    def close(self):
        self.db.close()

    def create_cursor(self):
        self.cur = self.db.cursor()

    # 连接数据库:
    def connect_database(self):
        self.db = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                  database=self.database, charset=self.charset)

    # 注册操作
    def register(self, name, passwd):
        sql = "select * from user where name='%s'" % name
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return False  # 用户存在

        hash1 = hashlib.md5((name + SALT).encode())  # 在原本的密码与新添的字符串拼接在加密
        hash1.update(passwd.encode())  # 加密处理
        passwd = hash1.hexdigest()  # 加盐后的密码

        # 插入数据库
        sql = "insert into user (name,password) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def login(self, name, passwd):

        # 要先转换成加密后的密码再进行比对
        hash1 = hashlib.md5((name + SALT).encode())  # 在原本的密码与新添的字符串拼接在加密
        hash1.update(passwd.encode())  # 加密处理
        passwd = hash1.hexdigest()  # 加盐后的密码
        print(passwd)
        # 数据库查找
        sql = "select * from user where name='%s' and password='%s'" % (name, passwd)
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False

    def query(self, word):
        sql = "select explatation from word where word='%s'" % word
        self.cur.execute(sql)
        r = self.cur.fetchone()
        # 如果找到就是一个元组
        if r:
            return r[0]

    def do_insert_hist(self, name, word):
        sql = "insert into wordrecord (name,word) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except Exception:
            self.db.rollback()

    def show_history(self, name):
        sql = "select * from wordrecord where name='%s'" % name
        try:
            self.cur.execute(sql)
            record = self.cur.fetchmany(10)
            if not record:
                return None
            return record
        except Exception:
            self.cur.rollback()
