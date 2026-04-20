"""
URL configuration for mysite2 project.

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
# from .views import sum_view
from . import views
urlpatterns = [
    path('experiment', views.experiment),
    path('admin/', admin.site.urls),
    path('sum/', views.sum_view),
    path('login', views.login_view),
    path('login2', views.login2_view),
    path('test', views.test_view),
    path('test2', views.mytemp_view),
    path('mycal', views.mycal_view),
    path('test_for',views.for_view),
    path('',views.index_view),
    path('sss',views.sport_view,name='sport'),
    path('news',views.news_view),
    path('page<str:n>',views.pagen_view,name='pagen'),
]