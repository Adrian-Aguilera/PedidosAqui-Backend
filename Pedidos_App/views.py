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
        if request.method == 'POST':
            data = json.loads(request.body)
            try:
                #obtener el id del restaurante par asignar al pedido
                restaurante = Restaurantes.objects.get(id=data['restaurante'])
                serializer = PedidosSerializer(data=data)
            except Exception as e:
                return JsonResponse({'error': {
                    "mensaje": f'{str(e)}',
                }})
        else:
            return JsonResponse({'error': 'Method not allowed'})