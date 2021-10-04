from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class NIRS_Systems(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    num_of_sources = models.IntegerField(null=False)
    num_of_detectors = models.IntegerField(null=False)
    wavelenghts = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Aux_Systems(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Projects(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    CAAE = models.CharField(max_length=30, blank=True, null=True)
    FPIC_file = models.FileField(upload_to='main_web/media/Projects/', null=True, blank=True)
    prin_investigator = models.CharField(max_length=100, null=False)
    co_investigator = models.CharField(max_length=100, null=True, blank=True)
    probe_details = models.TextField(null=True, blank=True)
    protocol_details = models.CharField(max_length=150, null=True, blank=True)
    nirs_systems_id = models.ForeignKey(NIRS_Systems, on_delete=models.CASCADE)
    aux_systems_id = models.ForeignKey(Aux_Systems, null=True, blank=True, on_delete=models.CASCADE)
    project_file = models.FileField(upload_to='main_web/media/Projects/', null=True, blank=True)
    auth_user_id = models.ForeignKey(User, db_column="user", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)