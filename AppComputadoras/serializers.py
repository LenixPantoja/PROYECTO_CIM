from rest_framework import serializers
from AppComputadoras.models import *

class MouseSerializers(serializers.Serializer):
    class Meta:
        model = Mouse
        fields = '__all__'

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

class Accesorios(serializers.Serializer):
    class Meta:
        model = Accesorios
        fields = '__all__'