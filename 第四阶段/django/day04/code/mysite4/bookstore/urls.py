from django.urls import path
from . import views
# from . import views 用于导入与当前目录（即 urls.py 文件所在目录）同级的 views.py 模块中的视图函数。
urlpatterns=[
    path('add_book',views.add_view),
    path('all',views.show_all),
    path('3author_inform',views.add_author),
    path('mod/<int:id>',views.mod_view),
    path('del/<int:id>',views.del_view),
    path('low_price',views.low_shows),
    path('contain',views.contain_show),
    path('lowed',views.lowprice),
    path('Qm',views.Q_method),
    path('set_cookie',views.set_cookies_view),
    path('get_cookie',views.get_cookies_view),
]
