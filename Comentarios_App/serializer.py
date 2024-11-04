from .models import ComentariosRestaurantes, ComentariosMenus
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


'''Comentarios de los menus'''
class ComentariosMenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentariosMenus
        fields = ['id','menu', 'usuario', 'comentario', 'fecha', 'puntaje']

class ComentariosMenusToolsSerializer(serializers.ModelSerializer):
    usuario = UsuariosSerializerTools()
    class Meta:
        model = ComentariosMenus
        fields = ['id','menu', 'usuario', 'comentario', 'fecha', 'puntaje']