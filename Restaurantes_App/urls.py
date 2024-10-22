from django.urls import path
from .views import RestaurantesMethods
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('listar/', RestaurantesMethods.restaurantesListar, name='restaurantesListar'),
    path('eliminar/', RestaurantesMethods.restaurantesEliminar, name='restaurantesEliminar'),
    path('crear/', RestaurantesMethods.restaurantesCrear, name='restaurantesCrear'),
    path('listar/menu/todos/', RestaurantesMethods.MenusRestaurantesListar, name='MenuRestaurantesListar'),
    path('crear/menu/', RestaurantesMethods.CrearMenuRestaurantes, name='CrearMenuRestaurantes'),
    path('editar/menu/estado/', RestaurantesMethods.editarMenu, name='editarMenuEstado se le tiene que mandar el id del menu y el nuevo estado'),
    path('listar/restaurantes/usuarioRestaurante/', RestaurantesMethods.ListarRestaurantesByUsuarioRestaurante, name='ListarRestaurantesByUsuarioRestaurante'),
    path('editar/restaurante/', RestaurantesMethods.RestaurantesEditar, name='RestaurantesEditar')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)