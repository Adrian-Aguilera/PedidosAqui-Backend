from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from dotenv import load_dotenv
from asgiref.sync import sync_to_async, async_to_sync
import json
from .serializer import RestaurantesSerializer, MenuRestaurantesSerializer
from .models import Restaurantes, MenuRestaurantes
from Controller.RestaurantesController import MenusController, RestaurantesController
load_dotenv(override=True)
# Create your views here.

class RestaurantesMethods(APIView):
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def restaurantesCrear(request):
        if request.method == 'POST':
            data = request.data
            try:
                serializer = RestaurantesSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'data':{
                        "nombre": serializer.data['nombre'],
                        "ubicacion": serializer.data['ubicacion'],
                        "descripcion": serializer.data['descripcion'],
                        "telefono": serializer.data['telefono'],
                        "tipoCocina": serializer.data['tipoCocina'],
                        "puntaje": serializer.data['puntaje'],
                        "imagen": serializer.data['imagen']
                    }})
                else:
                    return JsonResponse({'error': 'Error al crear el restaurante'})
            except Exception as e:
                return JsonResponse({'error': f'Create restaurant error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def restaurantesEliminar(request):
        ''' Eliminar un restaurante '''
        if request.method == 'POST':
            data = request.data
            print(data)
            try:
                restaurante = Restaurantes.objects.get(id=data['restauranteID'])
                restaurante.delete()
                return JsonResponse({'data': {
                    "mensaje": "Restaurante eliminado exitosamente",
                    "nombre": restaurante.nombre,
                }})
            except Exception as e:
                return JsonResponse({'error': {
                    "mensaje": f'{str(e)}',
                }})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def restaurantesListar(request):
        if request.method == 'GET':
            try:
                restaurantes = Restaurantes.objects.all()
                for restaurante in restaurantes:
                    if restaurante.imagen == None:
                        restaurante.imagen = None
                    else:
                        restaurante.imagen = f'/restaurantesMethods/api{restaurante.imagen}'
                serializer = RestaurantesSerializer(restaurantes, many=True)
                return JsonResponse({'data': serializer.data})
            except Exception as e:
                return JsonResponse({'error': f'List restaurants error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def MenusRestaurantesListar(request):
        ''' Listar los menus de todos los restaurantes '''
        if request.method == 'GET':
            try:
                controller = MenusController()
                menus = controller.listarMenus_All()
                return JsonResponse({'data': menus})
            except Exception as e:
                return JsonResponse({'error': f'List menu restaurants error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def MenusByRestaurante(request):
        if request.method == 'POST':
            ''' Listar los menus de un restaurante '''
            try:
                controller = MenusController()
                data = request.data
                menus = controller.MenusByRestaurante(data)
                #tomar el campo imagen y concatenarle restaurantesMethods/api/
                for menu in menus:
                    if menu['imagen'] == None:
                        menu['imagen'] = None
                    else:
                        menu['imagen'] = f'/restaurantesMethods/api{menu["imagen"]}'
                return JsonResponse({'data': menus})
            except Exception as e:
                return JsonResponse({'error': f'List menu restaurants error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def InformacionMenu(request):
        ''' Informacion del menu '''
        if request.method == 'POST':
            try:
                '''tomar el id de la url'''
                controller = MenusController()
                data = request.data
                menuID = data.get('menuID')
                menuFuncion = controller.InformacionByMenuID(menuID)
                return JsonResponse({'data': menuFuncion})
            except Exception as e:
                return JsonResponse({'error': f'Informacion menu restaurants error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def eliminarMenu(request):
        if request.method == 'POST':
            ''' Eliminar un menu de un restaurante '''
            try:
                controller = MenusController()
                data = request.data
                menuFuncion = controller.eliminarMenu(data)
                return JsonResponse({'data': menuFuncion})
            except Exception as e:
                return JsonResponse({'error': f'Eliminar menu restaurants error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def CrearMenuRestaurantes(request):
        '''Para este menu se le tiene que mandar como formato "form-data"'''
        if request.method == 'POST':
            try:
                controller = MenusController()
                data = request.data
                menuFuncion = controller.crearMenu(data)
                return JsonResponse({'data': menuFuncion})
            except Exception as e:
                return JsonResponse({'error': f'Create menu restaurants error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def editarMenu(request):
        '''Editar el estado del menu de un restaurante se le tiene que mandar el id del menu y el nuevo estado'''
        if request.method == 'POST':
            try:
                controller = MenusController()
                data = request.data
                menuFuncion = controller.editarMenuByRestaurante(data)
                return JsonResponse({'data': menuFuncion})
            except Exception as e:
                return JsonResponse({'error': f'Editar menu restaurants error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def ListarRestaurantesByUsuarioRestaurante(request):
        if request.method == 'POST':
            try:
                data = request.data
                print(data)
                controller = RestaurantesController()
                restaurantes = controller.RestaurantesByUsuario(data)
                return JsonResponse({'data': restaurantes})
            except Exception as e:
                return JsonResponse({'error': f'List restaurants by user error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def RestaurantesEditar(request):
        if request.method == 'POST':
            try:
                data = request.data
                controller = RestaurantesController()
                restaurantes = controller.EditarRestaurante(data)
                return JsonResponse({'data': restaurantes})
            except Exception as e:
                return JsonResponse({'error': f'Edit restaurants error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})
