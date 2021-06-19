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
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    CAAE = models.CharField(max_length=30, null=False)
    FPIC_file = models.FileField(upload_to='main_web/documents/FPIC/', null=False)
    prin_investigator = models.CharField(max_length=100, null=True)
    co_investigator = models.CharField(max_length=100, null=False)
    optical_probe_details = models.TextField(null=False)
    nirs_systems_id = models.ForeignKey(NIRS_Systems, on_delete=models.CASCADE)
    aux_systems_id = models.ForeignKey(Aux_Systems, on_delete=models.CASCADE)
    auth_user_id = models.ForeignKey(User, db_column="user", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='project'

