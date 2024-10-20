from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializer import PedidosSerializer
from .models import Pedidos
from Pedidos_App.models import Restaurantes
import json
# Create your views here.


class PedidosMethods(APIView):
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