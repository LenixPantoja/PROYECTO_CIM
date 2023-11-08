from rest_framework import serializers
from AppResponsables.models import *

class Responsable(serializers.Serializer):
    class Meta:
        model = Responsable
        fields = '__all__'

