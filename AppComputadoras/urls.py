from django.urls import path
from AppComputadoras.views import *

urlpatterns = [
    path('api/CrearMouse',AppComputers_API_CrearMouse.as_view(), name='CrearMouse')
]