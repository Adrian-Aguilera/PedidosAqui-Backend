from django.urls import path
from .views import PedidosMethods

urlpatterns = [
    path('crear/pedidos', PedidosMethods.pedidosCrear, name='pedidosCrear'),
    path('listar/ByUsuario/', PedidosMethods.listarPedidosByUsuario, name='listarPedidosByUsuario'),
]