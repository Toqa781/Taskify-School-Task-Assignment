# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('AdminHome/', views.adminhome, name='admin_home'),
    path('availableTasks/', views.teacherhome, name='teacher_home'),

]
