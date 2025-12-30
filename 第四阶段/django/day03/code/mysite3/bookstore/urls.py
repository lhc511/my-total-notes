from django.urls import path
from . import views
# from . import views 用于导入与当前目录（即 urls.py 文件所在目录）同级的 views.py 模块中的视图函数。
urlpatterns=[
    path('add_book',views.add_view),
    path('3author_inform',views.add_author)

]