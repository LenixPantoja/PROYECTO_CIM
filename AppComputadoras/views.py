""" Librerias  """
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from django.http import JsonResponse
from base64 import *
""" Modelos """
from AppComputadoras.serializers import *
from AppComputadoras.models import *
# Create your views here.

class AppComputers_API_CrearMouse(APIView):
    def post(self, request, format = None):

        try:

            serializer = MouseSerializers(data = request.data)

            if serializer.is_valid():
                dataMouse = request.data
                mouse = Mouse(
                marca_mouse = dataMouse['marca_mouse'],
                modelo_mouse = dataMouse['modelo_mouse'],
                serial_mouse = dataMouse['serial_mouse'],
                fecha_adquisicion_mouse =  dataMouse['fecha_adquisicion_mouse'],
                fecha_instalacion_mouse = dataMouse['fecha_instalacion_mouse'],
                fecha_garantia_mouse = dataMouse['fecha_garantia_mouse'],
                registro_fotografico_mouse  = b64encode(dataMouse['registro_fotografico_mouse']),
                foto_requisicion_mouse = b64encode(dataMouse['foto_requisicion_mouse']),
                foto_acta_salida = b64encode(dataMouse['foto_acta_salida']),
                foto_acta_recepcion = b64encode(dataMouse['foto_acta_recepcion']),
                foto_factura = b64encode(dataMouse['foto_factura'])
                )
                mouse.save()
                return Response({'mensaje': 'Se creo el mouse :)'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
