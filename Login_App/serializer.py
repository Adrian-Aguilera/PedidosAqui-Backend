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
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.get('password')
        instancia = Usuarios(**validated_data)
        instancia.set_password(password)
        instancia.save()
        return instancia

class UsuariosSerializerInList(serializers.ModelSerializer):
    '''Solo los campos que se quieren mostrar en la lista'''
    class Meta:
        model = Usuarios
        fields = ['id', 'nombre', 'correo', 'apellido']

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.correo = validated_data.get('correo', instance.correo)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        password = validated_data.get('password', None)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UsuariosSerializerTools(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id', 'nombre']