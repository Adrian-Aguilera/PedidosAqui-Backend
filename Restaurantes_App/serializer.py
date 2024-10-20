from .models import Restaurantes
from rest_framework import serializers

class RestaurantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurantes
        fields = '__all__'
