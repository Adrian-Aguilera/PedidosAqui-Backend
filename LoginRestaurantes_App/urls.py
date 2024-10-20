from django.urls import path
from .views import RestaurantesLoginMethod

urlpatterns = [
    path('login/', RestaurantesLoginMethod.login, name='login'),
    path('crear/', RestaurantesLoginMethod.CreateCuenta, name='create'),
    path('perfil/informacion/', RestaurantesLoginMethod.perfil, name='perfil'),
    path('perfil/editar/', RestaurantesLoginMethod.EditarUsuario, name='EditarUsuario'),
]