from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q,F
# Create your views here.
from . import models
def add_view(request):
    if request.method == "GET":
        return render(request, 'bookstore/add_book.html')
    elif request.method == "POST":
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = float(request.POST.get('price','0'))
        m_price = float(request.POST.get('m_price','0'))
        try:
            models.Book.objects.create(title=title,pub=pub,price=price,market_price=m_price)
            return HttpResponse('ok')
        except Exception as err:
            return HttpResponse('失败')

def show_all(request):
    books=models.Book.objects.all()
    #price=50是将 50赋值给price 再通过函数filter过滤，而price>50值是一个表达式(True/False),不能用于筛选
    # books=models.Book.objects.filter(price__gt=50)#表示筛选price大于50的的数据
    # books=models.Book.objects.filter(market_price__lt="40")#表示筛选price大于50的的数据
    # for abook in books:
    #     print("书名"+abook.title)
    return render(request,'bookstore/list.html',locals())

def mod_view(request,id):
    try:
        abook = models.Book.objects.get(id=id)
    except:
        return  HttpResponse('查询出错')
    if request.method=="GET":
        return render(request, 'bookstore/mod.html',locals())

    elif request.method=="POST":
        m_price=float(request.POST.get('m_price','0'))
        abook.market_price=m_price # 修改字端值
        abook.save()
        #在此处的与urls等网页展现方法一样，通过路径激活对应函数
        return HttpResponseRedirect('/bookstore/all')

def del_view(request,id):
    try:
        abook=models.Book.objects.get(id=id)
    except:
        return HttpResponse("失败")
    abook.delete()
    return HttpResponseRedirect('/bookstore/all')

def low_shows(request):
    if request.method=="GET":
        return render(request,'bookstore/low_price.html')
    elif request.method=="POST":
        price=request.POST.get('price')
        books=models.Book.objects.filter(market_price__lt=price)
        return render(request,'bookstore/low_price.html',locals())

def contain_show(request):
    if request.method=="GET":
        return render(request,'bookstore/contain_show.html')
    elif request.method=="POST":
        name=request.POST.get('name')
        books=models.Book.objects.filter(pub__contains=name)
        return render(request,'bookstore/contain_show.html',locals())

def lowprice(request):
    price = request.POST.get('price')
    books = models.Book.objects.filter(market_price__lt=F('price'))
    return render(request, 'bookstore/lowed.html', locals())

def Q_method(request):
    if request.method=="GET":
        return render(request, 'bookstore/Qmethod.html', locals())
    elif request.method=='POST':
        price = request.POST.get('price')
        pub=request.POST.get("pub")
        books = models.Book.objects.filter(Q(price__lt=price)&~Q(pub=pub))
    return render(request, 'bookstore/Qmethod.html', locals())

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

def set_cookies_view(request):
    resp=HttpResponse('ok')

    #在设置了具体过期时间后即使注释了该行代玛浏览器也不会删除已经添加的键值对
    resp.set_cookie('myvar',100,max_age=1000000)

    #通过键来删除浏览器cookies上的键值对
    # resp.delete_cookie('myvar')
    return resp
def get_cookies_view(request):
    #拿到cookies的值
    v=request.COOKIES.get('myvar')
    return HttpResponse('myvar='+v)