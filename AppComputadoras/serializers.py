""" Librerias """
from rest_framework import serializers
from AppComputadoras.models import *
from django.core.files.uploadedfile import InMemoryUploadedFile
# Librerias para cargar imagenes por api
# ---------------------------------------------------------------
from drf_extra_fields.fields import Base64ImageField
# ---------------------------------------------------------------


# Definicion serializador para el modelo Mouse
class MouseSerializers(serializers.ModelSerializer):
    registro_fotografico_mouse = Base64ImageField(required = False)
    foto_requisicion_mouse = Base64ImageField(required = False)
    foto_acta_salida = Base64ImageField(required = False)
    foto_acta_recepcion = Base64ImageField(required = False)
    foto_factura = Base64ImageField(required = False)
    class Meta:
        model = Mouse
        fields = ('__all__')

# Definicion serializador para el modelo Teclado
class TecladoSerializers(serializers.ModelSerializer):
    registro_fotografico_teclado = Base64ImageField(required = False)
    foto_requisicion_teclado = Base64ImageField(required = False)
    foto_acta_salida_teclado = Base64ImageField(required = False)
    foto_acta_recepcion_teclado = Base64ImageField(required =False)
    foto_factura_teclado = Base64ImageField(required = False)
    class Meta:
        model = Teclado
        fields = ('__all__')

# Definicion serializador para el modelo Monitor
class MonitorSerializers(serializers.ModelSerializer):
    registro_fotografico_monitor = Base64ImageField(required = False)
    foto_requisicion_monitor = Base64ImageField(required = False)
    foto_acta_salida_monitor = Base64ImageField(required = False)
    foto_acta_recepcion_monitor = Base64ImageField(required = False)
    foto_factura_monitor = Base64ImageField(required = False)
    class Meta:
        model = Monitor
        fields = ('__all__')

# Definicion serializador para el modelo Torre
class TorreSerializers(serializers.ModelSerializer):
    registro_fotografico_torre = Base64ImageField(required = False)
    foto_requisicion_torre = Base64ImageField(required = False)
    foto_acta_salida_torre = Base64ImageField(required = False)
    foto_acta_recepcion_torre = Base64ImageField(required = False)
    foto_factura_torre = Base64ImageField(required = False)
    class Meta:
        model = Torre
        fields = ('__all__')

# Definicion serializador para el modelo Ciudad
class CiudadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('__all__')

# Definicion serializador para el modelo Sede
class SedeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = ('__all__')

# Definicion serializador para el modelo Area
class AreaSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Area
        fields = ('__all__')

# Definicion serializador para el modelo Workstation
class WorkstationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Workstation
        fields = ('__all__')

# Definicion serializador para el modelo Computador
class ComputadorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Computador
        fields = ('__all__')

# Definicion serializador para el modelo Impresoras
class ImpresorasSerializers(serializers.ModelSerializer):
    registro_fotografico_impresora = Base64ImageField(required = False)
    foto_requisicion_impresora = Base64ImageField(required = False)
    foto_acta_salida_impresora = Base64ImageField(required = False)
    foto_acta_recepcion_impresora = Base64ImageField(required = False)
    foto_factura_impresora = Base64ImageField(required = False)
    class Meta:
        model = Impresoras
        fields = ('__all__')

# Definicion serializador para el modelo Accesorio
class AccesoriosSerializers(serializers.ModelSerializer):
    registro_fotografico_accesorio = Base64ImageField(required = False)
    foto_requisicion_accesorio = Base64ImageField(required = False)
    foto_acta_salida_accesorio = Base64ImageField(required = False)
    foto_acta_recepcion_accesorio = Base64ImageField(required = False)
    foto_factura_accesorio = Base64ImageField(required = False)
    class Meta:
        model = Accesorios
        fields = ('__all__')

