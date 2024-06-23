from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
#from django.views import csrf_exempt
from myapp.models import User
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from .models import Task
@login_required
def showTask(request):
    try:
        tasks = Task.objects.filter(admin=request.user)
    except Exception as e:
        tasks = None
        print('Exception:' , e)  # Debugging line
        # You may want to log the error or display a more user-friendly message

    context = {
        'task': tasks,  # Pass tasks to the template context
    }
    
    return render(request, 'AdminHome/AdminHome.html', context)

@login_required
def viewlist(request):
    tasks = Task.objects.filter(admin=request.user)
    return render(request, 'viewlist.html', {'task': tasks})
    
from django.shortcuts import render, get_object_or_404
from tasks.models import Task

def task_detail(request,taskid):
    return render(request, 'task.html', {'Task': get_object_or_404(Task,id=taskid )})


