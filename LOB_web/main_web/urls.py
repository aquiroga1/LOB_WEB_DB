from django.contrib import admin
from django.urls import path

from loginapp.views import login_page, home_page, index


urlpatterns = [
    path('home', home_page, name='home'),
    path('login/', login_page),
    path('admin/', admin.site.urls, name='admin'),
    # path('index/', index, name='index'),

]
