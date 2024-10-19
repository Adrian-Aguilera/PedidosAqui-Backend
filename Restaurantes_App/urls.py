from django.urls import path
from .views import RestaurantesMethods

urlpatterns = [
    path('listar/', RestaurantesMethods.restaurantesListar, name='restaurantesListar'),
]