from rest_framework import serializers
from AppMantenimientos.models import *

class Actividades(serializers.Serializer):
    class Meta:
        model = Actividades
        fields = '__all__'

class Mantenimiento(serializers.Serializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'