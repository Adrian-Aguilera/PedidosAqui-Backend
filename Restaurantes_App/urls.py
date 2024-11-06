from django.urls import path
from .views import RestaurantesMethods
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('listar/', RestaurantesMethods.restaurantesListar, name='restaurantesListar'),
    path('crear/', RestaurantesMethods.restaurantesCrear, name='restaurantesCrear'),
    path('listar/menu/todos/', RestaurantesMethods.MenusRestaurantesListar, name='MenuRestaurantesListar'),
    path('crear/menu/', RestaurantesMethods.CrearMenuRestaurantes, name='CrearMenuRestaurantes'),
    path('editar/menu/', RestaurantesMethods.editarMenu, name='EditarMenu'),
    path('datos/menu/', RestaurantesMethods.InformacionMenu, name='retornar informacion del menu'),
    path('listar/restaurante/menu/todos/', RestaurantesMethods.MenusByRestaurante, name='lista todos los menus de un restaurante'),
    path('eliminar/restaurante/menu/', RestaurantesMethods.eliminarMenu, name='eliminarMenu'),
    path('listar/restaurantes/usuarioRestaurante/', RestaurantesMethods.ListarRestaurantesByUsuarioRestaurante, name='ListarRestaurantesByUsuarioRestaurante'),
    path('editar/restaurante/', RestaurantesMethods.RestaurantesEditar, name='RestaurantesEditar'),
    path('eliminar/restaurante/', RestaurantesMethods.restaurantesEliminar, name='restaurantesEliminar'),
    path('informacion/restaurante/', RestaurantesMethods.informacionRestaurante, name='informacionRestaurante le pasa el id del restaurante'),

    path('buscar/restaurante/', RestaurantesMethods.buscarRestaurante, name='buscarRestaurante'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)