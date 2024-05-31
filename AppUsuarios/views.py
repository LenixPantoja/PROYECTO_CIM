""" Librerias """
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.hashers import make_password  
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics 
from rest_framework import viewsets
#from models import *

# Serializadores de AppUsuarios
from AppUsuarios.serializers import *

# Views de AppUsuarios
from AppUsuarios.models import *

# Librerias JWT
from django.http import JsonResponse   
from rest_framework import permissions, status 
from rest_framework.decorators import api_view, permission_classes

# Api para la clase AppUser_login
class AppUser_loginApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):

        if request.user.is_authenticated:
            # Obtencion del usuario autenticado
            user = request.user 
            # Serialización del usuario para la obtencion de sus datos completos
            serializers = UsuarioSerializer(user)
            # Retorna los datos del usuario
            return Response(serializers.data)
        
        else:
            return Response({"detail": "El usuario no está autenticado"}, status = 401)

# Api para la clase AppUser_Persona
class AppUser_Persona_ApiView(APIView):
    #Spermission_classes = (permissions.IsAuthenticated,)

    # Metodo POST
    def post(self, request, format =  None):
        # Serializacion de los datos del usuario
        user_data = request.data["persona"]
        user_serializer =  PersonaSerializer(data = user_data)

        if user_serializer.is_valid():
            user = user_serializer.save()
            # Asignación del usuario al Rol
            rol_data = {
                "user": user.id,
                "rol": request.data["rol"],
                "tipo_documento": request.data["tipo_documento"], 
                "numero_identificacion": request.data["numero_identificacion"],
                "fecha_nacimiento": request.data["fecha_nacimiento"],
                "direccion_residencia": request.data["direccion_residencia"],
                "numero_celular": request.data["numero_celular"],
                "correo_electronico": request.data["correo_electronico"],
                "fecha_creacion_persona": request.data["fecha_creacion_persona"],
                "fecha_modificacion_persona": request.data["fecha_modificacion_persona"]
            }
            
            persona_serealizer = PersonaSerializer(data = rol_data)
            
            if persona_serealizer.is_valid():
                persona_serealizer.save()
                return Response(persona_serealizer.data, status = status.HTTP_201_CREATED)
            return  Response(persona_serealizer.errors, status = status.HTTP_400_BAD_REQUEST)
        return  Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Metodo GET
    def get(self, request, format = None):
        try:
            # Obtención de la lista de las personas
            personas = Persona.objects.all()
            serializer = PersonaSerializer(personas, many = True)
            # Creación de la lista de diccionarios con las claves y valores
            personas_data = []
            for data_dict in serializer.data:
                persona_info = {f"{key}": value for key, value in data_dict.items()}
                user = User.objects.get(id = persona_info['user'])
                rol = Rol.objects.get(id = persona_info['rol'])
                personas_data.append({
                    'id': persona_info['id'],
                    'UsernameLogin': user.username,
                    'Numero_identificacion': persona_info['numero_identificacion'],
                    'Direccion_residencia': persona_info['direccion_residencia'],
                    'Rol': rol.nombre_rol,
                    'Numero_celular': persona_info['numero_celular'],
                    'Correo_electronico': persona_info['correo_electronico']
                })
            return Response(personas_data)
        except Exception as e:
            return Response({"Error": str(e)}, status = status.HTTP_400_BAD_REQUEST)

    #Metodo PUT
    def put(self, request, pk, format =None):
        try:
            persona = Persona.objects.get(pk=pk)
            serializer = PersonaSerializer(persona, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Persona.DoesNotExist:
            return Response({"Error": "La persona no existe"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Metodo DELETE    
    def delete(self, request, pk, format = None):
        try:
            persona = Persona.objects.get(pk=pk)
            persona.delete()
            return Response({"msg": "Persona eliminada correctamente"})
        except Persona.DoesNotExist:
            return Response({"error": "La persona no existe"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
