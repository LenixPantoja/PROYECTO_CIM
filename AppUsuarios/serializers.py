""" Librerias """
from rest_framework import serializers
from AppUsuarios.models import *

# Definición del serializador para el modelo Rol
class RolSerializer(serializers.Serializer):
    class Meta:
        model = Rol
        fields = '__all__'

# Definición del serializador para el modelo Persona
class PersonaSerializer(serializers.Serializer):
    class Meta:
        model = Persona
        fields = '__all__'