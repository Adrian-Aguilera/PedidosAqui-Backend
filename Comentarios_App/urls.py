from django.urls import path
from .views import ComentariosRestaurantesView, ComentariosMenusView

urlpatterns = [
    path('comentarios/restautante-crear/', ComentariosRestaurantesView.ComentariosRestaurantesCrear, name='comentarios-restaurantes-crear'),
    path('comentarios/restautante-listar/<int:id>', ComentariosRestaurantesView.ComentariosRestaurantesListar, name='comentarios-restaurantes-listar'),
    path('comentarios/restautante-listar/', ComentariosRestaurantesView.ComentariosRestaurantesListar, name='comentarios-restaurantes-listar'),

    path('comentarios/menu-crear/', ComentariosMenusView.ComentariosMenusCrear, name='comentarios-menu-crear'),
    path('comentarios/menu-listar/<int:id>', ComentariosMenusView.ComentariosMenusListar, name='comentarios-menu-listar'),
]