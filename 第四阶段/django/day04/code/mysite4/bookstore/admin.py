from django.contrib import admin
from django.contrib.admin import ModelAdmin

from . import models
# Register your models here.
class BookManager(admin.ModelAdmin):
    list_display = ['id','title','pub','price','market_price']#展现字段对应的内容
    list_display_links = ['id','title']#让字段作为一个链接可以跳转到编辑页面
    list_filter = ['pub']#用出版社来过滤
    search_fields = ['title','pub']#创建一个搜索栏，可以在其中搜索相应字的值
    list_editable = ['market_price']

class AuthorManager(admin.ModelAdmin):
    list_display = ['id','name','age']

class WifeManager(admin.ModelAdmin):
    list_display = ['id','name','author']

admin.site.register(models.Book,BookManager)
admin.site.register(models.Author,AuthorManager)
admin.site.register(models.Wife,WifeManager)

