from django.urls import path
from . import views

urlpatterns = [
    path("", views.application_list, name="application_list"),
    path("edit/<int:application_id>/", views.application_edit, name="application_edit"),
    path("delete/<int:application_id>/", views.application_delete, name="application_delete"),
]
