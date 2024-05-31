""" Librerias """
from django.urls import path
from AppComputadoras.views import *


# Lista de URL para las operaciones de creación de objetos en la API
urlpatterns = [
    path('api/CrearMouse',AppComputers_API_CrearMouse.as_view(), name='CrearMouse'),
    path('api/CrearMouse/<int:pk>/',AppComputers_API_CrearMouse.as_view(), name='Mouse_Encontrado'),
    path('api/CrearTeclado',AppComputers_API_CrearTeclado.as_view(), name='CrearTeclado'),
    path('api/CrearTeclado/<int:pk>/',AppComputers_API_CrearTeclado.as_view(), name='Teclado_Encontrado'),
    path('api/CrearMonitor',AppComputers_API_CrearMonitor.as_view(), name='CrearMonitor'),
    path('api/CrearMonitor/<int:pk>/',AppComputers_API_CrearMonitor.as_view(), name='Monitor_Encontrado'),
    path('api/CrearTorre',AppComputers_API_CrearTorre.as_view(), name='CrearTorre'),
    path('api/CrearTorre/<int:pk>/',AppComputers_API_CrearTorre.as_view(), name='Torre_Encontrada'),
    path('api/CrearCiudad/',AppComputers_API_Ciudad.as_view(), name='CiudadSede'),
    path('api/CrearCiudad/<int:pk>/',AppComputers_API_Ciudad.as_view(), name='Ciudad_Encontrada'),
    path('api/CrearSede',AppComputers_API_CrearSede.as_view(), name='Sede_Encontrada'),
    path('api/CrearSede/<int:pk>/',AppComputers_API_CrearSede.as_view(), name='CrearSede'),
    path('api/CrearArea/',AppComputers_API_CrearArea.as_view(), name='CrearArea'),
    path('api/CrearArea/<int:pk>/',AppComputers_API_CrearArea.as_view(), name='Area_Encontrada'),
    path('api/CrearWorkstation',AppComputers_API_CrearWorkstation.as_view(), name='CrearWorkstation'),
    path('api/CrearWorkstation/<int:pk>/',AppComputers_API_CrearWorkstation.as_view(), name='Workstation_Encontrado'),
    path('api/CrearComputador',AppComputers_API_CrearComputador.as_view(), name='CrearComputador'),
    path('api/CrearComputador/<int:pk>/',AppComputers_API_CrearComputador.as_view(), name='Computador_Encontado'),
    path('api/CrearImpresora',AppComputers_API_CrearImpresora.as_view(), name='CrearImpresora'),
    path('api/CrearImpresora/<int:pk>/',AppComputers_API_CrearImpresora.as_view(), name='Impresora_Encontrada'),
    path('api/CrearAccesorio',AppComputers_API_CrearAccesorio.as_view(), name='CrearAccesorio'),
    path('api/CrearAccesorio/<int:pk>/',AppComputers_API_CrearAccesorio.as_view(), name='Accesorio_Encontrado')
    #path('api/CiudadSede',AppComputers_API_CiudadSede.as_view(), name='CiudadSede'),
]