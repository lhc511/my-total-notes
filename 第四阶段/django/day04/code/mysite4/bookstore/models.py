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
    title = models.CharField(max_length=30,null=False,unique=True,verbose_name="书名")  #CharField(max_length=30)相当于varchar(30),db_index=True用于自动添加索引

    # pub_date=models.DateField(auto_now=True)#自动填充当前时间
    # pub_date=models.DateField(default="1987-09-07")#填充默认值
    # 而一个对象相当于一条记录i
    pub=models.CharField(max_length=50,verbose_name="出版社",null=True)

    # default为新添加字段所必须填写的默认值，或者为 null=True
    price = models.DecimalField(decimal_places=2, max_digits=7, default='99999', verbose_name="定价")  # 最多有七位数，最多有两个小数位
    market_price=models.DecimalField(decimal_places=2,max_digits=7,default='99999',verbose_name='零售价')

    def __str__(self):#用于将被显示的对象以 制定的形式(下方)输出
        return '书名:' + self.title

class Author(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(verbose_name='年龄',default=1)
    email=models.EmailField(verbose_name='邮箱',default='xxx@yyy.zz')

    def __str__(self):
        return '作者：'+self.name

    # class Meta:
    #     db_table='myauthor'

class Wife(models.Model):
    name=models.CharField(max_length=30,verbose_name='姓名',default='无')
    author=models.OneToOneField(Author,on_delete=models.CASCADE)
