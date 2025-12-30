from django.db import models

# Create your models here.

#此处为多对多
class Author3(models.Model):
    name=models.CharField(max_length=30,verbose_name='姓名')

    def __str__(self):
        return '作家3：'+self.name
class Book3(models.Model):
    title = models.CharField(max_length=30, verbose_name='书名')

    #此处可以用来查询该书由哪几个作家编写
    authors=models.ManyToManyField(Author3)

    def __str__(self):
        return '作家3：' + self.title