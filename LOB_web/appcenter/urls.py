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
    path('datacenter/subjectsdt/subjects_update/<int:id>/', subjects_update, name='subjects_update'),
    path('datacenter/subjectsdt/subjects_delete/<int:id>/', subjects_delete, name='subjects_delete'),
    path('datacenter/projectsdt/projects_update/<int:id>/', projects_update, name='projects_update'),
    path('datacenter/projectsdt/projects_delete/<int:id>/', projects_delete, name='projects_delete'),
    path('datacenter/measurementsdt/measurements_update/<int:id>/', measurements_update, name='measurements_update'),
    path('datacenter/measurementsdt/measurements_delete/<int:id>/', measurements_delete, name='measurements_delete'),
]

