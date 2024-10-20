from .models import Restaurantes, Pedidos, MenuRestaurantes
from rest_framework import serializers

class MenuFormaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuRestaurantes
        fields = ['id', 'titulo', 'nombre']

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
    class Meta:
        model = Pedidos
        fields = ['restaurante', 'cliente', 'menus', 'tiempoEstimado', 'status', 'ubicacionEntrega']