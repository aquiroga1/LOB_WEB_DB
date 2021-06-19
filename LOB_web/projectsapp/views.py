from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import *



def projects_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_projects = ProjectsForm(request.POST)
            print(form_projects.is_valid)
            if form_projects.is_valid():
                obj = Projects()
                obj.title = form_projects.cleaned_data['title']
                obj.description = form_projects.cleaned_data['description']
                obj.CAAE = form_projects.cleaned_data['CAAE']
                obj.FPIC_file = form_projects.cleaned_data['FPIC_file']
                obj.prin_investigator = form_projects.cleaned_data['prin_investigator']
                obj.co_investigator = formprojects.cleaned_data['co_investigator']
                obj.optical_probe_details = form_projects.cleaned_data['optical_probe_details']
                obj.nirs_systems_id = form_projects.cleaned_data['nirs_systems_id']
                obj.aux_systems_id = form_projects.cleaned_data['aux_systems_id']
                obj.auth_user_id = request.user
                # finally save the object in db
                print(obj.title)
                obj.save()

                return HttpResponseRedirect('/')
        else:
            form_projects = ProjectsForm()
            form_NIRS_systems = NIRS_SystemsForm()
            form_Aux_systems = Aux_Systems()
        return render(request, "projects_app/projects.html", {'form_projects': form_projects,})
    else:
        return redirect("/login")
