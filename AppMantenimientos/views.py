""" Librerias  """
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from django.http import JsonResponse

""" Modelos """
from AppMantenimientos.serializers import *
from AppMantenimientos.models import *

# Definir la vista para la creación de actividad
class AppMantenimientos_API_CrearActividad(APIView):
    # Metodo POST
    def post(self, request, format = None):
        try:
            # Crear una instancia del serializador con los datos de la solicitud
            serializer = ActividadesSerializers(data = request.data)

            if serializer.is_valid():
                dataActividad = request.data
                # Crear una instancia del modelo Actividades con los datos proporcionados y guarda la instancia
                actividad = Actividades(
                    nombre_actividad = dataActividad['nombre_actividad'],
                    descripcion_actividad = dataActividad['descripcion_actividad'],
                    tipo_actividad = dataActividad['tipo_actividad']
                )
                actividad.save()
            return Response({'mensaje': 'Se creo la actividad :)'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Metodo GET    
    def get(self, request, format=None):
       try:
            lista_resposables = []
            actividades = Actividades.objects.all()
            serializer = ActividadesSerializers(actividades, many=True)
            return Response(serializer.data)    
       except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    # Metodo PUT
    def put(self, request, pk, format = None):
        try:
            actividad = Actividades.objects.get(pk = pk)
            serializer = ActividadesSerializers(actividad, data = request.data)
            serializer.save()
            return Response(serializer.data)
        except Actividades.DoesNotExist:
            return Response ("La actividad no existe", status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response ({'Error': str(e)}, status = status.HTTP_400_BAD_REQUEST) 
    
    # Metodo DELETE    
    def delete(self, request, pk, fomat = None):
        try:
            actividad = Actividades.objects.get(pk=pk)
            actividad.delete()
            return Response({"Msg": 'Registro eliminado correctamente'}, status = status.HTTP_200_OK)
        except Actividades.DoesNotExist:
            return Response({'error': 'No existe la actividad'}, status=status.HTTP_400_BAD_REQUEST)    
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# --------------------------------------------------------------------------------------------------------------------------- #

# Definir la vista para la creación de mantenimiento
class AppMantenimientos_API_CrearMantenimiento(APIView):
    # Metodo POST
    def post(self, request, format = None):
        try:
            # Crear una instancia del serializador con los datos de la solicitud
            serializer = MantenimientoSerializers(data = request.data)

            if serializer.is_valid():
                dataMantenimiento = request.data
                # Obtener instancias de modelos relacionados
                actividades = Actividades.objects.get(id = dataMantenimiento['actividad'])
                computador = Computador.objects.get(id = dataMantenimiento['computador'])
                tecnico_mantenimiento = Persona.objects.get(id = dataMantenimiento['tecnico_mantenimiento'])
                # Crear una objeto del modelo Mantenimiento con los datos proporcionados y guarda en la base de datos
                mantenimiento = Mantenimiento(
                    computador = computador,
                    tipo_mantenimiento = dataMantenimiento['tipo_mantenimiento'],
                    fecha_mantenimiento = dataMantenimiento['fecha_mantenimiento'],
                    observaciones = dataMantenimiento['observaciones'],
                    tecnico_mantenimiento = tecnico_mantenimiento,
                    #actividad = actividad,
                    cumple = dataMantenimiento['cumple'],
                    no_cumple = dataMantenimiento['no_cumple'],
                    no_aplica = dataMantenimiento['no_aplica'],
                )
                mantenimiento.save()
                mantenimiento.actividad.add(actividades)     
            return Response({'mensaje': 'Se creo el mantenimiento :)'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Metodo GET
    def get(self, request, format=None):
        try:
            # Obtener todas las actividades
            mantenimientos = Mantenimiento.objects.all()
            serializer = MantenimientoSerializers(mantenimientos, many=True)
            return Response(serializer.data)    
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Metodo PUT
    def put(self, request, pk, format=None):
        try:
            mantenimiento =Mantenimiento.objects.get(pk = pk)
            serializers = MantenimientoSerializers(mantenimiento, data = request.data)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data)
        except Mantenimiento.DoesNotExist:
            return Response("el mantenimiento no existe", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Metodo DELETE    
    def delete(self, request, pk, format=None):
        try:
            mantenimiento = Mantenimiento.objects.get(pk = pk)
            mantenimiento.delete()
            return Response({"Msg": 'Registro eliminado correctamente'}, status=status.HTTP_200_OK)
        except Mantenimiento.DoesNotExist:
            return Response({"Error": "El mantenimiento no existe"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)