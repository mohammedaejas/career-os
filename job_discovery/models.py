from django.db import models


class JobListing(models.Model):

    WORK_MODE_CHOICES = [
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
        ('On-site', 'On-site'),
    ]

    EXPERIENCE_CHOICES = [
        ('Fresher', 'Fresher'),
        ('Entry-level', 'Entry-level'),
        ('Experienced', 'Experienced'),
    ]

    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)

    work_mode = models.CharField(
        max_length=20,
        choices=WORK_MODE_CHOICES
    )

    required_skills = models.TextField(blank=True)

    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES
    )

    application_url = models.URLField()

    posted_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
