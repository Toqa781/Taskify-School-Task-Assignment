from django.urls import path
from . import views
from tasks.models import Task

urlpatterns = [

    path('',views.showPage,name='showPage'),
    path('save/',views.SaveData,name='SaveData')
    
]
