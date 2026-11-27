from django.contrib import admin
from .models import JobListing


@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):

    list_display = (
        'job_title',
        'company_name',
        'location',
        'work_mode',
        'experience_level',
        'created_at',
    )

    list_filter = (
        'work_mode',
        'experience_level',
    )

    search_fields = (
        'job_title',
        'company_name',
        'location',
        'required_skills',
    )
