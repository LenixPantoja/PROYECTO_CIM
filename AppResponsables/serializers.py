from rest_framework import serializers
from AppResponsables.models import *

class ResponsableSerializers(serializers.Serializer):
    class Meta:
        model = Responsable
        fields = '__all__'

