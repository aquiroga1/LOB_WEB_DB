from django.shortcuts import render, redirect
from .forms import *


def subjects_page(request):
    if request.user.is_authenticated:
        form = SubjectsForm()
        return render(request, "subjects_app/subjects.html", {'form': form})
    else:
        return redirect("/login")


