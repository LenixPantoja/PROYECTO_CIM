""" Librerias """
from django.db import models
import os
from django.conf import settings

# Definir el modelo Responsable con sus respectivos campos
class Responsable(models.Model):
    nombres_completos = models.CharField(max_length=255)
    numero_documento = models.CharField(max_length=50)
    firma_responsable = models.ImageField(blank=True, null=True, upload_to='RegistroFotograficoResponsable/')

    class Meta:
        verbose_name = 'Responsable'
        verbose_name_plural = 'Responsables'

    def save(self, *args, **kwargs):
        if self.firma_responsable:
              self.save_image('firma_responsable', 'firma_responsable')
        
        super(Responsable, self).save( *args, **kwargs)

    def save_image(self, field_name, folder_name):
        archivo_imagen = getattr(self, field_name)
        if archivo_imagen:
            firma_carpeta_responsable = os.path.join(settings.MEDIA_ROOT, 'RegistroFotograficoResponsable', f'Responsable{self.firma_responsables}')
            os.makedirs(firma_carpeta_responsable, exist_ok=True)
            # Agrega al nombre de cada imagen un numero consecutivo.
            archivo_exixtente = [file for file in os.listdir(firma_carpeta_responsable) if file.startswith(self.firma_responsables)]
            suffix = len(archivo_exixtente) + 1
            # Guardar la imagen en la carpeta con el nombre del serialmouse y sufijo
            nombre_imagen = f'{self.firma_responsables}_{suffix}.png'
            ruta_imagen = os.path.join(firma_carpeta_responsable, nombre_imagen)
            # Guardar la imagen en la ruta especificada
            with open(ruta_imagen, 'wb') as f:
                for chunk in archivo_imagen.chunks():
                    f.write(chunk)
            # Actualizamos el campo de la imagen en el modelo
            setattr(self, field_name, os.path.relpath(ruta_imagen, settings.MEDIA_ROOT))
    
    # def save_image(self, field_name, folder_name):
    #     archivo_imagen = getattr(self, field_name)
    #     if archivo_imagen:
    #         firma_carpeta_responsable = os.path.join(settings.MEDIA_ROOT, 'RegistroFotograficoResponsable')
    #         os.makedirs(firma_carpeta_responsable, exist_ok=True)
    #         # Agrega al nombre de cada imagen un numero consecutivo.
    #         archivo_existente = [file for file in os.listdir(firma_carpeta_responsable) if file.startswith(field_name)]
    #         suffix = len(archivo_existente) + 1
    #         # Guardar la imagen en la carpeta con el nombre del serialmouse y sufijo
    #         nombre_imagen = f'{field_name}_{suffix}.png'
    #         ruta_imagen = os.path.join(firma_carpeta_responsable, nombre_imagen)
    #         # Guardar la imagen en la ruta especificada
    #         with open(ruta_imagen, 'wb') as f:
    #             for chunk in archivo_imagen.chunks():
    #                 f.write(chunk)
    #         # Actualizamos el campo de la imagen en el modelo
    #         setattr(self, field_name, os.path.relpath(ruta_imagen, settings.MEDIA_ROOT))

    def __str__(self):
          return str(self.nombres_completos)