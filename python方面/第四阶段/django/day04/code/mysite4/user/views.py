from django.http import HttpResponse
from django.shortcuts import render
from . import models
# Create your views here.
def reg_view(request):
    if request.method=='GET':
        return render(request,'register.html')
    elif request.method=="POST":
        user=request.POST.get('user')
        password=request.POST.get('password')
        password_confirm=request.POST.get('password_confirm')
        try:
            models.User.objects.create(username=user,password=password)
            responds=HttpResponse('ok')
            responds.set_cookie('username',user)
            return responds
        except:
            return HttpResponse("失败")


