from django.urls import path

from . import views


urlpatterns = [
    path('',views.appcenter, name="Central de Apps"),
    
]
