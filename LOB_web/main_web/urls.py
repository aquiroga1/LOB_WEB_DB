"""main_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from loginapp.views import login_page, home_page, logout_page
from subjectsapp.views import subjects_page, medical_records_page, index, index2
from projectsapp.views import projects_page, index_p
from measurementsapp.views import measurements_page, index_m
from appcenter.views import appcenter, recordcenter, datacenter



urlpatterns = [
    path('admin/', admin.site.urls),
    path('appcenter/', appcenter, name='appcenter'),
    path('home', home_page, name='home'),
    path('login/', login_page),
    path('logout/', logout_page, name='logout'),
    path('subjects/', subjects_page, name='subjects'),
    path('medical_records/', medical_records_page, name='medical_records'),
    path('projects/', projects_page, name='projects'),
    path('measurements/', measurements_page, name='measurements'),
    path('index/', index, name='index'),
    path('index2/', index2, name='index2'),
    path('index_m/', index_m, name='index_m'),
    path('index_p/', index_p, name='index_p'),
    path('recordcenter/', recordcenter, name='recordcenter'),
    path('datacenter/', datacenter, name='datacenter'),
]
