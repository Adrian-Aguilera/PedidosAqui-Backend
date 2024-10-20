from .models import Restaurantes, Pedidos, MenuRestaurantes
from rest_framework import serializers

class PedidosSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(many=True, queryset=MenuRestaurantes.objects.all())
    class Meta:
        model = Pedidos
        fields = ['restaurante', 'pedido', 'precio', 'fecha', 'status', 'ubicacionEntrega']
    def create(self, validated_data):
        # Extraer los menús del validated_data
        menus = validated_data.pop('menu')
        # Crear el pedido
        pedido = Pedidos.objects.create(**validated_data)
        # Asignar los menús al pedido
        pedido.menuCount.set(menus)
        return pedido

class PedidosToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = ['restaurante', 'cliente', 'menuCount', 'tiempoEstimado', 'status', 'ubicacionEntrega']