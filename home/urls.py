from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home/<str:pk>',views.user_home,name="user_home"),
    path('about_us/',views.about_us,name="about_us"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('pricing/',views.pricing,name="pricing"),
    path('payment/',views.payment,name="payment"),
    path('staffredirect/',views.staffredirect,name="staffredirect"),
]
