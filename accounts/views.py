from django.shortcuts import render, redirect

from tasks.models import Task
from tasks.forms import TaskForm


def home(request):

    tasks = Task.objects.all()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = TaskForm()

    return render(request, "home.html", {
        "tasks": tasks,
        "form": form
    })