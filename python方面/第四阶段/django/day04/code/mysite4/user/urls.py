from . import views
from django.urls import path, include

urlpatterns = [
    path('reg',views.reg_view)

]