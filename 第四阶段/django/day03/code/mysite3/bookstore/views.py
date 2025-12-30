from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models
def add_view(request):
    try:
        # # 方法一
        # abook=models.Book.objects.create(title="c++",price=68)
        # return HttpResponse('添加图书成功')

        # 方法二
        # abook=models.Book(price=98)
        # abook.title='c++1'
        # abook.save() #  真正执行sql语句
        # return HttpResponse('添加图书成功')

        return HttpResponse('添加图书成功')
    except Exception as err:
        return HttpResponse('失败')

def add_author(request):
    try:
        if request.method=="GET":
            return render(request, "3author_inform.html")

        elif request.method=="POST":
            name=request.POST.get('name')
            age=request.POST.get('age')
            email=request.POST.get('email')
            author=models.Author.objects.create(name=name,age=age,email=email)
            return render(request, "3author_inform.html")

    except Exception as err:
        return HttpResponse("加载失败")

