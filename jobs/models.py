from django.db import models
from django.contrib.auth.models import User


class JobApplication(models.Model):

    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    job_role = models.CharField(max_length=200)
    job_location = models.CharField(max_length=200, blank=True)
    application_date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Applied'
    )

    job_description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.job_role} at {self.company_name}"
