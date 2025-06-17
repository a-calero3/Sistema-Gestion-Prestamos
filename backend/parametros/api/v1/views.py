from rest_framework import generics
from parametros.models import Parametro
from .serializers import ParametroSerializer

class CrearParametroView(generics.CreateAPIView):
    query_set = Parametro.objects.all()
    serializer_class = ParametroSerializer 