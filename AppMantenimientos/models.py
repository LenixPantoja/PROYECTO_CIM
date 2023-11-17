""" Librerias """
from django.db import models
from AppComputadoras.models import Computador
from AppUsuarios.models import Persona


# Definir el modelo "Actividades" para las actividades de mantenimiento
class Actividades(models.Model):
    nombre_actividad = models.TextField()
    descripcion_actividad = models.TextField()
    tipo_actividad = models.CharField(max_length=100)
    fecha_creacion_actividad = models.DateTimeField(auto_now=True)
    fecha_modificacion_actividad = models.DateTimeField(auto_now=True)

# Definir el modelo "Mantenimiento" para el registro de mantenimientos
class Mantenimiento(models.Model):
    computador = models.ForeignKey(Computador, on_delete=models.CASCADE)
    tipo_mantenimiento = models.CharField(max_length=100)
    fecha_mantenimiento = models.DateField()
    observaciones = models.TextField()
    tecnico_mantenimiento = models.ForeignKey(Persona, verbose_name="TecnicoDeMantenimientos", on_delete=models.CASCADE)
    fecha_creacion_mantenimiento = models.DateTimeField(auto_now=True)
    fecha_modificacion_mantenimiento = models.DateTimeField(auto_now=True)
    actividad = models.ManyToManyField(Actividades, verbose_name="Actividades")
    cumple = models.BooleanField()
    no_cumple = models.BooleanField()
    no_aplica = models.BooleanField()

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'


    def __str__(self):
        # Representación en cadena para el objeto Mantenimiento
        return str("CODIGO_INTERNO_TORRE: " + self.computador.torre.codigo_interno_torre + " | " + self.computador.responsable.nombres_completos)


