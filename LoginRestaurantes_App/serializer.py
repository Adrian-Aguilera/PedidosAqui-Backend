from rest_framework import serializers
from .models import RestaurantesUsuarios
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate


class UsuariosRestaurantesSerializerAutenticado(TokenObtainPairSerializer):
    correo = serializers.CharField(required=True)

    def validate(self, attrs):
        correo = attrs.get('correo')
        password = attrs.get('password')

        if correo and password:
            try:
                usuarioLogeado = authenticate(request=None, correo=correo, password=password)
                if usuarioLogeado is not None:
                    nuevoToken = self.get_token(usuarioLogeado)
                    '''Retonar los tokens'''
                    return {
                        'refresh': str(nuevoToken),
                        'access': str(nuevoToken.access_token),
                        'correo': usuarioLogeado.correo,
                        'restauranteID': usuarioLogeado.id,
                        'nombre': usuarioLogeado.nombre,
                    }
                else:
                    print("no usuario")
                    raise serializers.ValidationError(
                        {'detail': 'No active account found with the given credentials'}
                    )
            except Exception as e:
                raise serializers.ValidationError(f'Error: {str(e)}')
        else:
            raise serializers.ValidationError('Falta campo correo o password')