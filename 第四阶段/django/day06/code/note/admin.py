from django.contrib import admin

# Register your models here.
from . import models
class NoteManager(admin.ModelAdmin):
    list_display = ['id','title','user']
admin.site.register(models.Note,NoteManager)
