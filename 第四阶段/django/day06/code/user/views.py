from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import models
from . import forms

# 导入django中的模型类User
from django.contrib.auth.models import User


# Create your views here.
def reg_view(request):
    dic = request.COOKIES
    print('COOKIES=', str(dic))

    if request.method == "GET":
        return render(request, 'user/register.html')
    elif request.method == "POST":
        username = request.POST.get('username', '')
        password1 = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        # 验证用户名长度
        if len(username) < 6:
            username_error = '用户名太短'
            return render(request, 'user/register.html', locals())
        # 验证密码是否为空
        if not password1:
            password_error = '密码不能为空'
            return render(request, 'user/register.html', locals())
        # 两次密码是否一致
        if password1 != password2:
            password2_error = "密码不一致"
            return render(request, 'user/register.html', locals())
        try:
            auser = User.objects.get(username=username)
            username_error = '用户名已经存在'
            return render(request, 'user/register.html', locals())
        except:
            # 创建超级用户,django会自动帮忙进行加密
            asuer = User.objects.create_superuser(username=username, password=password1, email="")

            # 创建普通用户
            # asuer=User.objects.create_user(username=username,password=password1)
            html = """注册成功<a href='/user/login'>进入登陆</a>"""
            resp = HttpResponse(html)
            # 在cookies中将 username变量 当中的值 存储到 浏览器中叫username的键中
            resp.set_cookie('username', username)
            return resp

        # #数据库中是否已存在该用户名,若没有则完成注册
        # try:
        #     auser=models.User.objects.get(username=username)
        #     username_error='用户名已经存在'
        #     return render(request,'user/register.html',locals())
        # except:
        #     asuer=models.User.objects.create(username=username,password=password1)

        #     html="""注册成功<a href='/user/login'>进入登陆</a>"""
        #     resp= HttpResponse(html)
        #     #在cookies中将 username变量 当中的值 存储到 浏览器中叫username的键中
        #     resp.set_cookie('username',username)
        #     return resp


def login_view(request):
    if request.method == 'GET':
        # username = request.COOKIES.get('username', '')
        return render(request, 'user/login.html', locals())
    elif request.method == "POST":
        username = request.POST.get('username', '')
        password1 = request.POST.get('password', '')
        if username == '':
            username_error = '不能唯空'
            return render(request, 'user/login.html', locals())
# ***************   django的admin管理系统的表      ********************
        # try:
        #     # 从服务端获取该用户对像
        #     auser = models.User.objects.get(username=username)#笔记用户中的表的用户对像
        #     # return HttpResponse(auser)
        #     # auser = User.objects.get(username=username) #django管理系统admin中的auth_user表的用户对像
        #     # 检查用户密码是否与数据库一致(该处的函数用于将输入的密码转换成加密的字符串再与数据库中的密码(经加密)进行比对)
        #     if auser.check_password(password1):
        #         # 记录一个登陆状态，登陆后在服务端创建一个键值对
        #         request.session['user'] = {
        #             'username': username,
        #             'id': auser.id  # 记录用户当前的id
        #         }
        #
        #         resp = HttpResponseRedirect('/')
        #
        #         # 当request.POST的字典集中有'remember'时，将cookies中的数据重新设置
        #         # 当html标签中form表单中的name值提交到cookies，说明被选择要记住
        #         if 'remember' in request.POST:
        #             resp.set_cookie('username', username)
        #         return resp
        #     else:
        #         password_error = '密码错误'
        #         return render(request, 'user/login.html', locals())
        # except:
        #     password_error = '密码错误'
        #     return render(request, 'user/login.html', locals())

# ***************  笔记用户的表*******************
        try:
            #从服务端获取该用户对像
            auser=models.User.objects.get(username=username,password=password1)

            #记录一个登陆状态，登陆后在服务端创建一个键值对
            request.session['user']={
                'username':username,
                'id':auser.id#记录用户当前的id
            }
            resp=HttpResponseRedirect('/')
            #当request.POST的字典集中有'remember'时，将cookies中的数据重新设置
            if 'remember' in request.POST:
                resp.set_cookie('username',username)
            return resp
        except:
            password_error='密码错误'
            return render(request,'user/login.html',locals())


def logout_view(request):
    if 'user' in request.session:
        del request.session['user']
    return HttpResponseRedirect('/')  # 返回主页


def reg2_view(request):
    if request.method == 'GET':
        myform1 = forms.MyRegForm()
        return render(request, 'user/reg2.html', locals())
    elif request.method == "POST":
        # 直接传递一个字典，对应类中的属性
        myform = forms.MyRegForm(request.POST)
        if myform.is_valid():  # 该处的验证环节会在forms里面定义的函数内完成
            # cleaned_data会过滤掉一些无用的键值对，此处过滤掉csrf验证
            dic = myform.cleaned_data
            username = dic['username']
            password1 = dic['password']
            password2 = dic['password2']

            # 表单验证
            return HttpResponse(str(dic))
        else:
            return HttpResponse("验证失败")

            # if len(username)<6:
            #     return HttpResponse('用户名太短')
            # return HttpResponse(str(dic))
        # if len(username)<6:
        #     return HttpResponse("用户名太短")

        # 通过form表单模块来提交返回函数
        # dic=dict(request.POST)
        # return HttpResponse(str(dic))
    # as_p()会自动生成html文档,p是指用p标签来分隔每一个文本框
    # html=myform1.as_p()
    # print(html)
    # return HttpResponse(html)

    # 设置session的值
    # request.session['abc']=123
    #
    # #获取session的值
    # val=request.session.get('abc')
    # print(val)
    # return HttpResponse('ok')
