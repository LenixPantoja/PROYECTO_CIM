""" Librerias """
from django.urls import path
from AppResponsables.views import *

# Definir las URL para las vistas de la aplicación AppResponsables
urlpatterns = [
    path('api/CrearResponsable',AppResponsables_API_CrearResponsable.as_view(), name='CrearResponsable'),
]