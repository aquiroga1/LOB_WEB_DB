from django import forms
from .models import *


class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ["name", "email", "telephone", "condition", "gender", "birth_date", "height",
                  "skin_color","handedness", "scholar_level", "additional_info",
                  ]
