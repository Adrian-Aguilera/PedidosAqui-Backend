from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from dotenv import load_dotenv
from asgiref.sync import sync_to_async, async_to_sync
import json
from .serializer import RestaurantesSerializer
from .models import Restaurantes
load_dotenv(override=True)
# Create your views here.

class RestaurantesMethods(APIView):
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def restaurantesCrear(request):
        if request.method == 'POST':
            data = json.loads(request.body)
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

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def restaurantesListar(request):
        if request.method == 'GET':
            try:
                restaurantes = Restaurantes.objects.all()
                serializer = RestaurantesSerializer(restaurantes, many=True)
                return JsonResponse({'data': serializer.data})
            except Exception as e:
                return JsonResponse({'error': f'List restaurants error: {str(e)}'})
        else:
            return JsonResponse({'error': 'Method not allowed'})
