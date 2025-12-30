from django.urls import path
from . import views

urlpatterns=[
    path('news_page',views.news_page)

]
