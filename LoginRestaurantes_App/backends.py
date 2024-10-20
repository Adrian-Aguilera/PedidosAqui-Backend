from django.contrib.auth.backends import BaseBackend
from .models import RestaurantesUsuarios

class UsuariosRestaurantesBackend(BaseBackend):
    def authenticate(self, request, correo=None, password=None):
        try:
            user = RestaurantesUsuarios.objects.get(correo=correo)
        except RestaurantesUsuarios.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return RestaurantesUsuarios.objects.get(pk=user_id)
        except RestaurantesUsuarios.DoesNotExist:
            return None