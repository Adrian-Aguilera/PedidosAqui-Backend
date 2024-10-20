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
class UsuariosRestaurantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantesUsuarios
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.get('password')
        instancia = RestaurantesUsuarios(**validated_data)
        instancia.set_password(password)
        instancia.save()
        return instancia

class UsuariosRestaurantesSerializerInList(serializers.ModelSerializer):
    '''Solo los campos que se quieren mostrar en la lista'''
    class Meta:
        model = RestaurantesUsuarios
        fields = ['id', 'nombre', 'correo']

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.correo = validated_data.get('correo', instance.correo)
        password = validated_data.get('password', None)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance