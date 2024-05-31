""" Librerias """
from django.urls import path
from .views import *
from AppUsuarios import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

# Definición de las URL para las vistas basadas en API 
urlpatterns = [
    #path('rol/', RolAPIView.as_view(), name = 'rol_api'),

    # Crear token 
    #path('post/create/', views.create_post, name = 'creando-post'),

    # Api generadora del token
    path('api/Login/', TokenObtainPairView.as_view(), name = 'loginTkn'),
    
    # Api actualizador del token creado
    path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token-refresh'),

    # Url's para obtener
    path('api/getUser/', AppUser_loginApiView.as_view(), name = 'get-User'),

    path('api/Persona/', AppUser_Persona_ApiView.as_view(), name = 'Api-Persona'),

    path('api/Persona/<int:pk>/', AppUser_Persona_ApiView.as_view(), name='Api-Persona_Encontrada')
]