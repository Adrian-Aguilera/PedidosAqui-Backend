from rest_framework import serializers
from .models import Usuarios
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

'''Crear serializers para los usuarios'''
class UsuariosSerializerAutenticado(TokenObtainPairSerializer):
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
                        'idUsuario': usuarioLogeado.id,
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

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'correo', 'apellido', 'password']

    def create(self, validated_data):
        password = validated_data.get('password')
        instancia = Usuarios(**validated_data)
        instancia.set_password(password)
        instancia.save()
        return instancia