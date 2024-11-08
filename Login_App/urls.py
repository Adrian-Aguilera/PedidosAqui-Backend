from django.urls import path
from .views import LoginMethod, ClienteTokenObtainPairView

urlpatterns = [
    path('login/', LoginMethod.login, name='login'),
    path('create/', LoginMethod.CreateCuenta, name='create'),
    path('perfil/informacion/', LoginMethod.perfil, name='perfil'),
    path('perfil/editar/', LoginMethod.EditarUsuario, name='EditarUsuario'),
    path('listar/', LoginMethod.listarUsuarios, name='listarUsuarios'),

    path('cliente/tokens/', ClienteTokenObtainPairView.as_view(), name='cliente-token-obtain-pair'),
]