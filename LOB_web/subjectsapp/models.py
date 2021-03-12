from django.db import models


class Subjects(models.Model):
    gender_choices = [
        ["F", "Female"],
        ["M", "Male"],
        ["N", "None of these options"]
    ]
    condition_choices = [
        ["P", "Patient"],
        ["N", "Not Patient"],
    ]
    skin_color_choices = [
        ["B", "Black"],
        ["W", "White"],
        ["N", "None of these options"]
    ]
    handedness_choices = [
        ["L", "Left"],
        ["R", "Right"],
    ]
    scholar_level_choices = [
        ["L", "Left"],
        ["R", "Right"],
    ]

    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    telephone = models.CharField(max_length=12)
    condition = models.CharField(max_length=1, choices=condition_choices)
    gender = models.CharField(max_length=1, choices=gender_choices)
    birth_date = models.DateField(auto_now=False, null=True, blank=True)
    height = models.DecimalField(max_digits=2, decimal_places=1)
    skin_color = models.CharField(max_length=1, choices=skin_color_choices)
    handedness = models.CharField(max_length=1, choices=handedness_choices)
    scholar_level = models.CharField(max_length=1, choices=scholar_level_choices)
    additional_info = models.CharField(max_length=100)



