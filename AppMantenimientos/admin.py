from django.contrib import admin
from AppMantenimientos.models import Mantenimiento, Actividades
# Register your models here.

@admin.register(Actividades)
class ActividadesAdmin(admin.ModelAdmin):
    list_display = ('nombre_actividad', 'descripcion_actividad', 'tipo_actividad', 'fecha_creacion_actividad', 'fecha_modificacion_actividad')
    list_filter = ('tipo_actividad', 'fecha_creacion_actividad', 'fecha_modificacion_actividad')
    search_fields = ('nombre_actividad', 'tipo_actividad')


@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('tipo_mantenimiento', 'fecha_mantenimiento', 'display_actividades', 'cumple', 'no_cumple', 'no_aplica')
    list_filter = ('tipo_mantenimiento', 'fecha_mantenimiento', 'cumple', 'no_cumple', 'no_aplica')
    search_fields = ('tipo_mantenimiento', 'computador__nombre', 'tecnico_mantenimiento__nombre')

    def display_actividades(self, obj):
        return ', '.join([actividad.descripcion_actividad for actividad in obj.actividad.all()])

    display_actividades.short_description = 'Actividades'
