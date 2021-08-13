from django import forms
from .models import *
from django.forms.widgets import DateInput, TextInput


class SubjectsForm(forms.ModelForm):

   class Meta:
      model = Subjects
      fields = ["name", "email", "telephone", "condition", "gender", "birth_date", "height", "weight",
                "skin_color", "handedness", "scholar_level", "additional_info"
                ]

      widgets = {
                'birth_date': DateInput(attrs={'type': 'date'})
            }


class DiseasesForm(forms.ModelForm):
    class Meta:
        model = Diseases
        fields = ["name", "description",
                  ]


class ComorbiditiesForm(forms.ModelForm):
    class Meta:
        model = Comorbidities
        fields = ["name", "abbreviation"]


class Medical_RecordForm(forms.ModelForm):
    class Meta:
        model = Medical_Record

        widgets = {
            'diseases_id': forms.Select(attrs={'style': 'width:315px'}),
            'comorbidities_ids': forms.SelectMultiple(attrs={'style': 'width:275px;border-color:white; color white; height:100px'}),
            'subjects_id': forms.Select(attrs={'style': 'width:324px'})

        }


        fields = ["subjects_id", "HC_number", "diseases_id", "comorbidities_ids", "surgery",
                  "clinical_outcomes"]