from rest_framework import serializers
from AppMantenimientos.models import *

class ActividadesSerializers(serializers.Serializer):
    class Meta:
        model = Actividades
        fields = '__all__'

class MantenimientoSerializers(serializers.Serializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'