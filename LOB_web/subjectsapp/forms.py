from django import forms
from .models import *
from django.forms.widgets import DateInput, TextInput


class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ["name", "email", "telephone", "condition", "gender", "birth_date", "height", "weight",
                  "skin_color", "handedness", "scholar_level", "additional_info",
                  ]
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'})
        }
        #
        # widgets = {
        #     'name': TextInput(attrs={'placeholder': 'Name'})
        # }


        # name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
        # email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))

