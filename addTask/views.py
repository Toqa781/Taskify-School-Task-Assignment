from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.models import Task


@login_required
def showPage(request):
    admin_username = request.user
        

    # Retrieve the latest task created by the admin user
    task = Task.objects.filter(admin__username=admin_username).order_by('-id').first()

    return render(request, 'addTask/addTask.html', {'task': task})


@login_required
def SaveData(request):
   
    if request.method == 'POST':
        title = request.POST.get('title')
        teacher = request.POST.get('teacher')
        choose = request.POST.get('choose')
        Description = request.POST.get('Description')
        admin = request.user  # Get the currently logged-in user

        # Create and save the Task object if it doesn't already exist
        if not Task.objects.filter(title=title, teacher=teacher, choose=choose, Description=Description, admin=admin).exists() :
            data = Task(title=title, teacher=teacher, choose=choose, Description=Description, admin=admin)
            data.save()

    return  redirect('showPage') 



