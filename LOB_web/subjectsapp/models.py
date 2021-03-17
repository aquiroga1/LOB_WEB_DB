from django.db import models


class Subjects(models.Model):
    gender_choices = [
        ("F", "Female"),
        ("M", "Male"),
    ]
    condition_choices = [
        ("P", "Patient"),
        ("H", "Healthy"),
    ]
    skin_color_choices = [
        ("N", "No info"),
        ("B", "Black"),
        ("W", "White"),
        ("Y", "Yellow"),
        ("BR", "Brown"),
    ]
    handedness_choices = [
        ("N", "No info"),
        ("L", "Left"),
        ("R", "Right"),
    ]
    scholar_level_choices = [
        ("N", "No education"),
        ("PS", "Pre school"),
        ("E", "Elementary"),
        ("HS", "Higher school"),
        ("T", "Technical"),
    ]

    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=True)
    telephone = models.CharField(max_length=100, null=True)
    condition = models.CharField(max_length=20, null=False, choices=condition_choices)
    gender = models.CharField(max_length=20, null=False, choices=gender_choices)
    birth_date = models.DateField(auto_now=False, null=False, blank=True)
    height = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    skin_color = models.CharField(max_length=20, null=True, default='No info', choices=skin_color_choices)
    handedness = models.CharField(max_length=20, null=False, default='No info', choices=handedness_choices)
    scholar_level = models.CharField(max_length=20, null=False, default='No info', choices=scholar_level_choices)
    additional_info = models.TextField(max_length=200, null=True)



