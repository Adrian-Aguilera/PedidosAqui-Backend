from Restaurantes_App.models import Restaurantes, MenuRestaurantes
from Restaurantes_App.serializer import RestaurantesSerializer, MenuRestaurantesSerializer
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