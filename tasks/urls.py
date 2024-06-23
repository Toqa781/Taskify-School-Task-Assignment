from django.urls import path
from . import views

urlpatterns = [
    path('', views.showTask , name='showTask'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('viewlist/' , views.viewlist, name='list'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('tasks/<int:task_id>/Edit.html', views.edit, name='edit'),
]
