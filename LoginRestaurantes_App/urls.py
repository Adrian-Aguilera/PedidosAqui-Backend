from django.urls import path
from .views import RestaurantesLoginMethod, RestaurantesTokenObtainPairView

urlpatterns = [
    path('login/', RestaurantesLoginMethod.login, name='login'),
    path('crear/', RestaurantesLoginMethod.CreateCuenta, name='create'),
    path('perfil/informacion/', RestaurantesLoginMethod.loadperfil, name='perfil'),
    path('perfil/editar/', RestaurantesLoginMethod.EditarUsuario, name='EditarUsuario'),
    path('listar/restaurantes/usuarios/', RestaurantesLoginMethod.listarUsuarios, name='listarUsuarios'),
    
    path('restaurantes/tokens/', RestaurantesTokenObtainPairView.as_view(), name='restaurantes-token-obtain-pair'),
]