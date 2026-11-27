from django.shortcuts import render, get_object_or_404
from .models import JobListing


def job_list(request):
    jobs = JobListing.objects.all()

    query = request.GET.get('q', '')
    location = request.GET.get('location', '')
    work_mode = request.GET.get('work_mode', '')

    if query:
        jobs = jobs.filter(job_title__icontains=query) | jobs.filter(company_name__icontains=query)

    if location:
        jobs = jobs.filter(location__icontains=location)

    if work_mode:
        jobs = jobs.filter(work_mode=work_mode)

    context = {
        'jobs': jobs,
        'query': query,
        'location': location,
        'work_mode': work_mode,
    }

    return render(request, 'job_discovery/job_list.html', context)


def job_detail(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)

    return render(
        request,
        'job_discovery/job_detail.html',
        {'job': job}
    )
