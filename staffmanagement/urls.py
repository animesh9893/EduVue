from django.urls import path
from . import views

urlpatterns = [
    path('<username>/',views.staff_management,name="staff_management"),
]
