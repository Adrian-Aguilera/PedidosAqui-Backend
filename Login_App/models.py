from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UsuariosManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError('El correo debe ser proporcionado')
        if not extra_fields.get('nombre'):
            raise ValueError('El nombre debe ser proporcionado')
        if not extra_fields.get('apellido'):
            raise ValueError('El apellido debe ser proporcionado')

        correo = self.normalize_email(correo)
        user = self.model(correo=correo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(correo, password, **extra_fields)

class Usuarios(AbstractBaseUser):
    nombre = models.CharField(max_length=255, help_text='Nombre del usuario')
    correo = models.EmailField(max_length=255, unique=True, help_text='Correo electrónico del usuario')
    apellido = models.CharField(max_length=255, help_text='Apellido del usuario')
    password = models.CharField(max_length=255, help_text='Contraseña del usuario')
    #propiedades heredadas de django
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = []

    objects = UsuariosManager()

    def __str__(self):
        return self.correo
