from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'education', 'target_role')
    search_fields = ('name', 'email', 'target_role')
