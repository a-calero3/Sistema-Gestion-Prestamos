from rest_framework import serializers
from parametros.models import Parametro

class ParametroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametro
        fields = ['id', 'nombre_tabla', 'codigo', 'descripcion']