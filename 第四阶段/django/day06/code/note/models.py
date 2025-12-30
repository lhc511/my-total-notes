from django.db import models

# Create your models here.
from django.db import models
from user.models import User

class Note(models.Model):
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    mod_time = models.DateTimeField('修改时间', auto_now=True)
    #note中的所有记录关联到一个User对象，即关联到每一个用户
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    # def __str__(self):
    #     return " : "+str(self.title)+" : "+str(self.content)+" : "+str(self.create_time)