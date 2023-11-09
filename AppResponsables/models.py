from django.db import models
# Create your models here.

class Responsable(models.Model):
    nombres_completos = models.CharField(max_length=255)
    numero_documento = models.CharField(max_length=50)
    firma_responsable = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = 'Responsable'
        verbose_name_plural = 'Responsables'

    def __str__(self):
          return str(self.nombres_completos)