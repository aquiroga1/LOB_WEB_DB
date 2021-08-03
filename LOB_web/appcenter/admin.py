from django.contrib import admin
from .models import App, Datatable, Record

# Register your models here.

class AppAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(App, AppAdmin)

class RecordAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Record, AppAdmin)

class DatatableAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Datatable, AppAdmin)