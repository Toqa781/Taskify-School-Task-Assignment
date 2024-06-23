def home_view(request):
    return render(request, 'home.html')


# views.py
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            try:
                profile = user.profile
                if profile.role == 'admin':
                    return redirect('admin_home')  # Update with your actual admin home view
                elif profile.role == 'teacher':
                    return redirect('teacher_home')  # Update with your actual teacher home view
            except Profile.DoesNotExist:
                messages.error(request, 'Profile not found for this user.')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def logoutUser(request):
    auth_logout(request)
    return redirect('home')


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import CreateUserForm
from .models import Profile


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            Profile.objects.create(user=user, role=role)
            messages.success(request, 'Account created for ' + user.username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def adminhome(request):
    return render(request, 'admin_home.html')


def teacherhome(request):
    return render(request, 'availableTasks.html')
