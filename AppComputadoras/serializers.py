""" Librerias """
from rest_framework import serializers
from AppComputadoras.models import *
from django.core.files.uploadedfile import InMemoryUploadedFile

# Definicion serializador para el modelo Mouse
class MouseSerializers(serializers.Serializer):
    class Meta:
        model = Mouse
        fields = '__all__'

# Definicion serializador para el modelo Teclado
class TecladoSerializers(serializers.Serializer):
    class Meta:
        model = Teclado
        fields = '__all__'

# Definicion serializador para el modelo Monitor
class MonitorSerializers(serializers.Serializer):
    class Meta:
        model = Monitor
        fields = '__all__'

# Definicion serializador para el modelo Torre
class TorreSerializers(serializers.Serializer):
    class Meta:
        model = Torre
        fields = '__all__'

# Definicion serializador para el modelo Ciudad
class CiudadSerializers(serializers.Serializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

# Definicion serializador para el modelo Sede
class SedeSerializers(serializers.Serializer):
    class Meta:
        model = Sede
        fields = '__all__'

# Definicion serializador para el modelo Area
class AreaSerializers(serializers.Serializer):
    class Meta: 
        model = Area
        fields = '__all__'

# Definicion serializador para el modelo Workstation
class WorkstationSerializers(serializers.Serializer):
    class Meta:
        model = Workstation
        fields = '__all__'

# Definicion serializador para el modelo Computador
class ComputadorSerializers(serializers.Serializer):
    class Meta:
        model = Computador
        fields = '__all__'

# Definicion serializador para el modelo Impresoras
class ImpresorasSerializers(serializers.Serializer):
    class Meta:
        model = Impresoras
        fields = '__all__'

# Definicion serializador para el modelo Accesorio
class AccesoriosSerializers(serializers.Serializer):
    class Meta:
        model = Accesorios
        fields = '__all__'

