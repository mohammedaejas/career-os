from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import JobApplication
from .forms import JobApplicationForm


@login_required
def application_list(request):
    applications = JobApplication.objects.filter(user=request.user)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()

            return redirect('application_list')
    else:
        form = JobApplicationForm()

    context = {
        'form': form,
        'applications': applications,
    }

    return render(request, 'jobs/application_list.html', context)


@login_required
def application_edit(request, application_id):
    application = get_object_or_404(
        JobApplication,
        id=application_id,
        user=request.user
    )

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=application)

        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = JobApplicationForm(instance=application)

    context = {
        'form': form,
        'application': application,
    }

    return render(request, 'jobs/application_edit.html', context)


@login_required
def application_delete(request, application_id):
    application = get_object_or_404(
        JobApplication,
        id=application_id,
        user=request.user
    )

    if request.method == 'POST':
        application.delete()

    return redirect('application_list')
