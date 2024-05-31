""" Librerias  """
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from django.http import JsonResponse
""" Modelos """
from AppResponsables.serializers import *
from AppResponsables.models import *
""" Otras Librerias """
from django.core.files.storage import default_storage
from pathlib import *

# Definir la clase de la vista basada en API para crear un Responsable
class AppResponsables_API_CrearResponsable(APIView):
    # Metodo POST
    def post(self, request, format = None):
        try:
            # Serializar los datos recibidos en la solicitud
            serializer = ResponsableSerializers(data = request.data)
            if serializer.is_valid():
                dataResponsable = request.data
                
                responsable = Responsable(
                    nombres_completos = dataResponsable['nombres_completos'],
                    numero_documento = dataResponsable['numero_documento'],
                    firma_responsable = dataResponsable['firma_responsable']
                )
                responsable.save()
            return Response({'mensaje': 'Se creo el Responsable :)'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Metodo GET
    """def get(self, request, format=None):
        try:
            responsables = Responsable.objects.all()
            serializer = ResponsableSerializers(responsables, many = True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)"""
    def get(self, request, format=None):
        try:
            lista_responsables = []
            responsables = Responsable.objects.all()
            for miResponsable in responsables:
                firma = miResponsable.firma_responsable
                firma_url = None
                if firma:
                    firma_url = firma.url
                lista_responsables.append({
                    "id": miResponsable.id,
                    "nombres_completos": miResponsable.nombres_completos,
                    "numero_documento": miResponsable.numero_documento,
                    "firma_responsable": firma_url
                })
            return Response(lista_responsables)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Metodo PUT
    def put(self, request, pk, format=None):
        try:
            responsable = Responsable.objects.get(pk = pk)
            serializers = ResponsableSerializers(responsable, data=request.data)
            serializers.is_valid(raise_exception = True)
            serializers.save()
            return Response(serializers.data)
        except Responsable.DoesNotExist:
            return Response({'error': 'El Responsable no existe'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Metodo DELETE
    def delete(self, request, pk, format=None):
        try:
            responsable = Responsable.objects.get(pk = pk)
            responsable.delete()
            return Response({"Msg": 'Registro eliminado correctamente'}, status = status.HTTP_200_OK)
        except Responsable.DoesNotExist:
            return Response({'error': 'El Responsable no existe'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)