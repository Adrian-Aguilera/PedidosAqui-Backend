from .models import Restaurantes, MenuRestaurantes
from rest_framework import serializers

class RestaurantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurantes
        fields = '__all__'

class MenuRestaurantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuRestaurantes
        fields = '__all__'