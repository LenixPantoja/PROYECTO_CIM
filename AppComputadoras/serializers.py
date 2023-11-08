from rest_framework import serializers
from AppComputadoras.models import *
from django.core.files.uploadedfile import InMemoryUploadedFile

class MouseSerializers(serializers.Serializer):
    class Meta:
        model = Mouse
        fields = '__all__'
"""
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        for key, value in data.items():
            if isinstance(value, InMemoryUploadedFile):
                data[key] = value.file.read()
        return data
"""

class TecladoSerializers(serializers.Serializer):
    class Meta:
        model = Teclado
        fields = '__all__'

class MonitorSerializers(serializers.Serializer):
    class Meta:
        model = Monitor
        fields = '__all__'

class TorreSerializers(serializers.Serializer):
    class Meta:
        model = Torre
        fields = '__all__'

class CiudadSerializers(serializers.Serializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

class SedeSerializers(serializers.Serializer):
    class Meta:
        model = Sede
        fields = '__all__'

class AreaSerializers(serializers.Serializer):
    class Meta: 
        model = Area
        fields = '__all__'

class WorkstationSerializers(serializers.Serializer):
    class Meta:
        model = Workstation
        fields = '__all__'

class ComputadorSerializers(serializers.Serializer):
    class Meta:
        model = Computador
        fields = '__all__'

class ImpresorasSerializers(serializers.Serializer):
    class Meta:
        model = Impresoras
        fields = '__all__'

class AccesoriosSerializers(serializers.Serializer):
    class Meta:
        model = Accesorios
        fields = '__all__'

