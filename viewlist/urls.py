from django.urls import path
from . import views

urlpatterns= [
    path('viewlist/',views.viewlist, name='list'),
    path('tasks/<int:taskid>/', views.task_detail, name='task_detail'),

]