from django.contrib import admin

# Register your models here.
#将模型类注册到后台管理
from . import models
admin.site.register(models.Author3)
admin.site.register(models.Book3)