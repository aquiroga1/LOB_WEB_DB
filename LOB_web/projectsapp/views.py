from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.views.generic import FormView


def projects_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_projects = ProjectsForm(request.POST)
            if form_projects.is_valid():
                obj = Projects()
                obj.title = form_projects.cleaned_data['title']
                obj.description = form_projects.cleaned_data['description']
                obj.CAAE = form_projects.cleaned_data['CAAE']
                obj.FPIC_file = form_projects.cleaned_data['FPIC_file']
                obj.prin_investigator = form_projects.cleaned_data['prin_investigator']
                obj.co_investigator = form_projects.cleaned_data['co_investigator']
                obj.probe_details = form_projects.cleaned_data['probe_details']
                obj.nirs_systems_id = form_projects.cleaned_data['nirs_systems_id']
                obj.aux_systems_id = form_projects.cleaned_data['aux_systems_id']
                obj.auth_user_id = request.user
                # finally save the object in db
                obj.save()
                    #if se é paciente
                        #return HttpResponseRedirect('/medical_record')
                return HttpResponseRedirect('/subjects')
        else:
            form_projects = ProjectsForm
        return render(request, "projectsapp/projectsapp.html", {'form_projects': form_projects})
    else:
        return redirect("/login")
