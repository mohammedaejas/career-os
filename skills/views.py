from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Skill


@login_required
def skill_list(request):
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'skills/skill_list.html', {'skills': skills})


@login_required
def add_skill(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        category = request.POST.get('category')
        proficiency = request.POST.get('proficiency')

        valid_categories = dict(Skill.CATEGORY_CHOICES)
        valid_levels = dict(Skill.LEVEL_CHOICES)

        if name and category in valid_categories and proficiency in valid_levels:
            Skill.objects.create(
                user=request.user,
                name=name,
                category=category,
                proficiency=proficiency
            )
            return redirect('skill_list')

    return render(request, 'skills/add_skill.html')


@login_required
def edit_skill(request, skill_id):
    skill = get_object_or_404(
        Skill,
        id=skill_id,
        user=request.user
    )

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        category = request.POST.get('category')
        proficiency = request.POST.get('proficiency')

        valid_categories = dict(Skill.CATEGORY_CHOICES)
        valid_levels = dict(Skill.LEVEL_CHOICES)

        if name and category in valid_categories and proficiency in valid_levels:
            skill.name = name
            skill.category = category
            skill.proficiency = proficiency
            skill.save()

            return redirect('skill_list')

    return render(request, 'skills/edit_skill.html', {'skill': skill})


@login_required
@require_POST
def delete_skill(request, skill_id):
    skill = get_object_or_404(
        Skill,
        id=skill_id,
        user=request.user
    )
    skill.delete()
    return redirect('skill_list')
