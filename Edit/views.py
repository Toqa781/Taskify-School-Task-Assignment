from django.shortcuts import render

# from tasks.forms import TaskForm
from tasks.models import Task

# def edit(request,taskid):
#     edits = Task.objects.get(id=taskid)
#     form = TaskForm(instance=edits)
#     context = {'edits': edits}
#     return render(request, 'Edit.html', context)
