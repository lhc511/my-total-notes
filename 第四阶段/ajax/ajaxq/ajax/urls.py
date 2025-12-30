from django.urls import path
from . import views
urlpatterns = [
    path('load_test/',views.load_test,name='load_test'),
    path('load_test_server/',views.load_test_server,name='load_test_server'),

    path('jquery_get/',views.jquery_get),
    path('jquery_get_server/',views.jquery_get_server),
    path('jquery_post_server/',views.jquery_post_server),
    path('jquery_post/',views.jquery_post),
    path('jquery_ajax_server/',views.jquery_ajax_server),
    path('jquery_ajax/',views.jquery_ajax),
    path('practice/',views.practice),
    path('practice_server/',views.practice_server),
    path('jquery_ajax_user/',views.jquery_ajax_user),
    path('jquery_ajax_user_server/',views.jquery_ajax_user_server),


    path('cross/',views.cross),
    path('cross_server/',views.cross_server),
    path('cross_server_json/',views.cross_server_json),
]