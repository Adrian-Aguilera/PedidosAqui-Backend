from django.urls import path
from .views import ComentariosRestaurantesView

urlpatterns = [
    path('comentarios/restautante-crear/', ComentariosRestaurantesView.ComentariosRestaurantesCrear, name='comentarios-restaurantes-crear'),
    path('comentarios/restautante-listar/<int:id>/', ComentariosRestaurantesView.ComentariosRestaurantesListar, name='comentarios-restaurantes-listar'),
]