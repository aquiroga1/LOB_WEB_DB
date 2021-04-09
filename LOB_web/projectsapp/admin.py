from django.contrib import admin
from .models import *

# Register your models here.

class NIRS_SystemAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(NIRS_Systems, NIRS_SystemAdmin)

class Aux_SystemAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Aux_Systems, Aux_SystemAdmin)

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Projects, ProjectAdmin)

