from django.contrib import admin
from .models import Projects

# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Projects, ProjectsAdmin)
