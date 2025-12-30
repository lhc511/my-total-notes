import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User
# Create your views here.
def xhr(request):
    return render(request,'user/xhr.html')

# 请求时渲染一个静态页面，在页面上放一个按钮
def get_xhr(request):
    return render(request, 'user/get-xhr.html')

# 按下按钮后，js中的ajax通过对应路由拿回响应
def get_xhr_server(request):
    if request.GET.get('uname'):
        uname = request.GET['uname']
        return HttpResponse('welcome %s' % uname)
    return HttpResponse('is a xhr server')

def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        nickname=request.POST['nickname']
        if not uname:
            return HttpResponse("清输入用户名")
        if not pwd:
            return HttpResponse("清输入密码")
        if not nickname:
            return HttpResponse("清输入昵称")

        try:
            User.objects.create(uname=uname,pwd=pwd,nickname=nickname)
            return HttpResponse("注册成功")
        except:
            return HttpResponse("注册失败")

def checkuname(request):
    uname=request.GET.get('uname')
    users=User.objects.filter(uname=uname).all()
    if users:
        return HttpResponse("1")
    return HttpResponse('0')

def make_post(request):
    if request.method == 'GET':
        return render(request,'user/make_post.html')

    elif request.method == 'POST':
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        return HttpResponse("your post is ok %s %s"%(uname,pwd))
    else:
        raise

def get_user(request):
    return render(request,'user/get_user.html')

def get_user_server(request):
    users=User.objects.all()
    msg=''
    for u in users:
        msg+='%s_%s_%s|'%(u.uname,u.pwd,u.nickname)
    last_msg=msg[0:-1]
    return HttpResponse(last_msg)

def json_obj(request):
    return render(request,'user/json_obj.html')

def json_dumps(request):
    # 生成单个对像的json字符串/ 序列化 ->obj->str  把对像转化成字符串
    dic={
        'uname':'lili',
        'uage':'30',
    }
    # sort_keys = True  让输出的json串有序排列(按需求，不一定都用)
    json_str=json.dumps(dic,sort_keys=True,separators=(',',':'))
    # return HttpResponse(json_str)

    # 生成多个对象的json字符串
    s=[{
        'uname':'lili',
        'age':18,
    },
        {
            'uname': 'panghu',
            'age': 20,
        }
    ]
    json_str_array=json.dumps(s)

    # ********* django中的json转换字符串方法(不推荐)
    # from django.core import serializers
    # users=User.objects.all()
    # json_str_all=serializers.serialize('json',users)
    #
    # return HttpResponse(json_str_all,content_type='application/json')
    l=[]
    users=User.objects.all()
    for i in users:
        d={}
        d['uname']=i.uname
        l.append(d)
    json.dumps(l)
    return HttpResponse(json_str_array,content_type='application/json')
    # return JsonResponse(s)
