from django.contrib import admin
from django.urls import path

from loginapp.views import login_page, home_page

urlpatterns = [
    path('home', home_page),
    path('login/', login_page),
    path('admin/', admin.site.urls),
]
