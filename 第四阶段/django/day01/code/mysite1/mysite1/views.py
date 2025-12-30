from django.http import HttpResponse, HttpResponseRedirect

index_html='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <a href="/mypage?a=888&b=999">进入mypage</a>
    <form action="/mypage" method="get">
        <input type="text" name="a">
        <input type="text" name="b">
        <input type="submit" value="提交">
    </form>
</body>
</html>
'''

def index_view(request):
    return HttpResponse(index_html)


def page1_view(request):
    html = "<h1>这是一个web页面<h1>"
    return HttpResponse(html)


def page2_view(request):
    html = "<h1>这是2个web页面<h1>"
    return HttpResponse(html)


def pagen_view(request, n):  #"n"是字符串，因为从路由拆下来的都是字符串
    html = "<h1>=======这是%s个web页面<h1>" % n
    return HttpResponse(html)


# def add(request, num1, num2):
#     num = num1 + num2
#     html = '<h1>%d<h1>' % num
#     return HttpResponse(html)
#
#
# def sub(request, num1, num2):
#     num = num1 - num2
#     html = '<h1>%d<h1>' % num
#     return HttpResponse(html)
#
#
# def mul(request, num1, num2):
#     num = num1 * num2
#     html = '<h1>%d<h1>' % num
#     return HttpResponse(html)


def method(request, num1, calculate, num2):
    if calculate == "add":
        num = num1 + num2
        html = '<h1>===%d<h1>' % num
        return HttpResponse(html)
    elif calculate == "sub":
        num = num1 - num2
        html = '<h1>===%d<h1>' % num
        return HttpResponse(html)
    elif calculate == "mul":
        num = num1 * num2
        html = '<h1>===%d<h1>' % num
        return HttpResponse(html)
    else:
        return HttpResponseRedirect("https://www.baidu.com")
        # html = '出错了'
        # return HttpResponse(html)


def person_view(request, **kwargs):
    s = str(kwargs)
    return HttpResponse(s)


def person_birthday(request, year, month, day):
    # def person_birthday(request,**args):
    # return HttpResponse(args)
    s = "生日为:" + str(year) + "年"
    s += str(month) + "月"
    s += str(day) + "日"
    return HttpResponse(s)


def mypage_view(request):
    # 用来示意get请求中的查询参数
    if request.method == "GET":  #methond是request中的属性，通信方式
        # a = request.GET["a"]
        # a = request.GET.get("a",'没有对应的值')#如果没有传输a的值就设置为默认
        # b = request.GET.get("b",'没有对应的值')#如果没有传输a的值就设置为默认
        # html = "a=" + a+"b="+b

        a=request.GET.getlist("a")
        html="a="+str(a)
        # b = request.GET.getlist("b")
        # html="b="+str(b)

        # html=str(dict(request.GET))
        return HttpResponse(html)
    else:
        return HttpResponse("当前不是get请求")
