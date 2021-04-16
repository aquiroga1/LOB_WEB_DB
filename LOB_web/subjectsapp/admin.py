from django.contrib import admin
from .models import Subjects

# Register your models here.

class SubjectsAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Subjects, SubjectsAdmin)