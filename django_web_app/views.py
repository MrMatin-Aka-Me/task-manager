from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskFrom

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'django_web_app/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'django_web_app/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Incorrect form'
    form = TaskFrom()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'django_web_app/create.html', context)

# Create your views here.
