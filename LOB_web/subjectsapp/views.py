from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import *]
from .models import *


def subjects_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_subjects = SubjectsForm(request.POST)
            if form_subjects.is_valid():
                obj = Subjects()
                obj.name = form_subjects.cleaned_data['name']
                obj.email = form_subjects.cleaned_data['email']
                obj.telephone = form_subjects.cleaned_data['telephone']
                obj.condition = form_subjects.cleaned_data['condition']
                obj.name = form_subjects.cleaned_data['gender']
                obj.email = form_subjects.cleaned_data['birth_date']
                obj.telephone = form_subjects.cleaned_data['height']
                obj.condition = form_subjects.cleaned_data['weight']
                obj.condition = form_subjects.cleaned_data['skin_color']
                obj.name = form_subjects.cleaned_data['handedness']
                obj.email = form_subjects.cleaned_data['scholar_level']
                obj.telephone = form_subjects.cleaned_data['additional_info']
                # finally save the object in db
                obj.save()

                return HttpResponseRedirect('/')
        else:
            form_subjects = SubjectsForm()
            form_diseases = DiseasesForm()
            form_comorbidities = ComorbiditiesForm()
            form_medical_records = Medical_RecordForm()
        return render(request, "subjects_app/subjects.html", {'form_subjects': form_subjects,
                          'form_diseases': form_diseases, 'form_comorbidities': form_comorbidities,
                                                                  'form_medical_records': form_medical_records})
    else:
        return redirect("/login")
