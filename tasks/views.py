from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def showTask(request):
    try:
        tasks = Task.objects.filter(admin=request.user)
    except Exception as e:
        tasks = None
        print('Exception:', e)
        # You may want to log the error or display a more user-friendly message

    context = {
        'task': tasks,  # Pass tasks to the template context
    }
    
    return render(request, 'AdminHome/AdminHome.html', context)

    
def task_detail(request,taskid):
    return render(request, 'task.html', {'Task': get_object_or_404(Task,id=taskid )})

def viewlist(request):
    return render(request, 'viewlist.html')


def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('showTask')
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@login_required
def edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': '', 'task_id': task_id})
            else:
                messages.success(request, '')
                return redirect('task_detail', task_id=task_id)
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
            else:
                messages.error(request, 'Form validation failed. Please check the input fields.')
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task
    }
    return render(request, 'Edit.html', context)