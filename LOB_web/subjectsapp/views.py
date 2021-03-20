from django.shortcuts import render
from .forms import *


def subjects_page(request):
    form = SubjectsForm()
    return render(request, "subjects_app/subjects.html", {'form': form})

