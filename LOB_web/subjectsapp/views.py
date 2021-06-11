from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
from .models import Subjects


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
                obj.auth_user_id = request.user
                # finally save the object in db
                obj.save()
                return HttpResponseRedirect('/subjects')
        else:
            form_subjects = SubjectsForm()
        return render(request, "subjects_app/subjects.html", {'form_subjects': form_subjects})
    else:
        return redirect("/login")


def diseases_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_diseases = DiseasesForm(request.POST)
            if form_diseases.is_valid():
                obj = Diseases()
                obj.name = form_diseases.cleaned_data['name']
                obj.description = form_diseases.cleaned_data['description']
                # finally save the object in db
                obj.save()
                return HttpResponseRedirect('/subjects')
        else:
            form_diseases = DiseasesForm()
        return render(request, "subjects_app/subjects.html", {'form_diseases': form_diseases})
    else:
        return redirect("/login")


def comorbidities_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_comorbidities = ComorbiditiesForm(request.POST)
            if form_comorbidities.is_valid():
                obj = Comorbidities()
                obj.name = form_comorbidities.cleaned_data['name']
                obj.abbreviation = form_comorbidities.cleaned_data['abbreviation']
                # finally save the object in db
                obj.save()
                return HttpResponseRedirect('/subjects')
        else:
            form_comorbidities = ComorbiditiesForm()
        return render(request, "subjects_app/subjects.html", {'form_comorbidities': form_comorbidities})
    else:
        return redirect("/login")


def medical_records_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
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
            form_medical_records = Medical_RecordForm()
        return render(request, "subjects_app/medical_record.html", {'form_medical_records': form_medical_records})
    else:
        return redirect("/login")

class Medical_Records_Page(FormView):
    template_name= "subjects_app/medical_record.html"
    form_class = SubjectsForm
    success_url = '/thanks/'

    def form_valid(self, form):
        org = form.cleaned_data.get('organization')
        emails = form.cleaned_data.get("share_email_with")

        users = User.objects.filter(email__in=emails)
        instance = Setupuser.objects.create(organization=org)

        for user in users:
            instance.emails_for_help.add(user)

        return redirect("/")

def index(request):
    queryset1 = Subjects.objects.all()
    context = {
        'data': queryset1
    }
    return render(request, "index.html", context)

