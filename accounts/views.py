from django.shortcuts import render
from tasks.models import Task


def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})