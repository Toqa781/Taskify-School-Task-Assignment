from django.urls import path
from . import views

urlpatterns= [
    path('availableTasks/',views.availableTasks),
    path('availableTasks/task/<int:task_id>/', views.available_task_detail, name='available_task_detail'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/mark_as_done/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_done/<int:task_id>/', views.mark_as_done, name='mark_as_done'),
]