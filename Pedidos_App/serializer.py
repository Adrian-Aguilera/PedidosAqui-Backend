from .models import Restaurantes, Pedidos, MenuRestaurantes
from rest_framework import serializers
from Login_App.models import Usuarios
from Restaurantes_App.serializer import restaurantesToolsSerializer
class MenuFormaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuRestaurantes
        fields = ['id', 'titulo', 'nombre']

class ClienteFormaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id', 'nombre','correo']

class PedidosSerializer(serializers.ModelSerializer):
    menus = serializers.PrimaryKeyRelatedField(many=True, queryset=MenuRestaurantes.objects.all())

    class Meta:
        model = Pedidos
        fields = ['restaurante', 'cliente', 'menus', 'tiempoEstimado', 'status', 'ubicacionEntrega']

    def create(self, validated_data):
        # Extraer los menús del validated_data
        menus = validated_data.pop('menus')
        # Crear el pedido
        pedido = Pedidos.objects.create(**validated_data)
        # Asignar los menús al pedido
        pedido.menus.set(menus)
        return pedido

    def to_representation(self, instance):
        # Llamamos a la representación predeterminada
        representation = super().to_representation(instance)
        # Reemplazamos los menús con su versión expandida (ID y nombre)
        representation['menus'] = MenuFormaterSerializer(instance.menus.all(), many=True).data
        return representation

class PedidosToolsSerializer(serializers.ModelSerializer):
    menus = MenuFormaterSerializer(many=True)
    cliente = ClienteFormaterSerializer()
    restaurante = restaurantesToolsSerializer()
    class Meta:
        model = Pedidos
        fields = ['id','restaurante', 'cliente', 'menus', 'tiempoEstimado', 'status', 'ubicacionEntrega']

    def update(self, instance, validated_data):
        # Actualizar los campos simples
        instance.restaurante = validated_data.get('restaurante', instance.restaurante)
        instance.cliente = validated_data.get('cliente', instance.cliente)
        instance.tiempoEstimado = validated_data.get('tiempoEstimado', instance.tiempoEstimado)
        instance.status = validated_data.get('status', instance.status)  # Campo de texto, se asigna directamente
        instance.ubicacionEntrega = validated_data.get('ubicacionEntrega', instance.ubicacionEntrega)

        # Actualizar la relación ManyToMany usando `set()`
        if 'menus' in validated_data:
            menus = validated_data.get('menus')
            instance.menus.set(menus)  # Usar `set()` para actualizar la relación ManyToMany

        instance.save()
        return instance
