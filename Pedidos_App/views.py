from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializer import PedidosSerializer
from .models import Pedidos
from Pedidos_App.models import Restaurantes
import json
from Controller import PedidosController


class PedidosMethods(APIView):
    #json que se manda al crear un pedido
    '''
    {
        "restaurante": 1,
        "cliente": 1,
        "menu": [1, 2, 3],
        "tiempoEstimado": "2022-01-01T00:00:00",
        "status": "pendiente",
        "ubicacionEntrega": "entrega"
    }
    '''
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def pedidosCrear(request):
        '''para crear un pedido se le tiene que mandar un lista con los ids de los menús'''
        if request.method == 'POST':
            data = json.loads(request.body)
            try:
                serializer = PedidosSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({'data': {
                        "restaurante": serializer.data['restaurante'],
                        "cliente": serializer.data['cliente'],
                        "menu": serializer.data['menu'],
                        "tiempoEstimado": serializer.data['tiempoEstimado'],
                        "status": serializer.data['status'],
                        "ubicacionEntrega": serializer.data['ubicacionEntrega'],
                    }})
                else:
                    return JsonResponse({'error': 'Error al crear el pedido'})
            except Exception as e:
                return JsonResponse({'error': {
                    "mensaje": f'{str(e)}',
                }})
        else:
            return JsonResponse({'error': 'Method not allowed'})

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def listarPedidosByUsuario(request):
        '''para listar todos los pedidos de un usuario se le tiene que mandar el id del usuario'''
        if request.method == 'POST':
            data = json.loads(request.body)
            try:
                pedidos = PedidosController().listarPedidosByUsuario(data['idUsuario'])
                serializer = PedidosSerializer(pedidos, many=True)
                return JsonResponse({'data': serializer.data})
            except Exception as e:
                return JsonResponse({'error': f'List pedidos error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})