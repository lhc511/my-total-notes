from django.http import HttpResponse,Http404
from django.shortcuts import render

# Create your views here.
def index_view(request):
    print('主页被访问')
    return HttpResponse("主页")

def page1_view(request):
    raise Http404
    return HttpResponse('页面1')