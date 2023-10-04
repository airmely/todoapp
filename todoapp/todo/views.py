from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Tasks
from .forms import TaskForm, LoginForm, RegisterForm


@login_required(login_url='/login/')
def view_all_tasks(request):
    task = Tasks.objects.filter(user=request.user).order_by('-status')
    return render(
        request,
        'todo/main_page.html',
        {
            'task': task,
        }
    )


def create_new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    return render(request, 'todo/create_task.html', {'form': form})


def update_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)

    return render(request, 'todo/update_task.html', {'form': form})


def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return redirect('tasks')


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'todo/register.html',
                      {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            login(request, user)
            return redirect('tasks')
        else:
            return render(request, 'todo/register.html',
                          {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')


def login_user(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'todo/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Привет {username.title()}, Добро пожаловать!')
                return redirect('tasks')

        messages.error(request, f'Неправильное имя пользователя или пароль')
        return render(request, 'todo/login.html', {'form': form})
