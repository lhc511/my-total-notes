# index/views.py
import os.path

from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'index/index.html',locals())

from django.http import HttpResponse
def test_view(request):
    print("test被调用")
    return HttpResponse("请求到了test")

from django.conf import settings
def upload_view(request):
    if request.method=="GET":
        return render(request,'index/upload.html')
    if request.method=="POST":
        # 得到input上传的文件
        a_file=request.FILES['myfile']
        print('收到上传的文件',a_file.name)
        #计算保存文件的位置
        filename=os.path.join(settings.MEDIA_ROOT,a_file.name)
        with open(filename,'wb') as fw:
            fw.write(a_file.file.read())
            return  HttpResponse(a_file.name)
        #得到文件数据
        return HttpResponse(a_file.name)

