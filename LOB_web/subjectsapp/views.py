from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import *


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
                obj.gender = form_subjects.cleaned_data['gender']
                obj.birth_date = form_subjects.cleaned_data['birth_date']
                obj.height = form_subjects.cleaned_data['height']
                obj.weight = form_subjects.cleaned_data['weight']
                obj.skin_color = form_subjects.cleaned_data['skin_color']
                obj.handedness = form_subjects.cleaned_data['handedness']
                obj.scholar_level = form_subjects.cleaned_data['scholar_level']
                obj.additional_info = form_subjects.cleaned_data['additional_info']
                # finally save the object in db
                obj.save()
                return HttpResponseRedirect('/subjects')

            form_diseases = DiseasesForm(request.POST)
            if form_diseases.is_valid():
                obj = Diseases()
                obj.name = form_diseases.cleaned_data['name']
                obj.description = form_diseases.cleaned_data['description']
                # finally save the object in db
                obj.save()
                return HttpResponseRedirect('/subjects')

            form_comorbidities = ComorbiditiesForm(request.POST)
            if form_comorbidities.is_valid():
                obj = Comorbidities()
                obj.name = form_comorbidities.cleaned_data['name']
                obj.abbreviation = form_comorbidities.cleaned_data['abbreviation']
                # finally save the object in db
                obj.save()
                return HttpResponseRedirect('/subjects')

            form_medical_records = Medical_RecordForm(request.POST)
            if form_medical_records.is_valid():
                obj = Medical_Record()
                obj.subjects_id = form_medical_records.cleaned_data['subjects_id']
                obj.HC_number = form_medical_records.cleaned_data['HC_number']
                obj.diseases_id = form_medical_records.cleaned_data['diseases_id']
                obj.comorbidities_ids = form_medical_records.cleaned_data['comorbidities_ids']
                obj.surgery = form_medical_records.cleaned_data['surgery']
                obj.clinical_outcomes = form_medical_records.cleaned_data['clinical_outcomes']
                # finally save the object in db
                obj.save()
                return HttpResponseRedirect('/subjects')

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
