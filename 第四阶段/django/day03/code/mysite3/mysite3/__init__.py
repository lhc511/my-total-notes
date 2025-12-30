# 该文件在进入这个包时u一定会先执行一次 init————>initial

import pymysql

#让django用pymysql对mysql服务器进行操作
pymysql.install_as_MySQLdb()