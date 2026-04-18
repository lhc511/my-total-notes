"""该模块实现music应用的子路由配置"""

from django.urls import path
from . import views


# 分布式路由的子路由名称要和主路由名称保持一致，即都为urlpatterns
urlpatterns=[
    path('page1',views.page1_view),
    path('page2',views.page2_view),
    path('page3',views.page3_view),
]