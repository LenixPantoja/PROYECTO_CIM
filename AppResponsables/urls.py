from django.urls import path
from AppResponsables.views import *

urlpatterns = [
    path('api/CrearResponsable',AppResponsables_API_CrearResponsable.as_view(), name='CrearResponsable'),
]