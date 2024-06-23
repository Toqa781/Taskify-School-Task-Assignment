from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='completed'),
    path('task/<int:task_id>/mark_as_done/', views.mark_as_done, name='mark_as_done'),
    path('task/<int:task_id>/', views.task, name='task'),
]
