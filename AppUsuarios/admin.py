from django.contrib import admin
from AppUsuarios import models as AppUser
# Register your models here.

@admin.register(AppUser.Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre_rol', 'fecha_creacion_rol', 'fecha_modificacion_rol')
    search_fields = ('nombre_rol',)

@admin.register(AppUser.Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('user', 'rol', 'tipo_documento', 'numero_identificacion', 'fecha_nacimiento', 'direccion_residencia', 'numero_celular', 'correo_electronico', 'fecha_creacion_persona', 'fecha_modificacion_persona')
    list_filter = ('user', 'rol', 'tipo_documento', 'numero_identificacion', 'fecha_nacimiento', 'direccion_residencia', 'numero_celular', 'correo_electronico', 'fecha_creacion_persona', 'fecha_modificacion_persona')
    search_fields = ('user', 'rol', 'tipo_documento', 'numero_identificacion', 'fecha_nacimiento', 'direccion_residencia', 'numero_celular', 'correo_electronico', 'fecha_creacion_persona', 'fecha_modificacion_persona')

