
from django.http import HttpResponse

def experiment(request):
    pst=request.method
    # x = request.POST.get("x", "1")
    # op = request.POST.get("op", "add")
    # y = request.POST.get("y", "3")

    x = request.GET.get("x", "1")
    # op = request.GET.get("op", "add")
    op = request.GET.get("op", "add")
    y = request.GET.get("y", "3")
    if op == "add":
        result = str(int(x) + int(y))
        pst2=request.method
    elif op == "sub":
        result = str(int(x) - int(y))
        pst2 = request.method
    elif op == "mul":
        result = str(int(x) * int(y))
        pst2 = request.method
    else:
        result = str(int(x) / int(y))
        pst2 = request.method

    dic_var = {"x": x, "op": op, "y": y, "result": result,"pst":pst,"pst2":pst2}
    # dic_var={"op":op,"result":result}
    return render(request, 'experiment.html', dic_var)
    # return render(request,'experiment.html',dict1)

def sum_view(request):
# 127.0.0.1:8000/sum?start=1&stop=101&step=1
    if request.method == 'GET':
        try:
            # return HttpResponse(request.method)
            start = request.GET.get ('start', '0')
            start = int(start)
            # stop = request.GET.get('stop',"0")
            stop = request.GET['stop']
            stop = int(stop)
            step = request.GET.get ('step', '1')
            step=int(step)
            mysum=sum(range(start,stop,step))
            html=str(mysum)
            return HttpResponse(html)
        except Exception as err:
            return  HttpResponse("您给的查询字符串无效")
    # return HttpResponse("a")

login_form_html='''
    <form action='/login' method='post'>
        用户名:<input name='username' type="text">
        密码:<input name='password' type="text">
        <input type='submit' value='登陆'>
    </form>
'''

def login_view(request):
    if request.method=="GET":
        return HttpResponse(login_form_html)
    elif request.method=="POST":
        # return HttpResponse("a")
        name=request.POST.get('username','属性错误')
        html="姓名："+name
        # s=str(dict(request.POST))
        s=str(request.POST)
        html+=s
        # html=s
        return HttpResponse(html)

def login2_view(request):
    if request.method == 'GET':
        ##############方法一##################
        # # 返回模板生成的 html 给浏览器
        # # 方法1
        # #1.先加载模块
        # from django.template import loader
        # t=loader.get_template('mylogin.html')#通过settings中templates的dirs来加载并绑定到变量t
        # #2. 用模板生成html
        # html=t.render({'name':'tarena'})#最终在html页面上的{{ name }}默认值会变成 tarena
        # # 3. 将html 返回给浏览器
        # return HttpResponse(html)

        #############方法二################
        from django.shortcuts import render
        return render(request,"mylogin.html",{"name":"lalalal"})

def say_hello():
    return "你号"

class Dog:
    def say(self):
        return "汪汪"

from django.shortcuts import render
def test_view(request):
    s="hello world"
    lst=['aa','bb','cc']
    mydic={'name':'tedu','age':20}
    dic={"s":s,'lst':lst,'mydic':mydic,'say_hello':say_hello,'dog1':Dog()}
    # dic={"s":s,'lst':lst,'mydic':mydic,}
    return render(request,'mytest.html',dic)

def mytemp_view(request):
    # dic={"x":0}
    # return render(request,'mytemp.html',dic)
    x = 7
    return render(request,'mytemp.html',locals())

def mycal_view(request):
    # return HttpResponse(request.method)
    if request.method=="GET":
        return render(request,'count.html')

    if  request.method=="POST":
        x=request.POST.get("x","1")
        op=request.POST.get("op","add")
        y=request.POST.get("y","3")
        if op=="add":
            result=str(int(x)+int(y))
        elif op=="sub":
            result=str(int(x)-int(y))
        elif op=="mul":
            result=str(int(x)*int(y))
        else:
            result=str(int(x)/int(y))

        dic_var={"x":x,"op":op,"y":y,"result":result}
        # dic_var={"op":op,"result":result}
        return render(request,'count.html',dic_var)
        # return render(request,'count.html',locals())


def for_view(request):
    lst=['北京','上海','天津']
    s="<i>hello</i>"
    n=100
    s2="aa bb cc dd ee"
    return render(request,'for_view.html',locals())

def index_view(request):
    return render(request,'base.html')

def sport_view(request):
    return render(request,'sport.html')
def news_view(request):
    return render(request,'news.html')

def pagen_view(request,n):
    return HttpResponse("第"+n+"页")