from django.contrib.auth.backends import BaseBackend
from .models import Usuarios

class UsuariosBackend(BaseBackend):
    def authenticate(self, request, correo=None, password=None):
        try:
            user = Usuarios.objects.get(correo=correo)
        except Usuarios.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Usuarios.objects.get(pk=user_id)
        except Usuarios.DoesNotExist:
            return None