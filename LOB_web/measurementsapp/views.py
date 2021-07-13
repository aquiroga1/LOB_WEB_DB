from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.views.generic import FormView


def measurements_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_measurements = MeasurementsForm(request.POST, request.FILES)
            print(request.POST)
            print(form_measurements.is_valid())
            if form_measurements.is_valid():
                obj = Measurements()
                obj.subjects_id = form_measurements.cleaned_data['subjects_id']
                obj.local = form_measurements.cleaned_data['local']
                obj.date = form_measurements.cleaned_data['date']
                obj.project_id = form_measurements.cleaned_data['project_id']
                obj.file_name = form_measurements.cleaned_data['file_name']
                obj.incidents = form_measurements.cleaned_data['incidents']
                obj.observations = form_measurements.cleaned_data['observations']
                obj.FPIC_assignement = form_measurements.cleaned_data['FPIC_assignement']
                obj.auth_user_id = request.user
                # finally save the object in db
                obj.save()
                    #if se é paciente
                        #return HttpResponseRedirect('/medical_record')
                return HttpResponseRedirect('/subjects')
        else:
            form_measurements = MeasurementsForm
        return render(request, "measurementsapp/measurementsapp.html", {'form_measurements': form_measurements})
    else:
        return redirect("/login")

def index_m(request):
    context = {}
    measurement_data = Measurements.objects.all()
    context['measurement_data'] = measurement_data
    return render(request, "measurementsapp/measurement_datatable.html", context)