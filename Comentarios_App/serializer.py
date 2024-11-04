from .models import ComentariosRestaurantes
from rest_framework import serializers
from Login_App.serializer import UsuariosSerializerTools
from Restaurantes_App.models import Restaurantes, MenuRestaurantes

class ComentariosRestaurantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentariosRestaurantes
        fields = ['id','restaurante', 'usuario', 'comentario', 'fecha', 'puntaje']

class ComentariosRestaurantesToolsSerializer(serializers.ModelSerializer):
    usuario = UsuariosSerializerTools()
    class Meta:
        model = ComentariosRestaurantes
        fields = ['id','restaurante', 'usuario', 'comentario', 'fecha', 'puntaje']