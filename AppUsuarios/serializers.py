from rest_framework import serializers
from AppUsuarios.models import *

class RolSerializer(serializers.Serializer):
    class Meta:
        model = Rol
        fields = '__all__'

class PersonaSerializer(serializers.Serializer):
    class Meta:
        model = Persona
        fields = '__all__'

