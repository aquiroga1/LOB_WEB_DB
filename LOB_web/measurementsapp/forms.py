from django import forms
from .models import *
from django.forms.widgets import DateInput, TextInput

class MeasurementsForm(forms.ModelForm):
    class Meta:
        model = Measurements
        fields = ["subjects_id", "local", "date", "project_id", "file_name", "incidents", "observations",
                  "FPIC_assignement"
                  ]

        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'subjects_id': forms.Select(attrs={'style': 'width:324px'}),
            'project_id': forms.Select(attrs={'style': 'width:329px'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subjects_id'].queryset = self.fields['subjects_id'].queryset.order_by('-pk')
        self.fields['project_id'].queryset = self.fields['project_id'].queryset.order_by('-pk')

