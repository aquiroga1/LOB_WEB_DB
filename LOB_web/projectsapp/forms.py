from django import forms
from .models import *
from django.forms.widgets import DateInput, TextInput

class NIRS_Systems_Form(forms.ModelForm):
    class Meta:
        model = NIRS_Systems
        fields = ["name", "description", "num_of_sources", "num_of_detectors", "wavelenghts"
                  ]

class Aux_Systems_Form(forms.ModelForm):
    class Meta:
        model = Aux_Systems
        fields = ["name", "description",
                  ]

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ["title", "description", "CAAE", "FPIC_file", "prin_investigator", "co_investigator", "probe_details", "protocol_details",
                 "nirs_systems_id", "aux_systems_id", "project_file",
                  ]

        widgets = {
            'nirs_systems_id': forms.Select(attrs={'style': 'width:285px'}),
            'aux_systems_id': forms.Select(attrs={'style': 'width:290px'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nirs_systems_id'].queryset = self.fields['nirs_systems_id'].queryset.order_by('-pk')
        self.fields['aux_systems_id'].queryset = self.fields['aux_systems_id'].queryset.order_by('-pk')


        
    
