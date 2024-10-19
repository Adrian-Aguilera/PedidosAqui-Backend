from .models import Restaurantes, Pedidos
from rest_framework import serializers

class RestaurantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurantes
        fields = ['nombre', 'ubicacion', 'descripcion', 'telefono', 'tipoCocina', 'puntaje', 'imagen']

class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = ['restaurante', 'pedido', 'precio', 'fecha', 'status', 'ubicacionEntrega']