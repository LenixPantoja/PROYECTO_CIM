
""" Librerias """
from rest_framework import serializers
from AppMantenimientos.models import *

# Definir el serializador para el modelo Actividades
class ActividadesSerializers(serializers.Serializer):
    class Meta:
        model = Actividades
        fields = '__all__'

# Definir el serializador para el modelo Mantenimiento
class MantenimientoSerializers(serializers.Serializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'