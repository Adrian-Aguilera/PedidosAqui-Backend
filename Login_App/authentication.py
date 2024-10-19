from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import AuthenticationFailed
from .models import Usuarios

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        """
        Overrides the default method to fetch a user using your custom Usuarios model.
        """
        try:
            user_id = validated_token.get("user_id")
            if not user_id:
                raise AuthenticationFailed(_("User not found"), code="user_not_found")

            # Aquí obtienes el usuario de tu modelo personalizado
            user = Usuarios.objects.get(pk=user_id)
        except Usuarios.DoesNotExist:
            print("no usuario")
            raise AuthenticationFailed(_("User not found"), code="user_not_found")

        return user
