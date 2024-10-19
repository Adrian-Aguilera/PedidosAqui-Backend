from .models import Restaurantes, Pedidos
from rest_framework import serializers

class RestaurantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurantes
        fields = '__all__'

class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = ['restaurante', 'pedido', 'precio', 'fecha', 'status', 'ubicacionEntrega']