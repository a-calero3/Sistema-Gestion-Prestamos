from rest_framework import serializers
from django.contrib.auth.models import User
from parametros.models import Parametro
from usuarios.models import PerfilUsuario

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    rol_id = serializers.PrimaryKeyRelatedField( #este campo espera un ID de otra tabla
        queryset = Parametro.objects.filter(nombre_tabla = 'TIPROL'), # va a la tabla parametro pero filtra por TIPROL
        write_only =True #No aparece en las respuestas pero si se espera para el registro
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'rol_id') #campos que se reciben en el json
        extra_kwargs = {
            'password': {'write_only': True} # la contraseña no se muestra ald evolver la respuesta
        }
    
    def create(self, validated_data):
        # Extraemos el rol del json y lo quitamos para no pasar a User (no tiene este campo)
        rol_id = validated_data.pop('rol_id')

        #Creamos el usuario usando el método adecuado para encriptar la contraseña
        user = User.objects.create(**validated_data)

        #Creamos el perfil usuario asociado a ese usuario
        PerfilUsuario.objects.create(usuario = user, rol_id = rol_id)

        return user # retornamos el usuario

