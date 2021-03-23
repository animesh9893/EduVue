from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home/<str:pk>',views.user_home,name="user_home")
]
