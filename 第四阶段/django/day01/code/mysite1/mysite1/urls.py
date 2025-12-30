"""
URL configuration for mysite1 project.

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
urlpatterns = [
    #页面的查询是从上而下依次查询，如果第二个查询到了就不会执行下面的
    # 同时只要包含匹配当中的内容就会查询到，比如:page2oiho,就会返回page2的页面
    path('admin/', admin.site.urls),
    path('',views.index_view),
    path('page1/',views.page1_view),
    path('page2/',views.page2_view),
    path('page<int:n>/',views.pagen_view),
    path('<int:num1>/<str:calculate>/<int:num2>/',views.method),
    # path('page<int:num1>/add/<int:num2>/',views.add),
    # path('page<int:num1>/sub/<int:num2>/',views.sub),
    # path('page<int:num1>/mul/<int:num2>/',views.mul),
    path("person/<str:name>/<int:age>/",views.person_view),
    path("birthday/<int:year>/<int:month>/<int:day>/",views.person_birthday),
    path("mypage/",views.mypage_view),
]
