"""
URL configuration for mysite3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include
# 主路由配置文件

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shebao', views.shebao_view),
    # include函数用于实现分布式路由，当网址匹配到music应用就会自动跳转到music中的urls路径
    # 并寻找对应视图函数，并且第一个就是 应用 名称
    # 此处必须加斜杠，因为查找时的网址就是通过斜杠作为分割逐级下找，并在主路由中通过路由分布将关键字过滤然后再找

    path('music/', include('music.urls')),
    path('news/', include('news.urls')),
    path('sport/', include('sport.urls')),
    path('bookstore/', include('bookstore.urls')),

]
