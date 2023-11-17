""" Librerias """
from django.urls import path
from AppUsuarios.api import RolAPIView

# Definición de las URL para las vistas basadas en API 
urlpatterns = [
    path('rol/', RolAPIView.as_view(), name = 'rol_api'),
]