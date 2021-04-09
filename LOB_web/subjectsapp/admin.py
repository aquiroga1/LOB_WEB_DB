from django.contrib import admin
from .models import *

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Subjects, SubjectAdmin)

class DiseaseAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Diseases, DiseaseAdmin)

class ComorbiditieAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Comorbidities, ComorbiditieAdmin)

class Medical_RecordAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Medical_Record, Medical_RecordAdmin)
