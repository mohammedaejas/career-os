from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from tasks.models import Task
from tasks.forms import TaskForm
from .models import Profile
from .forms import ProfileForm


@login_required
def home(request):
    tasks = Task.objects.filter(owner=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect("home")
    else:
        form = TaskForm()

    return render(request, "home.html", {
        "tasks": tasks,
        "form": form,
    })


@login_required
def candidate_profile(request):
    user = request.user

    profile = Profile.objects.filter(user=user).first()

    if profile is None and user.email:
        profile = Profile.objects.filter(
            user__isnull=True,
            email__iexact=user.email,
        ).first()

        if profile:
            profile.user = user
            profile.save(update_fields=["user"])

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("candidate_profile")
    else:
        initial = {
            "name": user.get_full_name() or user.username,
            "email": user.email,
        }
        form = ProfileForm(instance=profile, initial=initial)

    return render(request, "accounts/profile.html", {
        "form": form,
        "profile": profile,
    })
