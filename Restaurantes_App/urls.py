from django.urls import path
from .views import RestaurantesMethods
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('listar/', RestaurantesMethods.restaurantesListar, name='restaurantesListar'),
    path('eliminar/', RestaurantesMethods.restaurantesEliminar, name='restaurantesEliminar'),
    path('crear/', RestaurantesMethods.restaurantesCrear, name='restaurantesCrear'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)