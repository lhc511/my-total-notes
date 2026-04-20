import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def load_test(request):
    return render(request,'ajax/load_test.html')

def load_test_server(request):
    return render(request,'ajax/load_test_server.html')

def jquery_get(request):
    # uname=request.GET.get('uname')
    # age=request.GET.get('age')
    # print(uname,age)
    return  render(request,'ajax/jquery_get.html')

def jquery_get_server(request):
    uname=request.GET.get('uname')
    age=request.GET.get('age')
    print(uname,age)
    d={'uname':uname,'age':age}
    return  HttpResponse(json.dumps(d),content_type='application/json')

def jquery_post(request):
    return render(request,'ajax/jquery_post.html')

def jquery_post_server(request):
    if int(request.POST.get('age'))>100:
        d = {'msg': 'wrong', 'code': 1200}
        return HttpResponse(json.dumps(d), content_type='application/json')
    # code是自定义的编码，比如1201代表了某一个函数功能
    d={'msg':'post is ok','code':1201}
    return HttpResponse(json.dumps(d),content_type='application/json')
def jquery_ajax(request):
    return  render(request,'ajax/jquery_ajax.html')

def jquery_ajax_server(request):
    import time
    time.sleep(3)
    d={'name':"guoxiaonao","age":18}
    return  HttpResponse(json.dumps(d),content_type='application/json')

def practice_server(request):

    name=request.GET['name']
    age=request.GET['age']
    return HttpResponse(json.dumps({'name':name,'age':age}),content_type='application/json')

def practice(request):
    return render(request,'ajax/pratice.html')

def jquery_ajax_user(request):
    return render(request,'ajax/jquery_ajax_user.html')

def jquery_ajax_user_server(request):
    d=[{'name': "guoxiaonao", "age": 18},{'name': "laowei", "age": 78}]
    return HttpResponse(json.dumps(d),content_type='application/json')



def cross(request):
    return render(request,'ajax/cross.html')

def cross_server(request):
    func=request.GET.get('callback')
    print(type(func))
    print(func)
    # return HttpResponse(func+"('我夸出来了')")#func(str)
    # 此处返回一段js代码
    return HttpResponse(func+"('我夸出来了')",content_type='text/javascript')#func(str)

def cross_server_json(request):
    func=request.GET.get('callback')
    d={'name': "guoxiaonao", "age": 18}
    return HttpResponse(func+"("+json.dumps(d),content_type='text/javascript')