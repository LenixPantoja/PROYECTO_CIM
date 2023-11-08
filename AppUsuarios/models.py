from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=200)
    fecha_creacion_rol = models.DateTimeField(auto_now=True)
    fecha_modificacion_rol = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
          return str(self.nombre_rol)
    
class Persona(models.Model):
    user = models.OneToOneField(User, verbose_name="UsuarioCIM", on_delete=models.CASCADE)
    rol = models.OneToOneField(Rol, verbose_name="Rol", on_delete=models.CASCADE) 
    tipo_documento = models.CharField(max_length=200)
    numero_identificacion = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    direccion_residencia = models.CharField(max_length=250)
    numero_celular = models.CharField(max_length=30)
    correo_electronico = models.EmailField()
    fecha_creacion_persona = models.DateTimeField(auto_now=True)
    fecha_modificacion_persona = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'TecnicoDeMantenimiento'
        verbose_name_plural = 'TecnicosDeMantenimientos'

    def __str__(self):
          return str(self.user.first_name + " " + self.user.last_name)

