from rest_framework.response import Response
from rest_framework.views import APIView
from AppUsuarios.models import Rol
from AppUsuarios.serializers import RolSerializer

class RolAPIView(APIView):

    def get(self, request):
        rols = Rol.objects.all()
        rols_serializer = RolSerializer(rols, many = True)
        return Response(rols_serializer.data)