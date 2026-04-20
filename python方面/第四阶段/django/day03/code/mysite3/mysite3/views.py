from django.http import HttpResponse
from django.shortcuts import render

def shebao_view(request):
    if request.method=="GET":
        method=request.method
        return render(request,'shebao.html',locals())
    elif request.method=="POST":
        method=request.method
        base=float(request.POST.get('base','0'))
        is_city=request.POST.get('base','1')#如果没获取到数据则默认为 "1"
        yl_gr=base*0.08
        yl_dw=base*0.19
        yl_dw=base*0.008
        if is_city=="1":
            sy_gr=base*0.002
        else:
            sy_gr=0
        return render(request,'shebao.html',locals())