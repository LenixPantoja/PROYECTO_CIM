""" Librerias """
from rest_framework import serializers
from AppResponsables.models import *

# Definir el serializador ResponsableSerializers
class ResponsableSerializers(serializers.Serializer):
    class Meta:
        # Especificar el modelo asociado al serializador y los campos a incluir
        model = Responsable
        fields = '__all__'

