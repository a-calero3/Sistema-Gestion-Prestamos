from rest_framework_simplejwt.authentication import JWTAuthentication
import logging

logger = logging.getLogger(__name__)

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Buscar el token de acceso dentro de la cookie
        token =  request.COOKIES.get('access')

        if token is None:
            logger.debug("No se encontró el token 'access' en la Cookie")
            return None

        try:
            # Validar el Token
            validated_token = self.get_validated_token(token)
            user = self.get_user(validated_token)
            logger.debug(f"Token validado para el usuario {user}")
            return user, validated_token
        except Exception as e:
            logger.debug(f"Error validando el Token: {e}")
        return 