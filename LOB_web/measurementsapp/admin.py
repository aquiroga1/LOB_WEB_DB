from django.contrib import admin
from measurementsapp.models import Measurements

# Register your models here.

class MeasurementsAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Measurements, MeasurementsAdmin)
