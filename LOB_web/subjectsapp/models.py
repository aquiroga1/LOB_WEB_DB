from django.contrib.auth.models import User
from django.db import models


class Subjects(models.Model):
    gender_choices = [
        ("Female", "Female"),
        ("Male", "Male"),
    ]
    condition_choices = [
        ("P", "Patient"),
        ("H", "Healthy"),
    ]
    skin_color_choices = [
        ("B", "Black"),
        ("W", "White"),
        ("Y", "Yellow"),
        ("BR", "Brown"),
        ("N", "No info"),
    ]
    handedness_choices = [
        ("L", "Left"),
        ("R", "Right"),
        ("N", "No info")
    ]
    scholar_level_choices = [
        ("NI", "No info"),
        ("N", "No education"),
        ("PS", "Pre school"),
        ("ES", "Elementary school"),
        ("MS", "Middle school"),
        ("HS", "High school"),
        ("T", "Technical"),
        ("G", "Graduate"),
        ("PG", "Post-Graduate"),
    ]

    name = models.CharField(max_length=100, null=False)
    birth_date = models.DateField(auto_now=False, null=True, blank=True)
    gender = models.CharField(max_length=20, null=False, choices=gender_choices)
    condition = models.CharField(max_length=20, null=False, choices=condition_choices)
    height = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    skin_color = models.CharField(max_length=20, null=True, default='No info', choices=skin_color_choices)
    handedness = models.CharField(max_length=20, null=False, default='No info', choices=handedness_choices)
    scholar_level = models.CharField(max_length=20, null=False, default='No info', choices=scholar_level_choices)
    telephone = models.CharField(max_length=100, null=True,blank=True)
    email = models.EmailField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    auth_user_id = models.ForeignKey(User, db_column="user", on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'subjects'

    def __str__(self):
        return str(self.name)


class Diseases(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comorbidities(models.Model):
    name = models.CharField(max_length=100, null=False)
    abbreviation = models.CharField(max_length=50, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Medical_Record(models.Model):
    subjects_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    HC_number = models.CharField(max_length=20, null=False)
    diseases_id = models.ForeignKey(Diseases, on_delete=models.CASCADE, null=True, blank=True)
    comorbidities_ids = models.ManyToManyField(Comorbidities, null=True, blank=True)
    surgery = models.TextField(null=True, blank=True)
    clinical_outcomes = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.subjects_id)

