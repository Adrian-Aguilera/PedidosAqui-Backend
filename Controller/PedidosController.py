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