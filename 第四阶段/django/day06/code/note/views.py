from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from  django.core.paginator import Paginator
from user.models import User
from . import models
# Create your views here.

def check_login(fn):#此处的fn是下面用修饰器修饰的函数(@修饰器名  下面的函数)
    def wrap(request,*args,**kwargs):
        # 此处用于检查中间件的配置（settings文件中的middleware）
        if not hasattr(request, 'session'):  # 没有登陆(request中没有session属性)
            return HttpResponseRedirect('/user/login')
        # 此处用于检查用户登陆的业务逻辑(用户是否登陆)
        if 'user' not in request.session:  #
            return HttpResponseRedirect('/user/login')
        # **************  以上为装饰器为函数添加的功能代码  ***************

        return fn(request,*args,**kwargs)
    return wrap


# def list_view(request):
#     #此处用于检查中间件的配置（settings文件中的middleware）
#     if not hasattr(request,'session'):#没有登陆(request中没有session属性)
#         return HttpResponseRedirect('/user/login')
#     #此处用于检查用户登陆的业务逻辑(用户是否登陆)
#     if 'user' not in request.session:#
#         return HttpResponseRedirect('/user/login')
#     #此时已经登陆,并从服务端创建的session中取得当前
#     # 用户的id
#     user_id=request.session['user']['id']
#     #根据已经登陆的用户id 找到当前登陆的用户
#     auser=User.objects.get(id=user_id)
#     notes=auser.note_set.all()
#     return render(request,'note/showall.html',locals())

#拥有分页功能的笔记主页
def list2_view(request):
    #此处用于检查中间件的配置（settings文件中的middleware）
    if not hasattr(request,'session'):#没有登陆(request中没有session属性)
        return HttpResponseRedirect('/user/login')
    #此处用于检查用户登陆的业务逻辑(用户是否登陆)
    if 'user' not in request.session:#
        return HttpResponseRedirect('/user/login')
    #此时已经登陆,并从服务端创建的session中取得当前
    # 用户的id
    user_id=request.session['user']['id']
    #根据已经登陆的用户id 找到当前登陆的用户
    auser=User.objects.get(id=user_id)
    notes=auser.note_set.all()
    #在此处添加分页功能
    paginator=Paginator(notes,5 )
    #当进入页面时默认page=1
    cur_page=int(request.GET.get('page',1))
    # 该page是一个当前页面所有数据对象的集合
    page=paginator.page(cur_page)#显示第 cur_page 页的内容
    # page和page.object_list一样都是数据集合
    # return HttpResponse(page.object_list)
    return render(request, 'note/listpage.html', locals())

@check_login
#以下是被修饰的函数，传入修饰器中的fn
def add_view(request):
    if request.method=="GET":
        return render(request,'note/add_note.html')

    elif request.method=="POST":
        title=request.POST.get('title','')
        content=request.POST.get('content','')
        #得到当前用户信息(id)
        user_id=request.session['user']['id']
        #拿到了这个 id 的 -登陆用户对象
        auser=User.objects.get(id=user_id)

        #拿到了这个用户对象的笔记(1对多)，一个用户 对 多个笔记
        anote=models.Note(user=auser)
        anote.title=title
        anote.content=content
        anote.save()
        #anote必须要在save保存之后才能取得
        # return HttpResponse(anote)
        return HttpResponseRedirect('/note/')

@check_login
def mod_view(request,id):#此处的id相当于传的是 note.id 在showall模板中传递
    user_id = request.session['user']['id']
    # 根据已经登陆的用户id 找到当前登陆的用户
    auser = User.objects.get(id=user_id)

    # 找到当前用户 id=1 的笔记         此处返回集合。，所以用[0]索引来找
    note = auser.note_set.filter(id=id)[0]
    #方法二
    # anote=models.Note.objects.get(id=id,user=auser)

    # return HttpResponse(note.id)
    if request.method=="GET":
        return render(request,'note/mod_note.html',locals())
    elif request.method=="POST":
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        note.title = title
        note.content = content
        note.save()
        return HttpResponseRedirect('/note/')

def del_view(request,id):
    user_id = request.session['user']['id']
    # 根据已经登陆的用户id 找到当前登陆的用户
    auser = User.objects.get(id=user_id)
    #此处的id指的是数据库中记录的 笔记 的id
    anote = models.Note.objects.get(id=id, user=auser)
    anote.delete()
    return HttpResponseRedirect('/note')

def mod_password(request):
    if request.method=="GET":
        return render(request,'note/mod_password.html')
    if request.method=="POST":
        username=request.session['user']['username']
        user_id=request.session['user']['id']
        # return HttpResponse(username)
        oldpassword=request.POST.get("oldpassword")
        newpassword=request.POST.get("newpassword")
        newpassword_confirm=request.POST.get("newpassword_confirm")
        if newpassword!=newpassword_confirm or oldpassword==newpassword or oldpassword==newpassword_confirm:
            return HttpResponseRedirect('mod_password')
        else:
            user=User.objects.get(username=username,id=user_id)
            user.password=newpassword
            user.save()
            mod=1
            return render(request,'note/mod_password.html',locals())

