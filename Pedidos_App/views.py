from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializer import PedidosSerializer
from .models import Pedidos
from Pedidos_App.models import Restaurantes
import json
from Controller.PedidosController import PedidosController
import random
from datetime import timedelta
from django.utils import timezone

class PedidosMethods(APIView):
    #json que se manda al crear un pedido
    '''
    {
        "restaurante": 1,
        "cliente": 1,
        "menu": [1, 2, 3],
        "status": "pendiente",
        "ubicacionEntrega": "entrega"
    }
    '''
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def pedidosCrear(request):
        '''para crear un pedido se le tiene que mandar un lista con los ids de los menús'''
        if request.method == 'POST':
            data = request.data
            try:
                #creaando el tiempo estimado para el pedido
                cantidad_menus = len(data.get('menu', []))
                tiempo_estimado_minutos = random.randint(5, 10) * cantidad_menus
                tiempo_estimado = timezone.now() + timedelta(minutes=tiempo_estimado_minutos)
                data['tiempoEstimado'] = tiempo_estimado
                serializer = PedidosSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'data': {
                        "restaurante": serializer.data['restaurante'],
                        "cliente": serializer.data['cliente'],
                        "menu": serializer.data['menus'],
                        "tiempoEstimado": serializer.data['tiempoEstimado'],
                        "status": serializer.data['status'],
                        "ubicacionEntrega": serializer.data['ubicacionEntrega'],
                    }})
                else:
                    return JsonResponse({'error': {
                        "mensaje": f'{str(serializer.errors)}',
                    }})
            except Exception as e:
                return JsonResponse({'error': {
                    "mensaje": f'{str(e)}',
                }})
        else:
            return JsonResponse({'error': 'Method not allowed'})


    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def listarPedidosByUsuario(request, id=None):
        '''para listar todos los pedidos de un usuario se le tiene que mandar el id del usuario'''
        if request.method == 'GET':
            try:
                controller = PedidosController()
                pedidos = controller.PedidosByUsuario(id)
                return JsonResponse({'data': {
                    "pedidos": pedidos,
                }})
            except Exception as e:
                return JsonResponse({'error': f'List pedidos error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def PedidosByRestaurante(request):
        '''Listar todos los pedidos de un restaurante'''
        if request.method == 'POST':
            data = request.data
            try:
                controller = PedidosController()
                pedidos = controller.PedidosByRestaurante(data.get('restauranteID'))
                return JsonResponse({'data': {
                    "pedidosByRestaurante": pedidos
                }})
            except Exception as e:
                return JsonResponse({'error': f'List pedidos error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def actualizarEstadoPedido(request):
        '''Actualizar el estado de un pedido ESTO SOLO DESDE EL DASHBOARD DE RESTAURANTES'''
        if request.method == 'POST':
            try:
                controller = PedidosController()
                data = request.data
                pedidoFuncion = controller.actualizarEstadoPedido(data)
                return JsonResponse({'data': pedidoFuncion})
            except Exception as e:
                return JsonResponse({'error': f'Actualizar pedido error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def listarPedidos_All(request):
        '''Listar todos los pedidos'''
        if request.method == 'GET':
            try:
                controller = PedidosController()
                pedidos = controller.listarPedidos_All()
                return JsonResponse({'data': {
                    "pedidos": pedidos,
                }})
            except Exception as e:
                return JsonResponse({'error': f'List pedidos error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def InformacionByPedidoID(request):
        '''Para obtener la informacion de un pedido'''
        if request.method == 'POST':
            try:
                controller = PedidosController()
                data = request.data
                InformacionByPedidoID = controller.InformacionByPedidoID(data=data)
                return JsonResponse({'data': InformacionByPedidoID})
            except Exception as e:
                return JsonResponse({'error': f'Informacion pedido error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def eliminarPedido(request):
        '''Eliminar un pedido'''
        if request.method == 'POST':
            try:
                controller = PedidosController()
                data = request.data
                pedidoFuncion = controller.EliminarPedidoByRestaurante(data)
                return JsonResponse({'data': pedidoFuncion})
            except Exception as e:
                return JsonResponse({'error': f'Eliminar pedido error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})