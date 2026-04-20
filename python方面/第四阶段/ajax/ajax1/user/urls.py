from django.urls import path
from . import views
urlpatterns = [
    path('xhr',views.xhr),
    path('get-xhr',views.get_xhr),
    path('get-xhr-server/',views.get_xhr_server),
    # path('showtext',views.showtext),
    # path('showtext_content',views.text),

    path('register/',views.register),
    path('checkuname/',views.checkuname),
    path('make_post/',views.make_post),
    path('get_user/',views.get_user),
    path('get_user_server/',views.get_user_server),

    path('json_obj/',views.json_obj),
    path('json_dumps/',views.json_dumps),
]
