from django.urls import path
from .views import PedidosMethods

urlpatterns = [
    path('crear/pedidos', PedidosMethods.pedidosCrear, name='pedidosCrear'),
    path('listar/ByUsuario/', PedidosMethods.listarPedidosByUsuario, name='listarPedidosByUsuario'),
    path('listar/ByRestaurante/', PedidosMethods.PedidosByRestaurante, name='PedidosByRestaurante'),
    path('actualizar/estado/pedido/', PedidosMethods.actualizarEstadoPedido, name='actualizarEstadoPedido'),
    path('listar/todos/', PedidosMethods.listarPedidos_All, name='listarPedidos_All'),
    path('informacion/pedido/', PedidosMethods.InformacionByPedidoID, name='informacion del pedido'),
]