from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, render, redirect

from .models import Task
from .forms import TaskForm


@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    return render(request, "tasks/task_list.html", {
        "tasks": tasks,
        "form": form,
    })


@login_required
@require_POST
def toggle_task(request, task_id):
    task = get_object_or_404(
        Task, id=task_id, owner=request.user
    )
    task.completed = not task.completed
    task.save(update_fields=["completed"])
    return redirect("task_list")


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(
        Task, id=task_id, owner=request.user
    )

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/edit_task.html", {
        "form": form,
        "task": task,
    })
