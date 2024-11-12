from Restaurantes_App.models import Restaurantes, MenuRestaurantes
from Restaurantes_App.serializer import RestaurantesSerializer, MenuRestaurantesSerializer, MenuToolsSerializer
from Pedidos_App.models import Pedidos
from LoginRestaurantes_App.models import RestaurantesUsuarios
from django.db.models import Q
class MenusController:
    def __init__(self):
        self.restaurantes = Restaurantes.objects.all()
        self.menuRestaurantes = MenuRestaurantes.objects.all()

    def listarMenus_All(self):
        '''Para listar todos los menús que se han creado'''
        try:
            serializer = MenuRestaurantesSerializer(self.menuRestaurantes, many=True)
            menus = serializer.data
            return menus
        except Exception as e:
            return f'Error: {str(e)}'

    def crearMenu(self, data):
        '''
            Para crear un menú se le tiene que mandar el id del restaurante que viene en data
            Usando el serializer se crea el menú y se lo guarda en la base de datos
        '''
        try:
            serializerMenu = MenuRestaurantesSerializer(data=data)
            if serializerMenu.is_valid():
                serializerMenu.save()
                return serializerMenu.data
            else:
                return {'errorSerializer': {
                    "mensaje": f'{str(serializerMenu.errors)}',
                }}
        except Exception as e:
            return f'Error: {str(e)}'

    def editarMenuByRestaurante(self, data):
        '''Editar El menu por el restaurante'''
        try:
            #buscar el menú en la base de datos (la instancia)
            menu = MenuRestaurantes.objects.get(id=data['menuID'])
            #usando el serializer se actualiza el menú
            serializerMenu = MenuRestaurantesSerializer(menu, data=data, partial=True)
            if serializerMenu.is_valid():
                serializerMenu.save()
                return serializerMenu.data
            else:
                return {'errorSerializer': {
                    "mensaje": f'{str(serializerMenu.errors)}',
                }}
        except Exception as e:
            return f'Error: {str(e)}'

    def MenusByRestaurante(self, data):
        '''
            Para listar los menus de un restaurante se le tiene que mandar el id del restaurante
            Usando el serializer se obtiene la lista de menus.
        '''
        try:
            # Filtrar los menus directamente por el ID del restaurante
            restaurante = Restaurantes.objects.get(id=data.get('restauranteID'))
            menus = self.menuRestaurantes.filter(restaurante_id=restaurante.id)
            # Serializar la lista de menus
            serializer = MenuToolsSerializer(menus, many=True)
            return serializer.data
        except Restaurantes.DoesNotExist:
            return {'error': 'El restaurante con el ID proporcionado no existe'}
        except Exception as e:
            return {'error': f'Error inesperado: {str(e)}'}

    def eliminarMenu(self, data):
        '''
            Para eliminar un menu se le tiene que mandar el id del menu
            Usando el serializer se elimina el menu y se lo guarda en la base de datos
        '''
        try:
            menu = MenuRestaurantes.objects.get(id=data.get('menuID'))
            menu.delete()
            return {'data': {
                "mensaje": "Menu eliminado exitosamente",
                "titulo": menu.titulo,
            }}
        except Exception as e:
            return {'error': {
                "mensaje": f'{str(e)}',
            }}

    def InformacionByMenuID(self, menuID):
        try:
            menu = MenuRestaurantes.objects.get(id=menuID)
            serializer = MenuToolsSerializer(menu, many=False)
            print(serializer.data)
            return serializer.data
        except Exception as e:
            return {'error': {
                "mensaje": f'{str(e)}',
            }}

class RestaurantesController:
    def __init__(self):
        self.restaurantes = Restaurantes.objects.all()
        self.menuRestaurantes = MenuRestaurantes.objects.all()

    def listarRestaurantes_All(self):
        '''Para listar todos los restaurantes que se han creado'''
        try:
            serializer = RestaurantesSerializer(self.restaurantes, many=True)
            restaurantes = serializer.data
            return restaurantes
        except Exception as e:
            return f'Error: {str(e)}'

    def RestaurantesByUsuario(self, data):
        '''
            Para listar los restaurantes que tiene un usuario se le tiene que mandar el id del usuario.
            Usando el serializer se obtiene la lista de restaurantes.
        '''
        try:
            # Filtrar los restaurantes directamente por el ID del usuario
            usuario_restaurante_id = data.get('usuarioRestauranteID')
            if not usuario_restaurante_id:
                return {'error': 'El ID del usuario es requerido'}
            restaurantes_lista = self.restaurantes.filter(usuarioRestaurante__id=usuario_restaurante_id)
            # Serializar la lista de restaurantes
            serializer_restaurantes = RestaurantesSerializer(restaurantes_lista, many=True)
            return serializer_restaurantes.data
        except RestaurantesUsuarios.DoesNotExist:
            return {'error': 'El usuario con el ID proporcionado no existe'}
        except Exception as e:
            return {'error': f'Error inesperado: {str(e)}'}

    def EditarRestaurante(self, data):
        '''
            Para editar un restaurante se le tiene que mandar el id del restaurante y el nuevo nombre
            Usando el serializer se actualiza el restaurante y se lo guarda en la base de datos
        '''
        try:
            restaurante = Restaurantes.objects.get(id=data.get("restauranteID"))
            serializerRestaurante = RestaurantesSerializer(restaurante, data=data, partial=True)
            if serializerRestaurante.is_valid():
                serializerRestaurante.save()
                return serializerRestaurante.data
            else:
                return {'errorSerializer': {
                    "mensaje": f'{str(serializerRestaurante.errors)}',
                }}
        except Exception as e:
            return f'Error: {str(e)}'

    def InformacionRestaurante(self, data):
        try:
            restaurante = Restaurantes.objects.get(id=data['restauranteID'])
            serializerRestaurante = RestaurantesSerializer(restaurante)
            return serializerRestaurante.data
        except Exception as e:
            return f'Error: {str(e)}'

    def buscarRestaurante(self, data):
        try:
            # Mostrar datos recibidos para depuración
            print("Datos recibidos:", data)

            # Construir filtros dinámicos
            filtros = Q()

            if 'nombre' in data and data['nombre']:
                filtros &= Q(nombre__icontains=data['nombre'])
                print("Filtro por nombre:", data['nombre'])
            
            if 'tipoCocina' in data and data['tipoCocina']:
                filtros &= Q(tipoCocina__icontains=data['tipoCocina'])
                print("Filtro por tipo de cocina:", data['tipoCocina'])  # Verificar valor enviado

            if 'ubicacion' in data and data['ubicacion']:
                filtros &= Q(ubicacion__icontains=data['ubicacion'])
                print("Filtro por ubicación:", data['ubicacion'])

            # Realizar la consulta
            restaurantes = Restaurantes.objects.filter(filtros)
            print("Restaurantes encontrados con filtros aplicados:", restaurantes)  # Verificar si devuelve resultados

            # Serializar resultados
            serializerRestaurante = RestaurantesSerializer(restaurantes, many=True)

            if serializerRestaurante.data:
                return {'success': True, 'data': serializerRestaurante.data}
            else:
                return {'success': False, 'data': [], 'error': 'No se encontraron restaurantes con los filtros proporcionados'}
            
        except Exception as e:
            return {'success': False, 'error': f'Error en la búsqueda: {str(e)}'}