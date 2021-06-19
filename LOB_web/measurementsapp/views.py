from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import *



def measurements_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_measurements = MeasurementsForm(request.POST)
            print(form_measurements.is_valid)
            if form_measurements.is_valid():
                print(form_measurements)
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
                print(obj.local)
                obj.save()
                return HttpResponseRedirect('/')
        else:
            form_measurements = MeasurementsForm()
        
        return render(request, "measurements_app/measurements.html", {'form_measurements': form_measurements})
    else:
        return redirect("/login")

