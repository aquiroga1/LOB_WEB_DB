from django.urls import path

from appcenter import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.center, name="Central de Aplicativos"),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)