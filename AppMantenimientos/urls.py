from django.urls import path
from AppMantenimientos.views import *

urlpatterns = [
    path('api/CrearActividad',AppMantenimientos_API_CrearActividad.as_view(), name='CrearActividad'),
    path('api/CrearMantenimiento',AppMantenimientos_API_CrearMantenimiento.as_view(), name='CrearMantenimiento'),
    
]