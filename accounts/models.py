from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="profile",
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    education = models.CharField(max_length=200, blank=True)
    skills = models.TextField(blank=True)
    career_interests = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    target_role = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
