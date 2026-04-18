from django.db import models

# Create your models here.

#出版社 一对多 中的 1
class Publisher(models.Model):
    name=models.CharField(max_length=50,verbose_name='出版社')
    def __str__(self):
        return '出版社' + self.name
#1对多 中的 多，此处意思为一个出版社出版多本书
class Book2(models.Model):
    title=models.CharField(max_length=30,verbose_name='书名')
    #                     外键对象   设置外键可为空
    pub=models.ForeignKey(Publisher,null=True,  on_delete=models.PROTECT)
    def __str__(self):
        return '书名2' + self.title