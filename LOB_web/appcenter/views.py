from django.http import request
from django.shortcuts import render, redirect
from appcenter.models import App

# Create your views here.

def appcenter(request):
    if request.user.is_authenticated:
        apps = App.objects.all()
        return render(request, "appcenter/appcenter.html", {"apps": apps})
    else:
        return redirect("/login")


