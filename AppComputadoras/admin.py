from django.contrib import admin
from AppComputadoras import models as AppComp
# Register your models here.
@admin.register(AppComp.Mouse)
class MouseAdmin(admin.ModelAdmin):
    list_display =('marca_mouse', 'modelo_mouse', 'fecha_adquisicion_mouse',)
    list_filter = ('marca_mouse', 'fecha_adquisicion_mouse',)
    search_fields = ('marca_mouse', 'modelo_mouse',)

@admin.register(AppComp.Teclado)
class TecladoAdmin(admin.ModelAdmin):
    list_display = ('marca_teclado', 'modelo_teclado', 'fecha_adquisicion_teclado',)
    list_filter = ('marca_teclado', 'fecha_adquisicion_teclado',)
    search_fields = ('marca_teclado', 'modelo_teclado',)

@admin.register(AppComp.Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ('codigo_interno_monitor', 'marca_monitor', 'modelo_monitor', 'fecha_adquisicion_monitor',)
    list_filter = ('marca_monitor', 'fecha_adquisicion_monitor',)
    search_fields = ('codigo_interno_monitor', 'marca_monitor', 'modelo_monitor',)

@admin.register(AppComp.Torre)
class TorreAdmin(admin.ModelAdmin):
    list_display = ('codigo_interno_torre', 'nombre_equipo', 'marca_torre', 'modelo_torre', 'fecha_adquisicion_torre',)
    list_filter = ('marca_torre', 'fecha_adquisicion_torre',)
    search_fields = ('codigo_interno_torre', 'nombre_equipo', 'marca_torre', 'modelo_torre',)

@admin.register(AppComp.Impresoras)
class ImpresorasAdmin(admin.ModelAdmin):
    list_display = ('codigo_interno_impresora', 'nombre_impresora', 'modelo_impresora', 'fecha_adquisicion_impresora',)
    list_filter = ('nombre_impresora', 'fecha_adquisicion_impresora',)
    search_fields = ('codigo_interno_impresora', 'nombre_impresora', 'modelo_impresora',)

@admin.register(AppComp.Accesorios)
class AccesoriosAdmin(admin.ModelAdmin):
    list_display = ('codigo_interno_accesorio', 'nombre_accesorio', 'modelo_accessorio', 'marca_accesorio', 'fecha_adquisicion_accesorio',)
    list_filter = ('marca_accesorio', 'fecha_adquisicion_accesorio',)
    search_fields = ('codigo_interno_accesorio', 'nombre_accesorio', 'modelo_accessorio',)

@admin.register(AppComp.Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre_ciudad',)
    search_fields = ('nombre_ciudad',)

@admin.register(AppComp.Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('nombre_sede', 'display_ciudades')

    def display_ciudades(self, obj):
        return ', '.join([ciudad.nombre_ciudad for ciudad in obj.ciudad.all()])

    display_ciudades.short_description = 'Ciudades'

@admin.register(AppComp.Workstation)
class WorkstationAdmin(admin.ModelAdmin):
    list_display = ('puesto_trabajo', 'fecha_creacion_workstation', 'fecha_modificacion_workstation')
    list_filter = ('fecha_creacion_workstation', 'fecha_modificacion_workstation')
    search_fields = ('puesto_trabajo', 'fecha_creacion_workstation')
    date_hierarchy = 'fecha_creacion_workstation'

    def get_area(self, obj):
        return obj.area.nombre_area if obj.area else "No asignada"
    get_area.short_description = 'Area'

@admin.register(AppComp.Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre_area', 'fecha_creacion_area', 'fecha_modificacion_area', 'get_sedes')
    list_filter = ('fecha_creacion_area', 'fecha_modificacion_area')
    search_fields = ('nombre_area',)


    def get_sedes(self, obj):
        return ", ".join([sede.nombre_sede for sede in obj.sedes.all()])
    get_sedes.short_description = 'Sedes'

@admin.register(AppComp.Computador)
class ComputadorAdmin(admin.ModelAdmin):
    list_display = ('workstation', 'area', 'workstation', 'display_responsables')

    def display_responsables(self, obj):
        return ', '.join([responsable.nombres_completos for responsable in obj.responsable.all()])

    display_responsables.short_description = 'Responsables'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form
