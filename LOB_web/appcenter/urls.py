from django.urls import path

from . import views
from subjectsapp.views import *
from measurementsapp.views import *
from projectsapp.views import *

urlpatterns = [
    path('',views.appcenter, name='appcenter'),
    path('recordcenter/', views.recordcenter, name='recordcenter'),
    path('datacenter/', views.datacenter, name='datacenter'),    
    path('recordcenter/projects/', projects_page, name='projects'),
    path('recordcenter/subjects/', subjects_page, name='subjects'),
    path('recordcenter/subjects/medical_records/', medical_records_page, name='medical_records'),
    path('recordcenter/measurements/', measurements_page, name='measurements'),
    path('datacenter/subjectsdt/', subject_datatable, name='subject_datatable'),
    path('datacenter/medicaldt/', medical_record_datatable, name='medical_record_datatable'),
    path('datacenter/measurementsdt/', measurement_datatable, name='measurement_datatable'),
    path('datacenter/projectsdt/', projects_datatable, name='projects_datatable'),
    path('subjects_update/<int:id>/', subjects_update, name='subjects_update'),
]

