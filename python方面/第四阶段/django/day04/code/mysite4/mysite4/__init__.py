import pymysql
pymysql.version_info = (2, 2, 7, "final", 0)  # 将版本信息设置为1.4.3
pymysql.install_as_MySQLdb()