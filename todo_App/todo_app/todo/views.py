from django.shortcuts import render, redirect

# Create your views here.

# todo/views.py

from django.shortcuts import render, redirect
from .models import TodoItem

def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        TodoItem.objects.create(task=task)
        return redirect('index')

