from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("aaaaaaaaa")
    return render(request,'index.html')
def page1(request):
    return render(request,'page1.html')
def page2(request):
    return render(request,'page2.html')
def page3(request):
    return render(request,'page3.html')

def money(request):
    # shebao(request)
    return render(request,'money.html')

def shebao(request):
    # n是什么类型的
    # n = request.POST.get("base")
    n = int(request.GET.get("base"))
    # n=str(type(n))
    is_city=int(request.GET.get("is_city"))

    p1=n*0.08
    p21=n*0.002
    p20=0
    p3=0
    p4=0
    p5=n*0.02+3
    p6=n*0.12
    p_city_sum=p1+p21+p3+p4+p5+p6
    p_countryside_sum=p1+p20+p3+p4+p5+p6

    f1 = n * 0.19
    f21 = n * 0.008
    f20 = 0.008*n
    f3 = 0.005*n
    f4 = 0.008*n
    f5 = n * 0.1
    f6 = n * 0.12
    f_city_sum = f1 + f21 + f3 + f4 + f5 + f6
    f_countryside_sum = f1 + f20 + f3 + f4 + f5 + f6

    city_sum=f_city_sum+p_city_sum
    countryside_sum=f_countryside_sum+p_countryside_sum

    # return HttpResponse(n)
    if n:
        return render(request,'shebao.html',locals())
    return render(request,'money.html')