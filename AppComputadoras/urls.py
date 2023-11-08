from django.urls import path
from AppComputadoras.views import *

urlpatterns = [
    path('api/CrearMouse',AppComputers_API_CrearMouse.as_view(), name='CrearMouse'),
    path('api/CrearTeclado',AppComputers_API_CrearTeclado.as_view(), name='CrearTeclado'),
    path('api/CrearMonitor',AppComputers_API_CrearMonitor.as_view(), name='CrearMonitor'),
    path('api/CrearTorre',AppComputers_API_CrearTorre.as_view(), name='CrearTorre'),
    path('api/CiudadSede',AppComputers_API_CiudadSede.as_view(), name='CiudadSede'),
    path('api/CrearArea',AppComputers_API_CrearArea.as_view(), name='CrearArea'),
    path('api/CrearWorkstation',AppComputers_API_CrearWorkstation.as_view(), name='CrearWorkstation'),
    path('api/CrearComputador',AppComputers_API_CrearComputador.as_view(), name='CrearComputador'),
    path('api/CrearImpresora',AppComputers_API_CrearImpresora.as_view(), name='CrearImpresora'),
    path('api/CrearAccesorio',AppComputers_API_CrearAccesorio.as_view(), name='CrearAccesorio'),
]