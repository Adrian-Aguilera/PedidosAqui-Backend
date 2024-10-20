from Pedidos_App.models import Pedidos
from Login_App.models import Usuarios
from Restaurantes_App.models import Restaurantes, MenuRestaurantes


class PedidosController:
    def __init__(self):
        self.pedidos = Pedidos.objects.all()

    def listarPedidosByUsuario(self, usuario):
        '''para listar todos los pedidos de un usuario se le tiene que mandar el id del usuario'''
        try:
            try:
                usuario = Usuarios.objects.get(id=usuario)
                pedidos = Pedidos.objects.filter(cliente=usuario)
                return pedidos
            except Exception as e:
                return {'error': {
                    "mensaje": f'{str(e)}',
                }}
        except Exception as e:
            return f'Error: {str(e)}'