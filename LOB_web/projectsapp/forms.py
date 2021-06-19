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
        fields = ["title", "description", "CAAE", "FPIC_file", "prin_investigator", "co_investigator", "probe_details",
                 "nirs_systems_id", "aux_systems_id"
                  ]