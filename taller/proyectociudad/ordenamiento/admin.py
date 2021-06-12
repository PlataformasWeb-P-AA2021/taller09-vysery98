from django.contrib import admin
from ordenamiento.models import Parroquia, Barrio
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ParroquiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre','tipo_parroquia')
    search_fields = ('nombre','tipo_parroquia')

admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'num_viviendas', 'num_parques', 'num_edificios')
    search_fields = ('parroquia__nombre', 'nombre')

admin.site.register(Barrio, BarrioAdmin)