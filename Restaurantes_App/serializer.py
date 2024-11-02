from .models import Restaurantes, MenuRestaurantes
from rest_framework import serializers

class RestaurantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurantes
        fields = '__all__'

    def create(self, validated_data):
        return Restaurantes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.ubicacion = validated_data.get('ubicacion', instance.ubicacion)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.tipoCocina = validated_data.get('tipoCocina', instance.tipoCocina)
        instance.puntaje = validated_data.get('puntaje', instance.puntaje)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.save()
        return instance

class MenuRestaurantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuRestaurantes
        fields = '__all__'

    def create(self, validated_data):
        return MenuRestaurantes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.status = validated_data.get('status', instance.status)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.save()
        return instance

class restaurantesToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurantes
        fields = ['id', 'nombre']
class MenuToolsSerializer(serializers.ModelSerializer):
    restaurante = restaurantesToolsSerializer()
    class Meta:
        model = MenuRestaurantes
        fields = ['id', 'restaurante', 'titulo', 'nombre', 'precio', 'fecha', 'status', 'imagen', 'descripcion', 'puntaje']