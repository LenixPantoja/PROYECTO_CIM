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

class AppResponsables_API_CrearResponsable(APIView):
    def post(self, request, format = None):
        try:
            serializer = ResponsableSerializers(data = request.data)
            if serializer.is_valid():
                dataResponsable = request.data
                files_path = 'firmas/'
                default_storage.save(files_path + f'{dataResponsable['nombres_completos']}.png', dataResponsable['firma_responsable'])
                responsable = Responsable(
                    nombres_completos = dataResponsable['nombres_completos'],
                    numero_documento = dataResponsable['numero_documento'],
                    firma_responsable = files_path + 'firma_responsable.png',
                )
                responsable.save()
            return Response({'mensaje': 'Se creo el Responsable :)'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)