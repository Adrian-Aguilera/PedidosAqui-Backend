from django.urls import path
from .views import PedidosMethods

urlpatterns = [
    path('crear/', PedidosMethods.pedidosCrear, name='pedidosCrear'),
    path('listar/ByUsuario/', PedidosMethods.listarPedidosByUsuario, name='listarPedidosByUsuario'),
]