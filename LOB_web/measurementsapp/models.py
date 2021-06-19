from projectsapp.models import Projects
from subjectsapp.models import Subjects
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Measurements(models.Model):
    incidents_choices = [
        ("Y", "Yes"),
        ("N", "No"),
    ]

    FPIC_assignement_choices = [
        ("Y", "Yes"),
        ("N", "No"),
    ]
    

    subjects_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    local = models.CharField(max_length=100, null=False)
    date = models.DateField(auto_now=False, null=False, blank=True)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100, null=False)
    incidents = models.CharField(max_length=20, null=False, choices= incidents_choices)
    observations = models.TextField(null=False)
    FPIC_assignement = models.CharField(max_length=20, null=True, choices= FPIC_assignement_choices)
    auth_user_id = models.ForeignKey(User, db_column="user", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='measurement'

def __str__(self):
    return str(self.subjects_id)
