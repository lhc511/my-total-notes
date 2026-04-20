from django.db import models


# Create your models here.

#orm关系映射
# 一个类相当于一张表
class Book(models.Model):
    # objects = models.Manager()  # 必须添加，确保 objects 属性可用[^1]

    # 当向已有数据的Django模型添加非空字段时，数据库需要为现有的所有记录填充该字段的值。
    # 如果未提供默认值（default），Django无法确定如何填充旧数据，从而抛出错误：

    #此处相当于定义了两个字段
    # 字段名=modules.字段类型(字段选项)
    title = models.CharField(max_length=30,db_index=True,db_column="shuming")  #CharField(max_length=30)相当于varchar(30),db_index=True用于自动添加索引

    # default为新添加字段所必须填写的默认值，或者为 null=True
    price = models.DecimalField(decimal_places=2,max_digits=7,default='0.00')#最多有七位数，最多有两个小数位
    # pub_date=models.DateField(auto_now=True)#自动填充当前时间
    # pub_date=models.DateField(default="1987-09-07")#填充默认值
    # 而一个对象相当于一条记录i
    pub=models.CharField(max_length=50,default='无')
    market_price=models.DecimalField(decimal_places=2,max_digits=7,default='0.00')

class Author(models.Model):
    name=models.CharField(max_length=20,default='null')
    age=models.IntegerField(default=1)
    email=models.EmailField(max_length=30)