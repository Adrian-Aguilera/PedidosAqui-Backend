from Pedidos_App.models import Pedidos
from Login_App.models import Usuarios
from Restaurantes_App.models import Restaurantes, MenuRestaurantes
from Pedidos_App.serializer import PedidosToolsSerializer

class PedidosController:
    def __init__(self):
        self.pedidos = Pedidos.objects.all()

    def PedidosByUsuario(self, usuario):
        '''para listar todos los pedidos de un usuario se le tiene que mandar el id del usuario'''
        try:
            try:
                usuario = Usuarios.objects.get(id=usuario)
                pedidos = self.pedidos.filter(cliente=usuario)
                #pasar por el serializer y devolver los pedidos
                serializer = PedidosToolsSerializer(pedidos, many=True)
                return serializer.data
            except Exception as e:
                return {'error': {
                    "mensaje": f'{str(e)}',
                }}
        except Exception as e:
            return f'Error: {str(e)}'

    def PedidosByRestaurante(self, restaurante):
        '''para listar todos los pedidos de un restaurante se le tiene que mandar el id del restaurante'''
        try:
            try:
                restaurante = Restaurantes.objects.get(id=restaurante)
                pedidos = self.pedidos.filter(restaurante=restaurante)
                #pasar por el serializer y devolver los pedidos
                serializer = PedidosToolsSerializer(pedidos, many=True)
                return serializer.data
            except Exception as e:
                return {'error': {
                    "mensaje": f'{str(e)}',
                }}
        except Exception as e:
            return f'Error: {str(e)}'

    def actualizarEstadoPedido(self, data):
        '''
            Para actualizar el estado de un pedido se le tiene que mandar el id del pedido y el nuevo estado
            Usando el serializer se crea el menú y se lo guarda en la base de datos
        '''
        try:
            #buscar el menú en la base de datos (la instancia)
            pedido = Pedidos.objects.get(id=data.get('pedidoID'))
            #usando el serializer se actualiza el menú
            serializerPedido = PedidosToolsSerializer(pedido, data=data, partial=True)
            if serializerPedido.is_valid():
                serializerPedido.save()
                return {'done': serializerPedido.data}
            else:
                return {'errorSerializer': serializerPedido.errors}
        except Exception as e:
            return f'Error: {str(e)}'

    def listarPedidos_All(self):
        '''Para listar todos los menús que se han creado'''
        try:
            serializer = PedidosToolsSerializer(self.pedidos, many=True)
            pedidos = serializer.data
            return pedidos
        except Exception as e:
            return f'Error: {str(e)}'

    def InformacionByPedidoID(self, data):
        '''Para obtener la informacion de un pedido'''
        try:
            pedido = Pedidos.objects.get(id=data.get('pedidoID'))
            serializer = PedidosToolsSerializer(pedido)
            return serializer.data
        except Exception as e:
            return f'Error: {str(e)}'

    def EliminarPedidoByRestaurante(self, data):
        '''Eliminar un pedido'''
        try:
            pedido = Pedidos.objects.get(id=data.get('pedidoID'))
            serializer = PedidosToolsSerializer(pedido)
            try:
                pedido.delete()
                return serializer.data
            except Exception as e:
                return {'error': serializer.errors}
        except Exception as e:
            return f'Error: {str(e)}'

    def EliminarPedidoByCliente(self, pedidoID):
        '''Eliminar un pedido'''
        try:
            pedido = Pedidos.objects.get(id=pedidoID)
            serializer = PedidosToolsSerializer(pedido)
            try:
                pedido.delete()
                return serializer.data
            except Exception as e:
                return {'error': serializer.errors}
            except Exception as e:
                return f'Error: {str(e)}'
        except Exception as e:
                return f'Error: {str(e)}'