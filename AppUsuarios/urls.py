from django.urls import path
from AppUsuarios.api import RolAPIView

urlpatterns = [
    path('rol/', RolAPIView.as_view(), name = 'rol_api'),
]