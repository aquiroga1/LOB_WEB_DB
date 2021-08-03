from django.http import request
from django.shortcuts import render, redirect
from appcenter.models import App


def appcenter(request):
    if request.user.is_authenticated:
        apps = App.objects.all()
        return render(request, "appcenter/appcenter.html", {"apps": apps})
    else:
        return redirect("/login")

def recordcenter(request):
    if request.user.is_authenticated:
        apps = App.objects.all()
        return render(request, "recordcenter/recordcenter.html", {"apps": apps})
    else:
        return redirect("/login")

def datacenter(request):
    if request.user.is_authenticated:
        apps = App.objects.all()
        return render(request, "datacenter/datacenter.html", {"apps": apps})
    else:
        return redirect("/login")

