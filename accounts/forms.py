from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "email",
            "education",
            "skills",
            "career_interests",
            "experience",
            "target_role",
        ]
        widgets = {
            "skills": forms.Textarea(attrs={"rows": 3}),
            "career_interests": forms.Textarea(attrs={"rows": 3}),
            "experience": forms.Textarea(attrs={"rows": 3}),
        }
