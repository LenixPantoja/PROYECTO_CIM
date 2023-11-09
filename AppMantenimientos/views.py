""" Librerias  """
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from django.http import JsonResponse
# Create your views here.
""" Modelos """
from AppMantenimientos.serializers import *
from AppMantenimientos.models import *

class AppMantenimientos_API_CrearActividad(APIView):
    def post(self, request, format = None):
        try:
            serializer = ActividadesSerializers(data = request.data)

            if serializer.is_valid():
                dataActividad = request.data
                actividad = Actividades(
                    nombre_actividad = dataActividad['nombre_actividad'],
                    descripcion_actividad = dataActividad['descripcion_actividad'],
                    tipo_actividad = dataActividad['tipo_actividad']
                )
                actividad.save()
            return Response({'mensaje': 'Se creo la actividad :)'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class AppMantenimientos_API_CrearMantenimiento(APIView):
    def post(self, request, format = None):
        try:
            serializer = MantenimientoSerializers(data = request.data)

            if serializer.is_valid():
                dataMantenimiento = request.data
                dataActividad = request.data
                actividad = Actividades(
                    nombre_actividad = dataActividad['nombre_actividad'],
                    descripcion_actividad = dataActividad['descripcion_actividad'],
                    tipo_actividad = dataActividad['tipo_actividad']
                )
                actividad.save()
                mantenimiento = Mantenimiento(
                    computador = dataMantenimiento['computador'],
                    tipo_mantenimiento = dataMantenimiento['tipo_mantenimiento'],
                    fecha_mantenimiento = dataMantenimiento['fecha_mantenimiento'],
                    observaciones = dataMantenimiento['observaciones'],
                    tecnico_mantenimiento = dataMantenimiento['tecnico_mantenimiento'],
                    actividad = actividad,
                    cumple = dataMantenimiento['cumple'],
                    no_cumple = dataMantenimiento['no_cumple'],
                    no_aplica = dataMantenimiento['no_aplica'],
                )
                mantenimiento.save()
            return Response({'mensaje': 'Se creo el mantenimiento :)'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



