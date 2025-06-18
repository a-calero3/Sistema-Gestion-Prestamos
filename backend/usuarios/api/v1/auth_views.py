from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

class LoginView(APIView):
    permission_classes = [AllowAny]  # Permite acceso público sin token para el login

    def post(self, request):

        # Obtener credenciales enviadas del front
        username = request.data.get('username')
        password = request.data.get('password')

        # Verificar que exista el usuario
        user = authenticate(username = username, password = password)

        if user:
            # Generar el token JWT (acces + refresh)
            refresh = RefreshToken.for_user(user)

            # Creando la respuesta
            response = Response({'message': 'Login exitoso'}, status=status.HTTP_200_OK)

            # Guardar el token de acceso en una cookie (HTTPOnly)
            response.set_cookie(
                key='access',
                value=str(refresh.access_token),
                httponly=True, # impide el acceso por JS (proteccion XSS)
                secure=False, # Si se usa htpps deberia cambiar a  True
                samesite='Lax' # Evita que se haga peticiones desde otro dominio
            )

            # Guardar el refresh token
            response.set_cookie(
                key='refresh',
                value=str(refresh),
                httponly=True,
                secure=False,
                samesite='Lax',
            )

            return response
        
        else:
            # Si las credenciales son invalidas
            return Response({'error': 'Credenciales invalidas'}, status=status.HTTP_401_UNAUTHORIZED)
