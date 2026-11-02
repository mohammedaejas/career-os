from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            'company_name',
            'job_role',
            'job_location',
            'status',
            'job_description',
        ]

        widgets = {
            'job_description': forms.Textarea(attrs={'rows': 4}),
        }
