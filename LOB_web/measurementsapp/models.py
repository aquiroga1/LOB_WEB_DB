from projectsapp.models import Projects
from subjectsapp.models import Subjects
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Measurements(models.Model):
    incidents_choices = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]

    FPIC_assignement_choices = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]
    

    subjects_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    local = models.CharField(max_length=100, null=False)
    date = models.DateField(auto_now=False, null=False, blank=True)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    file_name = models.FileField(upload_to='main_web/media/Measurements/', blank =True, null=True)
    incidents = models.CharField(max_length=20, null=False, choices= incidents_choices)
    observations = models.TextField(null=True, blank=True)
    FPIC_assignement = models.CharField(max_length=20, null=True, blank=True, choices= FPIC_assignement_choices)
    auth_user_id = models.ForeignKey(User, db_column="user", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

