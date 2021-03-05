from django.http import request
from django.shortcuts import render
from appcenter.models import App

# Create your views here.

def appcenter(request):
    
    apps = App.objects.all()
    return render(request, "appcenter/appcenter.html", {"apps": apps})

