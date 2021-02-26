from django.contrib import admin
from .models import App

# Register your models here.

class AppAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(App, AppAdmin)