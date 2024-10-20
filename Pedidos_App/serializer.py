from .models import Restaurantes, Pedidos, MenuRestaurantes
from rest_framework import serializers

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

class PedidosToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = ['restaurante', 'cliente', 'menus', 'tiempoEstimado', 'status', 'ubicacionEntrega']